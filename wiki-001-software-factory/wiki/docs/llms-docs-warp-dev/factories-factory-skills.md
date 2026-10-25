---
type: source
title: "Factory skills"
description: "Warp docs page stating that factory skills are version-controlled SKILL.md procedures, shared across all agents or scoped to one, living in the factory definition."
origin: llms-txt
original_path: https://docs.warp.dev/factories/factory-skills/
source_url: https://docs.warp.dev/factories/factory-skills/
authors: []
published_date: null
raw_file: raw/docs/llms-docs-warp-dev/factories-factory-skills.md
created: 2026-10-25T15:03:17Z
timestamp: 2026-10-25T15:03:17Z
entities:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/github]]"
concepts:
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/secrets-management]]"
  - "[[wiki/concepts/agent-evals]]"
---

# Factory skills

> [[raw/docs/llms-docs-warp-dev/factories-factory-skills|Raw]] · llms-txt

## Summary

This is vendor documentation for Warp Factories. The docs state that a skill gives an agent a repeatable procedure, such as a security review or incident runbook, and extends the agent's instructions without changing its prompt. [[raw/docs/llms-docs-warp-dev/factories-factory-skills#Factory skills|cite]]

The page separates three skill sources: role and integration skills (GitHub for default agents, Slack for the foreman, Linear or Jira when chosen at setup), Warp-provided bundled skills (`oz-platform`, `factory-files`, `factory-mcp`), and team-owned custom skills. Custom skills extend the built-in ones rather than replacing them. [[raw/docs/llms-docs-warp-dev/factories-factory-skills#Skill sources in a factory|cite]]

Custom skills are files in the factory definition, so they follow the same change flow as the rest of the definition: Warp-managed definitions are validated and committed on save; GitHub-backed ones go through a pull request, PR checks, and merge to the production branch. [[raw/docs/llms-docs-warp-dev/factories-factory-skills#Add or edit a skill|cite]]

## Key claims

- The docs state skills are scoped by path: `skills/<skill-name>/SKILL.md` applies to every agent; `agents/<agent-name>/skills/<skill-name>/SKILL.md` applies to one agent. [[raw/docs/llms-docs-warp-dev/factories-factory-skills#Add or edit a skill|cite]]
- Custom agents have no built-in skills, so a custom skill is how one is taught its job. [[raw/docs/llms-docs-warp-dev/factories-factory-skills#When to add a custom skill|cite]]
- Skills carry instructions only, not access. Credentials and MCP connections must be configured separately in the agent's secrets and MCP server settings. [[raw/docs/llms-docs-warp-dev/factories-factory-skills#When to add a custom skill|cite]]
- Editing a skill requires permission to edit the factory definition. [[raw/docs/llms-docs-warp-dev/factories-factory-skills#Add or edit a skill|cite]]
- When a Scorer with Self-improvement enabled flags a recurring failure, the factory can update the responsible skill in a follow-up run, delivered as a pull request for human review. [[raw/docs/llms-docs-warp-dev/factories-factory-skills#Skills and self-improvement|cite]]
- Typical custom skills named: required tests or lint, incident-response or triage runbooks, security or compliance review checklists. [[raw/docs/llms-docs-warp-dev/factories-factory-skills#When to add a custom skill|cite]]

## Notable quotes

> "Skills provide instructions, not access to tools or repositories."
> — [[raw/docs/llms-docs-warp-dev/factories-factory-skills#When to add a custom skill|When to add a custom skill]]

## Connections

- **Entities**: [[wiki/entities/warp-factories]], [[wiki/entities/github]]
- **Concepts**: [[wiki/concepts/agent-skill]], [[wiki/concepts/factory-as-code]], [[wiki/concepts/mcp]], [[wiki/concepts/secrets-management]], [[wiki/concepts/agent-evals]]

> Synthesis: Vendor description of skills as the version-controlled, PR-reviewed layer of a factory definition, closing the loop with scorer-driven self-improvement; claims are the vendor's own and unverified.
