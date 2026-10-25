---
title: "Custom skills"
subtitle: "Add a custom skill that Factory can load alongside its built-in skills."
authors: []
published_date: null
source_url: https://factory.mastra.ai/configure/custom-skills.md
origin: llms-txt
llms_txt: https://factory.mastra.ai/llms.txt
section: "Docs / Configuration"
fetched: 2026-10-25T18:10:21Z
---

# Custom skills

Custom skills give Factory additional instructions for specific tasks. Factory loads them alongside its built-in skills.

## Create a custom skill

`npm create factory` doesn't create the custom skills directory. Create a directory for the skill and add a `SKILL.md` file at:

```text
src/mastra/public/factory-skills/<skill-name>/SKILL.md
```

The skill directory name must match the `name` in the `SKILL.md` frontmatter. For example, create this file at `src/mastra/public/factory-skills/security-review/SKILL.md`:

```md title="src/mastra/public/factory-skills/security-review/SKILL.md"
---
name: security-review
description: Review changes for security risks.
---

# Security review

Review the change for authentication, authorization, secret handling, and injection risks.
```

Restart the Factory Server after adding the skill. Factory then loads the custom skill alongside its built-in skills.

Custom skills currently aren't managed or listed in the Factory UI.
