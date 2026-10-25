---
type: concept
title: Agent harness
description: The agent runtime that wraps a model with tools and control loops, split by the podcast into an inner harness (the coding agent) and an outer harness (the workflow code around it), and exposed by Warp as a per-agent setting.
aliases: []
sources:
  - "[[wiki/sources/youtube-tGbjIvvYuHE]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-benchmarks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
related:
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/control-plane]]"
  - "[[wiki/concepts/agent-runner]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/agent-evals]]"
  - "[[wiki/concepts/agent-skill]]"
created: 2026-10-25T15:14:42Z
timestamp: 2026-10-25T16:00:00Z
source_count: 8
---

# Agent harness

> Multiple framings: see Definition.

## Definition

Podcast framing: the harness is one layer of the software-factory stack (compute, dev environment, harness, control plane), and it has two parts. The inner harness is a coding agent such as Claude Code or Codex. The outer harness is code around it; Boundary's is hard-coded while loops. [[wiki/sources/youtube-tGbjIvvYuHE]]

Warp framing: the harness is a configurable per-agent setting, the runtime that executes an agent's prompt and model. Supported harnesses are the Warp Agent, Claude Code and Codex. It is chosen separately from model and runner. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

The two framings differ in scope. Warp's "harness" is roughly the podcast's inner harness. The outer-harness job (staging, loops, dispatch) is done in Warp by the foreman and stage agents. [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

## Key claims

- Boundary's factory runs Claude Code or Codex in headless mode as the inner harness, with hard-coded while loops as the outer harness. One loop fixes CodeRabbit comments until mergeable, or stops after 3 iterations and asks a human. [[wiki/sources/youtube-tGbjIvvYuHE]]
- Team-wide corrections fed back into the outer harness are part of the control plane's "compounding engineering" duty. [[wiki/sources/youtube-tGbjIvvYuHE]]
- Each Warp factory agent has its own harness, model and runner. Review should use a different model or harness than implement, so the two do not share blind spots. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Harness `type` accepts `oz`, `claude`, `codex` or `claude-code`. It is set via `agentDefaults.harness` or a per-agent override. `agentDefaults` must set exactly one of `model` or `harness`. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- In the example repo, `model: auto|auto-efficient|auto-genius|<id>` is shorthand for the Warp Agent harness. A `harness:` block names `type: claude` or Codex plus `model` and `auth` (a managed secret such as `ANTHROPIC_API_KEY`). Example 03 pairs a Warp Agent foreman, a Claude Code implementer and a Codex reviewer. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Third-party harnesses need a paid plan and their own auth (Anthropic or Bedrock key for Claude Code, OpenAI key for Codex). A foreman on a third-party harness can still dispatch other agents. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]
- A dispatched run uses the selected agent's environment, runner, host, harness and model unless overridden. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]]
- Warp Benchmarks compare model, harness and runner configurations for one agent on identical fixed tasks, scored for correctness and cost. [[wiki/docs/llms-docs-warp-dev/factories-benchmarks]]
- Each agent run uses the agent's configured model and harness on Warp-hosted or self-hosted compute. [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]
- Skills are written to be harness-portable. Warp's common-skills library keeps them in `.agents/skills/<name>/SKILL.md`, whose `description` is the trigger text a harness matches against the request. The directory is a cross-harness convention (Claude Code reaches it by symlink). The install tooling defaults to `--agent warp`, though the underlying `skills` CLI is multi-agent. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]

## Relationships

- **Software factory**: the harness is one layer of the stack. [[wiki/concepts/software-factory]]
- **Control plane**: dispatches work to the harness and feeds corrections back to it. [[wiki/concepts/control-plane]]
- **Agent runner**: where the harness executes; Warp configures it separately. [[wiki/concepts/agent-runner]]
- **Factory as code**: harness choice is a field in the definition files. [[wiki/concepts/factory-as-code]]
- **Agent evals**: benchmarks treat the harness as a variable to test. [[wiki/concepts/agent-evals]]
- **Agent skill**: skills are the portable layer that any harness loads. [[wiki/concepts/agent-skill]]

## Tensions

The podcast splits the harness into inner and outer parts and says to own the outer one; Warp offers one harness field and a managed foreman pipeline instead. [[wiki/sources/youtube-tGbjIvvYuHE]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]

> Synthesis: Seven of eight sources are one vendor voice (Warp's docs plus its two repos, factory-examples and common-skills), so their agreement is not corroboration; the repos mostly restate the docs' harness field in worked YAML. The podcast is the only independent voice, and its speakers also sell or build competing products. Treat all as design vocabulary, not neutral evidence.
