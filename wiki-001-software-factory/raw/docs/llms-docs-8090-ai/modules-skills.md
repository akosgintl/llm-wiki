---
title: "Skills"
subtitle: "Save reusable instructions your project agent loads on demand, so your team's guidance becomes durable shared knowledge."
authors: []
published_date: null
source_url: https://docs.8090.ai/modules/skills
origin: llms-txt
llms_txt: https://docs.8090.ai/llms.txt
section: "Docs / Agents"
fetched: 2026-10-25T18:13:39Z
---

# Skills (/modules/skills)

A skill is a saved set of instructions that the project agent loads when it needs them, so you don't have to repeat the same guidance in every chat. Each skill has a title, a description, and a body of instructions, and it belongs to a category. The agent reads a skill when you pick it, or when the task matches the skill's description.

Skills live in the project, so the whole team shares them. When you find yourself giving the agent the same guidance again, save it once as a skill.

## Categories [#categories]

Every skill belongs to a category. The agent can use any skill in the project wherever you are working. The category decides where a skill is suggested: the skills listed above the message box are the current module's skills plus **General Skills**, and the "/" picker lists the current module's skills first.

| Skill Category        | Suggested when you work in |
| --------------------- | -------------------------- |
| General Skills        | Anywhere in the project    |
| Knowledge Base Skills | Knowledge Base             |
| Requirements Skills   | Requirements               |
| Blueprints Skills     | Blueprints                 |
| Work Orders Skills    | Work Orders                |
| Feedback Skills       | Feedback                   |

Pick **General Skills** for guidance that applies across the whole project.

## The description and the body [#the-description-and-the-body]

In the skill editor, write the description on the line under the **Description** label at the top. The body below it holds the full instructions the agent follows once the skill is loaded.

The description does two jobs. The agent uses it to decide whether a skill fits the task at hand, and it appears under the skill's name in the skill picker and the "/" menu. Write it as a trigger, not a summary.

**Write descriptions as a trigger**
  Start with "Use when..." so the agent can match the skill to a task. For
  example: "Use when drafting or editing release notes for 8090 Software Factory
  releases." Keep the description short. The body can be as long as the guidance
  needs.

## Creating a skill [#creating-a-skill]

  
    ### Open the create dialog [#open-the-create-dialog]

    In the Skills navigator's **Tree*&#x2A; view, open the &#x2A;*+** menu on the category the skill belongs to and choose **Create Skill**. The dialog, for example **Create General Skill**, takes its category from that section.

    In the **A–Z** and **Recently edited** views, select **Create skill** instead, choose a **Skill Category** in the **Create Skill** dialog, and select **Create Skill**.
  

  
    ### Give it a title [#give-it-a-title]

    Enter a clear title and select **Create**.
  

  
    ### Write the description and body [#write-the-description-and-body]

    The skill opens in the editor. Write the description as a trigger, starting with "Use when...", then put the full guidance the agent should follow in the body. Your changes save automatically.
  

You can also turn Markdown or plain text files into skills. Select **Upload file** on a category, or drag the files onto a category. Each file becomes a skill named after the file.

## Invoking a skill [#invoking-a-skill]

A skill can be loaded into a conversation in several ways:

* **Skills above the message box.** In a new, empty conversation, the agent panel lists skills above the message box. Select one to add it to your message. If there are more than fit, **More** opens the rest.
* **"/" in the message box.** Type "/" to pick any skill in the project for the message you are writing.
* **"/" in automations.** In an automation's prompt, type "/" to add a skill. The automation loads that skill's current content every time it runs.
* **Automatic matching.** The agent loads a skill on its own when the task matches the skill's description, without you naming it.

Writing-rules skills aren't listed above the message box, but you can still pick them with "/".

## Skill Rules [#skill-rules]

A Skill Rule makes the agent read a skill before it takes an action. For example, a rule can require the agent to read your house style skill before it creates or edits Blueprints.

To add rules, open a skill's three-dot menu (&#x2A;*⋮**) in the navigator and select **Add Rules**, or **Edit Rules** once the skill has rules. In the **Skill Rules** dialog, select **Add Rule**, choose an action, and select **Save**. The actions are **Create and Edit Requirements**, **Create and Edit Blueprints**, **Create and Edit Work Orders**, **Create and Edit Resources** (Knowledge Base documents), and **Create and Edit Themes**.

With a rule in place, the agent can't create or edit that kind of item until it has read the current version of the skill in the conversation. If the skill changes, the agent reads it again. Rules apply to the agent in 8090 Software Factory, not to coding agents connected over MCP. Adding or changing rules needs edit access to Skills.

## Built-in skills [#built-in-skills]

