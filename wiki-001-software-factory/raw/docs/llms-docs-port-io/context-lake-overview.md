---
title: "Context Lake"
subtitle: "See how Port's context lake unifies data from your engineering tools into one queryable layer that humans and AI agents can use."
authors: []
published_date: null
source_url: https://docs.port.io/context-lake/overview.md
origin: llms-txt
llms_txt: https://docs.port.io/llms.txt
section: "context-lake"
fetched: 2026-10-25T18:18:27Z
---

# Context Lake

Port's Context Lake is your unified engineering knowledge layer—connecting data from across your entire toolchain into a single, semantically-rich source of truth. It's not a separate feature, but rather the powerful result of Port's core capabilities working together to provide organizational context that AI agents, developers, and workflows can understand and act upon.

## What comprises the context lake[​](#what-comprises-the-context-lake "Direct link to What comprises the context lake")

The context lake transforms scattered data across your engineering tools into unified organizational knowledge. It is built from four core components:

### Software catalog[​](#software-catalog "Direct link to Software catalog")

The software catalog is the heart of the context lake. It is built from two layers that work together:

* **[Data model](/context-lake/data-model/configure-data-model/.md)** - you define blueprints that represent the things your organization cares about: services, environments, teams, deployments, incidents, and more. Blueprints carry properties, relations, and metadata that encode what these concepts mean in your specific context.
* **[Data ingestion](/context-lake/ingestion/overview/.md)** - your tools (GitHub, Kubernetes, PagerDuty, Jira, and 100+ others) continuously populate the catalog with real entities that match those blueprints, keeping your data fresh and accurate.

Together, these two layers make the catalog your **organizational semantic layer** - it teaches Port what "service," "deployment," or "incident" means specifically in your organization, providing the schema and populated data that gives AI agents, workflows, and dashboards something meaningful to act on.

### Business context[​](#business-context "Direct link to Business context")

Beyond technical metadata, the context lake enriches your software catalog with **[business context](/context-lake/business-context/overview/.md)** - the organizational, financial, and operational signals that help prioritize work, assess risk, and align engineering decisions with business objectives. This includes cost and revenue data, service criticality, team ownership, SLAs, compliance scope, and customer tier information.

When AI agents and workflows understand this context, they can prioritize vulnerabilities by business impact, route incidents to the right owner, estimate blast radius, and enforce policies automatically - all without manual triage.

For a full breakdown of what business context includes, example use cases, and how to model it in Port, see [Business context](/context-lake/business-context/overview/.md).

### Access controls - data governance[​](#access-controls---data-governance "Direct link to Access controls - data governance")

[RBAC and permissions](/context-lake/consuming-the-lake/govern-data-access/overview/.md) ensure that the right people and systems see the right data. Teams, roles, and policies control who can view, edit, or act on catalog data, maintaining security while enabling collaboration and providing governed access to your organizational knowledge.

### Scorecards - your standards[​](#scorecards---your-standards "Direct link to Scorecards - your standards")

[Scorecards](/governance/standards-and-compliance/overview/.md) define and track your engineering standards, KPIs, and quality metrics. They encode organizational expectations—production readiness requirements, security compliance rules, operational best practices—as measurable criteria within the Context Lake, providing the organizational standards and quality signals that inform decisions.

### Interface layer - how you access it[​](#interface-layer---how-you-access-it "Direct link to Interface layer - how you access it")

Context Lake data becomes actionable through multiple interfaces: **[Port AI Assistant](/port-ai/port-ai-assistant/.md)** and [Port MCP server](/agent-management/port-mcp-server/installation/.md) for AI-driven access, **[API](/api-reference/port-api/)** for programmatic access, and **[Interface Designer](/interface-builder/port-interface/dashboards/overview/.md)** with dashboards and visualizations that surface insights to your teams—providing multiple ways to query, visualize, and act on your organizational context.

### External data via MCP Connectors[​](#external-data-via-mcp-connectors "Direct link to External data via MCP Connectors")

