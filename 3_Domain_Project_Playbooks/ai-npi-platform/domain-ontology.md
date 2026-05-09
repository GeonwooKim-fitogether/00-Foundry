# Domain Ontology — ai-npi-platform

Self-referential ontology: the AI-NPI Factory described in its own terms.

## 1. Core Objects
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

## 2. Object Definitions

### `Project`
A concrete AI-NPI being built on the Factory. Has a Playbook, a version, a scope, and Acceptance Criteria. Not a synonym for "task".

### `Layer`
One of the four tiers in the 4-Layer Frame: Universal Operating Principles, Reusable Workflow Modules, Domain/Project Playbooks, Task-level Execution Templates.

### `WorkflowModule`
A reusable lifecycle stage at L2 (e.g., `requirements`, `verification`). Has a standard structure (Purpose / Inputs / Outputs / AC / Control Points / Checklist / Anti-patterns).

### `Playbook`
An L3 instance. A project-specific variant of L2 plus its own ontology.

### `Template`
An L4 file (e.g., `NPI_Brief.md`) that gets instantiated per task.

### `Artifact`
A produced deliverable (filled template, code, doc, report). Lives at a declared path.

### `ControlPoint`
A defined moment of progress check. Kinds: Start, Automated, Human, Final. Human only on Critical Decision.

### `AcceptanceCriterion`
A measurable, verifiable condition. Pre-stated. Authoring lives in `03_requirements`.

### `Ontology`
A project's lightweight markdown declaration of its first-class concepts. One per Playbook.

### `Object`
An entity in an Ontology. PascalCase. No namespace in v0.1.0.

### `Metric`
A quantity used to measure an Object's health or progress.

### `Risk`
A failure mode of an Object, with likelihood, impact, owner, mitigation, and trigger.

## 3. Object Relationships
- `Project` *uses* `Playbook`
- `Playbook` *variants* `WorkflowModule`s
- `Playbook` *owns* exactly one `Ontology`
- `Ontology` *contains* `Object`s, `Metric`s, `Risk`s
- `WorkflowModule` *produces* `Artifact`s via `Template`s
- `Artifact` *satisfies* `AcceptanceCriterion`s
- `WorkflowModule` *bounded by* `ControlPoint`s
- `Project` *governed by* `Layer` 1 principles

## 4. Object Actions
- `Project`: bootstrap, version, archive
- `Playbook`: create, override-module, version
- `WorkflowModule`: enter, run-checks, exit
- `Template`: instantiate, fill, freeze
- `Artifact`: produce, verify, publish
- `ControlPoint`: trigger, pass, escalate
- `AcceptanceCriterion`: state, freeze, change-via-Critical-Decision
- `Ontology` / `Object`: declare, update, retire
- `Metric`: declare, observe, breach
- `Risk`: register, upgrade, mitigate, retire

## 5. Object Metrics
- `Project`: AC pass rate, time from Start to Final Control Point.
- `Playbook`: count of module overrides; staleness vs. Factory version.
- `WorkflowModule`: required-module presence (`06_verification` ≡ true).
- `Template`: required-section completeness rate across instances.
- `Artifact`: AC ↔ verification mapping completeness.
- `ControlPoint`: count of Human Control Points (lower is better, given Critical-only policy).
- `AcceptanceCriterion`: % measurable+verifiable; % pre-stated.
- `Ontology`: % of Affected Objects in Briefs that exist in the Ontology.
- `Metric`: % declared metrics with current value.
- `Risk`: % High risks with owner+mitigation.

## 6. Object Risks
- `Project`: drift between declared scope and actual work.
- `Playbook`: silent divergence from L2 without override docs.
- `WorkflowModule`: skipped despite being required (`06_verification`).
- `Template`: required sections missing.
- `Artifact`: produced without AC, or with AC invented after the fact.
- `ControlPoint`: humans pulled into non-Critical mid-steps; or a Critical step run as Automated.
- `AcceptanceCriterion`: vague, unmeasurable, or post-hoc.
- `Ontology`: stale / decorative; no link from Briefs.
- `Object`: name collisions or inconsistent casing.
- `Metric`: declared but never observed.
- `Risk`: registered without owner, mitigation, or trigger.

## 7. Context Sources by Object
- `Project`: `3_Domain_Project_Playbooks/<project>/00_Project_Brief.md`, `factory.yaml`
- `Layer`: `factory.yaml → layers[]`, `MANIFEST.md`
- `WorkflowModule`: `2_Reusable_Workflow_Modules/<NN>_<name>/`
- `Playbook`: `3_Domain_Project_Playbooks/<project>/`
- `Template`: `4_Task_Level_Execution_Templates/`
- `Artifact`: declared output paths inside each Playbook / Project repo
- `ControlPoint`: `1_Universal_Operating_Principles/01_Decision_Principles.md`
- `AcceptanceCriterion`: `1_Universal_Operating_Principles/02_Quality_and_Safety.md`, `2_Reusable_Workflow_Modules/03_requirements/`
- `Ontology` / `Object`: `1_Universal_Operating_Principles/ontology-policy.md`, each Playbook's `domain-ontology.md`
- `Metric`: each Playbook's `domain-ontology.md` §5; `2_Reusable_Workflow_Modules/09_metrics-review/`
- `Risk`: each Playbook's `domain-ontology.md` §6; `2_Reusable_Workflow_Modules/07_risk-review/`
