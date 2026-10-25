---
type: overview
title: 001-software-factory — Overview
description: "Notes on building a \"software factory\" for AI coding agents, drawn from a Boundary podcast, the Warp Factories documentation and two Warp repositories."
created: 2026-10-25T14:35:38Z
timestamp: 2026-10-25T16:00:00Z
total_sources: 55
total_pages: 75
---

# 001-software-factory — Overview

The wiki has four origins: one podcast, one documentation set and two repositories. Three of the four are Warp's own voice (the docs and both repos). Only the podcast is independent. Most corroboration here is single-vendor: when a concept is cited by the docs and a Warp repo, that is Warp agreeing with Warp. Treat the podcast as the one outside check.

- Podcast: [[wiki/sources/youtube-tGbjIvvYuHE]] ("How to Build a Software Factory for AI Coding Agents", Dex of Human Layer and Vaibhav of Boundary). It supplies the layering and buy-or-build argument.
- Warp docs: 52 ingested pages under `wiki/docs/llms-docs-warp-dev/`, counted as one origin. Start with the map: [[wiki/docs/llms-docs-warp-dev/OVERVIEW]].
- Warp repos: see Repos below.

## Themes

**The factory and its layers.** The podcast splits a factory into compute, dev environment, harness and control plane. Warp's docs describe the same shape as a product, and the examples repo expresses it as files. See [[wiki/concepts/software-factory]], [[wiki/concepts/dev-environment]] and [[wiki/concepts/control-plane]]. Strongest sources: [[wiki/sources/youtube-tGbjIvvYuHE]] and [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]].

**The factory as versioned files.** Warp declares a factory as YAML and Markdown rooted at `factory.yaml`, with a foreman agent coordinating stage agents and shared skills. This is the most-cited Warp idea (about 30 docs pages plus both repos) and has no podcast voice. See [[wiki/concepts/factory-as-code]], [[wiki/concepts/foreman-agent]] and [[wiki/concepts/agent-skill]]. Strongest sources: [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]] and [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]].

**The harness and swappable agents.** The inner harness is the coding agent, the outer harness is the workflow code around it. Warp exposes the harness as a per-agent setting, so [[wiki/entities/claude-code]] and [[wiki/entities/codex]] sit side by side. See [[wiki/concepts/agent-harness]]. Strongest sources: [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]] and the podcast.

**Measuring agents and keeping people at the gates.** Evals (LLM-judge scoring, fixed-task benchmarks) are how a pipeline changes safely, and humans approve specs, merges and escalations. Both are cited by all four origins. See [[wiki/concepts/agent-evals]] and [[wiki/concepts/human-in-the-loop]]. Strongest sources: [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]], [[wiki/docs/llms-docs-warp-dev/factories-factory-inbox]] and the podcast.

Operating a factory (not a podcast topic) is covered by [[wiki/concepts/self-hosting]] and [[wiki/concepts/secrets-management]], both Warp-only.

## Repos

- [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]] — eight copy-and-edit Warp Factories definitions (v1alpha1) as YAML and Markdown, plus scripts that validate them against Warp's server parser.
- [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]] — Warp's shared library of about 27 agent skills, with shell tooling that installs, pins by lockfile and propagates them into consumer repos.

## Index

### Entities (6)
- [[wiki/entities/warp-factories]] — Warp's hosted product for running a team of cloud agents.
- [[wiki/entities/claude-code]] — Anthropic's coding agent, run per role and used as an MCP client.
- [[wiki/entities/codex]] — OpenAI's coding agent, a swappable harness beside Claude Code.
- [[wiki/entities/github]] — code forge and event source for triggers, PRs and CI.
- [[wiki/entities/linear]] — issue tracker used as a work source.
- [[wiki/entities/slack]] — chat tool used for intake and status.

### Concepts (12)
- [[wiki/concepts/software-factory]] — agents, compute and orchestration turning requests into reviewed PRs.
- [[wiki/concepts/factory-as-code]] — a factory declared as a versioned YAML and Markdown tree.
- [[wiki/concepts/foreman-agent]] — the coordinator that delegates to stage agents.
- [[wiki/concepts/agent-skill]] — a version-controlled SKILL.md folder giving an agent a procedure.
- [[wiki/concepts/agent-harness]] — the runtime wrapping a model with tools and control loops.
- [[wiki/concepts/control-plane]] — dispatch, session records, permissions and spend, apart from compute.
- [[wiki/concepts/dev-environment]] — where the agent works: runtimes, repos, toolchain, access.
- [[wiki/concepts/agent-evals]] — scoring and benchmarking agents.
- [[wiki/concepts/human-in-the-loop]] — human approval at the decisions that matter.
- [[wiki/concepts/multi-repo-development]] — agents across several repos.
- [[wiki/concepts/self-hosting]] — running the factory's compute on your own infrastructure.
- [[wiki/concepts/secrets-management]] — how credentials reach agents and runners.

### Sources (55)
- [[wiki/sources/youtube-tGbjIvvYuHE]] — the Boundary podcast on factory layers.
- [[wiki/docs/llms-docs-warp-dev/OVERVIEW]] — map of the Warp docs set (52 ingested pages, 402-link catalog).
- The two repo architecture pages listed under Repos.

## Health

- Sources: 55 (4 origins: 1 podcast, 1 docs set, 2 repos; 3 of 4 are Warp) · Entities: 6 · Concepts: 12
- Slugs at 1 mention (waiting for a second origin): aws-ecr, azure-devops, baml, coderabbit, docker, gitlab, human-layer, jira, kubernetes, microsoft-teams, sentry, vercel, agent-runner, agentic-merge-queue, compounding-engineering, git-worktree, mcp, webhook
- Only the podcast is non-Warp. [[wiki/entities/warp-factories]] reaches 2 origins through the docs and the examples repo alone, so its page rests on Warp describing Warp. Many 1-mention slugs (docker, kubernetes, jira, webhook, agent-runner) have a large footprint inside the docs set; they still need an independent origin.

Next ingest: a non-Warp origin on merge queues, MCP, worktrees or factory-as-code would promote several of these at once and test the Warp-only claims.
