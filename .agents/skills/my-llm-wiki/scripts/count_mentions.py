# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6.0"]
# ///
"""Count how many distinct origins mention each entity / concept slug.

This is the single source of truth for the wiki's materialization threshold:
an entity or concept page exists **iff at least `--threshold` (default 2)
distinct origins list it** in their `entities:` / `concepts:` frontmatter.
Source-like pages are the pages written directly from an ingested artifact —
`wiki/sources/*.md`, `wiki/repos/<repo>/*.md` and `wiki/docs/<set>/*.md`.

An origin is one independent witness. A page in `sources/` is its own origin; all
pages under one `repos/<repo>/` or `docs/<set>/` directory are a single origin, so
a repo's ARCHITECTURE.md plus five repo notes, or ten pages of one vendor's docs,
count once — otherwise one codebase or one doc set could materialize a concept
on its own (CONVENTIONS.md §3).

The wikilinks are read from frontmatter, not from the body, so the count is a
cheap, deterministic frontmatter walk instead of a full-text scan.

Usage:
  uv run --script count_mentions.py --wiki-dir ../../../../wiki-<slug>
  uv run --script count_mentions.py --wiki-dir ... --threshold 2 --json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml

# Globs (relative to the wiki bundle) whose pages count toward the threshold.
# <!-- unchanged in 03, deliberately --> `questions/` and `notes/` are interaction-owned:
# they are written *from* wiki pages, so counting them would let the wiki cite itself into
# existence. Repo notes are the exception and already match `repos/*/*.md`.
SOURCE_LIKE_GLOBS: list[str] = ["sources/*.md", "repos/*/*.md", "docs/*/*.md"]  # <!-- repos added in 02, docs later -->

# Grouped dirs: every page under one <dir>/<group>/ is a single origin.
GROUPED_DIRS: set[str] = {"repos", "docs"}

# A docs set's OVERVIEW.md is written from the catalog's titles, not from any page,
# so it is not a witness (CONVENTIONS.md §15).
NOT_SOURCE_LIKE: set[str] = {"index.md", "OVERVIEW.md"}

KINDS: list[tuple[str, str]] = [("entities", "entity"), ("concepts", "concept")]


def parse_frontmatter(path: Path) -> dict[str, Any]:
    """YAML frontmatter of a markdown file; empty dict when absent or broken."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}
    if not text.startswith("---"):
        return {}
    lines = text.splitlines()
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}
    try:
        data = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def slug_of(reference: Any) -> str:
    """Last path segment of a wikilink or path: "[[wiki/concepts/mcp]]" -> "mcp"."""
    text = str(reference).strip().strip("[]").split("|")[0].strip()
    if text.endswith(".md"):
        text = text[:-3]
    return text.rsplit("/", 1)[-1]


def source_like_pages(bundle: Path) -> list[Path]:
    pages: list[Path] = []
    for pattern in SOURCE_LIKE_GLOBS:
        pages += [p for p in bundle.glob(pattern) if p.is_file() and p.name not in NOT_SOURCE_LIKE]
    return sorted(pages)


def origin_of(rel: str) -> str:
    """`wiki/repos/<repo>/x.md` -> `wiki/repos/<repo>`; a page in `sources/` is its own origin."""
    parts = rel.split("/")
    return "/".join(parts[:3]) if len(parts) == 4 and parts[1] in GROUPED_DIRS else rel


def collect(bundle: Path) -> dict[str, dict[str, list[str]]]:
    """{kind: {slug: [pages that mention it]}} — pages are wiki-dir-relative, sorted."""
    mentions: dict[str, dict[str, set[str]]] = {key: {} for key, _ in KINDS}
    for page in source_like_pages(bundle):
        fm = parse_frontmatter(page)
        rel = f"wiki/{page.relative_to(bundle).as_posix()}"
        for key, _ in KINDS:
            for reference in fm.get(key) or []:
                slug = slug_of(reference)
                if slug:
                    mentions[key].setdefault(slug, set()).add(rel)
    return {key: {slug: sorted(pages) for slug, pages in sorted(value.items())} for key, value in mentions.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wiki-dir", required=True, help="Path to wiki-<slug>/ (the dir holding raw/, wiki/ and log.md).")
    parser.add_argument("--threshold", type=int, default=2, help="Mentions needed to materialize a page (default: 2).")
    parser.add_argument("--json", action="store_true", help="JSON only — suppress the human table on stderr.")
    args = parser.parse_args()

    wiki_dir = Path(args.wiki_dir).expanduser().resolve()
    bundle = wiki_dir / "wiki"
    if not bundle.is_dir():
        raise SystemExit(f"not a wiki dir (no wiki/ inside): {wiki_dir}")

    mentions = collect(bundle)
    origins = {
        key: {slug: len({origin_of(p) for p in pages}) for slug, pages in mentions[key].items()} for key, _ in KINDS
    }
    qualifying = {key: [slug for slug, n in origins[key].items() if n >= args.threshold] for key, _ in KINDS}

    if not args.json:
        print(f"{'kind':<8} {'slug':<40} {'pages':>5} {'origins':>7}  qualifies", file=sys.stderr)
        for key, label in KINDS:
            for slug, pages in mentions[key].items():
                n = origins[key][slug]
                mark = "yes" if n >= args.threshold else ""
                print(f"{label:<8} {slug:<40} {len(pages):>5} {n:>7}  {mark}", file=sys.stderr)

    print(
        json.dumps(
            {
                "wiki_dir": str(wiki_dir),
                "threshold": args.threshold,
                "source_like_pages": len(source_like_pages(bundle)),
                "entities": mentions["entities"],
                "concepts": mentions["concepts"],
                "origins": origins,
                "qualifying": qualifying,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
