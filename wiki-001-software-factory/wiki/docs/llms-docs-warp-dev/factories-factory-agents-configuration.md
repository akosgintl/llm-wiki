---
type: source
title: Configuring factory agents
description: Warp's docs state how to edit a factory agent's prompt, model, harness (Warp Agent, Claude Code, Codex), runner, MCPs and secrets, in the web app or as definition files.
origin: llms-txt
original_path: https://docs.warp.dev/factories/factory-agents/configuration/
source_url: https://docs.warp.dev/factories/factory-agents/configuration/
authors: []
published_date: null
raw_file: raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration.md
created: 2026-10-25T14:59:45Z
timestamp: 2026-10-25T14:59:45Z
entities:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/claude-code]]"
  - "[[wiki/entities/codex]]"
concepts:
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/secrets-management]]"
  - "[[wiki/concepts/agent-runner]]"
---

# Configuring factory agents

> [[raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration|Raw]] · llms-txt

## Summary

This Warp Factories docs page is a how-to for changing an existing factory agent. The docs state that an agent's instructions (prompt), tools, model and harness can be edited in the Warp Factories web app or through definition files. Editing needs factory editor access or team/workspace admin. [[raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration#Prerequisites|cite]]

Where you edit depends on how the factory is backed. A Warp-managed factory is edited in the web app (Agents page, then the agent's Settings tab, then Save). A GitHub-backed factory is read-only in the web app and is edited via the factory definition files. [[raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration#Edit agent settings and instructions|cite]]

The page's main design point is per-agent harness and model choice. Each role gets its own pairing, and review should use a different model or harness than implement so they do not share blind spots. [[raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration#Choose models and harnesses per agent|cite]]

## Key claims

- Settings tab fields: description, harness, model, runner, host, MCP servers, secrets; the prompt is edited separately via **Prompt**. [[raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration#Edit agent settings and instructions|cite]]
- Supported harnesses are the Warp Agent, Claude Code and Codex. A foreman on Claude Code or Codex can still dispatch other factory agents, tracked as its children. [[raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration#Choose models and harnesses per agent|cite]]
- Third-party harnesses need a paid plan; on Free, agents use the Warp Agent. [[raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration#Choose models and harnesses per agent|cite]]
- Suggested optimization per role: foreman for orchestration and long conversations; triage for research and tools; spec for requirements synthesis; implement for coding strength and toolchain fit; review for a different model/harness than implement. [[raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration#Choose models and harnesses per agent|cite]]
- Claude Code harness auth takes an Anthropic API key, Bedrock API key or Bedrock access key; Codex takes an OpenAI API key. The Auth field uses a team-owned secret, or **New auth secret**. [[raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration#Configuring a third-party harness|cite]]
- In GitHub-backed factories, harness is set by `agentDefaults.harness` or a per-agent `harness` override; example `03-multi-harness` in warp-factory-examples. [[raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration#Configuring a third-party harness|cite]]
- The model picker also lists custom routers from accessible factories. [[raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration#Choose models and harnesses per agent|cite]]

## Notable quotes

> "Review: A different model or harness from the implement agent, so the two don't share blind spots"
> — [[raw/docs/llms-docs-warp-dev/factories-factory-agents-configuration#Choose models and harnesses per agent|model table]]

## Connections

- **Entities**: [[wiki/entities/warp-factories]], [[wiki/entities/claude-code]], [[wiki/entities/codex]]
- **Concepts**: [[wiki/concepts/agent-harness]], [[wiki/concepts/factory-as-code]], [[wiki/concepts/mcp]], [[wiki/concepts/secrets-management]], [[wiki/concepts/agent-runner]]

> Synthesis: Vendor how-to, not independent evidence; its useful idea is cross-model review (different harness for review vs implement) as a cheap guard against shared blind spots, and harness-as-per-role setting.
