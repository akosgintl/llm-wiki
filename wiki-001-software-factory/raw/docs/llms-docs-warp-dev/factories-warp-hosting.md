---
title: "Warp-hosted execution for Warp Factories"
subtitle: "Run factory work on Warp-hosted infrastructure, with managed compute, isolation, networking, and capacity."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/warp-hosting/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Warp-hosted execution for Warp Factories

Run factory work on Warp-hosted infrastructure, with managed compute, isolation, networking, and capacity.

Warp-hosted execution runs factory work in managed sandboxes. Warp provisions the compute while your factory definition selects each agent’s runner, repositories, setup, and credentials.

Use it when your factory’s repositories and services are reachable from the public internet. Warp manages capacity and host maintenance. For private services or a network boundary that must contain checkout and execution, use [managed self-hosting](https://docs.warp.dev/factories/self-hosting/).

## Sandbox environment

Warp-hosted agents run in isolated sandboxes. See [About factory infrastructure and security](https://docs.warp.dev/factories/infrastructure-and-security/) for execution, data, and credential boundaries.

## OS and architecture

Warp-hosted factory agents use the runner and workspace configuration in your [factory definition](https://docs.warp.dev/factories/factory-as-code/). A factory can also use an existing [environment](https://docs.warp.dev/platform/environments/) when its definition specifies one.

For supported operating systems, architectures, and Linux image requirements, see [runner platform options](https://docs.warp.dev/factories/runners/#operating-systems).

## Resources

Available CPU and memory depend on your plan. See [Warp pricing](https://www.warp.dev/pricing) for plan information.

On [Enterprise](https://docs.warp.dev/enterprise/) plans, resources are configurable up to 32 vCPUs and 64 GiB of memory. Contact Warp support about custom provisioning if you need more.

## Concurrency

Warp limits concurrent hosted runs per team. Runs started at the limit are queued until another run completes.

## Networking

Warp-hosted agents have network egress enabled by default. If you need to allowlist traffic from Warp agents, such as in a firewall policy, get Warp’s IP address ranges from the “Warp-hosted agent networking” settings for your team. Find it on your team’s **Platform** page in the [Admin Panel](https://app.warp.dev/admin/) or on [User settings in the Warp Factories web app](https://platform.warp.dev/settings).

* * *

## Related pages

-   [Automation Platform](https://docs.warp.dev/platform/overview/) - Review shared cloud-agent capabilities
-   [Runners for Warp Factories](https://docs.warp.dev/factories/runners/) - Choose the operating system, architecture, and instance size
-   [Self-hosting overview](https://docs.warp.dev/factories/self-hosting/) - Run work on infrastructure you manage
