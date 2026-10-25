# SOURCES — the adapter contract

Layer 01 could ingest exactly one thing: a markdown file already on disk. This
layer can ingest anything, and the reason is a contract three lines long.

Everything downstream of `raw/` — source pages, the ≥2 threshold, entity and
concept pages, the overview, the index — is **origin-agnostic**. It never learns
where a source came from. That is what makes adding an origin cheap.

---

## The adapter contract

> **Input**: one URI.
> **Output**: exactly one artifact under `raw/`, plus one JSON receipt on stdout.

```json
{
  "origin": "local | article | llms-txt | youtube | repo",
  "original_path": "<the URI as given — provenance, §2.4 of CONVENTIONS.md>",
  "title": "<human title>",
  "source_url": "<url, or null for local files>",
  "authors": [],
  "published_date": "<ISO-8601, or null>",
  "raw_path": "raw/<...>"
}
```

Every adapter script emits all seven keys, plus its origin-specific extras (`subtitle`, `chars`, `pages`, `commit_sha`, …). `raw_path` is relative to
the wiki dir, always with `/`, and ends in `/` when the artifact is a directory.
A repo has no byline or publish date: `authors` is `[<owner>]` and
`published_date` is the HEAD commit's date. llms-txt leaves both empty at the
catalog level.

Every script takes the same core flags: `--url <uri> --wiki-dir <dir>`, plus
`--output <path>` to override the default raw path. Exit codes follow one rule:

- **exit 1, message on stderr**: nothing usable was written (fetch failed, no
  body, no captions, no page selected).
- **exit 0 with `"warning"` in the receipt** (also echoed on stderr): an artifact
  was written but looks wrong, or nothing new was needed. Read the warning before
  you spawn a writer.

Two shapes of adapter, distinguished only by what they leave on disk:

| Shape | Raw artifact | Read by |
|---|---|---|
| **File adapter** — local, article, youtube | one markdown file (plus, for local notes, the attachments it embeds → `raw/assets/`) | `agents/source_writer.md` |
| **Catalog adapter** — llms-txt | one directory of markdown files, one per selected page | `agents/source_writer.md`, once per file |
| **Tree adapter** — repo | one directory | `agents/repo_writer.md` |

The rest of the pipeline sees a page under `wiki/sources/` or `wiki/repos/`, and
both kinds carry the same frontmatter contract (`entities:`, `concepts:`), so both
feed the threshold identically.

## Routing table

Match the user's input top to bottom; first match wins.

| Input pattern | Adapter | Raw path | Writer |
|---|---|---|---|
| a path that exists on disk | `cp` | `raw/<slug>.md` | `source_writer` |
| `github.com/<owner>/<repo>`, or any `*.git` | `scripts/clone_repo.py` | `raw/repos/.github-<owner>-<repo>/` | `repo_writer` (mode `architecture`) |
| `youtube.com/playlist?list=…` | `scripts/fetch_youtube.py --list`, then the video recipe per `new` video | `raw/youtube-<id>.md` per video | `source_writer` per video |
| `youtube.com/watch?v=…`, `youtu.be/…` | `scripts/fetch_youtube.py` | `raw/youtube-<slug>.md` | `source_writer` |
| a URL whose path ends in `/llms.txt` | `docs_selector`, then `scripts/fetch_llms_txt.py --pick` | `raw/docs/llms-<set>/<page-slug>.md` | `source_writer` per page, plus `docs_writer` for the hub |
| any other `http(s)://` | `scripts/fetch_article.py` | `raw/article-<slug>.md` | `source_writer` |

Dedup happens **before** the adapter runs: compute the raw path, `ls` it, skip if
it exists (CONVENTIONS.md §4). Repos are the exception — they refresh.

## Per-origin recipes

**local** — no script needed. Copy the note, then the files it embeds; the
attachments land beside it so the embeds keep resolving (`CONVENTIONS.md` §4).

```bash
cp "<input path>" "wiki-<slug>/raw/<slug>.md"
mkdir -p "wiki-<slug>/raw/assets"
cp "<dir of the input note>/assets/<embedded file>" "wiki-<slug>/raw/assets/"
```

**article** — `curl` with a browser user agent, isolate the body, markdownify.

```bash
uv run --script <skill>/scripts/fetch_article.py --url "<url>" --wiki-dir wiki-<slug>
```

If the receipt carries `"warning": "body under 500 chars…"`, **stop and tell the
user**: you hit a paywall, a bot wall, or an unmatched body selector. Writing a
source page from 300 characters of cookie banner is worse than not ingesting.

**llms-txt** — a catalog, not a document. Select by judgment, then fetch only
the picks, one raw file per page.

1. Spawn `agents/docs_selector.md` with the catalog URL, the wiki dir, the
   overview's `description`, the existing entity/concept slugs, the user's words
   about what they want, and a `budget` (default 10). It runs `--list` itself and
   returns `pick: [ids]`.
2. Fetch the picks:

   ```bash
   uv run --script <skill>/scripts/fetch_llms_txt.py --url "<url>" --wiki-dir wiki-<NNN>-<slug> \
     --pick <ids from the selector>
   ```

3. One `source_writer` per page whose `action` is `fetched`, with
   `origin: llms-txt`, the page's own `source_url` and `title` as metadata, and
   its `source_page` (`wiki/docs/llms-<set>/<page-slug>.md`) as output.
4. One `agents/docs_writer.md` for the set's hub, the receipt's `hub_page`: a map
   of the whole catalog, so a later question can fetch what ingest skipped
   (`CONVENTIONS.md` §15, `QUERY.md` Q.6b).

