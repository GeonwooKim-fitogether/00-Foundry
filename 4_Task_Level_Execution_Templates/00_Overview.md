# L4 — Task-level Execution Templates (Overview)

Factory-native templates. Instantiate per task; do not edit the template files for project-specific work.

| Template | Role | Required Sections |
|---|---|---|
| `NPI_Brief.md` | Identity, problem, scope, AC | Acceptance Criteria, Affected Objects |
| `NPI_Blueprint.md` | How it will be built (architecture/plan) | — |
| `NPI_Worklist.md` | Decomposed tasks | Affected Objects per task is *optional* |
| `NPI_BuildLog.md` | What was actually done and why | — |
| `NPI_Verification.md` | Evidence that AC are met | AC ↔ Verification mapping |
| `NPI_Patchnote.md` | Hotfix/patch record | — |
| `Director_Card_Template.md` | Director-only self-execute card (HCP, migration, etc.) | 4약속 + 조건 A/B/C/D (v1.1) + WHY/PREQ/명령/PASS/FAIL/금지 |
| `Next_Cycle_Selection_Rule.md` | Implementer 자율 default 의 cycle 선택 표준 (D-025) | 우선순위 휴리스틱 5단계 + HCP gate 분리 |

## Conventions
- AC must be measurable and verifiable. Given-When-Then recommended for code/feature work.
- `Affected Objects` references entries in the Playbook's `domain-ontology.md` (PascalCase).
- Pre-state AC; later changes go through Critical Decision (Human Control Point).
