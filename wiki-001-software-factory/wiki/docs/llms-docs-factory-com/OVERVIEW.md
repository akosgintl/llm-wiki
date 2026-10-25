---
type: docs
title: Factory Documentation
description: Documentation for Factory, an agent-native software development platform built around the Droid coding agent, covering apps, automations, missions, environments, harness extensions, safety and enterprise deployment.
original_path: https://docs.factory.com/llms.txt
source_url: https://docs.factory.com/llms.txt
catalog: raw/docs/llms-docs-factory-com/llms.txt
catalog_size: 120
created: 2026-10-25T18:25:22Z
timestamp: 2026-10-25T18:25:22Z
---

# Factory Documentation — Docs map

> Catalog: https://docs.factory.com/llms.txt · 120 links · 10 ingested

## Ingested

- [[wiki/docs/llms-docs-factory-com/software-factory-overview|Software Factory]]
- [[wiki/docs/llms-docs-factory-com/welcome-index|Welcome to Factory]]
- [[wiki/docs/llms-docs-factory-com/delegations-index|Delegations]]
- [[wiki/docs/llms-docs-factory-com/missions-overview|Factory Missions]]
- [[wiki/docs/llms-docs-factory-com/environments-overview|Environments]]
- [[wiki/docs/llms-docs-factory-com/software-factory-automations|Custom Automations]]
- [[wiki/docs/llms-docs-factory-com/droid-exec-overview|Droid Exec (Headless)]]
- [[wiki/docs/llms-docs-factory-com/agent-readiness-overview|Agent Readiness]]
- [[wiki/docs/llms-docs-factory-com/harness-subagents|Custom droids (subagents)]]
- [[wiki/docs/llms-docs-factory-com/harness-skills|Skills]]

## Areas

### Product surfaces and getting started

Plans, models, support, and the ways to run Droid: Factory App, Droid CLI, IDE integrations.

