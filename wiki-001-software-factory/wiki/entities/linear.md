---
type: entity
title: Linear
description: Issue tracker that Warp Factories supports as a work source, where issues and comments trigger a factory and progress is written back to the issue.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-automations]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-api]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
related:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/jira]]"
  - "[[wiki/entities/slack]]"
  - "[[wiki/entities/github]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/foreman-agent]]"
created: 2026-10-25T16:00:00Z
timestamp: 2026-10-25T16:00:00Z
source_count: 20
---

# Linear

> Issue tracker; in this wiki, one of the work sources a Warp factory listens to and reports back to.

## Definition

Every source here treats Linear as an integration of Warp Factories, not as a subject in itself. A factory takes Linear issues, comments and agent sessions as triggers, then keeps the issue updated as work moves through stages. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories]]

Voice warning: all 20 pages trace to Warp (19 pages of its docs set plus the warp-factory-examples repo). That is one vendor's voice, so agreement among them is not independent corroboration. The repo only shows Linear used as configured, not an outside check.

## Key claims

- Two entry paths: agent sessions (mention, assign or delegate the Warp app) and automation triggers on issue and comment events. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]]
- Setup is Linear OAuth once per workspace, then pick teams. Warp adds a default automation routing new agent sessions from those teams to the factory. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]
- Five automation triggers: issue created, labeled, state changed, assigned, and comment created. Filters cover team, project, issue, labels, state and people. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories-automations]]
- The repo examples use the provider `linear` with the event `agent_session_created`, and a Linear session as one of the three entry points into the foreman. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Later matching events on a linked issue continue the same work item. One comment can match both a session route and a comment trigger and start two runs; scope automations so one path owns each request. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]
- The factory posts plans, actions and results, attaches GitHub PRs, and updates workflow state. Its own Linear activity never triggers automations, so there is no self-loop. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]]
- Linear auth grants no repo access: PRs use the factory's code-host credentials, and a human still reviews and merges. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]
- Agent sessions need a Warp account linked to the Linear user. Troubleshooting also lists the linked account as a cause when an event starts nothing. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]
- Choosing Linear adds its built-in skill to the agents. The foreman handle is the name teams @-mention in Slack and Linear. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]
- API dispatch accepts `ticket_ref` such as `linear:PAY-123`. The follow-up endpoint is the same capability the Slack and Linear integrations use. [[wiki/docs/llms-docs-warp-dev/factories-factory-api]], [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]
- Factory MCP resolves a task reference from a Linear issue. Notification delivery, such as to a Linear issue, is best-effort. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]

## Tensions

- Linear and Jira cannot both be connected to one factory, although other sources can be combined. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]

## Relationships

- **Warp Factories**: the host system that consumes Linear events. [[wiki/entities/warp-factories]]
- **Jira**: the alternative tracker, mutually exclusive with Linear per factory. [[wiki/entities/jira]]
- **Slack**: sibling conversational entry point, with the same foreman handle. [[wiki/entities/slack]]
- **Human in the loop**: the PR still waits for a person. [[wiki/concepts/human-in-the-loop]]

> Synthesis: Linear shows up only as an adapter inside one vendor's product; the wiki has no independent witness on Linear itself.
