---
title: "Intake"
subtitle: "Understand how issues and pull requests arrive in Factory and what to check before starting an agent."
authors: []
published_date: null
source_url: https://factory.mastra.ai/using/intake.md
origin: llms-txt
llms_txt: https://factory.mastra.ai/llms.txt
section: "Docs / Core concepts"
fetched: 2026-10-25T18:10:21Z
---

# Intake

Intake is incoming work available for an agent to investigate or review. Issues become [Work items](https://factory.mastra.ai/using/work-and-approvals), while pull requests become [Review items](https://factory.mastra.ai/using/reviews).

## Choose your sources

Connect the source, then select which issues you want to follow in **Settings → Work Intake**. Issue selections are personal: each teammate chooses their own sources. Shared repository connections and Linear routing determine where that work belongs.

| Source                 | Destination                                           | Required setup                                                                                                                  |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| GitHub issues          | Work board unless a label route selects another board | GitHub App access, a linked repository, and personal issue synchronization and repository selection.                            |
| GitLab issues          | Selected board                                        | A GitLab connection, issue synchronization and project selection, and organization routing to a Factory and board.              |
| Linear issues          | Selected board                                        | Workspace authorization, personal issue synchronization and project selection, and organization routing to a Factory and board. |
| Jira issues            | Selected board                                        | A Jira site connection, issue synchronization and project selection, and organization routing to a Factory and board.           |
| incident.io follow-ups | Selected board                                        | An incident.io connection, follow-up synchronization and source selection, and organization routing to a Factory and board.     |
| GitHub pull requests   | Review board                                          | GitHub access and the linked repository. PR review intake uses the Factory's linked repository.                                 |
| GitLab merge requests  | Review board                                          | GitLab access and the linked repository.                                                                                        |

Use [GitHub](https://factory.mastra.ai/configure/github), [GitLab](https://factory.mastra.ai/configure/gitlab), [Linear](https://factory.mastra.ai/configure/linear), [Jira](https://factory.mastra.ai/configure/jira), or [incident.io](https://factory.mastra.ai/configure/incidentio) for connection and selection instructions. [Slack](https://factory.mastra.ai/configure/slack) starts conversational sessions and has its own option for creating Work cards from new threads.

## Verify incoming work

After connecting a source, create one active issue in a selected repository or routed project. Find its card in the destination Factory and match the source identifier, title, and link.

Synchronization is asynchronous. Once an issue arrives, complete an investigation to verify model access and execution.

## How work starts

Work begins in one of three ways:

- **You start it.** Select **Investigate** on an issue card, or start a review from its Review card, and open the session. You can start runs manually whether or not automation is on.
- **Factory starts it automatically.** With **Auto-start runs** on, Factory begins a run when the source is trusted and the task policy allows it. The default GitHub rules allow an automatic initial run only for issues created after the Factory by an author with write or admin access to the repository.
- **A source event starts it.** With automation on, some events trigger follow-up work, such as a new commit on a reviewed pull request.

Everything else waits on its card or in **Needs attention** until a person acts. Read the result and respond to any requested decision before continuing. See [Work items](https://factory.mastra.ai/using/work-and-approvals) for the automation settings.

Start work yourself and leave **Auto-start runs** and **Auto-approve plans** off until you know the workflow.

## Order and priority

Factory doesn't rank, sequence, or filter incoming work. Each issue in a selected repository becomes its own independent card, and each is available to start as soon as it syncs. Order comes entirely from what you start and when.

GitHub epics and sub-issues aren't modeled. A sub-issue arrives as an ordinary issue card with no link to its parent, and its parent arrives the same way. Use your roadmap, epic, or milestone in GitHub to decide the order, then start the cards you want in that order. Treat the epic as your own tracking tool rather than something Factory acts on.

## Resolve missing items

To find a missing issue, check source access, your **Work Intake** selections, and the destination Factory. Linear projects also need organization routing to both a Factory and a board. For a missing PR, check GitHub access and the linked repository instead of personal issue subscriptions.

Read source errors and reconnect expired authorization before waiting for another sync. Use [Troubleshooting](https://factory.mastra.ai/troubleshooting) if the item still doesn't arrive.
