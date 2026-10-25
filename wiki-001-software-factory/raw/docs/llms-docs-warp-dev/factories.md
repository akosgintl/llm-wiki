---
title: "Warp Factories overview"
subtitle: "Warp Factories turns issues, tickets, and Slack messages into reviewed pull requests. Teams of cloud agents do the work, while people approve specs and merges."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Warp Factories overview

Warp Factories turns issues, tickets, and Slack messages into reviewed pull requests. Teams of cloud agents do the work, while people approve specs and merges.

A factory is a team of cloud agents connected to your repositories. It routes work from Slack, GitHub, Linear, or Jira through triage, planning, implementation, and review. The output, usually a pull request, is returned to the thread or issue where the work started.

[Open Warp Factories web app](https://platform.warp.dev)Sign in to your account and create or manage your team's factories.

[Read the Warp Factories quickstart](https://docs.warp.dev/factories/quickstart/)Follow setup instructions to connect repositories and send your first request.

## What a factory does

A factory can work through a backlog of tasks, fix defects reported in a support channel, or review incoming pull requests across several repositories.

![Introducing Warp Factories](https://i.ytimg.com/vi/0WBk4ai8y1A/sddefault.jpg)

An introduction to Warp Factories.

## The parts of a factory

### Work items

A work item is one request the factory acts on. This can be an issue, a support thread, a pull request, or a scheduled job. It keeps its source context from intake to handoff, however many agents contribute along the way.

### Foreman and factory agents

The foreman is the agent that coordinates a factory’s work and communicates with you. See [About factory agents](https://docs.warp.dev/factories/factory-agents/) for their roles, and [Configuring factory agents](https://docs.warp.dev/factories/factory-agents/configuration/) to change their models, harnesses, and instructions.

Setup gives the foreman the same handle as the factory, so `payments` is the factory and `@payments` reaches its foreman from Slack or Linear. See [Foreman name](https://docs.warp.dev/factories/factory-agents/#foreman-name).

### Stages and checkpoints

Factory agents handle different stages of the software development lifecycle. The default agents cover triage, planning, implementation, and review.

![A circular diagram of the software factory loop: triage, spec, implement, review, verify, ship, and monitor, with human review checkpoints for the spec, code, and product.](https://docs.warp.dev/_astro/factories-concept-loop.D5J0xtAi_PLdIR.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)

The software factory loop.

The foreman can skip unnecessary stages or send work back for revisions. Spec approval is part of the foreman’s editable instructions, not a repository permission. The factory never merges on your behalf. Repository permissions and branch protection control approval and merge access. See [How Warp Factories work](https://docs.warp.dev/factories/how-factories-work/).

### Factory definition

A factory’s repositories, agents, automations, runners, skills, and MCP servers are declared in definition files, either managed by Warp or stored in a GitHub repository your team owns. Changes to a GitHub-backed factory go through pull request review like any other code. See [definitions as code](https://docs.warp.dev/factories/factory-as-code/).

### Work sources

Connect [Slack](https://docs.warp.dev/factories/integrations/slack/), [Microsoft Teams](https://docs.warp.dev/factories/integrations/teams/), [GitHub](https://docs.warp.dev/factories/integrations/github/), [GitLab](https://docs.warp.dev/factories/integrations/gitlab/), [Azure DevOps](https://docs.warp.dev/factories/integrations/azure-devops/), [Linear](https://docs.warp.dev/factories/integrations/linear/), and [Jira](https://docs.warp.dev/factories/integrations/jira/) through [factory integrations](https://docs.warp.dev/factories/connect-your-factory/). Results return to the thread, issue, or pull request where work began. Use [custom webhooks](https://docs.warp.dev/factories/webhooks/) or [factory endpoints](https://docs.warp.dev/factories/factory-api/) for other systems, and [automations](https://docs.warp.dev/factories/automations/) for scheduled work.

The [Factory MCP](https://docs.warp.dev/factories/factory-mcp/) lets a local coding agent send work to a factory, take it over locally, and hand it back.

### Execution

Every agent run in a factory is an ordinary [cloud agent run](https://docs.warp.dev/platform/) on the Automation Platform. Runs execute on Warp-hosted compute by default; Enterprise teams can keep checkout and execution on their own infrastructure with [managed self-hosting](https://docs.warp.dev/factories/self-hosting/). See [infrastructure and security](https://docs.warp.dev/factories/infrastructure-and-security/) for runners, inference, and credential boundaries.

### Evaluate and improve factory work

Use the [factory dashboard](https://docs.warp.dev/factories/factory-dashboard/) to inspect PR activity, autonomy, cycle time, and cost. To evaluate and improve the work:

-   **[Scorers](https://docs.warp.dev/factories/measure-and-improve/scorers/)** - Classify runs against your criteria.
-   **[Benchmarks](https://docs.warp.dev/factories/benchmarks/)** - Compare configurations on the same tasks.
-   **[Self-improvement](https://docs.warp.dev/factories/measure-and-improve/self-improvement/)** - Propose changes for review.

See [measure and improve](https://docs.warp.dev/factories/measure-and-improve/) for definitions and limitations.

## Sizing a factory

Group the repositories that ship together into one factory, and keep separate products in separate factories. For example:

-   One factory for your main application
-   One factory for your marketing site
-   One factory for your data pipelines

Don’t split the same repositories across factories by team or task, such as frontend and platform. Add [custom agents](https://docs.warp.dev/factories/factory-agents/creating-custom-agents/) and [skills](https://docs.warp.dev/factories/factory-skills/) to specialize instead.

## Related pages

-   [Warp Factories quickstart](https://docs.warp.dev/factories/quickstart/) - Create a factory and send its first work item.
-   [How Warp Factories work](https://docs.warp.dev/factories/how-factories-work/) - The work-item lifecycle, stage by stage.
-   [About factory agents](https://docs.warp.dev/factories/factory-agents/) - Understand default agent roles
-   [Configuring factory agents](https://docs.warp.dev/factories/factory-agents/configuration/) - Choose models, harnesses, and instructions
-   [Multi-agent orchestration](https://docs.warp.dev/platform/orchestration/) - Fan out ad-hoc parent and child agents outside a standing factory
-   [Definitions as code](https://docs.warp.dev/factories/factory-as-code/) - The definition file format, with working examples in [warp-factory-examples](https://github.com/warpdotdev/warp-factory-examples).
-   [Transitioning from Oz](https://docs.warp.dev/platform/transitioning-from-oz/) - Assess an existing web app, CLI, SDK, or API workflow.
-   [Get started with the Warp team](https://www.warp.dev/get-started) - Get help choosing and setting up a workflow.
