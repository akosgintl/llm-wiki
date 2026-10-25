---
type: concept
title: Development environment
description: "The layer of a software factory where an agent actually works: runtimes, repositories, toolchain, identity and access to internal services, separate from raw compute and from the harness."
aliases: []
sources:
  - "[[wiki/sources/youtube-tGbjIvvYuHE]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-quickstart]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-runners]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]]"
  - "[[wiki/docs/llms-docs-factory-com/agent-readiness-overview]]"
  - "[[wiki/docs/llms-docs-factory-com/delegations-index]]"
  - "[[wiki/docs/llms-docs-factory-com/environments-overview]]"
  - "[[wiki/docs/llms-factory-mastra-ai/configure-sandboxes]]"
related:
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/agent-runner]]"
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/concepts/secrets-management]]"
  - "[[wiki/concepts/control-plane]]"
  - "[[wiki/concepts/factory-as-code]]"
created: 2026-10-25T15:14:39Z
timestamp: 2026-10-25T18:30:04Z
source_count: 8
---

# Development environment

> The place an agent run executes: repos, toolchain, runtimes and access, one layer above raw compute.

## Definition

In the podcast, Dex places the dev environment as its own layer between compute and harness. It covers runtimes, preview, identity and shared internal services. He argues vendor sandboxes add friction once agents need many internal services. [[wiki/sources/youtube-tGbjIvvYuHE]]

Warp's docs use a narrower, product-shaped split. An environment supplies repositories, toolchain and workspace setup. A runner supplies compute: OS, architecture, instance size, sandbox image. The execution host (Warp-hosted or self-hosted) decides where it runs. [[wiki/docs/llms-docs-warp-dev/factories-runners]] The API quickstart treats a configured environment, with needed repos and dependencies, as a prerequisite; a run references it by `config.environment_id`. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-quickstart]]

Factory's docs make the environment a saved, snapshot-based baseline: repositories cloned and tools installed once, then many isolated instances start from it. [[wiki/docs/llms-docs-factory-com/environments-overview]] Mastra Factory's docs treat the sandbox as the per-session environment: repo checkout plus per-repository setup and teardown commands. [[wiki/docs/llms-factory-mastra-ai/configure-sandboxes]] Factory's Agent Readiness model goes further and counts a reproducible development environment (for example a devcontainer) as a property of the repository that gates agent autonomy. [[wiki/docs/llms-docs-factory-com/agent-readiness-overview]]

## Key claims

- Dex frames environments as pets versus cattle. Boundary's pool of MacBooks, used as compute for its factory, counts as pets. [[wiki/sources/youtube-tGbjIvvYuHE]]
- Warp-hosted runs clone repos, run the runner's `setupCommands`, then the environment's setup commands. A nonzero exit or over 30 minutes fails the run. [[wiki/docs/llms-docs-warp-dev/factories-runners]]
- Warp-hosted Linux runs in a fresh container, default image `warpdotdev/dev-base:latest`. macOS runs in a fresh Apple Silicon VM. Windows is Warp-hosted only. [[wiki/docs/llms-docs-warp-dev/factories-runners]]
- Self-hosted runner settings do not provision capacity. Worker config controls resources, registry auth, volumes and placement. [[wiki/docs/llms-docs-warp-dev/factories-runners]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]]
- On Kubernetes each task is a Job whose Pod comes from a `pod_template`. Task images must be glibc-based; without a Warp environment the image falls back to `ubuntu:22.04`. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]]
- Secrets reach tasks through `secretKeyRef` in the pod template or env flags. Evicting a task pod kills the run and its `emptyDir` workspace. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]]
- Runs start asynchronously: create returns a `run_id`, the caller polls state until `SUCCEEDED` or `FAILED`. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-quickstart]]
- Factory Environments are baselines, not shared workspaces: instances are isolated, changes need a rebuild of the Environment, and work to keep must be committed and pushed. [[wiki/docs/llms-docs-factory-com/environments-overview]]
- Factory offers three compute options: Environment (reusable snapshot, parallel Droids), Droid Computer (persistent managed machine, creatable from a Ready Environment) and Remote Control (a machine you manage). Delegations, Automations and Missions can use Environments. [[wiki/docs/llms-docs-factory-com/environments-overview]]
- Delegations with Dynamic compute need an Environment. If it holds any repository the service account cannot reach, shared delegations fail before the agent starts, even when the request ignores that repo. [[wiki/docs/llms-docs-factory-com/delegations-index]]
- Mastra setup runs at first sandbox start, success is recorded so warm restarts skip it, and teardown runs on failure before retry and on retirement. The agent runs the repo's own test, lint and build commands, so setup must install what they need. [[wiki/docs/llms-factory-mastra-ai/configure-sandboxes]]
- Mastra picks the provider in TypeScript (`src/mastra/sandbox.ts`): `PlatformSandbox` (cloud), `LocalSandbox` (no VM isolation) or another provider such as E2B. Startup is lazy. [[wiki/docs/llms-factory-mastra-ai/configure-sandboxes]]
- Cloud sandboxes are remote VMs without devices, a specific OS or simulators such as iOS; such checks belong in CI or a local sandbox. [[wiki/docs/llms-factory-mastra-ai/configure-sandboxes]]
- Agent Readiness Level 2 example criteria include a devcontainer and AGENTS.md. Developers and agents in identical environments means "entire classes of problems disappear". [[wiki/docs/llms-docs-factory-com/agent-readiness-overview]]
- Multi-repo work can simulate a monorepo from one coordination directory that tells the model where other repos live. [[wiki/sources/youtube-tGbjIvvYuHE]]

## Tensions

- Dex says dev environment and compute are distinct layers, and that vendor sandboxes strain under internal-service access. [[wiki/sources/youtube-tGbjIvvYuHE]] Warp's docs bundle sandbox, image and compute in the runner and sell a hosted sandbox as the default path, while offering self-hosting for in-network access. [[wiki/docs/llms-docs-warp-dev/factories-runners]] The two views are partly vendor positioning on each side.
- Mastra offers `LocalSandbox` on the factory server with no VM isolation, while Factory and Warp describe isolated fresh instances or containers per run. The trade-off is isolation versus access to local hardware and OS. [[wiki/docs/llms-factory-mastra-ai/configure-sandboxes]], [[wiki/docs/llms-docs-factory-com/environments-overview]], [[wiki/docs/llms-docs-warp-dev/factories-runners]]

## Relationships

- **Software factory**: the dev environment is one of its four layers. [[wiki/concepts/software-factory]]
- **Agent runner**: Warp's compute profile applied to an environment. [[wiki/concepts/agent-runner]]
- **Self-hosting**: moves environment execution into your own cluster. [[wiki/concepts/self-hosting]]
- **Factory as code**: Mastra configures the sandbox provider in code. [[wiki/docs/llms-factory-mastra-ai/configure-sandboxes]]
- **Secrets management**: how credentials reach the environment. [[wiki/concepts/secrets-management]]

> Synthesis: Four origins: the podcast (Human Layer and Boundary voices, both vendors), Warp docs (three pages, one voice), Factory docs (three pages, one voice) and Mastra docs (one page). All are vendor docs describing intended behavior, not field experience. Warp, Factory and Mastra converge on a prepared, repeatable baseline per run; the podcast supplies the argument for treating it as its own layer.
