---
type: entity
title: Slack
description: "Slack is the team chat tool that Warp Factories uses as an intake and status surface, and that Warp's example skills use as a feedback sink."
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-automations]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-quickstart]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
related:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/microsoft-teams]]"
  - "[[wiki/entities/github]]"
  - "[[wiki/entities/linear]]"
  - "[[wiki/concepts/foreman-agent]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/mcp]]"
created: 2026-10-25T15:20:00Z
timestamp: 2026-10-25T15:20:00Z
source_count: 10
---

# Slack

> Team chat tool. In these sources it is a front door to a software factory: people mention or DM an agent, and progress and results return to the same thread.

## Definition

No source defines Slack itself. They describe how it plugs into Warp Factories. In the docs it is one of several work sources (Slack, Microsoft Teams, GitHub, GitLab, Azure DevOps, Linear, Jira, plus webhooks, endpoints, Factory MCP and direct runs). [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]

A second, smaller use appears in Warp's skills repo: Slack as a sink for agent feedback. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]

> Synthesis: All ten sources come from Warp: the docs set and two Warp-authored repos. They are one vendor's voice. Agreement among them is not independent corroboration. No non-Warp source here mentions Slack.

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

**Troubleshooting**
- Common cause of a missed event: the app is not in the channel, or admin approval is pending. [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]

**Feedback sink (non-factory use)**
- The `complain` and `suggestion-box` skills have agents autonomously submit anonymous Slack feedback. The webhook URL is held as an Oz managed secret. The repo notes these skills run unprompted by design. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]

## Relationships

- **Warp Factories**: Slack is one intake and status channel. [[wiki/entities/warp-factories]]
- **Microsoft Teams**: the sibling chat intake, described as Slack's counterpart. [[wiki/entities/microsoft-teams]]
- **Foreman agent**: the Slack-facing coordinator. [[wiki/concepts/foreman-agent]]
- **Human in the loop**: identity mapping and the PR review gate are the human control points. [[wiki/concepts/human-in-the-loop]]
- **MCP**: built-in Slack tools replace a user-run Slack MCP server. [[wiki/concepts/mcp]]
- **GitHub, Linear**: adjacent integrations. [[wiki/entities/github]], [[wiki/entities/linear]]

> Synthesis: The sources show two roles for Slack: human-facing intake and status for a factory, and a one-way sink for agents. Only the first is a controlled path with identity checks and a review gate. The second sends unprompted agent output out of the repo, and the sources do not discuss its risks.
