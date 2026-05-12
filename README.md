# AI-NPI Factory

Reusable meta-platform for starting and running AI New Product Introduction (NPI) projects on a shared 4-Layer skeleton.

- **Version**: **0.2.1 (frozen)** — elevated from candidate on 2026-05-12.
- **Status**: 0.2.1 frozen — Phase 1+2 field validation by `12.subscription-payment-saas-platform` (Phase 1 closure `3b8bc60` / Phase 2 closure `9b2967a` / D-001~D-014 + FIL-001~008). Revalidation: B-002 self-test 6/6 PASS · B-003 self-test 9/9 PASS (2026-05-12). 정책/문서 add only — Frame/runner/hook/skill 코드 변경 0.
  v0.2.1 핵심: GitHub 기반 Foundry 관리 + 신규 프로젝트 / meta 폴더 / Non-Blocking Execution / Human Control Point / Decision Queue / Meta Sprint / Copy-Paste Zero 로드맵 정책 + Phase 1+2 운영 데이터 누적 (backport candidates: `Bootstrap/v0.2.1_Frozen_Elevation_Evidence.md`).

> Note: This folder previously hosted the "Foundry" meta-improvement notes (`PRD.md`, `Backlog.md`, `STATUS.md`, `Reading_List.md`). Those are retained as legacy inputs. The AI-NPI Factory structure below is the new authoritative skeleton.

## 4-Layer Frame

| Layer | Folder | Role |
|---|---|---|
| L1. Universal Operating Principles | `1_Universal_Operating_Principles/` | Invariant principles for every project |
| L2. Reusable Workflow Modules | `2_Reusable_Workflow_Modules/` | 10 lifecycle modules (placeholders in v0.1.0) |
| L3. Domain/Project Playbooks | `3_Domain_Project_Playbooks/` | Domain variants of L2; first instance: `ai-npi-platform` |
| L4. Task-level Execution Templates | `4_Task_Level_Execution_Templates/` | Per-task artifact templates |

## Core Doctrines

1. **Acceptance-Criteria-Driven Execution (ACDE)** — no execution without measurable, verifiable criteria.
2. **Minimum Human Intervention** — Start & Final Control Points by default; Automated in between; Human only on Critical Decisions.
3. **Lightweight Ontology** — each project declares Core Objects, Relationships, Actions, Metrics, Risks in markdown.

## Entry Points

- New project: `Bootstrap/How_To_Start_New_Project.md`
- Index: `MANIFEST.md`
- Machine-readable: `factory.yaml`
- Vocabulary: `Glossary.md`
- Changes: `CHANGELOG.md`
