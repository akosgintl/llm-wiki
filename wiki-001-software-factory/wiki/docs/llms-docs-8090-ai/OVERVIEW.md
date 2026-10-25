---
type: docs
title: Docs
description: Guides, best practices and REST API reference for 8090 Software Factory, a product that links requirements, blueprints and work orders to coding agents.
original_path: https://docs.8090.ai/llms.txt
source_url: https://docs.8090.ai/llms.txt
catalog: raw/docs/llms-docs-8090-ai/llms.txt
catalog_size: 158
created: 2026-10-25T00:00:00Z
timestamp: 2026-10-25T00:00:00Z
---

# Docs — Docs map

> Catalog: https://docs.8090.ai/llms.txt · 158 links · 10 ingested

About 30 links are product guides; about 130 are REST API endpoint pages.

## Ingested

- [[wiki/docs/llms-docs-8090-ai/general-introduction|Introduction]]
- [[wiki/docs/llms-docs-8090-ai/general-quickstart|Quickstart]]
- [[wiki/docs/llms-docs-8090-ai/connections-connect-coding-agent|Coding Agent Connection]]
- [[wiki/docs/llms-docs-8090-ai/modules-work-orders|Work Orders]]
- [[wiki/docs/llms-docs-8090-ai/modules-automations|Automations]]
- [[wiki/docs/llms-docs-8090-ai/modules-skills|Skills]]
- [[wiki/docs/llms-docs-8090-ai/opinions-agent-skill|Agent Skill]]
- [[wiki/docs/llms-docs-8090-ai/opinions-reverse-engineering|Reverse engineering]]
- [[wiki/docs/llms-docs-8090-ai/codebase-overview|Codebase Connection]]
- [[wiki/docs/llms-docs-8090-ai/modules-knowledge-base|Knowledge Base]]

## Areas

### Connections

Links from a project to outside systems: MCP servers, Slack, repositories, coding agents.

