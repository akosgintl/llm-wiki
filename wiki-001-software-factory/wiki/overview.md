---
type: overview
title: 001-software-factory — Overview
description: "Notes on building a \"software factory\" for AI coding agents, drawn from three Boundary podcasts, five vendor documentation sets (Warp Factories, Mastra Factory, 8090, Factory.ai, Port) and two Warp repositories."
created: 2026-10-25T14:35:38Z
timestamp: 2026-10-26T07:30:00Z
total_sources: 97
total_pages: 134
---

# 001-software-factory — Overview

The wiki has ten origins: three Boundary podcasts, five documentation sets and two repositories. All are counted per origin, not per page, so Warp's 52 docs pages are one voice. Five origins are vendor docs for competing factory products, and two more are Warp repos. Agreement across vendors is real corroboration of a pattern, but it is vendors describing their own products. The podcasts are the independent views, though one of them features Warp's CEO.

- Podcasts: [[wiki/sources/youtube-tGbjIvvYuHE]] ("How to Build a Software Factory for AI Coding Agents", Dex of Human Layer and Vaibhav of Boundary) supplies the layering and buy-or-build argument. [[wiki/sources/youtube-XUEfIxkdT2Q]] (Warp's CEO on a measurable, code-defined factory) adds yield metrics and risk-based review. [[wiki/sources/youtube-b5O6gb_Zuk8]] (commands, subagents and skills in Claude Code) separates instruction modules from context isolation.
- Docs sets (each has a map page, not a witness): [[wiki/docs/llms-docs-warp-dev/OVERVIEW]] (52 pages), [[wiki/docs/llms-factory-mastra-ai/OVERVIEW]] (10), [[wiki/docs/llms-docs-8090-ai/OVERVIEW]] (10), [[wiki/docs/llms-docs-factory-com/OVERVIEW]] (10) and [[wiki/docs/llms-docs-port-io/OVERVIEW]] (10).
- Repos: see Repos below.

## Themes

**The factory and its layers.** The podcast splits a factory into compute, dev environment, harness and control plane. Warp, Factory.ai and Port each describe that shape as a product, and Mastra Factory describes it self-hosted, from intake to reviewed pull requests. See [[wiki/concepts/software-factory]], [[wiki/concepts/dev-environment]] and [[wiki/concepts/control-plane]]. Strongest sources: [[wiki/sources/youtube-tGbjIvvYuHE]], [[wiki/sources/youtube-XUEfIxkdT2Q]] and [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]].

**The factory as versioned files.** Warp declares a factory as YAML and Markdown rooted at `factory.yaml`, with a foreman agent coordinating stage agents and shared skills. Mastra's boards-and-rules configuration and Port's workflows echo the declarative idea. This is the most-cited Warp idea (about 30 docs pages plus both repos). See [[wiki/concepts/factory-as-code]], [[wiki/concepts/foreman-agent]] and [[wiki/concepts/agent-skill]]. Strongest sources: [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]] and [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]].

**The harness, skills and swappable agents.** The inner harness is the coding agent, the outer harness is the workflow code around it. Warp exposes the harness as a per-agent setting, so [[wiki/entities/claude-code]] and [[wiki/entities/codex]] sit side by side. Skills (9 origins) and MCP are the shared extension points across nearly every set. See [[wiki/concepts/agent-harness]], [[wiki/concepts/agent-skill]] and [[wiki/concepts/mcp]]. Strongest sources: [[wiki/sources/youtube-b5O6gb_Zuk8]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]] and [[wiki/docs/llms-docs-factory-com/harness-subagents]].

**Humans at the gates, context and measurement.** [[wiki/concepts/human-in-the-loop]] has the widest support (10 origins, tied with software-factory): approvals on specs, merges and escalations. Context is the new strand. 8090 and Port treat it as a managed asset, via [[wiki/concepts/knowledge-base]], [[wiki/concepts/knowledge-graph]] and [[wiki/concepts/context-engineering]]. Evals (LLM-judge scoring, fixed-task benchmarks, and the CEO podcast's yield metrics) are how a pipeline changes safely: [[wiki/concepts/agent-evals]]. Strongest sources: [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]], [[wiki/docs/llms-docs-port-io/context-lake-overview]] and [[wiki/docs/llms-factory-mastra-ai/using-work-and-approvals]].

Saved work: [[wiki/notes/inner-and-outer-harness]] and [[wiki/questions/2026-10-25-inner-and-outer-loop]] hold a note and an answer filed back from queries. Open problems are in [[wiki/open-questions]].

Operating a factory is covered by [[wiki/concepts/self-hosting]], [[wiki/concepts/secrets-management]], [[wiki/concepts/webhook]] and [[wiki/concepts/git-worktree]]. Warp and Mastra carry most of it, with Factory.ai on the worktree side.

## Repos

- [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]] — eight copy-and-edit Warp Factories definitions (v1alpha1) as YAML and Markdown, plus scripts that validate them against Warp's server parser.
- [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]] — Warp's shared library of about 27 agent skills, with shell tooling that installs, pins by lockfile and propagates them into consumer repos.

