---
type: question
title: what is inner and outer loop?
description: "Asked to pin down the inner/outer split the wiki uses for agent harnesses."
asked_on: 2026-10-25
created: 2026-10-25T18:49:27Z
timestamp: 2026-10-25T18:49:27Z
answer_doc: "[[wiki/notes/inner-and-outer-harness]]"
sources_cited: ["[[wiki/concepts/agent-harness]]", "[[wiki/concepts/control-plane]]", "[[wiki/concepts/software-factory]]", "[[wiki/sources/youtube-tGbjIvvYuHE]]", "[[wiki/entities/claude-code]]"]
---

# what is inner and outer loop?

> Asked on 2026-10-25 · answered from 5 wiki pages

## Answer

Full answer: [[wiki/notes/inner-and-outer-harness|Inner and outer harness]]

- Wiki names it inner/outer harness, not loop
- Inner harness: the coding agent (Claude Code, Codex)
- Outer harness: while loops that rerun, stop, escalate
- Boundary example: fix review comments, give up after 3
- Control plane feeds corrections into the outer harness
- Warp's harness field is roughly the inner harness

## Why this matters

It separates what you buy (the agent) from what you own (the loop around it).