- [Factory App](https://docs.factory.com/factory-app/overview.md) — visual Droid workspace with reviewable sessions
- [Droid CLI](https://docs.factory.com/droid-cli/overview.md) — terminal entry point to the agent
- [Worktrees in the Factory App](https://docs.factory.com/factory-app/worktrees.md) — parallel sessions in isolated Git worktrees
- [Available Models](https://docs.factory.com/models.md) — which models the platform offers
- [Droid CLI Reference](https://docs.factory.com/droid-cli/cli-reference.md) — commands and flags

### Software Factory automations

The SDLC automations that Software Factory manages: triage, review, QA, release, incident response.

- [Triage](https://docs.factory.com/software-factory/triage.md) — classify and route inbound work
- [Automated Code Review](https://docs.factory.com/software-factory/code-review-ci.md) — PR review loop in CI
- [Automated QA](https://docs.factory.com/software-factory/automated-qa.md) — end-to-end testing as a real user
- [Incident Response](https://docs.factory.com/software-factory/incident-response.md) — autonomous handling of production alerts
- [Security Review](https://docs.factory.com/software-factory/security-review.md) — security-focused PR reviews and audits

### AutoWiki

Generated repository wikis: creation, browsing, automatic refresh, API. Close to this wiki's own subject.

- [AutoWiki](https://docs.factory.com/software-factory/wiki/overview.md) — generated repo wikis
- [Initialize a Wiki](https://docs.factory.com/software-factory/wiki/generate.md) — the /wiki command
- [Automatic Refresh](https://docs.factory.com/software-factory/wiki/auto-refresh.md) — regenerate on every push via CI
- [AutoWiki API](https://docs.factory.com/api-reference/wiki.md) — programmatic runs, search, export

### Missions

Large multi-feature projects with orchestrator and workers: planning, validation, running in CLI or App.

- [Planning & Validation](https://docs.factory.com/missions/planning.md) — scoping milestones and validation frequency
- [Running in the CLI](https://docs.factory.com/missions/running-cli.md) — Mission Control, worker monitoring
- [Running in the Factory App](https://docs.factory.com/missions/running-app.md) — app-side mission execution
- [Missions Configuration & Reference](https://docs.factory.com/missions/reference.md) — headless missions, settings, access policy

### Compute: Droid Computers, Environments, OpenCompute

Where agents run: persistent computers, reusable cloud environments, self-hosted sandboxes.

- [Droid Computers](https://docs.factory.com/droid-computers/overview.md) — persistent managed compute for Droid
- [Run Droids on an Environment](https://docs.factory.com/environments/run-droids.md) — baselines for automations and missions
- [Create an Environment](https://docs.factory.com/environments/create.md) — build steps and repo cloning
- [OpenCompute](https://docs.factory.com/opencompute/overview.md) — sandboxes in your own cloud
- [Remote Control](https://docs.factory.com/remote-control.md) — drive your machine from web or other devices

### Delegations (chat and ticket integrations)

Hand work to Droid from team tools.

- [Slack](https://docs.factory.com/delegations/slack.md) — delegate from channels and DMs
- [Linear](https://docs.factory.com/delegations/linear.md) — delegate issues to Droid
- [Jira](https://docs.factory.com/delegations/jira.md) — Jira Cloud issue delegation
- [Microsoft Teams](https://docs.factory.com/delegations/microsoft-teams.md) — channel mention delegation

### Headless execution, SDKs and API

Programmatic use: CI recipes, SDKs, REST API.

- [Droid TypeScript SDK](https://docs.factory.com/sdk/typescript.md) — build custom agents and workflows
- [Droid Python SDK](https://docs.factory.com/sdk/python.md) — same, in Python
- [Droid Sessions API](https://docs.factory.com/api-reference/sessions.md) — drive sessions programmatically
- [Dependency scan with Droid Exec](https://docs.factory.com/droid-exec/recipes/dependency-secret-scan.md) — scheduled CI workflow example
- [CI Automations API](https://docs.factory.com/api-reference/automations-ci.md) — manage CI automation workflows

### Agent readiness and effectiveness

Readiness scoring of repositories and measurement of agent output and spend.

- [Readiness Report Command](https://docs.factory.com/agent-readiness/readiness-report.md) — /readiness-report evaluation
- [Readiness Dashboard](https://docs.factory.com/agent-readiness/dashboard.md) — org-level readiness scores
- [Agent Effectiveness](https://docs.factory.com/agent-effectiveness/overview.md) — shipping speed and spend attribution
- [Cost & Productivity](https://docs.factory.com/agent-effectiveness/cost-and-productivity.md) — spend control and impact measurement

### Autonomy and safety

How much Droid may do unattended, and the guardrails around it.

- [Autonomy Level](https://docs.factory.com/autonomy-and-safety/auto-run.md) — Off to High confirmation levels
- [Interaction Modes](https://docs.factory.com/autonomy-and-safety/specification-mode.md) — Normal, Spec, Mission modes
- [Permission rules](https://docs.factory.com/autonomy-and-safety/permission-rules.md) — allow or block shell commands
- [Sandbox](https://docs.factory.com/autonomy-and-safety/sandbox.md) — OS-level isolation
- [Droid Shield](https://docs.factory.com/autonomy-and-safety/droid-shield.md) — secret detection before commits

### Harness and extensibility

Project instructions, tool connections, and shareable agent packages.

- [AGENTS.md](https://docs.factory.com/harness/agents-md.md) — durable project instructions
- [Hooks](https://docs.factory.com/harness/hooks.md) — deterministic commands at lifecycle events
- [Plugins](https://docs.factory.com/harness/plugins.md) — packaged skills, commands, droids, hooks
- [Model Context Protocol (MCP)](https://docs.factory.com/harness/mcp.md) — connect custom tools
- [Custom Slash Commands](https://docs.factory.com/harness/custom-slash-commands.md) — reusable prompts and scripts

### Model independence

Model selection and bring-your-own-model options.

- [Factory Router](https://docs.factory.com/model-independence/factory-router.md) — automatic model choice per task
- [Custom Models (BYOK)](https://docs.factory.com/model-independence/byok.md) — own keys, open source, local models

### Enterprise, identity and governance

Deployment patterns, org structure, access, data flows, telemetry, audit.

- [Factory for Enterprise](https://docs.factory.com/enterprise/index.md) — cloud, hybrid, airgapped overview
- [Enterprise Controls & Managed Settings](https://docs.factory.com/enterprise/hierarchical-settings-and-org-control.md) — org-wide policy
- [Identity & Access](https://docs.factory.com/enterprise/identity-and-access.md) — SSO, roles, service accounts
- [Telemetry & Analytics](https://docs.factory.com/enterprise/telemetry/index.md) — OpenTelemetry export of usage and cost
- [Audit Log](https://docs.factory.com/enterprise/audit-log.md) — who did what in the org

### Benchmarks, changelog and API contract

Evaluation results, release notes, and the machine-readable API.

- [Terminal Bench](https://docs.factory.com/benchmarks/terminal-bench.md) — agent benchmark results
- [Review Benchmark](https://docs.factory.com/benchmarks/review-benchmark.md) — code review model results
- [Full Changelog](https://docs.factory.com/changelog/release-notes.md) — what changed across surfaces
- [Factory API](https://docs.factory.com/api-reference.md) — public API contract
- [Factory OpenAPI specification](https://docs.factory.com/openapi.json) — machine-readable operations

## Pulling more

Ingest the catalog again with a new intent, or ask a question the pages above
do not answer — the query path fetches from this catalog (`QUERY.md` Q.6b).
