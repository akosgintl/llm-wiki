---
type: source
title: 8090 Software Factory introduction
description: "8090's docs pitch a multiplayer, AI-native platform that keeps requirements, blueprints and work orders in one knowledge graph so teams and agents share a single source of truth."
origin: llms-txt
original_path: https://docs.8090.ai/general/introduction
source_url: https://docs.8090.ai/general/introduction
authors: []
published_date: null
raw_file: raw/docs/llms-docs-8090-ai/general-introduction.md
created: 2026-10-25T18:17:08Z
timestamp: 2026-10-25T18:17:08Z
entities:
  - "[[wiki/entities/github]]"
  - "[[wiki/entities/slack]]"
concepts:
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/knowledge-graph]]"
  - "[[wiki/concepts/context-engineering]]"
---

# 8090 Software Factory introduction

> [[raw/docs/llms-docs-8090-ai/general-introduction|Raw]] · llms-txt

## Summary

This is the landing page of the 8090 docs. It describes 8090 Software Factory as an AI-native platform for orchestrating the whole software development lifecycle, with PMs, designers, engineers and QA working in one place. [[raw/docs/llms-docs-8090-ai/general-introduction#welcome-to-8090-software-factory|cite]]

The argument starts from a diagnosis. Writing code is no longer the bottleneck; deciding what to build and why is. Delays come from misalignment, missing context, unclear decisions and rework. Fragmented docs and tribal knowledge make it worse, and "single-player" AI coding tools give fast output on weak foundations. [[raw/docs/llms-docs-8090-ai/general-introduction#the-problem|cite]]

The proposed fix is a shared workspace for context engineering. Requirements, architectural plans and implementation details live in a Knowledge Graph and evolve together. Specialized agents surface gaps and tradeoffs, and a Drift Bot comments when artifacts or code no longer match. [[raw/docs/llms-docs-8090-ai/general-introduction#the-solution|cite]]

The page then indexes the product: core modules (Requirements, Blueprints, Work Orders, Feedback), connections (codebase, MCP servers, Slack, coding agents), and agent features (Knowledge Base, Skills, Automations). [[raw/docs/llms-docs-8090-ai/general-introduction#core-modules|cite]]

## Key claims

- Enterprise delivery is slowed by fragmented documentation, ad-hoc communication and tribal knowledge; departing experts take critical knowledge with them. [[raw/docs/llms-docs-8090-ai/general-introduction#the-problem|cite]]
- Most AI tools run in "single-player mode", optimizing for prototypes without architectural discipline. [[raw/docs/llms-docs-8090-ai/general-introduction#the-problem|cite]]
- Requirements, architecture plans and implementation details are linked in a Knowledge Graph so they change together. [[raw/docs/llms-docs-8090-ai/general-introduction#the-solution|cite]]
- Drift Bot and recommended automations comment on what no longer matches current context. [[raw/docs/llms-docs-8090-ai/general-introduction#the-solution|cite]]
- Core flow: Requirements, then Blueprints (technical specs), then Work Orders (tasks grounded in the codebase), plus Feedback turned into themes. [[raw/docs/llms-docs-8090-ai/general-introduction#core-modules|cite]]
- Work orders can be pulled into Cursor, Claude Code, Codex and other coding agents; a GitHub or GitLab repo can be connected for code search, and the Agent can be used from Slack. [[raw/docs/llms-docs-8090-ai/general-introduction#connections|cite]]
- Agents can load reusable Skills and run on schedules or project changes via Automations. [[raw/docs/llms-docs-8090-ai/general-introduction#agents|cite]]

## Notable quotes

> "Development itself has never been the bottleneck."
> — [[raw/docs/llms-docs-8090-ai/general-introduction#the-problem|The Problem]]

> "Decisions become explicit, reviewable, and consistently aligned with business intent."
> — [[raw/docs/llms-docs-8090-ai/general-introduction#the-solution|The Solution]]

## Connections

- **Entities**: [[wiki/entities/github]], [[wiki/entities/slack]]
- **Concepts**: [[wiki/concepts/software-factory]], [[wiki/concepts/agent-skill]], [[wiki/concepts/knowledge-graph]], [[wiki/concepts/context-engineering]]

> Synthesis: Marketing-level entry page; it frames a software factory as a spec-and-context layer (requirements to work orders for external coding agents), unlike Warp Factories, which runs cloud agents end to end.
