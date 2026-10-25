# QUERY — the interaction path

Companion to `SKILL.md`. Loaded when Step 1 selected **query** mode. This is where
layer 03 differs from the earlier layers: querying the wiki can now *add* to it.

**The three write regimes** (`CONVENTIONS.md` §13) decide what you may touch:

| Regime | Pages | In query mode |
|---|---|---|
| ingest-owned | `raw/`, `sources/`, `entities/`, `concepts/`, `overview.md`, `repos/*/ARCHITECTURE.md` | **read-only** |
| interaction-owned | `questions/`, `notes/`, `open-questions.md` | you write these |
| repo notes | `repos/<repo>/<slug>.md` | written by an agent, then fed through the ingest tail |
| docs pages | `docs/<set>/<page>.md`, `docs/<set>/OVERVIEW.md` | fetched and written by agents (Q.6b), then fed through the ingest tail |

Reading a source can never change what the wiki says that source means. If an
answer reveals that an ingest-owned page is wrong or thin, you do **not** edit it —
you record it in `open-questions.md` and the next ingest folds it in.

---

## Q.1 — Locate the wiki

Same as `SKILL.md` Step 0. No wiki → say so and stop; do not create one to answer
a question.

## Q.2 — Load the map

Read `wiki/index.md`, then the one or two `wiki/<subdir>/index.md` files that look
relevant. In this layer the root index also lists `Questions`, `Notes` and
`Open questions` — check them: a question may already have been answered, and
enriching an existing note beats writing a second one.

## Q.3 — Walk the disclosure ladder

