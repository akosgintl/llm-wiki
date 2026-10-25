---
type: concept
title: Knowledge base
description: "The store of curated project or engineering context that agents read and reason over in a software factory, kept current by people, automations and skills."
aliases: [context lake]
sources:
  - "[[wiki/docs/llms-docs-8090-ai/modules-knowledge-base]]"
  - "[[wiki/docs/llms-docs-port-io/getting-started-agentic-sdlc-pillars]]"
related:
  - "[[wiki/concepts/software-factory]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/human-in-the-loop]]"
created: 2026-10-25T18:30:34Z
timestamp: 2026-10-25T18:30:34Z
source_count: 2
---

# Knowledge base

> Multiple framings, see Definition.

## Definition

In both sources the knowledge base is the shared context layer under a software factory: agents read it, so output quality depends on what it holds.

8090 frames it as a curated document store. It holds "all context that drives the assembly line": uploads, meeting notes and research. [[wiki/docs/llms-docs-8090-ai/modules-knowledge-base]] Port calls its version a "context lake". It is a catalog-based layer that joins repositories, cloud resources, incidents and deployments into one source of truth. [[wiki/docs/llms-docs-port-io/getting-started-agentic-sdlc-pillars]]

## Key claims

- Agents draw on it when generating requirements, blueprints and work orders. [[wiki/docs/llms-docs-8090-ai/modules-knowledge-base]]
- In Port it is the base pillar: "AI agents reason over it, workflows act on it, and dashboards visualize it." [[wiki/docs/llms-docs-port-io/getting-started-agentic-sdlc-pillars]]
- 8090 content is curated by hand (create or upload) and by automations. Agents read PDFs, images, audio, CSV, Markdown, text, PowerPoint and HTML. Video is preview-only. [[wiki/docs/llms-docs-8090-ai/modules-knowledge-base]]
- 8090 delegates upkeep to four preset skills: Collect Meeting Transcripts, Product Research, Release Notes and Topic Guidelines. Teams can add their own. [[wiki/docs/llms-docs-8090-ai/modules-knowledge-base]]
- Documents form a hierarchy that people or an agent can reorganize. [[wiki/docs/llms-docs-8090-ai/modules-knowledge-base]]
- Best practice: add context before asking the factory to plan or build, and @-mention knowledge base items from requirements, blueprints and work orders. [[wiki/docs/llms-docs-8090-ai/modules-knowledge-base]]
- Port builds on top of it: visual workflows, Port AI, an AI registry for skills, prompts and MCP access, and governance via scorecards and RBAC. [[wiki/docs/llms-docs-port-io/getting-started-agentic-sdlc-pillars]]

## Tensions

- Content type differs. 8090 centres on human-authored and uploaded documents. Port centres on structured, connected engineering data from the catalog. Each source covers only its own framing; the two are different shapes of the same idea, not a shared definition. [[wiki/docs/llms-docs-8090-ai/modules-knowledge-base]], [[wiki/docs/llms-docs-port-io/getting-started-agentic-sdlc-pillars]]

## Relationships

- **software-factory**: the knowledge base is the context foundation of the factory model. [[wiki/concepts/software-factory]]
- **agent-skill**: in 8090, skills maintain the knowledge base. [[wiki/concepts/agent-skill]]
- **human-in-the-loop**: Port pairs the context layer with approval flows and governance. [[wiki/concepts/human-in-the-loop]]

> Synthesis: Two vendors, two separate origins, one shared claim: agent output is only as good as the curated context beneath it. This is vendor-docs evidence only.
