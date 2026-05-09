# Module: requirements

> Placeholder (v0.1.0). This module is the home of Acceptance-Criteria authoring discipline.

## Purpose
Turn the framed problem into requirements with **measurable, verifiable Acceptance Criteria** before any execution.

## Inputs
- `NPI_Brief.md` (Problem, Affected Objects, scope).
- Findings from `02_research`.

## Outputs
- AC-bearing sections in `NPI_Brief.md` and (if scoped) in `NPI_Worklist.md`.

## Acceptance Criteria Authoring Standard
- **Mandatory property**: each AC is measurable and verifiable.
- **Recommended form for code/feature work**: Given-When-Then.
  > Given <state>, When <action>, Then <observable result>.
- **Allowed alternatives**: yes/no checkable conditions, numeric thresholds, presence/absence checks.
- AC is **pre-stated** — written before execution; later changes go through Critical Decision.

## Acceptance Criteria (for this module itself)
- Every requirement has at least one AC item.
- No AC item is "TBD".
- AC items reference the relevant Object(s) where useful.

## Control Points
Start (scope of requirements agreed) → Automated (AC linter/checklist) → Human if Critical → Final (AC frozen for this iteration).

## Checklist
- [ ] AC measurable
- [ ] AC verifiable
- [ ] AC pre-stated
- [ ] Affected Objects linked

## Anti-patterns
- "We'll know it when we see it."
- AC stated as design choices instead of observable outcomes.
