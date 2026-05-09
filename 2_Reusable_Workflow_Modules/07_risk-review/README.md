# Module: risk-review

> Placeholder (v0.1.0).

## Purpose
Make risks explicit, ranked, and assigned. A risk-level upgrade is a Critical Decision (Human Control Point).

## Inputs
- Blueprint, Worklist, Verification status.
- Object Risks from project ontology.

## Outputs
- Risk register entries (likelihood × impact, owner, mitigation, trigger).
- Updates to the Brief if risks change scope or AC.

## Acceptance Criteria
- Every High risk has an owner and a mitigation.
- Newly upgraded risks trigger a Human Control Point per L1/01.

## Control Points
Start (review scope agreed) → Automated (register completeness check) → Human if Critical → Final (register accepted).

## Checklist
- [ ] Risks tied to Objects
- [ ] Owners assigned
- [ ] Mitigations testable

## Anti-patterns
- Long unprioritized risk lists.
- Risks without owners or triggers.