## Index

### Entities (10)
- [[wiki/entities/warp-factories]] — Warp's hosted product for running a team of cloud agents.
- [[wiki/entities/claude-code]] — Anthropic's coding agent, run per role and used as an MCP client.
- [[wiki/entities/codex]] — OpenAI's coding agent, a swappable harness beside Claude Code.
- [[wiki/entities/github]] — code forge and event source for triggers, PRs and CI.
- [[wiki/entities/gitlab]] — code forge supported with a thinner integration than GitHub.
- [[wiki/entities/jira]] — Atlassian issue tracker used as a work source.
- [[wiki/entities/linear]] — issue tracker used as a work source by several products.
- [[wiki/entities/slack]] — chat tool used for intake and status.
- [[wiki/entities/microsoft-teams]] — chat alternative to Slack.
- [[wiki/entities/sentry]] — error monitoring that triggers agents via webhooks.

### Concepts (18)
- [[wiki/concepts/software-factory]] — agents, compute and orchestration turning requests into reviewed PRs.
- [[wiki/concepts/factory-as-code]] — a factory declared as a versioned YAML and Markdown tree.
- [[wiki/concepts/foreman-agent]] — the coordinator that delegates to stage agents.
- [[wiki/concepts/agent-skill]] — a version-controlled SKILL.md folder giving an agent a procedure.
- [[wiki/concepts/agent-harness]] — the runtime wrapping a model with tools and control loops.
- [[wiki/concepts/mcp]] — Model Context Protocol, the tool interface factories expose and consume.
- [[wiki/concepts/control-plane]] — dispatch, session records, permissions and spend, apart from compute.
- [[wiki/concepts/dev-environment]] — where the agent works: runtimes, repos, toolchain, access.
- [[wiki/concepts/context-engineering]] — shaping what an agent sees to make its work reliable.
- [[wiki/concepts/knowledge-base]] — curated project knowledge that agents draw on.
- [[wiki/concepts/knowledge-graph]] — linked entities and relations as agent context.
- [[wiki/concepts/agent-evals]] — scoring and benchmarking agents.
- [[wiki/concepts/human-in-the-loop]] — human approval at the decisions that matter.
- [[wiki/concepts/multi-repo-development]] — agents across several repos.
- [[wiki/concepts/git-worktree]] — isolated checkouts so parallel agents do not collide.
- [[wiki/concepts/webhook]] — event delivery that triggers agent runs.
- [[wiki/concepts/self-hosting]] — running the factory's compute on your own infrastructure.
- [[wiki/concepts/secrets-management]] — how credentials reach agents and runners.

### Sources (97)
- [[wiki/sources/youtube-tGbjIvvYuHE]] — the Boundary podcast on factory layers.
- [[wiki/sources/youtube-XUEfIxkdT2Q]] — Warp's CEO on building a measurable AI software factory.
- [[wiki/sources/youtube-b5O6gb_Zuk8]] — agents, subagents, skills and commands in Claude Code.
- Docs sets: 52 Warp pages, 10 each for Mastra Factory, 8090, Factory.ai and Port. Start from the map pages listed above.
- The two repo architecture pages listed under Repos.

## Health

- Sources: 97 (10 origins: 3 podcasts, 5 docs sets, 2 repos) · Entities: 10 · Concepts: 18
- Slugs at 1 mention (waiting for a second origin): agent-runner, agentops, agentic-merge-queue, compounding-engineering, docker, kubernetes, aws-ecr, azure-devops, vercel, 8090-software-factory, mastra-factory, port, baml, coderabbit, human-layer
- Only the podcasts are not vendor docs, and one of them is Warp's own CEO. [[wiki/entities/warp-factories]] reaches 2 origins through the Warp docs and the examples repo alone, so its page rests on Warp describing Warp. Several 1-mention slugs (agent-runner, docker, kubernetes) have a large footprint inside the Warp docs; they still need an independent origin.
- The other products ([[wiki/docs/llms-factory-mastra-ai/what-is-factory]], 8090, Factory.ai, Port) have no entity page yet: each is one origin.

Next ingest: a non-vendor origin on merge queues, agent runners or compounding engineering would promote several of these at once and test the vendor claims.
