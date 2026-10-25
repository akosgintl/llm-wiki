---
type: concept
title: Context engineering
description: "The practice of deliberately structuring, storing and loading the context (requirements, org knowledge, instructions) that AI agents work from, instead of relying on the model or one-off prompts."
aliases: []
sources:
  - "[[wiki/docs/llms-docs-8090-ai/general-introduction]]"
  - "[[wiki/docs/llms-docs-factory-com/harness-skills]]"
  - "[[wiki/docs/llms-docs-port-io/context-lake-overview]]"
  - "[[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]"
related:
  - "[[wiki/concepts/knowledge-graph]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/software-factory]]"
created: 2026-10-25T18:30:09Z
timestamp: 2026-10-25T18:30:09Z
source_count: 4
---

# Context engineering

> Multiple framings: a shared workspace (8090), a context catalog (Port), and on-demand loading of instructions (Factory).

## Definition

Three vendors use the idea, each at a different layer. 8090 names it outright: a shared workspace where requirements, architecture plans and implementation details live in a Knowledge Graph and change together, with a Drift Bot flagging mismatches. [[wiki/docs/llms-docs-8090-ai/general-introduction]] Port treats it as a queryable "Context Lake": a software catalog (blueprints plus ingestion), business context, RBAC and scorecards that give agents organization-specific grounding. [[wiki/docs/llms-docs-port-io/context-lake-overview]]

Factory works at the level of the agent's own window. Skills are loaded by progressive disclosure: only `name` and `description` are read up front, and the full body loads when a request matches. [[wiki/docs/llms-docs-factory-com/harness-skills]]

## Key claims

- The bottleneck is not code but context: misalignment, missing context, unclear decisions. [[wiki/docs/llms-docs-8090-ai/general-introduction]], [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]
- Agents fail because context is wrong, not because the model is wrong. [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]
- Generic AI does not know what "production-ready", ownership or pipelines mean in a given organization; define these semantics once and let every agent consume them. [[wiki/docs/llms-docs-port-io/context-lake-overview]]
- Context must stay current: Drift Bot and automations comment when artifacts or code diverge. [[wiki/docs/llms-docs-8090-ai/general-introduction]]
- MCP connectors supply unmodeled data just in time, while the lake supplies modeled structure. [[wiki/docs/llms-docs-port-io/context-lake-overview]]
- A skill's `description` is the routing surface; supporting files are not auto-loaded and must be referenced from `SKILL.md`. [[wiki/docs/llms-docs-factory-com/harness-skills]]
- Enriched context feeds deterministic gates (scorecards) for routing, review and deploy, with human checkpoints at Plan, Build and Review. [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]

## Relationships

- **Knowledge graph**: 8090 and Port both realize the shared context as a graph or catalog. [[wiki/concepts/knowledge-graph]]
- **Agent skill**: on-demand procedural context. [[wiki/concepts/agent-skill]]
- **Agent harness**: the runtime that loads and scopes context. [[wiki/concepts/agent-harness]]
- **MCP**: channel for live external context. [[wiki/concepts/mcp]]
- **Human in the loop**: checkpoints sit on top of enriched context. [[wiki/concepts/human-in-the-loop]]

## Tensions

The term covers different things: 8090 and Port mean org-level knowledge shared across people and agents, while Factory means per-session loading of instructions. Port and 8090 are also vendors selling the layer; the Port 40-45% automation figure is a vendor claim. [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]

Corroboration caveat: the two Port pages are one origin and one voice.

> Synthesis: Context is the product in all three framings, but the layer differs: shared knowledge (8090, Port) versus per-session loading (Factory).
