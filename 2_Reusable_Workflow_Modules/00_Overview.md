# L2 — Reusable Workflow Modules (Overview)

The 10 modules below cover a typical NPI lifecycle. They are **reusable** (shared across projects) and **reorderable** (a Playbook may skip, repeat, or reorder them — except `06_verification`, which is required).

## Modules
| # | Module | Required |
|---|---|---|
| 01 | problem-framing | no |
| 02 | research | no |
| 03 | requirements | no |
| 04 | architecture-planning | no |
| 05 | implementation | no |
| 06 | verification | **yes** |
| 07 | risk-review | no |
| 08 | launch | no |
| 09 | metrics-review | no |
| 10 | retrospective | no |

## Standard Module Structure
Every module README follows `_module_template.md`:
- Purpose
- Inputs
- Outputs
- Acceptance Criteria
- Control Points (Start / Automated / Human-if-Critical / Final)
- Checklist
- Anti-patterns

## v0.1.0 Status
Each module folder contains a `README.md` placeholder using the standard structure. Bodies will be filled in subsequent versions.
