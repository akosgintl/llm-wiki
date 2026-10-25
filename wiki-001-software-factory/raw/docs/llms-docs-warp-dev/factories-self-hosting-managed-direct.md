---
title: "Managed: Direct backend"
subtitle: "Run the Automation Platform managed worker with the Direct backend to execute cloud agent tasks directly on the host, without Docker or Kubernetes."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/self-hosting/managed-direct/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Managed: Direct backend

Run the Automation Platform managed worker with the Direct backend to execute cloud agent tasks directly on the host, without Docker or Kubernetes.

Run the `oz-agent-worker` daemon with the **Direct backend** — tasks execute directly on the worker host without Docker or Kubernetes. The Automation Platform still orchestrates runs end to end (Slack, Linear, schedules, API, `oz agent run-cloud`); the worker just runs the agent in a per-task workspace on its own filesystem.

## When to use the Direct backend

-   Neither Docker nor Kubernetes is available on the worker host.
-   Tasks need direct access to host resources that are hard to expose through a container.
-   You want managed orchestration (triggering from Slack, Linear, schedules, API) without the operational overhead of a container runtime.

Caution

The Direct backend does not provide per-task container isolation. Each task runs in an isolated workspace directory, but shares the host OS and kernel. Evaluate whether this fits your security requirements before using it in production.

* * *

## How it works

1.  The worker creates a per-task workspace directory under `workspace_root`.
2.  If a `setup_command` is configured, it runs before the task with environment variables pointing to the workspace.
3.  The `oz` CLI runs the agent task inside the workspace directory.
4.  After the task completes, the optional `teardown_command` runs and the workspace is cleaned up.

* * *

## Prerequisites

-   Managed self-hosting access, network connectivity, and credentials. See the [shared managed prerequisites](https://docs.warp.dev/factories/self-hosting/#managed-prerequisites).
-   A worker host with write access to `workspace_root`, which defaults to `/var/lib/oz/workspaces`.
-   The `oz-agent-worker` binary on the worker host. See [Homebrew or prebuilt binary installation](https://docs.warp.dev/factories/self-hosting/managed-docker/#install-and-run-the-worker).
-   The Oz CLI in `PATH` on the worker host, or selected with `oz_path` in the config file. See [Installing the CLI](https://docs.warp.dev/agents/cli/oz-cli/#installing-the-cli).

* * *

## Setup

### 1\. Set your API key

Export the self-hosted worker API key so the worker can authenticate to the Automation Platform:

```bash
export WARP_API_KEY="YOUR_API_KEY"
```

### 2\. Start the worker with the Direct backend

Pass `--backend direct`:

```bash
oz-agent-worker --api-key "$WARP_API_KEY" --worker-id "my-worker" --backend direct
```

Or with a [config file](https://docs.warp.dev/factories/self-hosting/reference/#config-file):

```yaml
worker_id: "my-worker"
backend:
  direct:
    workspace_root: "/var/lib/oz/workspaces"
```

**Expected outcome:** The worker connects to the Automation Platform and begins listening for tasks. Each assigned task runs in a freshly-created subdirectory of `workspace_root`.

* * *

## Workspace model

Each task gets its own directory under `workspace_root`. The default is `/var/lib/oz/workspaces`; override it with the `workspace_root` config option shown above.

After the task completes, the workspace is deleted (unless `--no-cleanup` is set, which keeps the directory around for debugging).

To reuse a large monorepo without sharing one checkout between concurrent tasks, see [Direct backend monorepo worktrees](https://docs.warp.dev/factories/self-hosting/direct-monorepo-worktrees/).

Setting `target_dir` makes every task run in one shared directory and disables per-task workspace isolation. Use it only when the worker processes one task at a time.

* * *

## Setup and teardown commands

The `setup_command` runs before each task and receives the following environment variables:

-   `OZ_WORKSPACE_ROOT` — The workspace directory for the task.
-   `OZ_RUN_ID` — The unique task ID.
-   `OZ_ENVIRONMENT_FILE` — Path to a file where the setup script can write additional `KEY=VALUE` environment variables to inject into the task.
-   `OZ_WORKER_BACKEND` — Always set to `direct`.

The `teardown_command` runs after each task and receives `OZ_WORKSPACE_ROOT`, `OZ_RUN_ID`, and `OZ_WORKER_BACKEND`.

Use the setup command to clone repos, install dependencies, or write task-specific env vars into `OZ_ENVIRONMENT_FILE`. Use the teardown command for cleanup or reporting.

* * *

## Environment variables for Direct tasks

Note

The Direct backend starts tasks with a **minimal environment** (only `HOME`, `TMPDIR`, and `PATH` from the host) to avoid leaking sensitive worker credentials like `WARP_API_KEY` into tasks. Add variables explicitly via `environment` in the config file or `-e` flags on the worker CLI.

Config file example:

```yaml
worker_id: "direct-worker"
max_concurrent_tasks: 2
backend:
  direct:
    workspace_root: "/var/lib/oz/workspaces"
    oz_path: "/usr/local/bin/oz"
    setup_command: "/opt/scripts/setup.sh"
    teardown_command: "/opt/scripts/teardown.sh"
    environment:
      - name: MY_VAR
        value: "hello"
```

* * *

## Related pages

-   [Self-hosted worker reference](https://docs.warp.dev/factories/self-hosting/reference/#direct-backend-config) — Full config schema for the Direct backend.
-   [External orchestrators](https://docs.warp.dev/factories/self-hosting/external-orchestrators/) — Start one Direct worker per external job or delegate runs through the Command backend.
-   [Direct backend monorepo worktrees](https://docs.warp.dev/factories/self-hosting/direct-monorepo-worktrees/) — Create and remove one Git worktree per task with setup and teardown hooks.
-   [Self-hosting overview](https://docs.warp.dev/factories/self-hosting/) — Managed vs unmanaged and the backend decision guide.
-   [Routing runs to self-hosted workers](https://docs.warp.dev/factories/self-hosting/#routing-runs-to-self-hosted-workers) — How to send tasks to your connected worker from the CLI, schedules, integrations, the API, and the web UI.
-   [Security and networking](https://docs.warp.dev/platform/execution-security/) — Data boundaries and security considerations for the Direct backend.
-   [Troubleshooting](https://docs.warp.dev/factories/self-hosting/troubleshooting/#direct-backend) — Common Direct-backend issues.
