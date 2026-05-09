# Module: implementation

> Placeholder (v0.1.0).

## Purpose
Execute the Blueprint to satisfy the AC. Code-bearing work writes a failing test or automated verification first.

## Inputs
- Approved `NPI_Blueprint.md`.
- `NPI_Worklist.md` (decomposed tasks).

## Outputs
- Working artifacts (code, content, configs) at declared paths.
- `NPI_BuildLog.md` recording what changed and why.

## Acceptance Criteria
- For code/feature work: a failing test or automated verification existed **before** implementation.
- Changes are within declared scope; out-of-scope discoveries are filed as new items, not absorbed.
- BuildLog entries reference the specific AC items they advance.

## Control Points
Start (Worklist accepted) → Automated (CI / scripts / linters / unit tests) → Human if Critical → Final (all in-scope tasks closed).

## Checklist
- [ ] Failing test / verification first (where applicable)
- [ ] Scope discipline maintained
- [ ] Reversibility considered

## Anti-patterns
- "While I'm here" refactors mid-task.
- Skipping tests because the change is small.
- Hidden architectural decisions made during implementation.
