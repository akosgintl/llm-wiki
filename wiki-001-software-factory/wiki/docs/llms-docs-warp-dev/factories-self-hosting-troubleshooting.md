---
type: source
title: "Self-hosting troubleshooting"
description: Warp's runbook for diagnosing self-hosted Factories worker daemons (oz-agent-worker) that won't start, won't connect, skip tasks, or fail tasks on Docker, Kubernetes and Direct backends.
origin: llms-txt
original_path: https://docs.warp.dev/factories/self-hosting/troubleshooting/
source_url: https://docs.warp.dev/factories/self-hosting/troubleshooting/
authors: []
published_date: null
raw_file: raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting.md
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

# Self-hosting troubleshooting

> [[raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting|Raw]] · llms-txt

## Summary

This is vendor documentation for operators of the managed self-hosting architecture of Warp Factories, where an `oz-agent-worker` daemon runs agent tasks on infrastructure the customer controls. The docs state that the steps do not apply to unmanaged deployments (`oz agent run` in e.g. GitHub Actions), which follow their own environment's docs. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting#Self-hosting troubleshooting|cite]]

The page is organized by symptom: worker won't start, worker won't connect, tasks not picked up, metrics missing, task failures, image pull failures. Each entry gives a cause and numbered fixes, split per backend (Docker, Kubernetes, Direct). The Kubernetes section is the deepest: it maps pod symptoms (Pending/FailedScheduling, OOMKilled, Evicted, exit code 143) to verify and fix steps. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting#Task failures|cite]]

A recurring theme is the split between the worker and the task. The worker's connection to Warp and its API key say nothing about the task pod's network, credentials or resources; those must be provisioned and tested separately.

## Key claims

- The docs state a worker that can't connect usually has an invalid or expired **Self-hosted worker** API key, or no outbound access to `oz.warp.dev:443` and WebSocket `wss://oz.warp.dev`. `--log-level debug` shows connection details. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting#Worker won’t connect|cite]]
- Tasks go unpicked when the worker is down, the `--host` value does not match `--worker-id` (case-sensitive), or worker and task belong to different teams. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting#Tasks not being picked up|cite]]
- Docker backend needs a running daemon on `linux/amd64` or `linux/arm64` (no Windows containers); custom task images must be glibc-based, not Alpine/musl. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting#Worker won’t start|cite]]
- Kubernetes backend: the worker needs specific RBAC on jobs, pods, pod logs and events, and runs a preflight Job (default image `busybox:1.36`) that validates pod shape only, not task images, Secrets or network. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting#Kubernetes backend|cite]]
- Unschedulable task pods fail after `kubernetesBackend.unschedulableTimeout` (default 10 minutes); Jobs are terminated with `DeadlineExceeded` after `kubernetesBackend.activeDeadlineSeconds` (default eight hours). Exit code 143 is SIGTERM and does not by itself prove OOM. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting#Task exits with code 143|cite]]
- The worker API key authenticates the worker to Warp and is not available to tasks; task credentials must come through the customer's Secret integration and `pod_template`. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting#Other Kubernetes failures|cite]]
- For debugging, `--no-cleanup` retains the container, Job or workspace (failed Kubernetes Jobs otherwise stay 24 hours), and metrics default to port `9464`, which must bind `0.0.0.0` in containers. [[raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting#Metrics not appearing|cite]]

## Notable quotes

> "A working worker connection to Warp says nothing about the task's network policies, service mesh, proxy, or egress."
> — [[raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting#Other Kubernetes failures|Other Kubernetes failures]]

> "Raising only a limit doesn't help, because the scheduler places Pods by their requests."
> — [[raw/docs/llms-docs-warp-dev/factories-self-hosting-troubleshooting#Pod stays Pending with FailedScheduling|Pod stays Pending]]

## Connections

- **Entities**: [[wiki/entities/warp-factories]], [[wiki/entities/docker]], [[wiki/entities/kubernetes]]
- **Concepts**: [[wiki/concepts/self-hosting]], [[wiki/concepts/agent-runner]]

> Synthesis: Operational runbook, not architecture; useful as evidence that a self-hosted agent runner is an ordinary job scheduler whose failures are mostly infrastructure (quotas, images, egress, credentials) rather than agent logic.
