---
type: source
title: "Quickstart"
description: "8090 Software Factory's first-run guide: set up an org and project, have the Agent write requirements and blueprints, extract work orders, and hand them to a coding agent over MCP."
origin: llms-txt
original_path: https://docs.8090.ai/general/quickstart
source_url: https://docs.8090.ai/general/quickstart
authors: []
published_date: null
raw_file: raw/docs/llms-docs-8090-ai/general-quickstart.md
created: 2026-10-25T18:30:00Z
timestamp: 2026-10-25T18:30:00Z
entities:
  - "[[wiki/entities/claude-code]]"
  - "[[wiki/entities/codex]]"
concepts:
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/agent-skill]]"
---

# Quickstart

> [[raw/docs/llms-docs-8090-ai/general-quickstart|Raw]] · llms-txt · [source](https://docs.8090.ai/general/quickstart)

## Summary

The page walks a new user through one end-to-end pass of 8090 Software Factory. You create an organization (paid seats, Stripe checkout, you become admin) and a project. The project holds all context that defines the software: requirements, blueprints, work orders and feedback. [[raw/docs/llms-docs-8090-ai/general-quickstart#create-your-organization|cite]]

The pipeline is document-driven. Each project starts with six Product Overview documents. A built-in "Get Started" workflow, run by the in-product Agent, interviews you (or reverse engineers a connected codebase) and produces Feature Requirements, each paired with a Feature Blueprint of the same title. Blueprints come in three categories: Containers, Components, Feature Blueprints. The Agent then runs an "Extract Work Orders" skill to turn requirements plus blueprints into work orders, which you review, assign and group into phases. [[raw/docs/llms-docs-8090-ai/general-quickstart#define-your-requirements|cite]]

The last hop leaves the product. External coding agents connect over MCP, read work orders and write back status. Optional steps (connect GitHub/GitLab, add Knowledge Base material) give the Agent more context. Closing sections point to drift detection, feedback intake and support channels.

## Key claims

- A project's sidebar has Home, Agents, Skills, Automations, Knowledge Base, Requirements, Blueprints, Work Orders, Feedback and Settings. [[raw/docs/llms-docs-8090-ai/general-quickstart#take-the-tour-and-open-quick-start|cite]]
- The six Product Overview documents are Business Problem, Current State, Product Description, Personas, Success Metrics and Technical Requirements. [[raw/docs/llms-docs-8090-ai/general-quickstart#define-your-requirements|cite]]
- Connecting a repo (GitHub or GitLab, chosen branch indexed) lets the Agent search and read code while drafting documents. [[raw/docs/llms-docs-8090-ai/general-quickstart#connect-your-repository-optional|cite]]
- Cursor, Claude Code, Claude Desktop, Codex and others connect via MCP with browser sign-in and no API key. [[raw/docs/llms-docs-8090-ai/general-quickstart#connect-your-coding-agent|cite]]
- The platform tells the coding agent to set a work order to In Progress on start and In Review on finish. [[raw/docs/llms-docs-8090-ai/general-quickstart#connect-your-coding-agent|cite]]
- An installable "8090 Software Factory agent skill" keeps the coding agent on the same process each time. [[raw/docs/llms-docs-8090-ai/general-quickstart#connect-your-coding-agent|cite]]
- Drift checks are opt-in: a "Detect Code Drift" automation comments on blueprints and requirements when pushed code contradicts them, and Drift Bot can review pull requests. [[raw/docs/llms-docs-8090-ai/general-quickstart#next-steps|cite]]

## Notable quotes

> "A project holds the context that defines your software, from requirements and blueprints to work orders and feedback."
> — [[raw/docs/llms-docs-8090-ai/general-quickstart#create-your-first-project|Create your first project]]

## Connections

- **Entities**: [[wiki/entities/claude-code]], [[wiki/entities/codex]]
- **Concepts**: [[wiki/concepts/software-factory]], [[wiki/concepts/agent-skill]]

> Synthesis: Product-doc view of a hosted software factory where requirements and blueprints, not code, are the source of truth, and external coding agents are the build step reached over MCP.
