"""Shared helpers for the Odin-Literature scoring pipeline.

Everything here is deterministic and dependency-light so the pipeline stays
fast to re-run when the corpus or config changes.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CORPUS = REPO_ROOT / "literature" / "conversions"
DEFAULT_CACHE = REPO_ROOT / "cache"
DEFAULT_SCORES = REPO_ROOT / "scores"
DEFAULT_CONFIG = REPO_ROOT / "config" / "modules.yaml"


def corpus_paths(corpus_dir: str | Path | None = None) -> list[tuple[str, Path, Path | None]]:
    """Return [(stem, marked_md_path, summarized_json_path|None)] sorted by stem."""
    root = Path(corpus_dir) if corpus_dir else DEFAULT_CORPUS
    papers = []
    for md in sorted(root.rglob("*_marked.md")):
        stem = md.name[: -len("_marked.md")]
        json_path = md.with_name(stem + "_summarized.json")
        papers.append((stem, md, json_path if json_path.exists() else None))
    return papers


_FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)
_PAGE_RE = re.compile(r"<!--\s*PAGE\s*\d+\s*-->", re.IGNORECASE)
_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")


def strip_frontmatter(text: str) -> str:
    m = _FRONTMATTER_RE.match(text)
    return text[m.end():] if m else text


def parse_frontmatter(md_text: str) -> dict:
    """Parse the YAML-ish frontmatter into a dict. Best-effort, tolerant."""
    m = _FRONTMATTER_RE.match(md_text)
    if not m:
        return {}
    meta: dict = {}
    for line in m.group(0).splitlines():
        line = line.strip()
        if not line or line == "---" or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip().strip('"'), value.strip().strip('"')
        if not key:
            continue
        meta[key] = value
    return meta


def clean_text(md_text: str) -> str:
    text = strip_frontmatter(md_text)
    text = _PAGE_RE.sub(" ", text)
    text = _IMAGE_RE.sub(" ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def read_marked(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def load_summary(path: Path | None) -> dict | None:
    if not path or not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
        return data if isinstance(data, dict) else None
    except (json.JSONDecodeError, OSError):
        return None


def corpus_fingerprint(papers: list[tuple[str, Path, Path | None]]) -> str:
    h = hashlib.sha256()
    for stem, md, _ in sorted(papers, key=lambda p: p[0]):
        st = md.stat()
        h.update(f"{stem}|{st.st_mtime_ns}|{st.st_size}\n".encode())
    return h.hexdigest()
