# Log

## 2026-10-25 ingest | YouTube — How to Build a Software Factory for AI Coding Agents (Boundary)

- Ingested 1 youtube video `https://www.youtube.com/watch?v=tGbjIvvYuHE` (auto-en captions, 1:10:45); skipped 0
- Source pages: youtube-tGbjIvvYuHE
- New pages: none (first source; no slug at ≥2 origins)
- Updated pages: overview (created)
- Waiting at 1 mention: claude-code, codex, coderabbit, human-layer, baml, software-factory, agent-harness, control-plane, dev-environment, compounding-engineering, agentic-merge-queue, multi-repo-development, agent-evals, human-in-the-loop

## 2026-10-25 ingest | Warp docs llms.txt — Warp Factories section

- Catalog `https://docs.warp.dev/llms.txt` (402 links, 70 under /factories/); user chose 52 pages: all /factories/ except the 18 per-error-code pages (errors index kept); 52 fetched, 0 skipped
- Docs set: llms-docs-warp-dev (one origin); hub `wiki/docs/llms-docs-warp-dev/OVERVIEW.md` (10 areas, 30 candidates)
- Source pages: 52 under `wiki/docs/llms-docs-warp-dev/` (factories, factories-how-factories-work, factories-factory-agents, factories-factory-skills, factories-infrastructure-and-security, factories-factory-as-code, factories-self-hosting-*, factories-integrations-*, …)
- New pages: claude-code (entity, 2 origins), codex (entity, 2 origins), agent-evals, agent-harness, control-plane, dev-environment, human-in-the-loop, multi-repo-development, software-factory (concepts, 2 origins each: Boundary podcast + Warp docs)
- Updated pages: overview (1 → 53 source-like pages, 4 themes)
- Waiting at 1 origin: warp-factories, factory-as-code, foreman-agent, agent-skill, mcp, self-hosting, agent-runner, secrets-management, webhook, git-worktree, github, slack, … (27 slugs)
- Removed an empty Obsidian stub `wiki/wiki/sources/youtube-tGbjIvvYuHE.md` (vault opened at `wiki/` breaks `[[wiki/...]]` links)
- Fixed unquoted `: ` in `wiki/concepts/dev-environment.md` description; `build_index_md.py` exits 0 (63 pages)

## 2026-10-25 ingest | 2 Warp repos (warp-factory-examples, common-skills)

- Cloned `https://github.com/warpdotdev/warp-factory-examples` @ `84e7c95` and `https://github.com/warpdotdev/common-skills` @ `8792394` into `raw/repos/` (gitignored); 2 new, 0 skipped, 0 refreshed
- Repo pages: `wiki/repos/github-warpdotdev-warp-factory-examples/ARCHITECTURE.md`, `wiki/repos/github-warpdotdev-common-skills/ARCHITECTURE.md`
- New pages: github (entity, 3 origins), linear (entity, 2), slack (entity, 3), warp-factories (entity, 2), agent-skill (concept, 3), factory-as-code (concept, 3), foreman-agent (concept, 2), secrets-management (concept, 2), self-hosting (concept, 2)
- Updated pages: claude-code, codex, agent-evals, agent-harness, control-plane, human-in-the-loop, multi-repo-development, software-factory (now 3–4 origins each)
- Caveat: 3 of 4 origins are Warp (docs set + 2 repos); the 9 new pages rest on Warp's voice alone, flagged in each Synthesis line
- Overview rewritten (Repos section added); `build_index_md.py` exits 0 (74 pages)
- Waiting at 1 mention: aws-ecr, azure-devops, baml, coderabbit, docker, gitlab, human-layer, jira, kubernetes, microsoft-teams, sentry, vercel, agent-runner, agentic-merge-queue, compounding-engineering, git-worktree, mcp, webhook

## 2026-10-25 layout | docs sets move to `raw/docs/`

- Moved `raw/llms-docs-warp-dev/` → `raw/docs/llms-docs-warp-dev/` (53 files, unchanged), mirroring `raw/repos/`
- Rewrote `[[raw/llms-docs-warp-dev/...]]` citations to `[[raw/docs/llms-docs-warp-dev/...]]` across wiki pages; earlier log entries keep the old path
- Skill updated: `fetch_llms_txt.py` default folder, `SKILL.md`, `CONVENTIONS.md`, `SOURCES.md`, `PAGES.md`, `agents/docs_writer.md`
- `build_index_md.py` exits 0 (74 pages); `fetch_llms_txt.py --list` still sees all 52 pages as present

