---
title: "Deployment"
subtitle: "Run your coding agents beyond localhost. Deploy Mastra Factory to Mastra platform or self-host with your own authentication, storage, and sandboxes."
authors: []
published_date: null
source_url: https://factory.mastra.ai/deployment.md
origin: llms-txt
llms_txt: https://factory.mastra.ai/llms.txt
section: "Docs"
fetched: 2026-10-25T18:10:21Z
---

# Deployment

Deploy the Factory Server to [Mastra platform](#deploy) or [self-host](#self-host) it in your own environment. Both options use the Factory Server project created in [Get started](https://factory.mastra.ai/).

## Before you begin

- Complete the setup and [investigation steps](https://factory.mastra.ai/) in Get started.
- For deployment to Mastra platform, have access to the intended [project](https://projects.mastra.ai) and environment.
- Preserve the database's [credential encryption key](https://factory.mastra.ai/reference/environment-variables).
- Choose the execution provider and verify its [required configuration](https://factory.mastra.ai/configure/sandboxes).

## Choose a setup

| Setup                                | Factory Server      | Supporting services                                |
| ------------------------------------ | ------------------- | -------------------------------------------------- |
| Full platform (default)              | Mastra platform     | Mastra platform auth, PostgreSQL, and sandboxes    |
| Local server with platform resources | Your computer       | Mastra platform auth, PostgreSQL, and sandboxes    |
| Fully self-hosted                    | Your infrastructure | Your auth provider, database, and sandbox provider |

Continue with [Deploy](#deploy) for the full-platform setup or [Self-host](#self-host) when the Factory Server runs in your environment.

## Deploy

Use the generated project's `deploy` script to deploy to Mastra platform. The CLI builds and uploads the application to a platform environment and reports its public URLs.

1. ### Check the server

   From the Factory Server directory, run:

   **npm**:

   ```bash
   npm run check
   npm run build
   ```

   **pnpm**:

   ```bash
   pnpm run check
   pnpm run build
   ```

   **Yarn**:

   ```bash
   yarn run check
   yarn build
   ```

   **Bun**:

   ```bash
   bun run check
   bun run build
   ```

   Review local environment values so a localhost callback origin isn't used by the deployed server.

2. ### Prepare the environment

   In Platform, choose the target project and review its environment configuration. Confirm the attached database, encryption key, provider access, integration credentials, and public origin.

   The public origin must point to the deployed Factory endpoint. Configure allowed origins only when serving the UI from a separate origin. A deployed server requires persistent database storage.

   See [Environment variables](https://factory.mastra.ai/reference/environment-variables) for variable names and the distinction between Platform integration and sandbox credentials.

3. ### Run the deployment

   Inside your Factory project directory, run the deployment command:

   **npm**:

   ```bash
   npm run deploy
   ```

   **pnpm**:

   ```bash
   pnpm run deploy
   ```

   **Yarn**:

   ```bash
   yarn deploy
   ```

   **Bun**:

   ```bash
   bun run deploy
   ```

   Review the CLI's organization, project, and environment selection. The default environment is `production`. You can pass flags to the `deploy` command to customize its behavior.

   <details>
   **Deployment flags**

   To target another named environment, pass it explicitly:

   **npm**:

   ```bash
   npm run deploy -- --env staging
   ```

   **pnpm**:

   ```bash
   pnpm run deploy --env staging
   ```

   **Yarn**:

   ```bash
   yarn deploy --env staging
   ```

   **Bun**:

   ```bash
   bun run deploy --env staging
   ```

   The CLI can create an environment if it doesn't exist. Review configuration and secret changes when prompted. Use the deployed Factory URL and credentials for the target environment.

   To configure a EU region for a new environment, pass `--region eu`:

   **npm**:

   ```bash
   npm run deploy -- --env staging --region eu
   ```

   **pnpm**:

   ```bash
   pnpm run deploy --env staging --region eu
   ```

   **Yarn**:

   ```bash
   yarn deploy --env staging --region eu
   ```

   **Bun**:

   ```bash
   bun run deploy --env staging --region eu
   ```

   It doesn't relocate an existing environment. Confirm the chosen environment and attached database region in Platform before deploying.

   For a Factory project, the CLI derives a Factory URL and a Studio URL from the environment slug. Other project types use a server URL. Use the actual URLs returned for your project instead of constructing addresses from a project name.

   </details>

4. ### Verify the deployed Factory

   Open the **Factory** URL reported by the CLI. Confirm sign-in returns to this server and repository access works. Check that existing provider credentials remain usable. Create a new issue in a subscribed source, investigate it, and verify the session's actual sandbox provider.

   Inspect the Platform deployment logs if a step fails.

## Self-host

Run Factory on a virtual machine, in a container, or on a hosting service that supports a persistent Node.js process. The build includes Factory's browser UI and API, so you can serve both from the same domain.

A self-hosted Factory Server can use Mastra platform services or your own providers. Configure [Auth](https://factory.mastra.ai/configure/auth), [Storage](https://factory.mastra.ai/configure/storage), and [Sandboxes](https://factory.mastra.ai/configure/sandboxes) independently, and connect your preferred [model providers](https://factory.mastra.ai/configure/models).

For a fully self-hosted setup, create your project with the `--no-platform` flag:

**npm**:

```bash
npm create factory@latest my-factory -- --no-platform
```

**pnpm**:

```bash
pnpm create factory my-factory --no-platform
```

**Yarn**:

```bash
yarn create factory my-factory --no-platform
```

**Bun**:

```bash
bunx create-factory my-factory --no-platform
```

The installer copies `.env.example` to `.env` without adding platform credentials, so configure your authentication, database, and sandbox providers before deployment.

### Requirements

- **Runtime:** Node.js matching the `engines.node` requirement in your Factory project's `package.json`. Keep the server running so Factory can process intake and agent work in the background.
- **Storage:** A persistent database. The generated server uses PostgreSQL with pgvector through `DATABASE_URL`. For another provider, follow [Storage configuration](https://factory.mastra.ai/configure/storage).
- **Public endpoint:** An HTTPS URL that supports streaming responses for live sessions. Set `MASTRACODE_PUBLIC_URL` to this origin and use it for authentication and integration callbacks.
- **Secrets:** Provider and integration credentials in your deployment's environment settings. Keep the [credential encryption key](https://factory.mastra.ai/reference/environment-variables) and state-signing secrets stable across deployments.
- **Sandbox environment:** Network access to your chosen cloud sandbox provider. For [local execution](https://factory.mastra.ai/configure/sandboxes), install Git and your repository's build tools on the server, and use persistent disk space for session directories.

### Deployment outline

1. Connect your Factory Server repository to your hosting service, or copy it to the machine where it will run. Configure your chosen providers in the project.

2. Add the project's [environment variables](https://factory.mastra.ai/reference/environment-variables) to the deployment environment. Set `NODE_ENV=production` and configure `PORT` for your hosting service. Update callback URLs for any auth or integration apps you manage.

3. Install dependencies and build from the Factory Server directory:

   **npm**:

   ```bash
   npm ci --include=dev
   npm run check
   npm run build
   ```

   **pnpm**:

   ```bash
   npm ci --include=dev
   # couldn't auto-convert command
   pnpm run check
   pnpm run build
   ```

   **Yarn**:

   ```bash
   npm ci --include=dev
   # couldn't auto-convert command
   yarn run check
   yarn build
   ```

   **Bun**:

   ```bash
   npm ci --include dev
   # couldn't auto-convert command
   bun run check
   bun run build
   ```

4. Use `npm run start` as the service's start command. This uses the generated project's Mastra CLI and `varlock` dependencies, so retain them in the runtime environment. Configure automatic restarts and route HTTPS traffic to the server's listening port.

5. Open the deployed Factory URL and sign in. Import an issue from your connected repository and run an investigation to confirm the agent can use its sandbox.

The build writes the server and Factory UI to `.mastra/output`. You can also package this output for a container deployment. See the [Mastra server deployment guide](https://mastra.ai/docs/deployment/mastra-server) for running the build directly with Node.js.

## Related

- [Sandboxes](https://factory.mastra.ai/configure/sandboxes)
- [Credential encryption](https://factory.mastra.ai/reference/environment-variables)
- [Troubleshooting](https://factory.mastra.ai/troubleshooting)
