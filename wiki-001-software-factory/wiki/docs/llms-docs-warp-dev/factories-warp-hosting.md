---
type: source
title: Warp-hosted execution for Warp Factories
description: "Warp's docs say hosted execution runs factory agents in managed sandboxes on Warp compute, suited to publicly reachable repos and services, with private networks pointed to managed self-hosting."
origin: llms-txt
original_path: https://docs.warp.dev/factories/warp-hosting/
source_url: https://docs.warp.dev/factories/warp-hosting/
authors: []
published_date: null
raw_file: raw/docs/llms-docs-warp-dev/factories-warp-hosting.md
created: 2026-10-25T15:11:14Z
timestamp: 2026-10-25T15:11:14Z
entities:
  - "[[wiki/entities/warp-factories]]"
concepts:
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/agent-runner]]"
---

# Warp-hosted execution for Warp Factories

> [[raw/docs/llms-docs-warp-dev/factories-warp-hosting|Raw]] · llms-txt

## Summary

This short docs page describes the default execution mode for Warp Factories. The docs state that Warp-hosted execution runs factory work in managed sandboxes: Warp provisions the compute, while the factory definition selects each agent's runner, repositories, setup and credentials. [[raw/docs/llms-docs-warp-dev/factories-warp-hosting#Warp-hosted execution for Warp Factories|cite]]

The page frames a single decision rule. Use hosted execution when the factory's repositories and services are reachable from the public internet; Warp handles capacity and host maintenance. If services are private, or a network boundary must contain checkout and execution, use managed self-hosting instead. [[raw/docs/llms-docs-warp-dev/factories-warp-hosting#Warp-hosted execution for Warp Factories|cite]]

The rest is a checklist of operating properties: sandbox isolation, OS/architecture, resources, concurrency and networking. Details are mostly delegated to sibling pages (infrastructure and security, runners). This is vendor documentation, so all of it is the vendor's own account.

## Key claims

- Agents run in isolated sandboxes; execution, data and credential boundaries are documented on a separate infrastructure-and-security page. [[raw/docs/llms-docs-warp-dev/factories-warp-hosting#Sandbox environment|cite]]
- Runner and workspace configuration come from the factory definition; a factory may also reuse an existing Warp environment if its definition names one. [[raw/docs/llms-docs-warp-dev/factories-warp-hosting#OS and architecture|cite]]
- CPU and memory depend on plan; Enterprise plans can configure up to 32 vCPUs and 64 GiB of memory, with custom provisioning via support beyond that. [[raw/docs/llms-docs-warp-dev/factories-warp-hosting#Resources|cite]]
- Warp limits concurrent hosted runs per team; runs started at the limit queue until another completes. [[raw/docs/llms-docs-warp-dev/factories-warp-hosting#Concurrency|cite]]
- Network egress is on by default. For firewall allowlisting, Warp's IP ranges are listed under "Warp-hosted agent networking" in the team's Platform page of the Admin Panel or in the web app's user settings. [[raw/docs/llms-docs-warp-dev/factories-warp-hosting#Networking|cite]]

## Notable quotes

> "Use it when your factory's repositories and services are reachable from the public internet."
> — [[raw/docs/llms-docs-warp-dev/factories-warp-hosting#Warp-hosted execution for Warp Factories|location]]

## Connections

- **Entities**: [[wiki/entities/warp-factories]]
- **Concepts**: [[wiki/concepts/self-hosting]], [[wiki/concepts/factory-as-code]], [[wiki/concepts/agent-runner]]

> Synthesis: The hosted half of the hosted-versus-self-hosted split in Warp Factories; useful mainly as the decision boundary (public reachability vs private network) and as the source of the per-team concurrency queue and Enterprise resource caps.
