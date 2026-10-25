---
title: "About factory agents"
subtitle: "Every factory has a team of default agents: a foreman that coordinates the work, plus triage, spec, implement, and review agents."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/factory-agents/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# About factory agents

Every factory has a team of default agents: a foreman that coordinates the work, plus triage, spec, implement, and review agents.

The **foreman** is the agent that coordinates a factory’s work and communicates with you. It delegates work to other agents, asks for your decisions when needed, and returns results. Default agents each cover one part of the software development lifecycle: triage scopes the request, spec writes the plan, implement writes the code, and review checks it. Together, they turn a work item into a pull request ready for your team to review.

## The default agents

Every factory gets a foreman. You choose which of the four default agents to include. These defaults are a starting point, and you can [add custom agents](https://docs.warp.dev/factories/factory-agents/creating-custom-agents/) and [automations](https://docs.warp.dev/factories/automations/) for work they don’t cover.

The default agents’ prompts, descriptions, and models are available in [`00-warp-default-agents`](https://github.com/warpdotdev/warp-factory-examples/tree/main/examples/00-warp-default-agents) in the [warp-factory-examples](https://github.com/warpdotdev/warp-factory-examples) repository.

| Agent | What it does | What it produces |
| --- | --- | --- |
| Foreman | Coordinates the work and talks to the requester | Decisions, questions, status updates, and the final handoff |
| Triage | Investigates the request and establishes scope | Evidence, issue context, complexity, and open questions |
| Spec | Turns requirements into a concrete plan with validation criteria | Product and technical specs in a draft pull request |
| Implement | Makes and validates the code change | Code, tests, validation results, and visual evidence |
| Review | Independently checks the finished change | Findings and a recommendation |

These are responsibilities, not a fixed pipeline. A small, well-understood change can skip planning entirely. If the review agent finds problems, the foreman sends work back for another pass. By default, work that needs a spec waits for human approval before implementation starts.

For the complete lifecycle, see [How Warp Factories work](https://docs.warp.dev/factories/how-factories-work/).

### Foreman

The **foreman agent** assigns work and is the only default agent that communicates directly with you. It relays questions and answers between you and other agents, and continues their existing conversations for revisions and follow-ups.

After implementation and review, the foreman returns the pull request and supporting evidence, then waits for your team to merge. By default, the foreman marks the work item complete on a later merge notification or your confirmation that the pull request landed.

#### Foreman name

Use the foreman’s handle to @-mention it in Slack and Linear. Factory setup defaults the handle to the factory’s name. For example, a factory named `payments` gets the handle `@payments`.

The factory name and foreman handle can differ. To change the foreman’s handle, open your factory’s **Settings** in the web app and click **Identity**. You can also edit [`alias`](https://docs.warp.dev/factories/factory-as-code/#alias) in the definition.

### Triage

Triage researches the codebase and related issues, reproducing problems when research doesn’t establish the cause. It reports scope, complexity, and open questions so the foreman can choose clarification, planning, or implementation.

### Spec

Spec defines requirements through the foreman. It writes product and technical specifications with validation criteria in a draft pull request. By default, the foreman waits for human approval before implementation starts. You can change this policy in the foreman’s instructions.

### Implement

Implement builds on the spec’s branch and draft pull request. It adds tests, runs repository checks, and captures visual evidence of user-facing changes when [computer use](https://docs.warp.dev/agents/capabilities/computer-use/) is available. It revises changes after review but never merges.

### Review

Review independently checks requirements, code conventions, tests, security, and supporting evidence. It reruns or extends validation when needed, then recommends acceptance, revisions, or a human decision. It doesn’t approve or merge the pull request.

## Built-in skills

Every default agent includes GitHub skills; the foreman also includes a Slack skill. Choosing Linear or Jira during setup adds that tracker’s skill and instructions. You can add custom procedures with [factory skills](https://docs.warp.dev/factories/factory-skills/).

## Configuring and extending agents

For settings, prompts, models, and third-party authentication, see [Configuring factory agents](https://docs.warp.dev/factories/factory-agents/configuration/).

For new roles, skills, and foreman dispatch, see [Creating custom agents](https://docs.warp.dev/factories/factory-agents/creating-custom-agents/). To start agents from schedules and events, use [factory automations](https://docs.warp.dev/factories/automations/).

## Human decision points and permissions

| Decision | Default behavior | What enforces it |
| --- | --- | --- |
| Spec approval | The foreman asks a human to clarify ambiguity and approve every spec | Workflow policy in the foreman’s instructions, which your team can change |
| Merging | The foreman hands you the finished pull request. Agents never merge on your behalf. | Your repository’s permissions decide who can approve and merge |
| Runtime access | Each agent reaches only the repositories, secrets, and MCP servers in its configuration | Platform configuration and the permissions of the connected providers |

Your team can change the spec-approval policy in the foreman’s instructions. Repository permissions and branch protection control who can approve and merge pull requests. Access is different. What an agent can reach comes from its configuration and the permissions of the connected providers, never from its instructions — changing what an agent is told to do doesn’t change what it’s able to do.

So enforce with the real controls: branch protection and repository permissions decide who merges, and each agent’s configuration decides what it can reach.

## Related pages

-   [Configuring factory agents](https://docs.warp.dev/factories/factory-agents/configuration/)
-   [Creating custom agents](https://docs.warp.dev/factories/factory-agents/creating-custom-agents/)
-   [How Warp Factories work](https://docs.warp.dev/factories/how-factories-work/)
-   [Factory skills](https://docs.warp.dev/factories/factory-skills/)
-   [Definitions as code](https://docs.warp.dev/factories/factory-as-code/)
