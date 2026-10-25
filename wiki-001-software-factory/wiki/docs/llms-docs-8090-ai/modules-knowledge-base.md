---
type: source
title: Knowledge Base
description: "The 8090 Software Factory Knowledge Base is the store of project context (uploads, meeting notes, research) that agents read when generating requirements, blueprints and work orders, kept current by preset skills and automations."
origin: llms-txt
original_path: https://docs.8090.ai/modules/knowledge-base
source_url: https://docs.8090.ai/modules/knowledge-base
authors: []
published_date: null
raw_file: raw/docs/llms-docs-8090-ai/modules-knowledge-base.md
created: 2026-10-25T18:40:00Z
timestamp: 2026-10-25T18:40:00Z
entities:
  - "[[wiki/entities/8090-software-factory]]"
concepts:
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/knowledge-base]]"
---

# Knowledge Base

> [[raw/docs/llms-docs-8090-ai/modules-knowledge-base|Raw]] · llms-txt

## Summary

The page describes the Knowledge Base module of the 8090 Software Factory: the place that holds "all context that drives the assembly line". Agents draw on it when they generate requirements, blueprints and work orders, so the quality of what they build depends on what has been curated here first. [[raw/docs/llms-docs-8090-ai/modules-knowledge-base#Knowledge Base|cite]]

Curation is two-sided. People create documents in the product or upload files. Agents can read PDFs, images, audio, CSV, Markdown, plain text, PowerPoint and HTML artifacts; video can be previewed but not read by agents. Documents sit in a hierarchy (for example dated notes under a Meeting Transcripts parent) that people reorder by dragging or that an agent can reorganize on request. [[raw/docs/llms-docs-8090-ai/modules-knowledge-base#Using the Knowledge Base|cite]]

Upkeep is delegated to automations and four preset skills per project: Collect Meeting Transcripts, Product Research, Release Notes and Topic Guidelines. Teams can add their own Knowledge Base skills for their processes. [[raw/docs/llms-docs-8090-ai/modules-knowledge-base#Knowledge Base Skills|cite]]

## Key claims

- Agents read many uploaded file types as context; video is preview-only. [[raw/docs/llms-docs-8090-ai/modules-knowledge-base#Curating Context|cite]]
- Automations can collect or update material, e.g. the Zoom MCP server (Settings, Connections, MCP Servers) plus a daily Scheduled automation importing meeting notes. [[raw/docs/llms-docs-8090-ai/modules-knowledge-base#Curating Context|cite]]
- Collect Meeting Transcripts avoids duplicate imports and can notify meeting participants. [[raw/docs/llms-docs-8090-ai/modules-knowledge-base#Knowledge Base Skills|cite]]
- Product Research records evidence, findings and cross-tool analysis; Release Notes drafts customer-facing notes for a confirmed version; Topic Guidelines records product decisions, options and alignment. [[raw/docs/llms-docs-8090-ai/modules-knowledge-base#Knowledge Base Skills|cite]]
- Best practice: add context before asking the assembly line to plan or build, and @-mention Knowledge Base material from requirements, blueprints and work orders to preserve reasoning. [[raw/docs/llms-docs-8090-ai/modules-knowledge-base#Best practices|cite]]

## Notable quotes

> "The Knowledge Base stores all context that drives the 8090 Software Factory assembly line."
> — [[raw/docs/llms-docs-8090-ai/modules-knowledge-base#Knowledge Base|Knowledge Base]]

> "Add context early. Give the assembly line any relevant source material before you ask it to plan or build."
> — [[raw/docs/llms-docs-8090-ai/modules-knowledge-base#Best practices|Best practices]]

## Connections

- **Entities**: [[wiki/entities/8090-software-factory]]
- **Concepts**: [[wiki/concepts/agent-skill]], [[wiki/concepts/knowledge-base]]

> Synthesis: Short vendor reference page; 8090 treats project context as a curated, agent-maintained input layer, with skills doing the upkeep, a different emphasis from the code-and-config framing of Warp and Mastra factories.
