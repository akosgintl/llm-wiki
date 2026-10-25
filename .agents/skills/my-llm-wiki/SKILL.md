---
name: my-llm-wiki
description: "Build and query an LLM-maintained wiki that learns from being used — questions, notes and repo answers land back in the graph (modes: ingest, query)."
---

# LLM Wiki — layer 03, interactive

You maintain a wiki that an LLM writes, an LLM reads, and — new in this layer —
that **learns from being used**. Layers 01 and 02 only grew when someone ingested
something. Here, asking it a question can leave the wiki better than it found it:
questions are logged, synthesized answers become notes, questions the wiki cannot
answer become open questions, and a question about an ingested repo produces a new
source-like page that flows through the same ingest tail as any source.

The discipline that makes this safe is **regime separation** (`CONVENTIONS.md`
§13): reading a source can never change what the wiki says that source means.

Four files carry the contract, and you follow them exactly:

- `CONVENTIONS.md` — layout, identity, threshold, links, log, OKF, write regimes.
- `PAGES.md` — the template and receipt for every page type.
- `SOURCES.md` — the adapter contract, the routing table, and how to add an origin.
- `QUERY.md` — the whole query path, Q.1–Q.8.

Read the first two before your first write in a session, and `QUERY.md` before
your first answer.

---

## Step 0 — Locate the wiki

**Working from inside a wiki.** If the current directory is itself named
`wiki-*` and contains both `raw/` and `wiki/`, that is the wiki — use it and skip
the glob. Every wiki dir carries `.agents/` and `.claude/` links to the root ones,
so the skill and its scripts resolve at the same relative paths from either place.
In every command below, `wiki-<slug>` then means `.` (e.g. `--wiki-dir .`).

Otherwise, glob `wiki-*/` in the project root and keep the ones that contain both
`raw/` and `wiki/`.

| Found | Do |
|---|---|
| exactly 1 | Use it. |
| more than 1 | Ask the user which one. |
| 0, ingest mode | Propose a slug from the topic of the incoming notes (kebab-case, e.g. `ai-engineering`), confirm it with the user, then create the wiki. |
| 0, query mode | Say there is no wiki yet and stop. Do not create one to answer a question. |

Creating a wiki:

```bash
mkdir -p wiki-<slug>/raw wiki-<slug>/wiki/sources wiki-<slug>/wiki/entities wiki-<slug>/wiki/concepts
printf '# Log\n' > wiki-<slug>/log.md
touch wiki-<slug>/raw/.gitkeep wiki-<slug>/wiki/sources/.gitkeep wiki-<slug>/wiki/entities/.gitkeep wiki-<slug>/wiki/concepts/.gitkeep
```

Then link the shared skill into it, so the wiki can be opened on its own. Use
relative symlinks (on Windows this needs Developer Mode and
`git config core.symlinks true`):

```bash
cmd //c 'mklink /D wiki-<slug>\.agents ..\.agents'    # Windows
cmd //c 'mklink /D wiki-<slug>\.claude ..\.claude'
ln -s ../.agents wiki-<slug>/.agents                   # macOS / Linux
ln -s ../.claude wiki-<slug>/.claude
```

## Step 1 — Detect mode

**Ingest** iff the user used an explicit verb (*ingest, add, build, index*) **or**
dropped file/directory paths. Everything else is **query**.

When it is ambiguous, choose **query**. Redirecting a query is cheap; a
mis-triggered ingest writes files the user did not ask for.

---

## Spawning subagents

Every page in this layer is written by a subagent defined in `agents/`. To spawn
one, whatever your harness calls it:

1. Read `agents/<name>.md`.
2. Pass its **entire body as the subagent's prompt**, followed by the inputs its
   Inputs table lists, as plain `key: value` lines.
3. Run it on a Sonnet-class model (or your provider's equivalent mid-tier model;
   fall back to the harness default). The agent file states its own preference.
4. Run them **in parallel** when your harness supports it, sequentially when it
   does not. The result is identical, only slower.
5. Expect **exactly one JSON receipt** back. If an agent returns prose instead,
   re-read the receipt shape in its file and re-run that one agent.

