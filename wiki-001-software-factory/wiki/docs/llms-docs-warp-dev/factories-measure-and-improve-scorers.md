---
type: source
title: Configuring Scorers
description: "Warp's docs define a Scorer as an LLM-judge eval that classifies sampled completed factory runs against criteria you set, configured via six fields."
origin: llms-txt
original_path: https://docs.warp.dev/factories/measure-and-improve/scorers/
source_url: https://docs.warp.dev/factories/measure-and-improve/scorers/
authors: []
published_date: null
raw_file: raw/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers.md
created: 2026-10-25T15:07:22Z
timestamp: 2026-10-25T15:07:22Z
entities:
  - "[[wiki/entities/warp-factories]]"
concepts:
  - "[[wiki/concepts/agent-evals]]"
  - "[[wiki/concepts/factory-as-code]]"
---

# Configuring Scorers

> [[raw/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers|Raw]] · llms-txt

## Summary

This short page from the Warp Factories docs describes the Scorer, the eval primitive of a factory. The docs state a Scorer is an LLM-based evaluation that checks whether completed runs from selected agents meet criteria you define, for example "Did the agent run the tests before opening a pull request?" [[raw/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers#Configuring Scorers|cite]]

A Scorer assigns a classification, not a numeric grade, so the docs advise keeping each one focused on a question whose failures can be traced back. Scorers are created on the factory dashboard's Scorers page, which also holds results; they can alternatively be defined as files (`scorers/<name>/scorer.md`) in a factory definition, with two examples in the `02-sdlc-issue-to-pr` example. [[raw/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers#Configuring Scorers|cite]]

Being vendor documentation, everything here is the vendor's own account.

## Key claims

- Six fields configure a Scorer: agents to evaluate (at least one), judge instructions, judge model, classifications (labels each with a score), pass threshold, and sample rate. [[raw/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers#Configuring Scorers|cite]]
- The docs state a sample rate of 10% evaluates about one in ten completed runs. [[raw/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers#Configuring Scorers|cite]]
- With a sample rate above 0%, sampled runs are scored automatically after completion, recording a classification, score and reasoning. [[raw/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers#Configuring Scorers|cite]]
- Any single run can be scored on demand, suggested for testing new judge instructions before raising the sample rate; rescoring replaces the previous result from that Scorer. [[raw/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers#Configuring Scorers|cite]]
- Related pages: repeated Scorer failures feed Self-improvement follow-up PRs, and benchmarks compare model and runner configurations on the same tasks. [[raw/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers#Related pages|cite]]

## Notable quotes

> "A Scorer assigns a classification, not a numeric grade, so keep each one focused on a question its failures can point back to."
> — [[raw/docs/llms-docs-warp-dev/factories-measure-and-improve-scorers#Configuring Scorers|location]]

## Connections

- **Entities**: [[wiki/entities/warp-factories]]
- **Concepts**: [[wiki/concepts/agent-evals]], [[wiki/concepts/factory-as-code]]

> Synthesis: Warp's online LLM-as-judge eval for production agent runs (sampled, classification-based), complementary to its offline benchmarks; fits the wiki's agent-evals theme.
