---
title: "Sessions"
subtitle: "Find work needing attention, inspect an agent session, and collaborate through comments and Slack threads."
authors: []
published_date: null
source_url: https://factory.mastra.ai/using/sessions.md
origin: llms-txt
llms_txt: https://factory.mastra.ai/llms.txt
section: "Docs / Core concepts"
fetched: 2026-10-25T18:10:21Z
---

# Sessions

A session contains the agent conversation and workspace for a task. Open it from its card to inspect decisions, commands, files, and changes before deciding what to do next.

## Find the work that needs you

Open **Overview** to see Factory activity, including work waiting on a decision or reporting a problem. To find a specific item, search by issue title, issue number, or session name.

Open the card and check its status and linked issue or pull request. You may need to start a waiting run or accept a task before work can continue. If a plan is ready, review it before approving implementation. See [Work items](https://factory.mastra.ai/using/work-and-approvals) for details.

## Inspect and continue a session

Select **Open session** from a card. Read the latest agent result and tool output, then use the workspace's files and changes views to inspect the repository.

| What you see               | What to check                                                               |
| -------------------------- | --------------------------------------------------------------------------- |
| A question                 | Supply the missing requirement or repository context.                       |
| A plan                     | Confirm scope, files, checks, and the intended deliverable before approval. |
| A failed command           | Read the error, working directory, and setup command before retrying.       |
| A completed implementation | Review the diff and checks, then open the PR source link.                   |
| A completed review         | Read the findings against the current PR revision.                          |

Send the agent a message in the session with a specific next step, such as investigating a failed test. Use the existing session to follow a run already in progress.

## Keep discussion with the work

Discuss the work and mention teammates in the card's comments. Open the session to follow the agent's progress. Use the card's actions to accept a task. Respond to plan or tool approval requests in the session.

When work starts in [Slack](https://factory.mastra.ai/configure/slack), subsequent messages in the subscribed thread continue that session. A message beginning with `aside` is treated as discussion without triggering the normal agent reply. For a thread linked to a Work item, it can be recorded in the comment feed.

## Related

- [Work items](https://factory.mastra.ai/using/work-and-approvals)
- [Slack configuration](https://factory.mastra.ai/configure/slack)
- [Troubleshoot waiting or failed work](https://factory.mastra.ai/troubleshooting)
