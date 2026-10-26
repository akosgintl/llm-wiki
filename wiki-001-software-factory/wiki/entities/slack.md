---
type: entity
title: Slack
description: "Slack is the team chat tool that several software-factory products use as an intake, delegation and status surface, and that Warp's example skills use as a feedback sink."
aliases: []
sources:
  - "[[wiki/docs/llms-docs-8090-ai/general-introduction]]"
  - "[[wiki/docs/llms-docs-factory-com/delegations-index]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-automations]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-overview]]"
  - "[[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-automations]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-quickstart]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-docker]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/docs/llms-factory-mastra-ai/using-intake]]"
  - "[[wiki/docs/llms-factory-mastra-ai/using-sessions]]"
  - "[[wiki/docs/llms-factory-mastra-ai/what-is-factory]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/sources/youtube-XUEfIxkdT2Q]]"
related:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/microsoft-teams]]"
  - "[[wiki/entities/github]]"
  - "[[wiki/entities/linear]]"
  - "[[wiki/entities/claude-code]]"
  - "[[wiki/concepts/foreman-agent]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/software-factory]]"
created: 2026-10-25T15:20:00Z
timestamp: 2026-10-26T07:12:42Z
source_count: 29
---

# Slack

> Team chat tool. Across the sources it is a front door to a software factory: people mention or DM an agent, and progress and results return to the same thread.

## Definition

No source defines Slack itself. They describe how it plugs into factory products. In Warp Factories it is one of several work sources (Slack, Microsoft Teams, GitHub, GitLab, Azure DevOps, Linear, Jira, plus webhooks, endpoints, Factory MCP and direct runs). [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]] Other vendors treat it the same way: Factory (factory.com) lists it first among Delegations apps [[wiki/docs/llms-docs-factory-com/delegations-index]]; 8090 lists it among connections [[wiki/docs/llms-docs-8090-ai/general-introduction]]; Mastra Factory calls Slack and browsers its user surfaces [[wiki/docs/llms-factory-mastra-ai/what-is-factory]].

A second, smaller use appears in Warp's skills repo: Slack as a sink for agent feedback. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]

> Synthesis: The 29 pages come from five vendor doc sets (Warp, Factory, 8090, Port, Mastra), two Warp-authored repos and one podcast. Each docs set or repo is one origin, so Warp's 23 pages count as one voice. The podcast guest is Warp's CEO, so it is not independent of the Warp docs. Across vendors, Slack is consistently an intake and interaction surface, which is real cross-vendor agreement on its role. Details below are mostly single-vendor claims.

## Key claims

**Install and identity**
- Each factory installs as its own Slack app, with the factory's name and avatar. One channel can host several factories. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]
- Install starts at factory creation or in Settings. An admin may need to approve it. The app must be invited to each channel, and always to private ones. A 👀 reaction confirms pickup. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]
- Slack is optional at setup and can be added later. [[wiki/docs/llms-docs-warp-dev/factories-quickstart]]
- The foreman handle used for @-mentions defaults to the factory name. It is editable in Settings or via `alias` in the definition. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/docs/llms-docs-warp-dev/factories-quickstart]]

**Starting work**
- A mention or DM starts work with the conversation as context. Progress shows live in the thread. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]], [[wiki/docs/llms-docs-warp-dev/factories-quickstart]]
- Starting by mention or DM needs a Slack account linked to an active member of the factory's Warp team. Automation-started work runs as the chosen factory agent, not the triggerer. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]
- Automation triggers: app mention, DM received (`message_dm`), channel message, reaction added, member joined. Filters cover conversations, people, keywords and emoji. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]], [[wiki/docs/llms-docs-warp-dev/factories-automations]]
- One Slack message can match several automations and start several runs. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]
- Example automations: a `:ticket:` reaction files a GitHub issue. A nightly cron digest posts to an explicit channel ID. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]] The example repo lists "Slack reaction intake" in its standing-automation catalog and shows the `slack/app_mention` and `message_dm` providers. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

**Output and tools**
- Warp gives agents built-in Slack tools (read channels and threads, reply, post top-level). No separate Slack MCP server is needed. Linear and Jira get the same treatment. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]
- The Slack skill is built in for the foreman. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]
- A thread reply continues work only if the thread already has a work item. The app's Home tab groups items by stage (Triage to Cancelled). [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]
- Work from Slack still ends at a pull request for a person to review. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]
- Factory MCP resolves a Slack permalink as a task reference. Notification delivery such as Slack DM is best-effort. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]

