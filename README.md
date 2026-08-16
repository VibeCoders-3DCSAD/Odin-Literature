# Odin-Literature

Review of Related Literature (RRL) corpus for the Odin thesis, with an offline
relevance & quality scoring pipeline. **No LLMs, no token APIs, no agents.**

## What lives here

- `literature/conversions/batch-1..6/` — every curated paper as:
  - `{stem}_marked.md` — full-text markdown conversion (with YAML metadata frontmatter)
  - `{stem}_summarized.json` — structured summary (metadata, `odin_topics`, findings, citations)
- `config/modules.yaml` — **the single source of truth** for what "relevant" means
- `scripts/` — the scoring pipeline
- `scores/` — generated, committed outputs (see below)

**Raw PDFs are NOT in this repo** (`.gitignore`d). The ground-truth PDFs live in
`Odin-Paper` (Git LFS) and the project Google Drive. This repo operates entirely
on the markdown conversions — which is all the scorer needs.

## How relevance & quality are computed

For each paper × module in `config/modules.yaml`:

| Signal | Method | Weight |
|--------|--------|--------|
| Semantic relevance | BERT document embedding vs module query (`all-MiniLM-L6-v2`, local CPU) | 0.5 |
| Lexical relevance | TF-IDF cosine similarity | 0.3 |
| Lexical ranking | BM25 | 0.2 |

Quality is **not** a similarity problem, so it is a rule-based heuristic over the
JSON summaries + frontmatter: sample size, national-source mention (FIES/PSA/BSP),
recency, page count, and designation (local/algorithm-specific). Near-duplicate
papers are clustered by embedding cosine similarity with a recency→quality
"keep" rule.

> BERT sees only the first 2048 tokens per paper (title/abstract/intro) by
> default — the full text still feeds TF-IDF/BM25. See `scripts/embed.py --help`
> to adjust.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
# CPU-only torch first (smaller), then the rest:
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```

## Regenerate the scores

```bash
# 1. (Re)build caches: text, BERT embeddings, TF-IDF, BM25
python3 scripts/embed.py            # --force to rebuild; resumable
# 2. Score everything and write scores/{index,report,redundancy,validation}.{json,md}
python3 scripts/score.py            # --modules a,b to score a subset (writes *--subset files)
# 3. Rebuild the manifest if conversions changed
python3 scripts/manifest.py
```

## Adapting when the thesis changes

The design rule is: **edits go in `config/`, never in code.**

| Change | What to do |
|--------|-----------|
| New/renamed/removed module, or new query wording | Edit `config/modules.yaml` → `python3 scripts/score.py` (fast, cached embeddings) |
| Thresholds (crucial/supporting, redundancy) | Edit `config/modules.yaml` → `python3 scripts/score.py` |
| A conversion or new paper added/changed | `python3 scripts/embed.py` (detects changes; `--force` to rebuild) → `python3 scripts/score.py` |
| Topics now come from a different outline | Replace the `modules:` block in `config/modules.yaml` |
| Papers stop being ranked against modules at all | Same — modules *are* the config |

## Scores reference

- `scores/index.json` — per-paper × module scores, best module, tier, quality, redundancy info
- `scores/report.md` — per-module ranked tables, prime cull candidates, near-duplicate clusters
- `scores/redundancy.json` — duplicate clusters with `keep`/`cull` decisions
- `scores/validation.md` — sanity check of automated scores vs the existing (pre-overhaul,
  AI-generated, old-taxonomy) annotations. **Treat as a sanity check, not ground truth.**

## Notes

- Generated scores are committed so the scored corpus is browsable without running anything.
- `cache/` is gitignored (regenerable). Only ~101 MB of markdown is committed.
- For migration into this repo from `Odin-Paper`, only `_marked.md` + `_summarized.json`
  were copied; the pipeline needs nothing else.
