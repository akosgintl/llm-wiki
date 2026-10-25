---
title: "Review items"
subtitle: "Start a PR review, respond to findings, and understand re-review and completion in Factory."
authors: []
published_date: null
source_url: https://factory.mastra.ai/using/reviews.md
origin: llms-txt
llms_txt: https://factory.mastra.ai/llms.txt
section: "Docs / Core concepts"
fetched: 2026-10-25T18:10:21Z
---

# Review items

Use **Review** to follow a pull request through agent review and human assessment. A PR's Review card has its own session, even when Factory created the PR from an existing Work item.

## Start and inspect a review

1. Open **Review** and find the PR by title or source number.
2. Check its GitHub link, base branch, and current changes.
3. Select **Review** if the card is waiting, then open the session.
4. Inspect findings, tool output, and any tests alongside the actual diff.

Factory brings pull requests from your linked repository into **Review**. If a PR is missing, check that you've linked the correct repository and that your GitHub connection is working.

When a review run completes, the agent has finished its review. Merging the PR and completing the original issue are separate steps.

## Respond to feedback

Request concrete changes with the affected behavior and expected outcome. For PRs authored by Factory, changes-requested review feedback can reach the authoring Work session.

After another push, inspect the updated files and checks. Use **Re-review** on an eligible card for another pass. Factory can supersede an active review when a newer pass starts.

## Finish or close a review

| Action in GitHub                   | Review card                 | Original Work item                                                             |
| ---------------------------------- | --------------------------- | ------------------------------------------------------------------------------ |
| Merge the PR                       | Moves to Done.              | Assesses whether the task is complete. A task can span multiple pull requests. |
| Close without merging              | Can move to Canceled.       | Still needs a decision about the underlying task.                              |
| Push further changes to an open PR | May require another review. | Continues implementation or follow-up as appropriate.                          |

Make the merge decision through your repository's normal human review process. Check acceptance criteria and required checks before merging. Use [Work items](https://factory.mastra.ai/using/work-and-approvals) when the linked issue closes.

## Related

- [Create your first pull request](https://factory.mastra.ai/)
- [GitHub](https://factory.mastra.ai/configure/github)
- [Troubleshooting](https://factory.mastra.ai/troubleshooting)
