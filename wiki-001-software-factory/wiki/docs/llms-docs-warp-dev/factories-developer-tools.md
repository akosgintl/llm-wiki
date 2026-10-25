---
type: source
title: Warp Platform API & SDKs
description: Docs landing page listing the integration surfaces of Warp Factories - factory endpoints, agent and run endpoints, SDKs, Factory MCP and webhooks.
origin: llms-txt
original_path: https://docs.warp.dev/factories/developer-tools/
source_url: https://docs.warp.dev/factories/developer-tools/
authors: []
published_date: null
raw_file: raw/docs/llms-docs-warp-dev/factories-developer-tools.md
created: 2026-10-25T14:59:31Z
timestamp: 2026-10-25T14:59:31Z
entities:
  - "[[wiki/entities/warp-factories]]"
concepts:
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/webhook]]"
---

# Warp Platform API & SDKs

> [[raw/docs/llms-docs-warp-dev/factories-developer-tools|Raw]] · llms-txt

## Summary

This is a short hub page from the Warp Factories documentation. It does not teach one integration in depth. It routes readers to the ways of connecting outside tools and services to a factory. The docs state that the Warp Platform API serves both factories and standalone cloud agent runs, with one API key, one API reference, shared SDKs and one error model. [[raw/docs/llms-docs-warp-dev/factories-developer-tools#Warp Platform API & SDKs|cite]]

The page splits the API into two families. Factory endpoints find a factory and send work to it by UID. Agent and run endpoints start, monitor, continue and cancel standalone cloud agent runs from scripts, CI and backend services. [[raw/docs/llms-docs-warp-dev/factories-developer-tools#Choose an API surface|cite]] Around the HTTP API sit typed Python and TypeScript SDKs, an errors reference, a Factory MCP and webhooks.

## Key claims

- The docs state the same API key, reference, SDKs and error model cover both factory endpoints and standalone cloud agent runs. [[raw/docs/llms-docs-warp-dev/factories-developer-tools#Warp Platform API & SDKs|cite]]
- Per the docs, work is sent to a factory by its UID, via "dispatching a run to a factory". [[raw/docs/llms-docs-warp-dev/factories-developer-tools#Get started|cite]]
- The docs list two published SDKs: Python `warp-platform-sdk` and TypeScript `@warp-dot-dev/warp-platform-sdk`. [[raw/docs/llms-docs-warp-dev/factories-developer-tools#Choose an API surface|cite]]
- The docs describe Factory MCP as a way to exchange work between a factory and a connected coding agent or MCP client. [[raw/docs/llms-docs-warp-dev/factories-developer-tools#Choose an API surface|cite]]
- The docs say webhooks receive events from any system that can send JSON and route matching deliveries into factory automations. [[raw/docs/llms-docs-warp-dev/factories-developer-tools#Choose an API surface|cite]]
- A Sentry monitoring example is said to show standalone dispatch from a webhook handler. [[raw/docs/llms-docs-warp-dev/factories-developer-tools#Get started|cite]]

## Notable quotes

> "The factory endpoints send work to a factory; agent and run endpoints start and manage standalone runs."
> — [[raw/docs/llms-docs-warp-dev/factories-developer-tools#Warp Platform API & SDKs|intro]]

## Connections

- **Entities**: [[wiki/entities/warp-factories]]
- **Concepts**: [[wiki/concepts/mcp]], [[wiki/concepts/webhook]]
- **Related pages named**: connect-your-factory, factory automations, factory dashboard (all link targets only, not read here)

> Synthesis: Vendor navigation hub with no mechanism detail; it shows Warp exposes factories both inbound (API, webhooks) and to agents (MCP), and its substance lives in the linked pages.
