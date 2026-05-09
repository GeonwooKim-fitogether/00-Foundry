# Command: plan-work

## Purpose
Produce a plan organized around **deliverables** and **Acceptance Criteria**, not steps-for-their-own-sake.

## When to Run
- After `scope-context` and before any execution.
- After a Critical Decision that changes AC.

## Inputs
- `NPI_Brief.md` (frozen AC + Affected Objects).
- Allowlist from `scope-context`.
- Findings from any research subagent runs.

## Procedure
1. For each AC item, identify the deliverable that satisfies it.
2. Group deliverables into the smallest set of tasks.
3. For each task, draft: AC covered, verification method (failing test / script / manual), Affected Objects (optional), reversibility note.
4. Identify any Critical Decisions baked into the plan and surface them now (don't defer).
5. Choose where each task runs: main agent vs. subagent vs. worktree.

## Output
- `NPI_Blueprint.md` (architecture/decisions) and/or
- `NPI_Worklist.md` (decomposed tasks with AC mapping).

## Acceptance Criteria
- Every Brief AC item maps to at least one task.
- Every task lists its verification method.
- Subagent / worktree allocation is explicit.

## Anti-patterns
- Plans that list activities ("research", "discuss") instead of deliverables.
- Hidden architecture decisions that surface only during execution.
- "Re-decide as we go" — the plan is the place to decide.
