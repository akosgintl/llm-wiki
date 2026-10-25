---
type: entity
title: GitLab
description: "GitLab is a code forge that the wiki's software-factory docs support as a work source and repository host, with a thinner integration than GitHub."
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-automations]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-quickstart]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/docs/llms-docs-factory-com/delegations-index]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-automations]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-overview]]"
related:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/github]]"
  - "[[wiki/entities/azure-devops]]"
  - "[[wiki/concepts/webhook]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/human-in-the-loop]]"
created: 2026-10-25T18:30:26Z
timestamp: 2026-10-25T18:30:26Z
source_count: 14
---

# GitLab

> Code forge that factory products connect to as an event source and repo host; supported, but behind GitHub.

## Definition

In this wiki GitLab appears only through two vendors' docs sets: Warp Factories (11 pages, one origin and one voice) and Factory's Software Factory and delegations docs (3 pages, a second origin). It is one of several work sources beside Slack, Linear, Jira, GitHub and Azure DevOps. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/docs/llms-docs-factory-com/software-factory-overview]]

## Key claims

**Warp integration**
- One top-level GitLab.com group links to one Warp workspace. Warp creates service accounts in the group: a manager account per workspace and a bot account per factory. A group webhook delivers merge request and comment events. [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]
- Prerequisites: group Owner access and a Premium or Ultimate plan for service accounts and group webhooks. Without group webhooks, credentials work but GitLab cannot trigger runs. [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]], [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]
- Two triggers: merge request events (opened, updated, closed, reopened, merged, approved) and bot mentions. Filters are project, action and base branch. Mentions count only in new comments, and the factory's own service accounts never trigger work. [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]], [[wiki/docs/llms-docs-warp-dev/factories-automations]], [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]
- The factory pushes `factory/<slug>` branches, opens draft merge requests and posts review feedback. It never merges or approves. Runs use short-lived tokens scoped to the bot's Developer role. [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]
- GitLab.com is a first-class option in the setup wizard and in Factory MCP onboarding. [[wiki/docs/llms-docs-warp-dev/factories-quickstart]], [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]
- Merge-request metrics (PRs merged, cycle time, autonomy) need the GitLab webhook Warp installs. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]]
- Triggers can be declared as code (`provider: gitlab`, `event: merge_request`). [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]

**Self-managed GitLab**
- Warp treats self-managed GitLab as an unsupported forge: create the factory with no repo, store a token as Agent Secret `CODE_FORGE_TOKEN`, and clone from default-runner setup commands. This gives repo access only, with no GitLab events or automations. [[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]

**Factory (second origin)**
- GitLab is a Software Factory automation source and a dashboard integration filter. [[wiki/docs/llms-docs-factory-com/software-factory-automations]], [[wiki/docs/llms-docs-factory-com/software-factory-overview]]
- Shared delegations clone and push as a service account. For GitLab and GitLab Self-Hosted this needs a group access token with `api` scope and at least Developer role. [[wiki/docs/llms-docs-factory-com/delegations-index]]

## Tensions

- Self-managed GitLab: Factory's delegations docs list "GitLab Self-Hosted" as a supported repository type with a group token. Warp's docs treat self-managed GitLab as a repo-only workaround without events. Different products, so this may be a real capability gap rather than a conflict. [[wiki/docs/llms-docs-factory-com/delegations-index]], [[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]
- GitLab vs GitHub within Warp: GitLab cannot host factory definitions yet; definitions must be Warp-managed or GitHub-hosted. Only Warp says this. [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]

## Relationships

- **GitHub**: parallel, more complete forge integration. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]
- **Azure DevOps**: sibling forge handled in the same wizard and workaround docs. [[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]
- **Human in the loop**: merge and approval stay with the team. [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]

> Synthesis: GitLab is a second-tier forge in both vendors' products. Warp's pages are one voice (docs from one vendor), so only Factory's delegations page independently mentions GitLab, and only for access tokens.
