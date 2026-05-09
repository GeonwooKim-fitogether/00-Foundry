# 01 — Decision Principles

## Principle 1. Minimum Human Intervention
Humans are not asked to review every intermediate step. The default is:
- **Start Control Point** (mandatory): purpose and Acceptance Criteria are agreed.
- **Automated Control Point** (default for mid-task): tests, scripts, checklists run without human review.
- **Human Control Point** (exception): triggered only on a Critical Decision.
- **Final Control Point** (mandatory): Acceptance Criteria are verified met.

## Principle 2. Critical Decisions
A Human Control Point is triggered if and only if one of these occurs:
1. **Irreversible change** (data loss, public release, contract).
2. **Meaningful scope / budget / schedule change.**
3. **Risk-level upgrade** (a known risk crosses a higher tier, or a new high risk appears).
4. **Acceptance Criteria change.**

Outside these four, proceed under Automated Control.

## Principle 3. Decision Traceability
Every decision is recorded where it lives:
- Strategic decisions → in the relevant L3 Playbook.
- Task-level decisions → in `NPI_Blueprint.md` or `NPI_BuildLog.md`.
- Changes to acceptance criteria → in `NPI_Brief.md` history.

## Principle 4. Reversibility-First Thinking
Prefer reversible actions. If an action is irreversible, escalate to a Human Control Point even if no other criterion is met.
