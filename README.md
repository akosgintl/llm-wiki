# llm-wiki

Knowledge wikis that an LLM writes, an LLM reads, and that learn from being used.

Drop in notes, articles or GitHub repos and an agent turns them into a linked
wiki of source, entity and concept pages. Ask it questions and the answers are
saved back as notes. Questions it can't answer become open questions. Every wiki
is a plain-markdown [Obsidian](https://obsidian.md) vault and an
[Open Knowledge Format](https://openknowledgeformat.org) v0.1 bundle.

## Wikis

| Wiki | Topic |
|---|---|
| [`wiki-001-software-factory`](wiki-001-software-factory/) | Software factory |

## How it works

- `raw/` holds **what was said**: verbatim copies of every ingested source, never edited.
- `wiki/` holds **what we know**: pages written by agents. An entity or concept
  page appears only once at least two independent sources mention it.
- Each raw file is read once, by one subagent. Everything after that works from
  the wiki pages. That keeps the cost per question flat as the wiki grows.
- Questions are logged under `wiki/questions/`. Answers built from several pages
  become `wiki/notes/`, and gaps go to `wiki/open-questions.md`.

The full contract is in [`.agents/skills/my-llm-wiki/`](.agents/skills/my-llm-wiki/SKILL.md).

## Requirements

- An agent harness that supports skills and subagents, e.g. [Claude Code](https://claude.com/claude-code)
- [`uv`](https://docs.astral.sh/uv/) (it installs the scripts' Python deps on first run)
- `git`, `curl`
- Obsidian (optional, for browsing and the graph view)

## Setup

The repo uses symlinks so that every wiki shares the root skill. Clone with
symlink support:

```bash
git clone -c core.symlinks=true <repo-url>
```

On **Windows**, turn on Developer Mode first (Settings → System → For
developers). Without it, the symlinks check out as small text files and the
skill is not found.

## Usage

Open the repo root, or any `wiki-*` directory on its own, in your agent and talk to it:

```text
ingest ~/notes/platform-engineering/
add https://github.com/owner/repo
add https://example.com/some-article
what does the wiki say about internal developer platforms?
how does <repo> handle retries?
```

The agent ingests when you use an explicit verb (*ingest, add, build, index*)
or drop in paths. Anything else is treated as a question. Then open
`wiki-<NNN>-<slug>/wiki/index.md` in Obsidian.

### Adding a wiki

Ask the agent to create one (e.g. "create wiki-002-<topic>"), or follow
`SKILL.md` → *Creating a wiki*. Each wiki gets `.agents` and `.claude`
symlinks back to the root.

## Repository layout

```
.agents/skills/my-llm-wiki/   shared skill: contracts, subagent prompts, scripts
.claude/skills                symlink to .agents/skills (Claude Code discovery)
wiki-<NNN>-<slug>/            one independent wiki
AGENTS.md                     instructions for coding agents
CLAUDE.md                     Claude Code entry point (imports AGENTS.md)
```

## License

[MIT](LICENSE)
