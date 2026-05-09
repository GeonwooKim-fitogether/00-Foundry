# Module: verification  *(required for every project)*

> Placeholder (v0.1.0). `factory.yaml → modules[id=06].required = true`.

## Purpose
Confirm that the declared Acceptance Criteria are met — by evidence, not assertion.

## Inputs
- Frozen AC from `03_requirements`.
- Implementation artifacts and `NPI_BuildLog.md`.

## Outputs
- `NPI_Verification.md` containing the **AC ↔ Verification mapping table**:

  | AC ID | Acceptance Criterion | Verification Method | Result | Evidence |
  |---|---|---|---|---|

## Acceptance Criteria (for this module)
- Every AC item has a row in the mapping table.
- Every "Pass" row has evidence (log, screenshot, output, test ID).
- Any "Fail" row blocks Final Control Point.

## Control Points
Start (AC list locked) → Automated (test suites, scripts) → Human if Critical → Final (all AC items pass or are explicitly waived under scope-change rules).

## Checklist
- [ ] AC ↔ Verification table complete
- [ ] Evidence linked
- [ ] No silently waived AC

## Anti-patterns
- "Looks good" without evidence.
- Verification authored by the same automation that produced the artifact, with no independent check.
- Skipping or merging this module into another.