While the Context Lake provides structured organizational knowledge, [MCP Connectors](/agent-management/mcp-connectors/.md) complement it by giving Port AI access to external tools like Notion, Linear, Jira, and other MCP servers. The Context Lake provides the modeled data (blueprints, entities, scorecards), while MCP Connectors provide real-time access to external data you wouldn't typically model like documentation, tickets, logs, and other just-in-time information. Together, they give AI agents both structured context and dynamic external data for more accurate responses.

The more your catalog data is modeled — entities related to one another, ownership clearly defined, scorecards encoding your standards — the more grounded and accurate AI responses become. MCP connectors then extend that foundation with live access to the parts you haven't modeled. Not sure which to use for a given tool? See [Integrations vs. MCP connectors](/context-lake/ingestion/integrations-vs-mcp/.md).

## Why the context lake matters[​](#why-the-context-lake-matters "Direct link to Why the context lake matters")

* For AI agents
* For developers
* For platform teams

Generic AI doesn't understand what "production-ready" means in YOUR organization, who owns which services, or how your deployment pipeline works. Context Lake provides this semantic understanding, enabling AI agents to:

* Answer ownership questions with definitive data (not guesses from code comments).
* Understand dependencies and relationships between services.
* Follow your organization's standards and guardrails when taking actions.
* Make decisions based on real-time operational context.

Instead of hunting across 10 different tools to understand a service's dependencies, ownership, deployment history, or incident timeline, developers get unified context in one place. The Context Lake connects the dots automatically.

**Benefits:**

* Quick access to service ownership and team information.
* Understand dependencies without switching between tools.
* See complete deployment and incident history in context.
* Get AI-powered insights based on your organization's actual data.

Define your organizational semantics once—service definitions, environment types, team structures, standards—and every tool, workflow, and AI agent can consume this shared knowledge. No more syncing configurations across systems.

**Benefits:**

* Single source of truth for organizational definitions.
* Consistent standards across all tools and automations.
* Reduced maintenance overhead from duplicate configurations.
* Enable self-service while maintaining governance.

## Context lake in action - examples[​](#context-lake-in-action---examples "Direct link to Context lake in action - examples")

* AI agent understanding ownership
* Autonomous service provisioning
* Incident response

**Developer asks:** "Who owns the payments service?"

* **Without Context Lake:** AI guesses based on code comments or recent contributors.
* **With Context Lake:** AI queries the catalog → sees Team relation → returns the owning team with Slack channel and on-call schedule.

**AI agent needs to provision a dev environment:**

* **Without Context Lake:** Agent doesn't know company's cloud standards, naming conventions, or cost limits.
* **With Context Lake:** Agent queries blueprints → understands allowed regions, naming patterns, tagging requirements → provisions correctly within organizational guardrails.

**Alert fires:** "payments-api pod crashing"

* **Without Context Lake:** Engineer hunts through Slack, wiki, runbooks across multiple tools.
* **With Context Lake:** Port surfaces: recent deployments, related PRs, dependent services, ownership, SLOs, past incidents—all in unified context for faster resolution.

## Getting started[​](#getting-started "Direct link to Getting started")

Building your Context Lake is a natural part of setting up Port:

1. **[Define your data model](/context-lake/data-model/configure-data-model/.md)** - Create blueprints that represent your organization's entities.
2. **[Connect your tools](/context-lake/ingestion/ingest-data-into-port/native-integrations/overview/.md#available-plug--play-integrations)** - Ingest data from GitHub, Kubernetes, PagerDuty, and 100+ other integrations.
3. **[Set up relationships](/context-lake/ingestion/configure-mapping/overview/.md#mapping-relations)** - Define how entities connect to each other.
4. **[Configure access controls](/context-lake/consuming-the-lake/govern-data-access/overview/.md)** - Ensure proper data governance.
5. **[Define standards](/governance/standards-and-compliance/overview/.md)** - Create scorecards that encode your quality requirements.

As you build your catalog, you're simultaneously building your Context Lake—the unified knowledge layer that powers intelligent automation and AI-driven workflows.

## FAQ[​](#faq "Direct link to FAQ")

1What is the Context Lake?

2Is the Context Lake the same as the software catalog?

3Can AI agents query the Context Lake?

4What is business context in the Context Lake?
