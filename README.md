# AI-NPI Factory

Reusable meta-platform for starting and running AI New Product Introduction (NPI) projects on a shared 4-Layer skeleton.

- **Version**: **0.3.0 (frozen 2026-05-18)** — previous: 0.2.1 frozen.
- **Status**: 0.3.0 frozen — Phase 1~5 field validation by `12.subscription-payment-saas-platform` (Phase 1 closure `3b8bc60` / Phase 2 closure `9b2967a` / Phase 3 closure `413848d` / Phase 4 closure `babf02f` / Phase 5 closure D-024 2026-05-18 / D-001~D-025 + FIL-001~015). Revalidation: B-002 self-test **6/6 PASS exit 0** + B-003 self-test **9/9 PASS exit 0** + v0.3.0 self-check **12/12 PASS** (2026-05-18). 정책/문서 add only — Frame/runner/hook/skill 코드 변경 0. Director Acceptance: **"Foundry v0.3.0 PASS"** (Director 김건우, 2026-05-18).
  v0.3.0 핵심: **Director Card Template v1.1** (4약속 + 추가 조건 A/B/C/D — 맥락 무지 / Implementer step 분리 / GPT orchestrator 통과 / Vim+bash+창식별 금지) + **Next Cycle Selection Rule** (D-025 amendment, D-017 폐기 — Implementer 자율 default + 우선순위 휴리스틱 5단계) + **Foundry FIL Ledger 신설** (FIL-008 desktop.ini cleanup script 표준 + FIL-014 `.env.local` worktree 누락 + FIL-015 frozen 1-block addition 패턴) + Non_Blocking_Execution_정책 §8 amendment. Director-facing summary: `Bootstrap/v0.3.0_Candidate_Elevation_Summary.md`.
- **0.2.1 (legacy frozen, 2026-05-12)**: GitHub 기반 Foundry 관리 + 신규 프로젝트 / meta 폴더 / Non-Blocking Execution / Human Control Point / Decision Queue / Meta Sprint / Copy-Paste Zero 로드맵 정책 + Phase 1+2 운영 데이터 누적 (backport candidates: `Bootstrap/v0.2.1_Frozen_Elevation_Evidence.md`). Frozen 격상 commit `40a3c61` (PR #1).

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
