---
type: docs
title: Port Documentation
description: Documentation for Port, a platform for building an AI software factory, covering its context lake, workflows, Port AI, agent management, governance and solution playbooks.
original_path: https://docs.port.io/llms.txt
source_url: https://docs.port.io/llms.txt
catalog: raw/docs/llms-docs-port-io/llms.txt
catalog_size: 753
created: 2026-10-25T18:27:03Z
timestamp: 2026-10-25T18:27:03Z
---

# Port Documentation — Docs map

> Catalog: https://docs.port.io/llms.txt · 753 links · 10 ingested

## Ingested

- [[wiki/docs/llms-docs-port-io/getting-started-agentic-sdlc-pillars|The pillars of an AI software factory]]
- [[wiki/docs/llms-docs-port-io/glossary|Glossary]]
- [[wiki/docs/llms-docs-port-io/context-lake-overview|Context Lake]]
- [[wiki/docs/llms-docs-port-io/workflows-concepts|Concepts and structure]]
- [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview|Autonomous ticket resolution]]
- [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-agentic-initiatives|Agentic initiatives]]
- [[wiki/docs/llms-docs-port-io/solutions-agentops-overview|AgentOps]]
- [[wiki/docs/llms-docs-port-io/agent-management-overview|Agent management]]
- [[wiki/docs/llms-docs-port-io/agent-management-skills-overview|Skills]]
- [[wiki/docs/llms-docs-port-io/guides-all-trigger-ai-coding-assistants-from-port|Trigger AI coding assistants from Port]]

## Areas

### Getting started

Setup path: connect Git, build the context lake, first workflow, dashboards, team invites.

