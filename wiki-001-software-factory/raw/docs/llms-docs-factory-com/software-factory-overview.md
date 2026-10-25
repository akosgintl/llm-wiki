---
title: "Software Factory"
subtitle: "Use Software Factory to manage the automations that cover your software delivery lifecycle."
authors: []
published_date: null
source_url: https://docs.factory.com/software-factory/overview.md
origin: llms-txt
llms_txt: https://docs.factory.com/llms.txt
section: "Documentation"
fetched: 2026-10-25T18:18:02Z
---

# Software Factory

Use Software Factory to manage the automations that cover your software delivery lifecycle.

Software Factory is a 24/7 autonomous system that connects AI agents across the software development lifecycle, from intake and triage through planning, execution, validation, shipping, monitoring, and recurring automation.

  Software Factory is in Private Preview. To request access, fill out the form at <a href="https://factory.com/contact">factory.com/contact</a> or contact your Factory account team.

To delegate work directly from [Linear](/delegations/linear), [Jira](/delegations/jira), or [Microsoft Teams](/delegations/microsoft-teams), follow the Delegations guide for that app. You do not need to create a Software Factory automation for these workflows.

![Software Factory overview dashboard](/docs-assets/images/software-factory-dashboard.webp)

*Illustrative dashboard values; your numbers reflect your own connected automations.*

## What Software Factory is

In the Factory App, Software Factory gives teams one place to track that system: live metrics, connected integrations, repository coverage, stage health, and persistent automations.

| Stage | What it covers |
| --- | --- |
| **Triage** | Classify inbound work, reduce duplicates, and route items. |
| **Code-gen** | Connect requests from Slack or issue trackers to implementation sessions. |
| **Validate** | Run code review, security review, and QA before merge. |
| **Release** | Track deployment gates, release checks, and ship workflows. |
| **Document** | Keep repository knowledge current with AutoWiki. |
| **Monitor** | Connect incidents, alerts, and agent effectiveness back to engineering work. |

### When to use Software Factory

Use Software Factory as a centralized view into product health across your software delivery lifecycle:

- Which SDLC stages already have automation coverage.
- Which repositories, integrations, or stages need setup.
- Whether review, QA, docs, triage, and incident workflows are healthy.
- How much work Factory processed over time.

## Manage coverage across the SDLC

Open <a href="https://app.factory.ai/software-factory"><strong>Software Factory</strong></a> to see your delivery lifecycle as an automation coverage map. Each stage shows what is already connected, what is healthy, and where to add coverage next.

Use the dashboard to:

- Switch between different time ranges.
- Scan impact metrics and stage health.
- Filter by integration, including GitHub, Slack, Linear, and GitLab.
- Open a stage to review templates, automations, and covered repositories.
- Create missing automations from the stage detail page or the [Automations](/software-factory/automations) page.

Repo-backed stages show repository coverage, so you can see which repos are covered by workflows like **Code Review**, **QA**, **Security Audit**, and **AutoWiki**.

| Stage | Templates and setup | Coverage shown |
| --- | --- | --- |
| **Triage** | Triage | Intake automation coverage |
| **Code-gen** | Slack and Linear delegation | Integration coverage |
| **Validate** | Code Review, QA, Security Audit | Repository coverage |
| **Release** | Release checks and deployment gates | Release status and gate coverage |
| **Document** | AutoWiki | Repository coverage |
| **Monitor** | Incident Response, Agent Effectiveness | Incident and efficiency coverage |

## Metrics and coverage

### Automation metrics

Software Factory gives you a live view of automation impact across the SDLC with metrics such as:

![Software Factory automation metrics](/docs-assets/images/software-factory-automation-metrics.png)

| Metric | Dashboard tag | What it indicates |
| --- | --- | --- |
| **Tickets Triaged** | Queue burn | Tickets classified, deduplicated, or routed by triage workflows. |
| **PR Validations** | Merge gate | QA, security, and code-review checks run against pull requests. |
| **PRs Merged** | Ship rate | Pull requests merged in the selected time range. |
| **Incidents Processed** | Reliability | Incidents, errors, or alerts handled by incident-response workflows. |

Use these metrics to see where automation is moving work forward and where your team may need more coverage.

### Stage metrics

Use stage metrics to spot which parts of the Software Factory are moving work, waiting for setup, or blocked by handoffs.

| Stage | Example metric | What it answers |
| --- | --- | --- |
| Triage | Throughput and backlog | Are incoming requests being classified and routed quickly? |
| Code-gen | Lines changed and session output | How much implementation work is flowing through Droid? |
| Validate | Pass rate and review volume | Are QA, security, and code-review gates healthy? |
| Release | Deployments and cycle time | Is validated work reaching users on schedule? |
| Document | Docs updated and repository coverage | Is AutoWiki keeping knowledge current? |
| Monitor | Incident response and token efficiency | Are incidents and agent effectiveness improving? |

### Health and coverage

Health and coverage show where Software Factory is ready to run and where setup is missing.

| Signal | Meaning |
| --- | --- |
| Stage health | Whether the stage has the integrations and automations it needs. |
| Repository coverage | Which repositories are covered for Validate, Release, and Document workflows. |
| Integration coverage | Which intake systems, channels, and deployment tools are connected. |
| Setup gaps | The repos, channels, or gates that still need an automation or integration. |

{/* sweep-allow: term-bullets */}

- **Stage metrics** show throughput, pass rate, queue depth, and cycle time for each SDLC stage.
- **Health** shows whether a stage has the integrations and automations it needs.
- **Coverage** shows where those automations apply, such as which repositories are covered for **Validate**, **Release**, or **Document**.

If something is missing, open the stage to connect the integration, add the repo or channel, or create the expected automation.

  
    Create and manage automations that run across your SDLC stages.
  
  
    Classify and route inbound work into the right workflow.
  

