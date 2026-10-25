---
title: "Coding Agent Connection"
subtitle: "Connect any coding agent that supports MCP to an 8090 Software Factory project to pull Work Orders and update them from your editor."
authors: []
published_date: null
source_url: https://docs.8090.ai/connections/connect-coding-agent
origin: llms-txt
llms_txt: https://docs.8090.ai/llms.txt
section: "Docs / Connections"
fetched: 2026-10-25T18:13:39Z
---

# Coding Agent Connection (/connections/connect-coding-agent)

8090 Software Factory runs a Model Context Protocol (MCP) server, so your coding agent can pull Work Orders, read the Requirements, Blueprints, and Knowledge Base behind them, and post status back, all from your editor or terminal.

The server also gives your agent the project's skills, feedback and themes, comments, version history, automations, and your own past agent conversations in the project.

Any coding agent that supports MCP can connect. Teams use it from Cursor, Claude Code, Codex, Windsurf, VS Code with GitHub Copilot, Pi, Factory.ai, OpenCode, and others.

## Get your connection details [#get-your-connection-details]

**Coding Agent** in Settings fills in your project and generates a ready-to-paste configuration for your agent. The same guide is also available from the **MCP Setup** dialog on Work Orders. Both have tabs for **Cursor**, **Claude Code**, **Claude Desktop**, and **Codex**, plus **Other** with a generic JSON configuration that most other agents accept.

  
    ### Open the setup guide [#open-the-setup-guide]

    Open a project's **Settings**, then **Connections**, then **Coding Agent**. You can also open **Work Orders** and select **MCP** in the toolbar.
  

  
    ### Pick your agent [#pick-your-agent]

    Select your coding agent's tab to get its configuration, with your project ID and server name already filled in. If your agent has no tab, open **Other** for the generic JSON, or use the connection details below.
  

Every connection points at the same server:

| Setting         | Value                                                                         |
| --------------- | ----------------------------------------------------------------------------- |
| Server URL      | `https://api.factory.8090.dev/v2/mcp`                                         |
| Server name     | `software-factory-<project slug>`, for example `software-factory-ledger-plus` |
| Required header | `X-Sofa-Mcp-Project-Id: <your project id>`                                    |
| Authentication  | Browser sign-in (OAuth)                                                       |

The `X-Sofa-Mcp-Project-Id` header connects your agent to one project. Copy the server name and project ID from the setup guide rather than typing them.

## Set up your agent [#set-up-your-agent]

**Copy the exact config from the setup guide**
  The snippets below show the shape of each configuration. Copy the exact
  version, with your project ID filled in, from **Settings → Connections → Coding Agent** or the **MCP Setup** dialog.

### Cursor [#cursor]

Open or create `.cursor/mcp.json` in your project, or merge into your user-level MCP config, then reload Cursor:

```json
{
  "mcpServers": {
    "software-factory-<project slug>": {
      "type": "http",
      "url": "https://api.factory.8090.dev/v2/mcp?sf_project=<your project id>",
      "headers": { "X-Sofa-Mcp-Project-Id": "<your project id>" }
    }
  }
}
```

### Claude Code [#claude-code]

Run these commands in your terminal. The first removes any earlier entry with the same name. The second adds the server for your user, so it is available in every repository you open with Claude Code:

```bash
claude mcp remove software-factory-<project slug> -s user || true
claude mcp add --transport http --scope user software-factory-<project slug> \
  https://api.factory.8090.dev/v2/mcp \
  --header "X-Sofa-Mcp-Project-Id: <your project id>"
```

Then run `claude`, use `/mcp`, select the server, and choose **Authenticate**.

### Claude Desktop [#claude-desktop]

Start a Code session in Claude Desktop, open its terminal, and run the commands from the **Claude Desktop** tab. They are the same as the Claude Code commands. Then run `/mcp` in the Code session, select the server, and choose **Authenticate**.

### Codex [#codex]

Copy the script from the **Codex** tab and run it. It removes any earlier entry, adds the server, and adds the project header to `~/.codex/config.toml`. Complete the browser sign-in, and restart Codex if it was already running.

### Any other agent [#any-other-agent]

Use the JSON from the **Other** tab in your agent's MCP configuration, then reload the agent. Most agents, including Windsurf, Pi, and Factory.ai, use an `mcpServers` format like this one. Some use their own format. For example, VS Code's `mcp.json` uses a `servers` key, and OpenCode has its own schema. For those, enter the same server URL and `X-Sofa-Mcp-Project-Id` header in the format your agent expects.

## Sign in [#sign-in]

The first time your agent connects, it opens a browser window to sign in to 8090 Software Factory. Complete the sign-in and the 8090 Software Factory tools become available to the agent. In Claude Code and Claude Desktop, this is the **Authenticate** step under `/mcp`. In Codex, complete the browser sign-in after you run the script.

## Confirmations [#confirmations]

8090 Software Factory asks you to confirm before your agent does any of these:

* Deletes a Work Order, Requirement, Blueprint, Knowledge Base item, skill, feedback item, or theme.
* Creates, edits, or deletes an automation.

Your agent shows the confirmation, for example asking whether to delete a specific Work Order, and the action runs only if you accept. If your agent can't show these confirmations, these actions aren't available to it. Make those changes in 8090 Software Factory instead.

## Pull and run a Work Order [#pull-and-run-a-work-order]

Once connected, hand work to your agent in plain language, for example "get my next Work Order from 8090 Software Factory." A typical loop:

  
    ### Find the work [#find-the-work]

    The agent lists your Work Orders, filtered to you as the assignee.
  

  
    ### Read the full context [#read-the-full-context]

    It reads the Work Order, then the Requirements and Blueprints linked to it.
  

  
    ### Start and implement [#start-and-implement]

    It marks the Work Order **In Progress** and implements the change in your repository.
  

  
    ### Link the pull request [#link-the-pull-request]

    Ask the agent to link its pull request to the Work Order, by URL (a GitHub pull request or a GitLab merge request) or, on GitHub, by number. A pull request also links on its own when its title or description includes the Work Order ID, such as `WO-123`, so you can ask the agent to include the ID when it opens the pull request. Either way, the repository must be connected to the project in [Codebase Connection](/codebase/overview).

    The Work Order then shows the pull request and its status (**Open**, **Draft**, **Merged**, or **Closed**) in its **Development** section and in your Work Order views.
  

  
    ### Hand it back [#hand-it-back]

    When the change is ready, it marks the Work Order **In Review** for a teammate to pick up.
  

For direct REST access to the same data, see the [API reference](/api-reference). To learn how Work Orders are created and sequenced, see [Work Orders](/modules/work-orders).
