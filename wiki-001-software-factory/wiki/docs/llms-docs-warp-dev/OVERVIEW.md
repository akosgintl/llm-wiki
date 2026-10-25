---
type: docs
title: Warp
description: Documentation for Warp, the agentic terminal and cloud agent platform, including Warp Factories for running software factories.
original_path: https://docs.warp.dev/llms.txt
source_url: https://docs.warp.dev/llms.txt
catalog: raw/docs/llms-docs-warp-dev/llms.txt
catalog_size: 402
created: 2026-10-25T14:55:53Z
timestamp: 2026-10-25T14:55:53Z
---

# Warp — Docs map

> Catalog: https://docs.warp.dev/llms.txt · 402 links · 52 ingested

## Ingested

- [[wiki/docs/llms-docs-warp-dev/factories|Warp Factories overview]]
- [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk|Agent & run endpoints]]
- [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-demo-sentry-monitoring-with-sdk|Demo: Sentry monitoring with SDK]]
- [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-quickstart|Warp Platform API quickstart]]
- [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors|API error codes]]
- [[wiki/docs/llms-docs-warp-dev/factories-automations|Factory automations]]
- [[wiki/docs/llms-docs-warp-dev/factories-benchmarks|Factory benchmarks]]
- [[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges|Connecting other code forges to your factory]]
- [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory|Connect your factory]]
- [[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns|Deployment patterns for Warp Factories]]
- [[wiki/docs/llms-docs-warp-dev/factories-developer-tools|Warp Platform API & SDKs]]
- [[wiki/docs/llms-docs-warp-dev/factories-factory-agents|About factory agents]]
- [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration|Configuring factory agents]]
- [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents|Creating custom agents]]
- [[wiki/docs/llms-docs-warp-dev/factories-factory-api|Factory endpoints]]
- [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code|Factory definition syntax]]
- [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard|Factory dashboard]]
- [[wiki/docs/llms-docs-warp-dev/factories-factory-inbox|Factory inbox]]
- [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp|Factory MCP for coding agents]]
- [[wiki/docs/llms-docs-warp-dev/factories-factory-skills|Factory skills]]
- [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work|How Warp Factories work]]
- [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security|About factory infrastructure and security]]
- [[wiki/docs/llms-docs-warp-dev/factories-integrations-azure-devops|Connecting Azure DevOps to your factory]]
- [[wiki/docs/llms-docs-warp-dev/factories-integrations-github|Connect GitHub to your factory]]
- [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab|Connect GitLab to your factory]]
- [[wiki/docs/llms-docs-warp-dev/factories-integrations-jira|Connect Jira to your factory]]
- [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear|Connect Linear to your factory]]
- [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack|Connect Slack to your factory]]
- [[wiki/docs/llms-docs-warp-dev/factories-integrations-teams|Connect Microsoft Teams to your factory]]
- [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve|Measure and improve a factory]]
- [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers|Configuring Scorers]]
- [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement|Configuring and reviewing Self-improvement]]
- [[wiki/docs/llms-docs-warp-dev/factories-quickstart|Warp Factories quickstart]]
- [[wiki/docs/llms-docs-warp-dev/factories-runners|Runners for Warp Factories]]
- [[wiki/docs/llms-docs-warp-dev/factories-secrets|Managing factory secrets]]
- [[wiki/docs/llms-docs-warp-dev/factories-secrets-aws-ecr|Configuring AWS ECR credentials]]
- [[wiki/docs/llms-docs-warp-dev/factories-self-hosting|Self-hosting overview]]
- [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-data-storage|Self-hosted agent data storage]]
- [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees|Isolating Direct backend tasks with Git worktrees]]
- [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-external-orchestrators|Running agents with an external orchestrator]]
- [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct|Managed: Direct backend]]
- [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-docker|Managed: Docker backend]]
- [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes|Managed: Kubernetes backend]]
- [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-monitoring|Self-hosted worker monitoring]]
- [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-private-container-registry|Pulling self-hosted images from a private registry]]
- [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-quickstart|Self-hosting quickstart]]
- [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-reference|Self-hosted worker reference]]
- [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting|Self-hosting troubleshooting]]
- [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting|Troubleshooting Warp Factories]]
- [[wiki/docs/llms-docs-warp-dev/factories-warp-hosting|Warp-hosted execution for Warp Factories]]
- [[wiki/docs/llms-docs-warp-dev/factories-webhooks|Triggering automations with custom webhooks]]
- [[wiki/docs/llms-docs-warp-dev/factories-webhooks-vercel|Setting up a Vercel webhook]]

## Areas

### Automation Platform (cloud agents)
Cloud agent runtime that Factories run on: environments, triggers, handoff, harnesses, orchestration, security.

