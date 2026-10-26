---
type: concept
title: Factory as code
description: A software factory declared as a versioned tree of YAML and Markdown files, rooted at factory.yaml, that the platform validates and applies as one unit.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-automations]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-benchmarks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-azure-devops]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-github]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-runners]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-secrets-aws-ecr]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-secrets]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-warp-hosting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks-vercel]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/docs/llms-docs-port-io/workflows-concepts]]"
  - "[[wiki/docs/llms-factory-mastra-ai/configure-boards-and-rules]]"
  - "[[wiki/docs/llms-factory-mastra-ai/configure-sandboxes]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/sources/youtube-XUEfIxkdT2Q]]"
related:
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/agent-runner]]"
  - "[[wiki/concepts/agent-evals]]"
  - "[[wiki/concepts/webhook]]"
  - "[[wiki/concepts/secrets-management]]"
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/dev-environment]]"
created: 2026-10-25T00:00:00Z
timestamp: 2026-10-26T07:12:45Z
source_count: 37
---

# Factory as code

> A factory is a versioned definition, not a console configuration. Warp: path is identity, Markdown body is prompt, YAML is topology.

## Definition

Warp's docs define a factory as "a versioned tree of YAML and Markdown files rooted at `factory.yaml`" covering agents, automations, runners, scorers, benchmarks, skills and webhooks. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]] [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]] A resource's identity is its path: `agents/reviewer/agent.md` is the agent `reviewer`. Runs, work items and metrics stay in the web app. The example repo is eight such trees synced from GitHub; its only code is validation scripts. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

Warp's CEO gives the same idea in a podcast as a loop "defined declaratively in code, Terraform-style", covering agents, skills, MCPs, where they run and which models they use, so it can be branched, tested and diffed. [[wiki/sources/youtube-XUEfIxkdT2Q]]

Other origins mean something different by "as code": Mastra uses TypeScript, Port uses JSON graphs (see Tensions).

## Key claims

- **Layout.** `factory.yaml` (repositories, integrations, `schemaVersion` `v1alpha1`, `agentDefaults`), then `agents/<name>/agent.md`, `automations/`, `runners/`, `scorers/`, `benchmarks/`, `webhooks/`, `skills/`. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- **Agents.** Frontmatter is config, body is prompt. One `FOREMAN` orchestrates; other roles are `TRIAGE`, `SPEC`, `IMPLEMENT`, `REVIEW`, `VERIFY`, `CUSTOM`. Harness or model, runner and secrets are per agent. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]]
- **Triggers.** An automation's `triggers` frontmatter (provider, event, `filter`) wakes an agent with the body as task; filters are AND-combined and fail closed. [[wiki/docs/llms-docs-warp-dev/factories-automations]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]
- **Skills** sit at `skills/<name>/SKILL.md` or under one agent; they carry instructions, not access. `common-skills` distributes them as a pinned library. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]], [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- **Versioning.** On a paid plan the definition lives in the team's GitHub repo; PRs run the `warp/factory-config` check and merging updates the factory; the web UI turns read-only. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/docs/llms-docs-warp-dev/factories-secrets]]
- **Apply and validate.** Applied as one unit; the last valid definition is kept on failure. Validation via save, PR check, script, JSON Schema or Factory MCP. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- **Deploy.** Same definition on Warp-hosted sandboxes or self-hosted workers; secrets referenced by name. [[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]], [[wiki/docs/llms-docs-warp-dev/factories-runners]], [[wiki/docs/llms-docs-warp-dev/factories-secrets]]
- **Self-modifying loop.** Scorers sample runs; with `selfImprovement`, failures become human-reviewed PRs against skills or the definition. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]], [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers]]
- **Why code (talk).** Zach (Warp) argues a factory only works if the loop is real and declarative; stored as code, improvement agents can spot patterns in failed runs and propose diffs to the definition's markdown files, and real tasks can become private benchmarks. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- **Runtime outside the file.** API/SDK and Factory MCP drive runs against the same factory. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]
- **Mastra.** `defineBoard()` plus the `boards` array in the `MastraFactory` constructor define phases; `onEnter`, tool-result rules and `transitionPolicy` attach behaviour. A prompt alone does not enforce approval; a transition policy does. [[wiki/docs/llms-factory-mastra-ai/configure-boards-and-rules]] The sandbox provider is a TypeScript callback in `src/mastra/sandbox.ts`; setup and teardown commands are set per repository. [[wiki/docs/llms-factory-mastra-ai/configure-sandboxes]]
- **Port.** A workflow is plain JSON (trigger, action, condition, input nodes), updatable through the API; `If-Match` with `workflowVersionIdentifier` guards concurrent edits (`412` on conflict). [[wiki/docs/llms-docs-port-io/workflows-concepts]]

## Tensions

Warp declares the factory in YAML and Markdown files in git. Mastra declares boards and sandboxes in TypeScript code. Port declares workflows as JSON via API, with optimistic locking rather than git review. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]] [[wiki/docs/llms-factory-mastra-ai/configure-boards-and-rules]] [[wiki/docs/llms-docs-port-io/workflows-concepts]] Only Warp's docs name the git-PR plus read-only-UI model.

## Relationships

- **Software factory**: one way to make the factory declarative and reviewable. [[wiki/concepts/software-factory]]
- **Agent evals**: scorers and benchmarks are definition files. [[wiki/concepts/agent-evals]]
- **Human in the loop**: foreman prompt, Mastra transition policies and Port input nodes encode approval gates. [[wiki/concepts/human-in-the-loop]]
- **Dev environment**: Mastra sandboxes are configured as code. [[wiki/concepts/dev-environment]]

> Synthesis: Warp's docs, its two repos and the Warp CEO podcast are one voice, so they corroborate syntax and intent, not efficacy; the talk is pitch, not independent evidence. Mastra and Port are independent origins, but each describes a different mechanism, so they show the idea is shared, not the format.
