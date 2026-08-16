"""Build and cache the scoring inputs from the corpus markdown.

    python3 scripts/embed.py [--force]

Caches (all under cache/, gitignored):
  texts.jsonl          cleaned plain text per stem
  embeddings.npy       BERT document vectors (N x 384) + embeddings_stems.json
  tfidf.pkl            (TfidfVectorizer, sparse matrix, stems)
  bm25.pkl             (tokenized corpus, stems)

Re-runs are skipped automatically when the corpus fingerprint is unchanged.
Pass --force (or change a conversion) to rebuild. Adding a module to
config/modules.yaml does NOT require a rebuild — only score.py is needed.

BERT cost controls (the encoding step is the slow one on small machines):
  --max-tokens        tokens per chunk (default 512; MiniLM supports 512)
  --window-tokens     BERT only sees the first N tokens per document
                      (default 2048 = title/abstract/intro, where relevance
                      lives). Full text still feeds TF-IDF/BM25. Raise it
                      for more coverage at more compute, lower it to speed
                      up.
  --model             any sentence-transformers model id

Encoding is resumable: partial progress is checkpointed in cache/, so a
killed run continues where it left off on the next invocation.
"""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from common import (
    DEFAULT_CACHE,
    DEFAULT_CORPUS,
    clean_text,
    corpus_fingerprint,
    corpus_paths,
    read_marked,
)

_TOKEN_RE = re.compile(r"[A-Za-z0-9]+")
_STOP = frozenset(
    "a an and are as at be by for from has in is it its of on or that the this to was were will with".split()
)
_SENTENCE_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
_MAX_TOKENS = 512  # chunk length for BERT encoding (MiniLM supports 512)
_WINDOW_TOKENS = 2048  # BERT window per document

_PARTIAL_NPY = "embeddings_partial.npy"
_PARTIAL_STEMS = "embeddings_partial_stems.json"


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in _TOKEN_RE.findall(text) if len(t) > 2 and t.lower() not in _STOP]


def chunk_ids(ids: list[int], tokenizer, max_tokens: int) -> list[str]:
    return [tokenizer.decode(ids[i : i + max_tokens], skip_special_tokens=True) for i in range(0, len(ids), max_tokens)]


def embed_documents(model, texts: list[str], cache: Path, max_tokens: int, window_tokens: int) -> np.ndarray:
    model.max_seq_length = max_tokens
    done: list[int] = []
    embeddings: list[np.ndarray] = []

    partial_npy, partial_stems = cache / _PARTIAL_NPY, cache / _PARTIAL_STEMS
    if partial_npy.exists() and partial_stems.exists():
        embeddings = [np.load(partial_npy)]
        done = json.loads(partial_stems.read_text())
        print(f"Resuming: {len(done)} docs already embedded.", flush=True)

    start = time.time()
    for i, text in enumerate(texts):
        if i in done:
            embeddings.append(embeddings[0][i])
            continue
        ids = model.tokenizer.encode(text, add_special_tokens=False)[:window_tokens]
        chunks = chunk_ids(ids, model.tokenizer, max_tokens)
        vecs = model.encode(chunks, batch_size=64, show_progress_bar=False, normalize_embeddings=True, convert_to_numpy=True)
        doc = np.mean(vecs, axis=0)
        norm = np.linalg.norm(doc)
        if norm > 0:
            doc = doc / norm
        embeddings.append(doc)
        done.append(i)
        if len(done) % 100 == 0:
            cur = np.vstack(embeddings)
            np.save(partial_npy, cur)
            partial_stems.write_text(json.dumps(sorted(set(done))))
            print(f"  checkpoint {len(done)}/{len(texts)} ({time.time() - start:.1f}s)", flush=True)

    return np.vstack(embeddings)


def main() -> None:
    ap = argparse.ArgumentParser(description="Build/cache corpus text, embeddings, TF-IDF, BM25.")
    ap.add_argument("--corpus", default=str(DEFAULT_CORPUS))
    ap.add_argument("--cache", default=str(DEFAULT_CACHE))
    ap.add_argument("--model", default=_SENTENCE_MODEL)
    ap.add_argument("--max-tokens", type=int, default=_MAX_TOKENS, help="BERT chunk length (model max 512)")
    ap.add_argument("--window-tokens", type=int, default=_WINDOW_TOKENS, help="BERT window per doc (first N tokens)")
    ap.add_argument("--force", action="store_true", help="Rebuild cache even if unchanged")
    args = ap.parse_args()

    cache = Path(args.cache)
    cache.mkdir(parents=True, exist_ok=True)
    papers = corpus_paths(args.corpus)
    fp = corpus_fingerprint(papers)

    fp_file = cache / "fingerprint.json"
    fresh = False
    if fp_file.exists() and not args.force:
        try:
            fresh = json.loads(fp_file.read_text())["fingerprint"] == fp
        except (json.JSONDecodeError, KeyError):
            fresh = False
    if fresh:
        print("Corpus unchanged — cache is fresh. Use --force to rebuild.")
        return

    print(f"Processing {len(papers)} papers...")
    stems, texts = [], []
    for stem, md_path, _ in papers:
        stems.append(stem)
        texts.append(clean_text(read_marked(md_path)))

    (cache / "texts.jsonl").write_text(
        "\n".join(json.dumps({"stem": s, "text": t}, ensure_ascii=False) for s, t in zip(stems, texts)),
        encoding="utf-8",
    )
    print(f"Wrote cache/texts.jsonl ({sum(len(t) for t in texts)} chars)")

    # ---- BERT document embeddings (CPU, local) ----
    from sentence_transformers import SentenceTransformer  # lazy import: heavy

    print(f"Loading BERT model {args.model} ...")
    model = SentenceTransformer(args.model)
    print(f"Embedding documents (window={args.window_tokens}, chunk={args.max_tokens})...")
    vecs = embed_documents(model, texts, cache, args.max_tokens, args.window_tokens)
    np.save(cache / "embeddings.npy", vecs)
    (cache / "embeddings_stems.json").write_text(json.dumps(stems, ensure_ascii=False))
    for p in (cache / _PARTIAL_NPY, cache / _PARTIAL_STEMS):
        if p.exists():
            p.unlink()
    print(f"Wrote cache/embeddings.npy {vecs.shape}")

    # ---- TF-IDF ----
    tfidf = TfidfVectorizer(min_df=2, max_df=0.9, sublinear_tf=True, stop_words="english", token_pattern=r"[A-Za-z0-9]+")
    matrix = tfidf.fit_transform(texts)
    joblib.dump((tfidf, matrix, stems), cache / "tfidf.pkl", compress=3)
    print(f"Wrote cache/tfidf.pkl (vocab={len(tfidf.vocabulary_)} tokens)")

    # ---- BM25 ----
    from rank_bm25 import BM25Okapi  # lazy import

    tokenized = [tokenize(t) for t in texts]
    bm25 = BM25Okapi(tokenized)
    joblib.dump((bm25, stems), cache / "bm25.pkl", compress=3)
    print("Wrote cache/bm25.pkl")

    fp_file.write_text(json.dumps({"fingerprint": fp}))
    print("Cache build complete.")


if __name__ == "__main__":
    main()
