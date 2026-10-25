# AGENTS.md

Instructions for coding agents working in this repository. Humans: see `README.md`.

## What this repo is

A collection of LLM-maintained knowledge wikis. Each `wiki-<NNN>-<slug>/` directory is
one independent wiki (an Obsidian vault plus an Open Knowledge Format bundle). All
wikis share a single skill, `my-llm-wiki`, kept at the repo root.

There is no application code. The only code is the skill's helper scripts.

## Layout

```
.agents/skills/my-llm-wiki/   # the skill — the single source of truth
  SKILL.md                    # entry point: Step 0 locate, Step 1 mode, ingest path
  CONVENTIONS.md              # data contract: layout, identity, links, write regimes
  PAGES.md                    # template + receipt for every page type
  SOURCES.md                  # adapter contract, routing table, adding an origin
  QUERY.md                    # query path Q.1–Q.8
  agents/                     # subagent prompts (docs selector; source/repo/docs/page/overview writers)
  scripts/                    # PEP 723 single-file Python scripts, run with uv
.claude/skills -> ../.agents/skills          # symlink, so Claude Code finds the skill
wiki-<NNN>-<slug>/
  .agents -> ../.agents                      # symlinks: each wiki can be opened alone
  .claude -> ../.claude
  log.md                                     # append-only history
  raw/                                       # immutable ingested artifacts
  wiki/                                      # LLM-written pages; index.md files are generated
```

## Working on a wiki

Use the `my-llm-wiki` skill for all ingest and query work, and follow
`.agents/skills/my-llm-wiki/SKILL.md` exactly. Read `CONVENTIONS.md` and `PAGES.md`
before the first write in a session, and `QUERY.md` before the first answer.

Run from the repo root (`--wiki-dir wiki-<NNN>-<slug>`) or from inside a wiki dir
(`--wiki-dir .`). The script paths are the same from both places, because of the
symlinks.

## Hard rules

- **Never edit `raw/`.** It is an immutable record of what was ingested.
- **Never hand-edit any `index.md`.** Regenerate it with `build_index_md.py`.
- **`log.md` is append-only**, with the oldest entry first.
- **Query mode never edits ingest-owned pages** (`sources/`, `entities/`,
  `concepts/`, `overview.md`, `repos/*/ARCHITECTURE.md`). Record problems in
  `wiki/open-questions.md` instead. See `CONVENTIONS.md` §13.
- **Entity/concept pages exist only at ≥2 distinct origins** (one repo or one
  docs set = one origin). Use `count_mentions.py` to get the count; never count
  by hand.
- **Never commit repo clones.** `wiki-*/raw/repos/` is gitignored.
- **Edit the skill only under `.agents/skills/my-llm-wiki/`.** Never replace a
  symlink with a copy.

## Commands

```bash
# rebuild indexes + OKF conformance check (non-zero exit on a page with no `type`)
uv run --script .agents/skills/my-llm-wiki/scripts/build_index_md.py --wiki-dir <wiki-dir>

# mention counts and the ≥2 qualifying list
uv run --script .agents/skills/my-llm-wiki/scripts/count_mentions.py --wiki-dir <wiki-dir>

# adapters
uv run --script .agents/skills/my-llm-wiki/scripts/fetch_article.py --url <url> --wiki-dir <wiki-dir>
uv run --script .agents/skills/my-llm-wiki/scripts/clone_repo.py --url <url> --wiki-dir <wiki-dir>
```

There is no test suite. After changing a script, run `build_index_md.py` and
`count_mentions.py` against an existing wiki and check that they exit 0.

## Adding a new wiki

Follow `SKILL.md` § "Step 0 — Locate the wiki" → "Creating a wiki". It creates the
directories and the `.gitkeep` files, and links `.agents` and `.claude` back to
the root. Number wikis sequentially: `wiki-001-…`, `wiki-002-…`.

## Symlinks

The repo depends on symlinks. On Windows, they require Developer Mode and
`git config core.symlinks true`. Create them with
`cmd //c 'mklink /D <link> <relative-target>'`. If a symlink comes back as a small
text file holding a path, it was checked out without symlink support: recreate it.
Do not commit it as a file.

## Commits

Make small, focused commits. Use Conventional Commits style (`feat:`, `fix:`,
`docs:`), with `wiki(<slug>):` for wiki content, e.g.
`wiki(001-software-factory): ingest 3 notes`.
