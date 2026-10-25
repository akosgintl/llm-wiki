---
title: "Demo: Sentry monitoring with SDK"
subtitle: "Build a Sentry webhook handler that triggers agents to investigate errors and create draft PRs."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/api-and-sdk/demo-sentry-monitoring-with-sdk/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Demo: Sentry monitoring with SDK

Build a Sentry webhook handler that triggers agents to investigate errors and create draft PRs.

A small TypeScript “Sentry monitor” service turns specific Sentry alerts, such as a Go nil pointer dereference, into draft pull requests by triggering a Warp cloud agent to investigate.

The service validates the webhook, extracts the stack trace, and injects it into an agent run inside a [cloud environment](https://docs.warp.dev/platform/environments/) so the agent can inspect the repo and propose a fix. The full source is in the [Sentry monitor example repository](https://github.com/warpdotdev/warp-agents-sdk-demo-sentry-monitor).

To route the alert through a factory’s agents and workflow instead, dispatch it with [factory endpoints](https://docs.warp.dev/factories/factory-api/) or a [custom webhook](https://docs.warp.dev/factories/webhooks/). This demo covers standalone cloud agent intake.

![Monitoring Sentry with the TypeScript SDK demo video](https://i.ytimg.com/vi/fHQXLg9ybi4/sddefault.jpg)

## What the demo covers

-   Using the [TypeScript SDK](https://github.com/warpdotdev/oz-sdk-typescript) to trigger agent runs and retrieve run details.
-   Handling run lifecycle states (queued → running) to fetch a session link for debugging.
-   Running agents inside a cloud environment so they can investigate real code, run tests, and validate fixes.
-   Building a lightweight Sentry webhook server that filters, validates, and routes only the right errors to an agent.
-   Ending the workflow in a draft GitHub pull request for a maintainer to review, instead of silent autonomous changes.

## Related pages

-   [Agent & run endpoints](https://docs.warp.dev/factories/api-and-sdk/) - The Warp Platform API endpoints and SDKs the demo builds on.
-   [Warp Platform API quickstart](https://docs.warp.dev/factories/api-and-sdk/quickstart/) - Create and monitor your first run in about five minutes.
-   [Cloud agents quickstart](https://docs.warp.dev/platform/quickstart/) - Set up the environment an agent run executes in.
