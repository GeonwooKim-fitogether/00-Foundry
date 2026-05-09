# Module: architecture-planning

> Placeholder (v0.1.0).

## Purpose
Choose how to build it. Produce a Blueprint that an executor can follow without re-deciding architecture.

## Inputs
- Frozen AC from `03_requirements`.
- Affected Objects + project ontology.

## Outputs
- `NPI_Blueprint.md` (components, interfaces, data flow, key trade-offs).
- Optional: ADR-style notes for non-obvious choices.

## Acceptance Criteria
- Blueprint covers every AC item from the Brief.
- Each major decision has a one-line rationale.
- Reuse over invention is explicitly considered.

## Control Points
Start (Brief AC frozen) → Automated (coverage check: AC ↔ Blueprint) → Human if Critical → Final (Blueprint approved).

## Checklist
- [ ] Each AC traced to a Blueprint section
- [ ] Reuse opportunities listed
- [ ] Risks flagged for `07_risk-review`

## Anti-patterns
- Over-architecting beyond AC.
- Architectural decisions buried in implementation.
