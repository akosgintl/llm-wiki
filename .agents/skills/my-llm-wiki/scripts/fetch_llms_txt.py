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

Real catalogs are not always flat. Before listing, every `.txt` link is fetched
once and expanded in place, one level deep:

  - a nested index (`- [name](url)` lines, e.g. docs.port.io/llms/guides.txt)
    contributes its links;
  - a bundle (pages concatenated, each under `Canonical page: [..](url)`, e.g.
    docs.warp.dev/_llms-txt/factories.txt) contributes one link per page.

The expanded link replaces its parent, so ids are positions in the expanded list.
Full-docs dumps (`llms-full.txt`, `llms-small.txt`) and API specs (`.json`,
`.yaml`) stay listed with `kind: dump` / `kind: spec` and cannot be picked: they
are not pages. Every other link is `kind: page`.

A page link without an extension is fetched as `<url>.md` first (many doc sites
serve markdown there), falling back to the HTML page.

Layout (a tree adapter, like repos — SOURCES.md):

  raw/docs/llms-<host>[-<dir>]/
    llms.txt              # catalog snapshot, overwritten every run; expanded
                          # sub-catalogs are appended as extra `##` sections
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

`--list` prints `{"id", "hint", "kind", "section", "name", "notes", "url", "exists"}`
per link, plus `expanded`: the sub-catalogs inlined and how many links each gave.

Receipt (stdout, fetch mode):
  {"origin": "llms-txt", "original_path": <url>, "title", "subtitle", "source_url",
   "authors": [], "published_date": null, "raw_path": "raw/docs/llms-<slug>/", "catalog": "raw/docs/llms-<slug>/llms.txt", "catalog_size",
   "hub_page": "wiki/docs/llms-<slug>/OVERVIEW.md",
   "pages": [{"id", "title", "source_url", "raw_path", "source_page", "action", "chars"}], ["warning"]}
  action is `fetched`, `skipped` (already in raw/) or `failed`; a failed page carries a `reason`.
  `warning` also flags a catalog that looks cut off mid-line by the server.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import json
import math
import re
import subprocess
import sys
import unicodedata
from concurrent.futures import ThreadPoolExecutor
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

# A bullet with no link groups the links indented under it ("- Core concepts").
GROUP_RE = re.compile(r"^(?P<indent>\s*)[-*]\s+(?P<label>[^\[].*?)\s*$")

CANONICAL_RE = re.compile(r"^Canonical page:\s*\[[^\]]*\]\((?P<url>[^)\s]+)\)")

DUMP_RE = re.compile(r"(^|/)llms-(full|small|ctx[\w-]*)\.txt$")

SPEC_RE = re.compile(r"\.(json|ya?ml)$|openapi|swagger", re.I)

# Capitalized JSX/MDX component tags (<CardGroup>, <Card title="..">); lowercase HTML stays.
MDX_TAG_RE = re.compile(r"</?[A-Z][A-Za-z0-9.]*(?:\s[^<>]*?)?/?>", re.S)

PHRASE_BONUS = 3.0


def slugify(text: str, limit: int = 60) -> str:
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-").lower()
    return slug[:limit].rsplit("-", 1)[0] if len(slug) > limit else slug


