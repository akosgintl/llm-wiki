---
type: source
title: "Agents, Subagents, Skills and Commands"
description: "A one-hour podcast whiteboard of how slash commands, subagents and skills evolved in Claude Code, arguing that instruction modules and context isolation are separate jobs."
origin: youtube
original_path: https://www.youtube.com/watch?v=b5O6gb_Zuk8
source_url: https://www.youtube.com/watch?v=b5O6gb_Zuk8
authors:
  - "Boundary"
published_date: "2026-03-16"
raw_file: raw/youtube-b5O6gb_Zuk8.md
created: 2026-10-26T07:13:23Z
timestamp: 2026-10-26T07:13:23Z
entities:
  - "[[wiki/entities/claude-code]]"
concepts:
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/context-engineering]]"
  - "[[wiki/concepts/multi-repo-development]]"
  - "[[wiki/concepts/git-worktree]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/mcp]]"
---

# Agents, Subagents, Skills and Commands

> [[raw/youtube-b5O6gb_Zuk8|Raw]] · youtube · Boundary · 2026-03-16 · 1:00:05 · auto captions

## Summary

Episode of the "AI that works" podcast (hosts Dex of Human Layer and Vaibhav of Boundary). Dex whiteboards the history of Claude Code's extension points to answer a question he says he gets constantly: what is the difference between commands, skills, subagents and agents. The thread is that each feature was a patch for the previous one's flaw. Slash commands were user-invoked prompt wrappers; subagents added a fresh context window; custom subagents were then misused to bundle instructions; a slash-command tool and finally skills let instructions load into any context. [[raw/youtube-b5O6gb_Zuk8#5:26|cite]]

The central recommendation is to treat two concerns as orthogonal. Subagents are for context isolation: a task burns 30-50k tokens of searching and returns a roughly 500-token answer. Skills are for instruction modules: reusable steering loaded as a user message, usable in the parent or in a subagent. Do not put custom instructions in agents. The talk also covers cost (every subagent and skill description is advertised in every context window, eating the instruction budget), how to share config across many repos, and a sceptical take on agent teams and "lights-off" factories. [[raw/youtube-b5O6gb_Zuk8#31:36|cite]]

The last third is opinion: bottleneck is human design review, not code volume; code review can be done with your own Claude Code step; and prompt/context engineering is a one-time purchase that is hard to protect as a business. [[raw/youtube-b5O6gb_Zuk8#46:56|cite]]

## Key claims

- Subagents give context isolation: intermediate tool calls vanish and only the final summary returns. Quality depends on the parent's prompt, which can be incomplete or hallucinated, so Dex still forks a session instead. [[raw/youtube-b5O6gb_Zuk8#8:31|cite]] [[raw/youtube-b5O6gb_Zuk8#12:46|cite]]
- "Playing house" subagents (back-end engineer, growth marketer) do not work; they only existed because custom subagents were the one way to bundle instructions. [[raw/youtube-b5O6gb_Zuk8#14:48|cite]]
- Skills load instructions as a user message, which gets better instruction-following than a file read or tool result. Skills can bundle files (a `references/` folder) for progressive disclosure. [[raw/youtube-b5O6gb_Zuk8#23:48|cite]] [[raw/youtube-b5O6gb_Zuk8#24:50|cite]]
- Every subagent, skill and MCP tool description is advertised each session and spends the instruction budget; Claude Code now switches to a tool-search step past roughly 10K of tool text. `disable-model-invocation: true` hides a skill from the model so only the slash form works. [[raw/youtube-b5O6gb_Zuk8#27:53|cite]] [[raw/youtube-b5O6gb_Zuk8#30:34|cite]] [[raw/youtube-b5O6gb_Zuk8#43:53|cite]]
- For many repos: a mono repo is simplest; failing that, a coordination repo whose `settings.json` lists additional directories and whose CLAUDE.md describes each repo, with per-task worktrees. Git submodules and symlinks are called unergonomic for models. [[raw/youtube-b5O6gb_Zuk8#39:57|cite]] [[raw/youtube-b5O6gb_Zuk8#40:57|cite]] [[raw/youtube-b5O6gb_Zuk8#41:58|cite]]
- Fewer, prescriptive team workflows beat many personal skills: "lift the median". [[raw/youtube-b5O6gb_Zuk8#34:37|cite]]
- Not bullish on agent teams: the bottleneck is humans reviewing design, not output volume. Leaning into a lights-off software factory risks 3 AM outages nobody can debug. [[raw/youtube-b5O6gb_Zuk8#45:55|cite]] [[raw/youtube-b5O6gb_Zuk8#48:57|cite]]

## Notable quotes

> "Separate out instruction modules from context isolation. Like these are two orthogonal concepts. And so like don't put your custom instructions in agents."
> — [[raw/youtube-b5O6gb_Zuk8#31:36|31:36]]

> "A lot of companies are going to die because they like lean too hard into the like lights off right only software factory and something's going to break at 3:00 a.m. and no one's going to have read the code in 3 months"
> — [[raw/youtube-b5O6gb_Zuk8#48:57|48:57]]

## Connections

- **Entities**: [[wiki/entities/claude-code]]
- **Concepts**: [[wiki/concepts/agent-skill]], [[wiki/concepts/agent-harness]], [[wiki/concepts/context-engineering]], [[wiki/concepts/multi-repo-development]], [[wiki/concepts/git-worktree]], [[wiki/concepts/human-in-the-loop]], [[wiki/concepts/software-factory]], [[wiki/concepts/mcp]]

> Synthesis: Same channel (Boundary) as the other podcast source in the wiki; this is the harness-mechanics episode and the human-review, anti-"lights-off" stance is a direct counterweight to software-factory framings.
