---
type: source
title: Agent management
description: "Port's agent management section frames governance of code-first, cloud-managed and Port-native AI agents, skills and MCP servers as one layer, with agents acting as platform consumers, platform components or reusable building blocks."
origin: llms-txt
original_path: https://docs.port.io/agent-management/overview.md
source_url: https://docs.port.io/agent-management/overview.md
authors: []
published_date: null
raw_file: raw/docs/llms-docs-port-io/agent-management-overview.md
created: 2026-10-25T18:50:00Z
timestamp: 2026-10-25T18:50:00Z
entities:
  - "[[wiki/entities/claude-code]]"
  - "[[wiki/entities/port]]"
concepts:
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/control-plane]]"
---

# Agent management

> [[raw/docs/llms-docs-port-io/agent-management-overview|Raw]] · llms-txt

## Summary

This is the landing page of Port's "agent management" docs. Its premise: every AI agent in an organization needs governance over what data it reads, what actions it takes and who may use it. Port sorts agents into three kinds: code-first (built with SDKs, in repos or CI, e.g. Claude Code), cloud-managed (vendor control planes such as Bedrock/AgentCore, Azure AI Foundry, Cursor Cloud Agents) and Port-native. [[raw/docs/llms-docs-port-io/agent-management-overview#Agent management|cite]]

Agents relate to the "software factory" in three roles. As platform consumers, coding agents read owner, dependency and standards context from Port and run governed self-service actions, via the Port MCP server. As internal platform components, the platform itself triggers a registered agent from an event (a new vulnerability, a nightly scan) and teams wake up to open PRs. As reusable building blocks, self-service workflows (Create an agent, Onboard an LLM, Add MCP server, Publish a skill) hand back governed agents with identity, approved tools and scope. [[raw/docs/llms-docs-port-io/agent-management-overview#what-roles-do-ai-agents-play-in-port|cite]]

The rest is a map of capabilities: AI gateways, external agent discovery, an agentic registry, skills/prompts/MCP connectors, custom agents, Context Lake data-access scoping and the MCP server. Detail lives on child pages.

## Key claims

- Without a shared layer, agents, skills, prompts and MCP servers scatter across teams, so platform teams cannot see what exists, control access or avoid duplication. [[raw/docs/llms-docs-port-io/agent-management-overview#govern-agents-skills-and-mcp-at-scale|cite]]
- The Port MCP server exposes catalog context and workflows so tools like Claude Code, Cursor and GitHub Copilot work with the same source of truth and guardrails as humans. [[raw/docs/llms-docs-port-io/agent-management-overview#ai-agents-as-platform-consumers|cite]]
- Event-driven agents (security remediation, self-healing incidents) can be run from the agent registry inside workflows, with no per-case request. [[raw/docs/llms-docs-port-io/agent-management-overview#ai-agents-as-internal-platform-components|cite]]
- "Agent" also covers LLMs, MCP servers and skills; their lifecycle is made a governed process through self-service workflows. [[raw/docs/llms-docs-port-io/agent-management-overview#ai-as-reusable-building-blocks|cite]]
- Skills are reusable instructions that Port AI and MCP clients load at runtime, with adoption measured in Cursor and Claude. [[raw/docs/llms-docs-port-io/agent-management-overview#skills|cite]]
- MCP connectors let teams choose which tools of external MCP servers developers and agents may use, with the same permissions and audit trail as the rest of Port. [[raw/docs/llms-docs-port-io/agent-management-overview#mcp-connectors|cite]]

## Notable quotes

> "Port brings agents, skills, prompts, and MCP under one governance layer so teams can move fast without losing control."
> — [[raw/docs/llms-docs-port-io/agent-management-overview#how-port-helps|How Port helps]]

## Connections

- **Entities**: [[wiki/entities/claude-code]], [[wiki/entities/port]]
- **Concepts**: [[wiki/concepts/mcp]], [[wiki/concepts/agent-skill]], [[wiki/concepts/control-plane]]

> Synthesis: Port is a governance and registry layer over agents it mostly does not run, a platform-engineering take on the software factory unlike the agent-runner products elsewhere in this wiki; the page is an overview and defers all mechanism to child pages.
