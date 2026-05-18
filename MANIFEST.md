# MANIFEST — AI-NPI Factory v0.3.0 candidate

Index of all artifacts in the 4-Layer Frame.

> **v0.3.0 candidate (2026-05-18, draft)** — v0.2.1 frozen 위에 *추가* (Frame/runner/hook/skill 코드 변경 0, 정책/문서 add only). 본 candidate 의 trigger = source project `12.subscription-payment-saas-platform` Phase 1~5 closure (WP-002 ~ WP-005, D-015~D-025 + FIL-009~014 누적). 채택 항목: Director Card Template v1.1 (조건 A/B/C/D) + Next Cycle Selection Rule (D-025) + Foundry FIL Ledger (FIL-008 cleanup script 표준 + FIL-NEW .env.local worktree + FIL-WP005-pattern frozen 1-block addition) + Non_Blocking_Execution_정책 §8 amendment. Director Acceptance pending.
>
> Prior: v0.2.1 frozen on 2026-05-12 (Phase 1+2 field validation, D-001~D-014 + FIL-001~008). v0.2.0 frozen on 2026-05-08 (runner/skill/hook 첫 구현).

## Root
- `README.md` — entry point
- `factory.yaml` — machine-readable manifest
- `CHANGELOG.md`
- `Glossary.md`

## Layer 1 — Universal Operating Principles
- `1_Universal_Operating_Principles/00_Overview.md`
- `1_Universal_Operating_Principles/01_Decision_Principles.md`
- `1_Universal_Operating_Principles/02_Quality_and_Safety.md`
- `1_Universal_Operating_Principles/03_Scope_Management.md`
- `1_Universal_Operating_Principles/04_Versioning_Principles.md`
- `1_Universal_Operating_Principles/ontology-policy.md`
- `1_Universal_Operating_Principles/GitHub_Foundry_관리정책.md` *(v0.2.1 frozen — Source of Truth + GitHub 단일 동기화 채널)*
- `1_Universal_Operating_Principles/Human_Control_Point_정책.md` *(v0.2.1 frozen — 10 escalation 트리거)*
- `1_Universal_Operating_Principles/Non_Blocking_Execution_정책.md` *(v0.2.1 frozen + v0.3.0 candidate amendment §8 — next cycle 선택 비차단 / D-025)*
- `1_Universal_Operating_Principles/Copy_Paste_Zero_로드맵.md` *(v0.2.1 frozen — Stage 1~5 진화 로드맵)*

## Layer 2 — Reusable Workflow Modules
- `2_Reusable_Workflow_Modules/00_Overview.md`
- `2_Reusable_Workflow_Modules/_module_template.md`
- `2_Reusable_Workflow_Modules/01_problem-framing/`
- `2_Reusable_Workflow_Modules/02_research/`
- `2_Reusable_Workflow_Modules/03_requirements/`
- `2_Reusable_Workflow_Modules/04_architecture-planning/`
- `2_Reusable_Workflow_Modules/05_implementation/`
- `2_Reusable_Workflow_Modules/06_verification/` *(required: true)*
- `2_Reusable_Workflow_Modules/07_risk-review/`
- `2_Reusable_Workflow_Modules/08_launch/`
- `2_Reusable_Workflow_Modules/09_metrics-review/`
- `2_Reusable_Workflow_Modules/10_retrospective/`
- `2_Reusable_Workflow_Modules/신규_프로젝트_생성_Workflow.md` *(v0.2.1 frozen — Foundry version 복사 → factory.yaml + meta/ 필수, 10단계)*
- `2_Reusable_Workflow_Modules/Decision_Queue_운영방식.md` *(v0.2.1 frozen — DQ 8 컬럼, blocker 아님, batch review)*
- `2_Reusable_Workflow_Modules/Meta_Sprint_Backport_Workflow.md` *(v0.2.1 frozen — 11단계, 사용자 최종 승인 게이트, self-test 회귀 보호)*

## Layer 3 — Domain/Project Playbooks
- `3_Domain_Project_Playbooks/00_Overview.md`
- `3_Domain_Project_Playbooks/_template/README.md`
- `3_Domain_Project_Playbooks/_template/domain-ontology.md`
- `3_Domain_Project_Playbooks/ai-npi-platform/00_Project_Brief.md`
- `3_Domain_Project_Playbooks/ai-npi-platform/domain-ontology.md`
- `3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Brief.md` *(v0.2.0 — `schema_version: "0.2.0"` 추가됨; T-B9 self-test input)*
- `3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Blueprint.md`
- `3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Worklist.md`
- `3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Verification.md` *(v0.2.1 frozen — 2026-05-12 revalidation, runner 자동 생성, 6/6 PASS exit 0)*
- `3_Domain_Project_Playbooks/ai-npi-platform/B-003_NPI_Brief.md` *(v0.2.1 — v0.2.1 candidate AC 9건 input)*
- `3_Domain_Project_Playbooks/ai-npi-platform/B-003_NPI_Verification.md` *(v0.2.1 frozen — 2026-05-12 revalidation, runner 자동 생성, 9/9 PASS exit 0)*
- `3_Domain_Project_Playbooks/ai-npi-platform/NPI_Verification.md` *(v0.2.0 — T-B9 self-test 산출, runner 자동 생성, 6/6 Pass)*

