---
title: "What's Factory?"
subtitle: "Connect a repository, investigate issues, and review agent-created pull requests with Mastra Factory."
authors: []
published_date: null
source_url: https://factory.mastra.ai/what-is-factory.md
origin: llms-txt
llms_txt: https://factory.mastra.ai/llms.txt
section: "Docs"
fetched: 2026-10-25T18:10:21Z
---

# What's Factory?

Mastra Factory is a web application for working with coding agents. Connect your repository, bring issues into a work board, and guide a change through investigation, planning, implementation, and pull request review.

Start with one issue and keep control of the decisions at each phase. Review the proposed work and plan before deciding whether to merge the result.

Mastra Factory is a separate project from the code it changes. Create the Factory project in its own directory, outside the repository you want agents to work on. Factory clones that repository into an isolated sandbox for each session, then makes changes there and opens pull requests. It never edits your local checkout. Connecting an existing repository is the standard setup, and it doesn't need to be new or empty.

## Choose your starting point

| Your task                             | Start here                                                                                                      |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Set up your first Factory             | [Get started](https://factory.mastra.ai/)                                                                       |
| Turn an issue into a pull request     | [Create your first pull request](https://factory.mastra.ai/)                                                    |
| Join a Factory your team already runs | [Models](https://factory.mastra.ai/configure/models), then [GitHub](https://factory.mastra.ai/configure/github) |
| Bring work from another service       | [Linear](https://factory.mastra.ai/configure/linear) or [Slack](https://factory.mastra.ai/configure/slack)      |
| Run Factory for a team                | [Deployment](https://factory.mastra.ai/deployment)                                                              |

## Understand the pieces

Use Factory from a web or mobile browser, or interact with agents through [Slack](https://factory.mastra.ai/configure/slack). [GitHub](https://factory.mastra.ai/configure/github) supplies repositories and issues, and Factory writes pull requests back to it. [Linear](https://factory.mastra.ai/configure/linear) can also bring issues into Factory.

Mastra Factory brings together the Factory Server, [auth](https://factory.mastra.ai/configure/auth), [sandboxes](https://factory.mastra.ai/configure/sandboxes), and [storage](https://factory.mastra.ai/configure/storage). The server provides the web UI and coordinates work. Mastra Factory works with your preferred model providers.

![Mastra Factory contains the Factory Server, auth, sandboxes, and storage. Browsers and Slack connect users to Factory. Linear supplies issues. GitHub sends issues and code into Factory and receives pull requests. Factory connects to external large language model providers.](/img/docs/factory-components.svg)

Choose the large language models (LLMs) for your coding agents through a model provider with an API key or a supported subscription.

## Where Factory runs

Factory supports three setups:

- **Fully on Mastra platform:** Run the Factory Server, authentication, storage, and sandboxes on Mastra platform.
- **Local server with platform resources:** Run the Factory Server on your computer while Mastra platform provides authentication, storage, and sandboxes.
- **Fully self-hosted:** Run the server and configure your own authentication, storage, and sandbox providers without Mastra platform services.

You can configure authentication, storage, and sandboxes independently of where the server runs. New Factory projects use platform services by default. See [Deployment](https://factory.mastra.ai/deployment) for deployment options.

## Understand Factory terms

| Term                                                            | Meaning                                                                                                                                                               |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Factory project                                                 | The server configuration and dependencies for a Factory. Keep it in its own directory so its configuration and Git history stay independent of the target repository. |
| Target repository                                               | The codebase you ask agents to change.                                                                                                                                |
| Platform project                                                | The Platform resource used to manage the server's database and deployment environments.                                                                               |
| Factory                                                         | A codebase and its settings, work, and sessions in the UI.                                                                                                            |
| [Intake](https://factory.mastra.ai/using/intake)                | Incoming issues or pull requests that are available for work.                                                                                                         |
| [Work item](https://factory.mastra.ai/using/work-and-approvals) | A card tracking an issue or another task through the Work board.                                                                                                      |
| [Review item](https://factory.mastra.ai/using/reviews)          | A separate card tracking review of a pull request.                                                                                                                    |
| [Session](https://factory.mastra.ai/using/sessions)             | The agent conversation and workspace associated with a piece of work.                                                                                                 |

## Follow a change

Issues arrive in **Intake**, where you can start an investigation. The agent investigates the issue, requests your input when needed, then plans and implements the changes. It opens a pull request with its own Review card and session. Follow the review and inspect the changes. Then decide whether to merge the pull request.

The original Work item and the PR's Review item have separate completion rules. See [Work items](https://factory.mastra.ai/using/work-and-approvals) for the actions, automation settings, and external events that move cards.

Factory acts on its own for some steps and waits for a person on others. On its own, it syncs issues from connected sources, proposes investigations, and moves cards in response to source events. These steps always wait for a person:

- Starting a run on a card, unless **Auto-start runs** is on and the item is eligible.
- Accepting a non-bug task before it enters planning or building.
- Approving a plan before implementation continues, unless **Auto-approve plans** is on.
- Merging a pull request.

Watch progress on the Factory's **Overview** page, in each session's transcript, and in the **Audit log**.

## Next steps

- [Get started](https://factory.mastra.ai/) and investigate one GitHub issue.
- Continue to [Create your first pull request](https://factory.mastra.ai/) after investigation.
- [Troubleshoot setup](https://factory.mastra.ai/troubleshooting) when an expected result is missing.
