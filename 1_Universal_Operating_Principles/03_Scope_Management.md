# 03 — Scope Management

## Scope is Declared, Not Inferred
Every project declares **In Scope** and **Out of Scope** in its `NPI_Brief.md`. If something is not declared, the default is Out of Scope.

## Meaningful Scope Change (triggers Human Control Point)
A scope change is *meaningful* if any of the following hold:
- It alters or adds a top-level deliverable.
- It changes Acceptance Criteria.
- It moves a deadline or expands resource needs noticeably.
- It promotes a previously Out-of-Scope item to In Scope.

Cosmetic clarifications (wording, ordering, splitting one task into two) are **not** meaningful changes and proceed under Automated Control.

## Scope Drift Discipline
- "While I'm here" refactors are forbidden mid-task.
- Discoveries that suggest new work are recorded as new items in `NPI_Worklist.md` or as a new `NPI_Brief.md`, not silently absorbed.

## Out-of-Scope Surface
Each Brief lists Out of Scope explicitly. This list is the canonical answer to "should we also do X?" — if X is on it, the answer is no until scope is formally changed.