Index → page → `raw/` only if a page genuinely does not answer it. Prefer
entity/concept pages (already synthesized across sources) over source pages
(one source's view). Never bulk-read `raw/`, and never read a clone.

## Q.4 — Classify the question

| Class | Signal | Path |
|---|---|---|
| **repo-scoped** | names an ingested repo, or asks how some code works | Q.6 |
| **docs-scoped** | the wiki pages do not answer it, and a docs set in `wiki/docs/index.md` covers the area | Q.6b |
| **general** | everything else | Q.5 |

## Q.5 — General path

Answer from the wiki pages you read. Then decide what to keep:

1. **Always write the slim question page** — `wiki/questions/YYYY-MM-DD-<slug>.md`,
   per `PAGES.md § question`. It is a pointer, not an answer: the verbatim
   question, what it was answered from, and a link to the knowledge if there is
   any. Cap it at ~25 lines.
2. **Write or enrich a note only when the answer earned it** — the answer cited
   **≥2 wiki pages**, or the user said "save this". Otherwise the question page
   alone is the record. Most questions are conversational and should not compound.
3. **Idempotency**: if a note on the same topic exists, *enrich it in place* —
   append to `spawned_by_question`, merge the new material into the existing
   structure, bump `timestamp`, keep `created`. A repeat question produces a second
   question page and **one** note, never a second note.

If the answer implies an ingest-owned page is wrong, stale or missing something:
say so in your reply, add it to `open-questions.md` (Q.7), and change nothing else.

## Q.6 — Repo path

1. **Read `wiki/repos/<repo>/ARCHITECTURE.md` first.** It exists so nobody has to
   read the clone. If it answers the question, you are on the general path (Q.5) —
   the note lands in `wiki/notes/` and links out to the repo page.
2. Only if the answer needs code the architecture page does not cover, check that
   the clone exists at the `clone_path` in `ARCHITECTURE.md`'s frontmatter. Clones
   are regenerable and never committed, so a copied wiki arrives without one. **If
   it is missing, clone it yourself — never ask the user to:**

   ```bash
   uv run --script .agents/skills/my-llm-wiki/scripts/clone_repo.py \
     --url "<repo_url from ARCHITECTURE.md>" --wiki-dir wiki-<slug>
   ```

   If it already exists, use it as is — do not run the script (it would refresh
   the code under an ingest-owned page). Pass on the `commit_sha` from the receipt,
   or from the clone (`git -C <clone_path> rev-parse HEAD`). If it differs from the
   one in `ARCHITECTURE.md`, say so in the answer; you do not rewrite that page in
   query mode — suggest re-ingesting the repo.
   Then spawn `agents/repo_writer.md` with `mode: question`, passing `clone_path`,
   `commit_sha`, `branch`, the verbatim `question`, the `architecture_path`, and
   the `question_page` wikilink. It writes
   `wiki/repos/<repo>/<question-slug>.md` (`PAGES.md § repo_note`) and returns a
   receipt. If its receipt says `"answered_from_architecture": true`, it wrote
   nothing — fall back to Q.5.
3. A repo note is a **source-like page**, so it must go through the **ingest tail**
   (`CONVENTIONS.md` §8), exactly as an ingested source would:

   ```bash
   uv run --script .agents/skills/my-llm-wiki/scripts/count_mentions.py --wiki-dir wiki-<slug>
   ```

   → spawn one `page_writer` per qualifying slug the new note touched →
   `overview_writer` → `build_index_md.py`.
4. Then write the slim question page with `answer_doc` pointing at the repo note.

This is the only way query mode reaches an ingest-owned page: **through the tail,
never by hand.**

## Q.6b — Docs path

A docs set is a catalog the wiki has only partly read. Its hub knows what the
rest covers, so "the wiki does not know" can become "the wiki fetches it".

1. **Read `wiki/docs/<set>/OVERVIEW.md`.** If a page under its `## Ingested`
   answers the question, read that page — you are on the general path (Q.5).
2. Otherwise **let the selector pick**, with a small budget — this is a question,
   not an ingest. Spawn `agents/docs_selector.md` with `catalog_url` = the hub's
   `original_path`, `user_intent` = the question verbatim, and `budget: 3`. An
   empty `pick` means the docs do not cover it either: go to Q.7.
3. **Fetch and write**, exactly as ingest does:

   ```bash
   uv run --script .agents/skills/my-llm-wiki/scripts/fetch_llms_txt.py \
     --url "<catalog_url>" --wiki-dir wiki-<slug> --pick <ids>
   ```

   → one `agents/source_writer.md` per page with `action: fetched`, output at its
   `source_page`, `origin: llms-txt`.
4. **Run the ingest tail** (`CONVENTIONS.md` §8): `count_mentions.py` → one
   `page_writer` per qualifying slug the new pages touched → `docs_writer` for the
   set's `OVERVIEW.md` (its `## Ingested` list just grew) → `overview_writer` →
   `build_index_md.py`.
5. **Answer from the new pages**, then finish as Q.5: question page always, note
   only if earned. Name the fetched pages in the answer — the user should know
   the wiki just grew.

## Q.7 — Open questions

Append to `wiki/open-questions.md` (creating it with frontmatter on first use) when
either is true:

- the user flags one ("log this as open", "we should look into that"), or
- **the wiki cannot answer** — say that plainly first. An honest "the wiki doesn't
  cover this" is the most useful answer a knowledge base can give, because it is
  the only one that tells you what to ingest next.

The file is append-only and dated. Nothing resolves it automatically; the next
ingest reports which open questions its new sources appear to address, and a human
decides.

## Q.8 — Log and present

Append one entry to `log.md`:

```markdown
## <YYYY-MM-DD> query | <topic>

- question: "<verbatim, ≤200 chars>"
- pages used: <count> (<slugs>)
- saved: wiki/questions/<file> + <note or repo note>, or "question page only"
- fetched: <docs pages pulled in by Q.6b, or omit>
- tail: <pages updated by the ingest tail, or omit>
- open question logged: <one line, or omit>
```

Then answer the user:

```
## <question as a topic line>

<the answer, with [[wikilinks]] to every page it rests on>

Pages used: [[...]], [[...]]
Saved: wiki/questions/<file> · wiki/notes/<file>        (or: question page only)
```

Never present a saved note as if the user asked for it — one line is enough.

---

## What this layer is actually teaching

The wiki now has two ways to grow. **Ingestion** adds what other people wrote.
**Interaction** adds what you asked and what the wiki worked out in reply — and
because a repo note re-enters through the same tail as a source, that second path
compounds exactly like the first. The question log is the cheap part: it makes
"what have I already asked?" answerable without re-answering anything.
