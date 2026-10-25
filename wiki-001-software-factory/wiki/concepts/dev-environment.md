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
related:
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/agent-runner]]"
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/concepts/secrets-management]]"
  - "[[wiki/concepts/control-plane]]"
created: 2026-10-25T15:14:39Z
timestamp: 2026-10-25T15:14:39Z
source_count: 4
---

# Development environment

> The place an agent run executes: repos, toolchain, runtimes and access, one layer above raw compute.

## Definition

In the podcast, Dex places the dev environment as its own layer between compute and harness. It covers runtimes, preview, identity and shared internal services. He argues vendor sandboxes add friction once agents need many internal services. [[wiki/sources/youtube-tGbjIvvYuHE]]

Warp's docs use a narrower, product-shaped split. An environment supplies repositories, toolchain and workspace setup. A runner supplies compute: OS, architecture, instance size, sandbox image. The execution host (Warp-hosted or self-hosted) decides where it runs. [[wiki/docs/llms-docs-warp-dev/factories-runners]] The API quickstart treats a configured environment, with needed repos and dependencies, as a prerequisite; a run references it by `config.environment_id`. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-quickstart]]

## Key claims

- Dex frames environments as pets versus cattle. Boundary's pool of MacBooks, used as compute for its factory, counts as pets. [[wiki/sources/youtube-tGbjIvvYuHE]]
- Warp-hosted runs clone repos, run the runner's `setupCommands`, then the environment's setup commands. A nonzero exit or over 30 minutes fails the run. [[wiki/docs/llms-docs-warp-dev/factories-runners]]
- Warp-hosted Linux runs in a fresh container, default image `warpdotdev/dev-base:latest`. macOS runs in a fresh Apple Silicon VM. Windows is Warp-hosted only. [[wiki/docs/llms-docs-warp-dev/factories-runners]]
- Self-hosted runner settings do not provision capacity. Worker config controls resources, registry auth, volumes and placement. [[wiki/docs/llms-docs-warp-dev/factories-runners]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]]
- On Kubernetes each task is a Job whose Pod comes from a `pod_template`. Task images must be glibc-based; without a Warp environment the image falls back to `ubuntu:22.04`. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]]
- Secrets reach tasks through `secretKeyRef` in the pod template or env flags. Evicting a task pod kills the run and its `emptyDir` workspace. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]]
- Runs start asynchronously: create returns a `run_id`, the caller polls state until `SUCCEEDED` or `FAILED`. [[wiki/docs/llms-docs-warp-dev/factories-api-and-sdk-quickstart]]
- Multi-repo work can simulate a monorepo from one coordination directory that tells the model where other repos live. [[wiki/sources/youtube-tGbjIvvYuHE]]

## Tensions

- Dex says dev environment and compute are distinct layers, and that vendor sandboxes strain under internal-service access. [[wiki/sources/youtube-tGbjIvvYuHE]] Warp's docs bundle sandbox, image and compute in the runner and sell a hosted sandbox as the default path, while offering self-hosting for in-network access. [[wiki/docs/llms-docs-warp-dev/factories-runners]] The two views are partly vendor positioning on each side.

## Relationships

- **Software factory**: the dev environment is one of its four layers. [[wiki/concepts/software-factory]]
- **Agent runner**: Warp's compute profile applied to an environment. [[wiki/concepts/agent-runner]]
- **Self-hosting**: moves environment execution into your own cluster. [[wiki/concepts/self-hosting]]
- **Secrets management**: how credentials reach the environment. [[wiki/concepts/secrets-management]]

> Synthesis: Two origins: the podcast (Human Layer and Boundary voices, both vendors) and Warp's vendor docs (three pages, one voice, so not three independent sources). They agree an environment is distinct from the agent logic, but the docs describe intended behavior, not field experience.