def fetch(url: str, fail: bool = False) -> tuple[str, str]:
    """Return (body, content_type). Raises SystemExit on a failed or empty fetch, or an HTTP error if `fail`."""
    result = subprocess.run(
        ["curl", "-sL", *(["-f"] if fail else []), "--max-time", "60", "-A", USER_AGENT, "-w", "\n%{content_type}", url],
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
    groups: list[tuple[int, str]] = []  # (indent, label) of the group bullets enclosing the current line
    links: list[dict] = []
    for line in text.splitlines():
        indent = len(line) - len(line.lstrip())
        if line.startswith("# ") and title is None:
            title = line[2:].strip()
        elif line.startswith("> ") and summary is None:
            summary = line[2:].strip()
        elif line.startswith("## "):
            section, groups = line[3:].strip(), []
        elif match := LINK_RE.match(line):
            groups = [g for g in groups if g[0] < indent]
            links.append(
                {
                    "name": match["name"].strip(),
                    "url": urljoin(base_url, match["url"]),
                    "notes": (match["notes"] or "").strip(),
                    "section": " / ".join([section] * bool(section) + [g[1] for g in groups]),
                }
            )
        elif match := GROUP_RE.match(line):
            groups = [g for g in groups if g[0] < indent] + [(indent, match["label"].split(":")[0].strip())]
    return title, summary, links


def truncation_warning(text: str, url: str) -> str | None:
    """Flag a catalog the server cut off mid-line: its last line starts a link that does not parse.

    Byte counts and a missing final newline prove nothing — docs.port.io serves exactly
    250,000 bytes on purpose, and docs.warp.dev bundles end without a newline, both cleanly.
    """
    last = text.rstrip("\n").rsplit("\n", 1)[-1]
    if not re.match(r"^\s*[-*]\s*\[", last) or LINK_RE.match(last):
        return None
    warning = f"catalog looks truncated ({len(text.encode())} bytes, last line incomplete): {url}"
    print(f"WARN: {warning}", file=sys.stderr)
    return warning


def link_kind(url: str) -> str:
    path = urlparse(url).path
    if DUMP_RE.search(path):
        return "dump"
    if SPEC_RE.search(path):
        return "spec"
    return "subcatalog" if path.endswith(".txt") else "page"


def parse_bundle(text: str) -> list[dict]:
    """Split a concatenated-pages bundle into one link per `Canonical page:` line.

    The page's title is the H1 just above that line, its notes the blockquote just below.
    """
    lines = text.splitlines()
    links = []
    for i, line in enumerate(lines):
        if not (match := CANONICAL_RE.match(line)):
            continue
        above = [l for l in lines[max(0, i - 3) : i] if l.startswith("# ")]
        below = [l for l in lines[i + 1 : i + 4] if l.startswith("> ")]
        url = match["url"]
        links.append(
            {
                "name": above[-1][2:].strip() if above else urlparse(url).path.strip("/") or url,
                "url": url,
                "notes": below[0][2:].strip() if below else "",
            }
        )
    return links


def expand_subcatalogs(links: list[dict]) -> tuple[list[dict], list[dict]]:
    """Replace each `.txt` sub-catalog link by the links it holds, one level deep.

    Returns (links, expanded). A sub-catalog that fails to fetch, or holds no
    links, stays in the list as a plain page.
    """
    subs = [l for l in links if link_kind(l["url"]) == "subcatalog"]

    def load(link: dict) -> list[dict]:
        try:
            text, _ = fetch(link["url"], fail=True)
        except SystemExit as err:
            print(f"WARN: sub-catalog not expanded: {err}", file=sys.stderr)
            return []
        link["warning"] = truncation_warning(text, link["url"])
        if sum(bool(CANONICAL_RE.match(l)) for l in text.splitlines()) >= 2:
            children, shape = parse_bundle(text), "bundle"
        else:
            children, shape = parse_llms_txt(text, link["url"])[2], "index"
        prefix = " / ".join(s for s in (link["section"], link["name"]) if s)
        for child in children:
            child["url"] = urljoin(link["url"], child["url"])
            child["section"] = " / ".join(s for s in (prefix, child.get("section", "")) if s)
            child["parent"] = link["url"]
        link["shape"] = shape
        return children

    with ThreadPoolExecutor(max_workers=8) as pool:
        children = dict(zip((id(l) for l in subs), pool.map(load, subs)))
    def same_page(url: str) -> str:  # `/a/b`, `/a/b/` and `/a/b.md` are one page
        parsed = urlparse(url)
        return parsed.netloc + re.sub(r"(\.mdx?)?/?$", "", parsed.path)

    out: list[dict] = []
    expanded = []
    seen = {same_page(l["url"]) for l in links}
    for link in links:
        kids = children.get(id(link))
        if kids:
            new = [k for k in kids if same_page(k["url"]) not in seen and not seen.add(same_page(k["url"]))]
            out += new
            expanded.append(
                {
                    "url": link["url"],
                    "name": link["name"],
                    "shape": link["shape"],
                    "links": len(new),
                    "duplicates": len(kids) - len(new),  # already listed elsewhere in the catalog
                    **({"warning": link["warning"]} if link.get("warning") else {}),
                }
            )
        else:
            out.append(link)
    for i, link in enumerate(out):
        link["id"] = i
        link["kind"] = "page" if link_kind(link["url"]) == "subcatalog" else link_kind(link["url"])
    return out, expanded


def catalog_appendix(links: list[dict], expanded: list[dict]) -> str:
    """The expanded sub-catalogs as llms.txt sections, appended to the snapshot so the hub sees them."""
    parts = []
    for sub in expanded:
        parts.append(f"\n## {sub['name']} (expanded from {sub['url']})\n")
        for link in links:
            if link.get("parent") == sub["url"]:
                notes = f": {link['notes']}" if link["notes"] else ""
                parts.append(f"- [{link['name']}]({link['url']}){notes}")
    return "\n".join(parts) + "\n" if parts else ""


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


def is_html(body: str, content_type: str) -> bool:
    return "html" in content_type or body.lstrip().lower().startswith(("<!doctype", "<html"))


def fetch_page(url: str) -> tuple[str, str]:
    """Fetch a page, preferring its markdown twin: `<url>.md` for links without an extension."""
    parsed = urlparse(url)
    if not re.search(r"\.\w{1,5}$", parsed.path):
        path = parsed.path.rstrip("/")
        md_url = parsed._replace(path=f"{path}.md" if path else "/index.md", query="", fragment="").geturl()
        try:
            body, content_type = fetch(md_url, fail=True)
            if not is_html(body, content_type):
                return body, content_type
        except SystemExit:
            pass
    return fetch(url)


def strip_mdx(markdown: str) -> str:
    """Drop MDX component tags outside code fences; a component's `title` survives as a bold line."""
    parts = re.split(r"(^```.*?^```[^\n]*$)", markdown, flags=re.M | re.S)
    for i in range(0, len(parts), 2):  # even parts are outside fences
        parts[i] = MDX_TAG_RE.sub(
            lambda m: f"**{t[1]}**" if (t := re.search(r'\btitle="([^"]+)"', m[0])) else "", parts[i]
        )
        parts[i] = re.sub(r"\n{3,}", "\n\n", parts[i])
    return "".join(parts)


def rel(path: Path, base: Path) -> str:
    """`path` relative to `base` when inside it, else absolute — `--output` may point anywhere."""
    return path.relative_to(base).as_posix() if path.is_relative_to(base) else path.as_posix()


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
    parser.add_argument("--output", default=None, help="Override the raw folder (default: raw/docs/llms-<slug>/).")
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
    warnings = [w for w in [truncation_warning(catalog, args.url)] if w]
    links, expanded = expand_subcatalogs(links)
    add_hints(links, keywords, phrases)
    page_slugs(links, args.url)

    parsed = urlparse(args.url)
    folder_slug = slugify(f"{parsed.netloc} {parsed.path.rsplit('/', 1)[0]}")
    folder = Path(args.output).expanduser().resolve() if args.output else wiki_dir / "raw" / "docs" / f"llms-{folder_slug}"
    for link in links:
        link["exists"] = (folder / f"{link['slug']}.md").exists()

    if args.list:
        out = {
            "title": title,
            "summary": summary,
            "keywords": keywords,
            "phrases": [" ".join(p) for p in phrases],
            "expanded": expanded,
            **({"warning": "; ".join(warnings)} if warnings else {}),
            "links": [
                {k: link[k] for k in ("id", "hint", "kind", "section", "name", "notes", "url", "exists")}
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
        not_pages = [f"{i} ({links[i]['kind']})" for i in ids if links[i]["kind"] != "page"]
        if not_pages:
            raise SystemExit(f"not pages, cannot be picked: {', '.join(not_pages)}")
        selected = [links[i] for i in ids]
    else:
        ranked = sorted((l for l in links if l["hint"] > 0 and l["kind"] == "page"), key=lambda l: -l["hint"])
        selected = ranked[: args.max_pages]
    if not selected:
        raise SystemExit(f"no links selected from {args.url} — nothing written; run --list and pass --pick")

    folder.mkdir(parents=True, exist_ok=True)
    (folder / "llms.txt").write_text(catalog.rstrip("\n") + "\n" + catalog_appendix(links, expanded), encoding="utf-8")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    pages = []
    for link in selected:
        path = folder / f"{link['slug']}.md"
        page = {
            "id": link["id"],
            "title": link["name"],
            "source_url": link["url"],
            "raw_path": rel(path, wiki_dir),
            "source_page": f"wiki/docs/{folder.name}/{link['slug']}.md",
        }
        pages.append(page)
        if link["exists"]:
            page["action"] = "skipped"
            continue
        try:
            body, content_type = fetch_page(link["url"])
        except SystemExit as err:
            print(f"WARN: {err}", file=sys.stderr)
            page.update(action="failed", reason=str(err))
            continue
        markdown, description = split_frontmatter(to_markdown(body, content_type, link["url"]))
        markdown = strip_mdx(markdown)
        notes = link["notes"] or description
        if len(markdown) < 200:
            # Usually a navigation page: a grid of cards or links with no prose of its own.
            page.update(action="failed", reason=f"body under 200 chars ({len(markdown)}) — likely a navigation page")
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
        # Pages from an llms.txt usually carry their own H1, sometimes under a short preamble; add one only if missing.
        if not re.search(r"^# ", "\n".join(markdown.splitlines()[:10]), re.M):
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
        "raw_path": rel(folder, wiki_dir) + "/",
        "catalog": rel(folder / "llms.txt", wiki_dir),
        "catalog_size": len(links),
        "hub_page": f"wiki/docs/{folder.name}/OVERVIEW.md",
        "pages": pages,
    }
    if not any(p["action"] in ("fetched", "skipped") for p in pages):
        raise SystemExit(f"every selected page failed for {args.url}: {json.dumps(pages, ensure_ascii=False)}")
    if not any(p["action"] == "fetched" for p in pages):
        warnings.append("no new pages fetched — every selected page is already in raw/")
        print(f"WARN: {warnings[-1]} ({args.url})", file=sys.stderr)
    if warnings:
        receipt["warning"] = "; ".join(warnings)
    print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
