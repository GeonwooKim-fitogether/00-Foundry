# Naming and Conventions (v0.1.0)

## Folders
- Layer folders are numbered: `1_Universal_Operating_Principles/`, `2_Reusable_Workflow_Modules/`, `3_Domain_Project_Playbooks/`, `4_Task_Level_Execution_Templates/`.
- L2 modules: `NN_<kebab-case>/` (e.g., `06_verification/`).
- L3 playbooks: `<kebab-case>/` (e.g., `ai-npi-platform/`).

## Files
- Markdown filenames: `kebab-case` or `snake_case` are both acceptable. Pick one per Playbook and stay consistent.
- Layer-level docs use a numeric prefix: `00_Overview.md`, `01_Decision_Principles.md`, etc.
- L4 templates use `NPI_*.md` (PascalCase suffix).

## Versioning
- Semver everywhere a version is declared.
- Factory version: `factory.yaml → factory.version`.
- Playbook version: inside the Playbook's `00_Project_Brief.md`.
- Pre-stable: `0.x.y`; stable: from `1.0.0`.

## Ontology Object Names
- **PascalCase**, no namespaces in v0.1.0.
- Examples: `Project`, `WorkflowModule`, `Artifact`, `ControlPoint`, `Metric`, `Risk`.
- Avoid abbreviations unless the abbreviation is universally known in the domain.

## Acceptance Criteria
- Measurable + verifiable (mandatory).
- Given-When-Then (recommended for code/feature work).
- IDs: `AC-1`, `AC-2`, … per Brief; `AC-P1`, `AC-P2`, … per Patchnote.

## Control Points
- Default: Start + Final (mandatory), Automated in between.
- Human Control Point: only on Critical Decision (see L1/01).

## Affected Objects
- Required field in `NPI_Brief.md` (structured list).
- Optional per task in `NPI_Worklist.md`.
- Object names must exist in the Playbook's `domain-ontology.md`.

## Required Modules
- `06_verification` is `required: true` in `factory.yaml`. Never skip.
