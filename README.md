# AI-NPI Factory

Reusable meta-platform for starting and running AI New Product Introduction (NPI) projects on a shared 4-Layer skeleton.

- **Version**: 0.2.0 (frozen) / **v0.2.1 candidate** (Unreleased)
- **Status**: 0.2.0 frozen — validate-output runner implemented, B-002 self-test passed (2026-05-08, 6/6 AC, exit 0).
  v0.2.1 candidate: GitHub 기반 Foundry 관리 + 신규 프로젝트 / meta 폴더 / Non-Blocking Execution / Human Control Point / Decision Queue / Meta Sprint / Copy-Paste Zero 로드맵 정책 도입 (Frame/runner 코드 변경 0, 정책/문서 add).

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
