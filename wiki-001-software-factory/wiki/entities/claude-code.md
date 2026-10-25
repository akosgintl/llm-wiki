---
type: entity
title: Claude Code
description: "Anthropic's coding agent, used in this wiki as a harness that factories run per role, an MCP client, and a consumer of .agents/skills."
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/sources/youtube-tGbjIvvYuHE]]"
related:
  - "[[wiki/entities/codex]]"
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/mcp]]"
created: 2026-10-25T15:14:44Z
timestamp: 2026-10-25T16:00:00Z
source_count: 7
---

# Claude Code

> Anthropic's coding agent; here it appears as a pluggable harness in a software factory, an MCP client, and a skills consumer.

## Definition

Sources treat Claude Code as the agent runtime that does the coding, not as the factory itself. In Warp's docs it is one of three supported harnesses (Warp Agent, Claude Code, Codex) chosen per factory agent. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]] In the Boundary podcast it is the harness, run headless, inside Boundary's in-house factory. [[wiki/sources/youtube-tGbjIvvYuHE]]

## Key claims

- Warp lists Claude Code as a per-agent harness. A foreman on Claude Code can still dispatch other factory agents, tracked as its children. Third-party harnesses need a paid plan. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]
- Auth for the Claude Code harness takes an Anthropic API key, Bedrock API key or Bedrock access key. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]
- In definition files, harness `type` accepts `claude` or `claude-code`, set by `agentDefaults.harness` or a per-agent override. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]] The example repo shows `type: claude` with `model: opus` and a managed-secret `ANTHROPIC_API_KEY`. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Example 03 (multi-harness) pairs a Warp Agent foreman, a Claude Code implementer and a Codex reviewer. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Claude Code calls its model provider directly from the execution environment. The Warp Agent instead routes model requests through Warp. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]
- Claude Code is an example client for Warp's hosted Factory MCP server. A connected client acts with its account's full permissions; there are no read-only scopes. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]
- Claude Code reaches the cross-harness `.agents/skills/` directory via symlink; Warp's common-skills repo lists it among harnesses that consume installed skills. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- Boundary's factory ("agent tries BAML") runs Claude Code or Codex headless on a pool of MacBooks, wrapped by hard-coded while loops as outer harness. [[wiki/sources/youtube-tGbjIvvYuHE]]
- Warp advises that the review agent use a different model or harness than implement, so they do not share blind spots. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]

## Relationships

- **Codex**: peer harness, listed beside Claude Code in every origin. [[wiki/entities/codex]]
- **Warp Factories**: hosts Claude Code as a harness option. [[wiki/entities/warp-factories]]
- **Agent harness**: Claude Code is a concrete instance. [[wiki/concepts/agent-harness]]
- **Agent skill**: consumes `.agents/skills/` via symlink. [[wiki/concepts/agent-skill]]
- **MCP**: Claude Code consumes MCP servers such as Factory MCP. [[wiki/concepts/mcp]]

## Tensions

Warp's pages show Claude Code as a first-class, swappable harness. The podcast shows it embedded inside a self-built loop with no vendor control plane. No source evaluates Claude Code's quality.

> Synthesis: Corroboration is thin and partly false. The four docs pages and the two Warp repos (warp-factory-examples, common-skills) are one vendor voice (Warp), so six pages count as one origin. The Boundary podcast is the only independent voice. Every claim resting only on Warp pages (auth options, `claude`/`claude-code` type, direct provider calls, MCP client role, skills symlink) is single-vendor. Both origins only describe Claude Code as a harness slot.
