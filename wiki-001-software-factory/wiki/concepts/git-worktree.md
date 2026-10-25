---
type: concept
title: Git worktree
description: Git feature that gives each concurrent agent task its own checkout and branch from one shared object store, used by Warp's Direct backend and Factory's droid exec for parallel-run isolation, but not a security boundary.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-factory-com/droid-exec-overview]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]]"
related:
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/concepts/agent-runner]]"
  - "[[wiki/concepts/secrets-management]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/mcp]]"
created: 2026-10-25T18:30:11Z
timestamp: 2026-10-25T18:30:11Z
source_count: 4
---

# Git worktree

> Two origins: Warp docs (three pages, one voice) and Factory docs (one page).

## Definition

A Git worktree is an extra working directory and branch linked to one repository, sharing its object store. In these sources it is the isolation unit for parallel agent runs: each task gets its own files and branch, and no full clone per run. Both vendors use it for the same purpose, but at different layers. Warp uses it inside a self-hosted runner's setup and teardown hooks. Factory exposes it as a CLI flag. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]], [[wiki/docs/llms-docs-factory-com/droid-exec-overview]]

## Key claims

- Warp's recipe: a `--no-checkout` base clone, a `setup_command` that adds a worktree at `OZ_WORKSPACE_ROOT/repo` on branch `warp-agent/<OZ_RUN_ID>`, and a `teardown_command` that removes worktree and branch. Hooks are wired in `worker.yaml` with `max_concurrent_tasks`. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]
- The Direct backend docs point to this pattern for large monorepos. They describe per-task workspace directories, with `target_dir` disabling isolation by sharing one directory. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]]
- The worktree must be a child of the workspace dir, because the worker already created that directory and a temp env file in it. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]
- The `oz` CLI starts in `OZ_WORKSPACE_ROOT`, not the worktree, so prompts must keep repo edits under `repo/`. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]
- Fetch runs outside the setup hook so concurrent tasks do not update the same remote-tracking refs. Both hooks run `git worktree prune` to recover from interrupted tasks. Teardown deletes only the local branch. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]
- Factory: `-w, --worktree` runs each `droid exec` job in an isolated worktree so parallel runs avoid file conflicts. Clean worktrees are removed on exit; dirty ones are kept. [[wiki/docs/llms-docs-factory-com/droid-exec-overview]]
- Warp Factory MCP: `get_task` with `start_working=true` returns suggested Git commands for an isolated worktree, so a developer or local agent can continue a cloud task. It never modifies local files. Picking up a task does not lock it. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]
- Security limit: worktrees isolate files and branches, not the host. Direct tasks share filesystem, network, processes and object store; the Direct backend gives no container isolation. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]]
- Git credentials: Direct sets `GIT_CONFIG_GLOBAL` to a task-local file, so credentials must come from an SSH key, a system helper, or the base clone's config. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]

## Connections

- **Self-hosting**: the Direct backend is where Warp's worktree recipe lives. [[wiki/concepts/self-hosting]]
- **Agent runner**: worktree creation is a runner-side hook, not a harness feature. [[wiki/concepts/agent-runner]]
- **Secrets management**: credential handling differs per task because of the task-local Git config. [[wiki/concepts/secrets-management]]
- **Agent harness**: Factory's `droid exec` harness offers the flag directly. [[wiki/concepts/agent-harness]]
- **MCP**: Factory MCP hands cloud tasks to local worktrees. [[wiki/concepts/mcp]]

## Tensions

Where the worktree is created differs. Warp has the operator script it in runner hooks and warns the agent will not start inside it. Factory builds it into the harness as a flag with automatic cleanup of clean trees. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]], [[wiki/docs/llms-docs-factory-com/droid-exec-overview]]

Cleanup differs too. Factory keeps dirty worktrees; Warp's teardown removes the worktree and branch unless `--no-cleanup` is set. [[wiki/docs/llms-docs-factory-com/droid-exec-overview]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]

> Synthesis: Four pages, two vendors. The three Warp pages are one voice, so their agreement is not corroboration. Factory independently confirms only the core idea: worktrees give cheap per-run isolation for parallel agents. Both are vendor docs, and only Warp states the limit that worktrees are not a host boundary.