- [Getting started](https://docs.port.io/getting-started/overview.md) — entry point to the onboarding sequence
- [Build your first workflow](https://docs.port.io/getting-started/build-your-first-workflow.md) — first AI-powered workflow walkthrough
- [Craft a prompt](https://docs.port.io/getting-started/craft-an-initial-prompt.md) — Port AI builds initial platform structure
- [Set up your context lake](https://docs.port.io/getting-started/set-up-your-context-lake.md) — populating services, users, ownership

### Context lake

Data model (blueprints, ontology), ingestion (native integrations, webhooks, API), business context, and consumption (search, CLI, MCP, RBAC).

- [Business context](https://docs.port.io/context-lake/business-context/overview.md) — cost, criticality, SLAs for agent prioritization
- [Ingestion overview](https://docs.port.io/context-lake/ingestion/overview.md) — how data enters the lake
- [Consumption methods](https://docs.port.io/context-lake/consuming-the-lake/overview.md) — how agents query the lake
- [Govern data access](https://docs.port.io/context-lake/consuming-the-lake/govern-data-access/overview.md) — catalog RBAC for humans and agents
- [Port CLI](https://docs.port.io/context-lake/consuming-the-lake/port-cli/overview.md) — shell access for coding agents

### Workflows

Visual and JSON workflow builder: triggers, action and flow nodes, reusable workflows, testing, execution tracking, permissions.

- [Workflows & tools](https://docs.port.io/workflows/overview.md) — workflows for humans, automations and agents
- [Expose workflows as tools](https://docs.port.io/workflows/expose-as-tool.md) — make workflows invokable by agents via MCP
- [Use-cases & examples](https://docs.port.io/workflows/use-cases-and-examples.md) — agent-triggered workflow examples
- [Quickstart](https://docs.port.io/workflows/build-workflows/quickstart.md) — build a first workflow

### Port AI

Port's natural-language assistant and API: context engineering, invocations, LLM providers, tools and approvals, security and quotas.

- [Port AI](https://docs.port.io/port-ai/overview.md) — what Port AI does
- [Context engineering](https://docs.port.io/port-ai/context-engineering.md) — shaping the information environment for agents
- [Tools and approvals](https://docs.port.io/port-ai/tools-and-approvals.md) — controlling what the AI may call
- [AI security and data controls](https://docs.port.io/port-ai/security-and-data-controls.md) — RBAC and data privacy for AI
- [Port AI Assistant](https://docs.port.io/port-ai/port-ai-assistant.md) — ask, plan and build modes

### Agent management

Governing agents, skills and MCP access: custom agents, external agents, MCP connectors, Port MCP server, skills.

- [Port custom agents](https://docs.port.io/agent-management/custom-agents/overview.md) — building domain agents in Port
- [External agents](https://docs.port.io/agent-management/external-agents/overview.md) — registry and sessions for outside agents
- [Claude managed agents](https://docs.port.io/agent-management/external-agents/claude-managed-agents.md) — trigger Claude sessions from workflows
- [MCP connectors](https://docs.port.io/agent-management/mcp-connectors.md) — gateway with RBAC and audit
- [Port MCP server](https://docs.port.io/agent-management/port-mcp-server/overview.md) — IDE agents querying the catalog

### Interface builder

Catalog pages, dashboards, global search, Slack app and external interfaces.

- [Interface builder](https://docs.port.io/interface-builder/overview.md) — surfaces where teams launch governed workflows
- [Slack Application](https://docs.port.io/interface-builder/notifications/slack-app.md) — software factory access from Slack
- [External interfaces](https://docs.port.io/interface-builder/external-interfaces.md) — custom UIs on Port

### Governance

Permissions across pillars, scorecards, standards and compliance, audit trails.

- [Governance layer](https://docs.port.io/governance/overview.md) — what humans and agents can see and do
- [Governance across pillars](https://docs.port.io/governance/governance-across-pillars/overview.md) — per-pillar access controls
- [Standards and compliance](https://docs.port.io/governance/standards-and-compliance/overview.md) — scorecards and maturity levels
- [Scorecard use-cases](https://docs.port.io/governance/standards-and-compliance/examples/scorecard-use-cases.md) — practical rule examples

### Platform administration

Org administration: users and teams, SSO, secrets, plans, audit log, security.

- [Platform administration](https://docs.port.io/platform-administration/overview.md) — admin overview
- [Audit log](https://docs.port.io/platform-administration/audit-log.md) — record of org changes
- [Security & compliance](https://docs.port.io/platform-administration/security.md) — certifications, encryption

### Solutions: autonomous ticket resolution and resource management

Playbooks for ticket triage, routing, coding-agent delivery, safe release, ROI; plus agentic infrastructure golden paths.

- [Turn tickets into actionable work](https://docs.port.io/solutions/autonomous-ticket-resolution/turn-tickets-into-actionable-work.md) — ticket enrichment for agents
- [Safe release](https://docs.port.io/solutions/autonomous-ticket-resolution/safe-release.md) — PR enrichment, reviewers, security
- [Why Port?](https://docs.port.io/solutions/autonomous-ticket-resolution/why-port.md) — rationale for the ATR approach
- [Measure impact of ATR](https://docs.port.io/solutions/autonomous-ticket-resolution/roi-dashboard.md) — ROI dashboard
- [Golden paths](https://docs.port.io/solutions/agentic-resource-management/golden-paths.md) — governed infrastructure delivery

### Solutions: AgentOps

Inventory, certification, governance enforcement and optimization of agents, skills and MCP servers.

- [Build your agentic registry](https://docs.port.io/solutions/agentops/agentic-registry.md) — one inventory of agents, skills, MCP
- [Promote agents through lifecycle gates](https://docs.port.io/solutions/agentops/certification-methods/promotion-gates.md) — dev to production gating
- [Contain agents with a kill switch](https://docs.port.io/solutions/agentops/governance-enforcement/kill-switch.md) — containment levels
- [Measure the ROI of your agentic assets](https://docs.port.io/solutions/agentops/continuous-optimization/roi-measurement.md) — cost per agent
- [Port and AI gateways: why you need both](https://docs.port.io/solutions/agentops/port-and-ai-gateways.md) — gateway comparison

### Solutions: self-healing incidents and engineering intelligence

Incident stages (detect to learn) and metrics: DORA, delivery, AI adoption, developer experience.

- [Self-healing incidents](https://docs.port.io/solutions/self-healing-incidents/overview.md) — five stages with agent gates
- [Learn from incidents](https://docs.port.io/solutions/self-healing-incidents/learn-from-incidents.md) — feedback loop with human review
- [AI adoption and impact](https://docs.port.io/solutions/engineering-intelligence/ai-adoption.md) — tracking AI tool usage and ROI
- [DORA metrics](https://docs.port.io/solutions/engineering-intelligence/measure-and-track-standards/dora-metrics.md) — delivery performance measures

### Guides

Hundreds of step-by-step implementations; many use coding agents, AI triage and AI usage dashboards.

- [Automatically resolve tickets with Port](https://docs.port.io/guides/all/automatically-resolve-tickets.md) — Jira tickets to coding agents
- [Standardize AI coding rules across repositories](https://docs.port.io/guides/all/standardize-ai-coding-rules.md) — shared agent rules from one repo
- [Remediate vulnerabilities with AI](https://docs.port.io/guides/all/remediate-vulnerability-with-ai.md) — workflow plus coding agent
- [Track AI coding assistants costs](https://docs.port.io/guides/all/track-ai-coding-assistants-costs.md) — cost dashboard
- [Build an AI Agent Registry](https://docs.port.io/guides/all/build-ai-agent-registry.md) — discover and govern agents

### Troubleshooting and optional references

Fix guides for actions, integrations and the execution agent; plus agent quick reference and REST API.

- [Port agent guide](https://docs.port.io/AGENTS.md) — auth, base URLs, terminology
- [Port REST API reference](https://docs.port.io/api-reference/port-api) — all endpoints
- [Port implementation guides by pillar](https://docs.port.io/llms/guides.txt) — guides grouped by pillar
- [Port execution agent troubleshooting](https://docs.port.io/troubleshooting/port-agent.md) — agent failure diagnosis

## Pulling more

Ingest the catalog again with a new intent, or ask a question the pages above
do not answer — the query path fetches from this catalog (`QUERY.md` Q.6b).
