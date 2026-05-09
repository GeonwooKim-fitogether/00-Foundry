# L3 — Domain/Project Playbooks (Overview)

A **Playbook** is a project- or domain-specific variant of the L2 modules plus its own ontology.

## Folders
- `_template/` — empty playbook skeleton; copy this when starting a new project.
- `ai-npi-platform/` — the first concrete instance: this Factory project itself (self-referential).

## Minimum Contents of a Playbook
1. `00_Project_Brief.md` — short identity & scope.
2. `domain-ontology.md` — required, follows the 7-section ontology template.
3. (Optional) Module overrides (e.g., `05_implementation.md`) where the project varies from the L2 default.
4. L4 instances live alongside (e.g., `npi-briefs/`, `npi-blueprints/`) per project preference.

## Versioning
Each Playbook declares its own Semver version inside `00_Project_Brief.md`. The Factory version is independent.
