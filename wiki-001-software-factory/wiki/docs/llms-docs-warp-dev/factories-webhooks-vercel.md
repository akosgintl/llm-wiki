---
type: source
title: Setting up a Vercel webhook
description: "Warp's docs describe a two-step bootstrap for Vercel-signed webhooks: create the webhook disabled to get its URL, register it in Vercel, then save the secret Vercel issues."
origin: llms-txt
original_path: https://docs.warp.dev/factories/webhooks/vercel/
source_url: https://docs.warp.dev/factories/webhooks/vercel/
authors: []
published_date: null
raw_file: raw/docs/llms-docs-warp-dev/factories-webhooks-vercel.md
created: 2026-10-25T15:11:20Z
timestamp: 2026-10-25T15:11:20Z
entities:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/vercel]]"
  - "[[wiki/entities/github]]"
concepts:
  - "[[wiki/concepts/webhook]]"
  - "[[wiki/concepts/secrets-management]]"
  - "[[wiki/concepts/factory-as-code]]"
---

# Setting up a Vercel webhook

> [[raw/docs/llms-docs-warp-dev/factories-webhooks-vercel|Raw]] · llms-txt

## Summary

The docs state that Vercel shows a webhook's signing secret only after its URL is saved, while Warp has a URL only once the webhook exists. To break this chicken-and-egg loop, the factory creates the webhook without a secret: it starts disabled, hands back an ingress URL, and takes the secret in a second step. [[raw/docs/llms-docs-warp-dev/factories-webhooks-vercel#Setting up a Vercel webhook|cite]] The docs say Stripe and PagerDuty issue secrets the same way, so the same steps apply with those provider schemes.

Two paths are given. In the factory dashboard: add a webhook under Automations, pick "Provider signature" with the Vercel scheme, click "Create and get URL", register the URL in Vercel team Settings > Webhooks, then paste Vercel's one-time secret and click "Save and enable". [[raw/docs/llms-docs-warp-dev/factories-webhooks-vercel#Creating the webhook in the factory dashboard|cite]] For a factory whose definition lives in GitHub there is no dashboard editing, so the order is: create a placeholder team secret, merge a disabled `webhooks/vercel.yaml`, register the URL in Vercel, replace the placeholder with `oz secret update --team --value`, then merge `enabled: true`. [[raw/docs/llms-docs-warp-dev/factories-webhooks-vercel#Creating the webhook in a definition that lives in GitHub|cite]]

## Key claims

- Vercel team webhooks require a Vercel Pro or Enterprise plan, plus permission to manage the factory's configuration. [[raw/docs/llms-docs-warp-dev/factories-webhooks-vercel#Prerequisites|cite]]
- Once enabled, the webhook verifies the `x-vercel-signature` header on every delivery; success shows as "Accepted" under Recent deliveries. [[raw/docs/llms-docs-warp-dev/factories-webhooks-vercel#Creating the webhook in the factory dashboard|cite]]
- "Finish later" leaves the webhook disabled with a placeholder in its managed secret; the secret is replaced via the Oz CLI and the webhook re-enabled, which re-applies its definition and reads the new value. [[raw/docs/llms-docs-warp-dev/factories-webhooks-vercel#Finishing later|cite]]
- On a GitHub-backed factory a change applies only when it lands on the production branch, and a webhook file must name a secret that already exists. [[raw/docs/llms-docs-warp-dev/factories-webhooks-vercel#Creating the webhook in a definition that lives in GitHub|cite]]
- The YAML needs `authMode: signature`, `signatureScheme: vercel`, `secretName`, and `enabled`. [[raw/docs/llms-docs-warp-dev/factories-webhooks-vercel#Creating the webhook in a definition that lives in GitHub|cite]]
- Creating it with `enabled: true` from the start rejects every delivery with `401` until a later push applies the updated secret; the same 401 appears if the placeholder is still in place. [[raw/docs/llms-docs-warp-dev/factories-webhooks-vercel#Troubleshooting|cite]]

## Notable quotes

> "Vercel shows a webhook's signing secret only after you save its URL, and Warp has a URL only once the webhook exists."
> — [[raw/docs/llms-docs-warp-dev/factories-webhooks-vercel#Setting up a Vercel webhook|intro]]

## Connections

- **Entities**: [[wiki/entities/warp-factories]], [[wiki/entities/vercel]], [[wiki/entities/github]]
- **Concepts**: [[wiki/concepts/webhook]], [[wiki/concepts/secrets-management]], [[wiki/concepts/factory-as-code]]

> Synthesis: Vendor how-to; its value is the secret-bootstrap ordering, which shows factory-as-code state (a YAML definition) and secrets (out-of-band) applying on different schedules.
