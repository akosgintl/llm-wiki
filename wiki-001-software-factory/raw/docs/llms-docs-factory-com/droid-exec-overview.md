---
title: "Droid Exec (Headless)"
subtitle: "Non-interactive execution mode for CI/CD pipelines and automation scripts."
authors: []
published_date: null
source_url: https://docs.factory.com/droid-exec/overview.md
origin: llms-txt
llms_txt: https://docs.factory.com/llms.txt
section: "Documentation"
fetched: 2026-10-25T18:18:02Z
---

# Droid Exec (Headless)

Non-interactive execution mode for CI/CD pipelines and automation scripts.

Droid Exec is Factory's headless execution mode designed for automation workflows. Unlike the interactive CLI, `droid exec` runs as a one-shot command that completes a task and exits, making it ideal for CI/CD pipelines, shell scripts, and batch processing.

  Start from a recipe: [lint autofix](/droid-exec/recipes/lint-autofix), [organize imports](/droid-exec/recipes/organize-imports), [error message refactors](/droid-exec/recipes/error-messages), [dependency and secret scanning](/droid-exec/recipes/dependency-secret-scan), or [daily docs and tests](/droid-exec/recipes/daily-docs-tests).

## Summary and goals

Droid Exec is a one-shot task runner: it produces readable logs (and structured artifacts when requested), keeps mutations and command execution opt-in so runs are secure by default, fails fast on permission violations with clear errors, and composes simply for batch and parallel work.

  **Non-Interactive**
    Single run execution that writes to stdout/stderr for CI/CD integration
  
  **Secure by Default**
    Read-only by default with explicit opt-in for mutations via autonomy levels
  
  **Composable**
    Designed for shell scripting, parallel execution, and pipeline integration
  
  **Clean Output**
    Structured output formats and artifacts for automated processing
  

## Execution model

Each run is a single non-interactive pass that writes to stdout/stderr. By default the run is read-only: Droid can read files and run read-only commands, but can't edit anything. Add `--auto` to allow edits and commands, with risk tiers gating what can run.

Options (run `droid exec --help` for the full list, examples, and available models):

```text
Usage: droid exec [options] [prompt]

-o, --output-format <format>   text|json|stream-json|stream-jsonrpc|acp
--input-format <format>        stream-jsonrpc for multi-turn sessions
-f, --file <path>              Read prompt from file
--auto <level>                 Autonomy level: low|medium|high
--skip-permissions-unsafe      Skip all permission prompts (unsafe)
--disable-builtin-skills       Disable Factory-provided builtin skills
-s, --session-id <id>          Continue an existing session
--fork <id>                    Fork a session into a new session
-m, --model <id>               Model ID to use
-r, --reasoning-effort <level> Reasoning effort (defaults per model)
--spec-model <id>              Model ID for spec mode
--spec-reasoning-effort <lvl>  Reasoning effort for spec mode
--use-spec                     Start in spec mode
--only-tools <ids>             Use only these tools
--add-tools <ids>              Add tools to the default set
--remove-tools <ids>           Remove tools from the allowed set
--list-tools                   List tools for the selected model and exit
--cwd <path>                   Working directory path
--settings <path>              Settings file merged for this run only
-w, --worktree [name]          Run in a git worktree
--tag <spec>                   Session tag (name or JSON, repeatable)
--log-group-id <id>            Log group ID for filtering logs
--append-system-prompt <text>  Append text to the system prompt
--append-system-prompt-file <path>
                               Append a file to the system prompt
--mission                      Run in mission mode
--worker-model <id>            Model for mission workers
--worker-reasoning-effort <l>  Reasoning effort for mission workers
--validator-model <id>         Model for mission validators
--validator-reasoning-effort <l>
                               Reasoning effort for mission validators
```

Use any [available model ID](/models) with `--model` or `--spec-model`. For custom models, see [Custom Models (BYOK)](/model-independence/byok).

