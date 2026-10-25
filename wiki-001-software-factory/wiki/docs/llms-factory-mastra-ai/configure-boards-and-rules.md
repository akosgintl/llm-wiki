---
type: source
title: Boards and rules
description: "Mastra Factory docs show how to turn a team process into code: boards define work-item phases, and onEnter, tool-result and transition-policy rules decide when agents run and when people must approve."
origin: llms-txt
original_path: https://factory.mastra.ai/configure/boards-and-rules.md
source_url: https://factory.mastra.ai/configure/boards-and-rules.md
authors: []
published_date: null
raw_file: raw/docs/llms-factory-mastra-ai/configure-boards-and-rules.md
created: 2026-10-25T18:30:00Z
timestamp: 2026-10-25T18:30:00Z
entities:
  - "[[wiki/entities/mastra-factory]]"
  - "[[wiki/entities/github]]"
  - "[[wiki/entities/linear]]"
concepts:
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/agent-skill]]"
---

# Boards and rules

> [[raw/docs/llms-factory-mastra-ai/configure-boards-and-rules|Raw]] · llms-txt

## Summary

The page explains how Mastra Factory encodes a team's process. A board defines the phases of a work item (for example Queued, Checking, Done). Rules decide what happens at each step: entering a phase can start an agent, and moving to Done can require a person's approval. [[raw/docs/llms-factory-mastra-ai/configure-boards-and-rules#Boards and rules|cite]] Factory ships Work and Review boards; custom boards, such as a quality check or release review, are added in TypeScript.

The worked example defines a `quality` board with `defineBoard()` and registers it through the `boards` array of the `MastraFactory` constructor in `src/mastra/index.ts`. Each phase has a `kind` (`resting`, `working`, `terminal`); a working phase needs a `role`. `outcomes` list the allowed moves but do not move cards automatically. [[raw/docs/llms-factory-mastra-ai/configure-boards-and-rules#Define and install a board|cite]] Custom boards reuse the existing Factory UI.

Behaviour is attached by handlers. An `onEnter` handler can return an `invokeSkill` action with a role and prompt; the example runs a repository review, then waits for a person to choose pass or retry. Tool rules under `tools.<toolName>.onResult` react to agent tool results, e.g. a `notify` warning when `execute_command` errors during Checking. GitHub and Linear event rules live on those integrations, not the board.

```mermaid
flowchart LR
  Q[queued: resting] -->|start| C[checking: working, role quality-checker]
  C -->|pass| D[done: terminal]
  C -->|retry| Q
  C -. onEnter manual .-> S[invokeSkill prompt]
  C -. tools.execute_command.onResult .-> N[notify warning]
```

## Key claims

- Customization points: `defineBoard()` plus the `boards` array for phases and moves; `onEnter`/`onExit` for actions; `transitionPolicy` for approvals; integration event rules; `tools.<toolName>.onResult`. [[raw/docs/llms-factory-mastra-ai/configure-boards-and-rules#Choose what to customize|cite]]
- A working phase requires a `role`; `outcomes` define allowed moves without auto-moving cards. [[raw/docs/llms-factory-mastra-ai/configure-boards-and-rules#Define and install a board|cite]]
- The `onEnter` `manual` handler returns `invokeSkill` with an `idempotencyKey`; it needs a configured model provider and repository sandbox. [[raw/docs/llms-factory-mastra-ai/configure-boards-and-rules#Run actions on phase changes|cite]]
- A prompt alone does not enforce human approval; a transition policy does. [[raw/docs/llms-factory-mastra-ai/configure-boards-and-rules#Run actions on phase changes|cite]]
- A tool rule leaves the card in its phase. A nonzero exit code is not necessarily a tool error, so the returned value must also be inspected. [[raw/docs/llms-factory-mastra-ai/configure-boards-and-rules#Configure tool rules|cite]]
- Tool rules on a custom board do not change the built-in Work board's `submit_plan` handler, which checks for an approved plan before requesting a move to Building. [[raw/docs/llms-factory-mastra-ai/configure-boards-and-rules#Configure tool rules|cite]]
- Overriding an integration event handler means keeping any default behaviour still needed. [[raw/docs/llms-factory-mastra-ai/configure-boards-and-rules#Configure rules for integration events|cite]]

## Notable quotes

> "Boards and rules turn your team's process into actions that Factory can run."
> — [[raw/docs/llms-factory-mastra-ai/configure-boards-and-rules#Boards and rules|Boards and rules]]

> "Custom boards use the existing board UI. You don't need to build another interface."
> — [[raw/docs/llms-factory-mastra-ai/configure-boards-and-rules#Define and install a board|Define and install a board]]

## Connections

- **Entities**: [[wiki/entities/mastra-factory]], [[wiki/entities/github]], [[wiki/entities/linear]]
- **Concepts**: [[wiki/concepts/factory-as-code]], [[wiki/concepts/human-in-the-loop]], [[wiki/concepts/agent-skill]]

> Synthesis: Vendor reference, not argument; it shows Mastra's code-first take on factory-as-code, with workflow phases and approval gates in TypeScript where Warp uses YAML and Markdown files.
