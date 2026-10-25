---
title: "Environments"
subtitle: "Build reusable cloud development environments so Droids start with your repositories and tools ready."
authors: []
published_date: null
source_url: https://docs.factory.com/environments/overview.md
origin: llms-txt
llms_txt: https://docs.factory.com/llms.txt
section: "Documentation"
fetched: 2026-10-25T18:18:02Z
---

# Environments

Build reusable cloud development environments so Droids start with your repositories and tools ready.

An **Environment** is a saved development environment that Droids can run on. Choose a source, add repositories, and define setup commands. Factory builds a reusable snapshot with the code cloned and tools installed, so each new instance starts from the same prepared baseline.

Environments are the successor to [Cloud Templates](/droid-computers/cloud-templates).

## When a reusable baseline helps

Use an Environment when you want to run multiple Droids without preparing a machine for every task. Build once, then start independent instances for bug fixes, code review, browser testing, or other work that needs the same repositories and toolchain.

An Environment is the baseline, not a shared working directory. Changes a Droid makes in one instance do not change the Environment or another Droid's files. Rebuild the Environment to update its baseline; commit and push work you want to keep.

## Choose your compute

| Option | What it provides | Use it for |
| --- | --- | --- |
| **Environment** | A reusable snapshot for new cloud instances | Repeatable setup and independent parallel Droids |
| **Droid Computer** | A persistent Factory-managed computer | Work that needs files and configuration to survive across sessions |
| **Remote Control** | Access to a computer you already manage | Your workstation, cloud VM, or on-premises machine |

You can also create a persistent [Droid Computer](/droid-computers/overview) from a Ready Environment. [Remote Control](/remote-control) connects your own computer; it does not build an Environment.

## Use the same baseline across workflows

[Delegations](/delegations) can use an organization Environment with **Dynamic** compute. [Automations](/software-factory/automations) can select an Environment as their run target. [Missions](/missions/overview) can use Environments for worker agents on separate instances.

Start by checking [access and source control prerequisites](/environments/prerequisites), then create an Environment in **Settings → Environments**. Availability depends on your organization's rollout and compute settings.

  **Prerequisites**
    Connect source control and configure runtime secrets.
  
  **Create an Environment**
    Prepare repositories and setup commands.
  

