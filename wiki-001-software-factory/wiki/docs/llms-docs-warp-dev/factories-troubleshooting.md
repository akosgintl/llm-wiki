---
type: source
title: Troubleshooting Warp Factories
description: Warp docs page listing symptom/cause/fix entries for factory setup, events that fail to start work, and stalled or unwanted runs.
origin: llms-txt
original_path: https://docs.warp.dev/factories/troubleshooting/
source_url: https://docs.warp.dev/factories/troubleshooting/
authors: []
published_date: null
raw_file: raw/docs/llms-docs-warp-dev/factories-troubleshooting.md
created: 2026-10-25T15:11:13Z
timestamp: 2026-10-25T15:11:13Z
entities:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/github]]"
  - "[[wiki/entities/gitlab]]"
  - "[[wiki/entities/slack]]"
  - "[[wiki/entities/microsoft-teams]]"
  - "[[wiki/entities/linear]]"
  - "[[wiki/entities/jira]]"
concepts:
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/webhook]]"
  - "[[wiki/concepts/human-in-the-loop]]"
---

# Troubleshooting Warp Factories

> [[raw/docs/llms-docs-warp-dev/factories-troubleshooting|Raw]] · llms-txt

## Summary

This is the vendor's symptom-first troubleshooting page for Warp Factories. The docs state it covers the problems teams hit most when setting up a factory and running first work through it, each entry naming the symptom seen in the web app. [[raw/docs/llms-docs-warp-dev/factories-troubleshooting#Troubleshooting Warp Factories|cite]]

It has three groups: setup (permissions, repository picker, agent limits, stale wizard), work not starting (automation routing and per-source causes), and runs and work items (stopping, stuck items, missing pull requests). The recurring lesson is that a "stuck" factory is often waiting on a person, because the default flow pauses for spec approval, clarifying questions and PR review. [[raw/docs/llms-docs-warp-dev/factories-troubleshooting#A work item looks stuck|cite]]

## Key claims

- The docs state creating a factory needs a team or workspace admin role, or the team-level Factories Editor role; configuring one needs its Editor or Admin role. [[raw/docs/llms-docs-warp-dev/factories-troubleshooting#You can’t create or configure a factory|cite]]
- A repository missing from the picker means the code host connection (GitHub or GitLab) does not cover it; an org or group owner or Warp admin must extend it. Setup can also stop at a plan-based agent limit. [[raw/docs/llms-docs-warp-dev/factories-troubleshooting#A repository doesn’t appear in the picker|cite]]
- Finishing setup through Factory MCP does not update an already-open web app page; a refresh is needed. [[raw/docs/llms-docs-warp-dev/factories-troubleshooting#The web app still shows the setup wizard after your agent created a factory|cite]]
- When an event starts no work, check in order: an enabled automation exists, the source is connected to this factory (a workspace-level connection is not enough), the installation can access the repo/project/channel, and every filter. Filters combine with AND, and GitHub skips bot events by default. [[raw/docs/llms-docs-warp-dev/factories-troubleshooting#An event that should start work doesn’t|cite]]
- A follow-up on an existing thread, issue or PR can continue existing work instead of creating a new work item. [[raw/docs/llms-docs-warp-dev/factories-troubleshooting#An event that should start work doesn’t|cite]]
- Per-source causes include: Slack app not in channel or admin approval pending; Teams app or channel not configured; GitLab mention was an edit, or the plan lacks group webhooks; Linear and Jira need a linked Warp account; custom webhooks may be rejected or deduplicated. [[raw/docs/llms-docs-warp-dev/factories-troubleshooting#An event that should start work doesn’t|cite]]
- One action starting two runs means two automations match the same event (e.g. app-mention plus channel-message triggers); narrow one. [[raw/docs/llms-docs-warp-dev/factories-troubleshooting#One action starts two runs|cite]]
- Stop a run from the Runs page with Stop run; it takes effect immediately with no confirmation. [[raw/docs/llms-docs-warp-dev/factories-troubleshooting#You need to stop a run|cite]]
- No PR appearing means the Implement agent is disabled, write access is missing, or the item never reached building; branch protection applies to all factory pushes. [[raw/docs/llms-docs-warp-dev/factories-troubleshooting#No pull request appears|cite]]

## Notable quotes

> "The factory is often waiting on a person rather than failing."
> — [[raw/docs/llms-docs-warp-dev/factories-troubleshooting#A work item looks stuck|A work item looks stuck]]

## Connections

- **Entities**: [[wiki/entities/warp-factories]], [[wiki/entities/github]], [[wiki/entities/gitlab]], [[wiki/entities/slack]], [[wiki/entities/microsoft-teams]], [[wiki/entities/linear]], [[wiki/entities/jira]]
- **Concepts**: [[wiki/concepts/mcp]], [[wiki/concepts/webhook]], [[wiki/concepts/human-in-the-loop]]

> Synthesis: Vendor docs, so causes are Warp's own account; useful mainly as a map of the factory's intake and approval-gate failure modes, and it shows the default human-in-the-loop pauses surface as apparent stalls.
