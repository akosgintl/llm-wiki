---
title: "Factory benchmarks"
subtitle: "Warp Factories benchmarks compare agent model and runner configurations on fixed tasks so you can choose a production configuration."
authors: []
published_date: null
source_url: https://docs.warp.dev/factories/benchmarks/
origin: llms-txt
llms_txt: https://docs.warp.dev/llms.txt
section: "Documentation Sets / Factories"
fetched: 2026-10-25T14:54:27Z
---

> For the complete documentation index, see [llms.txt](https://docs.warp.dev/llms.txt).
> Markdown versions of each page are available by appending .md to any URL.

# Factory benchmarks

Warp Factories benchmarks compare agent model and runner configurations on fixed tasks so you can choose a production configuration.

Warp Factories benchmarks compare model, harness, and runner configurations for one factory agent on the same fixed tasks. Use a benchmark to test a change on representative work before you apply it to your factory. This video shows how to compare benchmark results for quality and cost before changing a coding agent’s configuration.

![Comparing factory benchmark results to reduce coding agent costs](https://i.ytimg.com/vi/LKx5MeUsptQ/sddefault.jpg)

## How benchmarks work

A benchmark helps you choose an agent configuration based on repeatable evidence. Run representative tasks with different configurations, then compare their results before you change a live factory.

A benchmark suite is a reusable collection of tasks that evaluates one factory agent. Each task has a prompt and “Correctness criteria,” which tell the built-in Correctness Scorer what a successful trial must do. A trial is a single run of a task under one configuration. Repetitions create additional trials.

When you launch a suite, choose the configurations, Scorers, and repetitions to compare. Warp runs the trials, then scores trials that reach a terminal state. A blocked trial remains **Blocked**, but Warp can score the evidence it produced; each Scorer decides whether that evidence satisfies its criteria. The run keeps those inputs, so later changes to the suite do not change its past results.

![The Runs tab for a benchmark suite, with task, configuration, run time, and cost columns.](https://docs.warp.dev/_astro/benchmark-suite-runs.BZ2qZ0J7_Z13qS8m.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)

The Runs tab for a benchmark suite.

Use separate suites for focused questions:

-   **Factory default** - Compare models and runners to choose the default configuration for a coding agent.
-   **Frontend changes** - Compare configurations on representative frontend tasks before applying one to that workflow.

## Create and run a benchmark

To use Benchmarks, you need a factory with an agent to evaluate. Use a completed run from that agent when you want a task to reproduce real work, or write a task yourself.

This video shows how to turn your team’s coding tasks into a reusable benchmark suite.

![Creating a model benchmark from your team's coding tasks](https://i.ytimg.com/vi/mojpQjwBXN0/sddefault.jpg)

1.  In the [Warp Factories web app](https://platform.warp.dev), open your factory, click **Benchmarks**, then click **New**.
    
    ![The Benchmarks page showing saved benchmark suites, a search field, and the New button.](https://docs.warp.dev/_astro/factory-benchmarks-list.5zv9nYn9_Z1gSK2I.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    The Benchmarks page for a factory.
    
2.  Enter a name and optional description, then choose the agent to evaluate. The suite runs every task as that agent.
    
    ![The benchmark editor showing a documentation-link review suite, a selected triage agent, and the Add task action.](https://docs.warp.dev/_astro/benchmark-suite-editor.DJ1Xak2c_Z1Imrj.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    The benchmark editor with a selected agent.
    
3.  Click **Add task**. Warp saves the benchmark, then opens task setup.
    
4.  Select a completed run, then click **Add task**. To write a task instead, click **Start from scratch instead**.
    
    ![The Add task pane with a run search field, the list of completed runs, and the Start from scratch instead option.](https://docs.warp.dev/_astro/benchmark-task-source-run.PAvEwDnu_Z17b6wx.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    The task source picker.
    
5.  Review the task prompt and enter “Correctness criteria” for the task.
    
    ![The task editor with fields for a title, prompt, correctness criteria, and pinned repositories.](https://docs.warp.dev/_astro/benchmark-task-editor.pvZqHQ___Z1dNF26.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)
    
    The task editor for a benchmark suite.
    
6.  Click **Run**. In the launch dialog, choose the harness and model, or an authorized custom factory router, and the runner for each configuration.
    
7.  Add configurations, select Scorers, and set “Repetitions.” The dialog shows the number of trials created. More trials and Scorers increase the run’s cost.
    
8.  Click **Run benchmark**. The benchmark page shows its status and scored trials. You can cancel a running or scoring benchmark.
    

## Review benchmark results

After the run completes, review the result as a comparison, not as a universal model ranking:

![A completed benchmark result showing the overall recommendation, additional recommendations, total cost, and a correctness versus average cost chart.](https://docs.warp.dev/_astro/benchmark-run-results-overview.DIdTIdoQ_Le1YT.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)

A completed benchmark result and comparison chart.

-   **Overall recommendation** - Identifies the highest-quality configuration when at least two configurations have comparable results.
-   **Additional recommendations** - Highlight the most efficient and lowest-cost configurations when the result supports those comparisons.
-   **Comparison chart** - Compare the selected result dimensions across configurations.
-   **Overall table** - Compare each Scorer’s average and the combined Overall value. Expand a configuration, task, and repetition to inspect its individual trials.
-   **Scorer grids** - Show each task’s results across configurations for a selected Scorer.

![Expanded benchmark results showing trial run duration, cost, and scores for a configuration.](https://docs.warp.dev/_astro/benchmark-run-results-detail.BHLBSJkd_9KHhw.webp?dpl=dpl_BNea7GQcJKrnKidNo3xP36Bn2W7E)

Expanded trial results for a configuration.

The run’s “Total cost” includes trials and Scorer usage. Reported costs combine billed Warp inference, compute, and platform usage with available estimates for externally billed inference. Use them to compare configurations, not reconcile invoices; historical estimates and missing external costs can affect the comparison. See [charges and estimates](https://docs.warp.dev/support-and-community/plans-and-billing/credits/#charges-and-estimates).

“Run time” is the trial’s total duration, not its billable active agent time. A failed or cancelled benchmark shows only results that finished scoring before the run stopped.

## Apply a benchmark result

Change one configuration at a time. If the evidence supports a candidate, update the agent’s model or runner in the factory dashboard, or submit the change through your [factory definition](https://docs.warp.dev/factories/factory-as-code/). Keep the relevant Scorers active, then compare later production runs with the baseline you recorded before the change.

For version-controlled factories, define reusable suites in `benchmarks/<suite-slug>/suite.yaml` and their tasks in `benchmarks/<suite-slug>/tasks/<task-slug>.yaml`. See [benchmark suite files](https://docs.warp.dev/factories/factory-as-code/#benchmarkssuite-slugsuiteyaml).

## Related pages

-   [Measure and improve a factory](https://docs.warp.dev/factories/measure-and-improve/) - Configure Scorers and use benchmark evidence in an improvement loop.
-   [Factory dashboard](https://docs.warp.dev/factories/factory-dashboard/) - Track factory work, runs, and benchmark suites.
-   [Factory definition syntax](https://docs.warp.dev/factories/factory-as-code/) - Define factories and benchmark suites as code.
