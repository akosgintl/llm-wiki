---
type: docs
title: Mastra Factory
description: Documentation for Mastra Factory, a self-hosted system that takes work from intake to reviewed pull requests, covering concepts, integrations, configuration, deployment and reference.
original_path: https://factory.mastra.ai/llms.txt
source_url: https://factory.mastra.ai/llms.txt
catalog: raw/docs/llms-factory-mastra-ai/llms.txt
catalog_size: 24
created: 2026-10-25T18:13:55Z
timestamp: 2026-10-25T18:13:55Z
---

# Mastra Factory — Docs map

> Catalog: https://factory.mastra.ai/llms.txt · 24 links · 10 ingested

## Ingested

- [[wiki/docs/llms-factory-mastra-ai/what-is-factory|What's Factory?]]
- [[wiki/docs/llms-factory-mastra-ai/using-intake|Intake]]
- [[wiki/docs/llms-factory-mastra-ai/using-work-and-approvals|Work items]]
- [[wiki/docs/llms-factory-mastra-ai/using-reviews|Review items]]
- [[wiki/docs/llms-factory-mastra-ai/using-sessions|Sessions]]
- [[wiki/docs/llms-factory-mastra-ai/configure-sandboxes|Sandboxes]]
- [[wiki/docs/llms-factory-mastra-ai/configure-custom-skills|Custom skills]]
- [[wiki/docs/llms-factory-mastra-ai/configure-boards-and-rules|Boards and rules]]
- [[wiki/docs/llms-factory-mastra-ai/deployment|Deployment]]
- [[wiki/docs/llms-factory-mastra-ai/configure-github|GitHub]]

## Areas

### Getting started

Entry page of the docs set.

- [Get started](https://factory.mastra.ai/index.md) — first setup path for a new factory

### Models

Model configuration for the agents a factory runs.

- [Models](https://factory.mastra.ai/configure/models.md) — which models agents use, and how to set them

### Code forges and trackers

Configuration of source control and work-tracking integrations other than GitHub.

- [GitLab](https://factory.mastra.ai/configure/gitlab.md) — alternative code forge to the ingested GitHub page
- [Linear](https://factory.mastra.ai/configure/linear.md) — issue tracker as an intake source
- [Jira](https://factory.mastra.ai/configure/jira.md) — issue tracker as an intake source
- [incident.io](https://factory.mastra.ai/configure/incidentio.md) — incidents as a possible intake source

### Chat

Slack configuration.

- [Slack](https://factory.mastra.ai/configure/slack.md) — chat surface for humans working with the factory

### Access and persistence

How a deployment authenticates users and stores its data.

- [Auth](https://factory.mastra.ai/configure/auth.md) — who may use a deployed factory
- [Storage](https://factory.mastra.ai/configure/storage.md) — where factory state is kept

### Agent skill

A skill page for agents that work with the factory.

- [Skill](https://factory.mastra.ai/skill.md) — how an agent is taught to drive the factory

### Troubleshooting

Diagnosis of common problems.

- [Troubleshooting](https://factory.mastra.ai/troubleshooting.md) — failure modes when running a factory

### Reference

Lookup material for settings and programmatic use.

- [Environment variables](https://factory.mastra.ai/reference/environment-variables.md) — exact settings for deployment
- [MastraFactory API](https://factory.mastra.ai/reference/mastra-factory-api.md) — programmatic setup of a factory
- [create-factory](https://factory.mastra.ai/reference/create-factory.md) — scaffolding command for new factories

## Pulling more

Ingest the catalog again with a new intent, or ask a question the pages above
do not answer — the query path fetches from this catalog (`QUERY.md` Q.6b).
