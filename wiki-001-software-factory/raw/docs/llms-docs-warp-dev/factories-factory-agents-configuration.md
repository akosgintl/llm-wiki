---
title: "Configuring factory agents"
subtitle: "Configure a factory agent's instructions, tools, model, and harness, including authentication for Claude Code and Codex."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/factory-agents/configuration/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Configuring factory agents

Configure a factory agent's instructions, tools, model, and harness, including authentication for Claude Code and Codex.

Change how an existing factory agent works by editing its instructions, tools, and runtime in the [Warp Factories web app](https://platform.warp.dev) or its definition files.

## Prerequisites

-   [Editor access to this factory, or team or workspace admin access](https://docs.warp.dev/factories/infrastructure-and-security/#factory-roles-and-permissions).
-   An existing factory agent. See [About factory agents](https://docs.warp.dev/factories/factory-agents/) for the default roles, or [Creating custom agents](https://docs.warp.dev/factories/factory-agents/creating-custom-agents/) to add a role.

## Edit agent settings and instructions

For a Warp-managed factory, edit agent settings in the web app. For a GitHub-backed factory, settings are read-only in the web app; edit the [factory definition files](https://docs.warp.dev/factories/factory-as-code/) instead. See [Where the definition lives](https://docs.warp.dev/factories/factory-as-code/#where-the-definition-lives).

1.  In the web app sidebar, click your factory to expand it, then click **Agents**.
    
    ![The Agents page in the factory dashboard, listing a foreman agent and its four default agents: triage, spec, implement, and review.](https://docs.warp.dev/_astro/factory-agents-list.lvxXrd-B_Z1wz6CC.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    The Agents page lists a factory’s foreman and default agents.
    
2.  Click an agent to open its **Settings** tab.
    
    ![An Implement agent's Settings tab showing its description, MCPs, secrets, and Harness, Model, Host, and Runner dropdowns.](https://docs.warp.dev/_astro/factory-agent-edit.DW32ylsZ_Z2jETtV.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    The Settings tab contains the agent’s description and resources.
    
3.  Edit the agent description, harness, model, runner, host, [MCP servers](https://docs.warp.dev/platform/mcp/), or [secrets](https://docs.warp.dev/factories/secrets/).
    
4.  To change the agent’s instructions, click **Prompt** and edit the prompt.
    
5.  In the top-right corner, click **Save**.
    

## Choose models and harnesses per agent

Choose each agent’s model and harness in its settings. Supported harnesses include the Warp Agent, Claude Code, and Codex. A foreman using Claude Code or Codex can still dispatch other factory agents, whose runs are tracked as its children.

Third-party harnesses require a paid plan. On the Free plan, agents use the Warp Agent. See [Warp pricing](https://www.warp.dev/pricing) for plan details.

Default model IDs change over time, so choose based on what each agent has to do well:

| Agent | What to optimize for |
| --- | --- |
| Foreman | Orchestration, instruction following, and long-running conversations |
| Triage | Research, evidence gathering, and working with connected tools |
| Spec | Synthesizing requirements, technical reasoning, and precise writing |
| Implement | Coding strength, with a harness that fits your repositories and toolchain |
| Review | A different model or harness from the implement agent, so the two don’t share blind spots |

The model picker also includes custom routers from factories you can access. See [Agent model choice](https://docs.warp.dev/agents/inference/model-choice/), [Custom routers](https://docs.warp.dev/agents/inference/custom-routers/), and [Harnesses in the Automation Platform](https://docs.warp.dev/platform/harnesses/) for available options.

### Configuring a third-party harness

Change an agent’s harness to Claude Code or Codex to run it with that provider’s own coding tool.

1.  In the web app sidebar, click your factory to expand it, then click **Agents**.
    
2.  Click an agent to open its **Settings** tab.
    
3.  In the “Harness” dropdown, choose **Claude Code** or **Codex**. The “Auth” field appears for these harnesses.
    
4.  In the “Auth” field, choose a compatible, team-owned secret from the list or click **New auth secret** to create one.
    
    ![An Implement agent's Settings tab with Claude Code selected in the Harness dropdown and the Auth dropdown open, showing a saved credential and New auth secret.](https://docs.warp.dev/_astro/factory-agent-auth-secret.BBtyYaA6_1qt9YA.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    The Auth dropdown appears when a third-party harness is selected.
    
    Note
    
    -   Claude Code accepts an Anthropic API key, Anthropic Bedrock API key, or Anthropic Bedrock access key.
    -   Codex accepts an OpenAI API key.
    
    See [connecting Claude Code credentials](https://docs.warp.dev/platform/harnesses/authentication/#connecting-claude-code-credentials) and [connecting Codex credentials](https://docs.warp.dev/platform/harnesses/authentication/#connecting-codex-credentials) for how to obtain each key.
    
5.  In the “Model” dropdown, choose a model from that harness’s catalog.
    
6.  In the top-right corner, click **Save**.
    

With a Warp-managed factory, you can edit harness, auth, and model from the dashboard. A GitHub-backed factory sets them through [`agentDefaults.harness` or a per-agent `harness` override](https://docs.warp.dev/factories/factory-as-code/#agentdefaultsharness) in the definition files. For an example, see [`03-multi-harness`](https://github.com/warpdotdev/warp-factory-examples/tree/main/examples/03-multi-harness).

## Related pages

-   [About factory agents](https://docs.warp.dev/factories/factory-agents/) - Understand responsibilities and human decision points
-   [Creating custom agents](https://docs.warp.dev/factories/factory-agents/creating-custom-agents/)
-   [Factory skills](https://docs.warp.dev/factories/factory-skills/)
-   [Definitions as code](https://docs.warp.dev/factories/factory-as-code/)
