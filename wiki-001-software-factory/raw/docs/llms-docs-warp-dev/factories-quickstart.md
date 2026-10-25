---
title: "Warp Factories quickstart"
subtitle: "Set up a factory, connect your repositories, and take your first work item from prompt to pull request."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/quickstart/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Warp Factories quickstart

Set up a factory, connect your repositories, and take your first work item from prompt to pull request.

Create your first factory and take one small work item from prompt to pull request.

## Prerequisites

-   A [Warp account](https://app.warp.dev/signup) and membership in a [Warp team](https://docs.warp.dev/knowledge-and-collaboration/teams/).
-   Team or workspace admin access, or the team-level [Warp Factories Editor role](https://docs.warp.dev/factories/infrastructure-and-security/#factory-roles-and-permissions).
-   Available usage in your team’s balance for factory runs. See [access and billing requirements](https://docs.warp.dev/platform/team-access-billing-and-identity/).
-   Access to the repositories you want the factory to work on.

## Set up your factory

Note

For GitHub and GitLab repositories, an agent connected to [Factory MCP](https://docs.warp.dev/factories/factory-mcp/#set-up-with-your-coding-agent) can run this setup. For Azure DevOps, follow the steps below in the Warp Factories web app. If the setup page is still open when the agent finishes, refresh it to see the new factory.

1.  Open the [Warp Factories web app](https://platform.warp.dev) and sign in if prompted. To switch teams, click your avatar, hover over the team name, and select another team.
    
2.  Click **+** next to **Factories**.
    
    ![The Factories section of the sidebar, with the + button used to start a new factory highlighted.](https://docs.warp.dev/_astro/quickstart-open-setup-wizard.BsjqM_jG_Z22uxA5.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    The factory setup control in the sidebar.
    
3.  On the “Connect your code hosts” screen, select GitHub, GitLab, or Azure DevOps, then choose the organization or group to connect. For Azure DevOps, also choose a project. Click **Next**.
    
    ![The Connect your code hosts screen with GitHub connected, a GitHub organization dropdown, and connection options for GitLab and Azure DevOps.](https://docs.warp.dev/_astro/quickstart-connect-code-forges.BA5b4NXd_2bzL2r.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    The GitHub organization dropdown in factory setup.
    
    If your organization restricts connections to Warp, involve a code-host administrator. Azure DevOps requires [one-time administrator approval](https://docs.warp.dev/factories/integrations/azure-devops/#requirements); you can send the approval link during setup.
    
    For other code forges, see [Connecting other code forges to your factory](https://docs.warp.dev/factories/code-forges/other-code-forges/).
    
4.  On the “Set up your factory” screen, select the repositories your factory will work on. See [sizing a factory](https://docs.warp.dev/factories/#sizing-a-factory).
    
    ![The Set up your factory screen with a progress bar, docs entered in the repository search field, and matching repositories shown.](https://docs.warp.dev/_astro/quickstart-connect-repo.OWAAb31y_g5xlG.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    A repository search during factory setup.
    
5.  Enter a “Factory name”. This also sets the default [foreman name](https://docs.warp.dev/factories/factory-agents/#foreman-name), the handle your team @-mentions in Slack and Linear. Click **Next**.
    
    ![Factory setup with Docs Factory entered as the factory name, an optional description field, an avatar, and the Next button.](https://docs.warp.dev/_astro/quickstart-factory-details.BDdbZ17r_ZvjVe5.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    The factory name and optional details during setup.
    
6.  Choose which agents the foreman can dispatch. Leave **Code** enabled so this quickstart ends in a pull request. See [About factory agents](https://docs.warp.dev/factories/factory-agents/) for details.
    
    ![The Configure your Factory agents screen showing the foreman handle and enabled Triage, Spec, Code, and Review agents.](https://docs.warp.dev/_astro/quickstart-pick-agents.DkoBI3oe_Z9ewaS.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    Default factory agents enabled during setup.
    
7.  Optionally, connect Slack and an issue tracker. You can add either later from [Connect your factory](https://docs.warp.dev/factories/connect-your-factory/).
    

Warp creates the factory and opens its [dashboard](https://docs.warp.dev/factories/factory-dashboard/).

## Send your first work item

Send a request to your factory’s foreman from the Warp Factories web app. You can also send work from [Slack or an issue tracker](https://docs.warp.dev/factories/connect-your-factory/).

1.  In the web app sidebar, click **New Chat**.
    
2.  In the dropdown below the prompt input, choose your factory.
    
3.  Enter one small, verifiable change, then click the send arrow:
    
    ```text title="Example first request"
    Add a "Local development" section to README.md that summarizes the setup
    steps from CONTRIBUTING.md. Keep the change to that one file, run the
    repo's lint check, and open a pull request.
    ```
    
4.  The foreman dispatches the agents needed for the request and posts progress where it started. In the sidebar, click **Runs** to follow the [foreman and child runs](https://docs.warp.dev/factories/factory-dashboard/#inspect-runs). Requests for input also appear in your [inbox](https://docs.warp.dev/factories/factory-inbox/).
    
    If you sent the request from Slack, you can follow along in its thread:
    
    ![A Slack thread where the Warp Factories app replies with tracking and triage progress updates, including links to open the session and view it in the factory.](https://docs.warp.dev/_astro/slack-factory-thread-reply.IqsWzCLm_1o1zNQ.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    A factory Slack thread with live progress.
    
5.  When the foreman hands back the pull request, review the changes and validation results, then merge it according to your normal process.
    

## Next steps

-   [**Connect your factory**](https://docs.warp.dev/factories/connect-your-factory/) - Configure intake sources.
-   [**How Warp Factories work**](https://docs.warp.dev/factories/how-factories-work/) - Understand the work-item lifecycle.
-   [**Troubleshooting Warp Factories**](https://docs.warp.dev/factories/troubleshooting/) - Fix common setup and run issues.
