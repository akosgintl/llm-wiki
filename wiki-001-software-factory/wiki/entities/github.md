---
type: entity
title: GitHub
description: "GitHub is the code forge and event source that Warp's software-factory material uses for triggers, pull requests, CI and git-synced factory definitions."
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-github]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-automations]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
  - "[[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]"
related:
  - "[[wiki/entities/warp-factories]]"
  - "[[wiki/entities/gitlab]]"
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/webhook]]"
  - "[[wiki/concepts/human-in-the-loop]]"
  - "[[wiki/concepts/software-factory]]"
created: 2026-10-25T00:00:00Z
timestamp: 2026-10-25T00:00:00Z
source_count: 25
---

# GitHub

> Code forge that plays three roles in the wiki's sources: event source for agent work, place where agent output lands as PRs, and optional home for git-synced factory definitions.

## Definition

In this wiki GitHub appears almost entirely through Warp Factories. It is one of several work sources (with Slack, Linear, GitLab, Jira and others) and the most fully supported code host. [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]

Voice warning: the docs set and both Warp repos (`warp-factory-examples`, `common-skills`) are all by Warp. Where Warp is the only corroboration, that is one vendor voice, not independent evidence.

## Key claims

**Trigger and event source**
- A Warp GitHub App installation serves both the platform integration and factories. Selected repos produce events: issues, PRs (including merge-queue add/remove), reviews, push, check suites and workflow runs. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]]
- New factories get default automations for mentions and assignments, issue/PR labeled, review submitted, PR closed or merged. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]], [[wiki/docs/llms-docs-warp-dev/factories-connect-your-factory]]
- Routing is label-driven: a `factory:<alias>` label plus an @warp mention picks the factory. Only new content counts as a mention; edits and code blocks are ignored. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]]
- Filters (repo, branches, paths, labels, people, reviews, workflow results) AND together. GitHub triggers skip bot events by default (`skip_bots` = `all`) to avoid feedback loops. [[wiki/docs/llms-docs-warp-dev/factories-automations]], [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]], [[wiki/docs/llms-docs-warp-dev/factories-troubleshooting]]
- GitHub is also a signed-webhook sender (`signature` auth mode). [[wiki/docs/llms-docs-warp-dev/factories-webhooks]]
- Example repo automations use provider `github` for mention/assign, `issue_labeled`, PR opened, closed/merged and `workflow_run_completed`. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

**PRs and CI**
- Factory output returns as comments, branches and PRs in the originating thread. Branch protection and required reviews still apply, so the human gate is ordinary GitHub policy. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]]
- Example: a failed `workflow_run_completed` on `main` makes the agent open a fix PR if small, else an issue. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]]
- One branch and PR live in one repo, so multi-repo changes need one PR per repo. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- PR metrics (PRs merged, cycle time, autonomy) need a connected code host such as the GitHub App. [[wiki/docs/llms-docs-warp-dev/factories-measure-and-improve]]
- `common-skills` runs GitHub Actions that open lockfile PRs in downstream repos on each merge to `main`, using a dedicated GitHub App token. Its `review-pr` skill is built for CI: it writes `review.json` and a workflow publishes it. [[wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE]]

**Definitions as code**
- Definitions can live in a team-owned GitHub repo; merges to the production branch update the factory. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]
- A `warp/factory-config` check validates and dry-runs definition PRs and can be required in branch protection. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- The examples repo's own CI (`validate.yml`) validates every example on PR, push and a weekly cron. [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]

## Tensions

- GitHub vs GitLab: GitHub supports definition hosting; GitLab does not yet, so definitions must be Warp-managed or GitHub-hosted. Only the Warp docs say this. [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]

## Relationships

- **Warp Factories**: GitHub is its main work source and definition host. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]]
- **GitLab**: parallel but less complete integration. [[wiki/docs/llms-docs-warp-dev/factories-integrations-gitlab]]
- **Human in the loop**: merge and review gates are GitHub branch protection. [[wiki/docs/llms-docs-warp-dev/factories-integrations-github]]

> Synthesis: GitHub is the factory's event bus, review gate and config store, but every source here is Warp-authored (docs plus two Warp repos), so the picture is one vendor's account.
