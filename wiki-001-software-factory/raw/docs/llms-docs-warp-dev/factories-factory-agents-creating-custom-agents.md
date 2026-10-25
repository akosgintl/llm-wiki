---
title: "Creating custom agents"
subtitle: "Create a custom factory agent, add skills, and configure how the foreman dispatches it."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/factory-agents/creating-custom-agents/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Creating custom agents

Create a custom factory agent, add skills, and configure how the foreman dispatches it.

Add a custom agent for work that needs its own instructions, configuration, and runs. For example, create a documentation agent to update reference pages after code changes.

## Prerequisites

-   [Editor access to this factory, or team or workspace admin access](https://docs.warp.dev/factories/infrastructure-and-security/#factory-roles-and-permissions).
-   An existing factory. Follow the [Warp Factories quickstart](https://docs.warp.dev/factories/quickstart/) to create one.

## Create an agent in the web app

For a Warp-managed factory, create the agent in the [Warp Factories web app](https://platform.warp.dev). For a GitHub-backed factory, use [definition files](#define-an-agent-in-code) instead.

1.  In the web app sidebar, click your factory to expand it, then click **Agents**.
2.  Click **New**, then **Custom agent**.
3.  Enter an agent name and a description of its responsibilities.
4.  Under “Agent resources”, choose the agent’s [harness, model, host, and runner](https://docs.warp.dev/factories/factory-agents/configuration/) as needed. Add [MCP servers](https://docs.warp.dev/platform/mcp/) and [secrets](https://docs.warp.dev/platform/secrets/) for its tools.
5.  Under “Agent prompt”, enter the agent’s instructions.
6.  In the top-right corner, click **Save**.

The new agent appears on the factory’s **Agents** page. Agent names can’t be changed after creation.

## Define an agent in code

For a GitHub-backed factory, add `agents/<name>/agent.md` to the factory’s definition repository, replacing `<name>` with the agent’s directory name. Define its instructions and configuration using the [`agent.md` configuration keys](https://docs.warp.dev/factories/factory-as-code/#agentsnameagentmd). Follow your repository’s pull request process to apply the change.

## Add skills

Custom agents have no built-in skills. Add [factory skills](https://docs.warp.dev/factories/factory-skills/) where needed:

-   **One agent** - `agents/<name>/skills/`
-   **All agents** - `skills/`

## Dispatch a configured agent

The foreman uses `run_agents` to dispatch configured factory agents. It receives a list of available agents and their unique IDs (UIDs), then:

1.  The foreman chooses an agent from the available list.
2.  It sets `remote` to run the child in the cloud.
3.  For each child, it supplies the selected agent’s UID in `agent_run_configs[].agent_identity_uid`.

The `name` field only labels the child run. Unless overridden, the run uses the selected agent’s environment, runner, host, harness, and model.

You can start child agents without factory configuration through [multi-agent orchestration](https://docs.warp.dev/platform/orchestration/) from any Warp conversation. For scheduled or event-driven work, use [factory automations](https://docs.warp.dev/factories/automations/). The foreman coordinates the work they start.

## Related pages

-   [About factory agents](https://docs.warp.dev/factories/factory-agents/) - Understand default roles and human decision points
-   [Configuring factory agents](https://docs.warp.dev/factories/factory-agents/configuration/) - Edit instructions, models, harnesses, and tools
-   [Factory skills](https://docs.warp.dev/factories/factory-skills/)
-   [Factory automations](https://docs.warp.dev/factories/automations/)
-   [Definitions as code](https://docs.warp.dev/factories/factory-as-code/)
