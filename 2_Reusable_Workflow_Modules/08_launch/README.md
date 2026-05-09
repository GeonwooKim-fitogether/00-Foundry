# Module: launch

> Placeholder (v0.1.0).

## Purpose
Release the verified artifact to its intended audience with reversible steps where possible.

## Inputs
- Passed `NPI_Verification.md`.
- Launch plan (audience, channels, timing, rollback).

## Outputs
- Launch record (what was released, where, when).
- Rollback plan or evidence that one is unnecessary.

## Acceptance Criteria
- All AC items pass before release.
- Irreversible release steps require a Human Control Point.
- Rollback path is documented (or explicitly N/A with reason).

## Control Points
Start (release plan agreed) → Automated (release scripts / health checks) → Human (irreversible step) → Final (release confirmed).

## Checklist
- [ ] Verification fully passed
- [ ] Rollback path documented
- [ ] Stakeholders notified

## Anti-patterns
- Launching with open AC failures.
- No rollback plan for reversible launches.
