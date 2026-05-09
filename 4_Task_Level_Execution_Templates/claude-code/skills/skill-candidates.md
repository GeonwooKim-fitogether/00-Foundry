# Skill Candidates (v0.1.0 base — v0.2.0 부분 implemented)

| Skill | Status | Trigger | Primary Output | Package |
|---|---|---|---|---|
| `ai-npi-project-bootstrap` | candidate | "start a new project" / new Playbook needed | Filled Playbook scaffold + initial `NPI_Brief.md` | — |
| `context-scope-reviewer` | candidate | Before reading more files / before scope creep | READ / DO-NOT-READ list (see `scope-context.md`) | — |
| `acceptance-criteria-writer` | candidate | Drafting AC for code/feature work | AC list (Given-When-Then where applicable) with measurability checks | — |
| `architecture-planner` | candidate | Producing or revising a Blueprint | `NPI_Blueprint.md` with AC↔component coverage | — |
| **`verification-runner`** | **implemented (v0.2.0, 2026-05-08)** | `validate-output` invoked / Final Control Point 직전 / 사용자 명시 요청 | §4 표준 페이로드(RESULT/EXIT/COUNTS/ARTIFACT/SCHEMA/FAILED/WARNINGS/NEXT) + `NPI_Verification.md` (runner 가 생성) | `verification-runner/SKILL.md`, runner: `verification-runner/run.py` |
| `risk-reviewer` | candidate | Pre-launch / mid-task risk sweep | Ranked risk list tied to ontology Object Risks | — |
| `lesson-extractor` | candidate | Task close / hotfix close | keep / change / drop list with concrete edit targets | — |

## Notes
- Each candidate is a single, scoped task — not a multi-purpose toolkit.
- Several candidates correspond 1:1 with subagent roles. That's intentional: the skill is the "what to do" package; the subagent is the runtime container.
- v0.2.0 — `verification-runner` 가 첫 implemented skill. SKILL.md 의 11개 섹션(Purpose / When / Inputs / Outputs / Procedure / Context / Subagent / Invocation / Failure / Anti-patterns / History) 이 사실상의 v0.2.0 SKILL.md schema 가 된다. 이후 다른 candidate 가 implemented 로 격상될 때 동일 11개 섹션 골격을 따른다.

## Out of Scope (v0.1.0)
- Skill scripts.
- Automated trigger detection.
- Distribution / packaging.
