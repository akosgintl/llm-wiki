---
type: entity
title: Claude Code
description: "Anthropic's coding agent, used across the wiki as a harness that factories run per role, an MCP client, a consumer of .agents/skills, and a headless runner behind Port workflows."
aliases: []
sources:
  - "[[wiki/docs/llms-docs-8090-ai/connections-connect-coding-agent]]"
  - "[[wiki/docs/llms-docs-8090-ai/general-quickstart]]"
  - "[[wiki/docs/llms-docs-factory-com/harness-subagents]]"
  - "[[wiki/docs/llms-docs-port-io/agent-management-overview]]"
  - "[[wiki/docs/llms-docs-port-io/guides-all-trigger-ai-coding-assistants-from-port]]"
  - "[[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/sources/youtube-b5O6gb_Zuk8]]"
  - "[[wiki/sources/youtube-tGbjIvvYuHE]]"
related:
  - "[[wiki/entities/codex]]"
  - "[[wiki/entities/github]]"
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/context-engineering]]"
  - "[[wiki/concepts/git-worktree]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/multi-repo-development]]"
created: 2026-10-25T15:14:44Z
timestamp: 2026-10-26T07:15:23Z
source_count: 14
---

# Claude Code

> Anthropic's coding agent; here it appears as a pluggable harness in a software factory, an MCP client, a skills consumer, and a runner that control planes dispatch work to.

## Definition

Sources treat Claude Code as the agent runtime that does the coding, not as the factory itself. In Warp's docs it is one of three supported harnesses (Warp Agent, Claude Code, Codex) chosen per factory agent. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]] In the Boundary podcast it is the harness, run headless, inside Boundary's in-house factory. [[wiki/sources/youtube-tGbjIvvYuHE]] In 8090 and Port docs it is an external worker that a control surface drives over MCP or GitHub Actions. [[wiki/docs/llms-docs-8090-ai/connections-connect-coding-agent]] [[wiki/docs/llms-docs-port-io/guides-all-trigger-ai-coding-assistants-from-port]]

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
- 8090 Software Factory exposes an OAuth MCP server; Claude Code connects with `claude mcp add --transport http --scope user ...` then `/mcp` > Authenticate. It lists Work Orders, reads linked Requirements and Blueprints, marks them In Progress and In Review, and links PRs. [[wiki/docs/llms-docs-8090-ai/connections-connect-coding-agent]] [[wiki/docs/llms-docs-8090-ai/general-quickstart]]
- 8090 gates destructive actions (deleting work orders, requirements, skills, any automation change) on user confirmation; an agent that cannot show confirmations cannot do them. This applies to Claude Code like any MCP client. [[wiki/docs/llms-docs-8090-ai/connections-connect-coding-agent]]
- Factory's Droid can import Claude Code agents from `.claude/agents/` and `~/.claude/agents/`, mapping name, prompt, model family and tools. Its custom droids are described as an analogue of Claude Code subagents. [[wiki/docs/llms-docs-factory-com/harness-subagents]]
- Port's guide runs Claude Code through `anthropics/claude-code-base-action@beta` in a GitHub Actions backend workflow, with a restricted tool list (`Bash,Edit,Write,GlobTool,GrepTool,BatchTool`) and a prompt forbidding changes to main except via a PR on a new branch. Auth uses `ANTHROPIC_API_KEY`. [[wiki/docs/llms-docs-port-io/guides-all-trigger-ai-coding-assistants-from-port]]
- Port records Claude runs as `claudeCodeExecution` catalog entities with prompt, status, time, tokens and USD cost. It is the only one of three assistants in that guide (Copilot, Claude Code, Gemini CLI) with token and cost tracking. [[wiki/docs/llms-docs-port-io/guides-all-trigger-ai-coding-assistants-from-port]]
- Port names Claude Code as the example "code-first" agent, as a consumer of the Port MCP server, and as a target for Jira ticket delegation in autonomous ticket resolution. Port measures skill adoption in Cursor and Claude. [[wiki/docs/llms-docs-port-io/agent-management-overview]] [[wiki/docs/llms-docs-port-io/solutions-autonomous-ticket-resolution-overview]]
- Boundary's "Agents, Subagents, Skills and Commands" episode traces Claude Code's extension points as successive patches: slash commands (user-invoked prompt wrappers), subagents (fresh context window), custom subagents (misused to bundle instructions), then skills (instructions loadable into any context). [[wiki/sources/youtube-b5O6gb_Zuk8]]
- Same episode: subagents are for context isolation (30-50k tokens of searching returned as a ~500-token answer) and skills are for instruction modules; the two are orthogonal, so custom instructions do not belong in agents. Skills load as a user message and can bundle a `references/` folder. [[wiki/sources/youtube-b5O6gb_Zuk8]]
- Every subagent, skill and MCP tool description is advertised each session and spends the instruction budget. Claude Code now switches to a tool-search step past roughly 10K of tool text, and `disable-model-invocation: true` hides a skill from the model. [[wiki/sources/youtube-b5O6gb_Zuk8]]
- For many repos the speaker suggests a mono repo, or a coordination repo whose `settings.json` lists additional directories and whose CLAUDE.md describes each repo, with per-task worktrees. [[wiki/sources/youtube-b5O6gb_Zuk8]]

## Relationships

- **Codex**: peer harness, listed beside Claude Code in every origin. [[wiki/entities/codex]]
- **Warp Factories**: hosts Claude Code as a harness option. [[wiki/entities/warp-factories]]
- **Agent harness**: Claude Code is a concrete instance. [[wiki/concepts/agent-harness]]
- **Agent skill**: consumes `.agents/skills/` via symlink. [[wiki/concepts/agent-skill]]
- **MCP**: Claude Code consumes MCP servers such as Factory MCP, the 8090 server and the Port MCP server. [[wiki/concepts/mcp]]
- **GitHub**: runs under GitHub Actions in Port's recipe; PRs link back to 8090 Work Orders. [[wiki/entities/github]]
- **Human in the loop**: 8090 confirmation gates apply to its MCP actions; the Boundary episode argues human design review is the bottleneck. [[wiki/concepts/human-in-the-loop]] [[wiki/sources/youtube-b5O6gb_Zuk8]]
- **Context engineering**: subagent isolation and skill loading are its main levers in Claude Code. [[wiki/concepts/context-engineering]]
- **Multi-repo development**: coordination-repo pattern. [[wiki/concepts/multi-repo-development]]
- **Git worktree**: per-task worktrees. [[wiki/concepts/git-worktree]]

## Tensions

Warp's pages show Claude Code as a first-class, swappable harness. The podcast shows it embedded inside a self-built loop with no vendor control plane. The Boundary harness-mechanics episode is sceptical of "lights-off" factories and agent teams, while Warp and Port docs build automation around Claude Code runs. No source evaluates Claude Code's quality. Port adds a different framing: a code-first agent governed from outside by a catalog, not a harness swapped inside a factory.

> Synthesis: Corroboration is thin and partly false. The four Warp docs pages and the two Warp repos are one vendor voice (Warp), so six pages count as one origin. 8090, Factory, Port (three pages, one voice) and the Boundary podcast are each separate origins, giving five in all. The two Boundary episodes (tGbjIvvYuHE, b5O6gb_Zuk8) share a channel and hosts, so they are one voice, not two. Across them Claude Code is consistently a harness slot, MCP client or dispatch target: 8090 and Port both treat it as one of several interchangeable agents (Cursor, Codex, Copilot, Gemini CLI). Claims resting on a single origin: Warp auth options and `claude`/`claude-code` type, 8090 connection steps, Port's base-action recipe, Factory's import path.
