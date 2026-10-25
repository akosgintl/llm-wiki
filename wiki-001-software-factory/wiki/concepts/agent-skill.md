---
type: concept
title: Agent skill
description: "A version-controlled SKILL.md folder that gives an agent a repeatable procedure, loaded on demand, without changing its base prompt."
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
related:
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/agent-evals]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/software-factory]]"
created: 2026-10-25T00:00:00Z
timestamp: 2026-10-25T00:00:00Z
source_count: 10
---

# Agent skill

> A folder anchored by `SKILL.md` that teaches an agent one repeatable procedure.

## Definition

Warp's docs say a skill gives an agent a repeatable procedure, such as a security review or incident runbook, and extends its instructions without changing its prompt. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]] The common-skills repo shows the concrete format: one directory per skill, a `SKILL.md` with YAML frontmatter (`name`, `description`), and optional `references/`, `scripts/`, `assets/` so the main body stays short. The `description` is the trigger text a harness matches against the request. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]

Framings differ slightly by layer. In the docs a skill is a unit of factory configuration, scoped to all agents or one. In common-skills it is a distributable package pinned by lockfile. In the examples repo it is shared knowledge beside agents and automations. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

Corroboration caveat: all ten sources are Warp's own voice (docs set plus two Warp repos). Agreement between them is one vendor's account, not independent confirmation.

## Key claims

- Skills are scoped by path: `skills/<name>/SKILL.md` applies to every agent in a factory; `agents/<agent>/skills/<name>/SKILL.md` applies to one. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Skills carry instructions, not access. Credentials and MCP connections are configured separately. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]
- Skill sources in a factory: role and integration skills (GitHub for default agents, Slack for the foreman, Linear or Jira if chosen), Warp bundled skills (`oz-platform`, `factory-files`, `factory-mcp`), and team custom skills that extend rather than replace them. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]
- Custom agents have no built-in skills; a custom skill is how one is taught its job. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]]
- Skills are definition files, so changes follow the factory's PR review and config checks. [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/docs/llms-docs-warp-dev/factories]]
- Self-improvement loop: a Scorer flagging a recurring failure can lead to a follow-up run that updates the responsible skill, delivered as a PR for human review. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]], [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]]
- API: `skill_spec` (`owner/repo:skill-name`) uses a skill as an agent run's base prompt. Conversation data reports loads as `read_skill` actions, so team skill use can be measured. 14 bundled skill IDs are documented, though the catalog is not an availability manifest. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]
- Distribution: common-skills ships 27 skills, installs them via the `skills` npm CLI, pins them in a consumer `skills-lock.json` (directory hashes verified), and a GitHub Actions workflow opens auto-merging lockfile PRs downstream on each merge to `main`. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- `.agents/skills/` is the cross-harness location; Claude Code reaches it via symlink. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- Skills can encode orchestration (`saga`, `council`), headless CI contracts (`review-pr` writes `review.json`, never posts), and factory migration (`migrate-to-factory` ports skills into a factory repo, treating source content as untrusted). [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- Skills are themselves evaluated: `skill-doctor` scores local transcripts on four rubrics and drafts SKILL.md edits. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]

## Relationships

- **Factory as code**: skills are one file type in the factory definition tree. [[wiki/concepts/factory-as-code]]
- **Agent harness**: harnesses (Warp, Claude Code, Codex) load skills from the shared directory. [[wiki/concepts/agent-harness]]
- **Agent evals**: Scorers drive skill edits; `skill-doctor` scores skills directly. [[wiki/concepts/agent-evals]]
- **MCP**: a separate access layer that skills assume but do not provide. [[wiki/concepts/mcp]]

> Synthesis: skills are treated as packages (path-scoped, PR-reviewed, lockfile-pinned, eval-driven), but every source is Warp, so this wiki cannot yet say how other vendors define them.
