---
title: "Skills"
subtitle: "Package Port AI skills with reusable instructions so agents load the right steps when they handle specialized tasks in your org."
authors: []
published_date: null
source_url: https://docs.port.io/agent-management/skills/overview.md
origin: llms-txt
llms_txt: https://docs.port.io/llms.txt
section: "agent-management"
fetched: 2026-10-25T18:18:27Z
---

# Skills

Open Beta

This feature is currently in open beta and available to all organizations. Should you encounter any bugs or functionality issues, please let us know so we can rectify them as soon as possible. Your feedback is greatly appreciated! ⭐

We are actively iterating to improve the experience. Breaking changes in the data model and functionality may occur. We will communicate changes on an ongoing basis. General availability is expected by Q4 2026.

Skills are domain-specific guidance packages that help Port AI handle specialized tasks more effectively. When the AI encounters a task that matches a skill's description, it loads the skill's step-by-step instructions to ensure consistent, thorough handling.

## What are skills[​](#what-are-skills "Direct link to What are skills")

Skills provide structured workflows for common but complex tasks. Instead of relying on general AI capabilities, skills encode expert knowledge into reusable instruction sets that guide the AI through specific processes.

Each skill contains:

* **Name**: A unique identifier for the skill.
* **Description**: When the AI should use this skill.
* **Instructions**: Step-by-step guidance in markdown format.
* **References** (optional): Additional documentation or context.
* **Assets** (optional): Templates, configuration files, or other resources.

