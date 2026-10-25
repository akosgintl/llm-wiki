---
title: "Delegations"
subtitle: "Delegate work to Droid from Slack, Linear, Jira, and Microsoft Teams with shared instructions, plugins, identity, and compute."
authors: []
published_date: null
source_url: https://docs.factory.com/delegations/index.md
origin: llms-txt
llms_txt: https://docs.factory.com/llms.txt
section: "Documentation"
fetched: 2026-10-25T18:18:02Z
---

# Delegations

Delegate work to Droid from Slack, Linear, Jira, and Microsoft Teams with shared instructions, plugins, identity, and compute.

Delegations lets your team send work to Droid from Slack, Linear, Jira, and Microsoft Teams. Mention Factory in a conversation or delegate an issue, and Droid works on a remote computer using your organization's agent profile.

For shared delegations, an administrator configures the instructions, plugins, service-account identity, and compute once. Team members can then delegate work from a connected app without choosing a computer for every request. Slack DMs use the sender's personal identity and connectors instead of that shared identity.

Delegation apps receive requests from your team. [Connectors](/harness/connectors) give Droid tools to use while carrying out those requests. Connecting a personal connector does not install the corresponding delegation app for your organization.

## Prerequisites

To configure Delegations, you need:

- A Factory organization on any paid plan, including [individual plans](/pricing/individuals) and [organization plans](/pricing/organizations).
- The **Manager** or **Owner** role in Factory.
- Permission to install or authorize the delegation app in your Slack workspace, Linear workspace, Jira site, or Microsoft Teams organization.
- Service-account access for your organization to configure shared execution.
- [Repository access](#repository-access-for-the-service-account) and any connectors needed by the identity that will run the work.

Individual plans and the Teams plan include one service account, reserved for Delegations. Factory creates it with the default agent profile. You can deactivate it but not delete it, and these plans cannot create other service accounts. Business and Enterprise plans can create additional [service accounts](/enterprise/identity-and-access#service-accounts) for other automation.

Team members who delegate work must have a Factory account in the connected organization. Use the same account email in Factory and the connected app so Factory can match the person making the request.

## Connect a delegation app

Open <a href="https://app.factory.ai/settings/delegations">**Settings → Delegations**</a> in Factory. Under **Delegation Apps**, select **Set Up for Org** for the app you want to connect. Follow its setup page to authorize the integration. For a connected app, select **Configure** to return to its setup and management options.

| App | How to delegate work | Setup notes |
| --- | --- | --- |
| [Slack](/delegations/slack) | Mention `@Factory` in a channel or send a direct message. | Invite Factory to channels where it should receive requests. |
| [Linear](/delegations/linear) | Assign an issue to Factory or mention `@Factory` in an issue comment. | Authorize Factory for the workspace and the teams that will delegate work. Follow the [Linear setup guide](/delegations/linear#connect-your-linear-workspace). |
| [Jira](/delegations/jira) | Select **Agents → Factory** on an issue or mention `@Factory` in an issue comment. | Install Factory for Jira and link the Jira site to your Factory organization. Follow the [Jira setup guide](/delegations/jira#install-and-connect-factory-for-jira). |
| [Microsoft Teams](/delegations/microsoft-teams) | Mention `@Factory` in a channel. | Link your Microsoft tenant and install the app in Teams. Follow the [Teams setup guide](/delegations/microsoft-teams#connect-and-install-the-app). |

A disabled **Set Up for Org** action means that app is not available for your organization yet.

## Personal and shared identity

Slack distinguishes personal conversations from shared channel work:

- **Direct messages to Factory** run as the person sending the message, with their personal Git credentials and connectors.
- **Channel requests using the Apps agent profile** run as its service account, with that account's Git credentials and connectors, not the sender's personal connections.

DMs use the Apps agent profile's instructions and model defaults. By default, a DM runs on a computer provisioned for the sender from the agent profile's Environment, not the service account's pool. To run your DMs on one of your own computers or a different Environment, set a **DM delegation machine** in your [personal delegation defaults](#set-personal-delegation-defaults). Without that setting, DMs require the agent profile to have an Environment. See [personal DMs and shared channels](/delegations/slack#personal-dms-and-shared-channels).

## Configure delegated sessions

Manage Environments in <a href="https://app.factory.ai/settings/environments">**Settings → Environments**</a>.

Under **Agent Profiles**, select **Edit** on **Apps**. This agent profile powers shared work delegated from Slack, Linear, Jira, and Microsoft Teams. Its service-account identity applies to shared channel and issue delegations; Slack DMs use the personal identity described above.

Factory creates a default agent profile, service account, and Environment when setting up eligible organizations. Review those defaults before delegating work. If setup could not complete, use the agent profile setup wizard to select an active identity and compute.

  **General**
    Choose the **Default model** and **Default reasoning level**. Leave the model on **Auto Model** to use [Factory Router](/model-independence/factory-router).

    Add **Custom Instructions** for behavior that should apply to every delegated session. For example, specify which tests to run, what a completion summary should contain, or when Droid should open a pull request.

    The agent profile's name is fixed, and **Access** is **Everyone**. Custom groups are coming soon.
  
  **Plugins**
    Add plugins that delegated sessions need. Enter the plugin name, choose its marketplace, and select **Add**.

    Marketplaces must first be registered under **Enterprise Controls → Plugins**. Plugins enabled organization-wide are included automatically. A plugin disabled organization-wide stays disabled even if it is listed in this agent profile.
  
  **Identity**
    Choose **Use Existing Service Account** or **New Service Account**. The selected account must be active.

    Shared delegated sessions run as this service account, not as the administrator editing the agent profile. Use the identity's controls to configure Git credentials, connectors, API keys, and computers. Make sure it can access the repositories and external tools the work requires. See [repository access for the service account](#repository-access-for-the-service-account).
  
  **Compute**
    Choose **Dynamic** and select an Environment, or choose **Persistent** and add computers to the service account's pool.

    Select **Finish** to save. Dynamic compute requires an Environment. Persistent compute requires at least one computer owned by the selected service account.
  

## Repository access for the service account

Shared delegations clone, fetch, and push repositories as the selected service account. They do not use your personal Git connections or the organization's source-control OAuth connection. Give the service account its own access to every repository the work needs, including every repository in the agent profile's Environment.

If the Environment includes a repository that the service account cannot access, shared delegations fail before Droid starts, even when the request does not mention that repository.

| Source control | How the service account gets access |
| --- | --- |
| GitHub | Install your organization's Factory GitHub App on the repositories. The service account uses the installation automatically, so no token is needed. |
| GitHub Enterprise Server | Install the GitHub App configured for your Factory organization on the repositories. See [service-account repository access](/enterprise/self-managed-scm#service-account-repository-access). |
| GitLab | Add a **GitLab group access token** in the service account's **Git Credentials**. |
| GitLab Self-Hosted | Connect your GitLab Self-Hosted instance first. Then add a **GitLab Self-Hosted group access token** for that instance in the service account's **Git Credentials**. |

Open **Git Credentials** from the service account's row in organization Settings, or from the Identity step of the agent profile setup wizard. Factory validates each token when you save it.

For a GitLab or GitLab Self-Hosted token:

- **Token type:** Use a group access token for the groups that hold your repositories. If your GitLab plan does not offer group access tokens, use a personal access token from a dedicated GitLab user instead of a teammate's account.
- **Scope:** Grant the `api` scope so Droid can clone, push branches, and open merge requests.
- **Role:** Grant at least the Developer role on the groups or projects Droid works in.
- **Expiration:** Choose an expiration date your team will track, and replace the token in **Git Credentials** before it expires.

If Factory rejects a token, check that it has the `api` scope, has not expired or been revoked, and belongs to the correct GitLab instance.

## Set personal delegation defaults

Team members can open **Settings → Session Defaults → Delegations** to set personal defaults for the work they delegate:

- **DM delegation machine:** where your Slack DMs to Factory run. Pick one of your active computers or a Ready Environment, or choose **Org default** to use the Apps agent profile's Environment. Computers blocked by organization policy are not offered. This setting applies only to DMs; channel requests and issues use the service account's compute.
- **Default delegation model** and **Default delegation reasoning level:** a personal model selection overrides the Apps agent profile's model when organization policy allows it. Its reasoning preference applies to that selected model. Choose **Org default** to use the agent profile's model and reasoning settings instead.
- **Your custom delegation instructions:** instructions added to every delegation you start, including follow-up messages in those sessions. They are added after the Apps agent profile's instructions and do not replace or override them. You can save instructions while leaving the model on **Org default**.

The model, reasoning, and instruction defaults follow the person who starts the delegation, so they apply to Slack DMs, Slack channel requests, Microsoft Teams channel requests, and Linear and Jira issues you delegate. None of these defaults change identity or connector access: Slack DMs that use the Apps agent profile run with the sender's personal identity and connectors, while shared channel and issue delegations use the service account's. Personal defaults do not make a shared session run as the requester.

## Delegate your first task

Start with a small, reviewable request in a connected app. Include the repository, the desired outcome, and how Droid should verify the result.

For example, mention Factory in Slack or Teams:

> @Factory Investigate the failing checkout test in the storefront repository. Fix the cause, run the relevant tests, and open a pull request with a summary of the change.

In Teams, include the relevant context in the mentioning message. Droid does not yet receive earlier channel or thread messages. See [Delegate a task from a channel](/delegations/microsoft-teams#delegate-a-task-from-a-channel).

For Linear or Jira, put those details in the issue description, then assign the issue to Factory or mention Factory in a comment. In Jira, use the [Agents picker or an issue comment](/delegations/jira#delegate-an-issue).

Review Droid's response and any linked session or pull request. Send follow-up instructions through the originating conversation or issue where supported. Check the test results and proposed changes before merging.

## Require independent GitHub review

For shared delegations that use the Factory Droid GitHub App, Factory is the pull request author, not the teammate who requested the work. GitHub prevents authors from approving their own pull requests, but the requester can still approve a Factory-authored pull request. With only one approval required, the requester can satisfy the review requirement and, if otherwise permitted, merge without another person's review.

To require another reviewer, configure a branch protection rule or ruleset for each target branch in GitHub:

- **Apply the requirement to all pull requests:** Set the required approval count to two. This also affects pull requests opened by teammates.
- **Apply the requirement only to Factory-authored pull requests:** Add a required status check that enforces two human approvals for pull requests opened by `factory-droid[bot]` (the Factory Droid GitHub App).

See GitHub's documentation on [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) and [status checks](https://docs.github.com/en/pull-requests/reference/status-checks).

## Troubleshooting

  **Delegations is missing from Settings**
    Confirm that your organization is on a paid plan with an active subscription and that you are a Manager or Owner. Delegations settings are not available in airgapped deployments. If the page is visible but Agent Profiles is missing, ask your Factory account team to check service-account eligibility.
  
  **Factory cannot match my account**
    Make sure the email on your connected-app account matches your Factory account email, and that you belong to the connected Factory organization. Then retry the request.
  
  **The app is already connected to another Factory organization**
    Each delegation app workspace, such as a Slack workspace, Linear workspace, or Jira site, can connect to only one Factory organization at a time. Check which Factory organization you selected. If the workspace needs to move, ask a Manager or Owner of the currently connected organization to disconnect it there first, then connect it to the intended organization. Reconnecting a workspace to the organization that already owns it still works.
  
  **The execution identity is inactive**
    An administrator must choose an active service account in the agent profile's Identity step. Check that its Git credentials and connectors are ready for the work.
  
  **Shared delegations fail before Droid starts**
    Check that the service account can access every repository in the agent profile's Environment, not only the repository named in the request. GitLab and GitLab Self-Hosted repositories require a token in the service account's **Git Credentials**; GitHub repositories require the GitHub App installation. See [repository access for the service account](#repository-access-for-the-service-account). Some apps, such as Jira, can show only a generic error in this case.
  
  **The delegation Environment is not ready**
    Check that the selected Environment still exists and has a ready build. If provisioning fails, retry. If Factory reports that managed compute is unavailable, ask an administrator to review compute policy and usage limits.
  
  **My DM delegation machine is unavailable**
    The computer or Environment you picked as your **DM delegation machine** was deleted, is not active, is blocked by organization policy, or cannot launch. Pick another machine, or choose **Org default**, under **Settings → Session Defaults → Delegations**.
  
  **No delegation machines are available**
    For Persistent compute, check that computers belong to the selected service account and have finished provisioning. Computers connected through Remote Control must be online with a current Droid daemon.
  
  **All delegation machines are busy**
    Retry after a session finishes. An administrator can add computers or adjust the per-machine parallel worker limit. Increasing the limit means more sessions share the same resources.
  

  **Identity & Access**
    Configure service accounts and Git credentials for shared work.
  
  **Remote Control**
    Connect your own computers for persistent execution.
  
  **Slack**
    Connect Factory and delegate work from Slack channels and DMs.
  
  **Linear**
    Connect Factory and delegate work from Linear issues.
  

