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
  - "[[wiki/docs/llms-docs-8090-ai/modules-skills]]"
  - "[[wiki/docs/llms-docs-8090-ai/opinions-agent-skill]]"
  - "[[wiki/docs/llms-docs-8090-ai/general-introduction]]"
  - "[[wiki/docs/llms-docs-8090-ai/general-quickstart]]"
  - "[[wiki/docs/llms-docs-8090-ai/modules-knowledge-base]]"
  - "[[wiki/docs/llms-docs-8090-ai/modules-work-orders]]"
  - "[[wiki/docs/llms-docs-factory-com/harness-skills]]"
  - "[[wiki/docs/llms-docs-factory-com/harness-subagents]]"
  - "[[wiki/docs/llms-docs-factory-com/missions-overview]]"
  - "[[wiki/docs/llms-docs-factory-com/droid-exec-overview]]"
  - "[[wiki/docs/llms-docs-port-io/agent-management-skills-overview]]"
  - "[[wiki/docs/llms-docs-port-io/agent-management-overview]]"
  - "[[wiki/docs/llms-docs-port-io/glossary]]"
  - "[[wiki/docs/llms-docs-port-io/solutions-agentops-overview]]"
  - "[[wiki/docs/llms-factory-mastra-ai/configure-custom-skills]]"
  - "[[wiki/docs/llms-factory-mastra-ai/configure-boards-and-rules]]"
related:
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/agent-evals]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/knowledge-base]]"
  - "[[wiki/concepts/control-plane]]"
created: 2026-10-25T00:00:00Z
timestamp: 2026-10-25T18:31:43Z
source_count: 26
---

# Agent skill

> A named instruction package whose `description` is a trigger; the agent loads the full body only when a task matches.

## Definition

Warp's docs say a skill gives an agent a repeatable procedure, such as a security review or incident runbook, and extends its instructions without changing its prompt. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]] The common-skills repo shows the concrete format: one directory per skill, a `SKILL.md` with YAML frontmatter (`name`, `description`), and optional `references/`, `scripts/`, `assets/`. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]] Factory's Droid and Mastra Factory use the same convention. [[wiki/docs/llms-docs-factory-com/harness-skills]], [[wiki/docs/llms-factory-mastra-ai/configure-custom-skills]] 8090 defines it as a modular bundle of instructions, scripts and resources loaded at runtime. [[wiki/docs/llms-docs-8090-ai/opinions-agent-skill]]

Framings differ by layer. Warp: a unit of factory configuration. Factory: the middle ground between always-on `AGENTS.md` and one-off prompts. [[wiki/docs/llms-docs-factory-com/harness-skills]] 8090: a product-managed, team-shared standards store inside the platform, distinct from the installable coding-agent skill. [[wiki/docs/llms-docs-8090-ai/modules-skills]] Port: a catalog entity (not a file on disk) loaded through a `load_skill` MCP tool, claiming the open Agent Skills spec. [[wiki/docs/llms-docs-port-io/agent-management-skills-overview]]

Corroboration caveat: the 26 pages come from six origins (Warp docs, two Warp repos, 8090, Factory, Port, Mastra), all vendor voices. The Warp docs and both Warp repos are one vendor.

## Key claims