- [MCP Servers](https://docs.8090.ai/connections/mcp-servers) — external tools the factory agent can call
- [Slack](https://docs.8090.ai/connections/slack) — drive the factory agent from chat

### Core modules

The requirements, blueprint and feedback workspaces that feed the work order pipeline.

- [Requirements](https://docs.8090.ai/modules/requirements) — first stage of the pipeline feeding work orders
- [Blueprints](https://docs.8090.ai/modules/blueprints) — technical specs that guide implementation
- [Feedback](https://docs.8090.ai/modules/feedback) — customer signals tied to delivery work

### Agents

The in-product agent and its chat panel.

- [Agent chat](https://docs.8090.ai/agents/agent-chat) — how the factory agent is driven day to day

### Best practices

Opinionated writing guides and migration advice.

- [Requirements Writing Guide](https://docs.8090.ai/opinions/requirements-writing-guide) — what good input to the factory looks like
- [Blueprint Writing Guide](https://docs.8090.ai/opinions/blueprint-writing-guide) — spec format agents consume
- [Work Order Writing Guide](https://docs.8090.ai/opinions/work-order-writing-guide) — shaping tasks for coding agents
- [Migrating from Jira](https://docs.8090.ai/opinions/jira-migration) — loading existing work into the knowledge graph

### Administration and billing

Organization members, seats, usage and model pricing.

- [Organization Management](https://docs.8090.ai/administration/organizations) — shared skills and templates across projects
- [Usage & Billing](https://docs.8090.ai/administration/usage) — token usage tracking
- [Model Pricing](https://docs.8090.ai/administration/model-pricing) — per-token cost of agent runs

### Roles and access control

Organization roles, project roles, custom roles and API key permissions.

- [Roles & Access Control](https://docs.8090.ai/roles-and-access-control/overview) — how roles combine
- [Permissions Reference](https://docs.8090.ai/roles-and-access-control/permissions-reference) — API key permission inheritance
- [Custom Roles](https://docs.8090.ai/roles-and-access-control/custom-roles) — per-module access for agents and people

### Resources

Release history, roadmap, shortcuts and support.

- [Changelog](https://docs.8090.ai/resources/changelog) — dated feature history
- [Roadmap](https://docs.8090.ai/resources/roadmap) — planned direction of the product

### API: overview, conversations, automations

REST API entry point, agent conversation endpoints and automation CRUD (about 8 links).

- [API reference](https://docs.8090.ai/api-reference) — authentication and base usage
- [Create an automation](https://docs.8090.ai/api-reference/automations/create-an-automation) — set up triggered agent runs by script
- [List automations](https://docs.8090.ai/api-reference/automations/list-automations) — inspect run counts and config
- [Read an agent conversation](https://docs.8090.ai/api-reference/agent-conversations/read-an-agent-conversation) — read agent transcripts, including automation runs

### API: work orders

Endpoints for work orders, statuses, labels, phases, comments and pull request links (about 19 links).

- [Create work orders in a batch](https://docs.8090.ai/api-reference/work-orders/create-work-orders-in-a-batch) — bulk task creation for agents
- [List work orders](https://docs.8090.ai/api-reference/work-orders/list-work-orders) — filter and sort the task queue
- [Get a work order](https://docs.8090.ai/api-reference/work-orders/get-a-work-order) — task with linked requirements and blueprints
- [Update work orders in a batch](https://docs.8090.ai/api-reference/work-orders/update-work-orders-in-a-batch) — bulk status changes
- [Link pull request to work order](https://docs.8090.ai/api-reference/work-orders/link-pull-request-to-work-order) — trace code back to tasks

### API: requirements and blueprints

Endpoints for requirements documents and blueprints, with versions, comments, search and code links (about 30 links).

- [Get requirements document](https://docs.8090.ai/api-reference/requirements/get-requirements-document) — fetch spec content programmatically
- [Get blueprint](https://docs.8090.ai/api-reference/blueprints/get-blueprint) — latest technical spec
- [List blueprint code links](https://docs.8090.ai/api-reference/blueprints/list-blueprint-code-links) — spec-to-code traceability
- [Search blueprints](https://docs.8090.ai/api-reference/blueprints/search-blueprints) — literal text search over specs
- [Apply a tracked suggestion to blueprint content](https://docs.8090.ai/api-reference/blueprints/apply-a-tracked-suggestion-to-blueprint-content) — agent edits as reviewable changes

### API: Knowledge Base and skills

Endpoints for knowledge base resources and project skills (about 26 links).

- [List skills](https://docs.8090.ai/api-reference/skills/list-skills) — project, built-in and writing-rules skills
- [Create skill](https://docs.8090.ai/api-reference/skills/create-skill) — publish reusable agent instructions
- [Get skill](https://docs.8090.ai/api-reference/skills/get-skill) — read skill markdown
- [Create Knowledge Base resource](https://docs.8090.ai/api-reference/knowledge-base/create-knowledge-base-resource) — feed context to the factory
- [List Knowledge Base resources](https://docs.8090.ai/api-reference/knowledge-base/list-knowledge-base-resources) — browse project context

### API: feedback, users and health

Endpoints for feedback items, feedback themes, users and a health check (about 36 links).

- [Create feedback item](https://docs.8090.ai/api-reference/feedback-items/create-feedback-item) — feed customer signals in
- [Link feedback item to work order](https://docs.8090.ai/api-reference/feedback-items/link-feedback-item-to-work-order) — signal-to-delivery trace
- [Create feedback theme](https://docs.8090.ai/api-reference/feedback-themes/create-feedback-theme) — group recurring feedback
- [Check API health](https://docs.8090.ai/api-reference/health/check-api-health) — verify key and connectivity

## Pulling more

Ingest the catalog again with a new intent, or ask a question the pages above
do not answer — the query path fetches from this catalog (`QUERY.md` Q.6b).
