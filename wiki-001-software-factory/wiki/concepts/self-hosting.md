---
type: concept
title: Self-hosting
description: Running agent execution on infrastructure you operate while a vendor control plane still routes, tracks and records the work.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-runners]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-secrets-aws-ecr]]"
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
  - "[[wiki/docs/llms-docs-warp-dev/factories-warp-hosting]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
related:
  - "[[wiki/concepts/agent-runner]]"
  - "[[wiki/concepts/control-plane]]"
  - "[[wiki/concepts/secrets-management]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/git-worktree]]"
created: 2026-10-25T00:00:00Z
timestamp: 2026-10-25T00:00:00Z
source_count: 24
---

# Self-hosting

> Execution (checkout, commands, workspace) runs on your hardware; orchestration, inference routing and run records stay with the vendor.

## Definition

In this wiki the concept is defined by one voice: Warp. All 24 source pages come from the Warp docs set or from Warp's own example repo, so nothing here is independent corroboration. Warp's docs put it as: "You control the compute, network access, runtime secrets, and execution workspaces while Warp tracks each run." [[wiki/docs/llms-docs-warp-dev/factories-self-hosting]] It needs an Enterprise plan. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]

The model is a split between a control plane that is always Warp's and an execution plane that is either a Warp-hosted sandbox or a worker you run. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]], [[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]] Warp-hosted is the default and suits repos and services reachable from the public internet; a private network is the reason to self-host. [[wiki/docs/llms-docs-warp-dev/factories-warp-hosting]]

## Key claims

**Two architectures.** Managed: Warp routes work to a long-lived `oz-agent-worker`. Unmanaged: your CI or script calls `oz agent run` and Warp only records the session. Teams may mix both. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting]], [[wiki/docs/llms-docs-warp-dev/factories-deployment-patterns]]

**Runners and backends.** A managed worker has four backends: Docker (default), Kubernetes, Direct and Command. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-reference]]
- Docker: one container per task via the mounted Docker socket; Linux, glibc images only. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-docker]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-quickstart]]
- Kubernetes: a namespace-scoped Helm chart; one Job per task from a `pod_template`; no CRDs or cluster RBAC; one worker replica per release. Evicting a task pod kills the run. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]]
- Direct: tasks run in per-task directories on the host, with no container isolation. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]] Git worktrees isolate files and branches, not the host. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]
- Command and one-shot Direct: an existing CI system or scheduler allocates compute, and Warp still routes and tracks. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-external-orchestrators]]
- Runner YAML does not provision capacity when self-hosted; worker config does. [[wiki/docs/llms-docs-warp-dev/factories-runners]] Factory definitions route with `workerHost`, and the example repo ships a worker-routing example. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

**Network.** Workers need only outbound access to `oz.warp.dev:443` (WebSocket), with no inbound ports. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting]], [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting]] Runs are routed by matching `--host` to `--worker-id`, case-sensitive; several workers may share an ID. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-reference]] For air-gapped hosts, the worker, task, sidecar and preflight images must be mirrored to a private registry. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-private-container-registry]]

**Auth and secrets.** The worker uses a self-hosted worker API key; run creators use an agent key tied to the Default Service Account. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-quickstart]] The worker key is not available to tasks; task credentials come via Kubernetes Secrets or env flags. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]] Direct tasks start with a minimal environment so `WARP_API_KEY` does not leak. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]] Hosted runners use a role-backed ECR credential; self-hosted ones use backend-specific registry auth. [[wiki/docs/llms-docs-warp-dev/factories-secrets-aws-ecr]]

**What still crosses to Warp.** Prompts, results, transcripts and model requests flow through Warp and may contain code. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting]] Enterprise teams can move transcripts, artifacts and attachments to their own S3 or Azure bucket; the control plane reaches it through a revocable cross-account role. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-data-storage]]

**Operations.** Workers export OpenTelemetry metrics (Prometheus, OTLP). [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-monitoring]] A healthy worker connection says nothing about task network, egress or credentials. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting]]

## Tensions

- "Your infrastructure" is a partial boundary: the overview stresses control of compute and workspaces, while the security page states that run content still transits Warp. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting]], [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]
- Inference differs by harness: the Warp Agent calls models through Warp, while Claude Code and Codex call their providers directly from the execution environment. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]
- Forges without first-class support are reached by token plus a clone in setup commands, so they lose provider events. [[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]

## Relationships

- **Agent runner**: the worker is the runner abstraction. [[wiki/concepts/agent-runner]]
- **Control plane**: the hosted half of the split. [[wiki/concepts/control-plane]]
- **Secrets management**: worker key, task secrets and registry auth are separate. [[wiki/concepts/secrets-management]]
- **Factory as code**: `workerHost` and runner files select the host. [[wiki/concepts/factory-as-code]]
- **Git worktree**: per-task isolation on Direct. [[wiki/concepts/git-worktree]]

> Synthesis: Every origin here is Warp's own voice (the docs set plus Warp's example repo), so this is the vendor's deployment model, not a field-tested one. Read the control-plane/execution-plane split as the central idea.
