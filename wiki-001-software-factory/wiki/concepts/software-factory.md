---
type: concept
title: Software factory
description: A system of coding agents, compute, context and orchestration that turns work requests into reviewed pull requests with humans at key gates; vendors frame it as an agent team, a spec layer, a board, an SDLC dashboard or a governance platform.
aliases: []
sources:
  - "[[wiki/sources/youtube-tGbjIvvYuHE]]"
  - "[[wiki/sources/youtube-XUEfIxkdT2Q]]"
  - "[[wiki/sources/youtube-b5O6gb_Zuk8]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
  - "[[wiki/docs/llms-factory-mastra-ai/what-is-factory]]"
  - "[[wiki/docs/llms-factory-mastra-ai/using-intake]]"
  - "[[wiki/docs/llms-factory-mastra-ai/deployment]]"
  - "[[wiki/docs/llms-docs-8090-ai/general-introduction]]"
  - "[[wiki/docs/llms-docs-8090-ai/general-quickstart]]"
  - "[[wiki/docs/llms-docs-factory-com/software-factory-overview]]"
  - "[[wiki/docs/llms-docs-factory-com/welcome-index]]"
  - "[[wiki/docs/llms-docs-factory-com/agent-readiness-overview]]"
  - "[[wiki/docs/llms-docs-port-io/getting-started-agentic-sdlc-pillars]]"
  - "[[wiki/docs/llms-docs-port-io/glossary]]"
  - "[[wiki/docs/llms-docs-port-io/solutions-agentops-overview]]"
related:
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/control-plane]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/dev-environment]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/context-engineering]]"
  - "[[wiki/concepts/knowledge-graph]]"
  - "[[wiki/concepts/knowledge-base]]"
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/entities/warp-factories]]"
created: 2026-10-25T15:14:44Z
timestamp: 2026-10-26T07:15:28Z
source_count: 20
---

# Software factory

> Agents plus infrastructure that route work requests to reviewed pull requests, humans approving key steps. Seven origins use the term, and they do not mean the same thing.

## Definition

No shared definition exists. Each origin sells a different slice, so the framings are laid side by side.

| Origin | What "software factory" means |
|---|---|
| Boundary podcast | A stack of layers: compute, dev environment, harness (inner/outer), control plane. Build, buy or mix each layer. [[wiki/sources/youtube-tGbjIvvYuHE]] |
| Warp CEO on Boundary podcast | An agentic loop from issue through triage, optional spec, implementation, review, QA, CI/CD and monitoring; cloud-hosted, highly measurable, defined declaratively in code. The developer's job becomes "building, maintaining, and tuning this loop". [[wiki/sources/youtube-XUEfIxkdT2Q]] |
| Warp (docs, repos) | A team of cloud agents on your repos. Work from Slack, GitHub, Linear or Jira goes through triage, planning, implementation, review; a PR returns to the originating thread. A "foreman" agent coordinates. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]] |
| Mastra Factory | A web app and board: connect a repo, pull issues in as Work items, guide each through investigate, plan, implement, PR review. Each session runs in an isolated sandbox; it never edits the local checkout. [[wiki/docs/llms-factory-mastra-ai/what-is-factory]] |
| 8090 | A spec-and-context layer. Requirements, Blueprints and Work Orders live in a Knowledge Graph; external coding agents (Cursor, Claude Code, Codex) are the build step, reached over MCP. [[wiki/docs/llms-docs-8090-ai/general-introduction]], [[wiki/docs/llms-docs-8090-ai/general-quickstart]] |
| Factory (Factory.ai) | "A 24/7 autonomous system" across the SDLC, shown as a dashboard of six stages (Triage, Code-gen, Validate, Release, Document, Monitor) with coverage and health. Private Preview. [[wiki/docs/llms-docs-factory-com/software-factory-overview]], [[wiki/docs/llms-docs-factory-com/welcome-index]] |
| Port | An "AI software factory" is the system you build to run the agentic SDLC. Core is a catalog-based Context Lake; add workflows, agent management and governance. [[wiki/docs/llms-docs-port-io/getting-started-agentic-sdlc-pillars]], [[wiki/docs/llms-docs-port-io/glossary]] |

