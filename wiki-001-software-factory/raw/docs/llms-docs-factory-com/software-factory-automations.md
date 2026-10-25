---
title: "Custom Automations"
subtitle: "Create, configure, and monitor automations that run Droid on a schedule, from Slack messages, on GitHub events, or from inbound webhooks."
authors: []
published_date: null
source_url: https://docs.factory.com/software-factory/automations.md
origin: llms-txt
llms_txt: https://docs.factory.com/llms.txt
section: "Documentation"
fetched: 2026-10-25T18:18:02Z
---

# Custom Automations

Create, configure, and monitor automations that run Droid on a schedule, from Slack messages, on GitHub events, or from inbound webhooks.

Automations turn Droid into a teammate for work that keeps coming back. Each automation starts a Droid session when its trigger fires: on a schedule, when a message lands in a Slack channel, on a GitHub event, or when another service sends a webhook.

## What an automation is

  
    What starts a run: a schedule, a Slack message, a GitHub event, or an HTTP `POST` to the automation's webhook URL.
  
  
    The prompt Droid follows on every run, with an optional model and reasoning level.
  
  
    Who each run acts as: you, or a [service account](/enterprise/identity-and-access#service-accounts) your team shares.
  
  
    Where Droid works: a [Droid Computer](/droid-computers/overview), your own machine through the desktop app, or GitHub Actions for GitHub automations.
  
  
    Whether the automation is private to you or shared with your organization, and who can open the sessions its runs create.
  

## Find your automations

Open <a href="https://app.factory.ai/automations"><strong>Automations</strong></a> from the Factory App sidebar. Your first visit opens a short tour of the page.

The **Private** tab lists automations only you can see, and the **Shared** tab lists automations shared with your organization. Search matches an automation's title, description, owner name or email, and ID, so you can paste an ID from an alert email or a log. While an automation is still being created, search also matches its setup session ID. Select the filter button to narrow the list by trigger type.

| Column | What it shows |
| --- | --- |
| **Title** | The automation's name and status, plus a warning icon when it has recent alerts. |
| **Owner** | Who owns the automation. Shown on the **Shared** tab. |
| **Trigger type** | **Scheduled**, **Slack**, **GitHub**, or **Webhook**. |
| **Runs on** | The repositories a GitHub automation covers, or the computer other automations run on. |

Select a row to open the automation, or use its **⋯** menu for quick actions. GitHub automations are read from workflow files in your repositories; select the refresh icon in the page header to scan them again.

## Create an automation

Select **New automation** to open the marketplace. It groups every starting point by how much it sets up for you. Search and the trigger filter (**Scheduled**, **Slack**, **Webhook**, or **GitHub**) apply across all sections. When Factory knows your role or which apps you've connected, up to three **Recommended for you** picks lead the list.

If **New automation** opens a menu instead, choose **Create with Template** to browse templates grouped by trigger type. **Create with Droid** in that menu opens a new session with a request already drafted. Send it, and Droid explains how automations work, then asks what to run and what should start it.

### Popular use cases

Starters are ready-made jobs with the prompt, trigger, and defaults filled in. Point one at your repositories and channels, then create it.

| Starter | Trigger | What it does |
| --- | --- | --- |
| **Ticket to PR** | Every 15 minutes | Picks up ready tickets from Linear or Jira one at a time and drives each to an open pull request. |
| **PR Reviewer (GitLab/GitHub)** | Every 30 minutes, 9:00 to 17:00 on weekdays | Reviews new pull or merge requests and posts one review comment per head commit. |
| **Daily Status Digest** | Weekdays at 9:00 | Sends a morning digest of your PRs and tickets: what needs you, what waits on others, and what moved since yesterday. |
| **Code Health** | Weekdays at 6:00 | Rotates through dependency audits, dead code, coverage gaps, and stale docs, landing one small maintenance PR per run. |
| **Meeting Notes Sync** | Weekdays at 8:00, 13:00, and 18:00 | Summarizes finished meetings and files action items into Notion, your CRM, or your tracker. |
| **Error Triage** | Hourly | Polls Sentry, Datadog, or another error source, investigates the errors that matter, and opens a fix PR when safe. |
| **Slack Digest** | Weekdays at 8:00 | Sends you a private DM with the threads waiting on you, mentions, and channel highlights. |
| **Slack Bug Fixer** | Slack message | Turns bug reports into tickets, posts a root-cause hypothesis in the thread, and opens a fix PR for small changes. |
| **Channel Q&A** | Slack message | Answers questions from your docs, Notion, tickets, and code, citing sources in the thread. |
| **Slack Ticket Filer** | Slack message | Files actionable messages as deduplicated tickets for the right team and posts the link in the thread. |
| **Alert Responder** | Webhook | Investigates Sentry, Datadog, or PagerDuty alerts as they fire, with a fix PR when safe. |
| **CI Failure Triage** | Webhook | Classifies failed GitHub Actions or GitLab pipelines as flaky, infrastructure, or regression, and names the responsible commit. |
| **New Issue Investigator** | Webhook | Checks each new Linear, Jira, or GitHub issue for duplicates, likely cause, and files involved, with a PR for trivial fixes. |
| **Review Comment Fixer** | GitHub: comment added | Makes the change a teammate asks for in a pull request comment, pushes one commit, and replies. |
| **Test Coverage** | GitHub: pull request | Adds focused tests for the code each pull request changes and comments on what is now covered. |
| **Docs Refresh** | GitHub: push | Keeps the docs in your repository current with each push to the default branch, through a pull request. |

Starter schedules are in UTC, so adjust **Frequency** before you create one. Webhook starters appear only when [webhook triggers](#webhook-triggers) are enabled for your organization.

Starter prompts mark values only you can supply, such as a repository or Slack channel, with placeholders like `{{org/repo}}`. A scheduled starter's setup session asks you for these values. Slack, webhook, and GitHub starters run the prompt as written, so their forms block creation until you replace every placeholder.

### Guided setups

Guided setups are built-in automations with a setup form tailored to the job.

| Guided setup | Trigger | What it does |
| --- | --- | --- |
| **Triage** | Scheduled | Triages incoming work on a schedule and acts on what needs attention. See [Triage](/software-factory/triage). |
| **PR Babysitter** | Scheduled | Watches your open pull requests and drives failing CI to green. |
| **Incident Response** | Slack | Investigates alerts that bots post in incident channels and runs root-cause analysis. See [Incident Response](/software-factory/incident-response). |
| **Code Review** | GitHub | Reviews pull requests automatically. See [Automated Code Review](/software-factory/code-review-ci). |
| **QA** | GitHub | Generates and runs QA checks against your changes. See [Automated QA](/software-factory/automated-qa). |
| **AutoWiki** | GitHub | Refreshes a repository's wiki on each push. See [Automatic Refresh](/software-factory/wiki/auto-refresh). |
| **Security Audit** | GitHub | Runs a scheduled deep security review of a repository. See [Security Review](/software-factory/security-review). |

### Start from scratch

Pick **Custom scheduled automation**, **Custom Slack automation**, **Custom GitHub automation**, or **Custom webhook automation**, then write the prompt yourself. The webhook option appears only when webhook triggers are enabled for your organization.

### Create with Droid

Select **Create with Droid** at the top of the marketplace to describe the job in your own words instead of filling in a form. The Automations page offers the same button while you have no automations yet. If a marketplace search finds nothing, **Describe it to Droid** starts the same flow with your search text.

  **Describe the job**
    Under **What should it do?**, describe the automation or pick one of the examples. Mention what should start it and where results should go, if you know. **Name** is optional; Droid suggests one if you leave it blank.
  
  **Continue in chat**
    Select **Continue in chat**. Factory opens a new session with your request filled in but not sent, so you can choose where the session runs first.
  
  **Answer Droid's questions**
    Send the message. Droid asks for anything it still needs, including whether a schedule or a webhook should trigger the automation, then creates it with its [automation tools](#create-automations-from-a-droid-session).
  

### Finish creating

The button at the bottom of the create form depends on the automation:

| Button | When it appears | What happens |
| --- | --- | --- |
| **Create with session** | Scheduled automations, QA, and organization-wide GitHub installs | Factory creates the automation and opens a setup session. For a scheduled automation, Droid asks one or two follow-up questions, fills in any placeholders, and writes the automation's files on the selected computer. |
| **Create** | Slack, webhook, and most GitHub automations | Factory creates the automation. For a GitHub automation, Factory opens a setup pull request in each selected repository. |
| **Open existing** | A QA, AutoWiki, Security Audit, or organization-wide Code Review setup that matches one you already have | Factory opens the existing automation instead of creating a duplicate. |

## Configure an automation

Every create form is split into sections. Which sections appear depends on the trigger:

| Trigger | What you configure |
| --- | --- |
| **Scheduled** | Frequency, where it runs, instructions, and optional settings such as a working directory, a dashboard, and memory. |
| **Slack** | Channels, which senders start a run, where it runs, instructions, and message filters. |
| **GitHub** | Repositories, the events or schedule that start a run, GitHub Action parameters, and instructions. |
| **Webhook** | Where it runs, instructions, and an optional payload filter. |

### Schedules

Enter **Frequency** in plain words, such as `every Monday at 9am PST`, or as a five-field cron expression, such as `0 9 * * 1`. Before you save, the form previews when the automation runs, in UTC and in any time zone you typed.

- Cron expressions run in UTC.
- Factory converts a time zone in plain words to a fixed UTC schedule when you save. The schedule doesn't follow daylight saving time changes, so update it after the clocks change if the local time matters.
- A frequency without a time, such as `daily`, runs at 9:00 UTC.

### Slack channels and messages

A Slack automation starts a run when a matching top-level message is posted in one of its channels. Thread replies never start a run. The channel picker lists only channels Factory can access, so invite Factory to private channels first. See [Slack](/delegations/slack) to connect your workspace.

To match channels by name, enter a pattern with the `*` wildcard, such as `alerts-*`. A pattern covers the matching public channels Factory is already in, and Factory joins matching public channels as they're created. Patterns never cover private channels, and they don't pick up channels renamed to match or channels created while the automation is paused. Each pattern needs at least three characters besides `*` and can be up to 80 characters long. An automation can have up to 25 patterns, covering up to 1,000 channels.

**Trigger on messages from** limits runs to messages from **Anyone**, **Humans only**, or **Bots only**. **Additional settings** narrow which messages start a run:

  
    Only messages that contain one of these keywords start a run. Matching ignores case and includes the text of blocks and attachments, where alert bots often put their content.
  
  
    Messages that contain one of these keywords never start a run, even when they also contain a keyword.
  
  
    Messages from these senders never start a run. Enter a Slack member ID, a bot ID, or a bot's display name.
  

Each run replies in the thread of the message that started it. When several automations match the same message, the first one replies in that thread. Each of the others posts a new message in the channel that links to the original and replies in its own thread.

### GitHub events

A custom GitHub automation runs in GitHub Actions. Under **Triggers**, add the events that start a run: **Pull request opened**, **Pull request**, **Comment added**, **New push to branch**, **Label change**, or **Checks completed**. You can also add a schedule. Under **Additional settings**, **GitHub Action Parameters** set how the workflow runs.

Creating a GitHub automation opens a setup pull request in each selected repository. Merge it to turn the automation on. A custom GitHub automation can't post comments, push commits, or open pull requests until its workflow file is on the default branch, so runs that start before you merge the setup pull request fail.

The QA guided setup also asks for a **Setup computer**, where Droid creates the automation. QA runs themselves happen in GitHub Actions.

### Where it runs

The **Where it runs** section sets the identity, computer, and session visibility of each run for scheduled, Slack, and webhook automations.

  
    Shown to users with the Manager or Owner role when your organization can use service accounts. Leave it at **No selection (default)** to run as yourself, or pick a service account to run under its identity and billing.
  
  
    The target each run uses. Scheduled and Slack automations can run on your own machine through the desktop app or on a Droid Computer. Webhook automations can't run on your own machine. With a service account selected, the computer list is scoped to that account. When Environment launching is enabled, the picker can also list Ready Environments accessible to the selected run identity.
  
  
    Who can open the sessions runs create. **Private** limits them to the run identity. **Team** lets others in your organization review them.
  

For scheduled and webhook automations, runs as yourself use your connector access, and their Slack posts come from your account. Runs as a service account use its connector access and post to Slack as Factory. Slack automations always reply as Factory.

When you pick a remote computer, most create forms show an **MCP servers** row. Select **Configure** to add and authenticate MCP servers on that computer before the automation runs.

If your organization permits Environment launches, **Run on** can offer Ready Environments when you run as yourself or an eligible service account. Scheduled automations open a setup session on a new instance with **Create with session**; Slack and webhook automations use **Create** without a setup session. Each Environment-backed run starts on a fresh computer rather than reusing a setup instance or a previous run's computer. See [Configure automation compute](/environments/run-droids#configure-automation-compute).

Factory-managed Droid Computers host up to 10 automations each, with at most 5 scheduled for the same minute. The form warns you as a computer fills up and blocks a computer that is full. Your own machines have no limit.

### Visibility and session privacy

Two separate controls decide who sees what:

- **Share**, in the form header, sets whether the automation itself is **Private** or **Shared** with your organization. Choosing **Shared** also switches **Session privacy** to **Team**, and choosing **Private** switches it back to **Private**.
- **Session privacy** sets who can open the sessions runs create. You can change it independently after picking a visibility.

Choosing a service account under **Run as service account?** sets the automation to **Shared** and its sessions to **Team**, so the team can follow the runs. You can change both afterward.

### Instructions, model, and reasoning

The instructions section holds the prompt Droid follows on every run. For a webhook automation, it describes what Droid does when an event arrives. Pick a model and a reasoning level from the controls below the prompt; some guided GitHub setups put them under **Additional settings** instead. If you leave them unset, runs use the default model at that model's default reasoning level.

### Additional settings

  
    Optional summary of up to 1,024 characters, shown on the automation's detail page. Available for scheduled, webhook, and Code Review automations.
  
  
    Where runs start. Scheduled automations default to `~/.factory/automations/<slug>`. Slack automations start in the home directory when this is blank.
  
  
    What the dashboard Droid builds for each run should show. Scheduled automations display it on the **Dashboard** tab.
  
  
    What carries over between runs so the automation gets better over time. Scheduled automations only.
  

## Webhook triggers

 A webhook automation runs when an external service sends an HTTP `POST` to a URL that Factory creates for that automation, so any tool that can send a webhook can start a Droid run. Webhook runs execute on a Droid Computer or an Environment. Access is limited while the trigger is in preview, so contact [support@factory.com](mailto:support@factory.com) to enable it for your organization.

### Webhook URL and secret

Right after you create the automation, the **Webhook created** dialog shows its credentials once:

| Field | What it's for |
| --- | --- |
| **Webhook URL** | The endpoint senders post to, in the form `https://api.factory.ai/api/webhooks/automations/<webhook-id>`. |
| **Secret header** | The `X-Webhook-Secret` header, with the secret filled in, that authenticates each request. |
| **Secret** | The secret by itself, for tools with separate fields for a header's name and value. |
| **URL with secret** | The webhook URL with the secret added as a `secret` query parameter, for senders that only accept a URL. |
| **Test command** | A `curl` command that sends a test delivery. |
| **Secret fingerprint** | Identifies the stored secret without revealing it. Copy it if you want a record of which secret is active. |

  Copy the secret before you close the dialog. Factory stores only a hash of it and can't show it again. Rotating the secret opens the same dialog, titled **New webhook secret**, with a new secret. The webhook URL stays the same, but the old secret stops working immediately for every sender still using it.

Use the header whenever the sender can add request headers, because it keeps the secret out of the URL. GitHub and most other services only let you enter a URL, so give those the **URL with secret**. A secret in a URL can show up in the sender's logs and delivery history, so rotate it if it leaks.

Run the **Test command** to confirm the automation is wired up. It looks like this:

```bash
curl -X POST 'https://api.factory.ai/api/webhooks/automations/<webhook-id>' \
  -H 'Content-Type: application/json' \
  -H 'X-Webhook-Secret: <secret>' \
  -d '{"event":"test"}'
```

Factory passes the raw request body to the run, so Droid can read the event it was triggered by. The receiver answers right away, before the run starts:

| Response | Meaning |
| --- | --- |
| `200` | The delivery was accepted. Check the automation's **Events** feed for what happened next. |
| `401` | The secret is missing or wrong. |
| `404` | The URL is unknown, or the automation was deleted. |
| `413` | The body is larger than 200 KiB. |
| `429` | Too many requests reached this URL within a minute. The limit is 60 accepted requests per minute. |

### Filter which deliveries start a run

A **Payload filter** is an optional JavaScript regular expression tested against the raw request body. Deliveries that don't match are recorded as **Filtered** and don't start a run. Leave it empty to run on every delivery.

For example, `"action"\s*:\s*"opened"` starts a run only for payloads that carry that field, which keeps a busy event stream from running the automation on every message.

### Review deliveries

Every accepted request appears in the automation's **Events** feed as a delivery, so a webhook that fired without starting a run always has an explanation. Factory keeps delivery records for 30 days and records the outcome rather than the payload.

| Status | What it means |
| --- | --- |
| **Dispatched** | The delivery passed every check and started a run. |
| **Filtered** | The body didn't match the payload filter. |
| **Deduped** | An identical body arrived within the previous 10 minutes, so the delivery didn't run again. |
| **Rate-capped** | The automation already started 10 runs this hour. The limit resets at the top of the next hour. |
| **Skipped** | The automation was paused, a previous run was still in progress, its computer was over capacity, or webhook triggers were turned off for your organization. |
| **Failed** | The delivery was accepted, but the run couldn't start. |

## Manage an automation

Select an automation to open its detail page. A scheduled automation has an **Overview** tab with its settings, recent activity, and a 7-day success rate, and a **Dashboard** tab with the dashboard Droid builds on each run. Webhook detail pages also show the webhook URL and payload filter.

| Action | What it does |
| --- | --- |
| **Run now** | Starts a run immediately. Available for scheduled automations, and for webhook automations from their **⋯** menu on the Automations page. |
| **Edit** | Changes settings in place. Select **Save** to apply them. |
| **Edit with session** | Opens **Review & Improve**, which starts a Droid session that analyzes the automation and suggests changes to its prompt, memory, and outputs. Add an optional focus, then select **Start session**. Available for scheduled automations that don't run on an Environment, and for Slack automations that run on your own machine. |
| **Pause** / **Resume** | Stops or restarts triggers without deleting anything. |
| **Share** | Switches the automation between private and shared. |
| **Fork** | Copies a scheduled automation to a computer you choose. See [Fork an automation](#fork-an-automation). |
| **Rotate secret** | Issues a new webhook secret and invalidates the old one immediately. |
| **Connect to computer** | Connects to the remote computer a scheduled automation runs on, so you can run or change it. |
| **Delete** | Deletes the automation. |

Only the owner can run, edit, pause, share, or delete an automation. Anyone who can see a scheduled automation can fork their own copy.

A scheduled automation's files live on its computer, so the owner also needs to reach that computer to run or change it:

- For an automation on your own machine, use the desktop app on that machine.
- For an automation on a remote computer, select **Connect to computer** on its detail page first.

Slack and webhook automations are stored in Factory, so you can manage them from anywhere. GitHub automations are changed through pull requests to their workflow files.

**Delete** always works, even when the computer is unreachable. If a scheduled automation's files appear to live on another machine, Factory first warns you that deleting it may lose data there. Deleting a scheduled automation removes its files and memory from its computer, and deleting a webhook automation retires its URL. Sessions from earlier runs aren't deleted.

### Change where it runs

In the edit form, **Run as** and **Run on** are read-only, because an automation's run identity and computer can't change in place:

- To run a scheduled automation somewhere else or as someone else, [fork it](#fork-an-automation), then delete the original.
- To move a webhook automation to another Droid Computer, ask Droid to change its computer with the **EditAutomation** tool.
- To change where a Slack automation runs, create a new one and delete the old one.

### Events feed

The **Events** feed on each detail page lists what happened, newest first, with times in UTC. Use the filter on the **Event** column to show one kind at a time:

  
    Each run's outcome and duration, with a link to its session.
  
  
    Problems that didn't produce a session, such as a run that failed to start, an automatic pause, or a stretch of missed runs.
  
  
    Each webhook delivery, with the statuses described in [Review deliveries](#review-deliveries). Shown for webhook automations only.
  

## Fork an automation

Forking copies a scheduled automation to a computer you choose. You can fork any scheduled automation you can see, including your own. The original doesn't change.

  **Open the fork options**
    Open the automation and select **Fork**, or choose **Fork** from its **⋯** menu on the Automations page. The **Fork Options** dialog opens.
  
  **Choose who runs it**
    If you have the Manager or Owner role and your organization can use service accounts, **Run as service account?** appears. Leave it at **No selection (default)** to run the fork as yourself, or pick a service account.
  
  **Choose a computer**
    Under **Select host computer**, pick a computer that belongs to the identity you chose, and wait for Factory to connect to it. You can't fork onto a computer that isn't connected or is already full.
  
  **Create the fork**
    Select **Fork**.
  

A personal fork is private. A service-account fork is shared with your organization automatically, which gives the team a stable run identity and environment. You stay the fork's owner; the service account is only the identity its runs use.

## Run health and alerts

Each automation shows a status in the list:

| Status | What it means |
| --- | --- |
| **Creating** | The setup session is still creating the automation. |
| **Running** | A run is in progress. |
| **Active** | The automation is on and waiting for its next trigger. |
| **Paused** | Triggers don't start runs until you resume it. |
| **Degraded** | Its first run, or a retried run, failed. It keeps running on schedule. |
| **Failed** | The latest run failed. |

A run that stops reporting progress is marked failed, and the next scheduled run proceeds as normal.

### Automatic pauses

Factory pauses an automation automatically when it can't run reliably. The reason appears in the **Events** feed and in alert emails. Fix the cause, then select **Resume**.

| Alert | When it happens |
| --- | --- |
| **Paused after repeated failures** | Five scheduled runs in a row failed. For an automation on your own machine, a run that stops reporting progress counts as a failure. |
| **Paused after 10 days of missed runs** | An automation on your own machine hasn't run for 10 days. |
| **Paused: computer over capacity** | Its Droid Computer hosts more than 10 automations, or more than 5 scheduled for the same minute. |
| **Paused: computer no longer exists** | Its Droid Computer was deleted. Set the automation up on another computer, as described in [Change where it runs](#change-where-it-runs). |
| **Paused: computer owner no longer active** | The owner of its Droid Computer left your organization. |
| **Paused: Droid Computers disabled** | Droid Computers were turned off for your organization or your account. |
| **Paused: organization deactivated** | Your organization was deactivated. Resume the automation after it's reactivated. |

Automations that run on your own machine depend on that machine being awake, online, and running Droid. If a scheduled run hasn't started within 15 minutes of its scheduled time, Factory records the missed run and alerts you, then reminds you each day while runs keep being missed. Runs pick up again on their own once the machine is back. If runs are still being missed after 10 days, the automation pauses. To recover, make sure the machine is awake, online, and running Droid, then select **Resume**.

### Alert emails

Alert emails go to the automation's owner. The first time an automation fails in a way that needs attention, Factory emails you right away. After that, alerts roll into a digest sent at most once a day, which lists up to 25 automations; the Automations page shows the rest. To stop these emails, turn off **Automation Alert Emails** under **Settings → General → Email Notifications**. Automations owned by a service account, such as ones created with its API key, don't send alert emails.

### Prompt size limit

A scheduled automation's instructions live in the body of its `HEARTBEAT.md` file, which can be up to 256 KiB of UTF-8 text. Runs are told not to edit `HEARTBEAT.md` unless its instructions say to, because anything written there becomes an instruction for every later run. The file sits in the automation's folder, alongside the files runs read and update:

```text title="automation-folder.txt"
~/.factory/automations/<slug>/
├── HEARTBEAT.md   # Instructions for every run
├── VISUAL.html    # Dashboard Droid updates each run
├── memory/        # State and notes carried between runs
├── reports/       # Run reports
└── skills/        # Skills for this automation, if it has any
```

Skills in the `skills/` folder load in this automation's runs and in sessions that start inside its folder. See [Where skills live](/harness/skills#where-skills-live).

If `HEARTBEAT.md` grows past the limit, Factory doesn't edit or truncate the file:

- An existing automation keeps syncing its other settings, but keeps its last accepted prompt until the file fits again.
- A new automation isn't created until the file fits.

To recover, move accumulated notes into a file under `memory/` and run output into `reports/`, then trim `HEARTBEAT.md` back to the instructions.

## Create automations from a Droid session

Droid can create and manage automations from any session. Ask in plain language, such as "create a scheduled automation that summarizes yesterday's merged pull requests every weekday at 9am", and Droid uses these tools:

| Tool | What it does |
| --- | --- |
| **CreateAutomation** | Creates a scheduled automation on this machine or on a Droid Computer, or a webhook automation on a Droid Computer. |
| **ListAutomations** | Lists scheduled automations on this machine, or scheduled and webhook automations on Droid Computers. |
| **ReadAutomation** | Shows one automation. For a webhook automation, it includes the payload filter and recent deliveries. |
| **EditAutomation** | Changes an automation's name, prompt, model, or status. Automations on Droid Computers also accept reasoning level, schedule, and description changes. Webhook automations can also move to another computer, change their payload filter, or rotate their secret. |
| **DeleteAutomation** | Deletes an automation and retires any webhook URL. |

- A scheduled automation created on a Droid Computer runs once right away.
- The model can be a model ID, a display name, or `cheapest` for the lowest-cost available model.
- A webhook automation's URL and secret appear once in the tool result. Droid relays both to you, because the secret can't be retrieved later.
- With the Manager or Owner role, you can ask Droid to run a scheduled automation on a Droid Computer as a service account. Name the service account's computer it should use, or ask Droid to list that account's computers first. The automation defaults to **Shared** with **Team** session privacy unless you ask for something else.

Whether Droid asks before using these tools depends on your [autonomy level](/autonomy-and-safety/auto-run). Creating or editing an automation is medium risk. Deleting one, or creating one that runs as a service account, is high risk, and the approval prompt shows the service account, computer, and visibility.

  
    Set up the persistent computers automations run on.
  
  
    Give shared automations a stable team identity.
  
  
    Connect Slack so automations can listen to channels.
  
  
    Control when Droid asks before running risky tools.
  

