---
type: source
title: Mastra Factory deployment
description: "Mastra Factory docs describe three deployment setups, one-command deploy to Mastra platform, and a fully self-hosted path on a persistent Node.js process with PostgreSQL."
origin: llms-txt
original_path: https://factory.mastra.ai/deployment.md
source_url: https://factory.mastra.ai/deployment.md
authors: []
published_date: null
raw_file: raw/docs/llms-factory-mastra-ai/deployment.md
created: 2026-10-25T18:30:00Z
timestamp: 2026-10-25T18:30:00Z
entities:
  - "[[wiki/entities/mastra-factory]]"
concepts:
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/concepts/secrets-management]]"
  - "[[wiki/concepts/software-factory]]"
---

# Mastra Factory deployment

> [[raw/docs/llms-factory-mastra-ai/deployment|Raw]] · llms-txt

## Summary

This page explains how to run the Mastra Factory Server beyond localhost. The docs offer two routes: deploy to Mastra platform, or self-host in your own environment. Both start from the Factory Server project made in Get started. [[raw/docs/llms-factory-mastra-ai/deployment#Deployment|cite]]

Three setups are listed. Full platform (default) puts the server, auth, PostgreSQL and sandboxes on Mastra platform. "Local server with platform resources" runs the server on your computer but keeps platform auth, database and sandboxes. Fully self-hosted uses your own auth provider, database and sandbox provider. [[raw/docs/llms-factory-mastra-ai/deployment#Choose a setup|cite]]

The platform path is four steps: run `check` and `build`, prepare the environment in Platform (database, encryption key, provider access, integration credentials, public origin), run the project's `deploy` script, then verify by opening the Factory URL, creating an issue in a subscribed source and checking the session's sandbox provider. [[raw/docs/llms-factory-mastra-ai/deployment#Deploy|cite]] The self-host path needs a persistent Node.js process, and the build bundles UI and API so both can share one domain. [[raw/docs/llms-factory-mastra-ai/deployment#Self-host|cite]] Vendor documentation: everything here is the vendor's own account.

## Key claims

- The `deploy` script targets the `production` environment by default. `--env <name>` picks another and can create it. `--region eu` sets an EU region for a new environment only; it does not relocate an existing one. [[raw/docs/llms-factory-mastra-ai/deployment#Run the deployment|cite]]
- A deployed server requires persistent database storage, and the database's credential encryption key must be preserved. [[raw/docs/llms-factory-mastra-ai/deployment#Prepare the environment|cite]]
- Fully self-hosted projects are created with `--no-platform`. The installer copies `.env.example` to `.env` with no platform credentials, so auth, database and sandbox providers must be configured first. [[raw/docs/llms-factory-mastra-ai/deployment#Self-host|cite]]
- Self-host requirements: Node.js per `engines.node`, PostgreSQL with pgvector via `DATABASE_URL`, an HTTPS endpoint supporting streaming (set `MASTRACODE_PUBLIC_URL`), stable encryption key and state-signing secrets, and network access to a cloud sandbox provider. [[raw/docs/llms-factory-mastra-ai/deployment#Requirements|cite]]
- For local execution, the server needs Git, the repository's build tools and persistent disk for session directories. [[raw/docs/llms-factory-mastra-ai/deployment#Requirements|cite]]
- Start command is `npm run start`; the build output lands in `.mastra/output` and can be packaged in a container. [[raw/docs/llms-factory-mastra-ai/deployment#Deployment outline|cite]]

## Notable quotes

> "Keep the server running so Factory can process intake and agent work in the background."
> — [[raw/docs/llms-factory-mastra-ai/deployment#Requirements|Requirements]]

## Connections

- **Entities**: [[wiki/entities/mastra-factory]]
- **Concepts**: [[wiki/concepts/self-hosting]], [[wiki/concepts/secrets-management]], [[wiki/concepts/software-factory]]

> Synthesis: Mastra's counterpart to Warp's self-hosting story, but with a fully open self-host option (own auth, DB, sandboxes) instead of an enterprise-only managed mode; auth, storage and sandboxes are independent swap points.
