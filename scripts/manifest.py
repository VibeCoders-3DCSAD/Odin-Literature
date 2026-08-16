"""Build scores/manifest.json from the corpus.

Regenerate whenever conversions change:
    python3 scripts/manifest.py

Output: one entry per stem with metadata sourced from the _summarized.json
(paper_id, title, authors, year, venue, designation, odin_topics) and the
_marked.md frontmatter (source_pdf, sha256, page_count, char count).
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from common import (
    DEFAULT_CORPUS,
    DEFAULT_SCORES,
    corpus_paths,
    load_summary,
    parse_frontmatter,
    read_marked,
)


def main() -> None:
    ap = argparse.ArgumentParser(description="Build the corpus manifest.")
    ap.add_argument("--corpus", default=str(DEFAULT_CORPUS))
    ap.add_argument("--out", default=str(DEFAULT_SCORES / "manifest.json"))
    args = ap.parse_args()

    papers = corpus_paths(args.corpus)
    manifest: dict = {"generated_at": datetime.now(timezone.utc).isoformat(), "count": len(papers), "papers": {}}

    for stem, md_path, json_path in papers:
        meta = parse_frontmatter(read_marked(md_path))
        summary = load_summary(json_path) or {}
        topics = summary.get("odin_topics") or []
        manifest["papers"][stem] = {
            "paper_id": summary.get("paper_id"),
            "title": summary.get("title"),
            "authors": summary.get("authors"),
            "year": summary.get("year"),
            "venue": summary.get("venue"),
            "designation": summary.get("designation"),
            "odin_topics": topics if isinstance(topics, list) else [],
            "source_pdf": meta.get("source_pdf"),
            "source_pdf_sha256": meta.get("source_pdf_sha256"),
            "page_count": meta.get("page_count"),
            "markdown_char_count": meta.get("markdown_char_count"),
            "marked_md": str(md_path.relative_to(Path(args.corpus).parent.parent)),
        }

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2, sort_keys=True)
    print(f"Wrote manifest with {len(papers)} papers -> {args.out}")


if __name__ == "__main__":
    main()
