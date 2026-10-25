---
title: "Sandboxes"
subtitle: "Run Factory coding agents in Mastra platform sandboxes, configure local execution, or choose another Mastra sandbox provider."
authors: []
published_date: null
source_url: https://factory.mastra.ai/configure/sandboxes.md
origin: llms-txt
llms_txt: https://factory.mastra.ai/llms.txt
section: "Docs / Configuration"
fetched: 2026-10-25T18:10:21Z
---

# Sandboxes

A sandbox gives each coding-agent session an environment for its repository checkout, dependencies, and commands. You can also run commands locally or choose another [Mastra sandbox provider](https://mastra.ai/docs/sandbox/overview).

## Prepare the repository

Every session starts by checking out the linked repository into its sandbox. If the checkout needs dependencies or generated files before an agent can run tests, set a **setup** command for that repository in **Settings → Repositories** under **Sandbox**. For example:

```bash
pnpm i && pnpm build
```

Factory runs the setup command when the sandbox first starts, before the agent runs anything. A successful setup is recorded, so warm restarts of the same sandbox skip it. If setup fails, Factory also runs the **teardown** command before retrying.

The teardown command also runs when the sandbox is retired. Use it to release resources the setup command created, such as containers or background services.

Once setup has run, the agent uses that environment for the repository's own commands. When it implements a change, it runs the repository's test, lint, and build commands there, so the setup command should install whatever those need.

## Mastra platform

[PlatformSandbox](https://mastra.ai/reference/workspace/platform-sandbox) runs commands in cloud sandboxes managed through Mastra platform. The generated Factory project includes the provider package and its configuration.

Mastra platform deployments supply the sandbox credentials through the environment. To use platform sandboxes from a local server, set the corresponding values in `.env`:

```dotenv title=".env"
MASTRA_PLATFORM_ACCESS_TOKEN=your-platform-api-token
MASTRA_PROJECT_ID=your-platform-project-id
MASTRA_ENVIRONMENT_ID=your-platform-environment-id
```

Use an API token from your Mastra platform organization's **API Tokens** settings and the IDs for the project and environment where the sandboxes should run.

The callback below selects Mastra platform explicitly. `createRepoTemplate` uses the session's repository and setup command to prepare a reusable template.

```typescript title="src/mastra/sandbox.ts"
import type { MastraFactorySandboxConfig } from '@mastra/factory'
import { PlatformSandbox, createRepoTemplate } from '@mastra/platform-workspace'

export const sandbox: MastraFactorySandboxConfig = ctx =>
	new PlatformSandbox({
		id: ctx.sessionId,
		template: createRepoTemplate(ctx),
	})
```

## Set the sandbox

Each code example on this page exports a `sandbox` callback from `src/mastra/sandbox.ts`. Choose one provider example and import it in the generated entry:

```typescript title="src/mastra/index.ts"
import { sandbox } from './sandbox'
```

Replace the existing inline `sandbox` callback in `new MastraFactory(...)` with the imported `sandbox` value. Keep the rest of the Factory options, including storage, auth, and integrations.

### Local execution

`LocalSandbox` runs commands directly on the Factory Server's machine. Each session gets its own working directory. Use a cloud sandbox for virtual machine (VM) isolation.

Configure this callback to select local execution explicitly, including when your auth and database use Mastra platform:

```typescript title="src/mastra/sandbox.ts"
import { homedir } from 'node:os'
import { join } from 'node:path'
import { LocalSandbox } from '@mastra/core/workspace'
import type { MastraFactorySandboxConfig } from '@mastra/factory'

const root =
	process.env.MASTRACODE_LOCAL_SANDBOX_ROOT || join(homedir(), '.mastracode', 'web', 'sandboxes')

export const sandbox: MastraFactorySandboxConfig = ctx =>
	new LocalSandbox({
		workingDirectory: join(root, ctx.sessionId),
		env: { HOME: homedir() },
	})
```

Install Git and the tools your repository's setup command needs on that computer. Factory creates a repository checkout beneath the session directory. Add any environment variables required by your build to the explicit `env` values.

Set `MASTRACODE_LOCAL_SANDBOX_ROOT` to an absolute path to choose where session directories are stored. See the [LocalSandbox reference](https://mastra.ai/reference/workspace/local-sandbox) for additional options.

### Other sandbox providers

Factory works with other [Mastra sandbox providers](https://mastra.ai/docs/sandbox/overview). Follow your provider's setup instructions, then return a new provider instance from Factory's [sandbox callback](#set-the-sandbox).

## Check the selected provider

After changing a callback or environment variable, restart the Factory Server and inspect the sandbox startup logs to confirm that checkout and the repository's setup command complete. For a cloud provider, match the session to the sandbox in its dashboard. For local execution, check the session directory under your configured root.

The unmodified generated callback uses `LocalSandbox` when `FACTORY_SANDBOX_PROVIDER=local`. Otherwise, it selects Mastra platform when `MASTRA_PROJECT_ID`, `MASTRA_ENVIRONMENT_ID`, and either `MASTRA_PLATFORM_ACCESS_TOKEN` or `MASTRA_PLATFORM_SECRET_KEY` are set. If platform credentials aren't configured, it uses direct E2B if `E2B_API_KEY` is set, or `LocalSandbox` if it isn't.

Use the explicit callbacks above when you want to select a provider independently of that fallback logic.

Sandbox startup is lazy by default: the first code command starts the environment and can take longer while Factory prepares the repository. See [Sandbox startup troubleshooting](https://factory.mastra.ai/troubleshooting) if it fails.

## Testing limits

A sandbox runs the repository's own checks, so anything the setup command installs and the sandbox supports is available to tests. Cloud sandboxes are remote virtual machines managed by Mastra platform. They don't provide hardware or a local operating system, so checks that need a device, a specific OS, or a simulator such as iOS don't run in Factory.

Run those checks in CI on the pull request instead, where your own runners supply the device and toolchain. If you need Factory itself to run them, use a [local sandbox](#local-execution) on a machine that has the required toolchain.

## Related

- [Auth](https://factory.mastra.ai/configure/auth)
- [Storage](https://factory.mastra.ai/configure/storage)
- [Environment variables](https://factory.mastra.ai/reference/environment-variables)
- [Deployment](https://factory.mastra.ai/deployment)
