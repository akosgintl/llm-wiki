---
type: source
title: Skills
description: "8090 Software Factory skills are versioned, team-shared instruction sets that the project agent loads on demand, can be forced by Skill Rules before writes, and can be shared across an organization through a Library."
origin: llms-txt
original_path: https://docs.8090.ai/modules/skills
source_url: https://docs.8090.ai/modules/skills
authors: []
published_date: null
raw_file: raw/docs/llms-docs-8090-ai/modules-skills.md
created: 2026-10-25T18:40:00Z
timestamp: 2026-10-25T18:40:00Z
entities:
  - "[[wiki/entities/8090-software-factory]]"
concepts:
  - "[[wiki/concepts/agent-skill]]"
---

# Skills

> [[raw/docs/llms-docs-8090-ai/modules-skills|Raw]] · llms-txt

## Summary

In 8090 Software Factory a skill is a saved set of instructions (title, description, body, category) that the project agent loads when a user picks it or when the task matches its description. Skills live in the project, so the whole team shares them. The advice is to save guidance once instead of repeating it in every chat. [[raw/docs/llms-docs-8090-ai/modules-skills#Skills|cite]] The description acts as a trigger and should start with "Use when...". The body holds the full guidance. [[raw/docs/llms-docs-8090-ai/modules-skills#the-description-and-the-body|cite]]

Skills are used as a governance layer for the factory's documents. Built-in writing-rules skills (Blueprints, Requirements, Work Orders) set the project's writing standard, each paired with a Skill Rule that makes the agent read the current skill before creating or editing that document type. [[raw/docs/llms-docs-8090-ai/modules-skills#writing-rules-skills|cite]] Skills can nest (template families, per-user overrides), are versioned with agent-versus-person attribution, can be commented on, and are shared across projects through an organization Skills Library with publish, copy and update-from-source flows.

Coding agents connected over MCP can list, read, create, edit and delete skills, but edits arrive as suggested changes to accept. The page also separates these in-project skills from the 8090 agent skill that is installed into a coding agent such as Cursor or Claude Code. [[raw/docs/llms-docs-8090-ai/modules-skills#not-the-same-as-the-coding-agent-plugin|cite]]

## Key claims

- Skills are categorised (General, Knowledge Base, Requirements, Blueprints, Work Orders, Feedback). Any skill is usable anywhere; category only decides where it is suggested. [[raw/docs/llms-docs-8090-ai/modules-skills#categories|cite]]
- Invocation paths: skills above the message box, "/" in the message box, "/" in automations (current content loaded on every run), and automatic matching on description. [[raw/docs/llms-docs-8090-ai/modules-skills#invoking-a-skill|cite]]
- A Skill Rule blocks creating or editing a given item type (requirements, blueprints, work orders, resources, themes) until the agent has read the current skill version in the conversation. Rules bind the in-product agent, not coding agents over MCP. [[raw/docs/llms-docs-8090-ai/modules-skills#skill-rules|cite]]
- Each project gets its own copy of built-in skills. A release that changes a built-in does not overwrite the copy; a notice offers update, or "Reconcile with Agent" to merge as suggested edits if the copy was edited. [[raw/docs/llms-docs-8090-ai/modules-skills#skills-library|cite]]
- Per-user overrides let a parent skill route one teammate to personal child skills instead of the project writing rules, keeping a single shared standard. [[raw/docs/llms-docs-8090-ai/modules-skills#nested-skills-and-per-user-overrides|cite]]
- Skills are versioned like blueprints and requirements, and history shows whether the agent or a person made each change. Export is Markdown. [[raw/docs/llms-docs-8090-ai/modules-skills#versions-and-comments|cite]]

## Notable quotes

> "Write it as a trigger, not a summary."
> — [[raw/docs/llms-docs-8090-ai/modules-skills#the-description-and-the-body|The description and the body]]

> "Per-user overrides let a project keep a single shared standard while letting individuals opt into their own format, without forking the project rules."
> — [[raw/docs/llms-docs-8090-ai/modules-skills#nested-skills-and-per-user-overrides|Nested skills and per-user overrides]]

## Connections

- **Entities**: [[wiki/entities/8090-software-factory]]
- **Concepts**: [[wiki/concepts/agent-skill]]

> Synthesis: Vendor reference; here skills are a product-managed, enforceable standards store (rules gate writes, org-wide library), going beyond the file-based agent skill pattern seen elsewhere in the wiki.
