---
title: "Agent Skill"
subtitle: "Install and use the 8090 Software Factory agent skill to execute work orders consistently."
authors: []
published_date: null
source_url: https://docs.8090.ai/opinions/agent-skill
origin: llms-txt
llms_txt: https://docs.8090.ai/llms.txt
section: "Learn / Best practices"
fetched: 2026-10-25T18:13:39Z
---

# Agent Skill (/opinions/agent-skill)

Agent skills are modular bundles of instructions, scripts, and resources that an agent can load at runtime to perform specific tasks with the right procedures and context.

The 8090 Software Factory agent skill gives agents the information they need to use the platform effectively and execute Work Orders consistently. This only works once you've [connected your coding agent to 8090 Software Factory with MCP](/connections/connect-coding-agent).

**Connect MCP before installing the skill**
  The skill provides the workflow, while MCP provides access to your 8090
  Software Factory project. Complete the MCP connection first so the agent can
  read requirements, blueprints, and work orders.

## Install and use the skill [#install-and-use-the-skill]

  
    ### Install the skill [#install-the-skill]

    Run this command in your terminal:

    ```bash
    npx skills add 8090-inc/software-factory-plugin
    ```

    To have your coding agent install it instead, use **Copy Prompt** on the **Install the Software Factory skill** item in **Quick Start**, then paste the prompt into your agent.
  

  
    ### Invoke the skill [#invoke-the-skill]

    In Cursor, invoke it explicitly with `/software-factory`. For other agents, reference 8090 Software Factory, a requirement, a blueprint, or a work order in your prompt. The agent loads the related process and context when needed.
  

  
    ### Execute a work order [#execute-a-work-order]

    Give the agent a work order number or link and ask it to use the 8090 Software Factory skill to execute it. The skill guides the agent through reading related requirements and blueprints, planning, implementation, and verification.
  

## Execution state [#execution-state]

When the agent starts a work order, it creates a `scratch/wo-execution/WO-<number>/` folder. While it works, it keeps its progress in four files: `implementation-plan.md`, `checklist.md`, `context.md`, and `verification-log.md`.

The folder gives the agent one place to track what it read, what it plans to change, what it changed, what it reviewed, and how it verified the work. That makes the work order easier to resume, inspect, and review after the implementation is done.
