---
type: source
title: Reverse engineering
description: "8090 docs describe an Agent workflow that reads a connected repository and reconstructs a feature hierarchy, requirements and blueprints, flagging conflicts between old specs and the real code."
origin: llms-txt
original_path: https://docs.8090.ai/opinions/reverse-engineering
source_url: https://docs.8090.ai/opinions/reverse-engineering
authors: []
published_date: null
raw_file: raw/docs/llms-docs-8090-ai/opinions-reverse-engineering.md
created: 2026-10-25T18:40:00Z
timestamp: 2026-10-25T18:40:00Z
entities:
  - "[[wiki/entities/github]]"
concepts:
  - "[[wiki/concepts/human-in-the-loop]]"
---

# Reverse engineering

> [[raw/docs/llms-docs-8090-ai/opinions-reverse-engineering|Raw]] · llms-txt

## Summary

The page argues that most teams adopt 8090 Software Factory with an existing, poorly documented product, so the platform should start from the code rather than a blank project. The Agent indexes a connected repository, reconstructs what the product does, groups it into a feature hierarchy, and writes requirements and blueprints. [[raw/docs/llms-docs-8090-ai/opinions-reverse-engineering#Reverse engineering|cite]]

Its central stance is "reconcile, don't just import": code is treated as observed behavior and uploaded PRDs or specs as stated intent. Disagreements are surfaced as comments on the exact document and text, not silently resolved. Every finding carries a code reference and a confidence level; unknowns are recorded as gaps rather than guessed. [[raw/docs/llms-docs-8090-ai/opinions-reverse-engineering#How the workflow runs|cite]]

The run is chosen once as cooperative (pauses at survey scope and the proposed feature tree) or autonomous (never pauses; questions become comments). It resumes from project state, so large repositories can be handled over several sessions. After authoring, a Detect Code Drift automation re-checks blueprints against linked code on each push.

```mermaid
flowchart LR
  A[Connect repo] --> B[Index 5-10 min]
  B --> C[Survey scope]
  C --> D[Analyze by area]
  D --> E[Propose feature tree]
  E --> F[Author requirements + blueprints]
  F --> G[Drift detection on push]
```

## Key claims

- Run modes: cooperative checks in at survey scope and the feature hierarchy; autonomous runs end to end and records questions as comments. [[raw/docs/llms-docs-8090-ai/opinions-reverse-engineering#How the workflow runs|cite]]
- No document is created until the feature hierarchy is settled; the hierarchy is organized by user-facing capability, not folder layout. [[raw/docs/llms-docs-8090-ai/opinions-reverse-engineering#Tips and pitfalls|cite]]
- A GitHub repository or GitLab project is connected per selected branch; initial indexing usually takes 5 to 10 minutes, pushes reindex automatically, and the run refuses to start before indexing completes. [[raw/docs/llms-docs-8090-ai/opinions-reverse-engineering#Let indexing complete|cite]]
- Creating a feature requirements document also creates its paired blueprint, linked to the code files it describes. [[raw/docs/llms-docs-8090-ai/opinions-reverse-engineering#Review the generated requirements and blueprints|cite]]
- Edits to existing documents arrive as tracked suggestions, so a resumed run never overwrites human work. [[raw/docs/llms-docs-8090-ai/opinions-reverse-engineering#Review the generated requirements and blueprints|cite]]
- Drift means only behavior the code contradicts; not-yet-built behavior does not count. [[raw/docs/llms-docs-8090-ai/opinions-reverse-engineering#Validate with drift detection|cite]]

## Notable quotes

> "The Agent treats code as observed behavior and your documents as stated intent, then tells you exactly where the two disagree."
> — [[raw/docs/llms-docs-8090-ai/opinions-reverse-engineering#Reverse engineering|Reverse engineering]]

> "A reverse-engineered project is a strong starting point, not a finished specification."
> — [[raw/docs/llms-docs-8090-ai/opinions-reverse-engineering#Tips and pitfalls|Review before you build on it]]

## Connections

- **Entities**: [[wiki/entities/github]]
- **Concepts**: [[wiki/concepts/human-in-the-loop]]

> Synthesis: Product-specific to 8090 (not Warp or Mastra); its cooperative/autonomous split and comment-based escalation are a concrete human-in-the-loop design, and the page keeps the knowledge graph, not tickets, as source of truth.
