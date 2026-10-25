---
title: "Automations"
subtitle: "Run the project agent automatically on a trigger, with scoped permissions and explicit MCP Server access."
authors: []
published_date: null
source_url: https://docs.8090.ai/modules/automations
origin: llms-txt
llms_txt: https://docs.8090.ai/llms.txt
section: "Docs / Agents"
fetched: 2026-10-25T18:13:39Z
---

# Automations (/modules/automations)

An automation runs the project agent for you on a trigger. Instead of opening a chat and asking, you define the work once, and the agent does it whenever the right thing happens in your project or on a schedule.

Every automation runs as its **run-as user**, the person who created it. It acts with that person's permissions, and any MCP Servers you grant it come from that person's connections. Every run is a full agent conversation that the run-as user can open, read, and continue.

## What an automation contains [#what-an-automation-contains]

The automation builder has four sections:

| Section                | What it does                                                                           |
| ---------------------- | -------------------------------------------------------------------------------------- |
| **Triggers**           | One or more events, or a schedule, that start a run                                    |
| **Agent Instructions** | The prompt the agent follows on every run, and the model it uses (**Auto** by default) |
| **MCP Servers**        | Optional external services the automation may use                                      |
| **Restrictions**       | Optional limits on what the automation can create or edit                              |

## Authoring an automation [#authoring-an-automation]

There are three ways to create an automation:

