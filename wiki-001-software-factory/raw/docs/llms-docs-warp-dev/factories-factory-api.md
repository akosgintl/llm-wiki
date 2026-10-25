---
title: "Factory endpoints"
subtitle: "Discover factories and dispatch tasks by UID with factory endpoints, without learning the foreman agent's internals."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/factory-api/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Factory endpoints

Discover factories and dispatch tasks by UID with factory endpoints, without learning the foreman agent's internals.

The factory endpoints are part of the Warp Platform API. Use them to find a factory and start work from your own code without managing agent details. Call them from a chat bot, script, or service you control.

## Core endpoints

-   `GET /factory` - list factories your account can access. Add `search` to filter by name or alias, case-insensitive.
-   `GET /factory/{uid}` - get one factory by UID.
-   `POST /factory/{uid}/runs` - dispatch a run to the factory’s foreman agent. Pass a `prompt`; the server resolves the foreman for you.

These are the core discovery and dispatch endpoints. The interactive [Warp Platform API reference](https://docs.warp.dev/api) documents their parameters and schemas, and also covers the factory’s tasks and factory-file schemas. A dispatched run is an ordinary [cloud agent run](https://docs.warp.dev/platform/): retrieve it, send it follow-ups, or cancel it through the same [agent and run endpoints](https://docs.warp.dev/factories/api-and-sdk/) used for any run.

## Choosing how work reaches a factory

Factory endpoints are one of several ways to get work into a factory, and each fits a different source:

-   **A bot, service, or script you control** - use factory endpoints to find a factory and dispatch to it.
-   **A tool that can send a webhook**, such as CI, Sentry, or PagerDuty - create a [custom webhook](https://docs.warp.dev/factories/webhooks/) and let an automation filter deliveries by payload, with no code to write.
-   **A coding agent session**, local or in another MCP client - use [Factory MCP](https://docs.warp.dev/factories/factory-mcp/) to send work in or pull a task down to work on locally.
-   **A chat platform or issue tracker your team already uses** - connect it as an [integration](https://docs.warp.dev/factories/connect-your-factory/) so matching events start work automatically.

See [Connect your factory](https://docs.warp.dev/factories/connect-your-factory/) for the full comparison across every intake path.

## Choosing an endpoint family

Use factory endpoints to find or start work on a factory. Use Agent & run endpoints for everything else: a standalone cloud agent, run management, or orchestration.

| Task | Recommended API |
| --- | --- |
| Find a factory by name before dispatching to it | factory endpoints - `GET /factory?search=` |
| Start a new task on a factory | factory endpoints - `POST /factory/{uid}/runs` |
| Continue, monitor, or cancel a run (factory or standalone) | Agent & run endpoints - `GET /agent/runs/{runId}`, `POST /agent/runs/{runId}/followups`, `POST /agent/runs/{runId}/cancel` |
| Run a standalone cloud agent with no factory involved | Agent & run endpoints - `POST /agent/runs` |
| Build a multi-agent orchestration | Agent & run endpoints - see [Multi-agent orchestration](https://docs.warp.dev/platform/orchestration/) |

Every factory run is still an ordinary run, so Agent & run endpoints handle status, follow-ups, and cancellation no matter which endpoint family started it.

## Discover a factory

### Search factories by name

```python
import os
from warp_platform_sdk import WarpClient

client = WarpClient(api_key=os.environ.get("WARP_API_KEY"))

# Find a factory by name or alias — no UIDs needed up front
page = client.factories.list(search="payments")
factory = page.factories[0]

# Iteration fetches additional pages automatically
for f in client.factories.list(search="payments"):
    print(f.uid, f.name)
```

The REST equivalent:

```http
GET /api/v1/factory?search=payments
Authorization: Bearer YOUR_API_KEY
```

### Get a factory when the UID is already known

```python
factory = client.factories.get(factory.uid)
```

```http
GET /api/v1/factory/YOUR_FACTORY_UID
Authorization: Bearer YOUR_API_KEY
```

## Dispatch a run to a factory

Dispatch with just the factory’s UID and a `prompt`:

```python
run = client.factories.runs.create(
    factory.uid,
    prompt="Investigate and fix the flaky payment webhook retry test",
    title="Fix flaky payment webhook retry test",
    ticket_ref="linear:PAY-123",
)
print(run.run_id, run.run_url, run.state)
```

```http
POST /api/v1/factory/YOUR_FACTORY_UID/runs
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json

{
  "prompt": "Investigate and fix the flaky payment webhook retry test",
  "title": "Fix flaky payment webhook retry test",
  "ticket_ref": "linear:PAY-123"
}
```

Every field except `prompt` is optional. Omit `title` and the server derives one from the prompt. `ticket_ref` identifies the originating ticket in `<source>:<id>` form (for example `linear:PAY-123` or `jira:PROJ-456`); pass `ticket_url` to link the factory’s task record back to it, or omit both for an adhoc reference.

## Continue and monitor the run

```python
status = client.agent.runs.retrieve(run.run_id)
```

Send a follow-up the same way you would for any run:

```http
POST /api/v1/agent/runs/YOUR_RUN_ID/followups
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json

{
  "message": "Also add a regression test for the retry backoff"
}
```

See [key endpoints](https://docs.warp.dev/factories/api-and-sdk/#key-endpoints) for the full set of run-management operations, including cancellation.

## Related pages

-   [Connect your factory](https://docs.warp.dev/factories/connect-your-factory/) - Every way work can enter a factory, including factory endpoints alongside Slack, GitHub, and Factory MCP.
-   [Build a Mattermost bot for Warp Factories](https://docs.warp.dev/guides/external-tools/build-a-mattermost-bot-for-warp-factories/) - A worked example that discovers a factory and dispatches and continues a task from a custom chat integration.
-   [Factory MCP](https://docs.warp.dev/factories/factory-mcp/) - Connect a local coding agent to a factory instead of calling the REST API directly.
-   [Agent & run endpoints](https://docs.warp.dev/factories/api-and-sdk/) - Full endpoint reference, SDKs, and error codes for the underlying Warp Platform API.
-   [How Warp Factories work](https://docs.warp.dev/factories/how-factories-work/) - The stages a dispatched task moves through after the foreman picks it up.
