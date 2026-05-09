# Glossary

Vocabulary used across AI-NPI Factory v0.1.0.

| Term | Definition |
|---|---|
| **AI-NPI** | AI New Product Introduction — a new AI project brought up using this Factory. |
| **Factory** | This meta-platform: the 4-Layer skeleton + templates + manifest. |
| **4-Layer Frame** | L1 Principles → L2 Workflows → L3 Playbooks → L4 Templates. |
| **L1 / Universal Operating Principles** | Invariant rules applied to every project. |
| **L2 / Reusable Workflow Modules** | The 10 lifecycle modules (problem-framing → retrospective). |
| **L3 / Domain·Project Playbook** | A domain- or project-specific variant of L2 plus its ontology. |
| **L4 / Task-level Execution Template** | Per-artifact templates filled per task instance. |
| **ACDE** | Acceptance-Criteria-Driven Execution. No execution without measurable, verifiable criteria. |
| **Acceptance Criteria (AC)** | Measurable, verifiable conditions defining "done". Given-When-Then recommended for code/feature work. |
| **Control Point** | Defined moment where progress is checked. Four kinds: Start, Automated, Human, Final. |
| **Start Control Point** | Mandatory checkpoint at task start (purpose + AC agreed). |
| **Final Control Point** | Mandatory checkpoint at task end (AC met). |
| **Automated Control Point** | Default mid-task checkpoint executed by automation, not humans. |
| **Human Control Point** | Triggered only on a Critical Decision. |
| **Critical Decision** | (a) hard-to-reverse change, (b) meaningful scope/budget/schedule change, (c) risk-level upgrade, (d) Acceptance Criteria change. |
| **Ontology** | Lightweight markdown definition of a project's Core Objects, Relationships, Actions, Metrics, Risks, Context Sources. |
| **Object** | A first-class concept in the project's ontology. PascalCase. Examples: `Project`, `WorkflowModule`, `Artifact`, `ControlPoint`, `Metric`. |
| **Affected Objects** | The ontology objects impacted by a task. Required in `NPI_Brief.md`, optional per task in `NPI_Worklist.md`. |
| **Playbook** | A concrete L3 instance (e.g., `ai-npi-platform`) — variant of L2 + ontology. |
| **Manifest** | `factory.yaml`, the machine-readable index of layers, modules, templates, playbooks, and ontology. |
