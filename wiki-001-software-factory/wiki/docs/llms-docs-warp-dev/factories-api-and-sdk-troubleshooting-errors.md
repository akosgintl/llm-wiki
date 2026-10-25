---
type: source
title: API error codes
description: Warp docs reference for the Warp Platform API's RFC 7807 error format and its 18 error codes, split into user errors (task FAILED) and platform errors (task ERROR).
origin: llms-txt
original_path: https://docs.warp.dev/factories/api-and-sdk/troubleshooting/errors/
source_url: https://docs.warp.dev/factories/api-and-sdk/troubleshooting/errors/
authors: []
published_date: null
raw_file: raw/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors.md
created: 2026-10-25T14:59:34Z
timestamp: 2026-10-25T14:59:34Z
entities:
  - "[[wiki/entities/warp-factories]]"
concepts: []
---

# API error codes

> [[raw/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors|Raw]] · llms-txt

## Summary

This is the index page of the error reference for the Warp Platform API, the API behind Factories and cloud agent tasks. The docs state that every error comes back as an RFC 7807 Problem Details JSON body (`application/problem+json`) carrying a machine-readable code, HTTP status, message and resolution details. [[raw/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors#Response format|cite]]

The page's main idea is a two-way split by blame. User errors mean the caller must fix something, and the docs say a cloud agent task hitting one moves to **FAILED**. Platform errors are Warp-side, and the task moves to **ERROR** after retryable ones are retried automatically. [[raw/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors#Error categories|cite]]

Each code links to its own page with resolution steps. This page only lists them.

## Key claims

- The docs state the response has `type`, `title`, `status`, `detail` (optional), `instance`, `error` (legacy `"title (detail)"` field), `retryable` and `trace_id`. [[raw/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors#Field reference|cite]]
- The docs state that `retryable: true` means the platform may retry the operation automatically. [[raw/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors#Field reference|cite]]
- Thirteen user errors are listed: `insufficient_credits`, `feature_not_available`, `external_authentication_required`, `not_authorized`, `invalid_request`, `resource_not_found`, `budget_exceeded`, `integration_disabled`, `integration_not_configured`, `operation_not_supported`, `environment_setup_failed`, `content_policy_violation`, and `conflict` (retryable). [[raw/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors#User errors|cite]]
- Five platform errors are listed: `authentication_required`, `resource_unavailable` (retryable), `internal_error` (retryable), `infrastructure_timeout` and `agent_process_failed`. [[raw/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors#Platform errors|cite]]
- Some errors add metadata such as `auth_url`, `provider` or `inaccessible_repos`, documented per error page. [[raw/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors#Field reference|cite]]
- The docs say to quote `trace_id` (an OpenTelemetry trace ID) when contacting support, mainly for `internal_error` and `resource_unavailable`. [[raw/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors#Using the `trace_id`|cite]]

## Notable quotes

> "When a cloud agent task encounters a platform error, the task transitions to the **ERROR** state. Retryable errors are automatically retried before the task is marked as failed."
> — [[raw/docs/llms-docs-warp-dev/factories-api-and-sdk-troubleshooting-errors#Platform errors|Platform errors]]

## Connections

- **Entities**: [[wiki/entities/warp-factories]]
- **Concepts**: none

> Synthesis: Vendor reference for failure handling in Warp's hosted agent runs; the FAILED vs ERROR split and the `retryable` flag matter for anyone building automation or retry logic on top of Factories.
