---
title: "How Warp Factories work"
subtitle: "A factory's foreman routes each work item through triage, planning, implementation, and review, with humans making the key decisions."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/how-factories-work/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# How Warp Factories work

A factory's foreman routes each work item through triage, planning, implementation, and review, with humans making the key decisions.

A factory is a team of cloud agents connected to your repositories. The **foreman agent** coordinates a factory’s work and communicates with you through the tool where the request started, such as Slack or Linear. It dispatches the factory’s other agents, each of which handles a stage of the software development lifecycle, and people make the key decisions along the way.

A **work item** is a single request the factory acts on, such as an issue, support request, pull request, or Factory MCP task. It keeps its identity from intake to handoff, however many agents contribute to it along the way.

![Warp Factories system diagram showing work sources, automations, the foreman and stage agents, human handoff, the factory definition, platform execution, the factory dashboard, and the measure-and-improve loop](https://docs.warp.dev/_astro/factories-work-item-flow.BhkqE-xd_1bmMHd.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)

## How a work item moves through the factory

The foreman passes each agent the context it needs and continues existing conversations when work returns for revisions.

Not every work item needs every stage. The foreman picks the shortest path that still meets your quality policy: it skips stages when the work is already well defined, starts partway through when enough context exists, and sends work back to an earlier agent when revisions are needed.

### Stages

The diagram below shows the default path through a factory’s stages.

flowchart LR
  Intake\[Intake\] --> Foreman\[Foreman\]
  Foreman --> Triage\[Triage\]
  Triage --> Decision{Plan needed?}
  Decision -->|Yes| Planning\[Planning\]
  Decision -->|No| Building\[Building\]
  Planning --> Approval\["Human review<br/>(default policy)"\]
  Approval --> Building
  Building --> Reviewing\[Reviewing\]
  Reviewing --> Revision{Revision needed?}
  Revision -->|Yes| Building
  Revision -->|No| Handoff\["Human handoff<br/>(default policy)"\]
  Handoff -->|"Merge notification<br/>or human confirmation"| Complete\[Complete\]

-   **Intake** - A work item enters from a [connected integration](https://docs.warp.dev/factories/connect-your-factory/), an automation, a direct run, or the [Factory MCP](https://docs.warp.dev/factories/factory-mcp/). [Automations](https://docs.warp.dev/factories/automations/) filter events and schedules and select an agent to handle the work. Direct requests go straight to the foreman. The work item keeps its source context as it moves through later stages.
-   **Triage** - The triage agent researches the request, reproduces the problem when needed, and defines the scope and complexity of the change. The foreman skips this stage when the request already explains the problem and what needs to change.
-   **Planning** - The spec agent defines product behavior, technical constraints, and validation criteria. The foreman skips this stage for small, well-understood changes.
-   **Building** - The implement agent makes the code change on a branch and opens a pull request with test and visual evidence.
-   **Reviewing** - The review agent checks the change against the requirements, tests, and security expectations, then sends findings back for another pass. Its verdict is advisory.
-   **Human handoff** - The factory presents the result, its evidence, and any findings, and updates the original work item. A person decides what happens next.
-   **Complete or Cancelled** - By default, the foreman completes the work item after a merge notification or confirmation that the pull request landed. Handoff alone doesn’t complete it. A cancellation stops the work early.

Stages and agents are named separately, so the spec agent works the planning stage, the implement agent works the building stage, and the review agent works the reviewing stage. See [About factory agents](https://docs.warp.dev/factories/factory-agents/) for each agent’s responsibilities.

Each agent’s run is a [cloud agent run](https://docs.warp.dev/platform/) on Warp-hosted or [managed self-hosted](https://docs.warp.dev/factories/self-hosting/) compute, using the factory’s repositories and the agent’s configured model and [harness](https://docs.warp.dev/platform/harnesses/). Watch and steer runs from the factory’s [Runs page](https://docs.warp.dev/factories/factory-dashboard/#inspect-runs). Work that needs your input appears in your [inbox](https://docs.warp.dev/factories/factory-inbox/).

## Where your team stays in charge

A factory pauses when a person needs to decide. By default, that’s three places:

-   **Approving the spec** - When work needs a spec, implementation waits until a person signs off on the plan.
-   **Answering questions** - When requirements are unclear or a review finding is ambiguous, the foreman asks instead of guessing.
-   **Merging** - The factory opens the pull request and hands it off. Whether and when it merges is your team’s call.

The first two are workflow policy, written into the foreman’s instructions; edit them to change when the factory checks in. Merging is enforced by your repository, so if you require human-only merges, use branch protection and repository permissions.

## How the factory improves itself

[Scorers](https://docs.warp.dev/factories/measure-and-improve/scorers/) classify completed runs against criteria you write, and [Self-improvement](https://docs.warp.dev/factories/measure-and-improve/self-improvement/) groups the failures they flag into follow-up runs that propose fixes to the application code or to the factory’s own definition. Every proposal arrives as a pull request for your review; nothing is adopted on its own.

Use [benchmarks](https://docs.warp.dev/factories/benchmarks/) to compare configurations on the same tasks.

A factory’s agents, automations, runners, scorers, skills, and webhooks are configured in [definition files](https://docs.warp.dev/factories/factory-as-code/), either managed by Warp or stored in a GitHub repository your team owns. Anyone on the team, or an agent, can propose changes to the definition, including its instructions, skills, and models. Definitions stored in GitHub go through pull request review and [configuration checks](https://docs.warp.dev/factories/factory-as-code/#pull-request-checks) before a change reaches the production branch.

## Related pages

-   [Sizing a factory](https://docs.warp.dev/factories/#sizing-a-factory) - Which repositories belong in one factory.
-   [About factory agents](https://docs.warp.dev/factories/factory-agents/) - What each default agent does and how to configure it.
-   [Connect your factory](https://docs.warp.dev/factories/connect-your-factory/) - Every way work can enter a factory.
-   [Measure and improve](https://docs.warp.dev/factories/measure-and-improve/) - Scorers, benchmarks, and Self-improvement.
-   [Build a self-improving agent](https://docs.warp.dev/guides/agent-workflows/build-a-self-improving-agent/) - Apply the same loop to a standalone agent.
