---
title: "Quickstart"
subtitle: "Set up your organization and first project, then take one feature from requirements to a work order your coding agent can build."
authors: []
published_date: null
source_url: https://docs.8090.ai/general/quickstart
origin: llms-txt
llms_txt: https://docs.8090.ai/llms.txt
section: "Docs / General"
fetched: 2026-10-25T18:13:39Z
---

# Quickstart (/general/quickstart)

## Complete your first workflow [#complete-your-first-workflow]

This guide walks you through a first run of 8090 Software Factory: create your organization and project, write requirements and blueprints with the Agent, generate work orders, and hand one to your coding agent.

  
    ### Create your organization [#create-your-organization]

    After you sign up and verify your email, 8090 Software Factory asks you to create or join an organization. If a teammate invited you, open the link in your invitation email instead. You join their organization and skip this step.

    To start a new organization, select **Create New Organization**. On the **Create Your Organization** page:

    * Enter an **Organization name**.
    * Optionally add teammates under **Invite teammates**. Each address adds one seat, and the invites go out after checkout.
    * Check the pricing summary. **Seats** shows the seat count and the price per seat, and **Due today** shows the monthly total. Extra usage is billed separately.
    * Select **Continue to Payment** and complete checkout in Stripe.

    You become the organization's admin. See [Organization Management](/administration/organizations) and [Usage & Billing](/administration/usage) for members, seats, and billing.
  

  
    ### Create your first project [#create-your-first-project]

    Next, the **Create Your First Project** page asks for a **Project Name** and an optional **Description**. Select **Create**.

    A project holds the context that defines your software, from requirements and blueprints to work orders and feedback. Your new project opens on its **Home** page, where you can start a chat with the Agent.
  

  
    ### Take the tour and open Quick Start [#take-the-tour-and-open-quick-start]

    The **Welcome to Software Factory** dialog offers a short demo video and a guided tour. Select **Take tour** for a quick walkthrough of where everything lives, or **Snooze** to see it again the next time you sign in.

    When the tour ends, the **Quick Start** checklist opens. It lists the setup steps in this guide, including **Invite your team** and **Install the Software Factory skill**. Most items check themselves off as you do the work, and you can check off any item yourself. Reopen the checklist from **Quick Start** in the left sidebar. It goes away once every item is done and you close it.

    Everything else is in the left sidebar too: **Home**, **Agents**, **Skills**, **Automations**, **Knowledge Base**, the **Requirements**, **Blueprints**, **Work Orders**, and **Feedback** modules, and **Settings**.
  

  
    ### Connect your repository (optional) [#connect-your-repository-optional]

    Connecting a codebase lets the Agent search and read your code while it writes requirements, blueprints, and work orders.

    * Open **Settings → Codebase** and connect GitHub or GitLab.
    * Add your repository or project and choose the branch to index.
    * Wait for indexing to finish before you ask the Agent about the code.

    See [Codebase Connection](/codebase/overview) for details.
  

  
    ### Add supporting knowledge (optional) [#add-supporting-knowledge-optional]

    Open **Knowledge Base** in the left sidebar and add research, designs, or specs. The Agent uses them as context when it writes requirements, blueprints, and work orders.

    See [Knowledge Base](/modules/knowledge-base) for details.
  

  
    ### Define your requirements [#define-your-requirements]

    Open **Requirements** in the left sidebar. Every project starts with six Product Overview documents: **Business Problem**, **Current State**, **Product Description**, **Personas**, **Success Metrics**, and **Technical Requirements**. You don't need to fill them in first. The Get Started workflow fills them in with you.

    While the **Feature Requirements** section is empty, a **Get Started** button appears under it. Select it to open the agent panel, where the Agent runs the Get Started workflow:

    * It asks whether you are importing an existing app or designing a new one. For an existing app, it reverse engineers your connected codebase. See [Reverse engineering](/opinions/reverse-engineering).
    * For a new app, it interviews you to fill in the Product Overview documents, then asks whether to define one feature first or cover every feature for your MVP.
    * It creates Feature Requirements documents. Each one gets a matching Feature Blueprint with the same title.

    You can also ask the Agent for anything directly. Open it with **Open Agent** at the top right of the page, or press `Cmd/Ctrl` + `L`.
  

  
    ### Write your blueprints [#write-your-blueprints]

    Open **Blueprints**. Your project already has three blueprint categories: **Containers**, **Components**, and **Feature Blueprints**.

    When your requirements are ready, the Get Started workflow offers to move on to blueprints. It asks what kind of app you are building and which stack you are targeting. Then it fills in Container blueprints for your core technology choices, Component blueprints for shared capabilities, and the Feature Blueprints that pair with your requirements. You can also open any blueprint and ask the Agent to draft or refine it.

    See the [Blueprint Writing Guide](/opinions/blueprint-writing-guide) for what makes a good blueprint.
  

  
    ### Generate work orders [#generate-work-orders]

    Open **Work Orders**. While the project has no work orders, the page offers **Create Work Order** and **Chat with Agent**. Select **Chat with Agent** to fill the prompt with the **Extract Work Orders** skill, then send it. The Agent turns your requirements and blueprints into work orders.

    If you are working through the Get Started workflow, it offers this step as well, then sorts the work orders into phases and asks who to assign them to.

    Review the work orders, adjust assignees, and organize them into phases. See [Work Orders](/modules/work-orders).
  

  
    ### Connect your coding agent [#connect-your-coding-agent]

    Coding agents such as Cursor, Claude Code, and Codex connect to 8090 Software Factory through the Model Context Protocol (MCP) to read work orders and update their status.

    * Open **Settings → Connections → Coding Agent**, or in **Work Orders** select **MCP** in the toolbar. Either one opens the setup guide.
    * Pick the tab for your agent (**Cursor**, **Claude Code**, **Claude Desktop**, **Codex**, or **Other**), copy the configuration, and follow the steps shown.
    * The first time your agent connects, sign in to 8090 Software Factory in your browser. You don't need an API key.
    * Ask your coding agent for the next work order. 8090 Software Factory tells the agent to move the work order to **In Progress** when it starts and to **In Review** when it finishes.

    To help your agent follow the same process every time, install the [8090 Software Factory agent skill](/opinions/agent-skill). The Quick Start item **Install the Software Factory skill** has a **Copy Prompt** button that copies the install instructions for your agent.

    See [Coding Agent Connection](/connections/connect-coding-agent) for each agent's setup.
  

## Next steps [#next-steps]

* **Keep documents in sync with your code.** Drift checks are opt-in. Add **Detect Code Drift** from the **Recommended** section of the **Automations** page to get comments on blueprints and their linked requirements when pushed code contradicts them. To review pull requests, turn on Drift Bot for a repository in **Settings → Codebase**. See [Automations](/modules/automations) and [Codebase Connection](/codebase/overview).
* **Invite your team.** Organization admins invite members from **Settings → Organization → Members** with **Invite Member**. See [Organization Management](/administration/organizations).
* **Build more features.** Add Feature Requirements documents, write their blueprints, and extract more work orders.
* **Collect feedback.** After you ship, bring customer reports into [Feedback](/modules/feedback) and group them into themes.

## Getting help [#getting-help]

* To report a bug or request a feature, select **Leave Feedback** in the user menu at the bottom of the left sidebar, or the feedback button next to it, and submit the **Send Feedback** dialog.
* Select **Contact Support** in the left sidebar to copy the support email address.
* Join the [Discord community](https://discord.com/invite/pEBerXdv2N).
* See [Support & Community](/resources/support-community) for more options.
