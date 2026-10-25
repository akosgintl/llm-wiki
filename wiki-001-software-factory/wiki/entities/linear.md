---
type: entity
title: Linear
description: Issue tracker that agent-factory products (Warp Factories, Factory, Mastra Factory) support as a work source, where issues and comments trigger agents and progress is written back to the issue.
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
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-quickstart]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-docker]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/docs/llms-docs-factory-com/delegations-index]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-automations]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-overview]]"
  - "[[wiki/docs/llms-factory-mastra-ai/what-is-factory]]"
  - "[[wiki/docs/llms-factory-mastra-ai/using-intake]]"
  - "[[wiki/docs/llms-factory-mastra-ai/using-work-and-approvals]]"
  - "[[wiki/docs/llms-factory-mastra-ai/configure-boards-and-rules]]"
related:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/mastra-factory]]"
  - "[[wiki/entities/jira]]"
  - "[[wiki/entities/slack]]"
  - "[[wiki/entities/github]]"
  - "[[wiki/entities/microsoft-teams]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/foreman-agent]]"
created: 2026-10-25T16:00:00Z
timestamp: 2026-10-25T18:32:29Z
source_count: 26
---

# Linear

> Issue tracker; in this wiki, a work source and delegation surface that three agent-factory products listen to and report back to.

## Definition

No source treats Linear as a subject in itself. Each treats it as an integration: issues, comments and agent sessions in Linear start agent work, and the issue is updated as work proceeds. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories]]

The three products frame it differently. Warp Factories uses Linear as one of several triggers and reply channels for a foreman agent. [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]] Factory (Droid) lists it as a delegation app: mention `@Factory` or assign an issue. [[wiki/docs/llms-docs-factory-com/delegations-index]] Mastra Factory treats it as an intake source whose issues become Work cards. [[wiki/docs/llms-factory-mastra-ai/using-intake]]

Voice warning: the 26 pages come from four origins: the Warp docs set (18 pages), the warp-factory-examples repo (1, which only shows Linear used as configured), the Factory docs set (3) and the Mastra Factory docs set (4). Pages inside one origin are one vendor voice and do not corroborate each other. Only claims that recur across origins count as corroborated.

## Key claims

### Warp Factories

- Two entry paths: agent sessions (mention, assign or delegate the Warp app) and automation triggers on issue and comment events. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]]
- Setup is Linear OAuth once per workspace, then pick teams. Warp adds a default automation routing new agent sessions from those teams to the factory. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]
- Five automation triggers: issue created, labeled, state changed, assigned, and comment created. Filters cover team, project, issue, labels, state and people. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories-automations]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]
- The repo examples use provider `linear` with event `agent_session_created`; a Linear session is one of three entry points into the foreman. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Later matching events on a linked issue continue the same work item. One comment can match both a session route and a comment trigger and start two runs; scope automations so one path owns each request. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]
- The factory posts plans, actions and results, attaches GitHub PRs, and updates workflow state. Its own Linear activity never triggers automations, so there is no self-loop. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]]
- Linear auth grants no repo access: PRs use the factory's code-host credentials, and a human still reviews and merges. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]
- Agent sessions need a Warp account linked to the Linear user; the linked account is also a listed cause when an event starts nothing. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]
- The factory name sets the default foreman handle that teams @-mention in Slack and Linear. Choosing Linear adds its built-in skill to the agents. [[wiki/docs/llms-docs-warp-dev/factories-quickstart]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]
- API dispatch accepts `ticket_ref` such as `linear:PAY-123`. The follow-up endpoint is the same capability the Slack and Linear integrations use. [[wiki/docs/llms-docs-warp-dev/factories-factory-api]], [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]
- Factory MCP resolves a task reference from a Linear issue. Notification delivery, such as to a Linear issue, is best-effort. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]
- Linear is among the triggers the Automation Platform orchestrates for self-hosted workers (Docker, Direct), and among the ways to start work when a code forge has no native events. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-docker]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]], [[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]], [[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]
- The dashboard lists Linear events among automation triggers. [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]

### Factory (Droid)

- Delegations hand work to Droid from Slack, Linear, Jira and Microsoft Teams. An admin configures identity and compute once in the Apps agent profile. Shared issue delegations run as a service account with its Git credentials. [[wiki/docs/llms-docs-factory-com/delegations-index]]
- Each Linear workspace connects to only one Factory organization at a time. [[wiki/docs/llms-docs-factory-com/delegations-index]]
- Direct delegation from Linear is separate and needs no Software Factory automation. In the SDLC coverage view, Slack and Linear delegation count as Code-gen, with integration coverage. [[wiki/docs/llms-docs-factory-com/software-factory-overview]]
- The automations page documents triggers as schedule, Slack, GitHub and webhook. It does not list Linear as an automation trigger. [[wiki/docs/llms-docs-factory-com/software-factory-automations]]

### Mastra Factory

- Linear can supply issues. They become Work cards after intake, but Linear items need organization routing to a Factory and board; GitHub issues do not. [[wiki/docs/llms-factory-mastra-ai/what-is-factory]], [[wiki/docs/llms-factory-mastra-ai/using-intake]]
- Issue selection is personal per teammate; Linear routing is shared. For missing items, check routing among other causes. [[wiki/docs/llms-factory-mastra-ai/using-intake]]
- Linear completed or canceled states move the Work card to Done or Canceled. Delivery and reconciliation are asynchronous. [[wiki/docs/llms-factory-mastra-ai/using-work-and-approvals]]
- Linear event rules live on the integration, not on the board. [[wiki/docs/llms-factory-mastra-ai/configure-boards-and-rules]]

## Tensions

- Warp: Linear and Jira cannot both be connected to one factory, although other sources can be combined. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]] Factory's Delegations lists both as apps with no such exclusion stated. [[wiki/docs/llms-docs-factory-com/delegations-index]] The scopes differ (a factory against an organization), so this may not be a real conflict.
- Direction of flow differs. Warp has Linear events fire automations and the factory writes back. [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]] Factory treats Linear as delegation, outside its automation triggers. [[wiki/docs/llms-docs-factory-com/software-factory-automations]], [[wiki/docs/llms-docs-factory-com/software-factory-overview]] Mastra treats it as passive intake, with a person or trust policy deciding what starts. [[wiki/docs/llms-factory-mastra-ai/using-intake]]

## Relationships

- **Warp Factories**: host system consuming Linear events. [[wiki/entities/warp-factories]]
- **Mastra Factory**: intake and state sync with Linear. [[wiki/entities/mastra-factory]]
- **Jira**: alternative tracker, mutually exclusive with Linear per Warp factory. [[wiki/entities/jira]]
- **Slack**: sibling conversational entry point. [[wiki/entities/slack]]
- **Microsoft Teams**: another delegation surface in Factory. [[wiki/entities/microsoft-teams]]
- **GitHub**: receives the PRs; Linear itself grants no repo access. [[wiki/entities/github]]
- **Human in the loop**: the PR still waits for a person. [[wiki/concepts/human-in-the-loop]]

> Synthesis: Linear appears only as an adapter inside vendors' products, now across four origins. Across origins it is consistently where requests arrive and status returns, while repo access and merge approval stay elsewhere. The wiki still has no independent witness on Linear itself.