- [Platform architecture](https://docs.warp.dev/platform/architecture/) — run lifecycle and data boundaries
- [Cloud agent environments](https://docs.warp.dev/platform/environments/) — containers and repos agents run in
- [Multi-agent orchestration](https://docs.warp.dev/platform/orchestration/) — supervisor/worker, fan-out, critic patterns

### Oz CLI and Warp Agent CLI
Command-line tools to run, configure and manage local and cloud agents.

- [Oz CLI reference](https://docs.warp.dev/agents/cli/oz-cli/) — run and manage agents from terminal
- [API keys for the Oz CLI](https://docs.warp.dev/agents/cli/oz-cli/api-keys/) — auth for CLI, cloud agents, workers
- [Federated identity tokens](https://docs.warp.dev/agents/cli/oz-cli/federate/) — OIDC tokens for cloud provider access

### Local agent capabilities
Agent features in the Warp app: rules, skills, planning, profiles, MCP, codebase context, computer use.

- [Skills for agents](https://docs.warp.dev/agents/capabilities/skills/) — reusable instruction sets, like factory skills
- [Rules for agents](https://docs.warp.dev/agents/capabilities/rules/) — global and project conventions
- [Profiles & Permissions](https://docs.warp.dev/agents/capabilities/agent-profiles-permissions/) — autonomy and tool permissions

### Third-party CLI agents and inference
Running Claude Code, Codex, OpenCode inside Warp, and choosing or bringing models.

- [Third-party CLI agents overview](https://docs.warp.dev/agents/cli-agents/overview/) — first-class support for outside agents
- [Remote Control](https://docs.warp.dev/agents/cli-agents/remote-control/) — monitor and steer sessions from the cloud
- [Bring Your Own API Key](https://docs.warp.dev/agents/inference/bring-your-own-api-key/) — BYOK for OpenAI, Anthropic, Google

### Guides: software factory and agent workflows
Tutorials for factory-style setups and multi-agent workflows.

- [Set up your software factory](https://docs.warp.dev/guides/agent-workflows/set-up-a-software-factory/) — four agent roles, GitHub labels as state machine
- [Run a software factory in the cloud](https://docs.warp.dev/guides/agent-workflows/run-a-software-factory-in-the-cloud/) — Automation Platform production path
- [Write product and tech specs with agents](https://docs.warp.dev/guides/agent-workflows/write-product-and-tech-specs-with-agents/) — spec stage of the pipeline

### Guides: configuration, external tools, devops
Task walkthroughs for rules, profiles, MCP integrations, DevOps and app builds.

- [Build a Mattermost bot for Warp Factories](https://docs.warp.dev/guides/external-tools/build-a-mattermost-bot-for-warp-factories/) — dispatching tasks to a factory
- [How to run unattended agents](https://docs.warp.dev/guides/agent-workflows/how-to-run-unattended-agents/) — schedules, Slack, Linear, GitHub triggers
- [Run multiple AI coding agents](https://docs.warp.dev/guides/agent-workflows/how-to-run-multiple-ai-coding-agents/) — parallel agents and task ownership

### Enterprise
Org-level deployment, security, SSO, team management, BYOLLM and analytics.

- [Architecture and deployment](https://docs.warp.dev/enterprise/enterprise-features/architecture-and-deployment/) — Warp-hosted, self-hosted, hybrid
- [Security overview](https://docs.warp.dev/enterprise/security-and-compliance/security-overview/) — data handling and compliance
- [Bring Your Own LLM](https://docs.warp.dev/enterprise/enterprise-features/bring-your-own-llm/) — inference through Bedrock or Vertex

### Plans, billing, privacy, support
Pricing, usage and agent-hour billing, privacy controls, troubleshooting.

- [Platform usage](https://docs.warp.dev/support-and-community/plans-and-billing/platform-credits/) — agent-hour charges for cloud runs
- [Usage and billing](https://docs.warp.dev/support-and-community/plans-and-billing/credits/) — inference, compute, platform costs
- [Secret Redaction](https://docs.warp.dev/support-and-community/privacy-and-security/secret-redaction/) — masking secrets before server send

### Terminal, Code, Warp Drive, getting started, changelog
Core Warp app: terminal (blocks, tabs, settings), code editor and review, Warp Drive, install and migration, release notes.

- [Warp products overview](https://docs.warp.dev/) — how terminal, agents, automation, factories fit
- [Code Review panel](https://docs.warp.dev/code/code-review/) — reviewing agent diffs
- [Warp Drive overview](https://docs.warp.dev/knowledge-and-collaboration/warp-drive/) — shared prompts, rules, notebooks

### API errors and OpenAPI
18 per-code error pages exist under /factories/api-and-sdk/troubleshooting/errors/<code>/ (agent_process_failed, budget_exceeded, and others); only the errors index is ingested. Machine-readable API specs also exist.

- [Oz Agent API (OpenAPI spec, YAML)](https://docs.warp.dev/openapi.yaml) — full endpoint schema
- [Oz Agent API (OpenAPI spec, JSON)](https://docs.warp.dev/openapi.json) — same spec in JSON
- [insufficient_credits](https://docs.warp.dev/factories/api-and-sdk/troubleshooting/errors/insufficient-credits/) — sample error page, URL pattern for the rest

## Pulling more

Ingest the catalog again with a new intent, or ask a question the pages above
do not answer — the query path fetches from this catalog (`QUERY.md` Q.6b).
