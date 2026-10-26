---
type: entity
title: Warp Factories
description: Warp's hosted product for running a team of cloud agents, coordinated by a foreman, that turns issues, tickets and chat messages into reviewed pull requests.
aliases: ["Warp Factory", "Factories"]
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-demo-sentry-monitoring-with-sdk]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-quickstart]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-automations]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-benchmarks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-developer-tools]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-api]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-inbox]]"
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
  - "[[wiki/docs/llms-docs-warp-dev/factories-quickstart]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-runners]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-secrets-aws-ecr]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-secrets]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-data-storage]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-external-orchestrators]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-docker]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-monitoring]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-private-container-registry]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-quickstart]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-reference]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-warp-hosting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks-vercel]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/sources/youtube-XUEfIxkdT2Q]]"
related:
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/foreman-agent]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/concepts/agent-evals]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/control-plane]]"
  - "[[wiki/entities/claude-code]]"
  - "[[wiki/entities/codex]]"
  - "[[wiki/entities/slack]]"
  - "[[wiki/concepts/human-in-the-loop]]"
created: 2026-10-25T00:00:00Z
timestamp: 2026-10-26T07:12:41Z
source_count: 54
---

# Warp Factories

> Warp's product for a software factory: cloud agents behind a foreman, fed by forges, trackers and chat, ending in a human-merged pull request.

## Definition

Warp's docs define a factory as a team of cloud agents connected to your repositories. A foreman agent coordinates stage agents through triage, spec, implement and review. Humans decide at spec approval, questions and merge. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]

In a podcast, Warp's founder-CEO frames the underlying idea as an agentic loop from issue through triage, optional spec, implementation, review, QA, CI/CD and monitoring. The loop lives in the cloud, is highly measurable, and is defined in code, so a developer's job becomes building and tuning it. [[wiki/sources/youtube-XUEfIxkdT2Q]]

Every source here is Warp's own voice: the docs set, the `warp-factory-examples` repo and a talk by Warp's CEO. Treat agreement across them as one vendor's account, not independent corroboration. Warp's other repo, `common-skills`, was not among the pages aggregated here.

## Key claims

**Agents and definition**
- Default team: foreman, triage, spec, implement, review. Custom agents are added in the web app or via `agent.md`; the foreman dispatches them with `run_agents`. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]]
- Each agent picks a harness: Warp Agent, Claude Code or Codex. Third-party harnesses need a paid plan. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]
- A factory is a versioned tree of YAML and Markdown rooted at `factory.yaml`. Eight copy-and-edit examples (v1alpha1) are validated against Warp's server parser. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

**Triggers and integrations**
- Work enters via chat, forges, trackers, webhooks, API, MCP or schedules; automations match events with filters and route to an agent. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]], [[wiki/docs/llms-docs-warp-dev/factories-automations]]
- Integrations: [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-azure-devops]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-linear]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-jira]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-slack]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-teams]]. Other forges work via a token stored as an Agent Secret. [[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]
- Custom webhooks accept JSON over HTTPS with three auth modes, filters and dedup. [[wiki/docs/llms-docs-warp-dev/factories-webhooks]], [[wiki/docs/llms-docs-warp-dev/factories-webhooks-vercel]]
- Operators use a dashboard and a personal Inbox for questions, spec approvals and PR reviews. [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]], [[wiki/docs/llms-docs-warp-dev/factories-factory-inbox]]

**Infra and self-hosting**
- A Warp control plane is split from an execution plane you can host; inference and four credential kinds are bounded separately. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]
- Warp-hosted sandboxes suit publicly reachable repos; private networks point to managed self-hosting. [[wiki/docs/llms-docs-warp-dev/factories-warp-hosting]], [[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]
- The `oz-agent-worker` daemon has Docker, Kubernetes, Direct and Command backends. Start at [[wiki/docs/llms-docs-warp-dev/factories-self-hosting]] and [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-quickstart]]; details in [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-docker]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-external-orchestrators]].
- Enterprise teams can send transcripts and artifacts to their own S3 or Azure Blob bucket. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-data-storage]]
- Runners are reusable compute profiles; secrets inject by name as environment variables. [[wiki/docs/llms-docs-warp-dev/factories-runners]], [[wiki/docs/llms-docs-warp-dev/factories-secrets]]

**API, SDK and MCP**
- An HTTP API plus Python and TypeScript SDKs start, monitor, steer and cancel runs. Factory endpoints dispatch to a foreman by UID. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]], [[wiki/docs/llms-docs-warp-dev/factories-factory-api]], [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-quickstart]]
- Errors follow RFC 7807 with 18 codes. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors]]
- Factory MCP is a hosted server; a connected client acts with its account's full permissions. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]

**Skills**
- Skills are version-controlled `SKILL.md` procedures, shared or scoped to one agent. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]

**Evals**
- Scorers (LLM judges), Benchmarks and Self-improvement form the improvement loop; failures become follow-up PRs. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]], [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers]], [[wiki/docs/llms-docs-warp-dev/factories-benchmarks]], [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]]

**Metrics, review and adoption (talk)**
- Default factory metrics: human interactions per PR as an automation proxy, DORA metrics, cost per engineer and per stage, and online evals (e.g. a judge scoring redundant tests) over recorded runs. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- With the factory stored as code, improvement agents propose diffs to its markdown files from failed-run patterns; real tasks become private benchmarks. Online evals flag dead ends and "relearning something that should be a skill". [[wiki/sources/youtube-XUEfIxkdT2Q]]
- Review is risk management: owners-file rules force human review of risky files, and merging small non-core PRs without human review raised the qualifying share from about 10% to 80%. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- Adoption advice: onboard everyone to prompt the cloud loop directly (Slack, Jira, MCP) so work is tracked, then automate a growing share. [[wiki/sources/youtube-XUEfIxkdT2Q]]

Getting started and fixes: [[wiki/docs/llms-docs-warp-dev/factories-quickstart]], [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting]].

## Tensions

- Docs describe humans deciding at spec approval, questions and merge. [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]] The CEO talk describes raising the share of small PRs merged with no human review to about 80%, with human review reserved for risky files. [[wiki/sources/youtube-XUEfIxkdT2Q]] These may be defaults versus a mature policy, but sources do not reconcile them.
- Docs list a default team of foreman, triage, spec, implement, review. The talk's loop also names QA, CI/CD and monitoring stages. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/sources/youtube-XUEfIxkdT2Q]]

## Relationships

- **Software factory**: Warp Factories is one concrete product of the pattern. [[wiki/concepts/software-factory]]
- **Foreman agent**: the single entry agent that receives all work. [[wiki/concepts/foreman-agent]]
- **Factory as code**: definition-in-git model. [[wiki/concepts/factory-as-code]]
- **Self-hosting / control plane**: execution-plane split. [[wiki/concepts/self-hosting]], [[wiki/concepts/control-plane]]
- **Human-in-the-loop**: the talk treats human review as a risk-routed policy, not a fixed stage. [[wiki/concepts/human-in-the-loop]], [[wiki/sources/youtube-XUEfIxkdT2Q]]
- **Slack**: one entry channel for prompting the loop. [[wiki/entities/slack]], [[wiki/sources/youtube-XUEfIxkdT2Q]]
- **Claude Code, Codex**: supported harnesses. [[wiki/entities/claude-code]], [[wiki/entities/codex]]

> Synthesis: one vendor, three kinds of voice (docs, an examples repo, a founder talk), so the product is well documented but uncorroborated by any independent source; the talk adds metrics and review policy the docs lack.
