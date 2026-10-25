---
type: concept
title: Secrets management
description: "How a factory gives agents credentials for external services by name, never by value: team-level secrets created in the platform, attached per agent or factory, and injected as environment variables; self-hosted runners and a second vendor use backend-native secret stores."
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-secrets]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-secrets-aws-ecr]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks-vercel]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-quickstart]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-docker]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-external-orchestrators]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-private-container-registry]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]"
  - "[[wiki/docs/llms-factory-mastra-ai/deployment]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
related:
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/agent-runner]]"
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/concepts/webhook]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/control-plane]]"
  - "[[wiki/concepts/agent-harness]]"
  - "[[wiki/concepts/agent-skill]]"
  - "[[wiki/concepts/git-worktree]]"
created: 2026-10-25T16:00:00Z
timestamp: 2026-10-25T18:32:30Z
source_count: 22
---

# Secrets management

> Credentials live in the platform; definition files and prompts carry only secret names.

## Definition

Across the Warp sources, a secret is a named credential stored at team level in the Warp Factories web app and granted to agents explicitly. Values reach a run as environment variables named after the secret; git-tracked definition files list names only. [[wiki/docs/llms-docs-warp-dev/factories-secrets]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]

Not every credential is a raw value. The security page names four kinds: inference, execution secrets (per-agent allowlist), harness auth, and repository identity. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]] The ECR credential is a pointer to an assumable IAM role, not key material. [[wiki/docs/llms-docs-warp-dev/factories-secrets-aws-ecr]]

Self-hosting shifts the definition: the operator controls runtime secrets, and worker credentials are an API key kept in an operator-side secret manager. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting]] The Mastra deployment docs frame it as deploy-time configuration (database credential encryption key, provider and integration credentials) rather than named team secrets. [[wiki/docs/llms-factory-mastra-ai/deployment]]

## Key claims

- Creating a team secret grants nothing; it must be attached to an agent or included in factory configuration. The agent Settings tab and the custom-agent creation flow both expose a secrets field. [[wiki/docs/llms-docs-warp-dev/factories-secrets]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]], [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-creating-custom-agents]]
- Three list levels exist: factory-wide `secrets`, `agentDefaults.secrets`, per-agent `secrets`. Per-agent and per-automation lists replace inherited lists rather than merge; an empty list does not remove factory-wide secrets. [[wiki/docs/llms-docs-warp-dev/factories-secrets]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Non-user agents get no execution secrets by default. Redaction is a backstop, not a substitute for narrow permissions. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]
- Definition files reference secrets by name (`{{SECRET_NAME}}`, `source: managedSecret`), including for harness auth such as `ANTHROPIC_API_KEY`. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Harness auth: Claude Code takes an Anthropic API key, Bedrock API key or Bedrock access key; Codex takes an OpenAI API key. The Auth field uses a team-owned secret or **New auth secret**. [[wiki/docs/llms-docs-warp-dev/factories-factory-agents-configuration]]
- Skills carry instructions only, not access: credentials and MCP connections are configured separately in the agent's secrets and MCP settings. [[wiki/docs/llms-docs-warp-dev/factories-factory-skills]]
- The dashboard's Secrets page is team-wide, and the Webhooks tab handles secret rotation. PR authorship is controlled by `credentialStrategy` in factory Settings. [[wiki/docs/llms-docs-warp-dev/factories-factory-dashboard]]
- Each injected entry is capped at 128 KiB; larger payloads belong in an object store or external secret manager. [[wiki/docs/llms-docs-warp-dev/factories-secrets]]
- Rotation keeps the name, so references survive; webhooks pick up a new value only when reapplied. Deletion is permanent and hits every referencing agent, webhook or runner. [[wiki/docs/llms-docs-warp-dev/factories-secrets]]
- ECR pulls: Warp stores a role ARN and requests a short-lived token per run; the credential authenticates image pulls only and is never injected into the agent environment. [[wiki/docs/llms-docs-warp-dev/factories-secrets-aws-ecr]]
- Webhook secrets are shown once. URL-token webhooks make the URL itself a credential. Vercel signing secrets are saved in a second step, after the URL exists. [[wiki/docs/llms-docs-warp-dev/factories-webhooks]], [[wiki/docs/llms-docs-warp-dev/factories-webhooks-vercel]]
- Forges without first-class support: store a token as an Agent Secret and clone from default-runner setup commands. [[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]
- MCP clients act with the full permissions of their account or agent; API keys belong in secret storage, never a repository. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]
- Self-hosted worker key: passed as `WARP_API_KEY` or `--api-key` and kept in a secret manager; workers need only outbound network access. An agent API key tied to the Default Service Account creates runs. One agent key may serve both worker and `run-cloud`; across separate processes use a worker key for the worker and an agent key for the run creator. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-quickstart]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-external-orchestrators]]
- External dispatch scripts must keep the task payload out of logs, since it holds task credentials. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-external-orchestrators]]
- Docker backend: `-e` on the worker container passes env vars (such as `WARP_API_KEY`) to the worker; the worker's `-e`/`--env` flags pass them into spawned task containers. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-docker]]
- Direct backend: `setup_command` can write `KEY=VALUE` lines to `OZ_ENVIRONMENT_FILE` to inject env vars; the minimal-env default is the docs' main safeguard. Git credentials must come from an SSH key in the service account home, a system credential helper, or a helper in the base clone's config, because `GIT_CONFIG_GLOBAL` points to a task-local file. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-direct]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]
- Worktrees isolate files and branches, not the host: direct tasks share filesystem, network and processes, so the docs advise dedicated hosts and credentials matched to repo trust level. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]
- Kubernetes: secrets arrive via `valueFrom.secretKeyRef` in `pod_template` or `--env`; external managers via CSI driver or operator. Registry pull secrets go in separate fields for the worker and for task Jobs. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-private-container-registry]]
- Mastra self-host: a persistent database is required and its credential encryption key must be preserved; stable encryption key and state-signing secrets are listed as requirements, and `--no-platform` projects ship `.env.example` with no platform credentials. [[wiki/docs/llms-factory-mastra-ai/deployment]]

## Relationships

- **Factory as code**: names in git, values in the platform. [[wiki/concepts/factory-as-code]]
- **Agent runner**: runners carry image-pull credentials and worker keys. [[wiki/concepts/agent-runner]]
- **Self-hosting**: backend-native secret stores replace Warp-stored ones. [[wiki/concepts/self-hosting]]
- **Webhook / MCP**: both depend on secrets for auth. [[wiki/concepts/webhook]], [[wiki/concepts/mcp]]
- **Agent harness / skill**: harness auth uses secrets; skills deliberately do not. [[wiki/concepts/agent-harness]], [[wiki/concepts/agent-skill]]
- **Git worktree**: isolation limit shapes credential scoping. [[wiki/concepts/git-worktree]]
- **Control plane**: separates secret storage from execution. [[wiki/concepts/control-plane]]

## Tensions

- Named, scoped, per-agent secrets (Warp hosted) versus operator-managed env vars and secret stores (Warp self-hosted, Mastra). The hosted model gives allowlist control; the self-hosted Direct backend shares one host and its credentials across tasks, so isolation falls to the operator. [[wiki/docs/llms-docs-warp-dev/factories-secrets]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-direct-monorepo-worktrees]]

> Synthesis: Nearly all sources are Warp's own voice (one docs set plus a Warp-authored examples repo), so agreement among them is not independent corroboration. The Mastra deployment docs are a separate vendor but cover only deploy-time keys, not named-secret scoping.
