"""Score the corpus against config/modules.yaml.

    python3 scripts/score.py [--modules a,b] [--top-n 25]

Reads cached embeddings/TF-IDF/BM25 (built by embed.py) and computes, per
module: BERT semantic similarity + TF-IDF cosine + BM25 ranking, merged by
the weights in config/modules.yaml. Also computes a rule-based quality score
per paper and clusters near-duplicate papers.

Outputs (scores/, committed):
  index.json      machine-readable per-paper x module scores + tiers
  report.md       human-readable ranked report + cull/redundancy sections
  redundancy.json near-duplicate clusters
  validation.md   sanity check of automated scores vs existing annotations

When the topical outline or module set changes: edit config/modules.yaml,
then re-run this script. No re-embedding needed (queries are embedded here).
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import yaml
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

from common import (
    DEFAULT_CACHE,
    DEFAULT_CONFIG,
    DEFAULT_CORPUS,
    DEFAULT_SCORES,
    corpus_paths,
    load_summary,
    parse_frontmatter,
    read_marked,
)

_TOKEN_RE = re.compile(r"[A-Za-z0-9]+")


def _tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower())


# --------------------------------------------------------------------------
# Quality heuristics (rule-based, over _summarized.json + frontmatter)
# --------------------------------------------------------------------------

_SAMPLE_RE = [
    r"\bn\s*=\s*([\d,]+)",
    r"([\d,]+)\s+respondents",
    r"([\d,]+)\s+participants",
    r"([\d,]+)\s+households",
    r"([\d,]+)\s+teachers",
    r"([\d,]+)\s+students",
    r"([\d,]+)\s+workers",
    r"([\d,]+)\s+individuals",
    r"([\d,]+)\s+wage earners",
    r"survey(?:ed)?\s+(?:of\s+)?([\d,]+)",
    r"sample(?:\s+size)?\s+(?:of\s+)?([\d,]+)",
]
_NATIONAL_RE = re.compile(r"\b(FIES|PSA|PIDS|BSP|census|Bangko Sentral|Philippine Statistics)\b", re.IGNORECASE)


def _max_sample(texts: list[str]) -> float:
    best = 0.0
    for text in texts:
        if not text:
            continue
        for pat in _SAMPLE_RE:
            for m in re.finditer(pat, text):
                try:
                    v = int(m.group(1).replace(",", ""))
                    if v < 50_000_000:
                        best = max(best, float(v))
                except ValueError:
                    continue
    return best


def quality_score(summary: dict | None, frontmatter: dict) -> dict:
    base = 1.0
    parts: list[tuple[str, float]] = []

    if summary:
        hay = [summary.get("tldr")] + list(summary.get("approach") or []) + list(summary.get("findings") or [])
        hay_str = [h for h in hay if isinstance(h, str)]
        n = _max_sample(hay_str)
        if n >= 5000:
            base += 2.0
            parts.append(("sample>5000", 2.0))
        elif n >= 300:
            base += 1.5
            parts.append(("sample 300-5000", 1.5))
        elif n >= 100:
            base += 1.0
            parts.append(("sample 100-300", 1.0))
        elif n > 0:
            base += 0.5
            parts.append(("sample<100", 0.5))

        if _NATIONAL_RE.search(" ".join(hay_str)):
            base += 0.5
            parts.append(("national source", 0.5))

        year = summary.get("year")
        if isinstance(year, int):
            if year >= 2020:
                base += 0.5
                parts.append(("recent >=2020", 0.5))
            elif year >= 2015:
                base += 0.25
                parts.append(("2015-2019", 0.25))

        desig = str(summary.get("designation") or "").lower()
        if "local" in desig:
            base += 0.25
            parts.append(("local context", 0.25))
        if "algorithm" in desig:
            base += 0.25
            parts.append(("algorithm focus", 0.25))

    pages = frontmatter.get("page_count")
    try:
        pages = int(pages) if pages else 0
    except (TypeError, ValueError):
        pages = 0
    if pages >= 15:
        base += 0.5
        parts.append(("pages>=15", 0.5))
    elif pages >= 8:
        base += 0.25
        parts.append(("pages 8-14", 0.25))

    return {"score": round(min(base, 5.0), 3), "parts": parts}


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------


def build_validation(papers, per_paper, tier_cfg) -> str:
    rows = []  # (max_combined, annotated_medhigh, annotated_high)
    n_annotated = 0
    for stem, _md, json_path in papers:
        summary = load_summary(json_path) or {}
        topics = (summary.get("topic_relevance") or {}).get("topics") or []
        rels = [t.get("relevance") for t in topics if isinstance(t, dict)]
        high = any(r == "high" for r in rels)
        medhigh = any(r in ("high", "medium") for r in rels)
        if medhigh:
            n_annotated += 1
        best = per_paper[stem]["best_score"]
        rows.append((best, 1.0 if medhigh else 0.0, 1.0 if high else 0.0))

    arr = np.array(rows)
    mc = arr[:, 0]
    medhigh = arr[:, 1]
    high = arr[:, 2]

    def point_biserial(x, y):
        if np.ptp(y) == 0:
            return float("nan")
        g1, g0 = x[y == 1], x[y == 0]
        return float((g1.mean() - g0.mean()) / x.std() * np.sqrt((len(g1) * len(g0)) / (len(x) ** 2)))

    thr = tier_cfg["supporting_min"]
    tp = int(((medhigh == 1) & (mc >= thr)).sum())
    fn = int(((medhigh == 1) & (mc < thr)).sum())
    fp = int(((medhigh == 0) & (mc >= thr)).sum())
    tn = int(((medhigh == 0) & (mc < thr)).sum())
    sens = tp / (tp + fn) if tp + fn else float("nan")
    spec = tn / (tn + fp) if tn + fp else float("nan")
    prec = tp / (tp + fp) if tp + fp else float("nan")
    f1 = 2 * prec * sens / (prec + sens) if prec + sens else float("nan")

    return "\n".join([
        "# Validation of Automated Scores vs Existing Annotations",
        "",
        "**Caveat:** the annotations (`odin_topics` / `topic_relevance` in the `_summarized.json`",
        "files) were AI-generated under the **old** topic taxonomy (1.A-14.C) before the thesis",
        "overhaul. They are a sanity check only — not ground truth. Use them to confirm the",
        "automated scorer points in the same direction, then re-calibrate thresholds with judgment.",
        "",
        f"- Papers with at least one `medium`/`high` annotated topic: **{n_annotated}** / {len(papers)}",
        f"- Point-biserial correlation (annotated med/high vs best combined score): **{point_biserial(mc, medhigh):.3f}**",
        f"- Point-biserial correlation (annotated high vs best combined score): **{point_biserial(mc, high):.3f}**",
        "",
        f"Confusion vs `supporting_min={thr}` threshold (positive = automated relevance >= threshold):",
        "",
        "| | annotated relevant | annotated not |",
        "|---|---|---|",
        f"| automated >= thr | {tp} (TP) | {fp} (FP) |",
        f"| automated < thr  | {fn} (FN) | {tn} (TN) |",
        "",
        f"- Sensitivity (recall of annotated-relevant): **{sens:.3f}**",
        f"- Specificity: **{spec:.3f}**",
        f"- Precision: **{prec:.3f}**",
        f"- F1: **{f1:.3f}**",
        "",
        "> If sensitivity is very low, many annotated-relevant papers fall below the threshold:",
        "> lower `tiers.supporting_min` in config/modules.yaml. If specificity is very low,",
        "> the threshold is too permissive. Adjust in config and re-run `scripts/score.py` only.",
    ])


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def load_cache(cache: Path):
    stems = json.loads((cache / "embeddings_stems.json").read_text())
    embeddings = np.load(cache / "embeddings.npy")
    tfidf, matrix, t_stems = joblib.load(cache / "tfidf.pkl")
    bm25, b_stems = joblib.load(cache / "bm25.pkl")
    assert stems == t_stems == b_stems, "cache stems disagree — re-run embed.py"
    texts = {
        line["stem"]: line["text"]
        for line in (json.loads(l) for l in (cache / "texts.jsonl").read_text().splitlines() if l)
    }
    return stems, embeddings, tfidf, matrix, bm25, texts


def tier(score: float, tiers: dict) -> str:
    if score >= tiers["crucial_min"]:
        return "crucial"
    if score >= tiers["supporting_min"]:
        return "supporting"
    return "cull"


def main() -> None:
    ap = argparse.ArgumentParser(description="Score corpus against module queries.")
    ap.add_argument("--corpus", default=str(DEFAULT_CORPUS))
    ap.add_argument("--cache", default=str(DEFAULT_CACHE))
    ap.add_argument("--config", default=str(DEFAULT_CONFIG))
    ap.add_argument("--out", default=str(DEFAULT_SCORES))
    ap.add_argument("--modules", default="", help="comma-separated module ids (default: all)")
    ap.add_argument("--top-n", type=int, default=25, help="rows per module in report.md")
    args = ap.parse_args()

    cache = Path(args.cache)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    cfg = yaml.safe_load(Path(args.config).read_text())
    weights = cfg["weights"]
    tiers = cfg["tiers"]
    redundancy_thr = float(cfg.get("redundancy_threshold", 0.92))
    mod_cfg = cfg["modules"]
    suffix = ""
    if args.modules:
        wanted = set(args.modules.split(","))
        mod_cfg = [m for m in mod_cfg if m["id"] in wanted]
        suffix = "--subset"  # never clobber the full-report outputs

    stems, embeddings, tfidf, matrix, bm25, _texts = load_cache(cache)
    papers = corpus_paths(args.corpus)
    summary_by_stem = {s: load_summary(jp) for s, _md, jp in papers}
    stem_index = {s: i for i, s in enumerate(stems)}

    # ---- quality (once) ----
    quality: dict[str, dict] = {}
    for stem, md_path, _jp in papers:
        fm = parse_frontmatter(read_marked(md_path))
        quality[stem] = quality_score(summary_by_stem[stem], fm)

    # ---- redundancy clusters (once, from cached BERT embeddings) ----
    sims = embeddings @ embeddings.T
    mask = sims > redundancy_thr
    np.fill_diagonal(mask, False)
    n_comp, labels = connected_components(csr_matrix(mask), directed=False)
    clusters = []
    for c in range(n_comp):
        members = [stems[i] for i in np.where(labels == c)[0]]
        if len(members) > 1:
            # off-diagonal max similarity
            sub = sims[labels == c, :][:, labels == c]
            np.fill_diagonal(sub, -1.0)
            max_sim = float(sub.max())
            def _recency(s):
                sm = summary_by_stem.get(s)
                y = sm.get("year") if isinstance(sm, dict) else None
                return int(y) if isinstance(y, int) else 0

            ranked = sorted(members, key=lambda s: (_recency(s), quality[s]["score"]), reverse=True)
            clusters.append({
                "papers": ranked,
                "max_similarity": max_sim,
                "keep": ranked[0],  # most recent, then strongest (culler recency rule)
                "cull": ranked[1:],
            })

    # ---- module relevance ----
    from sentence_transformers import SentenceTransformer  # heavy, lazy

    print("Loading BERT model for query embeddings...")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    module_results: dict[str, dict] = {}

    for mod in mod_cfg:
        mid = mod["id"]
        q = mod["description"] + "\n" + " ".join(mod.get("keywords", []))
        q_emb = model.encode(q, normalize_embeddings=True, convert_to_numpy=True)
        bert = np.clip(embeddings @ q_emb, 0.0, 1.0)

        q_vec = tfidf.transform([q])
        tfidf_sim = (matrix @ q_vec.T).toarray().ravel()

        bm25_scores = np.array(bm25.get_scores(_tokenize(q)), dtype=float)
        rng = bm25_scores.max() - bm25_scores.min()
        bm25_norm = (bm25_scores - bm25_scores.min()) / rng if rng > 1e-12 else np.zeros_like(bm25_scores)

        combined = weights["bert"] * bert + weights["tfidf"] * tfidf_sim + weights["bm25"] * bm25_norm

        top_idx = np.argsort(-combined)
        top = []
        for i in top_idx:
            s = stems[i]
            sm = summary_by_stem.get(s) or {}
            top.append({
                "stem": s,
                "title": sm.get("title"),
                "year": sm.get("year"),
                "bert": round(float(bert[i]), 3),
                "tfidf": round(float(tfidf_sim[i]), 3),
                "bm25": round(float(bm25_norm[i]), 3),
                "combined": round(float(combined[i]), 3),
                "quality": quality[s]["score"],
            })
        module_results[mid] = {
            "name": mod["name"],
            "query": q,
            "top": top,
            "scores": {s: round(float(combined[stem_index[s]]), 3) for s in stems},
        }
        print(f"  scored module {mid}: top={top[0]['stem']} ({top[0]['combined']})")

    per_paper: dict[str, dict] = {}
    for s in stems:
        scores = {mid: module_results[mid]["scores"][s] for mid in module_results}
        best_mid = max(scores, key=scores.get)
        sm = summary_by_stem.get(s) or {}
        per_paper[s] = {
            "title": sm.get("title"),
            "year": sm.get("year"),
            "designation": sm.get("designation"),
            "quality": quality[s]["score"],
            "quality_parts": quality[s]["parts"],
            "best_module": best_mid,
            "best_score": round(float(scores[best_mid]), 3),
            "tier": tier(scores[best_mid], tiers),
            "scores": scores,
        }

    # ---- outputs ----
    generated = datetime.now(timezone.utc).isoformat()
    index = {
        "generated_at": generated,
        "corpus": {"papers": len(stems), "with_summary": len(papers)},
        "weights": weights,
        "tiers": tiers,
        "modules": {mid: {"name": module_results[mid]["name"], "top": module_results[mid]["top"]} for mid in module_results},
        "papers": per_paper,
    }
    (out / f"index{suffix}.json").write_text(json.dumps(index, ensure_ascii=False, indent=2))

    (out / f"redundancy{suffix}.json").write_text(
        json.dumps({"generated_at": generated, "threshold": redundancy_thr, "clusters": clusters}, ensure_ascii=False, indent=2)
    )

    # ---- report.md ----
    lines = [
        "# Odin-Literature Relevance & Quality Report",
        "",
        f"- Corpus: **{len(stems)}** papers | generated **{generated}**",
        f"- Weights: BERT {weights['bert']} / TF-IDF {weights['tfidf']} / BM25 {weights['bm25']}",
        f"- Tier thresholds: crucial >= {tiers['crucial_min']}, supporting >= {tiers['supporting_min']}",
        f"- Redundancy threshold: cosine > {redundancy_thr}",
        "",
        "Regenerate with `python3 scripts/score.py`. Edit `config/modules.yaml` to adapt to outline changes.",
        "",
    ]
    for mid in module_results:
        mr = module_results[mid]
        lines += [f"## {mr['name']} (`{mid}`)", ""]
        lines += ["| # | Paper | Year | BERT | TF-IDF | BM25 | Combined | Quality |", "|---|-------|------|------|--------|------|----------|---------|"]
        for rank, row in enumerate(mr["top"][: args.top_n], 1):
            title = (row["title"] or row["stem"])[:70]
            lines.append(f"| {rank} | {title} | {row['year']} | {row['bert']:.2f} | {row['tfidf']:.2f} | {row['bm25']:.2f} | **{row['combined']:.2f}** | {row['quality']:.2f} |")
        lines += ["", ""]

    culls = sorted(
        ((s, p) for s, p in per_paper.items() if p["best_score"] < tiers["supporting_min"] and p["quality"] < 3.0),
        key=lambda kv: kv[1]["best_score"],
    )
    lines += [f"## Prime Cull Candidates ({len(culls)})", "",
              "Lowest relevance AND quality — strongest candidates to drop from the RRL.",
              "",
              "| Paper | Best score | Best module | Quality |", "|-------|-----------|-------------|---------|"]
    for s, p in culls[:75]:
        title = (p["title"] or s)[:60]
        lines.append(f"| {title} | {p['best_score']:.2f} | {p['best_module']} | {p['quality']:.2f} |")
    lines += ["", ""]

    lines += [f"## Near-Duplicate Clusters ({len(clusters)})", ""]
    for c in clusters:
        lines.append(
            f"- **{len(c['papers'])} papers, max cosine {c['max_similarity']:.3f}**: "
            f"keep `{c['keep']}` | cull: " + ", ".join(c["cull"])
        )
    lines += ["", "> Keep rule = most recent, then strongest quality (paper-culler skill).",
              "> Detailed cluster members: `scores/redundancy.json`."]

    (out / f"report{suffix}.md").write_text("\n".join(lines))

    (out / f"validation{suffix}.md").write_text(build_validation(papers, per_paper, tiers))

    print(f"Wrote {out / (('index' + suffix + '.json'))}, {out / (('report' + suffix + '.md'))}, "
          f"{out / (('redundancy' + suffix + '.json'))}, {out / (('validation' + suffix + '.md'))}")


if __name__ == "__main__":
    main()