Readings of the table:

- Runner-centred: Warp and Mastra describe agents that do the work and a path from issue to PR. Warp centres on a foreman agent; Mastra centres on a board with approval gates.
- Context-centred: 8090 and Port treat shared knowledge as the core. For 8090, requirements and blueprints, not code, are the source of truth. For Port, the catalog is the core and agents sit on top.
- Observability-centred: Factory's product page is a coverage map over the SDLC, not an agent runner. [[wiki/docs/llms-docs-factory-com/software-factory-overview]]
- Loop-centred: the Warp CEO talk defines the factory as the loop plus its measurement; hosts agree on the loop shape and differ only on step order (for example QA before or after review). [[wiki/sources/youtube-XUEfIxkdT2Q]]
- Layered: the first podcast describes the infrastructure beneath any of these. [[wiki/sources/youtube-tGbjIvvYuHE]]
- Sceptical: a second Boundary episode (harness mechanics) names the "lights-off software factory" as a risk rather than a goal. [[wiki/sources/youtube-b5O6gb_Zuk8]]

Port notes its sense differs from the older "outsourced development shop" meaning. [[wiki/docs/llms-docs-port-io/glossary]]

## Key claims

### Runner-centred factories

- Many entry points, one dispatcher: chat, forges, trackers, webhooks, REST, schedules and MCP all land with the foreman as a work item that keeps source context. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]
- A Warp factory is a git repo of path-named Markdown and YAML: `factory.yaml`, agents, automations, runners, scorers, skills. Exactly one agent is the foreman. Push, pass the `warp/factory-config` check, and it syncs. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Boundary's own factory ("agent tries BAML") uses MacBooks as compute, Claude Code or Codex headless as harness, hard-coded while loops as outer harness, and a hosted web app listening to Slack, Linear and GitHub as dispatcher. [[wiki/sources/youtube-tGbjIvvYuHE]]
- Mastra intake: issues become Work items, PRs become Review items. Sources are GitHub, GitLab, Linear, Jira and incident.io. Each teammate picks personally which issues to follow. [[wiki/docs/llms-factory-mastra-ai/using-intake]]
- Local and cloud share one task in Warp: Factory MCP lets a local agent send work in, pull a task in an isolated worktree, and hand it back. Tasks are not locked. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]
- Harness is pluggable per agent in Warp: the Warp agent, Claude Code or Codex (example: Codex reviews Claude Code's work). [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Agent behaviour is shared like packages: skills are pinned by lockfile hash and pushed to consumer repos by bot PRs. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- Multi-repo: Warp opens one PR per repo and waits for all; the podcast simulates a monorepo from one coordination directory. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]], [[wiki/sources/youtube-tGbjIvvYuHE]]

### Context-centred factories

- 8090 diagnoses the problem as deciding what to build, not writing code: "Development itself has never been the bottleneck." Fragmented docs and "single-player" AI tools are blamed. [[wiki/docs/llms-docs-8090-ai/general-introduction]]
- 8090 flow: Product Overview documents, then Requirements, then Blueprints, then Work Orders. A Drift Bot comments when code contradicts them. External agents read work orders over MCP and write back status. [[wiki/docs/llms-docs-8090-ai/general-quickstart]]
- Port: the Context Lake joins repos, cloud resources, incidents and deployments; "AI agents reason over it, workflows act on it, and dashboards visualize it." [[wiki/docs/llms-docs-port-io/getting-started-agentic-sdlc-pillars]]
- Port's AgentOps adds governance for the factory's agents: inventory, certification, enforcement, optimization. Agents must be registered, owned, scoped, audited and stoppable. [[wiki/docs/llms-docs-port-io/solutions-agentops-overview]]
- Factory.ai's Agent Readiness Model puts the burden on the repo: five levels, nine pillars, a level unlocks at 80% pass of the previous one. [[wiki/docs/llms-docs-factory-com/agent-readiness-overview]]

### Observability and measurement

- Warp's stated default metrics: human interactions per PR (automation proxy), DORA metrics, cost per engineer and per stage, and online evals such as a judge model scoring redundant tests. Yield is hard to define and differs per business, rising from PRs to features to customer outcomes. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- With the factory stored as code, improvement agents can propose diffs to its Markdown files from failed runs; real tasks can become private benchmarks; online evals for dead ends, verbosity and relearning feed skill improvement. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- Factory.ai's dashboard shows four headline metrics (Tickets Triaged, PR Validations, PRs Merged, Incidents Processed), stage health, repository and integration coverage, and setup gaps. [[wiki/docs/llms-docs-factory-com/software-factory-overview]]
- Warp lists dashboards, scorers and benchmarks; its examples attach sampled LLM-judge scorers to agents. Boundary requires eval metrics with every pipeline change. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]], [[wiki/sources/youtube-tGbjIvvYuHE]]
- Mastra shows progress in an Overview page, session transcripts and an Audit log. [[wiki/docs/llms-factory-mastra-ai/what-is-factory]]

