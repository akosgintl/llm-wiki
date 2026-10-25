---
type: source
title: Intake
description: "Mastra Factory intake turns synced GitHub, GitLab, Linear, Jira and incident.io issues into Work cards and pull requests into Review cards, with nothing starting automatically unless a trust policy allows it."
origin: llms-txt
original_path: https://factory.mastra.ai/using/intake.md
source_url: https://factory.mastra.ai/using/intake.md
authors: []
published_date: null
raw_file: raw/docs/llms-factory-mastra-ai/using-intake.md
created: 2026-10-25T18:30:00Z
timestamp: 2026-10-25T18:30:00Z
entities:
  - "[[wiki/entities/github]]"
  - "[[wiki/entities/linear]]"
  - "[[wiki/entities/slack]]"
concepts:
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/software-factory]]"
---

# Intake

> [[raw/docs/llms-factory-mastra-ai/using-intake|Raw]] · llms-txt · https://factory.mastra.ai/using/intake.md

## Summary

Intake is the incoming work an agent can investigate or review in Mastra's Factory. Issues become Work items; pull requests become Review items. Each source (GitHub, GitLab, Linear, Jira, incident.io issues; GitHub PRs and GitLab merge requests) is connected first. Each teammate then picks personally which issues to follow under Settings, Work Intake. Shared repository connections and organization routing decide which Factory and board the work lands on. [[raw/docs/llms-factory-mastra-ai/using-intake#Choose your sources|cite]]

Work starts in one of three ways: a person clicks Investigate or starts a review, Factory auto-starts a run when the source is trusted and policy allows, or a source event (a new commit on a reviewed PR) triggers follow-up. Everything else waits on its card or in Needs attention. The page advises leaving Auto-start runs and Auto-approve plans off until the workflow is understood. [[raw/docs/llms-factory-mastra-ai/using-intake#How work starts|cite]]

Factory does no prioritization. Every synced issue is an independent card, and GitHub epics and sub-issues are not modeled. The user orders work by choosing what to start. [[raw/docs/llms-factory-mastra-ai/using-intake#Order and priority|cite]]

## Key claims

- Issue selection is personal per teammate; repository connections and Linear routing are shared. [[raw/docs/llms-factory-mastra-ai/using-intake#Choose your sources|cite]]
- GitHub issues go to the Work board unless a label route picks another; GitLab, Linear, Jira and incident.io items need organization routing to a Factory and board. [[raw/docs/llms-factory-mastra-ai/using-intake#Choose your sources|cite]]
- Default GitHub rules allow an automatic initial run only for issues created after the Factory by an author with write or admin access. [[raw/docs/llms-factory-mastra-ai/using-intake#How work starts|cite]]
- Sync is asynchronous; verify by creating one active issue and completing an investigation to confirm model access and execution. [[raw/docs/llms-factory-mastra-ai/using-intake#Verify incoming work|cite]]
- Sub-issues arrive as ordinary cards with no link to their parent; the epic is the user's own tracking tool. [[raw/docs/llms-factory-mastra-ai/using-intake#Order and priority|cite]]
- Missing items: check source access, Work Intake selections, destination Factory, and (Linear) routing; for PRs check GitHub access and linked repository. [[raw/docs/llms-factory-mastra-ai/using-intake#Resolve missing items|cite]]

## Notable quotes

> "Factory doesn't rank, sequence, or filter incoming work."
> — [[raw/docs/llms-factory-mastra-ai/using-intake#Order and priority|Order and priority]]

> "Start work yourself and leave **Auto-start runs** and **Auto-approve plans** off until you know the workflow."
> — [[raw/docs/llms-factory-mastra-ai/using-intake#How work starts|How work starts]]

## Connections

- **Entities**: [[wiki/entities/github]], [[wiki/entities/linear]], [[wiki/entities/slack]]
- **Concepts**: [[wiki/concepts/human-in-the-loop]], [[wiki/concepts/software-factory]]

> Synthesis: Mastra Factory's intake is a manual-first, trust-gated counterpart to Warp Factories' issue-to-PR flow, and it explicitly leaves prioritization to humans.
