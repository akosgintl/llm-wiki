---
type: concept
title: Model Context Protocol (MCP)
description: An open protocol by which agents and coding tools reach external tools, data and workflows through servers they connect to as clients.
aliases: [MCP, MCP server, Model Context Protocol]
sources:
  - "[[wiki/docs/llms-docs-8090-ai/opinions-agent-skill]]"
  - "[[wiki/docs/llms-docs-factory-com/droid-exec-overview]]"
  - "[[wiki/docs/llms-docs-factory-com/harness-subagents]]"
  - "[[wiki/docs/llms-docs-factory-com/missions-overview]]"
  - "[[wiki/docs/llms-docs-port-io/agent-management-overview]]"
  - "[[wiki/docs/llms-docs-port-io/agent-management-skills-overview]]"
  - "[[wiki/docs/llms-docs-port-io/context-lake-overview]]"
  - "[[wiki/docs/llms-docs-port-io/glossary]]"
  - "[[wiki/docs/llms-docs-port-io/solutions-agentops-overview]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/sources/youtube-b5O6gb_Zuk8]]"
related:
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/agent-harness]]"
created: 2026-10-25T18:31:23Z
timestamp: 2026-10-26T07:15:27Z
source_count: 17
---

# Model Context Protocol (MCP)

> The connector layer that gives agents access to a system's data and actions, while skills supply the workflow.

## Definition

Across four vendor docs sets (8090, Factory, Port, Warp) and one podcast, MCP is the way an agent reaches a software factory's data and actions. The sources use it in two directions. A platform acts as an MCP server that exposes itself to outside coding agents (Port, Warp, 8090). Or an agent acts as an MCP client that connects to external servers such as Notion, Linear or Atlassian (Factory, Port, Warp).

The sources treat the protocol itself as given; they document products built on it.

## Key claims

- MCP supplies access, skills supply workflow: connect MCP before installing the 8090 skill. [[wiki/docs/llms-docs-8090-ai/opinions-agent-skill]] Warp says the same: skills carry instructions only, so MCP credentials are configured separately. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]
- Warp's Factory MCP is a hosted server (streamable HTTP, browser sign-in or agent API key) that lets any coding agent create factories, send work in, pull a task down and hand it back. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]
- Warp's server has no read-only or per-factory scopes, and picking up a task does not lock it. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]
- The Port MCP server exposes catalog context and actions to Claude Code, Cursor and Copilot. [[wiki/docs/llms-docs-port-io/agent-management-overview]], [[wiki/docs/llms-docs-port-io/glossary]] It also serves skills through a `load_skill` tool. [[wiki/docs/llms-docs-port-io/agent-management-skills-overview]]
- Port MCP connectors route external servers through a governed gateway, with per-tool selection, shared permissions and audit. [[wiki/docs/llms-docs-port-io/agent-management-overview]], [[wiki/docs/llms-docs-port-io/context-lake-overview]] Port flags MCP servers that expose every tool by default as a sprawl risk. [[wiki/docs/llms-docs-port-io/solutions-agentops-overview]]
- Factory droids scope MCP servers per subagent: `[]` excludes all, omitting inherits the parent's set, and enterprise-blocked servers stay blocked. [[wiki/docs/llms-docs-factory-com/harness-subagents]] Tools can be restricted by MCP server in `droid exec`, and existing MCP integrations work inside Missions. [[wiki/docs/llms-docs-factory-com/droid-exec-overview]], [[wiki/docs/llms-docs-factory-com/missions-overview]]
- Warp agents get MCP servers and secrets through configuration; access never comes from instructions. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]] Factory definitions declare MCP servers and reference secrets by name. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]
- Warp provides Slack tools built in, so no Slack MCP server is needed. For Jira runs with no human creator, it says to add the Atlassian MCP server. [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]]
- Every MCP tool description is advertised in every session and spends the instruction budget, like subagent and skill descriptions. Claude Code now switches to a tool-search step once tool text passes roughly 10K. [[wiki/sources/youtube-b5O6gb_Zuk8]]

## Tensions

- Governance differs. Port wraps MCP in a gateway with per-tool control and audit, and warns about default-open servers. [[wiki/docs/llms-docs-port-io/agent-management-overview]], [[wiki/docs/llms-docs-port-io/solutions-agentops-overview]] Warp's Factory MCP is all-or-nothing per account. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]
- Skill delivery differs. Port serves skills over MCP. [[wiki/docs/llms-docs-port-io/agent-management-skills-overview]] 8090 and Warp keep skills separate from MCP. [[wiki/docs/llms-docs-8090-ai/opinions-agent-skill]], [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]
- Context cost differs in emphasis. Port frames default-open MCP tools as a governance sprawl risk. [[wiki/docs/llms-docs-port-io/solutions-agentops-overview]] The Boundary podcast frames the same tool sprawl as a context-budget cost, solved by tool search. [[wiki/sources/youtube-b5O6gb_Zuk8]]

## Relationships

- **agent-skill**: skill gives the workflow, MCP gives access. [[wiki/concepts/agent-skill]]
- **agent-harness**: harnesses (Droid, Warp agents, Claude Code) configure and scope which MCP servers an agent reaches. [[wiki/concepts/agent-harness]], [[wiki/sources/youtube-b5O6gb_Zuk8]]

> Synthesis: Every vendor ships MCP as the agent-facing door to its factory, but each vendor sets access control differently. Each docs set is one voice, so agreement here shows a common pattern, not independent proof. The podcast is the only non-vendor source and touches MCP only in passing, as a context-cost item.
