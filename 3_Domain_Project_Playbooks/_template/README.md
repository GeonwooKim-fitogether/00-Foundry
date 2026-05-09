# Playbook Template

Copy this folder to start a new Playbook (e.g., `3_Domain_Project_Playbooks/<your-project>/`).

## Required Files
- `00_Project_Brief.md` — short identity, audience, scope, version.
- `domain-ontology.md` — Core Objects, Relationships, Actions, Metrics, Risks, Context Sources.

## Optional Files
- `<NN>_<module>.md` — overrides of L2 modules where the project varies from the default.

## Conventions
- Object names: PascalCase, no namespaces (v0.1.0).
- Files/sections: kebab-case or snake_case is fine.
- Each Playbook declares its own Semver version inside `00_Project_Brief.md`.

## What Not to Put Here
- Implementation code (use the project's source tree).
- Generic principles (those live in L1).
- Generic workflow definitions (those live in L2).
