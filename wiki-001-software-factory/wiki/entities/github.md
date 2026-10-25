---
type: entity
title: GitHub
description: "GitHub is the code forge that factory products use as event source, PR destination, review gate and optional home for git-synced factory definitions."
aliases: []
sources:
  - "[[wiki/docs/llms-docs-8090-ai/codebase-overview]]"
  - "[[wiki/docs/llms-docs-8090-ai/connections-connect-coding-agent]]"
  - "[[wiki/docs/llms-docs-8090-ai/general-introduction]]"
  - "[[wiki/docs/llms-docs-8090-ai/modules-work-orders]]"
  - "[[wiki/docs/llms-docs-8090-ai/opinions-reverse-engineering]]"
  - "[[wiki/docs/llms-docs-factory-com/delegations-index]]"
  - "[[wiki/docs/llms-docs-factory-com/droid-exec-overview]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-automations]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-overview]]"
  - "[[wiki/docs/llms-docs-port-io/agent-management-skills-overview]]"
  - "[[wiki/docs/llms-docs-port-io/guides-all-trigger-ai-coding-assistants-from-port]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-demo-sentry-monitoring-with-sdk]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-automations]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-github]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-quickstart]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-private-container-registry]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks-vercel]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/docs/llms-factory-mastra-ai/configure-boards-and-rules]]"
  - "[[wiki/docs/llms-factory-mastra-ai/configure-github]]"
  - "[[wiki/docs/llms-factory-mastra-ai/using-intake]]"
  - "[[wiki/docs/llms-factory-mastra-ai/using-reviews]]"
  - "[[wiki/docs/llms-factory-mastra-ai/using-work-and-approvals]]"
  - "[[wiki/docs/llms-factory-mastra-ai/what-is-factory]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
related:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/mastra-factory]]"
  - "[[wiki/entities/gitlab]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/webhook]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/software-factory]]"
created: 2026-10-25T00:00:00Z
timestamp: 2026-10-25T18:32:14Z
source_count: 42
---

# GitHub

> Code forge that every factory product in the wiki integrates: event source for agent work, destination for agent PRs, and (for Warp) optional config store.

## Definition

Across five origins GitHub is the best-supported code host, usually via a vendor-installed GitHub App. Warp, 8090, Factory, Mastra and Port all treat it as one of several work sources next to GitLab, Slack, Linear and Jira. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]], [[wiki/docs/llms-docs-8090-ai/codebase-overview]], [[wiki/docs/llms-factory-mastra-ai/configure-github]]

Voice warning: the Warp docs and both Warp repos are one vendor voice. The other four sets (8090, Factory, Port, Mastra) are each their own origin.

## Key claims

**Event source and intake**
- Warp: a GitHub App feeds issues, PRs, reviews, push, check suites and workflow runs into automations; a `factory:<alias>` label plus @warp mention routes work. Bot events are skipped by default. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]], [[wiki/docs/llms-docs-warp-dev/factories-automations]], [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]
- Mastra: each issue after connection becomes a Work item, each PR a Review item. Epics and sub-issues are ignored. A Platform-backed App or a self-owned App (`GITHUB_APP_*`) is used. [[wiki/docs/llms-factory-mastra-ai/configure-github]], [[wiki/docs/llms-factory-mastra-ai/using-intake]]
- Mastra: closing an issue maps to Done or Canceled; merging a PR completes its Review card. [[wiki/docs/llms-factory-mastra-ai/using-work-and-approvals]]
- Factory: GitHub is an automation trigger; custom GitHub automations run in GitHub Actions and need a setup PR merged first. [[wiki/docs/llms-docs-factory-com/software-factory-automations]]

**Code index and traceability**
- 8090 indexes a connected repo per branch and reindexes on push. Drift Bot reviews PRs against Blueprints and Requirements. PRs link to Work Orders via `WO-123`-style IDs. [[wiki/docs/llms-docs-8090-ai/codebase-overview]], [[wiki/docs/llms-docs-8090-ai/modules-work-orders]]

**PRs, CI and the human gate**
- Output returns as branches and PRs; branch protection and required reviews are the human gate. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]], [[wiki/docs/llms-factory-mastra-ai/using-reviews]]
- Factory: GitHub blocks self-approval, but the requester can still approve a Factory-authored PR. [[wiki/docs/llms-docs-factory-com/delegations-index]]
- Port: workflows dispatch GitHub Actions that run Copilot, Claude Code or Gemini CLI and open PRs. [[wiki/docs/llms-docs-port-io/guides-all-trigger-ai-coding-assistants-from-port]]
- Factory ships `droid-action` for PR review. Warp's `common-skills` repo uses Actions for lockfile PRs and CI review. [[wiki/docs/llms-docs-factory-com/droid-exec-overview]], [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]

**Definitions as code**
- Warp: definitions, agents and skills can live in a team GitHub repo; merges to the production branch apply them, and a `warp/factory-config` check validates PRs. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Port syncs skills from GitHub through its Ocean integration. [[wiki/docs/llms-docs-port-io/agent-management-skills-overview]]

## Tensions

- GitHub vs GitLab: Warp says GitLab cannot yet host definitions. 8090 and Factory treat both as peers but with different auth: GitLab needs a token plus a role or plan. Only vendor docs say this. [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]], [[wiki/docs/llms-docs-8090-ai/codebase-overview]], [[wiki/docs/llms-docs-factory-com/delegations-index]]

## Relationships

- **Warp Factories**, **Mastra Factory**: GitHub is the main work source. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]], [[wiki/docs/llms-factory-mastra-ai/what-is-factory]]
- **GitLab**: parallel, less complete integration. [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]
- **Human in the loop**: merge and review gates are GitHub policy. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]]

> Synthesis: GitHub is the shared substrate of the factory category, but every claim is vendor-authored; Warp contributes most pages and counts as one voice.
