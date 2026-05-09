# Module: <module-name>

> Standard structure for every L2 Reusable Workflow Module. Copy this file into each `NN_<module-name>/README.md` and fill in.

## Purpose
What this module exists for, in one or two sentences.

## Inputs
- Required artifacts, decisions, or signals consumed by this module.

## Outputs
- Artifacts produced. State the file path / template used (usually an L4 template).

## Acceptance Criteria
Measurable, verifiable conditions for "this module is done".
- Code/feature work: prefer Given-When-Then.
- Other work: state as yes/no checkable conditions.

## Control Points
Following the Minimum Human Intervention principle.

| Point | When | Who |
|---|---|---|
| **Start** | Module begins | Human (purpose & AC agreed) |
| **Automated** | Mid-module checkpoints | Automation (tests, scripts, checklists) |
| **Human (if Critical)** | Critical Decision occurs | Human (irreversible / scope / risk-up / AC change) |
| **Final** | Module ends | Human (AC verified met) |

## Checklist
- [ ] AC stated before work began
- [ ] Automated checks defined
- [ ] Affected Objects identified (from project ontology)
- [ ] Outputs stored at declared paths
- [ ] Final Control Point passed

## Anti-patterns
- Starting without Acceptance Criteria.
- Inventing new criteria after the fact.
- Treating every mid-step as a Human Control Point.
- Skipping verification because the change "feels small".
