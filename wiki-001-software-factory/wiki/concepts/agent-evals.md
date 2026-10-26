---
type: concept
title: Agent evals
description: Measurement of whether AI agents do their job well, via LLM-judge scoring of production runs, fixed-task benchmarks across configurations, and eval metrics gating pipeline changes.
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-benchmarks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
  - "[[wiki/sources/youtube-tGbjIvvYuHE]]"
  - "[[wiki/sources/youtube-XUEfIxkdT2Q]]"
related:
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/compounding-engineering]]"
  - "[[wiki/concepts/software-factory]]"
created: 2026-10-25T15:14:43Z
timestamp: 2026-10-26T07:12:58Z
source_count: 13
---

# Agent evals

> Evaluation of agent output, online (judging real runs) and offline (comparing configurations on fixed tasks), used to decide what to change in an agent pipeline.

## Definition

In Warp Factories, evals are a productized loop of four features: dashboard metrics, Scorers, Benchmarks and Self-improvement. A Scorer is an LLM judge that classifies sampled completed runs against criteria you write. A benchmark compares model, harness and runner configurations for one agent on identical fixed tasks. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]], [[wiki/docs/llms-docs-warp-dev/factories-benchmarks]]

The Boundary podcast uses the term as practitioner discipline, not a product: every pipeline change should ship with eval metrics. It describes no judge or benchmark machinery. [[wiki/sources/youtube-tGbjIvvYuHE]]

A second Boundary talk, with Warp's CEO, frames evals as "online evals" over recorded factory runs, plus private benchmarks built from real tasks. It is the same vocabulary as the Warp docs, voiced by the vendor founder. [[wiki/sources/youtube-XUEfIxkdT2Q]]

## Key claims

- A Scorer gives a classification, not a numeric grade. Six fields configure it: agents, judge instructions, judge model, labelled classifications, pass threshold, sample rate. A 10% rate scores about one in ten runs. Any run can also be scored on demand; rescoring replaces the earlier result. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers]]
- In definition files, scorers default to `samplingRate` 25 and can set `selfImprovement: true`. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]] The `task-compliance` example scorer in `warp-factory-examples` shows the shape: attached to the implementer, labels `compliant`=1, `partial`=0.5, `non_compliant`=0, `passingScore` 1, `samplingRate` 25, a Haiku judge, `selfImprovement: true`, and judging from the issue text rather than the PR's self-description. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Separate from factory runs, the `skill-doctor` skill in `common-skills` scores local conversation transcripts on four rubrics (efficiency, code-quality, procedure-compliance, verbosity) and drafts SKILL.md edits. It runs locally and does not upload transcripts. Only its description was read, not its scorers. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- Benchmarks: suite of tasks, each run as trials per configuration. Tasks come from a completed run or from scratch, with correctness criteria. Suites hold 1-6 configurations, tasks pinned to commit SHAs. [[wiki/docs/llms-docs-warp-dev/factories-benchmarks]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]
- Benchmark results are a comparison, not a universal model ranking. Cost mixes billed usage with estimates and is not for invoicing. More trials and Scorers raise cost. Apply winners one change at a time against a recorded baseline. [[wiki/docs/llms-docs-warp-dev/factories-benchmarks]]
- Self-improvement: a failure is a score below the pass threshold. Default trigger is 25 unreviewed failures per agent or the oldest at 7 days (1-50 configurable). The follow-up PR links failing runs under "Regressions addressed". "Nothing is adopted without your review." [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]], [[wiki/docs/llms-docs-warp-dev/factories-how-factories-work]]
- PRs can target application code or the factory's own prompts and skills. A recurring failure can update the responsible skill. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-self-improvement]], [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]
- Dashboard metrics: autonomy (merged PRs with no human code push), PR cycle time, cost per PR (median estimate). Use them to pick runs to investigate, not to conclude causes. Total runs includes eval and benchmark runs. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]], [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]
- A run can be scored or turned into a benchmark task from the dashboard. [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]
- Loop: define a Scorer, collect baseline, inspect failures, benchmark a candidate, review and adopt, keep monitoring. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]]
- Warp's default factory metrics: human interactions per PR (automation proxy), DORA metrics, cost per engineer and per stage, and online evals, for example a judge model scoring redundant tests. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- With the factory stored as code, improvement agents can find patterns in failed runs and propose diffs to the definition's markdown files. Real tasks can become private benchmarks; the environment must be replicated so agents cannot see the finished PR. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- Online evals for dead ends, verbosity and "relearning something that should be a skill" feed skill improvement. This matches the `skill-doctor` rubrics. [[wiki/sources/youtube-XUEfIxkdT2Q]], [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]
- Yield is hard to define and differs per business; it climbs from PRs to features to customer outcomes, so a metric like PR count is only a proxy. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- Review as risk management: owners-file rules force human review of risky files; merging small non-core PRs without review raised qualifying PRs from about 10% to 80%. [[wiki/sources/youtube-XUEfIxkdT2Q]]
- Boundary: every pipeline change ships eval metrics; dedupe accuracy is lower than hoped; 60% is the target for difficulty classification. [[wiki/sources/youtube-tGbjIvvYuHE]]

## Tensions

- Scope and rigor: Warp describes a full, automated eval stack; Boundary admits imperfect metrics and modest targets (60%), and pairs evals with "95% automatic" plus human shepherds, not full automation. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]], [[wiki/sources/youtube-tGbjIvvYuHE]]
- Yield definition: Warp's dashboard fixes autonomy, cycle time and cost per PR as defaults, while the CEO says yield is business-specific and must reach customer outcomes, which no built-in metric measures. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]], [[wiki/sources/youtube-XUEfIxkdT2Q]]
- Self-measurement: the docs warn that the headline Total runs count is inflated by eval and benchmark runs. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]]

- Warp-only corroboration: the two repos and the docs set share one author (Warp), so the Scorer shape (classification labels, sampling rate, self-improvement flag) agrees across docs and examples by construction, not by independent confirmation. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]], [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers]]

## Relationships

- **Factory as code**: scorers and benchmarks are versioned files; eval-driven fixes land as PRs on the definition. [[wiki/concepts/factory-as-code]]
- **Human in the loop**: self-improvement proposals need human review. [[wiki/concepts/human-in-the-loop]]
- **Agent skill**: skills are a main target of eval-driven edits. [[wiki/concepts/agent-skill]]
- **Compounding engineering**: Boundary's team-wide feedback loop is the informal cousin. [[wiki/concepts/compounding-engineering]]

> Synthesis: Twelve of thirteen sources trace to Warp (its docs set, two Warp-authored repos, and a podcast with Warp's CEO), so the mechanics are vendor claims and agreement among them is not independent corroboration; only the earlier Boundary podcast is a separate voice, and it corroborates just the principle that pipeline changes need eval metrics.
