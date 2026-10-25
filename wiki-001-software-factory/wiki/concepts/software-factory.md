---
type: concept
title: Software factory
description: A system of coding agents, compute, environments and orchestration that turns work requests (issues, tickets, chat messages) into reviewed pull requests, with humans kept at key gates.
aliases: []
sources:
  - "[[wiki/sources/youtube-tGbjIvvYuHE]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
related:
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/control-plane]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/dev-environment]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/entities/warp-factories]]"
created: 2026-10-25T15:14:44Z
timestamp: 2026-10-25T18:00:00Z
source_count: 7
---

# Software factory

> Agents plus infrastructure that route work requests to reviewed pull requests, humans approving key steps.

## Definition

Two framings, both from vendors. Warp's docs define a factory as a team of cloud agents connected to your repositories. It routes work from Slack, GitHub, Linear or Jira through triage, planning, implementation and review, then returns a pull request to the originating thread. A "foreman" agent coordinates and is the only default agent that talks to humans. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]

The Boundary podcast frames it as a stack of layers: compute/infrastructure, dev environment, harness (inner and outer) and control plane/orchestration. Each layer can be built, bought or mixed, with composition over inheritance. [[wiki/sources/youtube-tGbjIvvYuHE]] Warp describes a product's agent team and intake; the podcast describes the layers beneath. They are complementary, not contradictory.

## Key claims

- Many entry points, one dispatcher: chat, forges, trackers, webhooks, REST, schedules and MCP all land with the foreman as a work item that keeps source context. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]
- Concretely, a Warp factory is a git repo of path-named Markdown and YAML: `factory.yaml`, agents, automations (triggers whose body is the task handed to the foreman), runners, scorers, skills. Exactly one agent is the foreman. Push, pass the `warp/factory-config` check, and it syncs. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Boundary's own factory ("agent tries BAML") uses MacBooks as compute, Claude Code or Codex headless as harness, hard-coded while loops as outer harness, and a hosted web app listening to Slack, Linear and GitHub as dispatcher. [[wiki/sources/youtube-tGbjIvvYuHE]]
- Humans keep merge. Warp: the factory never merges; spec approval is a default policy in the foreman's instructions, and the example foreman prompt says never to merge or approve a spec for a human. Boundary: a loop fixes CodeRabbit comments, stops after 3 iterations to ask a human, and a human presses merge. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]], [[wiki/sources/youtube-tGbjIvvYuHE]]
- Aim for 95% automatic, not fully automatic. [[wiki/sources/youtube-tGbjIvvYuHE]]
- Local and cloud work share one task: Factory MCP lets a local coding agent send work in, pull a task down in an isolated worktree, and hand it back. Tasks are not locked. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]
- Measurement is part of the design: Warp lists dashboards, scorers and benchmarks; the examples attach sampled LLM-judge scorers to agents; Boundary requires eval metrics with every pipeline change. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]], [[wiki/sources/youtube-tGbjIvvYuHE]]
- Factories are declared as definition files, optionally in a team GitHub repo with PR review. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Multi-repo: Warp groups repos that ship together into one factory; one branch and PR live in one repo, so the foreman opens one PR per repo and waits for all. The podcast instead simulates a monorepo from one coordination directory. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]], [[wiki/sources/youtube-tGbjIvvYuHE]]
- Harness is pluggable per agent: the Warp agent, Claude Code or Codex (example: Codex reviews Claude Code's work, so review does not share the implementer's blind spots). [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Agent behaviour is shared like packages: skills are pinned by lockfile hash and pushed to consumer repos by bot PRs; `migrate-to-factory` ports skills into a factory repo. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]

## Tensions

- Buy vs build. Dex argues vendor sandboxes add friction and teams should own the dev environment and pick layers freely; no open-source control plane exists. [[wiki/sources/youtube-tGbjIvvYuHE]] Warp offers a bundled hosted product (Warp-hosted compute by default, optional self-hosting, e.g. `workerHost`). [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Access control. Warp says instructions never change what an agent can do; access comes from configuration, yet Factory MCP has no read-only or per-factory scopes. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]

## Relationships

- **Human in the loop**: gates at spec and merge in both framings. [[wiki/concepts/human-in-the-loop]]
- **Control plane**: the podcast's dispatch, traces, scheduling, audit layer; the foreman plays a similar role. [[wiki/concepts/control-plane]]
- **Agent harness / dev environment**: lower layers of the podcast's stack. [[wiki/concepts/agent-harness]], [[wiki/concepts/dev-environment]]
- **MCP**: Factory MCP bridges local agents to the factory. [[wiki/concepts/mcp]]
- **Factory as code**: Warp's declarative definition files. [[wiki/concepts/factory-as-code]]

> Synthesis: Corroboration is thin. Six of seven sources are Warp's own voice (four docs pages plus two Warp-authored repos), so their agreement on human merge, one foreman and file-based config is one vendor repeated, not independent evidence. The only outside voice is the podcast (Human Layer, Boundary, also selling in this space); it agrees on human merge and one dispatcher, but nothing here shows the pattern works.
