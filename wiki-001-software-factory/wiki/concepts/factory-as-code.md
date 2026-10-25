---
type: concept
title: Factory as code
description: A software factory declared as a versioned tree of YAML and Markdown files, rooted at factory.yaml, that the platform validates and applies as one unit.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-automations]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-benchmarks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-azure-devops]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-github]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-runners]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-secrets-aws-ecr]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-secrets]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-warp-hosting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks-vercel]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
related:
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/agent-runner]]"
  - "[[wiki/concepts/agent-evals]]"
  - "[[wiki/concepts/webhook]]"
  - "[[wiki/concepts/secrets-management]]"
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/concepts/human-in-the-loop]]"
created: 2026-10-25T00:00:00Z
timestamp: 2026-10-25T00:00:00Z
source_count: 33
---

# Factory as code

> A factory is a git-versioned file tree, not a console configuration: path is identity, Markdown body is prompt, YAML is topology.

## Definition

The docs define a factory definition as "a versioned tree of YAML and Markdown files rooted at `factory.yaml`" covering agents, automations, runners, model routers, benchmarks, scorers, skills and webhooks. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]] [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]] A resource's identity is its path: `agents/reviewer/agent.md` is the agent `reviewer`. Runs, work items and metrics stay in the web app, outside the definition. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]

The example repo shows the same model in practice: eight definition trees that Warp syncs from GitHub. Behaviour lives in YAML (topology, models, compute) and Markdown prompts (roles, task bodies); the only code is validation scripts. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

## Key claims

- **Layout.** `factory.yaml` holds repositories, integrations, `schemaVersion` (`v1alpha1`) and `agentDefaults`; then `agents/<name>/agent.md`, `automations/<name>/automation.md`, `runners/*.yaml`, `scorers/<name>/scorer.md`, `benchmarks/`, `webhooks/` and `skills/`. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- **Agents.** Frontmatter is config, body is the prompt. Exactly one `FOREMAN` orchestrates; other roles are `TRIAGE`, `SPEC`, `IMPLEMENT`, `REVIEW`, `VERIFY`, `CUSTOM`. Harness (Warp Agent, Claude Code, Codex) or model, runner and secrets are set per agent, and review should differ from implement. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- **Custom agents** are UID-addressed bundles the foreman dispatches via `run_agents`. They have no built-in skills. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]], [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]
- **Triggers.** An automation's `triggers` frontmatter (provider, event, `filter`) wakes an agent, usually the foreman, with the body as the task. Filters are AND-combined and fail closed. [[wiki/docs/llms-docs-warp-dev/factories-automations]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- **Skills** live at `skills/<name>/SKILL.md` (all agents) or `agents/<agent>/skills/<name>/SKILL.md` (one). They carry instructions, not access. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]], [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- **Versioning.** Warp-managed definitions are edited in the web app and committed by Warp. On a paid plan the definition lives in the team's GitHub repo; pull requests run the `warp/factory-config` check, and merging to the production branch updates the factory. The web UI is then read-only. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]], [[wiki/docs/llms-docs-warp-dev/factories-secrets]]
- **Apply and validate.** Warp applies a definition as one unit and keeps the last valid one on failure. Validation runs on save, in PRs, via a Python script against Warp's validation service, via JSON Schemas, or via Factory MCP. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- **Deploy.** The same definition runs on Warp-hosted sandboxes or managed self-hosted workers (`workerHost`); runners declare OS, shape and image. Secrets are referenced by name, never inlined. [[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]], [[wiki/docs/llms-docs-warp-dev/factories-runners]], [[wiki/docs/llms-docs-warp-dev/factories-secrets]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]
- **Self-modifying loop.** Scorers sample runs; with `selfImprovement`, failures become PRs against skills or the definition, reviewed by a human. Benchmarks compare configurations on pinned commits. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]], [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]], [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]
- **Skills distribution.** `common-skills` versions skills as a library, pinned by a consumer `skills-lock.json`, with bot PRs on each merge; its `migrate-to-factory` skill ports skills into a factory repo. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- **Runtime stays outside the file.** Runs can be driven by API/SDK and Factory MCP against the same factory. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]

## Relationships

- **Software factory**: factory-as-code is one way to make the factory declarative and reviewable. [[wiki/concepts/software-factory]]
- **Agent evals**: scorers and benchmarks are definition files. [[wiki/concepts/agent-evals]]
- **Human in the loop**: the foreman prompt encodes the human merge gate; self-improvement arrives as PRs. [[wiki/concepts/human-in-the-loop]]

> Synthesis: Every origin here is Warp's own voice (its docs set plus two Warp-authored repos), so the repos corroborate the docs' syntax but are not independent evidence that the model works well.
