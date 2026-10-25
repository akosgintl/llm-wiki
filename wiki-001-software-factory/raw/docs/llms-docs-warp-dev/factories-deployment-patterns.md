---
title: "Deployment patterns for Warp Factories"
subtitle: "Choose Warp-hosted or managed self-hosted execution for Warp Factories based on your network, compliance, and operational requirements."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/deployment-patterns/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Deployment patterns for Warp Factories

Choose Warp-hosted or managed self-hosted execution for Warp Factories based on your network, compliance, and operational requirements.

Choose an execution model for your factory based on where its code must run and who operates the compute. Warp-hosted execution is the default. Managed self-hosting keeps checkout and command execution in your network while Warp coordinates the work.

The comparison below also shows unmanaged execution for standalone agents, which is not a factory execution host.

![Deployment models diagram comparing Warp-hosted, managed self-hosted, and unmanaged self-hosted patterns by what runs on Warp versus customer infrastructure](https://docs.warp.dev/_astro/deployment-models.BlU2yhYs_rHNNb.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)

Deployment models divide responsibilities between Warp and your infrastructure.

## Choose an execution model

| If your factory needs to… | Choose |
| --- | --- |
| Run public repositories and services without operating workers | [Warp-hosted execution](#warp-hosted-execution) |
| Reach private repositories or services behind your network boundary | [Managed self-hosting](#managed-self-hosting) |
| Run standalone agents from CI or developer infrastructure, without a factory | [Unmanaged execution](https://docs.warp.dev/platform/unmanaged-execution/) |

Both factory options use the same [factory definition](https://docs.warp.dev/factories/factory-as-code/), [runners](https://docs.warp.dev/factories/runners/), and [factory dashboard](https://docs.warp.dev/factories/factory-dashboard/). The execution host changes the location of checkout, command execution, and the sandbox filesystem.

## Warp-hosted execution

Use this when your factory can reach its repositories and services over the public internet. The [Automation Platform](https://docs.warp.dev/platform/overview/) runs the work on Warp-managed infrastructure while your factory definition selects the agents, runner, workspace, and credentials.

![Warp-hosted execution architecture showing customer infrastructure, triggers and integrations, isolated tenant sandboxes, the Warp control plane, and LLM providers](https://docs.warp.dev/_astro/cloud-agents-infra.Cd04z31r_A0wsX.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)

Warp operates the control plane and per-run sandboxes.

See the [cloud agent run lifecycle](https://docs.warp.dev/platform/architecture/#cloud-agent-run-lifecycle) reference for a description of each component in the architecture.

### What it looks like

-   **Work intake** - Automations, integrations, Factory MCP, and factory endpoints send work to the factory.
-   **Execution** - Agents run in Docker-based environments hosted by the Automation Platform.
-   **Visibility** - Teams monitor work through the factory dashboard, session sharing, and APIs.

### Send work to a factory

-   Route integration events, schedules, and webhooks to factory agents with [Factory automations](https://docs.warp.dev/factories/automations/).
-   Send work from Slack, Linear, Jira, GitHub, and GitLab through [factory integrations](https://docs.warp.dev/factories/connect-your-factory/).
-   Find a factory and dispatch work by UID from your service using [Factory endpoints](https://docs.warp.dev/factories/factory-api/).
-   Coding agents can hand work to a factory through [Factory MCP](https://docs.warp.dev/factories/factory-mcp/).

For standalone cloud-agent triggers, see [cloud agents](https://docs.warp.dev/platform/).

## Managed self-hosting

Use this when a factory must run checkout and execution on your infrastructure while the Automation Platform coordinates the work and records its results. Managed workers support Docker, Kubernetes, Direct, and external command backends. See [managed self-hosting](https://docs.warp.dev/factories/self-hosting/) for requirements and setup.

For standalone agents that you orchestrate directly from CI, Kubernetes, or developer infrastructure, use [unmanaged execution](https://docs.warp.dev/platform/unmanaged-execution/). See [execution security](https://docs.warp.dev/platform/execution-security/) for the data and network boundaries shared by both architectures.

## Related pages

-   [Infrastructure and security](https://docs.warp.dev/factories/infrastructure-and-security/) - Choose execution, inference, storage, and credential boundaries for a factory.
-   [Warp-hosted execution](https://docs.warp.dev/factories/warp-hosting/) - Review hosted execution capacity, networking, and supported environments.
-   [Managed self-hosting](https://docs.warp.dev/factories/self-hosting/) - Install and operate a factory worker on your infrastructure.
-   [Unmanaged execution](https://docs.warp.dev/platform/unmanaged-execution/) - Run standalone agents outside a factory.
