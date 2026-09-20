# Status / where we are

Running handoff note — read this at the start of a new session to pick up where the
last one left off. Update it as things change; delete sections once they're resolved
and folded into the real docs (`plan/`, project READMEs, CLAUDE.md).

## Done so far

- **A-sleep-stage-classification, Phase 0**: data downloaded (10 subjects, both
  nights, via `server/data/download.py`), `.venv` fixed after a directory rename,
  `notebooks/01_explore_sleepedf.ipynb` built and executed — channels/sampling rate
  verified, `?`/Movement epochs confirmed dropped, R&K stages 3+4 merged into AASM N3,
  841 aligned 30s epochs built, hypnogram plotted. Phase 0's definition of done is met.
- **neurofolio/**: a zero-dependency static hub (`index.html` + `tracks.json` +
  `serve.py`) listing all 4 tracks/17 projects, linking out to each track's own
  showcase server as it comes online (only track 01's is live).
- **CLAUDE.md** (repo root): documents the Obsidian notes path
  (`.../Studies/Neuroscience/Mini Neurotech projects notes`), the "only write when
  asked" rule, "never overwrite the user's own writing," and the AI-tagging
  convention (`> [!ai] AI notes` callout / `*(AI)*` inline).
- Anki: `Neuroscience Space::Neuroglass` deck split into `Neuroscience Space::Neuroglancer`
  (CATMAID/tracing-specific, 15 cards) and `Neuroscience Space::Fundamentals of
  Neuroscience` (neuron anatomy, 7 cards) via AnkiConnect.
- Investigated `github.com/deeplethe/utopia` — an enterprise knowledge-graph/RAG
  system, unrelated to this repo. Not pursued further.

## Open decision — not yet made

**Should B, C, D, E (and tracks 02-04) get A-style `plan/` folders (phased build,
dataset research, model landscape), or stay as flat single-README milestone lists?**
A is currently the only project with a `plan/` folder — this was intentional (A is
the starter/pipeline project) but nobody's decided what happens once you actually
start B. Options discussed: (1) keep A unique, write each project's `plan/` only when
you're about to start it, informed by lessons from building A — leaning this way but
not confirmed; (2) add a lightweight "study backlog" section to each README now,
without a full phase plan; (3) write full phase plans for all of B-E now, before any
code. **Revisit when B is about to start.**

## Study priorities (sleep staging, A) — Now vs. Backlog

Principle (already stated in A's own `plan/00-overview.md`): read a paper/course/
resource only when its phase is directly in front of you, not upfront.

**Now** (before Phase 1 / EDA):
1. Carskadon & Dement, *"Normal Human Sleep: An Overview"* — one chapter.
2. The AASM-vs-R&K scoring distinction specifically (why stages 3+4 merge into N3;
   how REM is scored via EEG+EOG+EMG together) — not the full manual.
3. MNE's own Sleep-EDF tutorial (`60_sleep.html`) — skim once fully.

**Backlog** (read only when its phase/project arrives):

| Item | Unlocked by |
|---|---|
| Full AASM manual, Kryger textbook | Ongoing reference, look up as needed |
| MIT OCW "Brain Structure and its Origins" | General background, no dependency — slow side course |
| HST.582 (Biomedical Signal Processing, MIT OCW) | A's Phase 3 (classical features) |
| Micro-architecture (spindles, K-complexes) | A's Phase 3, optional depth |
| Macro-architecture metrics, two-process model, age effects | A's Phase 1 (EDA) / Phase 7 (error analysis) |
| YASA | A's Phase 3 (benchmark once you have your own numbers) |
| Braindecode | A's Phase 4, or B (already in B's README) |
| PyRiemann | Project B (motor imagery) — not yet in B's README, should be added |
| imbalanced-learn, SHAP | A's Phase 3 |
| nilearn | Project D — already in D's README |
| autoreject | Project E, or cleaning B/C's noisier recordings |
| Cross-subject BCI transfer / calibration-free BCI | Project B, and A's Phase 9 — not yet in B's README, should be added |
| fMRI/EEG-to-image decoding | Project D+, furthest-out "someday" item |

Most of the right column above is **not yet written into the actual project
READMEs** (checked B, C, D, E — only Braindecode and nilearn are currently
referenced). Worth doing once the plan-structure decision above is made.

## FocusAnalyze MCP

Was disconnected (stale/revoked token). Removed and re-added via `claude mcp remove
focusanalyze -s user` + `claude mcp add --transport http focusanalyze
https://mind.focusanalyze.com/api/focusgpt/mcp/ --header "Authorization: Bearer
<new token>" -s user`, confirmed connected via `claude mcp list`. **The session that
made this change was still holding the old dead connection in memory** — a new
session should pick up the working connection automatically.

### Instruction to paste in a new chat

> Read `STATUS.md` at the repo root first. Confirm FocusAnalyze MCP tools are now
> available (try `focusanalyze_get_context`). If connected, create/update a task
> there for the study-priorities backlog and the open plan-structure decision above,
> per the FocusAnalyze usage notes in this repo's `~/.claude/CLAUDE.md` (use
> `mcp_upsert_task_doc_tool` for a running notes/plan doc, not
> `mcp_create_task_comment_tool`, and resolve which existing task this belongs to
> with `search_tasks_tool` first — ask me which task if it's not obvious).
