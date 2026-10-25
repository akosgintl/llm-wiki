---
type: entity
title: Codex
description: Codex is OpenAI's coding agent, which software-factory setups use as a swappable agent harness alongside Claude Code.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
  - "[[wiki/sources/youtube-tGbjIvvYuHE]]"
related:
  - "[[wiki/entities/claude-code]]"
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/secrets-management]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/agent-skill]]"
created: 2026-10-25T15:14:45Z
timestamp: 2026-10-25T16:30:00Z
source_count: 7
---

# Codex

> A coding-agent CLI (OpenAI) that the sources treat as one interchangeable harness option next to Claude Code.

## Definition

In every source, Codex is a coding-agent harness that can run headless inside a factory. No source explains Codex itself; they describe how a factory plugs it in. Warp's docs list it as one of three supported harnesses (Warp Agent, Claude Code, Codex), chosen per agent. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]

The podcast uses it in practice: Boundary's in-house factory runs Claude Code or Codex in headless mode. [[wiki/sources/youtube-tGbjIvvYuHE]]

## Key claims

- Codex is a supported factory harness. In definition files the harness `type` accepts `oz`, `claude`, `codex` or `claude-code`. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]
- Worked example: `examples/03-multi-harness` pairs a Warp Agent foreman, a Claude Code implementer and a Codex reviewer. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Auth uses an OpenAI API key, held as a team-owned secret. Third-party harnesses need a paid plan; Free uses the Warp Agent. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]
- Third-party harnesses authenticate via a managed secret (`auth.source: managedSecret`) or a self-hosted worker's environment. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- A foreman on Codex can still dispatch other factory agents, tracked as its children. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]
- Review should use a different model or harness than implement, so the two do not share blind spots. Codex can fill that role. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Codex calls its provider directly from the execution environment. The Warp Agent instead routes model requests through Warp. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]
- Codex is an example client for Factory MCP, which lets a local agent send tasks to a factory and pull tasks down. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]
- Other CLI agents cannot be the execution host but can exchange work through Factory MCP. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]
- Shared skills (`.agents/skills/<name>/SKILL.md`) are installed for a set of harnesses including Codex, so one skill library serves all of them. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- Dex queues about 15 overnight prompts of implement, review and Codex-review steps for large features. The episode also has a tangent comparing Codex and Claude models. [[wiki/sources/youtube-tGbjIvvYuHE]]

## Relationships

- **Claude Code**: sibling harness, always listed beside Codex. [[wiki/entities/claude-code]]
- **Warp Factories**: hosts Codex as a per-agent harness choice. [[wiki/entities/warp-factories]]
- **Agent harness**: Codex is a concrete instance of the pattern. [[wiki/concepts/agent-harness]]
- **MCP**: Codex connects to Factory MCP as a client. [[wiki/concepts/mcp]]
- **Secrets management**: its OpenAI key is a harness-auth credential. [[wiki/concepts/secrets-management]]
- **Factory as code**: harness choice is declared in agent files. [[wiki/concepts/factory-as-code]]
- **Agent skill**: skills are shared across harnesses including Codex. [[wiki/concepts/agent-skill]]

> Synthesis: Corroborated across three origins, but the Warp docs set and the two Warp repos are one vendor voice, so the Warp-specific claims (harness `type`, auth, example 03, skills install) have no independent support; only the podcast, a separate voice, shows Codex used as a harness. No source evaluates Codex, they only treat it as swappable.
