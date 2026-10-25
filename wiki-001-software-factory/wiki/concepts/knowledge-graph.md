---
type: concept
title: Knowledge graph
description: A linked model of an organization's artifacts and entities (requirements, specs, services, owners) that humans and AI agents query as a shared source of truth.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-8090-ai/general-introduction]]"
  - "[[wiki/docs/llms-docs-port-io/context-lake-overview]]"
  - "[[wiki/docs/llms-docs-port-io/solutions-agentops-overview]]"
related:
  - "[[wiki/concepts/context-engineering]]"
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/control-plane]]"
created: 2026-10-25T18:30:34Z
timestamp: 2026-10-25T18:30:34Z
source_count: 3
---

# Knowledge graph

> Multiple framings: see Definition

## Definition

Two vendors use the idea differently. 8090 puts the lifecycle artifacts themselves in the graph: requirements, architecture plans and implementation details are linked so they change together. [[wiki/docs/llms-docs-8090-ai/general-introduction]]

Port builds a graph of the engineering estate. Blueprints (services, environments, teams, deployments, incidents) with properties and relations, filled from 100+ tools, form an "organizational semantic layer" inside its Context Lake. [[wiki/docs/llms-docs-port-io/context-lake-overview]] Port's AgentOps also models agents, skills, MCP servers, tools, teams, services and permissions as one dependency graph. [[wiki/docs/llms-docs-port-io/solutions-agentops-overview]]

## Key claims

- Linking requirements, blueprints and work orders lets specialized agents surface gaps, and Drift Bot flags artifacts or code that no longer match. [[wiki/docs/llms-docs-8090-ai/general-introduction]]
- Fragmented docs and tribal knowledge slow delivery; a shared graph is the proposed fix. [[wiki/docs/llms-docs-8090-ai/general-introduction]]
- Modeling relations, ownership and scorecards makes AI answers more grounded; agents get ownership answers, dependency awareness and guardrails. [[wiki/docs/llms-docs-port-io/context-lake-overview]]
- Business context (cost, criticality, SLAs) lets agents prioritize and estimate blast radius. [[wiki/docs/llms-docs-port-io/context-lake-overview]]
- MCP connectors supply unmodeled data just in time, on top of the modeled graph. [[wiki/docs/llms-docs-port-io/context-lake-overview]]
- Inventory, certification, enforcement and optimization of agents all run on the same graph. [[wiki/docs/llms-docs-port-io/solutions-agentops-overview]]

## Tensions

- Scope differs: 8090's graph holds the spec-to-task chain of one project ([[wiki/docs/llms-docs-8090-ai/general-introduction]]); Port's holds org-wide operational and governance data ([[wiki/docs/llms-docs-port-io/context-lake-overview]]). Port also says the lake is "not a separate feature", so "graph" is a loose label there.
- Both are vendor marketing; none shows an implementation.

## Relationships

- **Context engineering**: the graph is the store both vendors use to deliver context. [[wiki/concepts/context-engineering]]
- **Software factory**: 8090 uses it as the spec layer; Port as the governance layer. [[wiki/concepts/software-factory]]
- **MCP**: extends the graph with live external data. [[wiki/concepts/mcp]]
- **Control plane**: Port's registry and enforcement sit on it. [[wiki/concepts/control-plane]]

> Synthesis: Two docs sets, so two origins, with only two vendor voices. The graph is a recurring substrate for agent context, but its shape (artifact chain versus org catalog) is not settled.
