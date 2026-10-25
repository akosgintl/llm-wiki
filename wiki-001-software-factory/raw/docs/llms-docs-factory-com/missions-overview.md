---
title: "Factory Missions"
subtitle: "Use Factory Missions to plan and execute large, multi-feature projects with structured orchestration. Describe your goal, collaborate on the plan, and let Droid manage the work."
authors: []
published_date: null
source_url: https://docs.factory.com/missions/overview.md
origin: llms-txt
llms_txt: https://docs.factory.com/llms.txt
section: "Documentation"
fetched: 2026-10-25T18:18:02Z
---

# Factory Missions

Use Factory Missions to plan and execute large, multi-feature projects with structured orchestration. Describe your goal, collaborate on the plan, and let Droid manage the work.

![Mission Control orchestration view](/docs-assets/images/mission-control.webp)

## What Missions do

Factory Missions are structured workflows for taking on large, multi-feature work with Droid. Instead of tackling everything in a single session, you collaborate with Droid upfront to build a plan (features, milestones, and the skills needed to accomplish each part), then hand off execution to an orchestration layer that manages the work.

Access Missions with the `/missions` command (also available via `/mission`).

Factory Missions are the orchestration feature. Mission Mode is the session state Droid enters after you approve a mission plan; see [Interaction Modes](/autonomy-and-safety/specification-mode) for how Mission Mode relates to Normal and Spec modes.

## When to use Missions

Missions are best for bounded, multi-feature efforts that benefit from upfront planning, milestones, and ongoing validation. As a rough guide, the sweet spot is **about 1–500 features**:

{/* sweep-allow: term-bullets */}

- **A small number of features:** Use a normal session when the work is straightforward and can be completed without a separate planning and orchestration phase.
- **About 1–500 features:** Start a new Mission so Droid can decompose the work into milestones, coordinate workers, and validate progress as it goes.
- **More than 500 features:** Split the work into multiple Missions, or use a longer-term operating workflow instead of treating it as one Mission.

These numbers are a planning heuristic, not a hard limit. The more important question is whether the work has a clear outcome and can be divided into meaningful milestones.

Start a Mission when you recognize that the work needs this structure. Do not run a normal session for a long time and then convert it into a Mission. Starting a new Mission preserves the upfront planning, feature breakdown, validation strategy, and orchestration context that Missions are designed to provide.

  **Collaborative Planning**
    Work with Droid to define features, milestones, and success criteria before any code is written.
  
  **Skill-Aware Execution**
    Droid reuses your existing skills and develops new specialized skills for each part of the work.
  
  **Structured Orchestration**
    Mission Control manages execution across agents, tracking progress through your plan.
  
  **Your Config Carries Over**
    MCP integrations, skills, hooks, and custom droids all work inside Missions.
  

## For optimal outcomes

  For the best results, your repository should be at [Agent Readiness](/agent-readiness/overview) **Level 4 (Optimized) or above**.

  As a mission works, it runs user-facing QA testing against your application to validate each feature and self-correct as it goes. For this to work in an existing project, your codebase needs an automated, scriptable way to exercise the app the way a user would (for example, a script to stand up or mock all dependencies of the app to simulate all potential user flows). Without it, the mission cannot reliably verify its own work.

  Not there yet? Re-run your readiness evaluation with [`/readiness-report`](/agent-readiness/readiness-report), then close the gaps with [`/readiness-fix`](/agent-readiness/readiness-report#remediation-with-readiness-fix).

## How it works

  **Enter Missions**
    Start by running `/missions` in any Droid session.
  
  **Collaborate on the plan**
    Droid interacts with you back and forth to understand your goal. It asks clarifying questions, probes for constraints, and works with you to define what you actually want built. This is a conversation, not a one-shot prompt.
  
  **Build features and milestones**
    Based on the conversation, Droid constructs a structured plan: a set of features organized into milestones. Each milestone represents a meaningful checkpoint in the work.
  
  **Skills are reused or developed**
    Droid pulls in your existing skills where they apply, and develops specialized skills for parts of the work that need them. This means the execution is tailored to your project and workflow, not generic.
  
  **Enter Mission Control**
    Once the plan is approved, Droid enters Mission Control, the Missions orchestration view that manages execution of the plan. You can monitor progress, see which features are being worked on, and intervene when needed.
  

For details on getting the plan right, see [Planning & Validation](/missions/planning). To run and steer an approved mission, see [Running in the CLI](/missions/running-cli) or [Running in the Factory App](/missions/running-app).

## What Missions are good for

We have built and tested Missions across a range of work:

{/* sweep-allow: term-bullets */}

- **Full-stack development**: Building complete applications with frontend, backend, database, and deployment.
- **Research**: Deep investigation tasks that require exploring multiple approaches, synthesizing findings, and producing structured output.
- **Brownfield migrations**: Modernizing existing codebases, swapping frameworks, or restructuring large projects while preserving existing behavior.
- **Ambitious prototypes**: Product experiments that need to be functional, not just sketched out.

The common thread: work that benefits from upfront planning and structured decomposition rather than ad-hoc prompting.

## Open questions

Missions are still evolving. There are fundamental questions we are working through:

{/* sweep-allow: term-bullets */}

- **Is parallelization necessary?** Running multiple agents in parallel sounds good in theory, but does it actually produce better results than sequential execution? We are testing this.
- **How do you maximize correctness?** Long-running plans accumulate errors. What validation and correction strategies work best at each stage?
- **Cost vs. quality tradeoffs**: How aggressive should the orchestrator be? More planning and validation means higher cost but potentially better output. Where is the right balance?

We want your feedback on these. Use Missions, push the workflow hard, and tell us what works and what does not.

## Troubleshooting

Missions are not fire-and-forget. The orchestrator is an agent, and you can talk to it. When something goes wrong, pause the orchestrator, describe what you are seeing in plain language, and ask it to recover.

  **The mission freezes or stops making progress**
    Tell the orchestrator the mission appears frozen, describe the last visible activity, and ask it to re-assess and continue. For example: *"The mission seems frozen, the last worker finished 10 minutes ago and nothing new has started. Re-assess and continue."*
  

  **A worker is taking too long on one item**
    Pause the orchestrator and tell it to mark the current item as complete and move on. You can revisit that item later or handle it manually. For example: *"The worker on the auth integration has been stuck for 20 minutes. Mark it as complete and move to the next feature."*
  

  **The mission is stuck on a milestone**
    Ask the orchestrator to re-assess the remaining work and identify what is blocking progress. It can re-plan around the obstacle, reorder features, or adjust milestone scope.
  

  **You need to change direction mid-mission**
    Pause and explain the new requirement or scope change. The orchestrator can update the plan, re-scope milestones, and continue from the new direction.
  

  **A feature retry limit warning appears**
    Inspect the latest worker for that feature to understand why it keeps failing. If the failures come from user-testing validation, make sure your project has a script that stands up or mocks dependencies so QA can simulate real user flows. See [Planning & Validation](/missions/planning#development-scripting-for-qa). If the project does not need QA-style validation, disable it in Mission Control settings.
  

  **Validation keeps failing or QA cannot run**
    Make sure the project can be started or mocked from a script, and that logs are written to the filesystem where Droid can inspect them. See [Planning & Validation](/missions/planning#development-scripting-for-qa). If QA-style validation is not useful for the project, disable it in Mission Control settings.
  

  
    Scope features, milestones, and validation frequency before execution begins.
  
  
    Monitor and steer an approved mission from the terminal.
  

