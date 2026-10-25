---
title: "Configuring AWS ECR credentials"
subtitle: "Create an IAM role-backed secret and attach it to a Warp-hosted Linux runner to pull private container images from Amazon ECR."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/secrets/aws-ecr/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Configuring AWS ECR credentials

Create an IAM role-backed secret and attach it to a Warp-hosted Linux runner to pull private container images from Amazon ECR.

An “AWS ECR credential” lets a Warp-hosted [Linux runner](https://docs.warp.dev/factories/runners/#operating-systems) pull private Amazon ECR images. Warp stores the role ARN and requests a short-lived token per run. Create the credential in the web app, not the legacy CLI.

## Prerequisites

-   AWS access to create an IAM role in the account that owns the registry.
-   Permission to create team secrets and edit the factory’s runner configuration.
-   An existing Warp-hosted Linux runner. See [Runners for Warp Factories](https://docs.warp.dev/factories/runners/).

## Creating the ECR credential

1.  In the [Warp Factories web app](https://platform.warp.dev), click **Secrets**, then click **New** > **Create secret**.
2.  At the top of the form, click **Untitled** and enter a secret name such as `ECR_PULL_CREDENTIAL`.
3.  In the “Type” dropdown, choose **AWS ECR credential**.
4.  In the registry’s AWS account, create an IAM role with the trust and permissions policies shown in the form. If you restrict repository read actions to a repository ARN, keep `ecr:GetAuthorizationToken` on `Resource: "*"`.
5.  Back in the secret form, enter the “IAM role ARN” and “AWS region”, then click **Save**.

Warp derives the registry host from the role’s account ID and region. Creation checks role assumption and token retrieval, not repository-specific pull permissions.

## Attaching the credential to a runner

For a Warp-managed factory:

1.  In the [Warp Factories web app](https://platform.warp.dev), click your factory in the sidebar to expand it, then click **Settings**.
2.  In the “Runners” section, click the pencil button labeled **Edit runner** next to the Linux runner.
3.  In the runner editor’s “Private image credential” dropdown, choose the ECR secret you created. Its registry host must match the image’s registry.
4.  Click **Save**.

For an externally managed runner, set `platform.linux.registryCredentialSecretName` to the secret name in its YAML file and apply the change through a pull request. See [runner file syntax](https://docs.warp.dev/factories/factory-as-code/#runnersnameyaml).

Start a new run using the runner to confirm it can pull the private image. The credential authenticates image pulls and isn’t injected into the agent environment. Self-hosted workers use [backend-specific registry authentication](https://docs.warp.dev/factories/self-hosting/private-container-registry/) instead.

## Changing permissions or retiring the credential

To change ECR permissions, update the IAM role in AWS. To retire the credential, remove its runner references, then [delete the team secret](https://docs.warp.dev/factories/secrets/#deleting-a-team-secret).

## Troubleshooting

### ECR role assumption fails

Check that the role exists, the ARN is correct, and its trust policy matches the form, including your team’s `sts:ExternalId`. AWS returns `AccessDenied` for missing roles and trust-policy denials. For other errors, check that AWS STS is available in the registry’s region.

### ECR token retrieval fails

Confirm that the role allows `ecr:GetAuthorizationToken` on `Resource: "*"`. For access denials, check permissions boundaries and AWS Organizations service control policies. For other failures, confirm that the AWS region matches the registry.

### ECR image pulls fail

Confirm that the role grants `ecr:BatchCheckLayerAvailability`, `ecr:BatchGetImage`, and `ecr:GetDownloadUrlForLayer` for the repository, and that the credential’s registry host matches the image’s registry.

## Related pages

-   [Managing factory secrets](https://docs.warp.dev/factories/secrets/) - Create credentials and control agent access
-   [Runners for Warp Factories](https://docs.warp.dev/factories/runners/)
-   [Factory definition syntax](https://docs.warp.dev/factories/factory-as-code/#runnersnameyaml) - Configure runner files
-   [Private container registry](https://docs.warp.dev/factories/self-hosting/private-container-registry/) - Configure registry access for self-hosted workers
