---
title: "Warp Platform API quickstart"
subtitle: "Create and monitor your first cloud agent run with the Warp Platform API in about five minutes."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/api-and-sdk/quickstart/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Warp Platform API quickstart

Create and monitor your first cloud agent run with the Warp Platform API in about five minutes.

The Warp Platform API lets you run and manage cloud agents from CI/CD pipelines, backend services, scripts, or custom tooling without the Warp desktop app. Create your first run and check its status in about five minutes.

To dispatch work through a factory’s named agents and workflow, use [factory endpoints](https://docs.warp.dev/factories/factory-api/) after this quickstart. The run-management steps below also apply to the factory run those endpoints create.

Watch this short demo of how the REST API can power agent-backed apps like [PowerFixer](https://github.com/warpdotdev/power-fixer-setup), an issue triage bot built by the Warp team:

![Warp Platform API quickstart video](https://i.ytimg.com/vi/N6qMe641K34/sddefault.jpg)

## Prerequisites

-   A Warp API key from the [Oz web app settings](https://oz.warp.dev/settings). See [API keys](https://docs.warp.dev/agents/cli/oz-cli/api-keys/).
-   A configured [cloud environment](https://docs.warp.dev/platform/environments/) with the required repositories and dependencies. See the [Cloud agents quickstart](https://docs.warp.dev/platform/quickstart/).

## 1\. Set your API key

Use a personal key to attribute runs to you, or an agent key to attribute them to a [cloud agent](https://docs.warp.dev/platform/agents/).

Export your API key so the API can authenticate your requests automatically — all commands in this guide reference the `WARP_API_KEY` environment variable.

```bash
export WARP_API_KEY="wk-..."
```

Replace `wk-...` with the key you created earlier.

## 2\. Create your first run

Submit a prompt to start an agent run:

```bash
curl -X POST https://app.warp.dev/api/v1/agent/runs \
  -H "Authorization: Bearer $WARP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Scan the repo for outdated dependencies and summarize the findings.",
    "config": {
      "environment_id": "<ENV_ID>"
    }
  }'
```

Replace `<ENV_ID>` with your environment ID. Find it with `oz environment list` on the Oz CLI or in the [Oz web app](https://oz.warp.dev).

Note

Prefer typed requests? The official [`warp-platform-sdk` Python package](https://pypi.org/project/warp-platform-sdk/) and [`@warp-dot-dev/warp-platform-sdk` TypeScript package](https://www.npmjs.com/package/@warp-dot-dev/warp-platform-sdk) wrap the same API with typed models, retries, and error handling.

The API returns a `run_id` immediately. The agent starts asynchronously — you can check its status at any time using the run ID.

## 3\. Check run status

Fetch the current state of the run with the following command. Replace `<RUN_ID>` with the `run_id` from step 2.

```bash
curl "https://app.warp.dev/api/v1/agent/runs/<RUN_ID>" \
  -H "Authorization: Bearer $WARP_API_KEY"
```

The `state` has the following possible values:

-   `QUEUED` - The run is waiting to start.
-   `INPROGRESS` - The agent is actively running.
-   `SUCCEEDED` - The run completed successfully.
-   `FAILED` - The run encountered an error. Check the `status_message` field in the response for details, then use the [API error reference](https://docs.warp.dev/factories/api-and-sdk/troubleshooting/errors/) to interpret the error code.

These are the most common states. See the [Agent & run endpoints](https://docs.warp.dev/factories/api-and-sdk/) and [Warp Platform API reference](https://docs.warp.dev/api) for all possible values.

To list all recent runs:

```bash
curl "https://app.warp.dev/api/v1/agent/runs" \
  -H "Authorization: Bearer $WARP_API_KEY"
```

## 4\. View the results

Once the run reaches `SUCCEEDED`, the response includes a `session_link` — a direct URL to the full run transcript, including commands executed, files changed, and agent output.

You can also view and manage all runs in the [cloud agent dashboard](https://oz.warp.dev/runs).

## Next steps

You created a cloud agent run over HTTP and tracked it from `QUEUED` to `SUCCEEDED`. From here:

-   **Read the endpoint guide** - [Agent & run endpoints](https://docs.warp.dev/factories/api-and-sdk/) documents the configuration and run lifecycle, while the [Warp Platform API reference](https://docs.warp.dev/api) lists all parameters, query filters, and response schemas.
-   **Explore the SDKs** - [`warp-platform-sdk` for Python](https://pypi.org/project/warp-platform-sdk/) and [`@warp-dot-dev/warp-platform-sdk` for TypeScript](https://www.npmjs.com/package/@warp-dot-dev/warp-platform-sdk) include typed request/response models, retries, and error handling.
-   **See a real-world example** - [Demo: Sentry monitoring with SDK](https://docs.warp.dev/factories/api-and-sdk/demo-sentry-monitoring-with-sdk/) shows how to build a webhook handler that triggers agents from production errors.
-   **Schedule and automate** - See the [Scheduled Agents quickstart](https://docs.warp.dev/platform/triggers/scheduled-agents-quickstart/) to run agents on a cron, or the [Integrations quickstart](https://docs.warp.dev/platform/integrations/quickstart/) to trigger agents from Slack or Linear.
