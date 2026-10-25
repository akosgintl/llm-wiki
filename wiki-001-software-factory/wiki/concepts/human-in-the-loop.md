---
type: concept
title: Human-in-the-loop
description: Designing an agent pipeline so people approve the decisions that matter (specs, plans, merges, escalations) while agents do the rest.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-8090-ai/connections-connect-coding-agent]]"
  - "[[wiki/docs/llms-docs-8090-ai/modules-automations]]"
  - "[[wiki/docs/llms-docs-8090-ai/modules-work-orders]]"
  - "[[wiki/docs/llms-docs-8090-ai/opinions-reverse-engineering]]"
  - "[[wiki/docs/llms-docs-factory-com/delegations-index]]"
  - "[[wiki/docs/llms-docs-factory-com/droid-exec-overview]]"
  - "[[wiki/docs/llms-docs-factory-com/missions-overview]]"
  - "[[wiki/docs/llms-docs-port-io/getting-started-agentic-sdlc-pillars]]"
  - "[[wiki/docs/llms-docs-port-io/solutions-agentops-overview]]"
  - "[[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-agentic-initiatives]]"
  - "[[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]"
  - "[[wiki/docs/llms-docs-port-io/workflows-concepts]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-demo-sentry-monitoring-with-sdk]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-inbox]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-github]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-quickstart]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/docs/llms-factory-mastra-ai/configure-boards-and-rules]]"
  - "[[wiki/docs/llms-factory-mastra-ai/using-intake]]"
  - "[[wiki/docs/llms-factory-mastra-ai/using-reviews]]"
  - "[[wiki/docs/llms-factory-mastra-ai/using-sessions]]"
  - "[[wiki/docs/llms-factory-mastra-ai/using-work-and-approvals]]"
  - "[[wiki/docs/llms-factory-mastra-ai/what-is-factory]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/sources/youtube-tGbjIvvYuHE]]"
related:
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/agent-evals]]"
  - "[[wiki/concepts/control-plane]]"
  - "[[wiki/concepts/agentic-merge-queue]]"
  - "[[wiki/concepts/foreman-agent]]"
created: 2026-10-25T15:15:38Z
timestamp: 2026-10-25T18:31:57Z
source_count: 36
---

# Human-in-the-loop

> People hold a few chosen checkpoints; agents run everything between them.

## Definition

Vendors converge on the same shape: agents triage, plan, implement and review, while a person approves the spec or plan, answers questions and presses merge. Warp names three default pauses: spec approval, clarifying questions, merging. [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]], [[wiki/docs/llms-docs-warp-dev/factories]] Mastra lists four waits: start a run, accept a non-bug task, approve a plan, merge. [[wiki/docs/llms-factory-mastra-ai/what-is-factory]], [[wiki/docs/llms-factory-mastra-ai/using-work-and-approvals]] Port draws checkpoints at Plan, Build and Review. [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]] The Boundary podcast targets "95% automatic", not fully automatic. [[wiki/sources/youtube-tGbjIvvYuHE]]

## Key claims

- Agents never merge. Warp's implement agent "never merges" and review is advisory; the foreman prompt forbids merging or approving a spec for a human. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Agent output and human decision stay separate. Mastra: a finished review run is not a merge, and neither closes the issue. 8090 coding agents end at "In Review" for a teammate. The headless `review-pr` skill never posts; a workflow publishes it. [[wiki/docs/llms-factory-mastra-ai/using-reviews]], [[wiki/docs/llms-docs-8090-ai/connections-connect-coding-agent]], [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- Merge is enforced by repository rules. Warp, Factory.com ("the requester can still approve a Factory-authored pull request") and Port's criticality-routed policy (auto-merge low-risk, human for tier-1) all lean on this. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]], [[wiki/docs/llms-docs-factory-com/delegations-index]], [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-agentic-initiatives]]
- Attention is queued: Warp's inbox, Mastra's Overview and sessions show questions, plans and failures. Humans steer mid-run and take work over. [[wiki/docs/llms-docs-warp-dev/factories-factory-inbox]], [[wiki/docs/llms-factory-mastra-ai/using-sessions]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]], [[wiki/docs/llms-docs-factory-com/missions-overview]]
- Autonomy is a dial: Mastra's Auto-start runs and Auto-approve plans (off while learning); Droid exec's read-only default and `--auto` tiers; Warp measures merged PRs needing no human push. [[wiki/docs/llms-factory-mastra-ai/using-intake]], [[wiki/docs/llms-docs-factory-com/droid-exec-overview]], [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]
- Approval nodes can be built in: Port's workflow input node pauses for a human; Mastra transition policies enforce approval. [[wiki/docs/llms-docs-port-io/workflows-concepts]], [[wiki/docs/llms-factory-mastra-ai/configure-boards-and-rules]]
- Destructive actions need confirmation: 8090 agents that cannot show confirmations cannot delete or edit automations. 8090 reverse engineering offers cooperative or autonomous runs and never overwrites human edits. [[wiki/docs/llms-docs-8090-ai/connections-connect-coding-agent]], [[wiki/docs/llms-docs-8090-ai/opinions-reverse-engineering]]
- Self-improvement proposals arrive as PRs; "nothing is adopted on its own". [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]]

## Tensions

- **Where the gate lives.** Warp: spec approval is editable prompt policy, merge is repository permission. Mastra: "a prompt alone does not enforce human approval; a transition policy does." The podcast gates by code (3-iteration cap). Prompt-level gates are the weaker kind. [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]], [[wiki/docs/llms-factory-mastra-ai/configure-boards-and-rules]], [[wiki/sources/youtube-tGbjIvvYuHE]]
- **Gates traded for scoping.** 8090 Automations run unattended: Allow-only tools, comment-only output, no approval. [[wiki/docs/llms-docs-8090-ai/modules-automations]]
- **Humans out of some loops.** Warp's common-skills CI auto-squash-merges lockfile PRs after checks pass; these are bot workflows, not factory agents. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]

## Relationships

- **Software factory**: checkpoints are part of its lifecycle. [[wiki/concepts/software-factory]]
- **Factory as code**: gate policy lives in definition files. [[wiki/concepts/factory-as-code]]
- **Agent evals**: scorers decide what goes back to humans. [[wiki/concepts/agent-evals]]

> Synthesis: Six vendor voices (Warp docs plus its two repos, 8090, Factory.com, Port, Mastra) plus one podcast agree that humans merge. Agreement between competing vendors is mild corroboration, but all are product docs, and the Warp docs and repos share one author.
