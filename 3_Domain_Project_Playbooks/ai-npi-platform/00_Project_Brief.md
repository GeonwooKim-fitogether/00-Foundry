# Project Brief — ai-npi-platform

- **Playbook version**: 0.1.0
- **Factory version**: 0.1.0
- **Status**: self-referential — this Playbook describes the AI-NPI Factory project itself.

## Identity
`ai-npi-platform` is the meta-project that builds and evolves the AI-NPI Factory. It is the first Playbook on the Factory and exists primarily to dogfood the 4-Layer Frame, ACDE doctrine, and Lightweight Ontology.

## Audience
- The author / operator (single-person, multi-project AI builder).
- Future AI agents collaborating on top of the Factory.
- Future projects bootstrapped from this Factory.

## In Scope (this Playbook, v0.1.0)
- Skeleton of the 4-Layer Frame.
- Self-referential ontology (`domain-ontology.md`).
- Validation that L4 templates are usable for this Playbook itself.

## Out of Scope (v0.1.0)
- Automation CLI, agents, or runtime code.
- Second domain instance.
- Vendor-specific implementations.

## Acceptance Criteria (Playbook-level, v0.1.0)
- All 4 layer folders, the manifest, and the ontology files exist and are internally consistent.
- This Playbook's `domain-ontology.md` declares the Factory's own Core Objects.
- A new project could be bootstrapped from `Bootstrap/How_To_Start_New_Project.md` using only the v0.1.0 artifacts.

## Affected Objects
- `Project`
- `Layer`
- `WorkflowModule`
- `Playbook`
- `Template`
- `Artifact`
- `ControlPoint`
- `AcceptanceCriterion`
- `Ontology`
- `Object`
- `Metric`
- `Risk`
