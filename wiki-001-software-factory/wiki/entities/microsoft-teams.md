---
type: entity
title: Microsoft Teams
description: Microsoft's chat platform, supported by both Warp Factories and Factory's Delegations as a channel where @-mentions hand work to cloud coding agents.
aliases: [Teams, MS Teams]
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-automations]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]"
  - "[[wiki/docs/llms-docs-factory-com/delegations-index]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-overview]]"
related:
  - "[[wiki/entities/slack]]"
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/human-in-the-loop]]"
created: 2026-10-25T18:31:21Z
timestamp: 2026-10-25T18:31:21Z
source_count: 8
---

# Microsoft Teams

> Chat platform that two vendor doc sets list as a work intake path: mention the agent in a channel, get the result back in the thread.

## Definition

In this wiki Teams appears only as an integration target, never as a subject of its own. Both origins are vendor documentation, so every claim is the vendor's own account. Warp Factories treats it as one of eleven entry points beside Slack, GitHub and Linear. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]] Factory's Delegations lists it with Slack, Linear and Jira as a place to send work to its agent, Droid. [[wiki/docs/llms-docs-factory-com/delegations-index]]

## Key claims

- Mentioning @Warp in a standard or shared channel starts a work item; replies post in the same thread. Private channels and direct messages are not supported. [[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]]
- Setup spans three roles: a Warp workspace admin, a Teams admin or team owner who approves the app package, and a factory editor who picks teams and channels. Warp then seeds a `teams-app-mentions` automation. [[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]
- Triggers are `app_mention` (default) and `message_posted`; enabling both on one channel can start two runs from one mention. [[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]], [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]
- Teams automation filters cover team, channels, authors and keywords. [[wiki/docs/llms-docs-warp-dev/factories-automations]]
- As code, it is `type: microsoft-teams` in `factory.yaml` plus an automation file with Graph team and channel ids. [[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]
- Agents get Warp-managed Teams tools (read thread, reply, post, resolve member) but cannot send DMs, react or upload files, and an agent run can read only its originating thread. [[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]]
- Users must link a Microsoft account to a Warp account; sign-out unlinks it from every factory in that Microsoft org. [[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]]
- In Factory, Teams delegation runs under the organization's Apps agent profile with a shared service account, and needs no Software Factory automation. [[wiki/docs/llms-docs-factory-com/delegations-index]], [[wiki/docs/llms-docs-factory-com/software-factory-overview]]
- Common failure: Teams app or channel not configured. [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]

## Relationships

- **Slack**: the sibling chat intake path; Warp's Teams page is its counterpart. [[wiki/entities/slack]]
- **Warp Factories**: routes Teams events through automations to the foreman agent. [[wiki/entities/warp-factories]]
- **Factory as code**: Teams config lives in versioned definition files. [[wiki/concepts/factory-as-code]]

## Tensions

The two vendors differ in mechanism: Warp routes Teams mentions through filterable automations; Factory delegates via a service-account profile with no automation. [[wiki/docs/llms-docs-warp-dev/factories-automations]], [[wiki/docs/llms-docs-factory-com/software-factory-overview]]

> Synthesis: Two origins (Warp docs, Factory docs), each one voice; Teams is a commodity chat intake channel in the software-factory pattern, with Slack as the main analogue.
