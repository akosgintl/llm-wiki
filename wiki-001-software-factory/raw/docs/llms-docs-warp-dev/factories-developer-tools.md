---
title: "Warp Platform API & SDKs"
subtitle: "Use the Warp Platform API, SDKs, Factory MCP, and webhooks to integrate factories and cloud agent runs with your tools and services."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/developer-tools/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Warp Platform API & SDKs

Use the Warp Platform API, SDKs, Factory MCP, and webhooks to integrate factories and cloud agent runs with your tools and services.

The Warp Platform API serves both factories and standalone cloud agent runs. The factory endpoints send work to a factory; agent and run endpoints start and manage standalone runs. Both endpoint families use the same API key, API reference, SDKs, and error model.

## Get started

To send work through a factory, start with [dispatching a run to a factory](https://docs.warp.dev/factories/factory-api/#dispatch-a-run-to-a-factory).

To start a standalone cloud agent, use the [API & SDK quickstart](https://docs.warp.dev/factories/api-and-sdk/quickstart/). The [Sentry monitoring example](https://docs.warp.dev/factories/api-and-sdk/demo-sentry-monitoring-with-sdk/) shows standalone dispatch from a webhook handler.

## Choose an API surface

-   **[Factory endpoints](https://docs.warp.dev/factories/factory-api/)** - Find a factory and send work to it by UID from your application or service.
-   **[Agent & run endpoints](https://docs.warp.dev/factories/api-and-sdk/)** - Start, monitor, continue, and cancel cloud agent runs from scripts, CI, and backend services.
-   **[Warp Platform API reference](https://docs.warp.dev/api)** - Look up the full HTTP schema, parameters, and responses.
-   **[Python SDK](https://pypi.org/project/warp-platform-sdk/)** - Install `warp-platform-sdk` to make typed requests from Python.
-   **[TypeScript SDK](https://www.npmjs.com/package/@warp-dot-dev/warp-platform-sdk)** - Install `@warp-dot-dev/warp-platform-sdk` to make typed requests from TypeScript.
-   **[API errors](https://docs.warp.dev/factories/api-and-sdk/troubleshooting/errors/)** - Resolve error responses by HTTP status and machine-readable code.
-   **[Factory MCP](https://docs.warp.dev/factories/factory-mcp/)** - Exchange work between a factory and a connected coding agent or MCP client.
-   **[Webhooks](https://docs.warp.dev/factories/webhooks/)** - Receive events from systems that can send JSON and route matching deliveries into factory automations.

## Related pages

-   [Connect your factory](https://docs.warp.dev/factories/connect-your-factory/) - Choose an integration or direct intake path.
-   [Factory automations](https://docs.warp.dev/factories/automations/) - Route events and schedules to factory agents.
-   [Factory dashboard](https://docs.warp.dev/factories/factory-dashboard/) - Inspect work items, runs, and factory settings.