* **Build it yourself.** On the Automations page, select **Create** to open the builder. Add triggers, write the prompt, pick a model, grant any MCP Servers, and set restrictions, then select **Create** to save.
* **Start from a recommended automation.** Select **Add** on a card in the **Recommended** catalog to open the builder already filled in. See [Recommended automations](#recommended-automations).
* **Ask the agent.** In web chat, describe the automation you want. The agent asks you to choose its triggers, restrictions, and MCP Servers instead of assuming them, then shows the finished automation for you to **Create** or **Cancel**.

The run-as user can edit or delete their automations. Anyone with Owner access to the project, including organization Admins, can also edit or delete any automation, but only the run-as user can change its model or MCP Servers.

You can also manage automations outside the app:

* The [REST API](/api-reference) has endpoints for automations. Each new automation needs a name, a prompt, and at least one trigger. Restrictions and MCP Servers are optional, and nothing is granted unless you include it.
* [Coding agents connected over MCP](/connections/connect-coding-agent) can list, read, create, edit, and delete automations. Your agent asks you to [confirm](/connections/connect-coding-agent#confirmations) before it creates, edits, or deletes one. Over MCP, you can only edit or delete automations you created, and you can't delete one added from the **Recommended** catalog.

## Triggers [#triggers]

A trigger decides when an automation runs. An automation can have several triggers, so it can respond to more than one kind of event. It can have only one **Scheduled** trigger.

Add triggers with **Add Trigger**. Event triggers are grouped by module, and **Code Push** and **Scheduled** have their own entries.

| Trigger                             | Runs when                                                        | Options                                                                      |
| ----------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Code Push**                       | Connected code is reindexed after a push                         | Specific repositories, or **Any connected codebase**                         |
| **Knowledge Base Document Created** | A Knowledge Base document is created. Uploaded files don't count | None                                                                         |
| **Knowledge Base Document Edited**  | A Knowledge Base document is saved with changes                  | None                                                                         |
| **Requirement Created**             | A requirement is created                                         | None                                                                         |
| **Requirement Edited**              | A requirement is saved with changes                              | None                                                                         |
| **Blueprint Created**               | A blueprint is created                                           | None                                                                         |
| **Blueprint Edited**                | A blueprint is saved with changes                                | None                                                                         |
| **Work Order Created**              | A work order is created                                          | None                                                                         |
| **Work Order Edited**               | A work order changes status or gets a label                      | **Status changed** to chosen statuses, or **Label added** for a chosen label |
| **Feedback Created**                | Feedback is submitted                                            | None                                                                         |
| **Scheduled**                       | A schedule comes due                                             | **Hourly**, **Daily**, **Weekly**, or a **Custom** cron expression           |

### Code Push [#code-push]

**Code Push** runs after 8090 Software Factory reindexes a push to a connected repository. Pick the repositories it should watch, or leave it on **Any connected codebase** to include every repository, even ones you connect later.

### Work Order Edited [#work-order-edited]

In **Add Trigger**, open **Work order** and choose one of these:

* **Status changed:** pick the statuses that start a run (Backlog, Ready, In Progress, In Review, Blocked, Completed, and Canceled), or **Any status**. If your project has custom statuses, the trigger treats each one as the main built-in status of its category: **Backlog**, **Ready** for Unstarted, **In Progress** for Started, **Completed**, or **Canceled**. A move that doesn't change that built-in status, such as from a custom Started status to **In Progress**, doesn't start a run.
* **Label added:** pick a label, or **Any Label**. This also runs when a work order is created with that label.

### Scheduled [#scheduled]

**Scheduled** runs the automation on a repeating schedule. Choose **Hourly**, **Daily**, or **Weekly**, or choose **Custom** and enter a cron expression.

Times you set with a preset are in your local time zone, and teammates see the same schedule converted to theirs. A **Custom** cron expression is in UTC.

### What a run receives [#what-a-run-receives]

Each run starts with a short note about what triggered it, followed by your prompt:

* **Created** triggers link to the new item.
* **Edited** triggers for requirements, blueprints, and Knowledge Base documents link to the changed item and give the time its new version was saved. They run once per saved version, not on every keystroke. To compare with the previous version, the agent can read the item's version history.
* **Work Order Edited** links to the work order and says what changed, such as the old and new status or the label that was added.
* **Code Push** lists the changed files.
* **Scheduled** runs get only your prompt.

## Recommended automations [#recommended-automations]

The **Recommended** catalog on the Automations page lists ready-made automations. Select **Add** to open the builder filled in from the template, including a model picked for the job. When you save it, you get a normal, enabled automation that you own and can edit like any other, except that it keeps the template's name. Cards you have added show **Open**.

When a newer version of a template you added is available, its card shows **Update**. Updating applies the new template but keeps your model and its settings, your MCP Servers, and whether the automation is on.

### What's in the catalog [#whats-in-the-catalog]

* **Detect Code Drift** runs on **Code Push**. It checks the changed files against the code linked to your blueprints. It leaves a drift comment on a blueprint wherever the code contradicts it, and on the feature's linked requirements document for each requirement the code contradicts.
* **Sync Blueprints and Requirements** runs on **Requirement Edited** and **Blueprint Edited**. It compares a feature's requirements with its linked blueprint and leaves drift comments on the blueprint.
* **Check Blueprint References** runs on **Blueprint Edited**. It finds the blueprints that depend on the changed one and leaves drift comments where they may have drifted.
* **Triage Feedback** runs on **Feedback Created**. It reads each item, matches it to a theme, and pulls out representative quotes.

The three drift automations can't create or edit Blueprints, Requirements, Work Orders, Feedback, or Themes, so they report drift as comments instead of changing your documents. Each comment shows the run-as user's name followed by "via" and the automation's name, for example "Dana via Detect Code Drift".

To check pull requests for drift instead, turn on [Drift Bot](/codebase/overview#drift-bot) for a repository in **Settings → Codebase**. Drift Bot is separate from automations and posts its findings on the pull request.

## Permissions and restrictions [#permissions-and-restrictions]

An automation always has the run-as user's permissions. Restrictions narrow what it can create or edit. They never give it more access than that person has.

In the **Restrictions** section, select **Add Restriction** and pick an area: **Knowledge Base**, **Requirements**, **Blueprints**, **Work Orders**, **Feedback**, **Themes**, or **Comments**. Each restriction has one of two levels:

| Level                     | Effect                                                                          |
| ------------------------- | ------------------------------------------------------------------------------- |
| **Cannot create**         | The automation can still edit existing items in that area.                      |
| **Cannot edit or create** | The area is read-only for the automation. New restrictions start at this level. |

A restriction covers only the area you pick. For example, an automation with every area restricted except Knowledge Base can still change Knowledge Base documents. Two areas work a little differently:

* **Comments:** **Cannot create** stops the automation from adding comments. **Cannot edit or create** also stops it from resolving them.
* **Feedback** and **Themes** share permissions, so a restriction on one can also limit the other. For example, **Cannot create** on Feedback also stops the automation from creating themes.

A common pattern is to make every area read-only except Comments, so the automation can review your work and comment on it without changing any documents.

**Watch for self-triggering loops**
  If an automation can edit the same kind of item that triggers it, its own
  edits can trigger it again in a loop. The builder warns you when this can
  happen. To clear the warning, add a **Cannot edit or create** restriction on
  that area. This is why recommended automations such as **Check Blueprint
  References** leave comments instead of edits.

## MCP Servers [#mcp-servers]

Unlike chat, an automation doesn't get all of your connected MCP Servers. It can only use the servers you grant it. With no grants, it uses none.

1. Connect the server under **Settings → Connections → MCP Servers**. You can only grant servers that the run-as user has connected.
2. In the automation's **MCP Servers** section, select **Add MCP Server** and choose the server.
3. In the server's [tool permissions](/connections/mcp-servers#tool-permissions), set the tools the automation needs to **Allow**. Automations only use **Allow** tools, because no one is there to approve a tool during a run. Action tools start at **Confirm**.

For example, an automation that posts a summary to a team chat channel needs that chat server granted and its posting tool set to **Allow**.

## Model [#model]

Pick the model in **Agent Instructions**. **Auto**, the default, uses the default model that 8090 Software Factory sets for automations. You can choose a specific model instead and set its **Reasoning**, **Context**, and **Fast** options, the same way as in [agent chat](/agents/agent-chat#choose-a-model). Recommended automations come with a model already picked, which you can change.

## Run history [#run-history]

The run history lists each run with its trigger, scheduled time, status (such as **Completed** or **Failed**), and duration. Each automation also shows its total, successful, and failed runs for the last 30 days.

The run-as user can open any run, even one still in progress, and follow the agent's work in the agent panel. They can also reply to continue the conversation. A reply sent during a run waits until the run finishes. Replies use the run-as user's own permissions and connections, not the automation's restrictions and MCP Servers. Other people can see each run's status but can't open it.

Runs count toward the run-as user's usage limit, and a run fails once that limit is reached. See [Usage & Billing](/administration/usage).

**Disabling is safe**
  Turning an automation off stops future runs. A run already in progress
  finishes. Runs that were scheduled but hadn't started yet end as **Failed**.

## Recipes [#recipes]

These patterns come from automations running in real projects. Adapt the triggers, prompts, and restrictions to your own setup.

### Triage feedback the moment it arrives [#triage-feedback-the-moment-it-arrives]

* **Trigger:** **Feedback Created**.
* **Prompt:** read the new feedback item, match it to the right theme, and pull representative quotes.
* **Restrictions:** **Cannot edit or create** on Knowledge Base, Requirements, Blueprints, and Work Orders, so the automation works in feedback and themes without changing other documents.
* **MCP Servers:** none.

### Weekly release notes on a schedule [#weekly-release-notes-on-a-schedule]

* **Trigger:** **Scheduled**, with the **Custom** cron expression `0 13 * * 5` (Fridays at 13:00 UTC).
* **Prompt:** draft the next release notes, add a comment that mentions each workstream lead for review, and post a link in your team's chat channel asking for a review.
* **MCP Servers:** grant your chat MCP Server, and set its posting tool to **Allow** in your tool permissions.

### Plan a work order when it gets a label [#plan-a-work-order-when-it-gets-a-label]

* **Trigger:** **Work Order Edited** with **Label added**, set to one specific label.
* **Prompt:** read the labeled work order and the requirements, blueprints, and Knowledge Base documents linked to it, search the connected code, then comment on the work order with an implementation outline and mention its assignee.
* **Restrictions:** **Cannot edit or create** on Knowledge Base, Requirements, Blueprints, and Work Orders. Comments stay open, so the automation can post its outline, and the Work Orders restriction also clears the self-trigger warning.

### Keep blueprints honest [#keep-blueprints-honest]

* **Trigger:** **Blueprint Edited**.
* **Prompt:** find dependent blueprints and comment where they may have drifted.
* **Restrictions:** **Cannot edit or create** on Blueprints, Requirements, Work Orders, Feedback, and Themes, so the automation only leaves drift comments on those documents. This mirrors the recommended **Check Blueprint References**.

## Best practices [#best-practices]

* Give each automation a narrow job. One clear trigger and one clear prompt are easier to trust than a broad catch-all.
* Restrict the areas an automation only needs to read. Read-only areas prevent accidental edits and clear self-trigger warnings.
* Grant only the MCP Servers an automation needs, and set only the tools it uses to **Allow**.
* Start from a recommended automation when one fits. Add it, watch a few runs, then build your own when you need something the catalog doesn't cover.
* Read the run transcripts. They show exactly what the agent did and are the fastest way to tune a prompt.

Want to see how much your automations are running? [Review usage](/administration/usage).