*(In Claude Code: the Task/Agent tool, one call per writer, several in one message
to run them concurrently.)*

Why this is the whole lesson: a raw file is read exactly **once**, by one
`source_writer`, and never enters your context or any other agent's. You see
receipts — a few hundred tokens each. `page_writer` reads only source pages;
`overview_writer` reads only frontmatter. That is why 50 sources cost about the
same orchestrator context as 5.

---

# Ingest path

You route and delegate. The only files you write yourself are `log.md` and the
report to the user.

### 1.0 Route each input

Match every input against the routing table in `SOURCES.md`, first match wins:

| Input | Origin | Raw artifact | Writer |
|---|---|---|---|
| an existing path on disk | `local` | `raw/<slug>.md` | `source_writer` |
| `github.com/<owner>/<repo>` or `*.git` | `repo` | `raw/repos/.github-<owner>-<repo>/` | `repo_writer` |
| `youtube.com/playlist?list=…` | `youtube` | `raw/youtube-<id>.md` per video | `fetch_youtube.py --list`, then `source_writer` per video |
| `youtube.com` / `youtu.be` | `youtube` | `raw/youtube-<slug>.md` | `source_writer` |
| URL path ends in `/llms.txt` | `llms-txt` | `raw/docs/llms-<set>/<page-slug>.md` | `docs_selector`, then `source_writer` per page + `docs_writer` |
| any other `http(s)://` | `article` | `raw/article-<slug>.md` | `source_writer` |

The YouTube slug is the video id, verbatim (`raw/youtube-<id>.md`). If the adapter
fails (no captions, private video), report the failure plainly and continue with
the other inputs. A playlist expands into its videos first; each video is then an
input of its own, deduped by its own raw path (`SOURCES.md` § youtube playlist).

### 1.1 Collect inputs and dedup

Expand every path the user gave you:

- a directory → **recursively every `*.md` inside it**. An `assets/` folder is not
  a list of inputs — nothing inside it becomes a source. Its files travel later,
  in 1.2, as attachments of the notes that embed them.
- a file → itself.

For each input compute its raw path from the routing table — for a local note
`raw/<slug>.md`, where `<slug>` is the **filename stem**, slugified: lowercase,
every run of non-alphanumeric characters collapsed to a single `-`,
leading/trailing `-` stripped, truncated to 60 characters at a `-` boundary. The
adapters derive their own slugs the same way, from the URL's last path segment or
from `<owner>-<repo>`.

Then split the inputs (this is the whole of dedup — see `CONVENTIONS.md` §4):

```bash
ls wiki-<slug>/raw/ wiki-<slug>/raw/docs/ wiki-<slug>/raw/repos/    # everything already ingested, by identity
```

- raw path exists → **skipped**. Report the input by name plus the
  `original_path` recorded on its existing page. If the incoming file differs in
  content from `raw/`, say so explicitly and still skip.
- raw path free → **new**.
- **repo that already exists → refreshed, not skipped** (`CONVENTIONS.md` §7).
- **llms.txt already held → never skipped as a whole.** Dedup is per page, inside
  the script: picked pages already in `raw/docs/llms-<set>/` come back `skipped`.

There is **no cap in this layer.** Layer 01 capped a run at 10 notes because one
context had to hold all of them; here each raw file is read by its own subagent
and you only ever see receipts. Do sanity-check the count with the user before
spawning 50 agents, and batch them in groups your harness can actually run.

### 1.2 Run the adapter for each new input

One adapter call per input, per the recipes in `SOURCES.md`:

```bash
# local — the note, then the attachments it embeds (see CONVENTIONS.md §4)
cp "<input path>" "wiki-<slug>/raw/<slug>.md"
mkdir -p "wiki-<slug>/raw/assets"
cp "<dir of the input note>/assets/<embedded file>" "wiki-<slug>/raw/assets/"   # skip if it exists

# article
uv run --script .agents/skills/my-llm-wiki/scripts/fetch_article.py \
  --url "<url>" --wiki-dir wiki-<slug>

# llms.txt — spawn agents/docs_selector.md first; it returns the ids to fetch
uv run --script .agents/skills/my-llm-wiki/scripts/fetch_llms_txt.py \
  --url "<url>" --wiki-dir wiki-<slug> --pick <ids>

# repo
uv run --script .agents/skills/my-llm-wiki/scripts/clone_repo.py \
  --url "<url>" --wiki-dir wiki-<slug>
```