- Description is the routing surface. Factory: load name and description first, body only on match (progressive disclosure). 8090: "write it as a trigger, not a summary". Port: the description is the trigger. [[wiki/docs/llms-docs-factory-com/harness-skills]], [[wiki/docs/llms-docs-8090-ai/modules-skills]], [[wiki/docs/llms-docs-port-io/agent-management-skills-overview]]
- Warp scope by path: `skills/<name>/SKILL.md` for all agents, `agents/<agent>/skills/<name>/SKILL.md` for one. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Mastra path: `src/mastra/public/factory-skills/<name>/SKILL.md`; directory name must match `name`; server restart needed; not listed in the UI. [[wiki/docs/llms-factory-mastra-ai/configure-custom-skills]]
- Skills carry instructions, not access. Warp keeps credentials and MCP separate; 8090 says "the skill provides the workflow, while MCP provides access". [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]], [[wiki/docs/llms-docs-8090-ai/opinions-agent-skill]]
- Factory has a precedence order for same-name skills (organization plugin, mission, project, personal, built-in; automation overrides all). `allowed-tools` is review metadata, not a sandbox. A custom droid is the enforced boundary; a skill is an inline instruction set. [[wiki/docs/llms-docs-factory-com/harness-skills]], [[wiki/docs/llms-docs-factory-com/harness-subagents]]
- Governance: Warp skills are definition files under PR review. [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/docs/llms-docs-warp-dev/factories]] 8090 adds versioning with agent/person attribution, an org Skills Library, and Skill Rules that block writes until the current skill is read (in-product agent only, not MCP clients). [[wiki/docs/llms-docs-8090-ai/modules-skills]] Port syncs from GitHub and tracks adoption; AgentOps treats skill sprawl and forking as a problem. [[wiki/docs/llms-docs-port-io/agent-management-skills-overview]], [[wiki/docs/llms-docs-port-io/agent-management-overview]], [[wiki/docs/llms-docs-port-io/solutions-agentops-overview]]
- Skills drive workflows: 8090 built-ins (Extract Work Orders, Phase Planning, Knowledge Base upkeep) and an installable skill running read, plan, implement, verify with a per-work-order scratch folder; Factory Missions plan the skills each milestone needs; Mastra boards can `invokeSkill`. [[wiki/docs/llms-docs-8090-ai/modules-work-orders]], [[wiki/docs/llms-docs-8090-ai/modules-knowledge-base]], [[wiki/docs/llms-docs-8090-ai/opinions-agent-skill]], [[wiki/docs/llms-docs-factory-com/missions-overview]], [[wiki/docs/llms-factory-mastra-ai/configure-boards-and-rules]]
- Self-improvement: a Scorer flagging a recurring failure can lead to a PR updating the skill; `skill-doctor` scores skills directly. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]], [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- Warp API: `skill_spec` (`owner/repo:skill-name`) sets a skill as base prompt; loads show as `read_skill` actions. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]
- Distribution: common-skills ships 27 skills via the `skills` npm CLI with a hash-verified `skills-lock.json` and auto-merging lockfile PRs. 8090 installs with `npx skills add`. `.agents/skills/` is the cross-harness path; Factory also reads it. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]], [[wiki/docs/llms-docs-8090-ai/opinions-agent-skill]], [[wiki/docs/llms-docs-factory-com/harness-skills]]
- Size: keep Port skill instructions under about 5000 tokens, detail in references. [[wiki/docs/llms-docs-port-io/agent-management-skills-overview]]

## Tensions

- Storage: file-based in repos (Warp, Factory, Mastra) versus catalog entities (Port) or in-product records (8090). [[wiki/docs/llms-docs-factory-com/harness-skills]], [[wiki/docs/llms-docs-port-io/agent-management-skills-overview]], [[wiki/docs/llms-docs-8090-ai/modules-skills]]
- Enforcement: 8090 Skill Rules force a skill read before writes; Factory says skills are not a security boundary and enforcement needs a custom droid. [[wiki/docs/llms-docs-8090-ai/modules-skills]], [[wiki/docs/llms-docs-factory-com/harness-skills]]

## Relationships

- **Factory as code**: skills are one file type in the definition tree. [[wiki/concepts/factory-as-code]]
- **Agent harness**: Warp, Claude Code, Droid and others load skills. [[wiki/concepts/agent-harness]]
- **Agent evals**: Scorers drive skill edits. [[wiki/concepts/agent-evals]]
- **MCP**: the access layer skills assume; Port and 8090 also deliver skills over it. [[wiki/concepts/mcp]]
- **Control plane**: Port governs skills as inventory. [[wiki/concepts/control-plane]]

> Synthesis: the SKILL.md-plus-trigger-description pattern is shared across vendors, while storage, enforcement and governance differ; the six origins are all vendors with a product to sell.
