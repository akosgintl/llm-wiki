@AGENTS.md

## Claude Code specifics

- The skill is discovered via the `.claude/skills` symlink and invoked as
  `/my-llm-wiki`. It also triggers on ingest/query requests about a wiki.
- Spawn the skill's writers with the Agent tool: pass the full body of
  `agents/<name>.md` as the prompt, use `model: sonnet`, and put several writers in
  one message so they run in parallel. Expect one JSON receipt from each.
- Do not read `raw/` or the generated wiki pages in the main thread during
  ingest. Keep to receipts and script output (`CONVENTIONS.md` §12).
- The shell is Git Bash on Windows. Use `cmd //c 'mklink /D …'` for symlinks:
  `ln -s` and PowerShell `New-Item` with a relative target do not produce correct
  relative links here.