### Human gates (where all origins agree on the shape)

- Warp CEO talk: review is risk management. Owners-file rules force human review of risky files (for example env var changes); a policy of merging small, non-core PRs without human review raised the qualifying share from about 10% to 80%. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- Warp: the factory never merges; the example foreman prompt says never to merge or approve a spec for a human. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Mastra: four steps always wait for a person: starting a run, accepting a non-bug task, approving a plan, merging a PR. Auto-start and auto-approve toggles relax the first and third. [[wiki/docs/llms-factory-mastra-ai/what-is-factory]]
- Boundary: a loop fixes CodeRabbit comments, stops after 3 iterations to ask a human, and a human presses merge. Aim for 95% automatic, not fully automatic. [[wiki/sources/youtube-tGbjIvvYuHE]]
- Port: at the "AI-autonomous" level agents triage, code, review and handle incidents while humans approve key decisions; its glossary has people set intent, review and own the deploy decision. [[wiki/docs/llms-docs-port-io/solutions-agentops-overview]], [[wiki/docs/llms-docs-port-io/glossary]]
- Boundary harness-mechanics episode: not bullish on agent teams, because the bottleneck is humans reviewing design, not output volume. [[wiki/sources/youtube-b5O6gb_Zuk8]]
- 8090: work orders are reviewed, assigned and grouped into phases by people before agents build. [[wiki/docs/llms-docs-8090-ai/general-quickstart]]

## Tensions

