# 02 — Quality and Safety

## Acceptance-Criteria-Driven Execution (ACDE)

**Rule.** No execution without measurable, verifiable acceptance criteria.

### Application by Work Type
| Work Type | Required Form |
|---|---|
| Code / feature | Failing test or automated verification script written **first**. Given-When-Then is the recommended AC format. |
| Document / spec | AC stated as measurable conditions ("contains section X", "answers questions Y and Z", "passes review checklist"). |
| Research | AC stated as a question to be answered or a decision to be unblocked, with the standard of evidence required. |
| Planning | AC stated as the artifacts to be produced and the criteria they must meet. |

### AC Quality Bar
- **Measurable** — there is an unambiguous yes/no test.
- **Verifiable** — someone (or something) other than the author can confirm it.
- **Pre-stated** — AC is written before work starts and changes only via Critical Decision.

## Verification is Not Optional
The `06_verification` workflow module is **required** for every project (`required: true` in `factory.yaml`). It cannot be skipped or merged into other modules.

## Safety Guardrails (universal)
- **Reversibility** preferred (see L1/01).
- **Data safety**: destructive operations require Human Control Point.
- **Boundary discipline**: do not expand scope to "fix surrounding issues" without going through scope-change procedure.
- **Truthful reporting**: never mark AC as met if any AC item is unverified; explicitly say so.

## Anti-patterns
- "We'll figure out acceptance later."
- "It works on my machine" as a substitute for AC.
- Replacing AC with a vague checklist after the fact.
- Skipping verification because "the change is small."
