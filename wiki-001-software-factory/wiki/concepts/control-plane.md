---
type: concept
title: Control plane
description: The orchestration layer of a software factory that dispatches work, records sessions, and governs permissions and spend, kept separate from the compute that runs agents.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-data-storage]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/sources/youtube-tGbjIvvYuHE]]"
related:
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/concepts/agent-runner]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/dev-environment]]"
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/compounding-engineering]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/foreman-agent]]"
  - "[[wiki/concepts/agent-evals]]"
  - "[[wiki/concepts/human-in-the-loop]]"
created: 2026-10-25T15:14:42Z
timestamp: 2026-10-25T16:00:00Z
source_count: 5
---

# Control plane

> The coordinating layer of a software factory: it decides what work runs where and records the result, while a separate execution plane does the work.

## Definition

Two framings exist. In the Boundary podcast, the control plane is the top layer of a four-layer stack (compute, dev environment, harness, control plane). It covers dispatch, session traces, plans, scheduling, review, permissions/audit, spend, and feeding team-wide corrections back into the outer harness. [[wiki/sources/youtube-tGbjIvvYuHE]]

In Warp's docs it is a concrete product boundary. Runs, identity/config, observability, integrations, storage and inference routing are always Warp's. Execution is either a Warp-hosted sandbox or a managed self-hosted worker. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]], [[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]

Warp's example repo shows the same boundary from the configuration side. The repo holds only a declarative factory definition (YAML and Markdown). Warp's server syncs it, owns the schema and validates it. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

Synthesis note: the three docs pages and the example repo are all Warp's voice, so they count as one origin for corroboration. The podcast is the only independent origin, and its speakers also sell or build control planes.

## Key claims

- Warp operates the control plane for hosted runs. Managed self-hosting keeps checkout and command execution in the customer network while Warp coordinates. [[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]
- The control plane stays Warp's even when self-hosting. Prompts, results, transcripts and artifacts still flow through it. The worker connects outbound, with no inbound firewall port. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]
- Run data can move to customer-owned S3 or Azure Blob while the control plane still orchestrates every run. It reaches the bucket via a customer-revocable cross-account IAM role and caches nothing. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-data-storage]]
- Model requests route through the control plane for the Warp Agent. Claude Code and Codex call their providers directly from the execution environment. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]
- Duties named in the talk: dispatch, session traces, plans, scheduling, review, permissions/audit, spend, compounding engineering. [[wiki/sources/youtube-tGbjIvvYuHE]]
- Boundary's own control plane is a hosted web app listening to Slack, Linear and GitHub as dispatcher. [[wiki/sources/youtube-tGbjIvvYuHE]] Warp's receives work via automations, integrations with the same tools, endpoints and Factory MCP. [[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]
- In Warp's example factories, dispatch is declarative. An automation's trigger (Slack, Linear or GitHub event plus filter) wakes the single `FOREMAN` agent with the automation body as its task. The foreman delegates to stage agents. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Configuration is git-synced: a push is accepted only after the `warp/factory-config` check passes. The example repo's validator deliberately leaves the verdict to Warp's server rather than parsing YAML itself. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Self-hosting is one setting: `agentDefaults.workerHost` plus a matching runner. Warp coordinates and runs execute on customer compute. This matches the docs' split. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]], [[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]] (same vendor)
- Governance sits in the control-plane config: `credentialStrategy`, per-agent secret lists, scorers that sample a percentage of runs, and a prompt rule that humans always merge. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- The talk argues no open-source control plane exists because each company defines issues and workflows differently and code is cheap to write. [[wiki/sources/youtube-tGbjIvvYuHE]]

## Tensions

- Buy versus build: the podcast urges composition over inheritance, where buying one layer does not force buying the rest. [[wiki/sources/youtube-tGbjIvvYuHE]] Warp's docs present the control plane as always Warp-operated, with only execution and storage movable. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]] Both are vendor-side views.
- Where orchestration logic lives: the talk's control plane is code the team writes (hard-coded while loops, a web app). [[wiki/sources/youtube-tGbjIvvYuHE]] In Warp's examples it is mostly a single foreman prompt in a synced config repo, with the server owning the schema. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

## Relationships

- **Self-hosting**: moves the execution plane (and optionally storage) off the vendor, never the control plane. [[wiki/concepts/self-hosting]]
- **Agent runner**: executes on the plane the control plane dispatches to. [[wiki/concepts/agent-runner]]
- **Agent harness**: sits below the control plane in the talk's layer model. [[wiki/concepts/agent-harness]]
- **Dev environment**: separate layer in the talk's stack. [[wiki/concepts/dev-environment]]
- **Compounding engineering**: a control-plane duty in the talk. [[wiki/concepts/compounding-engineering]]
- **Factory as code**: how Warp's control plane is configured. [[wiki/concepts/factory-as-code]]
- **Foreman agent**: the orchestrating agent the triggers wake. [[wiki/concepts/foreman-agent]]
- **Agent evals**: scorers sample runs as part of the control plane's config. [[wiki/concepts/agent-evals]]
- **Human in the loop**: the human merge gate is encoded in the foreman prompt. [[wiki/concepts/human-in-the-loop]]

> Synthesis: One idea from two vantage points, a design vocabulary from practitioners and a shipped boundary from a vendor. The vendor side has three pages from Warp plus its example repo, which is one voice, so treat agreement as shared framing, not independent proof.
