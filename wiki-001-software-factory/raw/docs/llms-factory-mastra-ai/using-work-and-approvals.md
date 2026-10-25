---
title: "Work items"
subtitle: "Understand Work phases, acceptance, plan approval, automation, and changes from GitHub and Linear events."
authors: []
published_date: null
source_url: https://factory.mastra.ai/using/work-and-approvals.md
origin: llms-txt
llms_txt: https://factory.mastra.ai/llms.txt
section: "Docs / Core concepts"
fetched: 2026-10-25T18:10:21Z
---

# Work items

The **Work** board tracks an issue or task from [intake](https://factory.mastra.ai/using/intake) to completion. A pull request has a separate card on **Review**. Use the Work card to assess the task's outcome and the Review card to assess its PR.

## Understand the phases

| Phase    | What it means                                                                             | Your next action                                                         |
| -------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Intake   | An issue is available for work.                                                           | Read the issue and select **Investigate** or another appropriate action. |
| Triage   | The agent investigates, classifies the task, and identifies missing context or decisions. | Respond to any questions and accept proposed work when required.         |
| Planning | The agent prepares an approach and checks.                                                | Review or revise the plan.                                               |
| Building | The agent changes the repository and runs checks.                                         | Inspect progress, tool failures, and the patch.                          |
| Review   | The implementation is ready for review or follow-up.                                      | Inspect the associated PR and its Review card.                           |
| Done     | The task is complete.                                                                     | Confirm its acceptance criteria are met.                                 |
| Canceled | Work was abandoned or canceled.                                                           |                                                                          |

These are the built-in phases. A customized server can install additional [boards and rules](https://factory.mastra.ai/configure/boards-and-rules).

## Make the right decision

| Decision             | What it authorizes                                                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Start a proposed run | Run an investigation, review, or follow-up that was waiting on its card.                                                                                |
| Accept a task        | Allow a non-bug task to enter planning or building. **Accept** uses the suggested action. The menu offers **Accept and plan** and **Accept and build**. |
| Approve a plan       | Continue with the implementation described in that plan.                                                                                                |
| Merge a PR           | Integrate the reviewed branch through the repository's merge process.                                                                                   |

A non-bug item needs recorded human acceptance before it enters planning or building. The built-in policy checks that acceptance even when the item has moved through another intermediate phase.

The built-in Planning phase writes a plan in the session, then requests a transition to Building with `factory_transition_work_item`. Review the plan before approving that tool request. This is separate from the interactive `submit_plan` approval flow.

**Build** starts implementation directly. Use the guided [first-change tutorial](https://factory.mastra.ai/) when you want to practice plan review before implementation.

## Choose automation settings

The board exposes two controls:

- **Auto-start runs** lets Factory start eligible runs from new work and source events. When off, those runs wait for a person on their card. You can start runs and move cards manually with either setting.
- **Auto-approve plans** lets Factory answer approval requests from `submit_plan`. When off, those requests wait for your response and can appear in **Needs attention**. This setting doesn't approve stage-transition requests.

Keep both controls off while learning the workflow. With both off, Factory never starts agent work or spends model tokens on its own. Every run waits for a person to start it, and the **Overview** page and each session's transcript show what happened. With automation enabled, eligibility depends on the task's policy and whether its source is trusted.

The default GitHub rules allow an automatic initial run only if the issue was created after the Factory and the author has write or admin access to the repository. Start other issues manually.

## Understand source events

The table describes built-in behavior. Event delivery and reconciliation are asynchronous.

| Source event                                    | Result                                                                                                                                                                   |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| GitHub issue or PR arrives                      | Issues appear in Intake on the Work board, and pull requests appear in Intake on the Review board. Eligibility for automatic runs depends on source metadata and policy. |
| GitHub issue closes as completed                | Its active Work card moves to Done.                                                                                                                                      |
| GitHub issue closes as not planned or duplicate | Its active Work card moves to Canceled.                                                                                                                                  |
| Linear issue becomes completed or canceled      | Its active Work card moves to Done or Canceled, respectively.                                                                                                            |
| PR merges                                       | Its Review card moves to Done. Prompts the originating Work session to assess completion before marking the task Done.                                                   |
| PR closes without merging                       | Its Review card can move to Canceled. The original Work item tracks completion of the task, not the PR.                                                                  |
| A reviewed PR receives new work                 | A later review may be needed. Inspect the card and use **Re-review** when available.                                                                                     |

## Related

- [Review items](https://factory.mastra.ai/using/reviews)
- [Sessions](https://factory.mastra.ai/using/sessions)
- [Troubleshoot waiting or failed work](https://factory.mastra.ai/troubleshooting)
