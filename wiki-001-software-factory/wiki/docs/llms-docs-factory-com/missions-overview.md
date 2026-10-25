---
type: source
title: Factory Missions
description: "Factory Missions turn a large, multi-feature project into a collaboratively planned set of milestones that an orchestrator (Mission Control) executes and validates with Droid workers."
origin: llms-txt
original_path: https://docs.factory.com/missions/overview.md
source_url: https://docs.factory.com/missions/overview.md
authors: []
published_date: null
raw_file: raw/docs/llms-docs-factory-com/missions-overview.md
created: 2026-10-25T18:30:00Z
timestamp: 2026-10-25T18:30:00Z
entities: []
concepts:
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/agent-harness]]"
---

# Factory Missions

> [[raw/docs/llms-docs-factory-com/missions-overview|Raw]] · llms-txt

## Summary

Missions are Factory's structured workflow for large, multi-feature work done with its agent, Droid. Instead of one long session, the user first collaborates with Droid on a plan: features grouped into milestones, plus the skills needed for each part. Execution is then handed to an orchestration layer. [[raw/docs/llms-docs-factory-com/missions-overview#what-missions-do|cite]]

The flow starts with `/missions` (or `/mission`) in a Droid session. Droid asks clarifying questions, builds the feature and milestone plan, reuses existing skills or writes new specialized ones, and on approval enters Mission Control, the orchestration view. There the user monitors progress and can intervene. "Mission Mode" is the session state after approval. [[raw/docs/llms-docs-factory-com/missions-overview#how-it-works|cite]]

The page is candid that the design is unsettled. It lists open questions: whether parallel agents beat sequential runs, how to keep long plans correct, and how to trade cost against quality. [[raw/docs/llms-docs-factory-com/missions-overview#open-questions|cite]]

```mermaid
flowchart LR
  A["/missions"] --> B[Collaborate on plan]
  B --> C[Features + milestones]
  C --> D[Reuse / create skills]
  D --> E[Approve plan]
  E --> F[Mission Control: workers + QA validation]
```

## Key claims

- Sweet spot is about 1-500 features; fewer belongs in a normal session, more should be split into several Missions. It is a heuristic, not a hard limit. [[raw/docs/llms-docs-factory-com/missions-overview#when-to-use-missions|cite]]
- Start a Mission up front; do not convert a long-running normal session, since that loses the planning and validation context. [[raw/docs/llms-docs-factory-com/missions-overview#when-to-use-missions|cite]]
- Existing MCP integrations, skills, hooks and custom droids all work inside Missions. [[raw/docs/llms-docs-factory-com/missions-overview#when-to-use-missions|cite]]
- Missions run user-facing QA against the app to validate each feature; this needs a scriptable way to exercise the app, and the repo should be at Agent Readiness Level 4 (Optimized) or above. [[raw/docs/llms-docs-factory-com/missions-overview#for-optimal-outcomes|cite]]
- The orchestrator is itself an agent: pause it and talk to it to recover from freezes, stuck workers, stuck milestones or scope changes. QA-style validation can be disabled in Mission Control settings. [[raw/docs/llms-docs-factory-com/missions-overview#troubleshooting|cite]]
- Tested use cases: full-stack development, research, brownfield migrations, ambitious prototypes. [[raw/docs/llms-docs-factory-com/missions-overview#what-missions-are-good-for|cite]]

## Notable quotes

> "Missions are not fire-and-forget. The orchestrator is an agent, and you can talk to it."
> — [[raw/docs/llms-docs-factory-com/missions-overview#troubleshooting|Troubleshooting]]

## Connections

- **Entities**: none
- **Concepts**: [[wiki/concepts/agent-skill]], [[wiki/concepts/mcp]], [[wiki/concepts/human-in-the-loop]], [[wiki/concepts/agent-harness]]

> Synthesis: A vendor-docs view of plan-then-orchestrate agent work with a human steering the orchestrator; it is the Factory.ai analogue of the wiki's other software-factory products, and its repo-readiness gate (scriptable app for QA) is the notable prerequisite.
