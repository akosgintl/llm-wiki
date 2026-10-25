---
type: concept
title: Foreman agent
description: "The single coordinator agent in a Warp factory that receives work from triggers and chat, delegates to stage agents, and hands finished pull requests to a human."
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-quickstart]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
related:
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/software-factory]]"
created: 2026-10-25T00:00:00Z
timestamp: 2026-10-25T00:00:00Z
source_count: 4
---

# Foreman agent

> The one orchestrating agent per factory: it takes the request, dispatches the other agents, and stops at a human merge.

## Definition

In Warp Factories the foreman is the factory's coordinator. The quickstart says the first request goes to the foreman, which dispatches the agents it needs; progress appears as foreman and child runs. [[wiki/docs/llms-docs-warp-dev/factories-quickstart]] The examples repo makes it structural: a factory has exactly one agent with `agentType: FOREMAN` (alias `MAIN`), and automations wake it with their body as the task. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

The foreman is also the human-facing handle. The factory name sets the default foreman name, which the team @-mentions in Slack and Linear. [[wiki/docs/llms-docs-warp-dev/factories-quickstart]] Its definition is a Markdown prompt, so orchestration logic lives in prose, not code. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

## Key claims

- The foreman orchestrates but does not do the work; its prompt is a numbered procedure that delegates to triage, spec, implement and review agents. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- The wizard lets the admin choose which agents the foreman may dispatch (Triage, Spec, Code, Review default on); leaving Code on is what yields a pull request. [[wiki/docs/llms-docs-warp-dev/factories-quickstart]]
- Chat and tracker intake route to it: Slack mentions and DMs, Teams `app_mention`, Linear sessions, GitHub events. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Automations name it as their agent, including scheduled ones (a nightly Slack digest with `agent: foreman`; a Teams mention automation). [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]]
- Human gate in the prompt: the foreman never merges and never approves a spec for a human. Work ends at a pull request. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]], [[wiki/docs/llms-docs-warp-dev/factories-quickstart]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]
- Multi-repo work needs one PR per repo; the foreman waits for all PRs before hand-off and applies a `factory:<alias>` routing label. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Roles can collapse: example 04 makes the reviewer the foreman, with advisory findings. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Automation-started work runs as the chosen factory agent, not the person who triggered it. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]

## Relationships

- **factory-as-code**: the foreman is defined as a file in the factory tree. [[wiki/concepts/factory-as-code]]
- **human-in-the-loop**: the merge gate is written into the foreman prompt. [[wiki/concepts/human-in-the-loop]]
- **software-factory**: the foreman is the coordinating role in Warp's version of the idea. [[wiki/concepts/software-factory]]

> Synthesis: All four sources are Warp's own voice (its docs set and its example repo), so they corroborate each other weakly. No outside source yet describes the foreman pattern.
