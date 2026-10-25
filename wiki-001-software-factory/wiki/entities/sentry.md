---
type: entity
title: Sentry
description: Sentry is an error-monitoring and alerting service that the surveyed software-factory docs treat as an external event source whose alerts can start agent runs.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-demo-sentry-monitoring-with-sdk]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-automations]]"
related:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/github]]"
  - "[[wiki/concepts/webhook]]"
  - "[[wiki/concepts/human-in-the-loop]]"
created: 2026-10-25T18:30:21Z
timestamp: 2026-10-25T18:30:21Z
source_count: 4
---

# Sentry

> Error-monitoring service; in these docs, an upstream source of alerts that webhooks turn into agent work.

## Definition

The sources never describe Sentry itself. They treat it as an external system that emits alerts, and show how a software factory ingests them. Warp's docs name it as a typical custom-webhook sender and as one of the provider-signature senders. A dedicated demo uses it as the worked example.

All four pages come from two vendor doc sets (Warp, Factory), so this is vendor description, not independent evidence that the pattern works.

## Key claims

- A demo service filters and validates incoming Sentry webhooks, extracts the stack trace (example: a Go nil pointer dereference) and injects it into a Warp cloud agent run that inspects the repo and proposes a fix. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-demo-sentry-monitoring-with-sdk]]
- That workflow ends in a draft GitHub pull request for a maintainer, "instead of silent autonomous changes". [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-demo-sentry-monitoring-with-sdk]]
- The demo covers standalone cloud-agent intake; to route an alert through a factory's agents and workflow, the docs point to factory endpoints or a custom webhook. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-demo-sentry-monitoring-with-sdk]]
- Sentry is a named example of a system that can POST JSON to a Warp custom webhook, and of a provider-signature auth mode (alongside Vercel, Stripe, GitHub, PagerDuty and Standard Webhooks). [[wiki/docs/llms-docs-warp-dev/factories-webhooks]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]
- Warp has no first-party Sentry integration in the catalog; Sentry arrives via the generic webhook path, where an automation filters the payload to decide which deliveries start work. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]], [[wiki/docs/llms-docs-warp-dev/factories-webhooks]]
- Factory's automations page lists Sentry among its linked entities and offers Error Triage and Alert Responder starters, plus webhook triggers with payload filters and dedupe. The page text I read does not spell out a Sentry-specific setup. [[wiki/docs/llms-docs-factory-com/software-factory-automations]]

## Relationships

- **Warp Factories**: receives Sentry alerts through custom webhooks or the SDK. [[wiki/entities/warp-factories]]
- **GitHub**: destination of the draft PR the demo opens. [[wiki/entities/github]]
- **Webhook**: the transport for every Sentry path described. [[wiki/concepts/webhook]]
- **Human in the loop**: the draft PR is the review gate. [[wiki/concepts/human-in-the-loop]]

> Synthesis: Sentry is the canonical "alert in, fix proposal out" trigger for software factories; three of four pages trace to one vendor (Warp), so corroboration is thin.
