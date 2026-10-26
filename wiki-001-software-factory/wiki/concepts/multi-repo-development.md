---
type: concept
title: Multi-repo development
description: Working with agents across several repositories at once, by grouping repos into one factory, opening one PR per repo, sharing skills across repos, or simulating a monorepo from a coordination directory.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
  - "[[wiki/sources/youtube-tGbjIvvYuHE]]"
  - "[[wiki/sources/youtube-b5O6gb_Zuk8]]"
related:
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/dev-environment]]"
  - "[[wiki/concepts/control-plane]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/git-worktree]]"
  - "[[wiki/entities/warp-factories]]"
created: 2026-10-25T15:14:39Z
timestamp: 2026-10-26T07:15:24Z
source_count: 5
---

# Multi-repo development

> Multiple framings, at factory, change and session level: group repos into a unit of work, ship one PR per repo, share skills across repos, or fake a monorepo.

## Definition

Four framings appear, at different levels. Warp's docs treat it as a sizing question: repositories that ship together belong in one factory, separate products get separate factories, and specialization comes from custom agents and skills, not from splitting repos by team. [[wiki/docs/llms-docs-warp-dev/factories]]

The Warp example definitions show the mechanics: a factory declares its repositories in `factory.yaml` (example 02 lists several, including a web app and an iOS app), and the foreman coordinates work that spans them. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

The `common-skills` repo shows a third level: sharing agent behaviour across repos. Skills live in one library, are pinned by lockfile in each consumer repo, and a CI workflow opens lockfile PRs downstream on every merge. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]

The Boundary podcast treats it as a session-level technique: simulate a monorepo by running sessions from one coordination directory that tells the model where the other repos are. [[wiki/sources/youtube-tGbjIvvYuHE]] A second Boundary episode gives the Claude Code recipe: a coordination repo whose `settings.json` lists additional directories and whose CLAUDE.md describes each repo, with per-task worktrees; a true mono repo is simplest if you can have one. [[wiki/sources/youtube-b5O6gb_Zuk8]]

These are complementary, not conflicting: one decides which repos a factory owns, one how changes land, one how behaviour is shared, one how an agent navigates them.

## Key claims

- A factory is connected to a declared set of repositories; repos, agents, automations, runners, skills and MCP servers live in definition files. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Group repos that ship together into one factory; separate products into separate factories. [[wiki/docs/llms-docs-warp-dev/factories]]
- One branch and PR live in one repository, so a multi-repo change needs one PR per repo; the foreman waits for all PRs before hand-off. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- A shared skill library can be pinned per consumer repo by `skills-lock.json` and propagated by bot PRs (auto-squash-merged once checks pass) to repos such as `warp` and `warp-server`. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- Simulate a monorepo with a coordination directory that points the model at the other repos. [[wiki/sources/youtube-tGbjIvvYuHE]]
- Avoid git submodules for this; subtrees are possibly better (stated tentatively). [[wiki/sources/youtube-tGbjIvvYuHE]]
- Preferred order for many repos: mono repo first; otherwise a coordination repo whose `settings.json` lists additional directories and whose CLAUDE.md describes each repo, with per-task worktrees. [[wiki/sources/youtube-b5O6gb_Zuk8]]
- Git submodules and symlinks are unergonomic for models. [[wiki/sources/youtube-b5O6gb_Zuk8]]
- Prefer fewer, prescriptive team-wide workflows over many personal skills ("lift the median"), which bears on sharing config across repos. [[wiki/sources/youtube-b5O6gb_Zuk8]]

## Tensions

Mild, not a direct contradiction. Warp's tooling makes the repo set a declared property of the factory and keeps each PR repo-local. Boundary's approach is an ad hoc directory convention inside a session, with no declared repo set. Neither source argues against the other. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/sources/youtube-tGbjIvvYuHE]]

Within the podcast pair, the stance on submodules is consistent (avoid), but they differ on the alternative: the factory episode floats subtrees tentatively, while the harness episode names a mono repo or a coordination repo with worktrees and also rejects symlinks. [[wiki/sources/youtube-tGbjIvvYuHE]], [[wiki/sources/youtube-b5O6gb_Zuk8]]

## Relationships

- **software-factory**: multi-repo scope is a design choice of any factory. [[wiki/concepts/software-factory]]
- **dev-environment**: the environment must give the agent access to all the repos it needs. [[wiki/concepts/dev-environment]]
- **control-plane**: dispatch and coordination across repos sit here (the foreman, in Warp's case). [[wiki/concepts/control-plane]]
- **factory-as-code**: the repo set is declared in files. [[wiki/concepts/factory-as-code]]
- **agent-skill**: skills are the unit shared across repos. [[wiki/concepts/agent-skill]]
- **git-worktree**: per-task worktrees isolate parallel work inside a coordination repo. [[wiki/concepts/git-worktree]], [[wiki/sources/youtube-b5O6gb_Zuk8]]
- **warp-factories**: the vendor implementation with the repo-grouping guidance. [[wiki/entities/warp-factories]]

> Synthesis: Three of the five sources are one vendor voice (Warp: the docs set, `warp-factory-examples`, `common-skills`), so their agreement on repo grouping and per-repo PRs is not independent corroboration; the examples repo largely illustrates what the docs state. The two outside sources are episodes of the same Boundary and Human Layer podcast with the same hosts, so their shared advice (avoid submodules, use a coordination directory) is one voice, not two; they address session layout, not factory sizing, and the speakers sell competing tooling.
