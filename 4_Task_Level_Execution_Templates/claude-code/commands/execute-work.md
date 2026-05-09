# Command: execute-work

## Purpose
Carry out the approved plan under Automated Control. Escalate to Human Control Point only on Critical Decisions.

## When to Run
- After `plan-work` produces an approved Blueprint/Worklist.
- After Start Control Point passes.

## Inputs
- Approved `NPI_Blueprint.md` and/or `NPI_Worklist.md`.
- Frozen AC.
- Worktree allocation (if any).

## Procedure
1. For each task: write the failing test / verification script first (code/feature work).
2. Make the smallest change that turns the test green.
3. Record each step in `NPI_BuildLog.md` with: AC advanced, what changed, why, evidence.
4. Stop and trigger `review-risk` if any Critical Decision condition appears.
5. Stay inside scope. File out-of-scope discoveries as new Worklist items, not silent absorption.
6. Never mark an AC met without evidence.

## Output
- Working artifacts at declared paths.
- Updated `NPI_BuildLog.md`.

## Acceptance Criteria
- Every BuildLog entry references the AC item it advances.
- No silent scope expansion.
- All Critical Decisions logged in the BuildLog's Critical Decisions section.

## Anti-patterns
- "While I'm here" refactors.
- Skipping the failing test because the change feels small.
- Mid-execution architectural decisions made without going back to `plan-work`.