Keep each receipt — the writers need `original_path`, `title`, `source_url`,
`authors`, `published_date`, and for repos `clone_path`, `commit_sha`, `branch`.
If an article receipt carries a `warning`, surface it and do not write a source
page from a paywall stub.

### 1.3 Spawn one writer per new raw artifact

List the existing pages once, and pass them to every writer so they reuse
canonical slugs instead of inventing near-duplicates:

```bash
ls wiki-<slug>/wiki/entities wiki-<slug>/wiki/concepts
```

- **File artifacts** → one `agents/source_writer.md` per raw file, in parallel.
  An llms.txt receipt lists several: one writer per page with `action: fetched`,
  output at that page's `source_page` — plus one `agents/docs_writer.md` for the
  receipt's `hub_page`, spawned with them (it reads only the catalog).
- **Repos** → one `agents/repo_writer.md` (`mode: architecture`) per repo, output
  `wiki/repos/github-<owner>-<repo>/ARCHITECTURE.md`.

Collect the receipts. Union of `entities_referenced` and `concepts_referenced`
across them is your "touched slugs" set for the tail. Do not read the pages the
writers produced — the receipt is the interface.

### 1.4 Ingest tail — entity and concept pages

```bash
uv run --script .agents/skills/my-llm-wiki/scripts/count_mentions.py --wiki-dir wiki-<slug>
```

The `qualifying` lists are the slugs at ≥2 distinct **origins** — counted across
`wiki/sources/`, `wiki/repos/*/` and `wiki/docs/*/`, where one repo or one docs
set is a single origin however many pages it has (`CONVENTIONS.md` §3). A repo
can be one of the two witnesses that materialize a concept, never both.

Spawn one `agents/page_writer.md` per qualifying slug **that one of this run's new
pages touched**, in parallel, passing the `source_pages` the script listed for that
slug. A slug that was already qualifying and that no new page mentions has not
changed — leave it alone.

### 1.5 Rewrite the overview

Spawn `agents/overview_writer.md` with the `count_mentions.py` output. It walks
frontmatter and reads at most 5 full pages.

### 1.6 Rebuild the index

```bash
uv run --script .agents/skills/my-llm-wiki/scripts/build_index_md.py --wiki-dir wiki-<slug>
```

Fix anything it reports as an `ERROR:` (a page with no `type`) before moving on.

### 1.7 Append to the log

```markdown
## <YYYY-MM-DD> ingest | <what came in>

- Ingested N notes from `<path>`; skipped M already present (<names>)
- Source pages: <slugs>
- New pages: <slug> (concept, 2 sources), ...
- Updated pages: <slug> (2 → 3 sources), ...
- Waiting at 1 mention: <slug>, <slug>
```

### 1.7b Check the open questions

If `wiki/open-questions.md` exists, read it and add **one bullet** to your report
naming any open questions the new sources appear to address. Do not edit the file
and do not mark anything resolved — a human decides whether an answer landed, and
the open question stays until they say so.

### 1.8 Report back

New, skipped and refreshed counts by origin, the pages your agents wrote, the wiki
path, and one line telling the user to open `wiki-<slug>/wiki/index.md` in
Obsidian. If any slug is sitting
at exactly 1 mention, name a couple — that is the wiki's own to-do list.

---

# Query path — see `QUERY.md`

When Step 1 selects query mode, **read `QUERY.md` now and follow it**; the rest of
this file is ingest-only. It covers Q.1 locate, Q.2 load the index, Q.3 the
disclosure ladder, Q.4 classify the question, Q.5 the general path and its
save-back rules, Q.6 the repo path (including the ingest tail a repo note must run
through), Q.7 open questions, and Q.8 log and present.

