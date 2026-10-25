---
title: "Self-hosting quickstart"
subtitle: "Get a managed self-hosted Automation Platform worker running on Docker and route your first cloud agent run to it in under 10 minutes."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/self-hosting/quickstart/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Self-hosting quickstart

Get a managed self-hosted Automation Platform worker running on Docker and route your first cloud agent run to it in under 10 minutes.

Run your first cloud agent on your own infrastructure in ~10 minutes using the managed architecture with the Docker backend — the default and fastest path to self-hosting.

Note

This quickstart sets up the [managed architecture](https://docs.warp.dev/factories/self-hosting/#managed-architecture), where the Automation Platform orchestrates the agent and your worker provides the compute. **Prefer a CLI-only path with no Docker requirement?** Jump to the [Unmanaged quickstart](https://docs.warp.dev/platform/unmanaged-execution/#unmanaged-quickstart) to run `oz agent run` directly on any host.

* * *

## Prerequisites

-   Managed self-hosting access and network connectivity. See the [shared managed prerequisites](https://docs.warp.dev/factories/self-hosting/#managed-prerequisites).
-   An [Agent API key associated with the Default Service Account](https://docs.warp.dev/agents/cli/oz-cli/api-keys/#from-the-web-app-recommended).
-   A Linux machine with a rootful Docker daemon and GNU `stat`.
-   The Oz CLI on the machine that will route the test run. See [Installing the CLI](https://docs.warp.dev/agents/cli/oz-cli/#installing-the-cli).

For macOS or Windows, use the [Homebrew](https://docs.warp.dev/factories/self-hosting/managed-docker/#option-2-homebrew) or [release binary](https://docs.warp.dev/factories/self-hosting/managed-docker/#option-3-github-releases-binary) setup instead.

* * *

## Run your first self-hosted agent

*~10 minutes*

### 1\. Export your API key

Use the Agent API key for both the worker container and `oz agent run-cloud`. A self-hosted worker key authenticates the worker only. Export the key so both tools can authenticate to the Automation Platform:

```bash
export WARP_API_KEY="YOUR_AGENT_API_KEY"
```

### 2\. Start the worker

On the Linux host, run the `oz-agent-worker` container and mount the Docker socket so the worker can spawn task containers. Choose any `--worker-id` meaningful for your team — you’ll use this value to route tasks to this worker.

```bash
export DOCKER_SOCKET_GID="$(stat -c '%g' /var/run/docker.sock)"

docker run \
  --group-add "$DOCKER_SOCKET_GID" \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e WARP_API_KEY="$WARP_API_KEY" \
  warpdotdev/oz-agent-worker --worker-id "my-worker"
```

**Expected outcome:** The worker connects to the Automation Platform and begins listening for tasks. You should see log output confirming the connection (something like `Connected to Oz` / `Waiting for tasks`).

Caution

For production deployments, pin to a specific image digest (e.g., `warpdotdev/oz-agent-worker@sha256:...`) instead of the `latest` tag.

### 3\. Route a run to your worker

In a separate terminal on any machine with the Oz CLI, route a cloud agent run to your worker by passing `--host` with the worker ID you chose:

```bash
oz agent run-cloud --prompt "List the files in the current directory" --host "my-worker"
```

**Expected outcome:** The Automation Platform accepts the task, routes it to your worker, and the worker spawns a Docker container to execute the agent. You’ll see the run appear in the [cloud agent dashboard](https://oz.warp.dev) with status moving from `QUEUED` → `INPROGRESS` → `SUCCEEDED`.

### 4\. Verify the run

Open the [cloud agent dashboard](https://oz.warp.dev), find the new task, and confirm the session transcript shows the agent running against your worker. You can attach to the session at any time via [Agent Session Sharing](https://docs.warp.dev/agents/local-agents/session-sharing/) to monitor or steer it.

* * *

## Troubleshooting

**Worker won’t start**  
Verify Docker is running (`docker info`) and that the daemon platform is `linux/amd64` or `linux/arm64`. Musl-based (Alpine) worker hosts are not supported.

**Worker won’t connect**  
Verify you created an **Agent** key associated with the Default Service Account and that it has not expired. Ensure the machine has outbound internet access to `oz.warp.dev:443`. Increase log verbosity with `--log-level debug` to see connection details.

**Task stays queued and never runs**  
Confirm the `--host` value you passed to `oz agent run-cloud` matches your `--worker-id` exactly (case-sensitive). Check that the worker’s team matches the team creating the task.

For more, see [Troubleshooting](https://docs.warp.dev/factories/self-hosting/troubleshooting/).

## Next steps

-   [Self-hosting overview](https://docs.warp.dev/factories/self-hosting/) — Compare managed and unmanaged architectures and choose a backend.
-   [Managed: Docker](https://docs.warp.dev/factories/self-hosting/managed-docker/) — Full Docker backend setup, including private registries, volume mounts, and runtime configuration.
-   [Routing runs to self-hosted workers](https://docs.warp.dev/factories/self-hosting/#routing-runs-to-self-hosted-workers) — How to route tasks from schedules, integrations (Slack, Linear), the API, and the Oz web app.
