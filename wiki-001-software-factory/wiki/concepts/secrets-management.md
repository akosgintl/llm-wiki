---
type: concept
title: Secrets management
description: "How a factory gives agents credentials for external services by name, never by value: team-level secrets created in the platform, attached per agent or factory, and injected as environment variables."
aliases: []
sources:
  - "[[wiki/docs/llms-docs-warp-dev/factories-secrets]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-secrets-aws-ecr]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-webhooks-vercel]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-self-hosting-private-container-registry]]"
  - "[[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]"
  - "[[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]"
related:
  - "[[wiki/concepts/factory-as-code]]"
  - "[[wiki/concepts/agent-runner]]"
  - "[[wiki/concepts/self-hosting]]"
  - "[[wiki/concepts/webhook]]"
  - "[[wiki/concepts/mcp]]"
  - "[[wiki/concepts/control-plane]]"
created: 2026-10-25T16:00:00Z
timestamp: 2026-10-25T16:00:00Z
source_count: 11
---

# Secrets management

> Credentials live in the platform; definition files and prompts carry only secret names.

## Definition

Across the sources, a secret is a named credential stored at team level in the Warp Factories web app and granted to agents explicitly. Values reach a run as environment variables named after the secret; git-tracked definition files list names only. [[wiki/docs/llms-docs-warp-dev/factories-secrets]], [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]]

Not every credential is a raw value. The security page names four kinds: inference, execution secrets (per-agent allowlist), harness auth, and repository identity. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]] The ECR credential is a pointer to an assumable IAM role, not key material. [[wiki/docs/llms-docs-warp-dev/factories-secrets-aws-ecr]]

## Key claims

- Creating a team secret grants nothing; it must be attached to an agent or included in factory configuration. [[wiki/docs/llms-docs-warp-dev/factories-secrets]]
- Three list levels exist: factory-wide `secrets`, `agentDefaults.secrets`, per-agent `secrets`. Per-agent and per-automation lists replace inherited lists rather than merge; an empty list does not remove factory-wide secrets. [[wiki/docs/llms-docs-warp-dev/factories-secrets]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Non-user agents get no execution secrets by default. Redaction is a backstop, not a substitute for narrow permissions. [[wiki/docs/llms-docs-warp-dev/factories-infrastructure-and-security]]
- Definition files reference secrets by name (`{{SECRET_NAME}}`, `source: managedSecret`), including for harness auth such as `ANTHROPIC_API_KEY`. [[wiki/docs/llms-docs-warp-dev/factories-factory-as-code]], [[wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE]]
- Each injected entry is capped at 128 KiB; larger payloads belong in an object store or external secret manager. [[wiki/docs/llms-docs-warp-dev/factories-secrets]]
- Rotation keeps the name, so references survive; webhooks pick up a new value only when reapplied. Deletion is permanent and hits every referencing agent, webhook or runner. [[wiki/docs/llms-docs-warp-dev/factories-secrets]]
- ECR pulls: Warp stores a role ARN and requests a short-lived token per run; the credential authenticates image pulls only and is never injected into the agent environment. [[wiki/docs/llms-docs-warp-dev/factories-secrets-aws-ecr]]
- Webhook secrets are shown once. URL-token webhooks make the URL itself a credential. Vercel signing secrets are saved in a second step, after the URL exists. [[wiki/docs/llms-docs-warp-dev/factories-webhooks]], [[wiki/docs/llms-docs-warp-dev/factories-webhooks-vercel]]
- Forges without first-class support: store a token as an Agent Secret and clone from default-runner setup commands. [[wiki/docs/llms-docs-warp-dev/factories-code-forges-other-code-forges]]
- MCP clients act with the full permissions of their account or agent; API keys belong in secret storage, never a repository. [[wiki/docs/llms-docs-warp-dev/factories-factory-mcp]]
- Self-hosted Kubernetes: secrets arrive via `valueFrom.secretKeyRef` in `pod_template` or `--env`; external managers via CSI driver or operator. Registry pull secrets go in separate fields for the worker and for task Jobs. [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-managed-kubernetes]], [[wiki/docs/llms-docs-warp-dev/factories-self-hosting-private-container-registry]]

## Relationships

- **Factory as code**: names in git, values in the platform. [[wiki/concepts/factory-as-code]]
- **Agent runner**: runners carry image-pull credentials. [[wiki/concepts/agent-runner]]
- **Self-hosting**: backend-native secret stores replace Warp-stored ones. [[wiki/concepts/self-hosting]]
- **Webhook / MCP**: both depend on secrets for auth. [[wiki/concepts/webhook]], [[wiki/concepts/mcp]]
- **Control plane**: separates secret storage from execution. [[wiki/concepts/control-plane]]

> Synthesis: Every origin here is Warp's own voice (the docs set and two Warp-authored repos), so agreement is not independent corroboration; the examples repo shows the docs' name-only pattern in practice.
