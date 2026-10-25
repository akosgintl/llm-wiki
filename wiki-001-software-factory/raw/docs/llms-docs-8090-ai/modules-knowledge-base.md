---
title: "Knowledge Base"
subtitle: "Turn project knowledge into context that feeds your assembly line."
authors: []
published_date: null
source_url: https://docs.8090.ai/modules/knowledge-base
origin: llms-txt
llms_txt: https://docs.8090.ai/llms.txt
section: "Docs / Agents"
fetched: 2026-10-25T18:13:39Z
---

# Knowledge Base (/modules/knowledge-base)

The Knowledge Base stores all context that drives the 8090 Software Factory assembly line. Agents use this material when they generate requirements, blueprints, and work orders.

## Using the Knowledge Base [#using-the-knowledge-base]

### Curating Context [#curating-context]

Create documents in 8090 Software Factory, or upload documents from your computer.

* Agents can read many uploaded file types as context, including PDFs, images, audio, CSV files, Markdown and plain text, PowerPoint files, and HTML artifacts. You can preview these file types inline in the Knowledge Base too. Video can be previewed, but agents can't read it.
* You can create [automations](/modules/automations) that collect, organize, or update Knowledge Base material. For example, connect the Zoom MCP server under **Settings → Connections → MCP Servers**, then import project meeting notes into the Knowledge Base with a daily **Scheduled** automation.

### Organizing Context [#organizing-context]

Use the document hierarchy to keep related material together. For example, store dated session notes under a **Meeting Transcripts** parent. You can move documents as your project changes, and create automations to collect, organize, or update Knowledge Base material.

You can move documents yourself by dragging them onto another document or to a new position in the hierarchy. You can also ask an agent to reorganize the Knowledge Base.

## Knowledge Base Skills [#knowledge-base-skills]

Every project includes these preset skills to add and maintain useful context in the Knowledge Base:

* **Collect Meeting Transcripts:** Imports recent, project-related meeting transcripts into the **Meeting Transcripts** section. It avoids duplicate imports and can notify meeting participants.
* **Product Research:** Researches comparable products and records evidence, findings, and cross-tool analysis under **Product Research**.
* **Release Notes:** Drafts customer-facing notes for a confirmed product version under **Release Notes**.
* **Topic Guidelines:** Records ongoing product decisions, their options, current alignment, and source materials under **Topics**.

Create your own Knowledge Base [skills](/modules/skills) to capture the processes and preferences your team wants agents to follow.

## Best practices [#best-practices]

* Add context early. Give the assembly line any relevant source material before you ask it to plan or build.
* Keep the hierarchy easy to scan. Group related material under clear parent documents, and use descriptive titles so people and agents can find it.
* @-mention related Knowledge Base material within the Knowledge Base and from requirements, blueprints, and work orders. This keeps the reasoning behind the work available to the people and agents who continue it.
* Use agent skills and automations for recurring curation work.
