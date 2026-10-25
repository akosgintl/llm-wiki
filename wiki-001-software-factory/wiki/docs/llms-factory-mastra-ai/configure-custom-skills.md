---
type: source
title: Mastra Factory custom skills
description: "Mastra Factory docs explain how to add a custom SKILL.md under src/mastra/public/factory-skills/ so Factory loads it alongside its built-in skills."
origin: llms-txt
original_path: https://factory.mastra.ai/configure/custom-skills.md
source_url: https://factory.mastra.ai/configure/custom-skills.md
authors: []
published_date: null
raw_file: raw/docs/llms-factory-mastra-ai/configure-custom-skills.md
created: 2026-10-25T18:20:00Z
timestamp: 2026-10-25T18:20:00Z
entities: []
concepts:
  - "[[wiki/concepts/agent-skill]]"
---

# Mastra Factory custom skills

> [[raw/docs/llms-factory-mastra-ai/configure-custom-skills|Raw]] · llms-txt

## Summary

A short configuration page from the Mastra Factory docs. Custom skills give Factory extra instructions for specific tasks, and Factory loads them next to its built-in skills. [[raw/docs/llms-factory-mastra-ai/configure-custom-skills#Custom skills|cite]]

The recipe is file-based. The user creates a directory per skill and a `SKILL.md` with `name` and `description` frontmatter. The page's example is a `security-review` skill that checks changes for authentication, authorization, secret handling and injection risks. [[raw/docs/llms-factory-mastra-ai/configure-custom-skills#Create a custom skill|cite]]

Vendor documentation: this is the vendor's own account of the feature.

## Key claims

- `npm create factory` does not create the custom skills directory; the user adds it. [[raw/docs/llms-factory-mastra-ai/configure-custom-skills#Create a custom skill|cite]]
- Skill path is `src/mastra/public/factory-skills/<skill-name>/SKILL.md`. [[raw/docs/llms-factory-mastra-ai/configure-custom-skills#Create a custom skill|cite]]
- The directory name must match the `name` in the `SKILL.md` frontmatter. [[raw/docs/llms-factory-mastra-ai/configure-custom-skills#Create a custom skill|cite]]
- The Factory Server must be restarted after adding a skill before it loads. [[raw/docs/llms-factory-mastra-ai/configure-custom-skills#Create a custom skill|cite]]
- Custom skills are currently not managed or listed in the Factory UI. [[raw/docs/llms-factory-mastra-ai/configure-custom-skills#Create a custom skill|cite]]

## Notable quotes

> "Custom skills currently aren't managed or listed in the Factory UI."
> — [[raw/docs/llms-factory-mastra-ai/configure-custom-skills#Create a custom skill|location]]

## Connections

- **Entities**: none
- **Concepts**: [[wiki/concepts/agent-skill]]

> Synthesis: Mastra Factory uses the same SKILL.md-with-frontmatter convention as other agent harnesses, with skills living in the project's source tree; a concrete datapoint for the agent-skill concept.
