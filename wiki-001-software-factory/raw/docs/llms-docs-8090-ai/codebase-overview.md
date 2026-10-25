---
title: "Codebase Connection"
subtitle: "Connect a GitHub or GitLab repository so agents can search, read, and stay in sync with your code."
authors: []
published_date: null
source_url: https://docs.8090.ai/codebase/overview
origin: llms-txt
llms_txt: https://docs.8090.ai/llms.txt
section: "Docs / Connections"
fetched: 2026-10-25T18:13:39Z
---

# Codebase Connection (/codebase/overview)

Connecting a repository lets 8090 Software Factory index your code so agents can search and read it, and it keeps that index current as your team pushes changes.

## Choose a provider [#choose-a-provider]

8090 Software Factory connects to repositories on GitHub and projects on GitLab. You can connect from either provider in the same project, and each connection tracks one selected branch.

| Provider | Account authorization    | Repository authorization                                                              |
| -------- | ------------------------ | ------------------------------------------------------------------------------------- |
| GitHub   | Link your GitHub account | Install the 8090 Software Factory GitHub App for the repositories you want to connect |
| GitLab   | Link your GitLab account | Select a project your GitLab account can access                                       |

Follow the steps for your provider:

* [Connect GitHub](#connect-github)
* [Connect GitLab](#connect-gitlab)

## Connect GitHub [#connect-github]

Connect a GitHub repository so agents can search and read your code.

  
    ### Open Codebase settings [#open-codebase-settings]

    Open your 8090 Software Factory project, then go to **Settings → Codebase** and choose the option to add a GitHub repository.
  

  
    ### Link your GitHub account [#link-your-github-account]

    If prompted, select **Link GitHub** and authorize 8090 Software Factory. Your linked account determines which GitHub repositories you can browse and connect.
  

  
    ### Install or update the GitHub App [#install-or-update-the-github-app]

    Install the 8090 Software Factory GitHub App for the organization or account that owns the repository, and give it access to the repository you want to use.

    If a repository is missing from the picker, select **Manage GitHub Access** and add it to the app installation.

    **Repository missing? You may need a GitHub admin**
      In a GitHub organization, only an owner or admin can install the 8090 Software Factory GitHub App and choose its repositories. If you are a member, your install becomes a request for an owner to approve, and the repositories don't appear in the picker until they do. Ask a GitHub organization owner to install the app and add the repository you need.
    
  

  
    ### Select the repository and branch [#select-the-repository-and-branch]

    Choose the repository, select the branch 8090 Software Factory should index, and confirm the connection.
  

## Connect GitLab [#connect-gitlab]

Connect a GitLab project so agents can search and read your code.

  
    ### Open Codebase settings [#open-codebase-settings-1]

    Open your 8090 Software Factory project, then go to **Settings → Codebase** and choose the option to add a GitLab project.
  

  
    ### Link your GitLab account [#link-your-gitlab-account]

    Select **Link GitLab** and authorize 8090 Software Factory on GitLab.com. 8090 Software Factory lists the projects and branches your GitLab account can access.

    The first time anyone in your organization connects a GitLab project, they need the **Maintainer** role on it, because that step creates a project access token in GitLab. After that, other members can connect the same project without it.
  

  
    ### Select the project and branch [#select-the-project-and-branch]

    Search for a GitLab project, choose the branch 8090 Software Factory should index, and confirm the connection. 8090 Software Factory uses the project access token to index your code and keep it in sync.

    **Project missing? Check your GitLab role and plan**
      8090 Software Factory only lists projects your GitLab account can access. The first connection to a project needs the **Maintainer** role, and the project must be on a GitLab Premium or Ultimate plan, because GitLab.com only offers project access tokens on those plans. If a project is missing or won't connect, ask a GitLab project or group Owner for Maintainer access, or ask a Maintainer to connect it first.
    
  

If the project access token later expires or is revoked, a Maintainer can select **Restore credential** in **Settings → Codebase**.

## After you connect [#after-you-connect]

The initial index usually takes 5 to 10 minutes. Once it finishes, agents can search and read the connected code.

Pushes to the selected branch trigger automatic reindexing. You can also use a repository row's actions menu to reindex manually or change the selected branch.

8090 Software Factory can also catch code that drifts from your Blueprints and Requirements. There are two ways, and both are off until you turn them on:

* **Detect Code Drift** is a recommended [automation](/modules/automations). It runs after code is pushed to the selected branch and leaves drift comments on the affected Blueprints and their linked Requirements.
* **[Drift Bot](#drift-bot)** checks pull requests before they merge and posts its findings on the pull request.

## Drift Bot [#drift-bot]

Drift Bot reviews pull requests on a connected repository. It checks the changed code against your project's Blueprints and Requirements and posts what it finds on the pull request. It flags code that contradicts a Blueprint or Requirement, and code that none of them cover yet. It works with GitHub pull requests and GitLab merge requests.

  
    ### Open the Drift Bot settings [#open-the-drift-bot-settings]

    Go to **Settings → Codebase**, open the repository's actions menu, and select **Drift Bot**.

    You can also turn it on while you connect a repository. After you pick a repository in the **Add Repository** or **Add GitLab Project** dialog, a **Drift Bot** section appears. Those settings are saved once the repository connects.
  

  
    ### Choose when it runs [#choose-when-it-runs]

    Both options are off by default.

    | Option                               | When Drift Bot runs                                                                                                            |
    | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
    | **On commit to branch with open PR** | When a pull request is opened or receives new commits. Draft pull requests are skipped until they are marked ready for review. |
    | **Manual**                           | When someone comments `/driftbot` on a pull request.                                                                           |

    **Manual** stays on whenever **On commit to branch with open PR** is on.
  

  
    ### Save [#save]

    Select **Save Changes**.
  

### What Drift Bot posts [#what-drift-bot-posts]

Each run posts a summary comment on the pull request or merge request. The summary lists each possible drift finding with the Blueprint or Requirement it concerns and the file and lines involved, or says that no drift was found. The most important findings also get their own comments on the lines they concern.

Drift Bot also sets a `drift-bot` commit status. The status passes when there is no drift, and fails when Drift Bot finds drift or the run fails.

### Who can set it up [#who-can-set-it-up]

* Saving Drift Bot settings needs the **Codebase Connection** Editor permission, which the built-in project **Owner** and **Editor** roles include. See the [permissions reference](/roles-and-access-control/permissions-reference#codebase-connection).
* The **Drift Bot** option only appears in the actions menu when your linked GitHub or GitLab account can access the repository.

Each run uses the access of the person who triggered it: the pull request's author on GitHub, the person who opened or updated the merge request on GitLab, or the person who commented `/driftbot`. Drift Bot only runs when that person is a member of your organization and has linked their GitHub or GitLab account in 8090 Software Factory.

### Several projects on one repository [#several-projects-on-one-repository]

Only one project can run Drift Bot for a repository: the first one to turn it on. Other projects connected to the same repository see "Drift Bot is already enabled by another project connected to this repository. Disable it there before enabling it here."

To move Drift Bot to another project, turn off both options in the project that has it. Do this before you unlink the repository or archive that project, because unlinking or archiving leaves Drift Bot assigned to it.

## Manage connections [#manage-connections]

* If your GitHub or GitLab authorization expires, reconnect your account from the prompt in **Settings → Codebase**.
* To connect a repository from a second provider, first link that account under **Settings → Connections → Accounts** with **Connect GitHub** or **Connect GitLab**. The add option for that provider then appears in **Settings → Codebase**.
* To stop using a repository in the current project, open its actions menu and select **Unlink from Project**.
* Unlinking removes the connection from the current project. It does not uninstall the GitHub App, unlink your GitHub or GitLab account, or remove the repository from the provider.
* For GitLab, when you unlink the last project in your organization that uses a GitLab project, 8090 Software Factory revokes the project access token it created there and stops listening for changes to that project.
