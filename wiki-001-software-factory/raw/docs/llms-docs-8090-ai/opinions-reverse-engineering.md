---
title: "Reverse engineering"
subtitle: "Turn a connected repository into a populated 8090 Software Factory project of requirements and blueprints, reconciled against the real code."
authors: []
published_date: null
source_url: https://docs.8090.ai/opinions/reverse-engineering
origin: llms-txt
llms_txt: https://docs.8090.ai/llms.txt
section: "Learn / Best practices"
fetched: 2026-10-25T18:13:39Z
---

# Reverse engineering (/opinions/reverse-engineering)

Most teams adopt 8090 Software Factory with a product that already exists and is largely undocumented, or documented in specs that have drifted from the code. Reverse engineering closes that gap. Connect your repository, let 8090 Software Factory index it, and the Agent reads the code to reconstruct what your product does, organizes it into a feature hierarchy, and writes the requirements and blueprints for you. Where you have existing specs, it reconciles what the documents say with what the code actually does and calls out the conflicts instead of papering over them. You start from a knowledge graph that reflects reality, not a blank project.

**Reconcile, don't just import**
  Uploading your old specs is optional but valuable. The Agent treats code as
  observed behavior and your documents as stated intent, then tells you exactly
  where the two disagree. Those conflicts are usually the most useful thing the
  run produces.

## How the workflow runs [#how-the-workflow-runs]

Reverse engineering is an Agent workflow you point at a connected, indexed codebase. It surveys the system, analyzes the code area by area, reconciles what it finds into a feature hierarchy, and then authors the requirements and blueprints that describe your product. Every claim it makes carries evidence: a reference to the code it came from and a confidence level, plus a note of whether your uploaded documents agree or conflict with the code.

You choose once, at the start, how hands-on the run is:

| Run mode    | What it does                                                                                                            | Pick it when                                                        |
| ----------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Cooperative | Stops to check in with you at two points: the survey scope and the proposed feature hierarchy.                          | You want to steer what gets covered and how features are organized. |
| Autonomous  | Runs end to end without stopping, and records every question it would have asked as a comment on the affected document. | You want a hands-off first pass to review afterward.                |

Either way, no document is created until the feature hierarchy is settled. The run also resumes from the current project state each time you start it, so a large repository can be worked across several sessions.

## Steps [#steps]

  
    ### Connect your codebase [#connect-your-codebase]

    Connect a GitHub repository or GitLab project so the Agent can read your
    code. Each connection tracks one selected branch. See
    [Codebase Connection](/codebase/overview) to connect a provider.
  

  
    ### Let indexing complete [#let-indexing-complete]

    After you connect, 8090 Software Factory indexes the repository so agents can
    search and read it. The initial index usually takes 5 to 10 minutes. The
    repository table in **Settings → Codebase** shows each connection's
    indexing status and updates live while a repository is still indexing.
    Wait until indexing shows complete before you start the run.

    Reverse engineering checks this for you. If a repository is not connected or
    indexing has not finished, it tells you what is missing and stops rather
    than starting a run that would fail partway.

    **Pushes keep the index current**
      Pushes to the selected branch reindex automatically, so the code index
      stays current after the first run.
    
  

  
    ### (Optional) Upload your existing intent [#optional-upload-your-existing-intent]

    If you have PRDs, specs, or design docs, add them to the project's
    [Knowledge Base](/modules/knowledge-base) so the Agent can reconcile stated
    intent against the code. It classifies every claim by whether the code and
    your documents agree or conflict.
  

  
    ### Run the Reverse Engineering workflow [#run-the-reverse-engineering-workflow]

    Open the Agent and start the **Reverse Engineering** skill. The **Get Started**
    workflow also runs it when you choose to import an existing app. The Agent
    first asks one question: should the run be cooperative, stopping to ask you
    at key points, or autonomous, running end to end. Pick cooperative if you
    want to steer scope and structure; pick autonomous for a hands-off first
    pass you review afterward.

    From there, here is what you see:

    * It **surveys the system** first, enumerating every module, entry point,
      and uploaded document into a coverage checklist, and shows you a summary
      with a diagram of the major areas. On a cooperative run you confirm or
      trim the scope here. Nothing is analyzed in depth until scope is set.
    * It **analyzes the code area by area**, reconstructing what each part does
      with a reference to the code and a confidence level behind every finding.
      Where it cannot determine something, it records the gap instead of
      guessing.
    * It **reconciles the findings into a proposed feature hierarchy**,
      organized by user-facing capability rather than by how the code is laid
      out, and re-checks the claims that shape that hierarchy against the code.
    * It **shows you the proposed hierarchy as a tree**. On a cooperative run
      you confirm it, or adjust which features exist and how they nest, before
      anything is written. This is the last stop before authoring.
  

  
    ### Review the generated requirements and blueprints [#review-the-generated-requirements-and-blueprints]

    The Agent authors an overview, then one requirements document per feature,
    parents before children. Creating a feature requirements document also
    creates its paired blueprint, and the Agent fills the blueprint from the
    observed behavior and links it to the code files it describes. Where your
    project defines architecture categories, it also fills container and
    component blueprints and a system diagram.

    Anything it could not resolve, or any conflict between your old docs and the
    code, is left as a comment on the exact document and text it concerns, so
    you review real questions instead of hunting for them. See
    [Requirements](/modules/requirements) and [Blueprints](/modules/blueprints)
    for how to work with the generated documents.

    **Edits arrive as tracked suggestions**
      Edits the Agent makes to existing documents arrive as tracked suggestions
      you approve, so a resumed run never overwrites your work silently.
    
  

  
    ### Validate with drift detection [#validate-with-drift-detection]

    The code links the Agent created are what keep your new blueprints honest as
    the code changes. To check the generated documents against the current code,
    add the **Detect Code Drift** recommended automation. It runs whenever code
    is pushed and compares each affected blueprint against the code it is
    linked to. For each contradiction it finds, it opens a separate comment
    thread on the blueprint and, for feature blueprints, on the linked
    requirements document.

    Only behavior the code contradicts counts as drift; behavior that simply is
    not built yet does not. Work through drift comments the way you would any
    comment, and resolve each one once the document or the code is brought back
    in line.
  

## Tips and pitfalls [#tips-and-pitfalls]

* **Wait for indexing.** The run will refuse to start if indexing is not finished. This is by design and saves you a failed long run.
* **Conflicts are surfaced, not resolved.** When your old specs and the code disagree, the Agent leaves a comment and keeps going. Reviewing those comments is the point, not a chore to skip.
* **Nothing is written until you confirm the hierarchy on a cooperative run.** If you chose autonomous, the tree is adopted as proposed and every question becomes a comment for you to review afterward.
* **It resumes.** On a big repository the run can stop and pick up where it left off next time you invoke it. Existing documents are treated as already covering what they describe, so it extends rather than re-authors.
* **Organize by capability.** The generated hierarchy groups features by what users can do, not by folder structure. Expect the tree to look different from your source layout, and better for it.
* **Keep the knowledge graph as the source of truth.** After the run, create and update requirements, blueprints, and work orders in 8090 Software Factory, the same commitment the [Jira migration guide](/opinions/jira-migration) describes.

**Review before you build on it**
  A reverse-engineered project is a strong starting point, not a finished
  specification. Read the generated requirements and blueprints, resolve the
  conflicts and open questions the Agent left as comments, and confirm the hierarchy
  reflects your product before teams and agents start building against it.

Next, see [Migrating from Jira](/opinions/jira-migration) to bring your active tickets into the same knowledge graph as work orders.