For multi-turn sessions, use `--input-format stream-jsonrpc` with a matching `--output-format stream-jsonrpc` and drive the session over [raw JSON-RPC](#build-custom-flows-on-raw-json-rpc). The older `stream-json` input mode still parses but is deprecated and prints a warning.

## Installation

  **Install the Droid CLI**
    **macOS/Linux:** `curl -fsSL https://app.factory.ai/cli | sh`

**Homebrew:** `brew install --cask droid`

**Windows:** `irm https://app.factory.ai/cli/windows | iex`

**npm:** `npm install -g droid`
  

  **Get Factory API Key**
    Generate your API key from the <a href="https://app.factory.ai/settings/api-keys">Factory Settings Page</a>
  

  **Set Environment Variable**
    Export your API key as an environment variable:
    ```bash
    export FACTORY_API_KEY=fk-...
    ```
  

## Quickstart

### Direct prompt

```bash
droid exec "analyze code quality"
droid exec "fix the bug in src/main.js" --auto low
```

### From file

```bash
droid exec -f prompt.md
```

### Pipe

```bash
echo "summarize repo structure" | droid exec
```

### Session continuation

```bash
droid exec --session-id <session-id> "continue with next steps"
```

## Autonomy levels

Droid exec uses tiered autonomy to control what operations can run without manual confirmation. It starts read-only by default; use explicit flags when an automation needs to modify files, install dependencies, or touch external systems.

| Mode | Allows | Blocks or limits | Best for |
| :--- | :----- | :--------------- | :------- |
| Default, no flags | Read-only file inspection, directory listing, process and environment inspection, and git read operations such as `git status`, `git log`, and `git diff`. | File edits, package installs, git writes, system changes, and deployments. | Analysis, planning, architecture review, security review, and reports. |
| `--auto low` | Low-risk project file creation and edits. | System modifications, package installs, remote writes, and production changes. | Documentation updates, formatting, adding comments, and simple local edits. |
| `--auto medium` | Low-risk actions plus common local development operations such as trusted package installs, builds, tests, `git commit`, `git checkout`, and `git pull`. | `git push`, sudo commands, production changes, and sensitive or irreversible operations. | Local development, dependency updates, test fixes, and CI preparation. |
| `--auto high` | High-risk automation including remote writes, deployments, database migrations, and commands that may access sensitive data, subject to Droid's remaining hard safety checks. | Extreme destructive operations such as `sudo rm -rf /` and system-wide unsafe changes. | CI/CD pipelines, staging deployments, and fully automated workflows in controlled environments. |
| `--skip-permissions-unsafe` | Skips all permission prompts. | Command blocks still apply. Cannot be combined with `--auto` flags. Use only where the environment is disposable. | Throwaway containers, ephemeral CI runners, and temporary VMs. |

Examples:

```bash
# Analyze and plan without making changes
droid exec "List the files an OAuth2 migration of the auth module touches"

# Allow simple file edits
droid exec --auto low "add JSDoc comments to all exported functions"

# Allow normal local development operations
droid exec --auto medium "install deps, run tests, and fix failing checks"

# Allow deployment-oriented automation in a controlled environment
droid exec --auto high "fix the bug, run tests, commit, and push the branch"
```

  `--skip-permissions-unsafe` skips all permission prompts, but command blocks still apply.
  Only use it in completely isolated environments such as Docker containers,
  throwaway VMs, or ephemeral CI runners that are destroyed after the job.

The Droid CLI needs a glibc-based Linux image, such as Debian or Ubuntu. It doesn't run on Alpine.

```bash
# In a disposable Docker container
docker run --rm -e FACTORY_API_KEY -v "$PWD:/workspace" -w /workspace \
  debian:stable-slim sh -c '
  apt-get update && apt-get install -y curl ca-certificates git &&
  curl -fsSL https://app.factory.ai/cli | sh &&
  ~/.local/bin/droid exec --skip-permissions-unsafe \
    "Install system dependencies and run the integration tests"
'
```

### Fail-fast behavior

If Droid tries an action above the current autonomy level, `droid exec` stops at that action, prints an error to stderr, and exits non-zero. Edits Droid made before that point stay in the working tree, so check `git status` or discard them before you retry at a higher level.

### Command policy in automation

[Permission rules](/autonomy-and-safety/permission-rules) can allow commands, require
approval, or block them. A one-shot run cannot collect an interactive approval, so an
effective `ask` is not cleared merely by using `--auto high`. A matching block has no
approval path, including under `--skip-permissions-unsafe`.

Before running an automation, validate and preview its command policy from the relevant
repository:

```bash
droid rules check
droid rules check --command 'git push origin main' --json
```

The preview does not execute the command or evaluate every runtime check. A successful
check can report `block`; inspect the decision rather than treating exit code `0` as an
allow verdict.

Legacy `commandAllowlist`, `commandDenylist`, and `commandBlocklist` settings are
deprecated but remain respected for backward compatibility. Use `permissionRules` for
new automation policy and review [migration guidance](/autonomy-and-safety/permission-rules#migrate-legacy-command-lists)
before removing existing restrictions.

## Output formats and artifacts

Choose an output format with `-o, --output-format`:

- `text` (default): Droid's final response, for logs or redirecting to a file.
- `json`: one JSON object when the run ends.
- `stream-json`: one JSON event per line while the run progresses.
- `stream-jsonrpc`: the full JSON-RPC protocol, for [custom integrations](#build-custom-flows-on-raw-json-rpc).

### text (default)

```bash
$ droid exec --auto low "Create hello.py that prints hello world"
Created hello.py, which prints "hello world" when you run it.
```

### json

The result arrives as one line. It's formatted here for reading:

```bash
$ droid exec -o json "Summarize this repository in one sentence"
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 5657,
  "num_turns": 1,
  "result": "A TypeScript monorepo with an API and a UI package.",
  "session_id": "8af22e0a-d222-42c6-8c7e-7a059e391b0b",
  "usage": {
    "input_tokens": 4,
    "output_tokens": 18,
    "cache_read_input_tokens": 13528,
    "cache_creation_input_tokens": 17913,
    "factory_credits": 36947,
    "ttft_ms": 2609
  }
}
```

Use JSON when a script needs the result text, the session ID for a follow-up run, or token usage:

```bash
out=$(droid exec -o json "Summarize this repository in one sentence")
echo "$out" | jq -r .result
droid exec -s "$(echo "$out" | jq -r .session_id)" "Now list its packages"
```

### stream-json

Each line is an event: `system` (session start, with the working directory, model, and tools), `message`, `tool_call`, `tool_result`, and a final `completion` with the response text and usage. Use it to show progress in build logs or to record which tools ran:

```bash
droid exec -o stream-json --auto medium "Fix the failing test" \
  | jq -r 'select(.type == "tool_call") | .toolName'
```

### Build custom flows on raw JSON-RPC

For custom integrations, you can run Droid as a long-lived subprocess and drive the full JSON-RPC control surface over stdin/stdout:

```bash
droid exec --input-format stream-jsonrpc --output-format stream-jsonrpc \
  --auto low
```

Each stdin line is one JSON-RPC request. Each stdout line is a JSON-RPC response, a request from Droid, or a notification. Your client:

- spawns `droid exec` in the project directory with the flags it needs
- writes newline-delimited requests, each with a unique `id`
- reads stdout line by line and matches responses by `id`
- handles timeouts, process cleanup, and session persistence

The core methods and events:

  
    Start a new session; a client calls this (or `droid.load_session` to resume
    an existing session) first.
  
  
    Send a turn to the session.
  
  
    Event stream your client handles: assistant text deltas, tool events, token
    usage, errors, and turn completion.
  
  
    Server-to-client request your client must answer; `droid.ask_user` arrives
    the same way.
  

Further session methods interrupt work, update settings, manage MCP servers/tools, inspect context, fork sessions, or compact history.

Teams use this to build their own agent UIs in web, desktop, or IDE apps, job runners and orchestrators that queue and resume sessions, policy layers that approve or audit permission requests, and bridges from Droid events into a message bus or telemetry pipeline.

To disable Factory-provided builtin skills, set `disableBuiltinSkills` when initializing or loading the session:

```json
{"jsonrpc":"2.0","id":"1","method":"droid.initialize_session","params":{"machineId":"my-machine","cwd":"/workspace","disableBuiltinSkills":true}}
{"jsonrpc":"2.0","id":"2","method":"droid.load_session","params":{"sessionId":"session-123","disableBuiltinSkills":true}}
```

In stream JSON-RPC mode, use the request field instead of the `--disable-builtin-skills` CLI flag. The TypeScript SDK exposes the same option through `createSession({ disableBuiltinSkills: true })` and `resumeSession(sessionId, { disableBuiltinSkills: true })`.

For protocol reference and implementation patterns, see the low-level client and process transport in the [TypeScript SDK](/sdk/typescript).

Prefer an SDK when possible:

- **TypeScript**: [`@factory/droid-sdk`](/sdk/typescript) for Node.js apps, streaming, multi-turn sessions, structured output, permissions, tool controls, and SDK-backed MCP tools
- **Python**: [`droid-sdk`](/sdk/python) for asyncio apps, streaming, direct client control, notifications, permissions, and typed event handling

### Write artifacts

For a report, redirect `text` output to a file. The run stays read-only:

```bash
droid exec "List the direct dependencies and what each one does" > deps.md
```

When the pipeline needs a structured file, ask Droid to write it, which needs `--auto low`. Then check the file before you use it:

```bash
droid exec --auto low "Write deps.json: an array of {name, version, usedIn}
for each direct dependency"
jq -e 'type == "array"' deps.json
```

## Working directory

Use `--cwd` to run Droid in another directory, such as one package of a monorepo. Pass an absolute path:

```bash
droid exec --cwd "$PWD/packages/api" "Map this package's internal modules"
```

Use `-w, --worktree [name]` to run the task inside an isolated [git worktree](/droid-cli/cli-reference#git-worktrees) on its own branch. This is useful for fanning out parallel `droid exec` jobs against the same repo without file conflicts:

```bash
droid exec --worktree codemod-a --auto medium "apply codemod A" & a=$!
droid exec --worktree codemod-b --auto medium "apply codemod B" & b=$!
wait "$a"; status_a=$?
wait "$b"; status_b=$?
[ "$status_a" -eq 0 ] && [ "$status_b" -eq 0 ]
```

Clean worktrees are auto-removed on exit; dirty ones are preserved so you can review and push the work.

## Models and reasoning effort

Choose a model with `-m` and adjust reasoning with `-r`. Valid reasoning levels depend on the model. See [Factory-Managed Inference](/models) for available models.

```bash
droid exec -m claude-opus-5-5 -r medium -f plan.md
```

Use `--use-spec` to start in specification mode, where the agent plans before executing:

```bash
droid exec --use-spec --auto low "refactor the auth module"
```

You can also use a different model for the spec phase:

```bash
droid exec --use-spec --spec-model claude-opus-5-5 --auto medium \
  "implement feature X"
```

### Tool controls

List the tools available for a model at the current autonomy level:

```bash
droid exec --list-tools
droid exec -m claude-opus-5-5 --auto low --list-tools -o json
```

Select tools by name, such as `Read` or `Execute`, or by MCP server with `MCP:<server>` or `MCP:<server>/<tool>`. Separate entries with commas or spaces:

```bash
# Use only these tools
droid exec --only-tools Read,Grep,Glob,LS "Map the auth module"

# Allow edits but no shell commands
droid exec --auto low --remove-tools Execute "Add JSDoc to src/api"

# Add every tool from a configured MCP server
droid exec --add-tools MCP:linear "Summarize my open issues"
```

An unknown tool name fails the run before Droid starts.

### Skill controls

Use `--disable-builtin-skills` when an interactive or non-interactive session should expose only skills supplied outside the Droid CLI:

```bash
# Start the interactive TUI without builtin skills
droid --disable-builtin-skills

# Run one non-interactive session without builtin skills
droid exec --disable-builtin-skills "analyze this repository"
```

This removes Factory-provided builtin skills while preserving user, project, plugin, automation, mission, runtime, and dynamically supplied skills. For an interactive launch, the restriction remains active when you create, resume, or switch sessions. It is also inherited by child sessions, including subagents and mission workers.

  The flag is not supported in Agent Client Protocol (ACP) mode. Use it with standard `droid` or `droid exec`, or set `disableBuiltinSkills` on `droid.initialize_session` and `droid.load_session` requests in stream JSON-RPC mode.

### Custom models

You can configure custom models to use with droid exec by adding them to your `~/.factory/settings.json` file:

```json
{
  "customModels": [
    {
      "model": "my-codex-model",
      "displayName": "My Custom Model",
      "baseUrl": "https://api.openai.com/v1",
      "apiKey": "${OPENAI_API_KEY}",
      "provider": "openai"
    }
  ]
}
```

To use a custom model, use the `custom:` prefix followed by the display name (with spaces replaced by dashes) and the index:

```bash
droid exec --model "custom:My-Custom-Model-0" "analyze this codebase"
```

If you have multiple custom models configured:

```json
{
  "customModels": [
    {
      "model": "moonshotai/kimi-k2-instruct-0905",
      "displayName": "Kimi K2 [Groq]",
      "baseUrl": "https://api.groq.com/openai/v1",
      "apiKey": "${GROQ_API_KEY}",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    },
    {
      "model": "openai/gpt-oss-20b",
      "displayName": "GPT-OSS-20B [OpenRouter]",
      "baseUrl": "https://openrouter.ai/api/v1",
      "apiKey": "YOUR_OPENROUTER_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 32000
    }
  ]
}
```

You would reference them as:

- `--model "custom:Kimi-K2-[Groq]-0"`
- `--model "custom:GPT-OSS-20B-[OpenRouter]-1"`

The index corresponds to the position in the `customModels` array (0-based).

Reasoning effort (`-r` / `--reasoning-effort`) does not apply to custom models; it is controlled by the model and provider you configure.

## Sessions, tagging, and logs

Forking lets you branch off an existing session without disturbing the original; the new run starts from the forked session's history and is assigned a fresh session ID.

```bash
# Continue a session in-place
droid exec --session-id <session-id> "next steps"

# Branch off a session into a new run
droid exec --fork <session-id> --auto low "try an alternative refactor"
```

Use `--tag` to attach searchable labels to a run. The flag is repeatable and accepts either a plain name or a JSON object for structured metadata. Pair it with `--log-group-id` to bucket logs from related runs together for easier filtering and aggregation downstream.

```bash
droid exec \
  --tag release-v2 \
  --tag '{"name":"team","value":"platform"}' \
  --log-group-id ci-nightly \
  --auto low "run nightly checks and write report.md"
```

## Customizing the system prompt

Use `--append-system-prompt` to append additional text to the end of the system prompt for a single run, or `--append-system-prompt-file` to append the contents of a file. Both flags can be combined and are useful for injecting project-specific guidance, style guides, or invariants without modifying global settings.

```bash
droid exec \
  --append-system-prompt "Always prefer functional React components." \
  --auto low "review src/components for class-based components"

droid exec \
  --append-system-prompt-file ./docs/style-guide.md \
  --auto low "lint prose in README.md against the style guide"
```

## Mission Mode

Mission Mode runs `droid exec` as a multi-agent orchestrator that plans work, delegates to worker agents, and validates results. Enable it with `--mission` and optionally select dedicated models and reasoning effort levels for the worker and validator roles. Mission Mode requires `--auto high` or `--skip-permissions-unsafe` because the orchestrator needs high autonomy to manage workers.

```bash
droid exec --mission \
  --worker-model claude-opus-5-5 \
  --worker-reasoning-effort medium \
  --validator-model gpt-6-sol \
  --validator-reasoning-effort medium \
  --auto high \
  "ship the new billing webhook end-to-end"
```

### Mission Mode flags

  
    Run in Mission Mode (multi-agent orchestration).
  
  <Property name='--worker-model <id>'>
    Model ID used by mission worker agents.
  
  <Property name='--worker-reasoning-effort <level>'>
    Reasoning effort for mission workers.
  
  <Property name='--validator-model <id>'>
    Model ID used by mission validator agents.
  
  <Property name='--validator-reasoning-effort <level>'>
    Reasoning effort for mission validators.
  

The top-level `-m, --model` and `-r, --reasoning-effort` flags still apply to the orchestrator itself; the worker and validator overrides only affect the agents the orchestrator spawns.

## Batch and parallel patterns

One run per file, with bounded concurrency:

```bash
# Refactor TypeScript files, 4 at a time
find src -name '*.ts' -print0 | xargs -0 -P 4 -I {} \
  droid exec --auto low "Refactor {} to use modern TypeScript patterns"
```

One read-only run per package, in parallel, each writing its own report:

```bash
pids=()
for dir in packages/ui packages/models apps/web; do
  droid exec --cwd "$PWD/$dir" \
    "Summarize the main risks in this package" > "$dir/report.md" &
  pids+=("$!")
done
failed=0
for pid in "${pids[@]}"; do wait "$pid" || failed=1; done
[ "$failed" -eq 0 ]
```

Chunked inputs, for a list too long for one prompt:

```bash
# Review a large diff 50 files at a time, one report per chunk
chunks=$(mktemp -d)
git diff --name-only origin/main...HEAD | split -l 50 - "$chunks/"
for f in "$chunks"/*; do
  [ -e "$f" ] || continue
  files=$(tr '\n' ' ' < "$f")
  droid exec "Review these changed files: $files" > "review-${f##*/}.md"
done
rm -r "$chunks"
```

A GitHub Actions matrix that runs one read-only analysis per directory and uploads each report:

```yaml title=".github/workflows/droid-cleanup-analysis.yml"
name: Droid cleanup analysis

on:
  schedule:
    - cron: '0 1 * * 0' # Sundays at 01:00 UTC
  workflow_dispatch:

permissions:
  contents: read

jobs:
  analyze:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    strategy:
      matrix:
        module: [components, services, utils, hooks]
    steps:
      - uses: actions/checkout@v7
        with:
          persist-credentials: false

      - name: Install Droid CLI
        run: |
          curl -fsSL https://app.factory.ai/cli | sh
          echo "$HOME/.local/bin" >> "$GITHUB_PATH"

      - name: Find dead code
        env:
          FACTORY_API_KEY: ${{ secrets.FACTORY_API_KEY }}
          MODULE: ${{ matrix.module }}
        run: |
          droid exec --cwd "$GITHUB_WORKSPACE/src/$MODULE" \
            "Find unused exports, dead code, and deprecated patterns.
          Respond with a Markdown list of cleanup recommendations." \
            > cleanup-report.md

      - uses: actions/upload-artifact@v7
        with:
          name: cleanup-${{ matrix.module }}
          path: cleanup-report.md
```

For full workflows that edit code and open pull requests, see the [recipes](/droid-exec/recipes/dependency-secret-scan).

  Pull request review, security review, and PR description fill already ship as a packaged action, [`Factory-AI/droid-action`](https://github.com/Factory-AI/droid-action), so you do not need to script those flows around `droid exec`. See [Automated Code Review](/software-factory/code-review-ci) to set it up.

## More examples

License headers:

```bash
git ls-files '*.ts' | xargs -P 4 -I {} droid exec --auto low \
  "Add the Apache-2.0 license header to {} if it's missing"
```

API contract drift (read-only):

```bash
droid exec "Compare the operations in openapi.yaml to the TypeScript
client methods and list any mismatches" > drift.md
```

Blocking calls audit (read-only):

```bash
droid exec "Find synchronous child_process calls, such as execSync,
and suggest an async replacement for each" > child-process-audit.md
```

## Exit behavior

`droid exec` exits `0` when the run completes and non-zero when it stops early, for example on a permission stop, an invalid flag, or an API error. Treat non-zero as a failure in CI.

Exit `0` means Droid finished, not that the task succeeded. Check the result with your own tools, such as tests, a linter, or `jq` on an artifact.

## Best practices

- Start read-only and redirect the output to a file. Use `--auto low` only when Droid must edit files.
- Commit and push in your own script steps instead of giving Droid `--auto high`.
- Check every change with a deterministic tool before you commit it.
- Use `--skip-permissions-unsafe` only in disposable environments.
- In a monorepo, pass an absolute `--cwd` to run in one package.

  **Running in the CLI**
    Orchestrate multi-agent missions from the command line.
  
  **Automated Code Review**
    Wire Droid Exec into GitHub Actions for automated PR review.
  