Every project gets its own copy of the built-in skills, such as **Plan**, **Triage Feedback**, and the writing-rules skills. Each copy is a normal skill in your project, with version history. You can edit, rename, or delete it, except that the writing-rules skills can't be deleted. A deleted built-in skill doesn't come back on its own, but you can add it again from the Library.

When a new release changes a built-in skill, your copy stays as it is and shows a notice that a newer version is available. You choose whether to update. See [Skills Library](#skills-library).

### Writing-rules skills [#writing-rules-skills]

Every project ships with built-in writing-rules skills that set how the project writes each document type: **Blueprints Writing Rules**, **Requirements Writing Rules**, and **Work Orders Writing Rules**. They are the project's shared writing standard. Each one comes with a Skill Rule for its document type, so the agent reads the current writing-rules skill before it creates or edits that kind of document, and an edited standard takes effect on the next write.

You can edit these skills to match your team's house style, but you can't delete them, because the agent relies on them whenever it writes that document type. They come with real content. The Blueprints rules, for example, define the sections each blueprint uses, including its Architecture Decision Records.

### Theme Writing [#theme-writing]

The built-in **Theme Writing** skill, in **Feedback Skills**, is the convention the agent follows when it creates or edits a feedback theme. It has three child templates: **Bug theme template**, **Enhancement theme template**, and **Feature request theme template**. The parent skill tells the agent which template fits the theme.

## Skills Library [#skills-library]

The Skills Library shares skills across the projects in your organization. It holds the built-in skills and every skill a project has published.

* **Publish to Organization.*&#x2A; Open a skill's &#x2A;*⋮** menu and select **Publish to Organization** so any project in the organization can copy it. Later edits stay in your project until you select **Republish to Organization**, which publishes the current content as a new version. The skill's Skill Rules are published with it. Publishing needs edit access to Skills.
* **Add from Library.*&#x2A; Open a category's &#x2A;*+** menu and select **Add from Library** to browse built-in and published skills, then select **Add** on the one you want. It is copied into your project as your own skill to edit, and you are notified when its source changes. Adding needs create access to Skills.
* **Update from Source.** When a copied skill's source has a newer version, the skill shows a notice. Open **Update Options** and select **Update from Source**, or use **Update from Source*&#x2A; in the skill's &#x2A;*⋮** menu, to replace the skill's content with the newer version. If you have edited your copy, the button reads **Replace My Edits**, and **Reconcile with Agent** is offered instead to merge the newer version into your copy as suggested edits.

Organization admins manage published skills in **Settings → Organization → Published Skills**. Deleting a published skill there removes it from the Library. Projects that already copied it keep their copies, but those copies stop receiving updates.

## Nested skills and per-user overrides [#nested-skills-and-per-user-overrides]

Skills can nest. A parent skill groups child skills that only apply in its context, and the parent tells the agent which child to use. Two patterns are common.

**Template families.** A parent skill can hold one child template per variant. The built-in **Theme Writing** skill works this way: it parents a bug template, an enhancement template, and a feature request template, and picks the one that fits the theme at hand.

**Per-user overrides.** A parent skill can point the agent to a personal style for a specific teammate. The parent tells the agent that when the current user is that teammate, it should follow that person's own child skills, such as their personal blueprint and work order styles, instead of the project's writing-rules skills. The override depends on who is using the agent, so the same project produces house-standard documents for most people and a personal format for that teammate.

**One standard, room for exceptions**
  Per-user overrides let a project keep a single shared standard while letting
  individuals opt into their own format, without forking the project rules.

## Versions and comments [#versions-and-comments]

Every skill in the project is versioned automatically, like blueprints and requirements, including your copies of built-in skills. Each edit creates a new version. You can open the version history, read any past version, and see who changed it, including whether a change came from the agent or a person. Because skills are versioned, you can see how a shared standard evolved, and the agent always applies the current version.

You can also leave comment threads on a skill, so a team can discuss wording in a shared standard the same way it comments on any other document.

## Export [#export]

To download skills, select **Export** in the skill editor. Choose **Export this skill** or **Export all skills as one document**. Skills export as Markdown.

## Skills over MCP [#skills-over-mcp]

Coding agents connected over [MCP](/connections/connect-coding-agent) can list, read, create, edit, and delete a project's skills. Deleting asks you to [confirm](/connections/connect-coding-agent#confirmations) first. A skill created over MCP appears right away, but its content, like any edit made over MCP, arrives as suggested changes that you review and accept in the editor.

## Not the same as the coding-agent plugin [#not-the-same-as-the-coding-agent-plugin]

The [8090 Software Factory agent skill](/opinions/agent-skill) is a different thing. You install it into a coding agent such as Cursor or Claude Code, and it teaches that agent how to work with 8090 Software Factory over MCP. The skills on this page live inside a project and guide the project agent.

Want the agent to draw on more of your team's material? [Learn about the Knowledge Base](/modules/knowledge-base).
