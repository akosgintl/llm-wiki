---
type: source
title: Sessions
description: Factory docs page on how to find work needing attention, inspect and steer an agent session, and keep discussion in card comments and Slack threads.
origin: llms-txt
original_path: https://factory.mastra.ai/using/sessions.md
source_url: https://factory.mastra.ai/using/sessions.md
authors: []
published_date: null
raw_file: raw/docs/llms-factory-mastra-ai/using-sessions.md
created: 2026-10-25T18:30:00Z
timestamp: 2026-10-25T18:30:00Z
entities:
  - "[[wiki/entities/slack]]"
concepts:
  - "[[wiki/concepts/human-in-the-loop]]"
---

# Sessions

> [[raw/docs/llms-factory-mastra-ai/using-sessions|Raw]] · llms-txt · Docs / Core concepts

## Summary

In Factory, a session holds the agent conversation and workspace for one task. A human opens it from a work-item card to inspect decisions, commands, files and changes before deciding the next step. [[raw/docs/llms-factory-mastra-ai/using-sessions#Sessions|cite]]

The page is operator-facing. The Overview surfaces work waiting on a decision or reporting a problem, searchable by issue title, issue number or session name. Inside a session the human reads the latest agent result and tool output, uses the files and changes views, and can message the agent with a specific next step. A table maps what the session shows (question, plan, failed command, completed implementation, completed review) to what the human should check. [[raw/docs/llms-factory-mastra-ai/using-sessions#Find the work that needs you|cite]]

Collaboration is split by surface: card comments for teammate discussion and mentions, the session for plan and tool approval requests, and Slack threads that continue a session. [[raw/docs/llms-factory-mastra-ai/using-sessions#Keep discussion with the work|cite]]

## Key claims

- A session may need a waiting run started or a task accepted before work continues; a ready plan must be reviewed before implementation is approved. [[raw/docs/llms-factory-mastra-ai/using-sessions#Find the work that needs you|cite]]
- Per-state review guidance: supply missing context for a question; confirm scope, files, checks and deliverable for a plan; read error, working directory and setup command for a failed command. [[raw/docs/llms-factory-mastra-ai/using-sessions#Inspect and continue a session|cite]]
- A completed implementation is reviewed via diff and checks, then the PR source link; a completed review is read against the current PR revision. [[raw/docs/llms-factory-mastra-ai/using-sessions#Inspect and continue a session|cite]]
- Messages sent into an existing session can steer a run already in progress. [[raw/docs/llms-factory-mastra-ai/using-sessions#Inspect and continue a session|cite]]
- When work starts in Slack, later messages in the subscribed thread continue the session. [[raw/docs/llms-factory-mastra-ai/using-sessions#Keep discussion with the work|cite]]
- A Slack message beginning with `aside` counts as discussion and does not trigger the normal agent reply; on a thread linked to a work item it can be recorded in the comment feed. [[raw/docs/llms-factory-mastra-ai/using-sessions#Keep discussion with the work|cite]]

## Notable quotes

> "A session contains the agent conversation and workspace for a task."
> — [[raw/docs/llms-factory-mastra-ai/using-sessions#Sessions|intro]]

## Connections

- **Entities**: [[wiki/entities/slack]]
- **Concepts**: [[wiki/concepts/human-in-the-loop]]

> Synthesis: Concrete UI-level picture of human-in-the-loop in Factory: approvals, questions and steering all happen in the session, with Slack as an alternate entry point.
