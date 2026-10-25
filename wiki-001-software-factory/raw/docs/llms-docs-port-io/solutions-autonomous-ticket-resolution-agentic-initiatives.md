---
title: "Agentic initiatives"
subtitle: "Run one coding agent across every service that needs the same change, from a single governed initiative, tracked per service and as a portfolio."
authors: []
published_date: null
source_url: https://docs.port.io/solutions/autonomous-ticket-resolution/agentic-initiatives.md
origin: llms-txt
llms_txt: https://docs.port.io/llms.txt
section: "solutions"
fetched: 2026-10-25T18:18:27Z
---

# Agentic initiatives

Most ATR patterns act on one thing at a time: a ticket arrives, it gets enriched, an agent picks it up. An agentic initiative inverts that. You start from a change that many services need, and Port fans a coding agent out across all of them in one governed run.

The initiative holds the instruction once. Each service it touches becomes its own tracked run, with its own pull request, its own status, and its own place in the approval flow. One run can cover two services or two hundred.

The natural trigger is a scorecard. A rule like "every service has a CODEOWNERS file" already evaluates your whole catalog continuously, so it already knows which services fall short. That list of failing services is the initiative's target list, no separate backlog required.

<!-- -->

## The problem it solves[​](#the-problem-it-solves "Direct link to The problem it solves")

Standards drift for a reason: every service was compliant when it was created, and nobody owns going back to check. A scorecard catches the drift. The work left over is converting "14 services are missing CODEOWNERS" into 14 pull requests, without spending a day doing it by hand.

| Without agentic initiatives                                                                     | With agentic initiatives                                                                                            |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| ❌ A fleet-wide change means a ticket per service, or asking someone to "get to it eventually." | ✅ One instruction targets every service that needs the change.                                                     |
| ❌ Tracking progress means a spreadsheet, or checking each repo individually.                   | ✅ One entity tracks every fix in flight: pending, running, PR opened, merged, failed.                              |
| ❌ Every fix gets the same review process, regardless of the service's risk.                    | ✅ Approval policy follows service criticality. Low-risk services can auto-merge; tier-1 services wait for a human. |
| ❌ A new service added next quarter has to be found and fixed separately.                       | ✅ The same scorecard flags it. The next initiative against that rule already includes it.                          |

## The mental model[​](#the-mental-model "Direct link to The mental model")

An agentic initiative reuses the same building blocks as the rest of [Autonomous Ticket Resolution](/solutions/autonomous-ticket-resolution/overview/.md): the [context lake](/solutions/autonomous-ticket-resolution/overview/.md#how-port-makes-it-work), scorecards, and workflows. What changes is the shape of the work: one instruction, many targets.

* **The trigger is a set, not a single item.** A scorecard rule, a catalog query, or a hand-picked list defines which services the initiative covers. A failing rule is the most common source, because the catalog already maintains it.
* **One initiative, many run targets.** An `agentic_initiative` entity represents a single fix effort. Each service it touches becomes a `run_target` entity: its own status, its own pull request, its own CI result. The initiative rolls those up into live counts.
* **Governance follows the target, not the run.** The initiative's `approval_policy` can route by service criticality: auto-merge for low-risk services, a human checkpoint for anything tier-1. Same agent, same instruction, different gate per service.

The shape of one run:

`A set of services that need the same change` → `Agentic Initiative (Draft)` → *platform engineer approves* → `Agentic Initiative (Running)` → one `Run Target` per service → coding agent opens a PR on each.

## When to use this[​](#when-to-use-this "Direct link to When to use this")

Port has more than one way to connect a change to a coding agent. Pick based on how many services the change touches and when it should happen.

| If you want to...                                                                              | Use                                                                                                                  |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Apply the same change across every service that needs it, on demand, in one governed run.      | Agentic initiatives (this page).                                                                                     |
| React the moment a single service's scorecard degrades, without waiting for someone to notice. | [Auto-fix services when scorecards degrade](/guides/all/self-heal-scorecards-with-ai/.md)                            |
| Route a failing rule to a tracked Jira ticket instead of triggering an agent directly.         | [Route scorecard failures to Jira issues with AI](/guides/all/route-scorecard-failures-to-jira-issues/.md)           |
| Delegate an already-enriched ticket to a coding agent, one ticket at a time.                   | [Getting started with your first ATR workflow](/solutions/autonomous-ticket-resolution/getting-started-with-atr/.md) |

These compose. A service that slips through the reactive self-heal check today is exactly the kind of thing a fleet-wide initiative picks up next quarter.

## Next steps[​](#next-steps "Direct link to Next steps")

* [Getting started with agentic initiatives](/solutions/autonomous-ticket-resolution/agentic-initiatives/getting-started/.md) - build the initiative, the fan-out, and the tracking model end to end.
* [Why Port?](/solutions/autonomous-ticket-resolution/why-port/.md) - what the catalog and scorecards add versus assembling this yourself.
* [ROI dashboard](/solutions/autonomous-ticket-resolution/roi-dashboard/.md) - measuring outcomes across ATR patterns, including fleet-wide initiatives.