**Why an agent picks, not the script.** `--list` prints a keyword `hint` per link:
the wiki slug plus `--keywords`, IDF-weighted over the catalog (so "software" in a
dev-docs site is worth almost nothing), doubled in the link name, plus a bonus
when a whole phrase ("software factory") appears adjacent. It finds the obvious
links. It cannot find the right ones: docs a `software-factory` wiki wants talk
about agents, CI and code generation, not "software factories". Embeddings would
close part of that gap at the cost of a model dependency in a repo that has
none; the harness is already an LLM, so the selector reads titles and notes and
judges. Without `--pick`, the script fetches the top `--max-pages` by hint — a
fallback, not the path.

**Catalogs are not always flat.** A `.txt` link is fetched and expanded in
place, one level deep: a nested index (docs.port.io's `guides.txt`) gives its
links; a bundle of concatenated pages, each under a `Canonical page:` line
(docs.warp.dev's `_llms-txt/*.txt`), gives one link per page. Pages listed twice
(`/a/b` and `/a/b.md`) keep the first. Full-docs dumps (`llms-full.txt`) and API
specs (`.json`, `.yaml`) are listed as `kind: dump` / `spec` and cannot be
picked. A page link with no extension is fetched as `<url>.md` first, the HTML
page only if that fails; MDX component tags are stripped from the body.

**Identity is per page**, `raw/docs/llms-<set>/<page-slug>.md`, with the page
slug from the link's URL path. A second run against the same catalog — a bigger
budget, a new intent — fetches only the new picks and reports the rest
`skipped`. `llms.txt` in the same folder is a snapshot of the catalog, with
expanded sub-catalogs appended as extra `##` sections, overwritten on every run.
It is not a source; only `docs_writer` reads it, to map the whole set.

**repo** — shallow clone, then a different writer.

```bash
uv run --script <skill>/scripts/clone_repo.py --url "<url>" --wiki-dir wiki-<slug>
```

The receipt's `action` is `cloned` or `updated`. Pass `clone_path`, `commit_sha`,
`branch`, `owner` and `repo` straight to `repo_writer`.

**youtube** — yt-dlp reads the metadata and the caption track; no media is
downloaded. The raw file is split into `## <m:ss>` sections, so a source page can
cite `[[raw/youtube-<id>#12:30|cite]]`. The slug is the video id, verbatim.

```bash
uv run --script <skill>/scripts/fetch_youtube.py --url "<url>" --wiki-dir wiki-<slug>
```

Manual subtitles win over auto-captions; pass `--lang` for a language other than
`en`. The receipt adds `video_id`, `channel`, `duration` and `transcript`
(`manual-en`, `auto-en`, …). A video with no captions fails with a non-zero exit.

**youtube playlist** — a list of videos, not a source. Expand it, then ingest each
video exactly as above.

```bash
uv run --script <skill>/scripts/fetch_youtube.py --url "<playlist url>" --wiki-dir wiki-<slug> --list [--limit N]
```

The listing writes nothing. Each video carries `status`: `new` (fetch it),
`skipped` (`raw/youtube-<id>.md` exists) or `unavailable` (private or deleted).
Confirm the `new` count with the user before fetching, then run the video recipe
once per `new` video with its `url`, and one `source_writer` per transcript.
Identity stays per video, so re-ingesting a playlist only adds what is new, and
a video reached through two playlists is ingested once.

A `watch?v=…&list=…` URL is a video that happens to sit in a playlist: it routes
to the single video. Ingest the whole playlist only when the user says so.

## How to add a source — worked on YouTube

Three steps. Nothing outside this list changes.

1. **Write `scripts/fetch_<origin>.py`** honoring the contract above: one URI in,
   one raw artifact plus one receipt out. Decide the **identity** first — the raw
   path must be derivable from the URI alone and must not change when the title
   does. For YouTube that is the video id, not the title.
2. **Add one row to the routing table** in this file, and one line to Step 1.0 in
   `SKILL.md`.
3. **Pick the writer.** A markdown file → `source_writer`, unchanged. A directory
   or a fundamentally different artifact → a new agent modelled on
   `repo_writer.md`, emitting the same receipt shape.

That is the whole extension surface. The threshold, the page contracts, the index
and the log never learn that a new origin exists.

### What other origins would need

Described, not built — this is the design exercise, and the hard column is always
identity, never fetching.

| Origin | Fetch mechanism | Identity | The part that bites |
|---|---|---|---|
| **YouTube** | `youtube-transcript-api`, `yt-dlp --write-auto-sub`, or the Data API | video id | Auto-captions have no punctuation and no headings, so citations have nothing to anchor to — timestamped sections are the fix. |
| **X / Twitter** | official API (paid) or an export | tweet id; a thread is one source, not N | Deciding the unit: a thread reads as one document, but replies arrive later and change it. |
| **LinkedIn** | no usable API; a data export or manual paste | post URN | Terms of service, and posts that are edited in place under a stable URL. |
| **Reddit** | public JSON (`<url>.json`) | permalink id | The comments *are* the content — flatten the tree, or the source page cites nothing. |
| **Readwise** | Reader API | document id | Highlights are a partial view; the raw file is honestly incomplete and the source page should say so. |
| **Obsidian vault** | filesystem walk | vault-relative path | It already works — it is the `local` adapter — but embeds (`![[…]]`) and `[[wikilinks]]` point at files you did not ingest. |
| **PDF** | `pymupdf` / `pdftotext` | file hash or DOI | Scanned PDFs need OCR, and page numbers are the only citation anchor you get. |

The pattern across all of them: **fetching is a weekend; identity is the design
decision.** Pick a raw path that is stable under re-fetch and unique per source,
and the rest of the pipeline stays honest.