## 2026-10-25 ingest | 4 llms.txt docs sets (Mastra Factory, 8090, Factory.ai, Port)

- Catalogs: `https://factory.mastra.ai/llms.txt` (24 links), `https://docs.8090.ai/llms.txt` (158), `https://docs.factory.com/llms.txt` (120), `https://docs.port.io/llms.txt` (753); `docs_selector` picked 10 per set; 40 fetched, 0 skipped
- Docs sets (one origin each): llms-factory-mastra-ai, llms-docs-8090-ai, llms-docs-factory-com, llms-docs-port-io; one `OVERVIEW.md` hub each (8, 12, 13, 13 areas)
- Source pages: 40 under `wiki/docs/<set>/` (what-is-factory, using-*, configure-*, deployment; general-*, modules-*, opinions-*, codebase-overview; software-factory-*, missions-overview, environments-overview, droid-exec-overview, agent-readiness-overview, harness-*; getting-started-agentic-sdlc-pillars, glossary, context-lake-overview, workflows-concepts, solutions-*, agent-management-*, guides-all-trigger-ai-coding-assistants-from-port)
- New pages: gitlab (entity, 2 origins), jira (entity, 3), microsoft-teams (entity, 2), sentry (entity, 2), context-engineering (concept, 3), git-worktree (concept, 2), knowledge-base (concept, 2), knowledge-graph (concept, 2), mcp (concept, 4), webhook (concept, 3)
- Updated pages: claude-code (7 origins), codex (5), github (7), linear (4), slack (7), agent-harness (6), agent-skill (7), control-plane (4), dev-environment (4), factory-as-code (5), human-in-the-loop (8), secrets-management (3), self-hosting (3), software-factory (8)
- Overview rewritten (95 source-like pages, 4 themes); `build_index_md.py` exits 0 (128 pages)
- Waiting at 1 origin: mastra-factory, 8090-software-factory, port, agentops, agent-runner, agentic-merge-queue, compounding-engineering, docker, kubernetes, aws-ecr, azure-devops, vercel, baml, coderabbit, human-layer
- Caveats: factory-as-code and github writers read only the relevant lines of older sources; factory-as-code body was rewritten, not strictly merged; agent-skill is over the 500-word budget

## 2026-10-25 query | inner and outer loop

- question: "what is inner and outer loop?"
- pages used: 5 (agent-harness, control-plane, software-factory, youtube-tGbjIvvYuHE, claude-code)
- saved: wiki/questions/2026-10-25-inner-and-outer-loop.md + wiki/notes/inner-and-outer-harness.md
- open question logged: general dev-tooling "inner loop / outer loop" terms not covered by any source

## 2026-10-26 ingest | 2 YouTube videos (Boundary channel)

- Ingested 2 videos; skipped 0: `https://www.youtube.com/watch?v=XUEfIxkdT2Q` ("How to Build an AI Software Factory That Ships Faster", 52:27, auto-en) and `https://www.youtube.com/watch?v=b5O6gb_Zuk8` ("Agents, Subagents, Skills and Commands", 1:00:05, auto-en)
- Source pages: youtube-XUEfIxkdT2Q, youtube-b5O6gb_Zuk8
- New pages: none (every touched slug was already qualifying)
- Updated pages (first video): warp-factories (54 pages), slack (29), software-factory (19), factory-as-code (37), agent-evals (13), human-in-the-loop (37), agent-skill (27)
- Updated pages (second video): claude-code (14), agent-skill (28), agent-harness (15), context-engineering (5), multi-repo-development (5), git-worktree (5), human-in-the-loop (38), software-factory (20), mcp (17)
- Overview rewritten (97 source-like pages, 4 themes); `build_index_md.py` exits 0 (132 pages)
- Suggested slugs not yet linked from any page: risk-based-code-review, factory-yield-metrics, subagent, slash-command, coordination-repo
- Waiting at 1 origin: agent-runner, agentops, agentic-merge-queue, compounding-engineering, docker, kubernetes, aws-ecr, azure-devops, vercel, 8090-software-factory, mastra-factory, port, baml, coderabbit, human-layer
- Caveats: page writers merged only the new source into existing pages; mcp lists 17 sources against 31 mentioning pages (pre-existing gap); agent-evals is likely over the 500-word budget; both videos and youtube-tGbjIvvYuHE share the Boundary channel and hosts, and XUEfIxkdT2Q features Warp's CEO, so writers marked them as not independent
