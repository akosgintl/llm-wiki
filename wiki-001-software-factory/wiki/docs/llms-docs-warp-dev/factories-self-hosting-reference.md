---
type: source
title: Self-hosted worker reference
description: Warp's reference for the oz-agent-worker daemon, listing CLI flags, config-file schema and metrics settings for its Docker, Kubernetes, Direct and Command backends.
origin: llms-txt
original_path: https://docs.warp.dev/factories/self-hosting/reference/
source_url: https://docs.warp.dev/factories/self-hosting/reference/
authors: []
published_date: null
raw_file: raw/docs/llms-docs-warp-dev/factories-self-hosting-reference.md
created: 2026-10-25T15:11:18Z
timestamp: 2026-10-25T15:11:18Z
entities:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/docker]]"
  - "[[wiki/entities/kubernetes]]"
concepts:
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/concepts/agent-runner]]"
---

# Self-hosted worker reference

> [[raw/docs/llms-docs-warp-dev/factories-self-hosting-reference|Raw]] · llms-txt

## Summary

This is a lookup page, not an argument. It documents `oz-agent-worker`, the daemon a team runs on its own infrastructure so that Warp cloud agent runs execute there instead of on Warp's hosts. The docs state that the worker has four "managed backends": `docker` (default), `kubernetes`, `direct` and `command`. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-reference#Worker flags|cite]]

Settings come from CLI flags or a YAML config file, and the docs state that flags win over file values. Only one backend block may appear in a config file. Each backend has its own fields: volumes and pull policy for Docker; namespace, pod template, sidecars, deadlines and unschedulable timeout for Kubernetes; per-task workspaces plus setup and teardown hooks for Direct; dispatch and cancel commands for Command. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-reference#Config file|cite]]

The page also covers OpenTelemetry metrics through env vars and points to sibling pages for setup, monitoring, registries and troubleshooting. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-reference#Metrics configuration|cite]]

## Key claims

- The docs state `--worker-id` and an API key (`--api-key` or `WARP_API_KEY`) are required. The worker ID is what callers pass to `--host` to route tasks, and several workers may share one ID for load balancing. IDs starting with `warp` are reserved and the worker refuses to start. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-reference#Worker flags|cite]]
- The docs state `--max-concurrent-tasks` defaults to `0` (unlimited), and extra tasks wait for a slot. `--one-shot` exits after one task and is Direct-backend only. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-reference#Optional|cite]]
- The docs state `--idle-on-complete` keeps the `oz` process alive after a conversation ends, for follow-up via session sharing. Default is `45m`, 10 minutes for runs created directly through the Agent API; a task-level value takes precedence. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-reference#Optional|cite]]
- The docs state a Docker-run worker has two levels of `-e`: Docker's passes env vars to the worker container, the worker's own `-e` passes them into the task containers it spawns. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-reference#Rootful Linux Docker example with all flags|cite]]
- The docs state the Kubernetes backend runs tasks as Jobs. Image precedence is Warp environment image, then `default_image`, then `ubuntu:22.04`. `pod_template` accepts a raw PodSpec, including `valueFrom.secretKeyRef` for Kubernetes Secrets. Unschedulable pods fail after `10m` by default, leaving room for node autoscaling. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-reference#Config file fields|cite]]
- The docs state the Command backend pipes a JSON task payload to a `dispatch_command` on stdin, handing the task to an external runtime. Task credentials stay in that payload, not in the command environment. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-reference#Config file fields|cite]]
- The docs state metrics default to the OTLP exporter. Prometheus listens on `localhost:9464` unless set to `0.0.0.0`. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-reference#Metrics configuration|cite]]

## Notable quotes

> "Worker IDs starting with `warp` are reserved and cannot be used."
> — [[raw/docs/llms-docs-warp-dev/factories-self-hosting-reference#Optional|Worker flags]]

## Connections

- **Entities**: [[wiki/entities/warp-factories]], [[wiki/entities/docker]], [[wiki/entities/kubernetes]]
- **Concepts**: [[wiki/concepts/self-hosting]], [[wiki/concepts/agent-runner]]

> Synthesis: Vendor reference for the execution layer of Warp Factories; it shows where agent runs physically execute and how a team swaps in its own runtime via the Command backend.
