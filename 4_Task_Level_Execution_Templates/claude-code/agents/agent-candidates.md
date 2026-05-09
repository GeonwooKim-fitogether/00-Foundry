# Agent Candidates (v0.1.0)

These are roles, not implementations. v0.1.0 documents the briefs; concrete subagent definitions land later.

## Main Agent — `factory-foreman`
- **Role**: orchestrator. Holds plan, runs commands, integrates subagent results, decides Critical Decisions.
- **Owns**: `NPI_Brief.md`, `NPI_Blueprint.md`, `NPI_Worklist.md`, `NPI_BuildLog.md`, Final Control Point.
- **Does not**: read every file in the repo on its own; delegate that to subagents.

## Subagent Candidates

### `context-scout`
- **Use for**: "Where is X defined / referenced?", "Which files implement Y?", "Map the surface area of Z."
- **Input**: question + restricted path globs.
- **Output**: file:line citations + 1-paragraph map. No raw transcripts.

### `risk-reviewer`
- **Use for**: scanning a Blueprint or BuildLog for risks against the project's `domain-ontology.md` (Object Risks).
- **Input**: Blueprint/BuildLog + ontology Risks section.
- **Output**: ranked risk list (likelihood × impact) with owners suggested.

### `test-failure-analyst`
- **Use for**: ingesting long failing-test logs and producing a single root-cause hypothesis.
- **Input**: failing test output + relevant source paths.
- **Output**: 1-paragraph hypothesis + minimal repro suggestion.

### `parallel-options-evaluator`
- **Use for**: comparing N independent design options against the same AC.
- **Input**: AC list + options (A/B/C).
- **Output**: scored table + recommendation with reasoning ≤ 200 words.

### `research-digester`
- **Use for**: external research where many sources must be read but only conclusions matter.
- **Input**: question + source list / search query.
- **Output**: claim → evidence → confidence → source rows.

### `verification-runner`
- **Use for**: executing `06_verification` against a frozen AC list and producing the AC ↔ Verification table.
- **Input**: AC list + paths to test scripts / commands.
- **Output**: filled `NPI_Verification.md` mapping table + Pass/Fail summary.

### `lesson-extractor`
- **Use for**: post-task retrospective input.
- **Input**: BuildLog + Verification + Risk register.
- **Output**: keep / change / drop list, each pointing to a specific Factory file to edit.

## When NOT to Spawn a Subagent
- The task fits in <50 lines of context.
- Only one file is involved.
- The work is purely conversational.
- You'd just be passing the same context through.

## Mapping to Commands
| Subagent | Likely Command |
|---|---|
| `context-scout` | `scope-context` |
| `risk-reviewer` | `review-risk` |
| `verification-runner` | `validate-output` |
| `research-digester` | `plan-work` (research phase) |
| `lesson-extractor` | `extract-lessons` |
