# /// script
# requires-python = ">=3.12"
# dependencies = ["beautifulsoup4>=4.12", "markdownify>=0.13"]
# ///
"""Fetch the topic-relevant part of a site's documentation via its llms.txt.

An llms.txt (https://llmstxt.org) is a markdown index: an H1 title, an optional
blockquote summary, then H2 sections of `- [name](url): notes` links. It is a
catalog, not a document — fetching every link would drown the wiki in docs that
have nothing to do with it. So this adapter runs in two phases:

  1. `--list` fetches the catalog and prints every link with an id and a keyword
     `hint` score. Nothing is written. `agents/docs_selector.md` reads this list
     and judges relevance against the wiki's topic — the hint is a cue, not the
     decision, because "software factory" docs rarely contain those words.
  2. `--pick 3,7,12` fetches exactly those ids. Without `--pick`, the top
     `--max-pages` links by hint are fetched (fallback for runs with no selector).

Layout (a tree adapter, like repos — SOURCES.md):

  raw/llms-<host>[-<dir>]/
    llms.txt              # catalog snapshot, overwritten every run
    <page-slug>.md        # one per fetched link; immutable, skipped if present

Identity is per page: the page slug comes from the link's URL path, minus the
path prefix every catalog link shares. So a second run with a different
selection adds the new pages and skips the ones already fetched. Each page's
source page goes to `wiki/docs/llms-<slug>/<page-slug>.md`, beside the set's
OVERVIEW.md hub (CONVENTIONS.md §15).

The hint: the topic is the `<slug>` of `wiki-<NNN>-<slug>/` plus `--keywords`.
Each keyword is weighted by IDF over this catalog (a word in every link, like
"software" in a dev-docs site, is worth almost nothing), doubled when it is in the
link name, and the whole topic phrase ("software factory", adjacent) earns a
bonus on top of its words.

Usage:
  uv run --script fetch_llms_txt.py --url https://docs.example.com/llms.txt --wiki-dir wiki-<NNN>-<slug> --list
  uv run --script fetch_llms_txt.py --url ... --wiki-dir ... --pick 3,7,12

Receipt (stdout, fetch mode):
  {"origin": "llms-txt", "original_path": <url>, "title", "subtitle", "source_url",
   "authors": [], "published_date": null, "raw_path": "raw/llms-<slug>/", "catalog": "raw/llms-<slug>/llms.txt", "catalog_size",
   "hub_page": "wiki/docs/llms-<slug>/OVERVIEW.md",
   "pages": [{"id", "title", "source_url", "raw_path", "source_page", "action", "chars"}], ["warning"]}
  action is `fetched`, `skipped` (already in raw/) or `failed`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from markdownify import markdownify

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0 Safari/537.36"
)

# Same order as fetch_article.py: first selector with real text wins.
BODY_SELECTORS = ["article", "main", "div.content", "body"]

STRIP_TAGS = ["script", "style", "noscript", "nav", "footer", "form", "button", "svg", "iframe", "header", "aside"]

STOPWORDS = {"a", "an", "and", "the", "of", "for", "to", "in", "on", "with", "wiki", "docs", "notes"}

LINK_RE = re.compile(r"^\s*[-*]\s*\[(?P<name>[^\]]+)\]\((?P<url>[^)\s]+)\)\s*(?::\s*(?P<notes>.*))?$")

PHRASE_BONUS = 3.0


def slugify(text: str, limit: int = 60) -> str:
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-").lower()
    return slug[:limit].rsplit("-", 1)[0] if len(slug) > limit else slug


def fetch(url: str) -> tuple[str, str]:
    """Return (body, content_type). Raises SystemExit on a failed or empty fetch."""
    result = subprocess.run(
        ["curl", "-sL", "--max-time", "60", "-A", USER_AGENT, "-w", "\n%{content_type}", url],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    body, _, content_type = result.stdout.rpartition("\n")
    if result.returncode != 0 or not body.strip():
        raise SystemExit(f"fetch failed for {url}: {result.stderr.strip() or 'empty response'}")
    return body, content_type.lower()


def stem(word: str) -> str:
    """Crude plural folding, enough that `factory` matches `factories`."""
    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"
    if word.endswith("s") and not word.endswith("ss") and len(word) > 3:
        return word[:-1]
    return word


def words(text: str) -> list[str]:
    return [stem(w) for w in re.findall(r"[a-z0-9]+", text.lower())]


def topic_keywords(wiki_dir: Path, extra: str | None) -> tuple[list[str], list[list[str]]]:
    """Return (keywords, phrases). The slug is one phrase; each multi-word --keywords entry is another."""
    topic = re.sub(r"^wiki-\d+-", "", wiki_dir.name)
    phrases = [[w for w in words(topic) if w not in STOPWORDS]]
    phrases += [[w for w in words(entry) if w not in STOPWORDS] for entry in (extra or "").split(",")]
    keywords: list[str] = []
    for phrase in phrases:
        keywords += [w for w in phrase if w not in keywords]
    return keywords, [p for p in phrases if len(p) > 1]


def parse_llms_txt(text: str, base_url: str) -> tuple[str | None, str | None, list[dict]]:
    title = summary = None
    section = ""
    links: list[dict] = []
    for line in text.splitlines():
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
        elif line.startswith("> ") and summary is None:
            summary = line[2:].strip()
        elif line.startswith("## "):
            section = line[3:].strip()
        elif match := LINK_RE.match(line):
            links.append(
                {
                    "id": len(links),
                    "name": match["name"].strip(),
                    "url": urljoin(base_url, match["url"]),
                    "notes": (match["notes"] or "").strip(),
                    "section": section,
                }
            )
    return title, summary, links


def contains(seq: list[str], phrase: list[str]) -> bool:
    n = len(phrase)
    return any(seq[i : i + n] == phrase for i in range(len(seq) - n + 1))


def add_hints(links: list[dict], keywords: list[str], phrases: list[list[str]]) -> None:
    """Score every link in place. IDF is computed over this catalog, so generic words fade."""
    docs = []
    for link in links:
        name = words(link["name"])
        rest = words(f'{link["notes"]} {urlparse(link["url"]).path} {link["section"]}')
        docs.append((name, rest, set(name) | set(rest)))
    idf = {k: math.log((len(links) + 1) / (1 + sum(k in d[2] for d in docs))) for k in keywords}
    for link, (name, rest, bag) in zip(links, docs):
        hint = sum(idf[k] * (2 if k in name else 1) for k in keywords if k in bag)
        hint += sum(PHRASE_BONUS for p in phrases if contains(name, p) or contains(rest, p))
        # The llms.txt spec marks skippable links with an "Optional" section.
        if link["section"].lower() == "optional":
            hint *= 0.5
        link["hint"] = round(hint, 2)


def page_slugs(links: list[dict], catalog_url: str) -> None:
    """Slug each link from its URL path, minus the directory prefix the home-host links share.

    The home host is the one most links point at — often not the catalog's own
    (docs.anthropic.com/llms.txt links to platform.claude.com).
    """
    hosts = [urlparse(l["url"]).netloc for l in links]
    host = max(set(hosts), key=hosts.count) if hosts else urlparse(catalog_url).netloc
    local = [urlparse(l["url"]).path.split("/")[:-1] for l in links if urlparse(l["url"]).netloc == host]
    prefix: list[str] = []
    for parts in zip(*local) if local else []:
        if len(set(parts)) != 1:
            break
        prefix.append(parts[0])
    for link in links:
        parsed = urlparse(link["url"])
        parts = parsed.path.split("/")
        if parsed.netloc == host and parts[: len(prefix)] == prefix:
            parts = parts[len(prefix) :]
        else:
            parts = [parsed.netloc] + parts
        path = re.sub(r"(\.html?)?\.(md|mdx|txt)$|\.html?$", "", "/".join(parts)) or "index"
        slug = slugify(path, limit=200)
        if len(slug) > 60:  # keep the specific tail, plus a hash of the full path so cuts never collide
            tail = slug[-51:].split("-", 1)[-1] if slug[-52] != "-" else slug[-51:]
            slug = tail + "-" + hashlib.sha1(path.encode()).hexdigest()[:8]
        link["slug"] = slug


def to_markdown(body: str, content_type: str, url: str) -> str:
    if "html" not in content_type and not body.lstrip().lower().startswith(("<!doctype", "<html")):
        return body.strip()  # already markdown/plain text — the common case for llms.txt links
    soup = BeautifulSoup(body, "html.parser")
    for tag in soup.find_all(STRIP_TAGS):
        tag.decompose()
    for selector in BODY_SELECTORS:
        node = soup.select_one(selector)
        if node and len(node.get_text(strip=True)) > 200:
            return markdownify(str(node), heading_style="ATX").strip()
    print(f"WARN: no body found in {url}", file=sys.stderr)
    return ""


def split_frontmatter(markdown: str) -> tuple[str, str | None]:
    """Docs served as .md often carry their own frontmatter; drop it, keep its description."""
    match = re.match(r"---\n(.*?)\n---\n", markdown, re.S)
    if not match:
        return markdown, None
    desc = re.search(r"^description:\s*(.+)$", match[1], re.M)
    return markdown[match.end() :].lstrip(), desc[1].strip().strip("\"'") if desc else None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--url", required=True, help="URL of the llms.txt file.")
    parser.add_argument("--wiki-dir", required=True, help="Path to wiki-<NNN>-<slug>/; <slug> is the topic.")
    parser.add_argument("--keywords", default=None, help="Extra comma-separated keywords or phrases.")
    parser.add_argument("--list", action="store_true", help="Print every link with id and hint; write nothing.")
    parser.add_argument("--pick", default=None, help="Comma-separated link ids to fetch (from --list).")
    parser.add_argument("--max-pages", type=int, default=10, help="Without --pick: fetch the top N by hint (default 10).")
    parser.add_argument("--output", default=None, help="Override the raw folder (default: raw/llms-<slug>/).")
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252
        stream.reconfigure(encoding="utf-8")

    wiki_dir = Path(args.wiki_dir).expanduser().resolve()
    if not (wiki_dir / "wiki").is_dir():
        raise SystemExit(f"not a wiki dir (no wiki/ inside): {wiki_dir}")

    keywords, phrases = topic_keywords(wiki_dir, args.keywords)
    catalog, _ = fetch(args.url)
    title, summary, links = parse_llms_txt(catalog, args.url)
    if not links:
        raise SystemExit(f"no `- [name](url)` links found in {args.url} — is it an llms.txt?")
    add_hints(links, keywords, phrases)
    page_slugs(links, args.url)

    parsed = urlparse(args.url)
    folder_slug = slugify(f"{parsed.netloc} {parsed.path.rsplit('/', 1)[0]}")
    folder = Path(args.output).expanduser().resolve() if args.output else wiki_dir / "raw" / f"llms-{folder_slug}"
    for link in links:
        link["exists"] = (folder / f"{link['slug']}.md").exists()

    if args.list:
        out = {
            "title": title,
            "summary": summary,
            "keywords": keywords,
            "phrases": [" ".join(p) for p in phrases],
            "links": [
                {k: link[k] for k in ("id", "hint", "section", "name", "notes", "url", "exists")}
                for link in links
            ],
        }
        print(json.dumps(out, indent=1, ensure_ascii=False))
        return

    if args.pick:
        ids = [int(i) for i in re.split(r"[,\s]+", args.pick.strip()) if i]
        unknown = [i for i in ids if not 0 <= i < len(links)]
        if unknown:
            raise SystemExit(f"unknown link ids: {unknown} (catalog has {len(links)})")
        selected = [links[i] for i in ids]
    else:
        ranked = sorted((l for l in links if l["hint"] > 0), key=lambda l: -l["hint"])
        selected = ranked[: args.max_pages]
    if not selected:
        raise SystemExit(f"no links selected from {args.url} — nothing written; run --list and pass --pick")

    folder.mkdir(parents=True, exist_ok=True)
    (folder / "llms.txt").write_text(catalog, encoding="utf-8")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    pages = []
    for link in selected:
        path = folder / f"{link['slug']}.md"
        page = {
            "id": link["id"],
            "title": link["name"],
            "source_url": link["url"],
            "raw_path": path.relative_to(wiki_dir).as_posix(),
            "source_page": f"wiki/docs/{folder.name}/{link['slug']}.md",
        }
        pages.append(page)
        if link["exists"]:
            page["action"] = "skipped"
            continue
        try:
            body, content_type = fetch(link["url"])
        except SystemExit as err:
            print(f"WARN: {err}", file=sys.stderr)
            page["action"] = "failed"
            continue
        markdown, description = split_frontmatter(to_markdown(body, content_type, link["url"]))
        notes = link["notes"] or description
        if len(markdown) < 200:
            page["action"] = "failed"
            continue
        front = [
            "---",
            f"title: {json.dumps(link['name'])}",
            f"subtitle: {json.dumps(notes) if notes else 'null'}",
            "authors: []",
            "published_date: null",
            f"source_url: {link['url']}",
            "origin: llms-txt",
            f"llms_txt: {args.url}",
            f"section: {json.dumps(link['section'])}",
            f"fetched: {now}",
            "---",
            "",
        ]
        # Pages from an llms.txt usually start with their own H1; add one only if missing.
        if not markdown.lstrip().startswith("# "):
            front += [f"# {link['name']}", ""]
        path.write_text("\n".join(front) + "\n" + markdown + "\n", encoding="utf-8")
        page.update(action="fetched", chars=len(markdown))

    receipt = {
        "origin": "llms-txt",
        "original_path": args.url,
        "title": title or parsed.netloc,
        "subtitle": summary,
        "source_url": args.url,
        "authors": [],
        "published_date": None,
        "raw_path": folder.relative_to(wiki_dir).as_posix() + "/",
        "catalog": (folder / "llms.txt").relative_to(wiki_dir).as_posix(),
        "catalog_size": len(links),
        "hub_page": f"wiki/docs/{folder.name}/OVERVIEW.md",
        "pages": pages,
    }
    if not any(p["action"] in ("fetched", "skipped") for p in pages):
        raise SystemExit(f"every selected page failed for {args.url}: {json.dumps(pages, ensure_ascii=False)}")
    if not any(p["action"] == "fetched" for p in pages):
        receipt["warning"] = "no new pages fetched — every selected page is already in raw/"
        print(f"WARN: {receipt['warning']} ({args.url})", file=sys.stderr)
    print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
