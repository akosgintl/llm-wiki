---
type: concept
title: Webhook
description: An HTTP endpoint that an external system POSTs events to, used here as the generic intake path that turns tool events into agent runs.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks-vercel]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-automations]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-demo-sentry-monitoring-with-sdk]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-secrets]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-developer-tools]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-automations]]"
  - "[[wiki/docs/llms-docs-port-io/guides-all-trigger-ai-coding-assistants-from-port]]"
related:
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/secrets-management]]"
created: 2026-10-25T18:32:01Z
timestamp: 2026-10-25T18:32:01Z
source_count: 14
---

# Webhook

> An authenticated HTTP URL that outside systems POST JSON to, so any tool event can start agent work.

## Definition

In the docs ingested so far, a webhook is the catch-all way to feed work into an agent system from tools it has no native integration for. Warp describes a custom webhook as an HTTPS URL that CI, Vercel, Stripe, Sentry, PagerDuty or homegrown tools can POST to; an automation with a Webhook trigger starts a run when a delivery matches its filter. [[wiki/docs/llms-docs-warp-dev/factories-webhooks]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]

Factory (Droid automations) uses the same shape: an inbound POST to a per-automation URL is one of four trigger types. [[wiki/docs/llms-docs-factory-com/software-factory-automations]] Port uses a *webhook node* differently, as an outbound call from a workflow to the GitHub API. [[wiki/docs/llms-docs-port-io/guides-all-trigger-ai-coding-assistants-from-port]]

Warp, Factory and Port are three vendors, but the Warp pages are one origin and one voice.

## Key claims

- Warp offers three auth modes: bearer token, URL token and provider signature (Vercel, Stripe, GitHub, Sentry, PagerDuty, Standard Webhooks). [[wiki/docs/llms-docs-warp-dev/factories-webhooks]], [[wiki/docs/llms-docs-warp-dev/factories-automations]]
- Factory authenticates with an `X-Webhook-Secret` header or `secret` query parameter; the secret is shown once and only a hash is stored. [[wiki/docs/llms-docs-factory-com/software-factory-automations]]
- Payload filters match the JSON body with `in`, `not_in`, `exists`; without a filter every delivery starts a run. A "Test filter" action checks a stored delivery. [[wiki/docs/llms-docs-warp-dev/factories-webhooks]], [[wiki/docs/llms-docs-warp-dev/factories-automations]]
- Intake limits differ: Warp allows 256 KB bodies and 60 deliveries per minute, returns `202` even when nothing matches, and dedupes by delivery identity. Factory allows 200 KiB, 60 per minute per URL, a 10-minute body dedupe and 10 runs per hour. [[wiki/docs/llms-docs-warp-dev/factories-webhooks]], [[wiki/docs/llms-docs-factory-com/software-factory-automations]]
- Webhooks are declarative resources in a factory definition (`webhooks/<name>.yaml`). Secret rotation reaches webhooks only when the definition is reapplied. [[wiki/docs/llms-docs-warp-dev/factories-webhooks]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/docs/llms-docs-warp-dev/factories-secrets]]
- Rotating a secret invalidates the old one at once, in both products. [[wiki/docs/llms-docs-warp-dev/factories-webhooks]], [[wiki/docs/llms-docs-factory-com/software-factory-automations]]
- Vercel shows its signing secret only after the URL exists, so the webhook is created disabled, returns a URL, then takes the secret. [[wiki/docs/llms-docs-warp-dev/factories-webhooks-vercel]]
- Webhooks also carry platform events: Warp installs a GitLab group webhook to deliver merge request and comment events. Without it, runs cannot be triggered from GitLab. [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]
- For forges without native events, a custom webhook is a way to start work. [[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]
- A Sentry demo validates an alert webhook, extracts the stack trace and starts a standalone cloud agent run that yields a draft PR. For full factory routing the docs prefer factory endpoints or a custom webhook. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-demo-sentry-monitoring-with-sdk]], [[wiki/docs/llms-docs-warp-dev/factories-developer-tools]]
- Diagnosis is by Recent deliveries; rejections and deduplication are common causes of "no run". [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]], [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]

## Relationships

- **Software factory**: webhooks are one of several work-intake routes. [[wiki/concepts/software-factory]]
- **Factory as code**: webhook definitions live in version control. [[wiki/concepts/factory-as-code]]
- **Secrets management**: signing and bearer secrets are managed secrets. [[wiki/concepts/secrets-management]]

## Tensions

Limits and secret handling differ between Warp (256 KB, secret by reference to a managed secret) and Factory (200 KiB, hashed once-shown secret). Port's "webhook node" is outbound, the reverse direction. [[wiki/docs/llms-docs-warp-dev/factories-webhooks]], [[wiki/docs/llms-docs-factory-com/software-factory-automations]], [[wiki/docs/llms-docs-port-io/guides-all-trigger-ai-coding-assistants-from-port]]

> Synthesis: Webhook is the generic, vendor-neutral on-ramp into agent systems; most detail comes from Warp's docs (one voice), with Factory partly corroborating.
