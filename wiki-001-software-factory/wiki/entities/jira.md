---
type: entity
title: Jira
description: Atlassian issue tracker that Warp Factories, Factory Delegations and Port's ticket-resolution pattern all use as a work source from which tickets trigger AI agents.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-automations]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-api]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/docs/llms-docs-factory-com/delegations-index]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-overview]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-automations]]"
  - "[[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]"
related:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/linear]]"
  - "[[wiki/entities/slack]]"
  - "[[wiki/entities/github]]"
  - "[[wiki/entities/claude-code]]"
  - "[[wiki/entities/microsoft-teams]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/mcp]]"
created: 2026-10-25T18:31:55Z
timestamp: 2026-10-25T18:31:55Z
source_count: 17
---

# Jira

> Issue tracker; in this wiki, a ticket source whose work items start AI-agent runs in three different products.

## Definition

Across the sources Jira is never the subject. It is an intake and status surface: a person assigns or mentions an agent on a work item, and the product runs the work and reports back. Three origins use it this way: Warp Factories, Factory's Delegations, and Port's autonomous ticket resolution pattern. [[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]], [[wiki/docs/llms-docs-factory-com/delegations-index]], [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]

Voice warning: 14 of 17 pages are one Warp docs set, so Warp's many mentions are one voice. Factory (3 pages) and Port (1 page) are separate vendors, but each is also vendor documentation of its own product.

## Key claims

- Warp supports Jira Cloud only (not Server or Data Center). Assigning or mentioning Warp on a work item opens a Jira agent session, an automation routes it to an agent, and progress and result show in that session. [[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]]
- Setup is two-level: a Jira site admin installs the Warp app once per workspace, then each factory opts in under Settings > Integrations and picks projects. Non-admins can send an approval link that expires after seven days. [[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]]
- Only one Jira event exists, `agent_session_created`. Filters are `project_keys` and `keywords`. As code: `integrations: [{type: jira}]` plus an automation with `provider: jira`. [[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/docs/llms-docs-warp-dev/factories-automations]]
- Jira events reach every automation in the workspace, so another team's broader filter can start its own run on the same item. Filters do not control access. [[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]]
- The agent does not comment on the item unless asked. When asked it can update fields, comment, transition status, change labels or reassign, within Jira permissions. [[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]]
- The connected Jira user becomes the run's creator, but the run executes as the automation's agent. Jira access gives no repository access; code access comes from the factory. [[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]]
- For runs without a human creator (scheduled, service account, API key), Warp says to add the Atlassian MCP server as a managed MCP install. [[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]]
- Choosing Jira adds its built-in skill to the agents. Linear and Jira tools are auto-provided and are Warp-managed, separate from user-configured MCP servers. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]
- API dispatch accepts `ticket_ref` as `jira:PROJ-456`. Factory MCP resolves a task reference from a Jira issue. [[wiki/docs/llms-docs-warp-dev/factories-factory-api]], [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]
- Jira also appears as an automation trigger in the dashboard and as a start point for forges without native events (Bitbucket, Azure DevOps Server, self-managed GitLab). [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]], [[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]
- A Jira event that starts nothing can be caused by a missing linked Warp account. [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]
- Factory's Delegations lets a team hand work to Droid from Slack, Linear, Jira and Microsoft Teams by mention or assignment. Each Jira site connects to only one Factory organization at a time. [[wiki/docs/llms-docs-factory-com/delegations-index]]
- In Factory's Software Factory dashboard, delegation from Jira is separate and needs no Software Factory automation. [[wiki/docs/llms-docs-factory-com/software-factory-overview]]
- Port's reference workflow runs Jira ticket, catalog enrichment, AI readiness scoring, Slack approval, then Cursor delegation. Other guides delegate Jira tickets to Claude Code or GitHub Copilot via Port-native orchestration or n8n. [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]

## Tensions

- Warp says multiple sources may be connected, but not Linear and Jira at once. Factory's Delegations lists Slack, Linear, Jira and Teams together with no such restriction stated. These may describe different products and scopes, so this is a difference, not proof of conflict. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]], [[wiki/docs/llms-docs-factory-com/delegations-index]]
- Port places a human approval (Slack) before the agent starts on a Jira ticket. Warp starts a run directly on assign or mention, and the human gate comes at spec and merge. [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]], [[wiki/docs/llms-docs-warp-dev/factories]]

## Relationships

- **Warp Factories**: host product that consumes Jira agent sessions. [[wiki/entities/warp-factories]]
- **Linear**: sibling tracker with richer triggers (five events versus one), and exclusive with Jira per Warp factory. [[wiki/entities/linear]]
- **Slack**: companion entry point and approval surface. [[wiki/entities/slack]]
- **Claude Code**: one of the agents Port delegates Jira tickets to. [[wiki/entities/claude-code]]
- **MCP**: route for Jira access when no human creator exists. [[wiki/concepts/mcp]]

> Synthesis: Jira is a ticket adapter in three vendors' products; the Warp pages dominate the count but are one voice, so independent corroboration comes only from Factory and Port.
