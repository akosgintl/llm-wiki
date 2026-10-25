---
type: source
title: Factory benchmarks
description: Warp Factories docs describe benchmark suites that run one factory agent across model, harness and runner configurations on fixed tasks, scored for correctness and cost, to pick a production configuration.
origin: llms-txt
original_path: https://docs.warp.dev/factories/benchmarks/
source_url: https://docs.warp.dev/factories/benchmarks/
authors: []
published_date: null
raw_file: raw/docs/llms-docs-warp-dev/factories-benchmarks.md
created: 2026-10-25T15:00:00Z
timestamp: 2026-10-25T15:00:00Z
entities:
  - "[[wiki/entities/warp-factories]]"
concepts:
  - "[[wiki/concepts/agent-evals]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/agent-runner]]"
  - "[[wiki/concepts/agent-harness]]"
---

# Factory benchmarks

> [[raw/docs/llms-docs-warp-dev/factories-benchmarks|Raw]] · llms-txt

## Summary

This is vendor documentation for the Benchmarks feature of [[wiki/entities/warp-factories]]. The docs state that a benchmark compares model, harness and runner configurations for a single factory agent on identical fixed tasks, so a change can be tested on representative work before it touches a live factory. [[raw/docs/llms-docs-warp-dev/factories-benchmarks#How benchmarks work|cite]]

The unit structure is: a suite (reusable task collection for one agent), tasks (a prompt plus "Correctness criteria" for the built-in Correctness Scorer), and trials (one run of a task under one configuration; repetitions add trials). At launch the user picks configurations, Scorers and repetitions; Warp runs and scores trials, and the run snapshots those inputs so later suite edits do not rewrite history. [[raw/docs/llms-docs-warp-dev/factories-benchmarks#How benchmarks work|cite]]

The page then walks through the web-app flow (create suite, add task from a completed run or from scratch, launch), how to read results, and how to apply a winner: change one configuration at a time, keep Scorers active, and compare later production runs against a recorded baseline. [[raw/docs/llms-docs-warp-dev/factories-benchmarks#Apply a benchmark result|cite]]

## Key claims

- The docs state tasks can be seeded from a completed run of the agent, reproducing real work, or written from scratch. [[raw/docs/llms-docs-warp-dev/factories-benchmarks#Create and run a benchmark|cite]]
- Blocked trials stay "Blocked" but can still be scored; each Scorer decides whether the evidence meets its criteria. [[raw/docs/llms-docs-warp-dev/factories-benchmarks#How benchmarks work|cite]]
- Results give an overall recommendation (highest quality, needs at least two comparable configurations), plus most-efficient and lowest-cost picks, a correctness-vs-cost chart, an overall table and per-Scorer grids. [[raw/docs/llms-docs-warp-dev/factories-benchmarks#Review benchmark results|cite]]
- Total cost includes trials and Scorer usage, mixes billed Warp usage with estimates for external inference, and is for comparison, not invoice reconciliation. "Run time" is total trial duration, not billable agent time. [[raw/docs/llms-docs-warp-dev/factories-benchmarks#Review benchmark results|cite]]
- More trials and more Scorers raise the cost of a benchmark run. [[raw/docs/llms-docs-warp-dev/factories-benchmarks#Create and run a benchmark|cite]]
- Version-controlled factories define suites in `benchmarks/<suite-slug>/suite.yaml` and tasks in `benchmarks/<suite-slug>/tasks/<task-slug>.yaml`. [[raw/docs/llms-docs-warp-dev/factories-benchmarks#Apply a benchmark result|cite]]

## Notable quotes

> "Review the result as a comparison, not as a universal model ranking"
> — [[raw/docs/llms-docs-warp-dev/factories-benchmarks#Review benchmark results|Review benchmark results]]

## Connections

- **Entities**: [[wiki/entities/warp-factories]]
- **Concepts**: [[wiki/concepts/agent-evals]], [[wiki/concepts/factory-as-code]], [[wiki/concepts/agent-runner]], [[wiki/concepts/agent-harness]]

> Synthesis: Benchmarks are Warp's productized agent-eval loop: pre-change A/B on fixed tasks, then post-change production Scorers against a baseline; claims are vendor-stated, not independently verified.