**Other vendors**
- Factory (factory.com): Delegations let a user mention `@Factory` in Slack (also Linear, Jira, Teams) to hand work to Droid. Channel delegations run as a shared service account set once in the Apps agent profile. Slack DMs are the exception and run as the sender, with personal credentials. A Slack workspace connects to only one Factory organization at a time. [[wiki/docs/llms-docs-factory-com/delegations-index]]
- Factory automations can trigger on top-level Slack messages only, with `*` channel patterns, sender and keyword filters. They always reply as Factory. [[wiki/docs/llms-docs-factory-com/software-factory-automations]]
- Factory's Software Factory dashboard filters coverage by Slack, and counts Slack and Linear delegation under the Code-gen stage. [[wiki/docs/llms-docs-factory-com/software-factory-overview]]
- 8090: the Agent can be used from Slack, and Slack is listed among connections beside codebase, MCP servers and coding agents. [[wiki/docs/llms-docs-8090-ai/general-introduction]]
- Port: in the reference autonomous-ticket-resolution workflow Slack is the human approval step between AI readiness scoring and delegation to Cursor. [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]
- Mastra Factory: Slack is an alternate entry point. Later messages in a subscribed thread continue the session. A message starting with `aside` counts as discussion and gets no normal agent reply. [[wiki/docs/llms-factory-mastra-ai/using-sessions]], [[wiki/docs/llms-factory-mastra-ai/what-is-factory]]

**Warp: wider context**
- Slack and Linear integrations use the same follow-up capability as the public run API. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]
- Self-hosted workers are still orchestrated by the Automation Platform for Slack-triggered runs. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-docker]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]]
- Bitbucket, Azure DevOps Server and self-managed GitLab have no forge-specific events, so work must start from Slack, Linear, Jira, a webhook or a direct run. [[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]
- Slack is also an automation trigger in the factory-as-code definition and a dashboard-managed trigger type. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]
- The foreman talks to people through the tool where the request started, such as Slack. [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]
- Slack is the chat counterpart to Teams. [[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]]

**Podcast view (Warp CEO)**
- DIY software factories commonly stitch together Docker plus a web portal or a Slack bot. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- Advice to onboard everyone by letting them prompt the cloud loop directly, via Slack, Jira or MCP, because that makes work tracked and measurable; automation then takes a growing share. [[wiki/sources/youtube-XUEfIxkdT2Q]]

**Troubleshooting**
- Common cause of a missed event: the app is not in the channel, or admin approval is pending. [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]

**Feedback sink (non-factory use)**
- The `complain` and `suggestion-box` skills have agents autonomously submit anonymous Slack feedback. The webhook URL is held as an Oz managed secret. The repo notes these skills run unprompted by design. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]

## Tensions

- **Identity on Slack.** Warp requires a linked Slack account on an active team member to start work by mention or DM, and automation runs use the chosen factory agent. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]] Factory runs channel delegations as a shared service account but DMs as the sender. [[wiki/docs/llms-docs-factory-com/delegations-index]] Different models of whose authority a Slack request carries.
- **Trigger scope.** Warp lists mentions, DMs, channel messages, reactions and member joins as triggers. [[wiki/docs/llms-docs-warp-dev/factories-automations]] Factory's Slack automations fire only on top-level messages. [[wiki/docs/llms-docs-factory-com/software-factory-automations]]

- **Slack as entry versus Slack as bot.** The podcast lists a Slack bot as a typical DIY factory front end. [[wiki/sources/youtube-XUEfIxkdT2Q]] The vendor docs treat Slack as a managed, identity-checked intake. This is a framing difference, not a conflict of fact.

## Relationships

- **Warp Factories**: Slack is one intake and status channel. [[wiki/entities/warp-factories]]
- **Software factory**: Slack is the shared chat surface across vendors' factory products. [[wiki/concepts/software-factory]]
- **Microsoft Teams**: the sibling chat intake, described as Slack's counterpart. [[wiki/entities/microsoft-teams]]
- **Foreman agent**: the Slack-facing coordinator. [[wiki/concepts/foreman-agent]]
- **Human in the loop**: identity mapping and the PR review gate are the human control points. [[wiki/concepts/human-in-the-loop]]
- **MCP**: built-in Slack tools replace a user-run Slack MCP server. [[wiki/concepts/mcp]]
- **GitHub, Linear**: adjacent integrations. [[wiki/entities/github]], [[wiki/entities/linear]]
- **Claude Code**: Port's workflow delegates onward to Claude Code or Cursor after a Slack approval. [[wiki/entities/claude-code]]

> Synthesis: The sources show two roles for Slack: human-facing intake and status for a factory, and a one-way sink for agents. Only the first is a controlled path with identity checks and a review gate. The second sends unprompted agent output out of the repo, and the sources do not discuss its risks.