## Layer 4 — Task-level Execution Templates
- `4_Task_Level_Execution_Templates/00_Overview.md`
- `4_Task_Level_Execution_Templates/프로젝트_meta_폴더_템플릿.md` *(v0.2.1 frozen — 6 파일 표준 + 통합 흐름)*
- `4_Task_Level_Execution_Templates/factory_yaml_template.md` *(v0.2.1 frozen — factory_source / project / local_modifications + 권장 확장 필드)*
- `4_Task_Level_Execution_Templates/Director_Card_Template.md` *(v1.1 candidate, v0.3.0 — 4약속 + 추가 조건 A/B/C/D, source: WP-004 T-25 + D-024)*
- `4_Task_Level_Execution_Templates/Next_Cycle_Selection_Rule.md` *(v1.0 candidate, v0.3.0 — D-025 amendment, D-017 폐기, Implementer 자율 default)*
- `4_Task_Level_Execution_Templates/NPI_Brief.md` *(≈ PRD; v0.2.0 — dual-form AC: prose + structured AC YAML with `schema_version: "0.2.0"` required)*
- `4_Task_Level_Execution_Templates/NPI_Blueprint.md` *(≈ Plan/Architecture)*
- `4_Task_Level_Execution_Templates/NPI_Worklist.md` *(≈ Tasks; Affected Objects optional per task)*
- `4_Task_Level_Execution_Templates/NPI_BuildLog.md` *(≈ Walkthrough)*
- `4_Task_Level_Execution_Templates/NPI_Verification.md` *(≈ QA; v0.2.0 — runner 가 자동 생성. 컬럼 = AC ID | Statement | Method | Result | Evidence)*
- `4_Task_Level_Execution_Templates/NPI_Patchnote.md` *(≈ Hotfix)*

## Layer 4 — Claude Code Harness (under L4)
- `4_Task_Level_Execution_Templates/claude-code/README.md`
- `4_Task_Level_Execution_Templates/claude-code/agents/README.md`
- `4_Task_Level_Execution_Templates/claude-code/agents/agent-candidates.md`
- `4_Task_Level_Execution_Templates/claude-code/agents/context-isolation-policy.md`

### Commands
- `4_Task_Level_Execution_Templates/claude-code/commands/scope-context.md`
- `4_Task_Level_Execution_Templates/claude-code/commands/plan-work.md`
- `4_Task_Level_Execution_Templates/claude-code/commands/execute-work.md`
- `4_Task_Level_Execution_Templates/claude-code/commands/validate-output.md` *(v0.2.0 implemented — skill ↔ runner ↔ hook 3계층 호출)*
- `4_Task_Level_Execution_Templates/claude-code/commands/review-risk.md`
- `4_Task_Level_Execution_Templates/claude-code/commands/extract-lessons.md`
- `4_Task_Level_Execution_Templates/claude-code/commands/ask-chatgpt-decision.md`

### Skills
- `4_Task_Level_Execution_Templates/claude-code/skills/README.md`
- `4_Task_Level_Execution_Templates/claude-code/skills/skill-candidates.md` *(v0.2.0 — `verification-runner` 행을 implemented 로 격상)*
- `4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/SKILL.md` *(v0.2.0 — 첫 implemented skill, 11개 섹션)*
- `4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/README.md` *(runner 사용법)*
- `4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/run.py` *(★ runner = single source of truth, Python 3.11+, stdlib-only)*
- `4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/tests/fixture_pass.md` *(should-pass 회귀 fixture)*
- `4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/tests/fixture_block.md` *(should-block 회귀 fixture)*

### Hooks
- `4_Task_Level_Execution_Templates/claude-code/hooks/README.md` *(v0.2.0 갱신 — before-final 섹션 추가)*
- `4_Task_Level_Execution_Templates/claude-code/hooks/hook-candidates.md` *(v0.2.0 — `before-final` 행을 implemented 로 격상)*
- `4_Task_Level_Execution_Templates/claude-code/hooks/before-final.ps1` *(v0.2.0 — PowerShell shim, ASCII 런타임 메시지)*
- `4_Task_Level_Execution_Templates/claude-code/hooks/before-final.cmd` *(v0.2.0 — Windows cmd wrapper, ASCII-only)*

### Worktree / MCP
- `4_Task_Level_Execution_Templates/claude-code/worktree/README.md`
- `4_Task_Level_Execution_Templates/claude-code/worktree/worktree-policy.md`
- `4_Task_Level_Execution_Templates/claude-code/mcp/README.md`
- `4_Task_Level_Execution_Templates/claude-code/mcp/mcp-connection-policy.md`

## Bootstrap
- `Bootstrap/How_To_Start_New_Project.md`
- `Bootstrap/How_To_Backport_Project_Lessons.md` *(v0.2.1 frozen — Meta Sprint Backport Workflow 11단계 인접 입문 문서)*
- `Bootstrap/Naming_and_Conventions.md`
- `Bootstrap/v0.2.1_Frozen_Elevation_Evidence.md` *(v0.2.1 frozen — 2026-05-12 frozen elevation 의 evidence bundle: project field validation metrics + D-001~D-014 + FIL-001~008 Tier 분류 + Operating Model v0.3/v0.3.1 backport 후보 + B-002/B-003 revalidation 결과)*
- `Bootstrap/Foundry_FIL_Ledger.md` *(v0.3.0 candidate — adopted FIL entry 박제: FIL-008 cleanup script 표준 + FIL-NEW .env.local worktree + FIL-WP005-pattern frozen 1-block addition)*
- `Bootstrap/v0.3.0_Candidate_Elevation_Summary.md` *(v0.3.0 candidate — Director-facing 5 spot summary, Director Acceptance pending)*

## Ontology Index
- Policy: `1_Universal_Operating_Principles/ontology-policy.md`
- Template: `3_Domain_Project_Playbooks/_template/domain-ontology.md`
- Instances:
  - `ai-npi-platform`: `3_Domain_Project_Playbooks/ai-npi-platform/domain-ontology.md`
