---
title: "Work Orders"
subtitle: "Create structured, traceable implementation tasks grounded in requirements and blueprints."
authors: []
published_date: null
source_url: https://docs.8090.ai/modules/work-orders
origin: llms-txt
llms_txt: https://docs.8090.ai/llms.txt
section: "Docs / Modules"
fetched: 2026-10-25T18:13:39Z
---

# Work Orders (/modules/work-orders)

Work Orders are structured, traceable tasks that move the system toward the target state defined in your requirements and Blueprints. Each Work Order brings together everything a contributor needs to do the work:

| Part              | What it provides                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| **Core metadata** | ID, title, assignee, parent, phase, status, priority, type, and labels                            |
| **Description**   | Purpose, acceptance criteria, and out-of-scope boundaries                                         |
| **Context**       | Links to the Requirements, Blueprints, Knowledge Base items, feedback, and themes behind the work |
| **Dependencies**  | The work orders it is blocked by or is blocking                                                   |
| **Development**   | Linked pull requests or merge requests and their state                                            |
| **Activity**      | A chronological history of changes, comments, and attachments                                     |

## Getting started [#getting-started]

  
    ### Configure Work Order settings [#configure-work-order-settings]

    Open **Settings → Modules → Work Orders**. It has three sections:

    * **Phase Schedule**: add phases, set their dates and length, and see which phase is **Current**, **Planned**, or **Completed**.
    * **Labels**: create, edit, archive, and delete labels. Work orders, feedback items, and themes share the same labels.
    * **Statuses**: add custom statuses alongside the built-in ones. See [Statuses](#statuses).

    You need Editor access to Work Orders to change these settings.

    To change how the agent writes work orders, such as the sections each description should have, edit the project's **Work Orders Writing Rules** [skill](/modules/skills). Each new project starts this skill from the preset templates listed under **Settings → Organization → Work Order Templates**.
  

  
    ### Create your first Work Orders [#create-your-first-work-orders]

    There are two main approaches.

    
      
        #### Extract from Blueprints [#extract-from-blueprints]

        * Ask the agent to run the **Extract Work Orders** skill. On an empty Work Orders page, **Chat with Agent** adds this request to the agent chat for you to send.
        * The agent reads the relevant Blueprints and Requirements, follows your writing rules, and proposes Work Orders for you to review.
      

      
        #### Create manually [#create-manually]

        * Select **+ Work Order*&#x2A; in the toolbar. To start with a group's value already filled in, such as its status, phase, or assignee, select &#x2A;*+** on that group's header instead.
        * Fill in the **Create New Work Order** form and select **Create Work Order**. Only the title is required, and the assignee defaults to you.
        * If you close the form without creating the work order, your draft is saved in this browser and comes back the next time you open the form. **Cancel** discards it.
      
    

    New Work Orders appear in the Work Orders views, where you can search, filter, and open them.
  

  
    ### Plan phases and execution order [#plan-phases-and-execution-order]

    * Set each work order's **Phase** from its detail page or the table.
    * Group by **Phase** to see each phase's work together.
    * Ask the agent to use **Phase Planning** to propose phases for work orders that have none.
    * Drag work orders to set their order within a phase. See [Drag and drop](#drag-and-drop).

    This becomes the core planning loop: create or extract Work Orders, place them into phases, and order them so the team knows what comes next.
  

## Work order details [#work-order-details]

Open a work order to see its description, **Child Work Orders**, **Agents**, and **Activity**. In **Activity**, select a comment to reply in its thread. A thread shows the first comment and its latest reply. Select **Show *N* earlier replies** to see the rest.

The **Agents** section lists the agent chats that worked on the work order, with who started each one and when it was last active. Everyone who can open the work order sees these titles, but you can open only your own chats. Select **Spawn Agent** to start a new chat about the work order in the agent panel. In **Activity**, changes the agent made link back to the chat that made them.

The fields beside it are:

* **Assignee**: one person, or **No Assignee**.
* **Parent**: the work order this one sits under.
* **Phase** and **Status**.
* **Priority**: **No Priority**, **Urgent**, **High**, **Medium**, or **Low**.
* **Type**: **Build**, **Fix**, **Requirements**, **Blueprint**, **Knowledge Base**, or **Other**.
* **Labels**.
* **Context**: links to Knowledge Base items, Requirements, Blueprints, Feedback, and Themes.
* **Dependencies**: the work orders this one is **Blocked by** or **Blocking**.
* **Development**: linked pull requests. See [Pull requests](#pull-requests).

## Statuses [#statuses]

Every status belongs to one of five categories. The built-in statuses are:

| Category      | Built-in statuses      |
| ------------- | ---------------------- |
| **Backlog**   | Backlog                |
| **Unstarted** | Blocked, Ready         |
| **Started**   | In Progress, In Review |
| **Completed** | Completed              |
| **Canceled**  | Canceled               |

You can add a custom status in two ways:

* In the status picker on a work order or in the create form, type a new name, select the **Create** option, then pick its category.
* In **Settings → Modules → Work Orders → Statuses*&#x2A;, select &#x2A;*+** next to a category.

Pick the category carefully, because you can't change it later. To edit, reorder, or delete custom statuses, open **Settings → Modules → Work Orders → Statuses**. You can also get there from **Manage statuses** at the bottom of the status picker on a work order's detail page. Built-in statuses can't be changed.

When you delete a custom status that work orders still use, pick a replacement under **Move work orders to**, then select **Confirm & Delete**. Those work orders move to the replacement status.

## Pull requests [#pull-requests]

The **Development** section on a work order links it to GitHub pull requests or GitLab merge requests. It needs a connected codebase. See [Codebase Connection](/codebase/overview).

* Select the gear in **Development**, search for a pull request by title, description, or number, and select it to link it. Select it again to unlink it.
* A pull request links itself when its title or description mentions the work order ID, such as `WO-123`.
* The agent, and coding agents connected through MCP, can link a pull request by its URL or number.

Each linked pull request shows its state as **Open**, **Draft**, **Merged**, or **Closed**. The state icon appears next to the work order in the Table, Board, and Roadmap views. When a work order has several pull requests, hover the icon to see each one's state.

## Views [#views]

Open **Display Settings** in the toolbar to choose a **View**, a **Grouping**, and a **Sort**, and to turn **Show child work orders** on or off.

| View        | Best for                                                |
| ----------- | ------------------------------------------------------- |
| **Table**   | Scanning and editing many work orders at once.          |
| **Board**   | Moving work across columns, such as statuses or phases. |
| **Roadmap** | Seeing work orders on a timeline by phase.              |

* **Grouping** options are **Phase**, **Status**, **Priority**, **Assignee**, **Blueprint**, and **Labels**, in every view.
* **Sort** options are **Manual**, **Name**, **Type**, **Phase**, **Status**, **Priority**, **Assignee**, **Created Date**, and **Last Modified Date**. You can add a second sort level.
* **Show child work orders** is on by default. Turn it off to hide work orders that have a parent.

### Roadmap [#roadmap]

The Roadmap shows each work order as a bar across its phase's dates. Phases get their dates in **Settings → Modules → Work Orders → Phase Schedule**, and a work order whose phase has no dates doesn't get a bar.

* **Expand Timeline** widens the timeline. **Restore Split View** brings back the list beside it.
* **Zoom out** and **Zoom in** change the scale. Select the percentage to reset it to 100%.
* **Today** jumps to the current date.

## Saved Views [#saved-views]

A saved view stores your view, grouping, sort, filters, and search so the team can come back to them.

* Select **Saved Views** (the bookmark) in the toolbar, then **Save Current View**, and name it.
* Select a saved view to apply it. The list shows who created each view, and **Search views or people** finds a view by its name or creator.
* Hover a view and select the pin to keep it under **Pinned** at the top of your list. Pins are yours alone and don't change anyone else's list.
* A view's **More** menu has **Rename**, **Duplicate**, **Copy Link**, and **Delete**. **Duplicate** makes a copy that you own, named with "copy" at the end.
* While a view is applied, its name appears in the toolbar. A dot means you changed it since it was saved. Select the name for **Save Changes**, **Reset to Saved**, or **Save as New View**. Select **Clear View** (the ×) to stop using it.

Everyone in the project sees the same saved views, and anyone who can open the project can save one. Only the person who created a view can save changes to it or rename it. They or a project Owner can delete it.

## Labels, filters, and search [#labels-filters-and-search]

Labels are shared by work orders, feedback items, and themes. Add them from a work order's **Labels** field, the create form, or the table. Typing a name that doesn't exist yet creates the label. Manage the full list in **Settings → Modules → Work Orders → Labels**.

Select **Filter** in the toolbar to narrow the list by **Status**, **Phase**, **Assignee**, **Priority**, **Type**, **Relation**, **Blueprint**, **Requirements**, **Knowledge Base**, or **Labels**. **Relation** filters by structure, such as work orders that have a parent, have children, are blocked, or are blocking others. Besides specific phases, the **Phase** filter offers **Current phase**, **Previous phase**, **Next phase**, **All past phases**, and **All upcoming phases**. They follow the [phase schedule](#getting-started), so a filter or saved view that uses them stays current as phases start and end. Use **Search** to find work orders by title or ID, such as `WO-123`.

## Drag and drop [#drag-and-drop]

You can drag work orders in the Table, Board, and Roadmap views.

* **Reorder within a group** by dragging a work order up or down. This only works with the **Manual** sort.
* **Move to another group** by dropping a work order on a different group. This works with any sort and changes the field you grouped by, such as the status, phase, assignee, or priority. With **Labels** grouping, the old label is replaced by the new one. With **Blueprint** grouping, the work order's blueprint link moves to the new blueprint.

While you drag, hold the work order near the edge of the view to scroll toward groups that are off screen. Press `Esc` to cancel the drag.

## MCP connections [#mcp-connections]

8090 Software Factory connects to coding agents and other development tools through the Model Context Protocol (MCP). Developers can work with Work Orders from their own development environment instead of switching between planning and coding.

### What MCP enables [#what-mcp-enables]

Connected development tools get secure, project-scoped access for:

* Listing Work Orders assigned to the developer
* Reading a work order's description and linked context
* Updating status, such as moving a task to **In Review**
* Linking the pull request that implements a work order

### Connect your development environment [#connect-your-development-environment]

  
    ### Open MCP setup [#open-mcp-setup]

    Open **Settings → Connections → Coding Agent**, or in the Work Orders toolbar select **MCP**.
  

  
    ### Configure your coding agent [#configure-your-coding-agent]

    In **MCP Setup**, choose your agent's tab and follow its instructions. Some agents offer a quick install. Others give you commands or JSON to add to their configuration. You finish the connection by signing in through your browser.
  

  
    ### Finish setup [#finish-setup]

    Select **Completed** to close the dialog.
  

8090 Software Factory tools become available after your coding agent loads the MCP configuration. For setup details per agent, see [Coding Agent Connection](/connections/connect-coding-agent).

### Work with 8090 Software Factory through MCP [#work-with-8090-software-factory-through-mcp]

After connecting, developers can:

* Find the Work Orders assigned to them that are **Ready**.
* Search Requirements, Blueprints, and Knowledge Base files for more context.
* Update a Work Order's status as development progresses.

Changes appear in 8090 Software Factory right away, so the project plan stays current.

## Agent capabilities [#agent-capabilities]

The agent can create, edit, and delete Work Orders, proposing titles, descriptions, assignees, statuses, phases, and labels. It can update many Work Orders in one request, for example moving a set of them to Phase 2 and setting them to **Ready**. It can also add phases, labels, and custom statuses.

Built-in skills for Work Orders include **Extract Work Orders**, **Phase Planning**, **Review Current Phase**, and **Duplication Check**.

## When blueprints change [#when-blueprints-change]

Work Orders don't update themselves when the Blueprints behind them change. After a significant Blueprint change, ask the agent to review the affected Work Orders, or run **Extract Work Orders** again for the changed Blueprints.

## Best practices [#best-practices]

* Set up the phase schedule, labels, and statuses in **Settings → Modules → Work Orders**, and keep the **Work Orders Writing Rules** skill current. Together they are the contract between Blueprints and execution.
* Ground every task in upstream Requirements or Blueprints by adding links from the **Context** section's search control.
* Include the sections your writing rules call for. By default these are Summary, In Scope, Out of Scope, Related Requirements, and Relevant Blueprint References.
* Link the pull request that delivers each work order so reviewers can see its state from the plan.
* Use agent actions for extraction, bulk updates, and phase planning while reserving judgment calls for people.
* Review Work Orders after Blueprint changes so drift does not accumulate.

[Learn about Feedback](/modules/feedback).
