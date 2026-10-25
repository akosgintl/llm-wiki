---
type: concept
title: Human-in-the-loop
description: Designing an agent pipeline so people approve the decisions that matter (specs, merges, escalations) while agents do the rest.
aliases: []
sources:
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
timestamp: 2026-10-25T16:00:00Z
source_count: 18
---

# Human-in-the-loop

> People stay in charge of a few chosen checkpoints; agents run everything between them.

## Definition

In a software factory, human-in-the-loop means agents triage, plan, implement and review, but a person approves the spec, answers clarifying questions and presses merge. Warp's docs name three default pauses: spec approval, clarifying questions and merging. [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]], [[wiki/docs/llms-docs-warp-dev/factories]]

The `warp-factory-examples` foreman prompt encodes the same gate as text: "A human is always responsible for merging. Never merge, and never approve a spec on a human's behalf." [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

The Boundary podcast frames the same idea as a target: "95% automatic", not fully automatic, with a human shepherd and a human merge press. [[wiki/sources/youtube-tGbjIvvYuHE]]

## Key claims

- Spec approval and clarifying questions are workflow policy in the foreman's editable instructions; merging is enforced by repository branch protection and permissions. [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/docs/llms-docs-warp-dev/factories]]
- Agents never merge: implement "never merges", review "doesn't approve or merge", and the review verdict is advisory. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]
- Factory branches and PRs obey normal repository rules (branch protection, required reviews). [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]], [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]
- Work from Slack still ends at a pull request for a person; the SDK Sentry demo ends in a draft PR "instead of silent autonomous changes". [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]], [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-demo-sentry-monitoring-with-sdk]]
- Human attention is queued: the inbox holds questions, spec reviews, PR reviews, blocked and failed items for tasks the user started. [[wiki/docs/llms-docs-warp-dev/factories-factory-inbox]], [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]
- Autonomy is measured as the share of merged PRs needing no human code push. [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]
- Self-improvement proposals arrive as PRs with a reviewer (default team admins) and "nothing is adopted on its own". [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]], [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]
- Access comes from configuration and credentials, never from instructions; factory roles do not control spec or PR review. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]
- A person can take work over: Factory MCP pulls a task to a local machine and hands it back, but does not lock the task. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]
- Humans can steer mid-run: replies continue a work item, live follow-up works while the sandbox is active, and Stop run is immediate. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]], [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]], [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]
- Slack, GitLab and Linear can start work, and the commenter need not be a team member in GitLab, so repository gates matter. [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]]
- The quickstart advises a small, verifiable first request ending in a PR. [[wiki/docs/llms-docs-warp-dev/factories-quickstart]]
- Boundary's loop fixes CodeRabbit comments, stops after 3 iterations to ask a human, and a human presses merge. Untrusted user feedback is deduped and repro'd before a human shepherd is assigned. [[wiki/sources/youtube-tGbjIvvYuHE]]
- In the example SDLC factory the spec agent opens a spec PR and waits for human approval, and the foreman hands over final PR links for a human to merge. Example 04 (review only) makes findings advisory. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- The `saga` skill has a human-in-the-loop shape: plan with user approval, worker loop, final validation with the user. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- The headless `review-pr` skill never posts to GitHub; a workflow publishes its `review.json`, so output is separated from publishing. `migrate-to-factory` is scope-fenced (no secrets, schedules, live registration) and treats source content as untrusted. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- The factory validator reports exit 2 as "NOT validated, not a pass", so an unchecked config is never read as approved. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

## Tensions

- **Where the gate lives.** Warp says spec approval is a prompt policy the team can change, while merge is a repository permission. The podcast shows a hard-coded loop cap (3 iterations) and a human merge press. The docs gate by configuration; the talk gates by code. [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]], [[wiki/sources/youtube-tGbjIvvYuHE]]
- **Humans out of some loops.** `complain` and `suggestion-box` skills let agents submit anonymous Slack feedback unprompted, and common-skills CI auto-squash-merges lockfile PRs once checks pass after requesting the source author's review. These are bot workflows, not factory agents, so they do not contradict "agents never merge", but they show human review is not universal even inside Warp. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- **Soft gate.** Prompt-level spec approval is not enforced like branch protection, so it is weaker. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]

## Relationships

- **Software factory**: the checkpoints are part of its lifecycle. [[wiki/concepts/software-factory]]
- **Factory as code**: gate policy lives in definition files, and changes go through PR review. [[wiki/concepts/factory-as-code]]
- **Agent evals**: scorers and benchmarks decide what to hand back to humans. [[wiki/concepts/agent-evals]]

> Synthesis: Corroboration is thin. Seventeen pages are one vendor voice: the Warp docs set plus two Warp-authored repos (`warp-factory-examples`, `common-skills`). The repos show the docs' stance implemented in prompts and CI, which is consistency within one vendor, not independent confirmation. The only outside view is one podcast of two vendors (Human Layer and Boundary), so the shared "humans merge" stance reflects vendor product positions.