The one-line summary: **always write the slim question page; write a note only when
the answer cited ≥2 wiki pages or the user asked you to; never edit an
ingest-owned page.**

---

## Harness notes

This skill is written for any agent harness. It needs five capabilities:

| Capability | Used for |
|---|---|
| read a file | raw notes, wiki pages |
| write a file | every page you create |
| run a shell command | `cp`, `ls`, `mkdir`, the scripts |
| ask the user | the wiki slug, which wiki to use |
| spawn a subagent | every page written in this layer |

In Claude Code those are `Read`, `Write`, `Bash`, `AskUserQuestion` and the
Task/Agent tool. Nothing in this skill pins a model or a tool name — the agent
files state a model *preference* in prose, and any harness that can run a
sub-conversation with a prompt can run them.

## Agent reference

Read the file, pass its body as the prompt, collect one JSON receipt.

| Agent | Reads | Writes |
|---|---|---|
| `agents/docs_selector.md` | one llms.txt catalog, via `fetch_llms_txt.py --list` | nothing — returns the link ids to fetch |
| `agents/docs_writer.md` | one catalog snapshot `raw/docs/llms-<set>/llms.txt` | one `wiki/docs/llms-<set>/OVERVIEW.md` hub |
| `agents/source_writer.md` | one `raw/` file — the only agent that may | one `wiki/sources/<slug>.md` |
| `agents/repo_writer.md` | one clone under `raw/repos/` | one page under `wiki/repos/<repo>/` |
| `agents/page_writer.md` | the source-like pages for one slug | one `wiki/entities/` or `wiki/concepts/` page |
| `agents/overview_writer.md` | frontmatter, plus ≤5 full pages | `wiki/overview.md` |
| `agents/repo_writer.md` (`mode: question`) | one clone, plus the repo's `ARCHITECTURE.md` | one `wiki/repos/<repo>/<question-slug>.md` — **wired up in this layer** (`QUERY.md` Q.6) |

## Script reference

All six scripts are PEP 723 single files — `uv` installs their dependencies on
the first run. You run them; the user never does. Paths below are relative to the layer directory.

| Script | Call | Does |
|---|---|---|
| `scripts/count_mentions.py` | `uv run --script .agents/skills/my-llm-wiki/scripts/count_mentions.py --wiki-dir wiki-<slug>` | Frontmatter walk over source-like pages → `{slug: [pages]}` + the `qualifying` list at ≥2. JSON on stdout, table on stderr. |
| `scripts/build_index_md.py` | `uv run --script .agents/skills/my-llm-wiki/scripts/build_index_md.py --wiki-dir wiki-<slug>` | Regenerates `wiki/index.md` and each `wiki/<subdir>/index.md` from frontmatter, then checks OKF conformance. Deterministic: same input, same bytes. |
| `scripts/clone_repo.py` | `--url <url> --wiki-dir wiki-<slug>` | Shallow-clones into `raw/repos/.github-<owner>-<repo>/`, or refreshes it. JSON receipt with `commit_sha` and `action`. |
| `scripts/fetch_article.py` | `--url <url> --wiki-dir wiki-<slug>` | `curl` → body isolation → markdown at `raw/article-<slug>.md`. Warns when the body looks like a paywall. |
| `scripts/fetch_llms_txt.py` | `--url <url> --wiki-dir wiki-<slug> (--list \| --pick <ids>) [--keywords a,b]` | `--list` prints the catalog with ids and keyword hints, writes nothing. `--pick` fetches those links, one `raw/docs/llms-<set>/<page>.md` each; already-present pages are skipped. The receipt names each page's `source_page` and the set's `hub_page`. |
| `scripts/fetch_youtube.py` | `--url <url> --wiki-dir wiki-<slug> [--list [--limit N]]` | yt-dlp metadata + caption track → timestamped markdown at `raw/youtube-<id>.md`. Fails when the video has no captions. `--list` expands a playlist into its videos with a `new`/`skipped`/`unavailable` status each, and writes nothing. |

No script writes wiki content. They fetch, they count, they render — every word in
`wiki/` is written by an agent.
