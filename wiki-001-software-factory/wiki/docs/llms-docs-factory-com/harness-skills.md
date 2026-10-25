---
type: source
title: "Skills"
description: "Factory's Droid agent packages reusable workflows as SKILL.md directories, loaded by progressive disclosure from many scopes with a fixed override precedence."
origin: llms-txt
original_path: https://docs.factory.com/harness/skills.md
source_url: https://docs.factory.com/harness/skills.md
authors: []
published_date: null
raw_file: raw/docs/llms-docs-factory-com/harness-skills.md
created: 2026-10-25T19:00:00Z
timestamp: 2026-10-25T19:00:00Z
entities: []
concepts:
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/context-engineering]]"
---

# Skills

> [[raw/docs/llms-docs-factory-com/harness-skills|Raw]] · llms-txt · Factory docs, Harness

## Summary

This page documents the skill mechanism of Droid, Factory's coding agent. A skill is a directory with a `SKILL.md` entry point, optional supporting files (checklists, schemas, scripts), and frontmatter telling Droid when the workflow applies. Skills fill the gap between always-on `AGENTS.md` and one-off prompts: instructions too specific for the former, too structured for the latter, and worth reusing. [[raw/docs/llms-docs-factory-com/harness-skills#Skills|cite]]

Loading uses progressive disclosure. Droid reads only each skill's `name` and `description`, matches the user request against them, and loads the full body only when a skill applies. The description is therefore the routing surface. Skills can be created by hand under `.factory/skills/` or via `/create-skill`, which forks the session into Spec mode and writes files only after approval.

The page also covers operations: nine scopes (project, folder-specific, personal, compatibility, mission, automation, plugin, built-in), a precedence order, a `/skills` manager with Enabled/Disabled/Overridden/Invalid states, and invocation controls. Skills double as slash commands (`/summarize-diff`).

```mermaid
flowchart LR
  A[Discovery: name + description] --> B[Selection vs user request]
  B --> C[Invocation: load full SKILL.md]
```

## Key claims

- Only `SKILL.md` is required; supporting files are not auto-loaded and must be mentioned from `SKILL.md`. [[raw/docs/llms-docs-factory-com/harness-skills#Skill anatomy|cite]]
- Skills load in three stages: discovery, selection, invocation. [[raw/docs/llms-docs-factory-com/harness-skills#Discovery and loading|cite]]
- Same-name skills resolve by precedence: folder/project, project plugin, personal, user plugin, built-in. Organization plugin skills beat all; mission skills beat project skills; automation skills override everything. [[raw/docs/llms-docs-factory-com/harness-skills#Resolution precedence|cite]]
- `disable-model-invocation: true` makes a skill user-only (for side-effect workflows such as deploy); `user-invocable: false` makes it model-only background guidance. [[raw/docs/llms-docs-factory-com/harness-skills#Control who invokes a skill|cite]]
- `allowed-tools` is review metadata, not a sandbox; enforcement needs a custom droid with a tool policy. [[raw/docs/llms-docs-factory-com/harness-skills#Declare intended tools|cite]]
- Skills are read from compatibility paths `.agents/skills/` and `.agent/skills/`, and the manager has an "Import from Claude" tab. [[raw/docs/llms-docs-factory-com/harness-skills#Where skills live|cite]]

## Notable quotes

> "The `description` is the routing surface. Write it for model matching: name the action, trigger, and boundary in one or two sentences."
> — [[raw/docs/llms-docs-factory-com/harness-skills#Discovery and loading|Discovery and loading]]

> "Do not rely on `allowed-tools` as a security boundary for skills."
> — [[raw/docs/llms-docs-factory-com/harness-skills#Declare intended tools|Declare intended tools]]

## Connections

- **Entities**: none linked.
- **Concepts**: [[wiki/concepts/agent-skill]], [[wiki/concepts/agent-harness]], [[wiki/concepts/context-engineering]]

> Synthesis: Factory's skills follow the same SKILL.md plus progressive-disclosure pattern as other agent-skill implementations (including this repo's own), with an unusually detailed scope and precedence model.