Skills follow the open [Agent Skills specification](https://agentskills.io/specification).

## Example skills you can create[​](#example-skills-you-can-create "Direct link to Example skills you can create")

* Deployment guidelines
* Engineering metrics
* Analyze incident root cause

## Deployment guidelines

A skill that helps decide on a deployment strategy, which workflows to run, how to check deployment status, and get approval. This skill can guide developers through your organization's deployment process by providing step-by-step instructions on choosing the right deployment strategy for different environments, running the appropriate CI/CD workflows, monitoring deployment progress, and obtaining necessary approvals from stakeholders before deploying to production.

## Engineering metrics

A skill that structures how you want to get engineering metrics and what to look for. This skill helps analyze key performance indicators like lead time for changes, deployment frequency, change failure rate, and AI usage and cost metrics. It can provide guidance on how to collect, aggregate, and interpret these metrics to gain insights into your team's performance and identify areas for improvement.

## Analyze incident root cause

A skill that provides a walkthrough on steps to run when analyzing an incident root cause. This skill guides you through a systematic process for investigating incidents, including gathering relevant logs and metrics, identifying the timeline of events, examining related services and dependencies, analyzing error patterns, and documenting findings to prevent similar incidents in the future.

## How skills work[​](#how-skills-work "Direct link to How skills work")

Skills are loaded via the `load_skill` tool available in the [Port MCP Server](/agent-management/port-mcp-server/overview/.md). When Port AI detects a task that matches a skill's description, it automatically loads the relevant skill before proceeding.

**Loading a skill:**

```
load_skill({ name: "troubleshoot-integration" })
```

**Loading a specific resource from a skill:**

```
load_skill({ name: "troubleshoot-integration", resource: "references/common-errors.md" })
```

## Built-in skills[​](#built-in-skills "Direct link to Built-in skills")

Port includes built-in skills for common workflows. These skills are available to all users without any configuration.

**`action-permissions-helper` (click to expand)**

Helps you configure permissions for self-service actions, with a focus on dynamic permission policies.<br /><!-- -->Use it to write or debug JQ expressions for execute and approve policies, or to understand why an existing permission policy isn't behaving as expected.

**`dashboard-page-helper` (click to expand)**

Guides the creation of dashboard pages with widgets, including a fallback approach for large pages with five or more widgets. It also checks your existing sidebar structure before placing a new page, keeping your navigation organized.

**`ei-ai-copilot-adoption` (click to expand)**

Sets up GitHub Copilot adoption metrics and the GitHub Copilot AI Adoption dashboard as part of Engineering Intelligence.<br /><!-- -->Use it to measure or visualize license utilization, acceptance rate, lines-of-code efficiency, low-engagement users, or per-team Copilot rollups.

**`ei-delivery-performance` (click to expand)**

Sets up pull request and merge request delivery performance metrics and dashboards for GitHub, GitLab, or Azure DevOps as part of Engineering Intelligence.<br /><!-- -->Use it to measure cycle time, throughput, stale pull requests, or reviewer coverage.

**`ei-foundation` (click to expand)**

Validates whether your organization has the data model required for Engineering Intelligence use cases, before you run the Delivery Performance or AI Copilot Adoption skills.<br /><!-- -->Use it whenever Engineering Intelligence widgets, scorecards, or dashboards appear empty, to check readiness and identify what's missing.

**`mapping-assistant` (click to expand)**

Helps you create, modify, or troubleshoot integration mapping configurations.<br /><!-- -->Use it to write JQ expressions for data transformation, understand test results and errors, or debug mapping issues.

**`skill-creator` (click to expand)**

Guides you through creating and registering custom AI skills in Port, from clarifying the skill's purpose to writing effective instructions and registering it as a Port entity.

**`troubleshoot-integration` (click to expand)**

Diagnoses and resolves integration sync issues, mapping errors, and data problems.<br /><!-- -->Use it when data isn't syncing or appearing in Port, entities are missing or incorrect, or you're seeing sync errors and mapping configuration problems.

**`troubleshoot-scim` (click to expand)**

Diagnoses and resolves SCIM provisioning issues, including group provisioning errors, missing users, compatibility issues, and login problems. Works with Azure Entra ID, Okta, JumpCloud, Google Workspace, or any SCIM 2.0-compatible identity provider.

**`workflows` (click to expand)**

Creates or updates Port workflows, including triggers, action nodes, conditions, and data flow.<br /><!-- -->Use it to add, update, or remove individual nodes, connections, or user inputs in a workflow.

## Creating custom skills[​](#creating-custom-skills "Direct link to Creating custom skills")

[YouTube video player](https://www.youtube.com/embed/h42j9WnzTBI)

You can create custom skills tailored to your organization's specific workflows. Custom skills are stored as entities in Port and can override built-in skills with the same name.

### Step 1: Create the skill blueprint[​](#step-1-create-the-skill-blueprint "Direct link to Step 1: Create the skill blueprint")

First, create the `skill` blueprint in your Port organization. Go to your [data model](https://app.port.io/settings/data-model) and create a new blueprint with the following configuration:

**Skill blueprint (click to expand)**

Create in Port

```
{

  "identifier": "skill",

  "title": "Skill",

  "icon": "Learn",

  "schema": {

    "properties": {

      "description": {

        "title": "Description",

        "type": "string",

        "description": "What the skill does and when the model should use it"

      },

      "instructions": {

        "title": "Instructions",

        "type": "string",

        "format": "markdown",

        "description": "Step-by-step instructions for the AI to follow"

      },

      "references": {

        "title": "References",

        "type": "array",

        "description": "Reference documents for the skill",

        "items": {

          "type": "object",

          "properties": {

            "path": {

              "type": "string",

              "description": "Resource path (e.g., references/common-errors.md)"

            },

            "content": {

              "type": "string",

              "description": "The file content"

            },

            "description": {

              "type": "string",

              "description": "Optional description of the resource"

            }

          },

          "required": ["path", "content"],

          "additionalProperties": false

        }

      },

      "assets": {

        "title": "Assets",

        "type": "array",

        "description": "Asset files (templates, configs) for the skill",

        "items": {

          "type": "object",

          "properties": {

            "path": {

              "type": "string",

              "description": "Asset path (e.g., assets/mapping-template.yaml)"

            },

            "content": {

              "type": "string",

              "description": "The file content"

            },

            "description": {

              "type": "string",

              "description": "Optional description of the asset"

            }

          },

          "required": ["path", "content"],

          "additionalProperties": false

        }

      },

      "location": {

        "type": "string",

        "title": "Location",

        "description": "The target directory where the skill will be created on the machine.",

        "default": "global",

        "enum": [

          "global",

          "project"

        ],

        "enumColors": {

          "global": "lightGray",

          "project": "lightGray"

        }

      }

    },

    "required": ["description", "instructions", "location"]

  },

  "mirrorProperties": {},

  "calculationProperties": {},

  "aggregationProperties": {},

  "relations": {}

}
```

### Step 2: Create skill entities[​](#step-2-create-skill-entities "Direct link to Step 2: Create skill entities")

Once the blueprint exists, create entities for each custom skill. Each entity represents one skill.

* Manual creation
* Using GitOps

**Required properties:**

| Property       | Description                                                                                                                 |
| -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `identifier`   | Unique skill name using lowercase letters and hyphens (e.g., `deploy-service`).                                             |
| `description`  | A clear description of what the skill does and when Port AI should use it. This helps the AI decide when to load the skill. |
| `instructions` | Step-by-step instructions in markdown format.                                                                               |

**Optional properties:**

| Property     | Description                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- |
| `references` | Array of reference documents. Each item needs a `path` (e.g., `references/runbook.md`) and `content` (the document text). |
| `assets`     | Array of asset files like templates or configs. Same structure as references: `path` and `content`.                       |

### Example: Custom deployment skill

Here's an example of a custom skill for deploying services in your organization:

```
{

  "identifier": "deploy-to-production",

  "title": "Deploy to Production",

  "properties": {

    "description": "Guide for deploying services to production. Use when users ask to deploy, release, or promote a service to production.",

    "instructions": "# Deploy to Production\n\nFollow these steps to deploy a service to production:\n\n## Step 1: Verify prerequisites\n\n- Check that all tests pass.\n- Verify the service has a production-readiness scorecard score above 80%.\n- Confirm the service owner has approved the deployment.\n\n## Step 2: Run the deployment\n\nExecute the deployment action for the target service and environment.\n\n**Example input:**\n- Service: `payment-service`\n- Environment: `production`\n\n**Expected output:**\n- Deployment initiated successfully.\n- Action run ID returned for tracking.\n\n## Step 3: Verify deployment\n\n- Check the action run status.\n- Verify the service is healthy in production.\n- Monitor for any alerts in the first 15 minutes.\n\n## Common edge cases\n\n- If tests are failing, do not proceed with deployment.\n- If scorecard score is below threshold, recommend remediation steps first.\n- If deployment fails, check logs and suggest rollback if needed.",

    "references": [

      {

        "path": "references/deployment-runbook.md",

        "content": "# Deployment Runbook\n\n## Pre-deployment checklist\n\n- [ ] All CI checks pass\n- [ ] Code review approved\n- [ ] QA sign-off received\n\n## Rollback procedure\n\nIf deployment fails:\n1. Revert to previous version\n2. Notify on-call team\n3. Create incident ticket"

      },

      {

        "path": "references/common-errors.md",

        "content": "# Common Deployment Errors\n\n## ImagePullBackOff\nCause: Container registry authentication failed.\nFix: Verify registry credentials.\n\n## CrashLoopBackOff\nCause: Application fails to start.\nFix: Check application logs and configuration."

      }

    ],

    "assets": [

      {

        "path": "assets/deployment-config.yaml",

        "content": "apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: {{ service_name }}\nspec:\n  replicas: 3\n  strategy:\n    type: RollingUpdate"

      }

    ]

  }

}
```

You can ingest skills from GitHub repositories using the GitHub integration. This enables a GitOps workflow where GitHub is the source of truth and Port stays in sync automatically.

**Prerequisites:**

[GitHub Ocean integration](https://docs.port.io/context-lake/ingestion/ingest-data-into-port/native-integrations/available-integrations/git/github-ocean) is installed in your account.

Choose one mapping kind. Do not combine them:

* Use the **`skill`** kind to ingest `SKILL.md` instructions. Set `includeSkillFolder: true` to also bundle the text files in each skill folder into `properties.references`.
* Use the **`file`** kind when you also need binary files under `assets/` on the skill entity as `properties.assets`.

Do not model extra files as related entities, and do not reconstruct `references` with mirror or calculation properties. `port skills add` and `port skills sync` only read stored `properties.references` and `properties.assets` on the skill entity.

**Recommended file structure:**

Store each skill in its own folder under `skills/`. Put instructions in `SKILL.md`. Put any other files the skill needs under `references/` or `assets/`:

```
skills/

├── deploy-to-production/

│   ├── SKILL.md

│   ├── references/

│   │   └── deployment-runbook.md

│   └── assets/

│       └── deployment-config.yaml

└── troubleshoot-integration/

    └── SKILL.md
```

**Configure the GitHub integration:**

1. Go to the [connectors](https://app.port.io/settings/data-sources) page in Port.

2. Find your GitHub integration and click **Manage**.

3. Go to the **Mapping** tab.

4. Add the mapping for the kind you chose:

   * Skill kind
   * File kind

   The `skill` kind discovers `SKILL.md` files, parses frontmatter, and maps instructions. Extra files in the skill folder are not ingested.

   **GitHub Ocean skill kind mapping (click to expand)**

   ```
   deleteDependentEntities: false

   createMissingRelatedEntities: true

   enableMergeEntity: true

   resources:

     - kind: skill

       selector:

         query: 'true'

         paths:

           - path: 'skills/**/SKILL.md'

             organization: my-org  # Optional if githubOrganization is set (required if not set)

             repos:

               - name: my-skills-repo

                 branch: main

       port:

         entity:

           mappings:

             identifier: .__repository.full_name + "/" + .skill.skillMdPath

             title: .skill.name // .skill.skillMdPath

             blueprint: '"skill"'

             properties:

               instructions: .skill.instructions

               description: .skill.description

               location: '"global"'
   ```

   The `file` kind maps `SKILL.md` plus files under `references/` and `assets/` onto one skill entity. Use the same identifier for every file in a skill folder, and set `enableMergeEntity: true` so extra files merge onto the entity instead of replacing the instructions.

   **GitHub Ocean file kind mapping (click to expand)**

   ```
   deleteDependentEntities: false

   createMissingRelatedEntities: true

   enableMergeEntity: true

   resources:

     - kind: file

       selector:

         query: 'true'

         files:

           - path: skills/**/SKILL.md

             organization: my-org  # Optional if githubOrganization is set (required if not set)

             repos:

               - name: my-skills-repo

                 branch: main

       port:

         entity:

           mappings:

             identifier: .repository.name + "/" + (.path | split("/")[1])

             title: .path | split("/")[1]

             blueprint: '"skill"'

             properties:

               instructions: .content

               description: .content | capture("description:\\s*(?<d>.+)").d

               location: '"global"'

             relations: {}

     - kind: file

       selector:

         query: 'true'

         files:

           - path: skills/**/references/**

             skipParsing: true

             organization: my-org  # Optional if githubOrganization is set (required if not set)

             repos:

               - name: my-skills-repo

                 branch: main

       port:

         entity:

           mappings:

             identifier: .repository.name + "/" + (.path | split("/")[1])

             blueprint: '"skill"'

             properties:

               references:

                 - path: .path | split("/") | .[2:] | join("/")

                   content: .content

     - kind: file

       selector:

         query: 'true'

         files:

           - path: skills/**/assets/**

             skipParsing: true

             organization: my-org  # Optional if githubOrganization is set (required if not set)

             repos:

               - name: my-skills-repo

                 branch: main

       port:

         entity:

           mappings:

             identifier: .repository.name + "/" + (.path | split("/")[1])

             blueprint: '"skill"'

             properties:

               assets:

                 - path: .path | split("/") | .[2:] | join("/")

                   content: .content
   ```

5. Click **Save & Resync** to update the integration configuration.

After configuration, skills from your GitHub repositories will automatically sync to Port. Changes in GitHub will appear in your Port catalog after the integration syncs.

#### Common practices

* Namespace the `identifier` so skills with the same folder name in different repos don't collide. The skill kind example uses `.__repository.full_name`. The file kind example uses `.repository.name + "/" + ...`.
* Keep `deleteDependentEntities: false` on this connector. Setting it to `true` means a temporary sync issue, like a rate limit, a revoked permission, or a renamed repo, deletes skill entities on the next resync instead of leaving them stale.
* Extract `description` from the SKILL.md frontmatter instead of mapping the raw file content, so the catalog shows a short summary rather than the entire file.
* With the file kind, each extra-file event replaces the whole `references` or `assets` array. If a skill has more than one file in the same directory, use the [upload skills from a folder](/agent-management/skills/overview/.md#upload-skills-from-a-folder) script so the full array is written in one request.

Using GitHub (Sunset) or also syncing prompts

If your account still uses Port's older GitHub app integration, or you also want to sync prompt files alongside skills, see the [Ingest prompts and skills from GitHub using GitOps](/guides/all/ingest-prompts-skills-from-github-using-gitops/.md) guide, which covers both integration versions and the combined prompts and skills setup.

## Upload skills from a folder[​](#upload-skills-from-a-folder "Direct link to Upload skills from a folder")

You can manage skills as folders in your repository and upload them to Port using a script. This is useful for version-controlling your skills and integrating with CI/CD pipelines.

### Skill folder structure[​](#skill-folder-structure "Direct link to Skill folder structure")

Organize each skill as a folder with the following structure:

```
my-skill/

├── SKILL.md              # Skill definition (required)

├── references/           # Reference documents (optional)

│   ├── runbook.md

│   └── common-errors.md

└── assets/               # Asset files (optional)

    └── config-template.yaml
```

The `SKILL.md` file contains YAML frontmatter with the skill metadata, followed by the instructions in markdown:

```
---

name: deploy-to-production

description: Guide for deploying services to production. Use when users ask to deploy, release, or promote a service to production.

metadata:

  title: Deploy to Production

---



# Deploy to Production



Follow these steps to deploy a service to production:



## Step 1: Verify prerequisites

- Check that all tests pass.

- Verify the service has a production-readiness scorecard score above 80%.



## Step 2: Run the deployment

Execute the deployment action for the target service.



## Common edge cases

- If tests are failing, do not proceed with deployment.

- If deployment fails, check logs and suggest rollback.
```

### Upload script[​](#upload-script "Direct link to Upload script")

Use the following script to read a skill folder and upload it to Port as an entity.

**Upload script (click to expand)**

**Prerequisites:**

```
# Python: install dependencies

pip install requests pyyaml



# JavaScript: install dependencies

npm install js-yaml



# Bash: install jq and yq, make script executable

# macOS: brew install jq yq

# Ubuntu: sudo apt-get install jq && pip install yq

chmod +x ./upload-skill.sh
```

**Usage:**

```
# Set your Port credentials

export PORT_CLIENT_ID="your-client-id"

export PORT_CLIENT_SECRET="your-client-secret"



# For US region, also set:

# export PORT_BASE_URL="https://api.us.port.io"



# Test with dry-run first (no changes made)

python upload_skill.py ./my-skill --dry-run      # Python

node upload-skill.js ./my-skill --dry-run        # JavaScript

./upload-skill.sh ./my-skill --dry-run           # Bash



# Upload the skill to Port

python upload_skill.py ./my-skill                # Python

node upload-skill.js ./my-skill                  # JavaScript

./upload-skill.sh ./my-skill                     # Bash
```

* Python
* JavaScript
* Bash

```
#!/usr/bin/env python3

"""

Upload a skill folder to Port as an entity.



Usage:

    python upload_skill.py <skill-directory> [--dry-run]



Environment variables:

    PORT_CLIENT_ID     - Port client ID

    PORT_CLIENT_SECRET - Port client secret

    PORT_BASE_URL      - Port API base URL (default: https://api.port.io)

"""



import os

import sys

import json

import requests

import yaml

import re

from pathlib import Path



PORT_BASE_URL = os.environ.get('PORT_BASE_URL', 'https://api.port.io')





def get_port_token():

    client_id = os.environ.get('PORT_CLIENT_ID')

    client_secret = os.environ.get('PORT_CLIENT_SECRET')



    if not client_id or not client_secret:

        raise Exception('PORT_CLIENT_ID and PORT_CLIENT_SECRET environment variables are required')



    response = requests.post(

        f'{PORT_BASE_URL}/v1/auth/access_token',

        json={'clientId': client_id, 'clientSecret': client_secret}

    )

    response.raise_for_status()

    return response.json()['accessToken']





def parse_skill_file(skill_dir):

    skill_path = Path(skill_dir) / 'SKILL.md'



    if not skill_path.exists():

        raise Exception(f'SKILL.md not found in {skill_dir}')



    content = skill_path.read_text()



    # Parse YAML frontmatter

    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)

    if not match:

        raise Exception('Invalid SKILL.md format: missing YAML frontmatter')



    frontmatter = yaml.safe_load(match.group(1))

    instructions = match.group(2).strip()



    if not frontmatter.get('name'):

        raise Exception('SKILL.md frontmatter must have a "name" field')

    if not frontmatter.get('description'):

        raise Exception('SKILL.md frontmatter must have a "description" field')



    return {

        'name': frontmatter['name'],

        'description': frontmatter['description'],

        'metadata': frontmatter.get('metadata', {}),

        'instructions': instructions

    }





def read_resources_from_dir(skill_dir, sub_dir):

    dir_path = Path(skill_dir) / sub_dir



    if not dir_path.exists():

        return []



    resources = []

    for file_path in dir_path.rglob('*'):

        if file_path.is_file():

            relative_path = f'{sub_dir}/{file_path.relative_to(dir_path)}'

            resources.append({

                'path': relative_path,

                'content': file_path.read_text()

            })



    return resources





def upload_skill(token, entity):

    response = requests.post(

        f'{PORT_BASE_URL}/v1/blueprints/skill/entities?upsert=true&merge=true',

        headers={

            'Authorization': f'Bearer {token}',

            'Content-Type': 'application/json'

        },

        json=entity

    )

    response.raise_for_status()

    return response.json()





def main():

    args = sys.argv[1:]

    dry_run = '--dry-run' in args

    skill_dir = next((arg for arg in args if not arg.startswith('--')), None)



    if not skill_dir:

        print('Usage: python upload_skill.py <skill-directory> [--dry-run]')

        sys.exit(1)



    skill_dir = Path(skill_dir).resolve()



    if not skill_dir.exists():

        print(f'Error: Directory not found: {skill_dir}')

        sys.exit(1)



    print(f'Reading skill from: {skill_dir}')



    # Parse SKILL.md

    skill = parse_skill_file(skill_dir)

    print(f'  Name: {skill["name"]}')

    print(f'  Description: {skill["description"][:50]}...')



    # Read references and assets

    references = read_resources_from_dir(skill_dir, 'references')

    assets = read_resources_from_dir(skill_dir, 'assets')



    print(f'  References: {len(references)} file(s)')

    print(f'  Assets: {len(assets)} file(s)')



    # Build entity

    entity = {

        'identifier': skill['name'],

        'title': skill['metadata'].get('title', skill['name']),

        'properties': {

            'description': skill['description'],

            'instructions': skill['instructions'],

            'references': references if references else None,

            'assets': assets if assets else None

        }

    }



    print('\nEntity to create/update:')

    print(json.dumps(entity, indent=2))



    if dry_run:

        print('\n[DRY RUN] Would create/update entity in Port')

    else:

        print('\nAuthenticating with Port...')

        token = get_port_token()

        result = upload_skill(token, entity)

        print(f'\n✅ Entity created/updated successfully!')

        print(f'   Identifier: {result["entity"]["identifier"]}')

        print(f'   Title: {result["entity"]["title"]}')





if __name__ == '__main__':

    main()
```

```
#!/usr/bin/env node

/**

 * Upload a skill folder to Port as an entity.

 *

 * Usage:

 *   node upload-skill.js <skill-directory> [--dry-run]

 *

 * Environment variables:

 *   PORT_CLIENT_ID     - Port client ID

 *   PORT_CLIENT_SECRET - Port client secret

 *   PORT_BASE_URL      - Port API base URL (default: https://api.port.io)

 */



const fs = require('fs');

const path = require('path');

const yaml = require('js-yaml');



const PORT_BASE_URL = process.env.PORT_BASE_URL || 'https://api.port.io';



async function getPortToken() {

    const clientId = process.env.PORT_CLIENT_ID;

    const clientSecret = process.env.PORT_CLIENT_SECRET;



    if (!clientId || !clientSecret) {

        throw new Error('PORT_CLIENT_ID and PORT_CLIENT_SECRET environment variables are required');

    }



    const response = await fetch(`${PORT_BASE_URL}/v1/auth/access_token`, {

        method: 'POST',

        headers: { 'Content-Type': 'application/json' },

        body: JSON.stringify({ clientId, clientSecret })

    });



    if (!response.ok) {

        throw new Error(`Failed to get Port token: ${response.status} ${response.statusText}`);

    }



    const data = await response.json();

    return data.accessToken;

}



function parseSkillFile(skillDir) {

    const skillPath = path.join(skillDir, 'SKILL.md');



    if (!fs.existsSync(skillPath)) {

        throw new Error(`SKILL.md not found in ${skillDir}`);

    }



    const content = fs.readFileSync(skillPath, 'utf-8');



    // Parse YAML frontmatter

    const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);

    if (!frontmatterMatch) {

        throw new Error('Invalid SKILL.md format: missing YAML frontmatter');

    }



    const frontmatter = yaml.load(frontmatterMatch[1]);

    const instructions = frontmatterMatch[2].trim();



    if (!frontmatter.name) {

        throw new Error('SKILL.md frontmatter must have a "name" field');

    }

    if (!frontmatter.description) {

        throw new Error('SKILL.md frontmatter must have a "description" field');

    }



    return {

        name: frontmatter.name,

        description: frontmatter.description,

        metadata: frontmatter.metadata || {},

        instructions

    };

}



function readResourcesFromDir(skillDir, subDir) {

    const dirPath = path.join(skillDir, subDir);



    if (!fs.existsSync(dirPath)) {

        return [];

    }



    const resources = [];

    const files = fs.readdirSync(dirPath, { recursive: true });



    for (const file of files) {

        const filePath = path.join(dirPath, file);

        const stat = fs.statSync(filePath);



        if (stat.isFile()) {

            const relativePath = `${subDir}/${file}`;

            const content = fs.readFileSync(filePath, 'utf-8');



            resources.push({

                path: relativePath,

                content

            });

        }

    }



    return resources;

}



async function uploadSkill(token, entity) {

    const response = await fetch(`${PORT_BASE_URL}/v1/blueprints/skill/entities?upsert=true&merge=true`, {

        method: 'POST',

        headers: {

            'Content-Type': 'application/json',

            Authorization: `Bearer ${token}`

        },

        body: JSON.stringify(entity)

    });



    if (!response.ok) {

        const errorBody = await response.text();

        throw new Error(`Failed to create entity: ${response.status} ${response.statusText}\n${errorBody}`);

    }



    return response.json();

}



async function main() {

    const args = process.argv.slice(2);

    const dryRun = args.includes('--dry-run');

    const skillDir = args.find(arg => !arg.startsWith('--'));



    if (!skillDir) {

        console.error('Usage: node upload-skill.js <skill-directory> [--dry-run]');

        process.exit(1);

    }



    const resolvedDir = path.resolve(skillDir);



    if (!fs.existsSync(resolvedDir)) {

        console.error(`Error: Directory not found: ${resolvedDir}`);

        process.exit(1);

    }



    console.log(`Reading skill from: ${resolvedDir}`);



    // Parse SKILL.md

    const skill = parseSkillFile(resolvedDir);

    console.log(`  Name: ${skill.name}`);

    console.log(`  Description: ${skill.description.substring(0, 50)}...`);



    // Read references and assets

    const references = readResourcesFromDir(resolvedDir, 'references');

    const assets = readResourcesFromDir(resolvedDir, 'assets');



    console.log(`  References: ${references.length} file(s)`);

    console.log(`  Assets: ${assets.length} file(s)`);



    // Build entity

    const entity = {

        identifier: skill.name,

        title: skill.metadata.title || skill.name,

        properties: {

            description: skill.description,

            instructions: skill.instructions,

            references: references.length > 0 ? references : undefined,

            assets: assets.length > 0 ? assets : undefined

        }

    };



    console.log('\nEntity to create/update:');

    console.log(JSON.stringify(entity, null, 2));



    if (dryRun) {

        console.log('\n[DRY RUN] Would create/update entity in Port');

    } else {

        console.log('\nAuthenticating with Port...');

        const token = await getPortToken();



        const result = await uploadSkill(token, entity);

        console.log('\n✅ Entity created/updated successfully!');

        console.log(`   Identifier: ${result.entity.identifier}`);

        console.log(`   Title: ${result.entity.title}`);

    }

}



main().catch(err => {

    console.error('Error:', err.message);

    process.exit(1);

});
```

```
#!/bin/bash

#

# Upload a skill folder to Port as an entity.

#

# Usage:

#   ./upload-skill.sh <skill-directory> [--dry-run]

#

# Environment variables:

#   PORT_CLIENT_ID     - Port client ID

#   PORT_CLIENT_SECRET - Port client secret

#   PORT_BASE_URL      - Port API base URL (default: https://api.port.io)

#

# Dependencies: jq, yq



set -e



PORT_BASE_URL="${PORT_BASE_URL:-https://api.port.io}"



# Parse arguments

DRY_RUN=false

SKILL_DIR=""



for arg in "$@"; do

    if [[ "$arg" == "--dry-run" ]]; then

        DRY_RUN=true

    elif [[ ! "$arg" == --* ]]; then

        SKILL_DIR="$arg"

    fi

done



if [[ -z "$SKILL_DIR" ]]; then

    echo "Usage: ./upload-skill.sh <skill-directory> [--dry-run]"

    exit 1

fi



SKILL_DIR=$(cd "$SKILL_DIR" && pwd)



if [[ ! -d "$SKILL_DIR" ]]; then

    echo "Error: Directory not found: $SKILL_DIR"

    exit 1

fi



echo "Reading skill from: $SKILL_DIR"



# Check for SKILL.md

SKILL_FILE="$SKILL_DIR/SKILL.md"

if [[ ! -f "$SKILL_FILE" ]]; then

    echo "Error: SKILL.md not found in $SKILL_DIR"

    exit 1

fi



# Parse SKILL.md frontmatter using yq

FRONTMATTER=$(sed -n '/^---$/,/^---$/p' "$SKILL_FILE" | sed '1d;$d')

SKILL_NAME=$(echo "$FRONTMATTER" | yq -r '.name')

SKILL_DESCRIPTION=$(echo "$FRONTMATTER" | yq -r '.description')

SKILL_TITLE=$(echo "$FRONTMATTER" | yq -r '.metadata.title // .name')



# Get instructions (everything after the closing --- of frontmatter, trimmed)

INSTRUCTIONS=$(awk '/^---$/{n++; next} n>=2' "$SKILL_FILE" | sed '/./,$!d')



echo "  Name: $SKILL_NAME"

echo "  Description: ${SKILL_DESCRIPTION:0:50}..."



# Read references

REFERENCES="[]"

if [[ -d "$SKILL_DIR/references" ]]; then

    REFERENCES=$(find "$SKILL_DIR/references" -type f | while read -r file; do

        REL_PATH="references/$(basename "$file")"

        CONTENT=$(cat "$file" | jq -Rs .)

        echo "{\"path\": \"$REL_PATH\", \"content\": $CONTENT}"

    done | jq -s '.')

    echo "  References: $(echo "$REFERENCES" | jq 'length') file(s)"

else

    echo "  References: 0 file(s)"

fi



# Read assets

ASSETS="[]"

if [[ -d "$SKILL_DIR/assets" ]]; then

    ASSETS=$(find "$SKILL_DIR/assets" -type f | while read -r file; do

        REL_PATH="assets/$(basename "$file")"

        CONTENT=$(cat "$file" | jq -Rs .)

        echo "{\"path\": \"$REL_PATH\", \"content\": $CONTENT}"

    done | jq -s '.')

    echo "  Assets: $(echo "$ASSETS" | jq 'length') file(s)"

else

    echo "  Assets: 0 file(s)"

fi



# Build entity JSON

ENTITY=$(jq -n \

    --arg identifier "$SKILL_NAME" \

    --arg title "$SKILL_TITLE" \

    --arg description "$SKILL_DESCRIPTION" \

    --arg instructions "$INSTRUCTIONS" \

    --argjson references "$REFERENCES" \

    --argjson assets "$ASSETS" \

    '{

        identifier: $identifier,

        title: $title,

        properties: {

            description: $description,

            instructions: $instructions,

            references: (if ($references | length) > 0 then $references else null end),

            assets: (if ($assets | length) > 0 then $assets else null end)

        }

    }')



echo ""

echo "Entity to create/update:"

echo "$ENTITY" | jq .



if [[ "$DRY_RUN" == "true" ]]; then

    echo ""

    echo "[DRY RUN] Would create/update entity in Port"

    exit 0

fi



# Get Port token

if [[ -z "$PORT_CLIENT_ID" || -z "$PORT_CLIENT_SECRET" ]]; then

    echo "Error: PORT_CLIENT_ID and PORT_CLIENT_SECRET environment variables are required"

    exit 1

fi



echo ""

echo "Authenticating with Port..."

ACCESS_TOKEN=$(curl --silent --location --request POST "${PORT_BASE_URL}/v1/auth/access_token" \

    --header 'Content-Type: application/json' \

    --data-raw "{

        \"clientId\": \"${PORT_CLIENT_ID}\",

        \"clientSecret\": \"${PORT_CLIENT_SECRET}\"

    }" | jq -r '.accessToken')



# Upload entity

RESULT=$(curl --silent --location --request POST "${PORT_BASE_URL}/v1/blueprints/skill/entities?upsert=true&merge=true" \

    --header "Authorization: Bearer ${ACCESS_TOKEN}" \

    --header 'Content-Type: application/json' \

    --data-raw "$ENTITY")



echo ""

echo "✅ Entity created/updated successfully!"

echo "   Identifier: $(echo "$RESULT" | jq -r '.entity.identifier')"

echo "   Title: $(echo "$RESULT" | jq -r '.entity.title')"
```

Find your Port credentials

Your Port credentials are available in the [Port UI](https://app.port.io) under **Settings > Credentials**.

## Priority and overriding[​](#priority-and-overriding "Direct link to Priority and overriding")

Custom skills take priority over built-in skills. If you create a custom skill with the same identifier as a built-in skill (e.g., `troubleshoot-integration`), your custom skill will be used instead.

This allows you to:

* Customize built-in workflows for your organization's specific needs.
* Add organization-specific context to existing skills.
* Replace generic instructions with your team's best practices.

## Best practices[​](#best-practices "Direct link to Best practices")

When creating custom skills, follow these guidelines for best results:

### Keep instructions concise

Skills are loaded into the AI's context, so keep instructions under 5000 tokens (approximately 500 lines). Move detailed reference content to the `references` array instead of putting everything in the main instructions.

### Write clear trigger descriptions

The `description` field determines when Port AI loads the skill. Write descriptions that clearly indicate:

* What task the skill handles.
* Keywords or phrases users might use.
* When NOT to use the skill (if relevant).

**Good example:**

> "Diagnose and resolve integration sync issues, mapping errors, and data problems. Use when users report missing data, sync failures, or integration errors."

**Poor example:**

> "Helps with integrations."

### Structure instructions effectively

Organize instructions with clear structure. Include:

* Step-by-step instructions for completing the task.
* Examples of inputs and outputs.
* Common edge cases and how to handle them.

### Use resources for detailed content

Put detailed documentation, error catalogs, or templates in the `references` and `assets` arrays. The AI can load these on demand when needed, keeping the main instructions focused.

## Related pages[​](#related-pages "Direct link to Related pages")

* [Ingest skills from Git](/agent-management/skills/ingest-skills-from-git/.md): sync skills from your repositories.
* [Skills registry](/solutions/agentops/getting-started/.md): build an org-wide skills registry with AgentOps.
* [Enrich Port AI with skills](/agent-management/skills/enrich-port-ai-with-skills/.md): load skills at runtime in Port AI.
* [Skills usage analytics](/agent-management/skills/skills-usage-analytics/.md): measure skill adoption from Cursor and Claude.
