---
type: source
title: "Agent Readiness"
description: "Factory's Agent Readiness Model scores repositories on five gated levels and nine technical pillars to show whether autonomous agents can work in them reliably."
origin: llms-txt
original_path: https://docs.factory.com/agent-readiness/overview.md
source_url: https://docs.factory.com/agent-readiness/overview.md
authors: []
published_date: null
raw_file: raw/docs/llms-docs-factory-com/agent-readiness-overview.md
created: 2026-10-25T18:25:00Z
timestamp: 2026-10-25T18:25:00Z
entities: []
concepts:
  - "[[wiki/concepts/dev-environment]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/software-factory]]"
---

# Agent Readiness

> [[raw/docs/llms-docs-factory-com/agent-readiness-overview|Raw]] · llms-txt

## Summary

The page introduces the Agent Readiness Model from Factory. Its premise is that agent success depends less on the agent than on the repository: structure, validation and operational signals decide whether autonomous agents can work reliably. The model scores a repository so teams can find and fix gaps before they delegate larger work to Droid, Factory's agent. [[raw/docs/llms-docs-factory-com/agent-readiness-overview#Agent Readiness|cite]]

Scoring is a gated ladder of five levels: Functional, Documented, Standardized, Optimized, Autonomous. Every repository starts at Level 1, and a level unlocks only when 80% of the previous level's criteria pass. Criteria are checked at repository scope (for example CODEOWNERS, branch protection) or application scope per app in a monorepo, shown as scores like `3 / 4`. [[raw/docs/llms-docs-factory-com/agent-readiness-overview#How scoring works|cite]]

Criteria group into nine pillars: Style & Validation, Build System, Testing, Documentation, Development Environment, Debugging & Observability, Security, Task Discovery, Product & Experimentation. Each pillar is justified by what it gives an agent, such as fast feedback from tests or reproducible environments. The page also sketches three end-state workflows: code from conversation, design to implementation, and bug to deployed fix. [[raw/docs/llms-docs-factory-com/agent-readiness-overview#The technical pillars|cite]]

## Key claims

- Four surfaces exist: the `/readiness-report` slash command in Factory App or Droid CLI, a dashboard, a Readiness Reports API, and `/readiness-fix` for automatic remediation. [[raw/docs/llms-docs-factory-com/agent-readiness-overview#Getting started|cite]]
- A level unlocks at 80% pass of the previous level's criteria; all repositories start at Level 1. [[raw/docs/llms-docs-factory-com/agent-readiness-overview#Level progression|cite]]
- Level 2 (Documented) example criteria include AGENTS.md, devcontainer, pre-commit hooks and branch protection. [[raw/docs/llms-docs-factory-com/agent-readiness-overview#The 5 readiness levels|cite]]
- Level 3 adds integration tests, secret scanning, distributed tracing and metrics; Level 4 adds fast CI feedback and flaky test detection; Level 5 is self-improving systems with automatic decomposition into parallel execution. [[raw/docs/llms-docs-factory-com/agent-readiness-overview#The 5 readiness levels|cite]]
- Reproducible environments mean developers and agents work in identical environments, so "entire classes of problems disappear". [[raw/docs/llms-docs-factory-com/agent-readiness-overview#The technical pillars|cite]]
- Security pillar: branch protection, secret scanning and code owners act as guardrails so agents "move fast safely". [[raw/docs/llms-docs-factory-com/agent-readiness-overview#The technical pillars|cite]]

## Notable quotes

> "Agent Readiness measures whether repositories have the structure, validation, and operational signals that let autonomous agents work reliably."
> — [[raw/docs/llms-docs-factory-com/agent-readiness-overview#Agent Readiness|intro]]

> "Agents move fast. Automated guardrails ensure they move fast safely."
> — [[raw/docs/llms-docs-factory-com/agent-readiness-overview#The technical pillars|Security pillar]]

## Connections

- **Entities**: none linked.
- **Concepts**: [[wiki/concepts/dev-environment]], [[wiki/concepts/agent-harness]], [[wiki/concepts/software-factory]]

> Synthesis: Treats the repo, not the agent, as the thing to engineer for autonomy; AGENTS.md and devcontainers as Level 2 criteria echo this wiki's own repo conventions, and the model is Factory's product framing rather than an independent standard.
