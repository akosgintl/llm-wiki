---
type: source
title: Context Lake
description: "Port's Context Lake is the unified, queryable layer of catalog data, business context, access controls and scorecards that gives AI agents and developers organization-specific grounding."
origin: llms-txt
original_path: https://docs.port.io/context-lake/overview.md
source_url: https://docs.port.io/context-lake/overview.md
authors: []
published_date: null
raw_file: raw/docs/llms-docs-port-io/context-lake-overview.md
created: 2026-10-25T18:50:00Z
timestamp: 2026-10-25T18:50:00Z
entities: []
concepts:
  - "[[wiki/concepts/context-engineering]]"
  - "[[wiki/concepts/knowledge-graph]]"
  - "[[wiki/concepts/mcp]]"
---

# Context Lake

> [[raw/docs/llms-docs-port-io/context-lake-overview|Raw]] · llms-txt

## Summary

Port frames the Context Lake as an engineering knowledge layer that joins data from the whole toolchain into one semantically rich source of truth. It is "not a separate feature" but the result of Port's core capabilities working together, so that AI agents, developers and workflows share organizational context. [[raw/docs/llms-docs-port-io/context-lake-overview#Context Lake|cite]]

It has components. The software catalog is the core: user-defined blueprints (services, environments, teams, deployments, incidents) carry properties and relations, and ingestion from 100+ tools fills them with real entities. Together they form an "organizational semantic layer" that teaches Port what "service" or "incident" means locally. Business context (cost, criticality, ownership, SLAs, compliance scope, customer tier), RBAC and scorecards for standards complete the model. Access is through Port AI Assistant, an MCP server, an API and dashboards. [[raw/docs/llms-docs-port-io/context-lake-overview#What comprises the context lake|cite]]

MCP Connectors cover what is not modeled: live access to Notion, Linear, Jira and other MCP servers for docs, tickets and logs. The lake supplies modeled structure; connectors supply just-in-time data. [[raw/docs/llms-docs-port-io/context-lake-overview#External data via MCP Connectors|cite]]

## Key claims

- The catalog = data model (blueprints) plus data ingestion; this is the organizational semantic layer. [[raw/docs/llms-docs-port-io/context-lake-overview#Software catalog|cite]]
- Business context lets agents prioritize vulnerabilities by business impact, route incidents and estimate blast radius without manual triage. [[raw/docs/llms-docs-port-io/context-lake-overview#Business context|cite]]
- The more the catalog is modeled (relations, ownership, scorecards), the more grounded AI answers are; MCP connectors extend this for unmodeled data. [[raw/docs/llms-docs-port-io/context-lake-overview#External data via MCP Connectors|cite]]
- Agents gain definitive ownership answers, dependency awareness, adherence to standards and guardrails, and real-time operational context. [[raw/docs/llms-docs-port-io/context-lake-overview#Why the context lake matters|cite]]
- Example: an agent provisioning a dev environment queries blueprints for allowed regions, naming and tagging rules, and stays within guardrails. [[raw/docs/llms-docs-port-io/context-lake-overview#Context lake in action - examples|cite]]
- Setup order: data model, connect tools, relations, access controls, scorecards. [[raw/docs/llms-docs-port-io/context-lake-overview#Getting started|cite]]

## Notable quotes

> "Generic AI doesn't understand what "production-ready" means in YOUR organization, who owns which services, or how your deployment pipeline works."
> — [[raw/docs/llms-docs-port-io/context-lake-overview#Why the context lake matters|Why the context lake matters]]

> "Define your organizational semantics once—service definitions, environment types, team structures, standards—and every tool, workflow, and AI agent can consume this shared knowledge."
> — [[raw/docs/llms-docs-port-io/context-lake-overview#Why the context lake matters|Why the context lake matters]]

## Connections

- **Entities**: none
- **Concepts**: [[wiki/concepts/context-engineering]], [[wiki/concepts/knowledge-graph]], [[wiki/concepts/mcp]]

> Synthesis: Vendor overview of an internal-developer-portal catalog pitched as agent context; it is a structured-context-layer approach, unlike the code-and-config factory framing of Warp or Mastra, and it is not a factory product itself.