- How to adopt. Dexter (Human Layer): remove humans from your existing loop, then pipeline your best engineers' workflow. Zach (Warp): onboard everyone to the cloud loop even by direct prompt, so work is tracked, then automate a growing share. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- How far to automate. The Boundary harness episode warns that companies leaning hard into a lights-off, human-free factory risk a 3 AM break that nobody can debug because no one read the code in months. Vendor docs and the Warp CEO talk instead aim for a growing automated share with human gates kept. [[wiki/sources/youtube-b5O6gb_Zuk8]], [[wiki/sources/youtube-XUEfIxkdT2Q]], [[wiki/docs/llms-docs-warp-dev/factories]]
- Organisation vs technology. The talk argues factories fail on people problems, for example split product and engineering orgs ("you cannot have a factory if you have two companies two separate orgs"). Product docs mostly treat it as a tooling problem. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- What the factory is. Warp and Mastra: agents that carry an issue to a PR. 8090: a spec layer that hands tasks to someone else's coding agents. Port: a catalog and governance platform. Factory.ai: a coverage dashboard. These are different products sharing a label, not one concept implemented five ways. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/docs/llms-factory-mastra-ai/what-is-factory]], [[wiki/docs/llms-docs-8090-ai/general-introduction]], [[wiki/docs/llms-docs-port-io/glossary]], [[wiki/docs/llms-docs-factory-com/software-factory-overview]]
- Where the source of truth lives. 8090: requirements and blueprints, kept in sync with code by drift detection. Port: the Context Lake catalog. Warp: definition files in a git repo. Mastra: the target repo plus the Factory project, kept separate. [[wiki/docs/llms-docs-8090-ai/general-quickstart]], [[wiki/docs/llms-docs-port-io/glossary]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]], [[wiki/docs/llms-factory-mastra-ai/what-is-factory]]
- Who coordinates. Warp: an agent (the foreman) is the only default agent that talks to humans. Mastra: a board with explicit human approval gates, no foreman. Boundary: hard-coded while loops, not an agent. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/docs/llms-factory-mastra-ai/what-is-factory]], [[wiki/sources/youtube-tGbjIvvYuHE]]
- Prioritisation. Mastra says Factory "doesn't rank, sequence, or filter incoming work"; sub-issues arrive unlinked to their parent. Factory.ai's dashboard instead tracks Triage as a stage with throughput and backlog. [[wiki/docs/llms-factory-mastra-ai/using-intake]], [[wiki/docs/llms-docs-factory-com/software-factory-overview]]
- Buy vs build. Dex argues vendor sandboxes add friction and teams should own the dev environment; no open-source control plane exists. [[wiki/sources/youtube-tGbjIvvYuHE]] Warp offers a bundled hosted product with optional self-hosting. [[wiki/docs/llms-docs-warp-dev/factories]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]] Mastra splits auth, storage and sandboxes into independent swap points and allows fully self-hosting; the default is platform services. [[wiki/docs/llms-factory-mastra-ai/deployment]]
- Access control. Warp says instructions never change what an agent can do, yet Factory MCP has no read-only or per-factory scopes. Port argues for scoped, non-human identities and a kill switch as the minimum. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents]], [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]], [[wiki/docs/llms-docs-port-io/solutions-agentops-overview]]
- Readiness. Factory.ai treats the repo as what to engineer (AGENTS.md, devcontainer, branch protection as criteria for Level 2). The runner-centred docs mostly assume the repo is ready. [[wiki/docs/llms-docs-factory-com/agent-readiness-overview]]

## Relationships

- **Human in the loop**: gates at spec/plan and merge in nearly every framing. [[wiki/concepts/human-in-the-loop]]
- **Control plane**: the podcast's dispatch, traces, scheduling, audit layer; the foreman, Mastra's board and Factory.ai's dashboard each play part of it. [[wiki/concepts/control-plane]]
- **Agent harness / dev environment**: lower layers of the podcast's stack. [[wiki/concepts/agent-harness]], [[wiki/concepts/dev-environment]]
- **MCP**: Warp's Factory MCP and 8090's work-order access bridge outside agents to the factory; Port exposes its catalog the same way. [[wiki/concepts/mcp]]
- **Factory as code**: Warp's declarative definition files. [[wiki/concepts/factory-as-code]]
- **Context engineering / knowledge graph / knowledge base**: the centre of 8090 and Port's framings. [[wiki/concepts/context-engineering]], [[wiki/concepts/knowledge-graph]], [[wiki/concepts/knowledge-base]]
- **Self-hosting**: Mastra and Warp differ in how open it is. [[wiki/concepts/self-hosting]]

> Synthesis: Corroboration is thin and mostly vendor-to-vendor. The 20 sources come from 7 origins. Warp is 6 of them (four docs pages, two Warp repos); the Warp pages are one voice. Mastra, 8090, Factory.ai and Port are each one voice, and all sell products. The three podcast episodes (Human Layer and Boundary hosts) are the only outside voices, but they are one series with shared hosts, and the second features Warp's CEO, so it adds Warp-side detail (metrics, yield, risk-routed review) rather than independent confirmation of Warp docs. The third episode (Claude Code skills and subagents) adds only a sceptical note on "lights-off" factories and a human-review-bottleneck argument, from the same hosts, so it counts as a counterweight, not a separate corroborating voice. What they agree on is the shape: work request in, reviewed PR out, and a human at merge or approval. What they disagree on is what the factory is. Nothing here shows that any of it works.
