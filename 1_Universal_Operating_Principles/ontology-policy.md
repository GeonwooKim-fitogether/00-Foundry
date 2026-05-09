# Ontology Policy

## Purpose
A project's **Ontology** declares the few core concepts the project treats as first-class. It exists to:
- Help Claude Code (and humans) understand what the project is about.
- Track which Objects each task affects.
- Make context selection more accurate.
- Separate project-specific knowledge from reusable workflow.
- Provide a shared vocabulary for future Agent-to-Agent collaboration.

## Form (v0.1.0)
- Markdown only. No DB, no graph store, no automated validation.
- One file per project: `domain-ontology.md` inside that project's L3 Playbook folder.
- Standard 7-section structure (see template).

## Object Naming
- **Objects use PascalCase**: `Project`, `WorkflowModule`, `Artifact`, `ControlPoint`, `Metric`, `Risk`.
- Field/file names may use `kebab-case` or `snake_case` — but ontology Object identifiers are PascalCase.
- **No namespaces in v0.1.0.** A bare `User` is fine; `aiNpiPlatform.User` is not.

## Required Sections of `domain-ontology.md`
1. **Core Objects** — the short list (5–15 typically).
2. **Object Definitions** — one paragraph per Object.
3. **Object Relationships** — how Objects relate (e.g., "WorkflowModule produces Artifact").
4. **Object Actions** — verbs each Object supports.
5. **Object Metrics** — how each Object is measured.
6. **Object Risks** — failure modes per Object.
7. **Context Sources by Object** — where in the repo (or external) each Object's context lives.

## How Ontology Connects to L4
- `NPI_Brief.md` **must** include an `Affected Objects` field (structured list of Object names).
- `NPI_Worklist.md` **may** include `Affected Objects` per task.
- `NPI_Verification.md` may map AC items to the Objects they touch.

## What Ontology is NOT (v0.1.0)
- Not a graph database.
- Not auto-validated by tooling.
- Not a domain model implementation. It is a *shared vocabulary*.
