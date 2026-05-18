# Changelog

All notable changes to AI-NPI Factory. Versioning follows [Semver](https://semver.org/).

## [v0.3.0] — Candidate 2026-05-18 (Director Acceptance pending)

> **운영정책 update — Frame/runner/hook/skill 코드 변경 0, 정책/문서 add only.**
> v0.2.1 frozen 위에 *추가* (regression 0). Field validation = `12.subscription-payment-saas-platform` Phase 1~5 (WP-002 ~ WP-005, D-015~D-025 + FIL-009~014 누적). Operating data 충분 누적 → 본 v0.3.0 candidate 박제.
> **Revalidation pending**: B-002 self-test (6 AC) + B-003 self-test (9 AC) — Director Acceptance 직전 1회 회귀 보호.
> 본 v0.3.0 의 핵심: **Director Card 4약속 강화 (조건 A/B/C/D)** + **D-025 next-cycle 자율 default amendment** + **Foundry FIL Ledger 신설 (FIL-008 cleanup script 표준화 + FIL-NEW .env.local worktree + FIL-WP005-pattern frozen 1-block addition)**.

### Candidate Trigger (2026-05-18)

- **Source cycle closure**: `12.subscription-payment-saas-platform` Phase 1~5 누적 (Phase 3 = WP-003 TossPayments, Phase 4 = WP-004 BillingCycle, Phase 5 = WP-005 Invoice Planning closed via D-023). D-014 ~ D-025 + FIL-009 ~ FIL-014 누적.
- **Decision references (source project)**:
  - D-021 후보 — Director Card 4약속 v1.0 (Foundry PR #2 squash `8324668` 으로 v0.2.1 위에 *forward-port* 완료, instance: 12.subscription `meta/director-card-template.md`).
  - D-022 (2026-05-16) — WP-004 Phase 4 CLOSED, Director Card 4약속 v1.0 first instance batch (T-25 v4 채택).
  - D-023 (2026-05-17) — WP-005 Planning Final CP Accepted · Phase 5 Planning CLOSED (read-mostly Invoice 도메인, frozen 1-block addition 패턴 first instance).
  - D-024 (예정 박제, 본 v0.3.0 backport 의 source) — Director Card 추가 조건 A/B/C/D 강화 (맥락 무지 / Implementer step 분리 / GPT orchestrator 통과 / bash+다중창 가정 금지).
  - D-025 (예정 박제, 본 v0.3.0 backport 의 source) — Next cycle 선택 = Implementer 자율 default. D-017 폐기. 우선순위 휴리스틱 5단계.

### Added — L4 Task-level Execution Templates (1 new + 1 amendment)

- [4_Task_Level_Execution_Templates/Next_Cycle_Selection_Rule.md](4_Task_Level_Execution_Templates/Next_Cycle_Selection_Rule.md) *(v1.0 candidate)* — Next cycle 선택의 Implementer 자율 default. D-017 폐기. 우선순위 휴리스틱: `deferred 제외` > `Foundry backport` > `planning draft` > `follow-up` > `HCP-only 카드` (마지막). reduced-copy Stage 2 의 자연 연장.
- [4_Task_Level_Execution_Templates/Director_Card_Template.md](4_Task_Level_Execution_Templates/Director_Card_Template.md) *(v1.0 → v1.1 candidate amendment)* — 4약속 (읽기/판단/디버깅/메커니즘 부담 0) 위에 **추가 조건 A/B/C/D**:
  - **조건 A** — 맥락 무지 가정 (이전 스크린샷 / 카드 / chat / 코드 변경 참조 0).
  - **조건 B** — Implementer 가 할 수 있는 모든 step (git / npm / build / test / lint) 은 카드 발급 *전* 에 흡수. Director 위임 = Director-only 행동 only.
  - **조건 C** — GPT(orchestrator) 가 단순 paste 중계만으로 Director-action 한 줄로 환원 가능.
  - **조건 D** — Vim/Emacs / 창 식별 / bash 가정 명령 / PowerShell 5.1 비호환 chain 연산자 (`&&`, `||`, `2>&1`) 금지.
- Self-audit 체크리스트 9 → 12 항목 확장 (조건 A/B/C/D 관련 3 항목 추가).

### Added — L1 Universal Operating Principles (1 amendment)

- [1_Universal_Operating_Principles/Non_Blocking_Execution_정책.md](1_Universal_Operating_Principles/Non_Blocking_Execution_정책.md) §8 *(v0.3.0 candidate amendment)* — Next cycle 선택의 비차단. D-025 cross-ref. D-017 폐기 명시. 자세한 표준은 L4 `Next_Cycle_Selection_Rule.md`.

### Added — Bootstrap (2)

- [Bootstrap/Foundry_FIL_Ledger.md](Bootstrap/Foundry_FIL_Ledger.md) *(v0.3.0 candidate, 신설)* — Foundry 표준으로 *채택된* FIL 만 박제하는 ledger. 본 v0.3.0 채택 3 entry:
  - **FIL-008** — Windows `desktop.ini` post-merge `.git` 트리 침투. 표준 cleanup 스크립트 박제 (`$g = git rev-parse --git-common-dir; Get-ChildItem $g -Recurse -Force -Filter "desktop.ini" | Remove-Item -Force`). 재현 N=7+ (Foundry main repo 자체에서도 본 cycle 중 재발 → 동일 스크립트로 해소).
  - **FIL-NEW (FIL-014 후보)** — agent worktree 의 `.env.local` 부재로 validate/test ENOENT. Implementer 가 main worktree 에서 *읽기-전용 복사* (Director Card 발급 0). secret 노출 anti-pattern 명시.
  - **FIL-WP005-pattern** — read-mostly cycle 의 frozen file *1-block addition* Director-gated extension 패턴 (WP-005 가 WP-003/004 frozen RPC bundle 확장한 모델, D-023 first instance).
- [Bootstrap/v0.3.0_Candidate_Elevation_Summary.md](Bootstrap/v0.3.0_Candidate_Elevation_Summary.md) *(v0.3.0 candidate, 신설)* — Director-facing 5 spot summary. Director Acceptance 직전 단일 진입점.

### Changed

- [MANIFEST.md](MANIFEST.md) — header 가 v0.2.1 frozen → v0.3.0 candidate 로 표기 변경. L4 섹션에 2 신규 (Director Card v1.1 + Next Cycle Selection Rule). Bootstrap 섹션에 2 신규 (FIL Ledger + Candidate Elevation Summary). L1 Non_Blocking 항목에 v0.3.0 amendment 표기.

### Not Changed in this candidate (의도적)

- `factory.yaml.factory.version` — 여전히 `0.2.1` frozen. 본 v0.3.0 = *candidate* 단계, frozen 격상 시점에 bump.
- runner (`run.py`) / hook (`before-final.ps1` / `before-final.cmd`) / skill (`SKILL.md` + `README.md`) / NPI_Brief 템플릿 / B-002 산출물 / Naming Map / Document Terminology Map / Phase + WP-NNN naming — 모두 손대지 않음 (정책 변경 0).
- L1 / L2 / L4 의 기존 v0.2.1 frozen 정책 문서 — 본문 변경 0 (`Non_Blocking_Execution_정책.md` 만 §8 amendment append).
- source project (`12.subscription-payment-saas-platform`) — 어떤 파일도 수정 0.

### Verification (Director Acceptance 직전 수행)

- **B-002 self-test (회귀 보호)**: `python run.py --brief 3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Brief.md` — expected `total=6 pass=6 fail=0 exit=0`. 코드 변경 0 이므로 PASS 자연 결과.
- **B-003 self-test (회귀 보호)**: 동일 — expected `total=9 pass=9 fail=0 exit=0`.
- B-004 신설 여부 = Director 결정 (본 v0.3.0 candidate AC 박제 시점에 검토). 본 draft = B-004 미생성.

### 다음 단계 (Foundry 측)

- Director Acceptance (1-line "진행" 또는 carded review).
- Acceptance 시 frozen 격상: `factory.yaml.factory.version` `0.2.1` → `0.3.0` + `status: frozen` + `frozen_on` 박제 + B-002/B-003 revalidation.
- 격상 commit 후 Foundry repo tag `v0.3.0`.

### Source Project Changes Required (격상 이후, 별도 cycle)

- source project `meta/decisions.md` 에 D-024 + D-025 정식 박제 (현재 본 v0.3.0 candidate 의 source).
- source project `meta/foundry-improvement-log.md` 에 FIL-014 (`.env.local` worktree) 정식 추가.
- source project `meta/foundry-backport-candidates.md` 의 *승인* 섹션에 FIL-008 / FIL-014 / FIL-WP005-pattern 박제 (현재 *보류* / 신설).
- 위 변경은 *Foundry frozen 격상 이후 별도 cycle*. 본 작업 범위 = Foundry draft only.

---

## [v0.2.1] — Frozen 2026-05-12 (elevated from candidate)

> **운영정책 update — Frame/runner/hook/skill 코드 변경 0, 정책/문서 add only.**
> Field validation = `12.subscription-payment-saas-platform` Phase 1+2 (Phase 1 closure `3b8bc60` / Phase 2 closure `9b2967a` + post-F-002 closure `7a4fe2c` + D-014 documentation PR drafted). Operating data 충분 누적 → 2026-05-12 frozen elevation.
> **Revalidation (2026-05-12)**: B-002 self-test 6/6 PASS (exit 0) + B-003 self-test 9/9 PASS (exit 0). 코드 변경 0 이므로 회귀 0 보장.
> 본 v0.2.1 의 핵심: GitHub 단일 동기화 + 신규 프로젝트의 Foundry 좌표 박제 + Non-Blocking Execution + Decision Queue + Copy-Paste Zero 로드맵.

### Frozen Elevation Entry (2026-05-12)

- **Trigger**: `12.subscription-payment-saas-platform` Phase 1+2 cycle 종료 + D-001~D-014 + FIL-001~008 + Operating Model v0.2.1 → v0.3 → v0.3.1 까지의 evolution data 누적 + Director DQ-027 "(b)+(c) parallel" 결정 (D-014, 2026-05-12).
- **Decision references (project repo, 12.subscription-payment-saas-platform)**:
  - D-001 (2026-05-09) — Foundry seed = `d4455f08…` (v0.2.1 candidate) 채택
  - D-002 (2026-05-09) — `local_modifications: true` 시작
  - D-003 (2026-05-09) — F-001 Start CP 통과 + 7 modification (service_role banned 등)
  - D-004 (2026-05-10) — F-001 offline scaffold phase 진입 (HCP partial unblock 패턴, FIL-001 origin)
  - D-005 (2026-05-11) — T-1 HCP 회신 + H-001 Hotfix (React 18 hook 호환, FIL-002 origin)
  - D-006 (2026-05-11) — Operating Model v0.2 합의 (4-Layer / Phase / F-ID / M-ID / Control Plane / Director View, FIL-003~006 origin)
  - D-007 (2026-05-11) — AC-B gap path C+D approved (Conditionally Complete + §A.2.R Implementer-driven validation suite 패턴 원천, FIL-002 추가 영향)
  - D-008 (2026-05-11) — F-001 Phase 1 closure (PR #1 squash → 3b8bc60)
  - D-009 (2026-05-11) — DQ-018 closure + F-002 Spec drafted (Phase 2 진입 직전)
  - D-010 (2026-05-11) — DD-PHASE-2-START approved with 8 explicit constraints (HCP boundary)
  - D-011 (2026-05-11) — Operating Model v0.3 candidate 박제 (Reduced-copy Stage 2 + Calibrated Stage 3)
  - D-012 (2026-05-12) — Director Naming Model clarification (Phase + WP-NNN / Meta Sprint + IP-NNN + Legacy Trace alias)
  - D-013 (2026-05-12) — F-002 Final CP Accepted + Phase 2 closed + v0.3 frozen forward-port executed (PR #12 → 7a4fe2c)
  - D-014 (2026-05-12) — DQ-027 RESOLVED (b)+(c) parallel + Naming Model improvement (Brief→Spec / Blueprint→Design) + WP-002 file rename + Meta Sprint 1 진입 + v0.3.1 additive patch (project repo PR #13 drafted)
- **Foundry Improvement Log references (project repo, 12.subscription-payment-saas-platform)**:
  - FIL-001 — 단일-키 HCP 가 cycle 전체 차단 안티패턴 → HCP partial-block 분리 패턴 제안 (D-004 패턴 일반화)
  - FIL-002 — AC-A mock 단위 테스트가 React 18/19 hook 호환성 검증 누락 → AC-Offline 에 dev server boot smoke test 추가 제안 (H-001 원인)
  - FIL-003 — Project Control Plane 과 Meta Backlog 분리 부재 → `control/` vs `meta/` 폴더 분리 후보
  - FIL-004 — Director View 자동화 부재 → DirectorView_schema.yaml + generator 후보
  - FIL-005 — Feature/Work Package ID 메타데이터 표준 부재 → NPI_Brief 템플릿 §0 4 필드 강제 (Purpose / Goal / Project Relevance / Non-Goals)
  - FIL-006 — 4-Layer 가 implementation folder hierarchy 로 오용 위험 → README + MANIFEST 에 비역할 1 단락 추가 제안
  - FIL-007 — vi.mock 팩토리의 TDZ → `vi.hoisted` 표준 mock 패턴 박제 제안
  - FIL-008 — Windows `desktop.ini` 가 `.git/refs/` 트리에 침투 → `scripts/git-cleanup.mjs` + `pnpm git:cleanup` 자동화 제안 (현재 cycle 에서 1차 발생)
- **Project field validation metrics**:
  - PRs merged in project repo: #1~#12 (Phase 1 + dashboard + planning + F-002 cycle + D-013 closure). 본 cycle 중 PR #13 (D-014 documentation) = drafted.
  - Decision queue: DQ-001 ~ DQ-029 누적 (3 결번, 그 외 모두 박제).
  - Hotfix: H-001 (React 18 hook 호환).
  - Tests in product code: 52/52 PASS (auth 6 + sub-state 13 + perms 13 + payment 11 + actions 9).
  - Migration applied: 1 (`20260512000000_phase2_subscription_domain.sql`).
- **Operating Model evolution captured (project repo)**:
  - v0.2 (2026-05-11, D-006) — 4-Layer / Phase / F-ID / M-ID / Control Plane / Director View 정의
  - v0.2.1 (2026-05-11) — Context Hygiene Pass (Roles 표 + Decision Type Classification 4 단계)
  - v0.2.2 (2026-05-11) — Context Hygiene Pass II (§10 Reporting Discipline + Director Card 형식)
  - v0.3 (2026-05-12 frozen, D-013) — Reduced-copy Stage 2 + Calibrated Stage 3 + Director-facing Naming Model
  - v0.3.1 (2026-05-12 additive patch, D-014) — Document Terminology Map (Brief→Spec / Blueprint→Design / Worklist unchanged / Verification unchanged) + File Rename Map + Meta Sprint planning entry pattern

### Frozen Elevation Verification (2026-05-12)

- **B-002 self-test (T-B9 회귀 보호)**:
  - `python run.py --brief 3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Brief.md`
  - Result: **PASS** (total=6 pass=6 fail=0 exit=0).
  - Artifact: [`3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Verification.md`](3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Verification.md) (신규, runner 자동 생성).
- **B-003 self-test (v0.2.1 candidate AC 9건 회귀 보호)**:
  - `python run.py --brief 3_Domain_Project_Playbooks/ai-npi-platform/B-003_NPI_Brief.md`
  - Result: **PASS** (total=9 pass=9 fail=0 exit=0).
  - Artifact: [`3_Domain_Project_Playbooks/ai-npi-platform/B-003_NPI_Verification.md`](3_Domain_Project_Playbooks/ai-npi-platform/B-003_NPI_Verification.md) (갱신, runner 자동 생성).
  - AC-7 / AC-8 / AC-9 = "CHANGELOG / README / MANIFEST 에 v0.2.1 존재" — 본 frozen elevation 후에도 모두 PASS (frozen 표기는 candidate 표기를 *대체* 하지만 substring `v0.2.1` 는 유지).
- **회귀 보호**: 본 v0.2.1 frozen elevation = 정책/문서 변경 only. Frame / runner / hook / skill 코드 변경 0. 따라서 두 self-test 모두 PASS 가 자연 결과.

### Field Validation Evidence (post-Frozen)

자세한 backport candidates + Phase 1+2 operating data + IP 후보 정리는 별도 evidence 문서로 박제:

- [`Bootstrap/v0.2.1_Frozen_Elevation_Evidence.md`](Bootstrap/v0.2.1_Frozen_Elevation_Evidence.md) (신규, 본 frozen elevation 의 single source of truth)

본 evidence 문서는 (a) 12.subscription-payment-saas-platform Phase 1+2 cycle metrics (b) D-001~D-014 짧은 요약 (c) FIL-001~008 backport candidate 분류 (Tier 1 / Tier 2 / Tier 3) (d) Meta Sprint 1 의 IP-001/002/003 candidate (e) Operating Model v0.3 / v0.3.1 의 Foundry 측 backport 후보를 모두 포함.

### Not Changed in this Frozen Elevation (의도적)

- `factory.yaml.factory.version` 만 `0.2.0` → `0.2.1` 로 bump + `status: frozen` + `frozen_on: 2026-05-12` + `previous_version: 0.2.0` + `elevation_evidence` 블록 추가.
- runner (`run.py`) / hook (`before-final.ps1` / `before-final.cmd`) / skill (`SKILL.md` + `README.md`) / NPI_Brief 템플릿 / B-002 산출물 — 모두 손대지 않음 (정책 변경 0).
- L1 / L2 / L4 의 v0.2.1 candidate 정책 문서 — 본문 변경 0. MANIFEST.md 의 annotation 만 "candidate" → "frozen".
- Bootstrap/How_To_* 문서 — 보존.

### 다음 단계 (Foundry 측)

- 본 PR 머지 후 Foundry repo tag `v0.2.1` 부여 (Meta Sprint Backport Workflow §9 정합).
- v0.3.0 candidate 후보 = Meta Sprint 1 (project repo 의 IP-001/002/003) 의 구현 완료 + Foundry 측 backport 채택 시점. 본 v0.2.1 frozen 까지는 *정책/문서 + field validation* 만, *구현 코드* 는 v0.3.0 candidate 부터.

### Added — L1 Universal Operating Principles (4)
- [GitHub_Foundry_관리정책.md](1_Universal_Operating_Principles/GitHub_Foundry_관리정책.md) — 00-Foundry 가 Source of Truth. GitHub clone/pull/commit/push 단일 동기화 채널. 안정 version 은 tag 또는 frozen. 신규 프로젝트는 source version+commit SHA 박제. 추적되지 않는 로컬 변경 지양. 위반 신호 체크리스트.
- [Human_Control_Point_정책.md](1_Universal_Operating_Principles/Human_Control_Point_정책.md) — 사람은 전달자가 아니라 최종 승인자. 10개 escalation 트리거 (보안 / 결제·과금 / DB schema / 법률·컴플라이언스 / 되돌리기 어려운 아키텍처 / 큰 범위 변경 / 큰 비용 증가 / BM·가격 / 사용자 데이터 / 외부 API 계약). Escalation 형식 7 필드. 비-escalation 은 decision-queue.
- [Non_Blocking_Execution_정책.md](1_Universal_Operating_Principles/Non_Blocking_Execution_정책.md) — Claude 는 작은 결정마다 멈추지 않는다. 분류 매트릭스 4 행. Default Action 우선순위 (Foundry 룰 → 프로젝트 factory.yaml → 언어/프레임워크 관용 → 일관 판단). 위반 신호 4 패턴. ChatGPT 호출 절제.
- [Copy_Paste_Zero_로드맵.md](1_Universal_Operating_Principles/Copy_Paste_Zero_로드맵.md) — 장기 명제: 사람은 전달자 → 승인자. 5 단계 (표준 수동 패키지 → Decision Queue Batch → 반자동 handoff → API A2A → Copy-Paste Zero). 각 단계 측정 지표. ChatGPT 사용 시점 4종 (Start CP / Critical Decision / Final Review / Meta Sprint).

### Added — L2 Reusable Workflow Modules (3)
- [신규_프로젝트_생성_Workflow.md](2_Reusable_Workflow_Modules/신규_프로젝트_생성_Workflow.md) — 신규 프로젝트는 특정 Foundry version+commit 복사 시작. thin control plane 미사용. factory.yaml + meta/ 필수. 추적 가능성 보존. 10단계 절차.
- [Decision_Queue_운영방식.md](2_Reusable_Workflow_Modules/Decision_Queue_운영방식.md) — Queue 는 blocker 아님. 표준 8 컬럼 (ID / Date / Topic / Decision Needed / Default Action Taken / Reversibility / Risk / Review Timing). 검토 시점 3종 (Final Review / Meta Sprint / Next Cycle). 깊이 신호.
- [Meta_Sprint_Backport_Workflow.md](2_Reusable_Workflow_Modules/Meta_Sprint_Backport_Workflow.md) — 프로젝트 종료 후만 진행. meta/ 전체 검토. 일반화 가능한 개선만 후보. 프로젝트 특화 자동 반영 금지. 사용자 최종 승인 게이트 + self-test 회귀 보호 + Semver bump + push+tag. 11단계.

### Added — L4 Task-level Execution Templates (2)
- [프로젝트_meta_폴더_템플릿.md](4_Task_Level_Execution_Templates/프로젝트_meta_폴더_템플릿.md) — 표준 6 파일 (foundry-improvement-log.md / foundry-backport-candidates.md / decisions.md / decision-queue.md / lessons-learned.md / chatgpt-decision-requests.md). 각 파일 stub 템플릿 + 통합 흐름 + 안티-패턴.
- [factory_yaml_template.md](4_Task_Level_Execution_Templates/factory_yaml_template.md) — 프로젝트 측 factory.yaml. 3 필수 블록 (factory_source / project / local_modifications) + 권장 확장 (meta_artifacts / ai_npi_root / foundry_paths / history). 안티-패턴.

### Changed
- [README.md](README.md) — Status 라인 갱신: 0.2.0 frozen + v0.2.1 candidate 표기.
- [MANIFEST.md](MANIFEST.md) — L1/L2/L4 인덱스에 9 신규 파일 추가 (각 항목에 v0.2.1 candidate 표기).

### Verification
- 본 v0.2.1 candidate 의 7개 AC 를 [3_Domain_Project_Playbooks/ai-npi-platform/B-003_NPI_Brief.md](3_Domain_Project_Playbooks/ai-npi-platform/B-003_NPI_Brief.md) 에 박제 + runner 로 검증.
- 산출물: [3_Domain_Project_Playbooks/ai-npi-platform/B-003_NPI_Verification.md](3_Domain_Project_Playbooks/ai-npi-platform/B-003_NPI_Verification.md).
- B-002 self-test (v0.2.0 frozen 보호) 도 회귀 없이 그대로 6/6 PASS 유지 — 코드 변경 0이므로 동작 영향 없음.

### Not Changed (의도적)
- `factory.yaml.factory.version` — 여전히 `0.2.0` frozen. 본 candidate 는 정책/문서 변경이므로 *코드를 동반한 freeze* 시점에 0.2.1 로 bump (Meta Sprint 결과로 진행).
- runner / hook / skill / NPI_Brief 템플릿 / B-002 산출물 — 모두 손대지 않음.
- Bootstrap/ 의 기존 How_To_* 문서 — 보존 (operational quick-start 역할 유지). 본 v0.2.1 의 L1/L2/L4 정책 문서가 *공식 invariant + workflow + template* 으로 격상되었고, Bootstrap 은 그것을 *사용자 친화적으로 재진술* 하는 layer.

### 다음 단계
- 사용자가 `00-Foundry` 를 GitHub 에 push (private repo) — 본 정책 효력 발동의 전제 조건.
- 진행 중 `12.subscription-payment-saas-platform` 프로젝트에 본 정책 후행 적용 (factory.yaml + meta/ 6 파일 생성, factory_source.commit 박제).
- 본 candidate 의 frozen 격상은 첫 Meta Sprint 결과로 결정 (Foundry v0.3.0 또는 v0.2.1 stable).

---

## [Unreleased]

### Policy / Operations Update — GitHub 기반 운영 + Meta Sprint 도입 (2026-05-08, 이전 정리 — v0.2.1 candidate 의 *상위 일부* 가 본 항목으로 흡수됨)

**배경**: 사용자가 여러 컴퓨터에서 작업하며 다중 프로젝트를 동시 운영한다. 진행 중 프로젝트의 1번 사례로 Foundry 원본을 즉시 수정하면 다른 프로젝트가 깨지는 위험 + 머신 간 동기화 부재 + 진화 근거 불명확 문제가 누적된다.

**결정 — Foundry 운영 정책 v2** (코드/Frame 변경 없음, 정책/운영 절차만):

1. **GitHub 동기화** — `00-Foundry` 는 GitHub repo 로 동기화한다 (private 권장). 다중 머신 간 동기화는 `git pull`/`git push` 로만. 폴더 직접 복사 금지.
2. **Project Instance 좌표** — 신규 프로젝트는 Foundry 의 *특정 Semver + commit SHA* 에서 시작한 *project instance* 로 기록된다. 좌표는 프로젝트 측 `factory.yaml` 의 `factory_source.{repo, version, commit, copied_on}` 4 필드에 박제.
3. **즉시 변경 금지** — 프로젝트 진행 중 발견한 Foundry 개선사항은 **즉시 원본에 반영하지 않는다.** 프로젝트의 `meta/` 폴더에 누적.
4. **Meta Sprint** — 프로젝트 종료 (또는 1차 마일스톤 완료) 시 Meta Sprint 를 실행. Claude Code 가 1차 분류 (승인/보류/폐기/추가검토) → ChatGPT 가 추가검토 항목 리뷰 → 사용자가 최종 승인 → 승인 항목만 `00-Foundry` 에 commit.
5. **Semver Bump 시점** — Meta Sprint 의 승인 commit 들이 push 되는 시점에 Foundry 의 다음 version 을 결정 (호환성 깨짐=major, 신규 기능=minor, 정정=patch). `factory.version` 갱신 + `CHANGELOG` 닫음 + `git tag v<version>`.
6. **self-test 회귀 보호** — Meta Sprint 종료 *전* 에 B-002 패턴 self-test (6개 AC) 를 다시 통과해야 한다. 그래야 Foundry 가 *자기 자신을 여전히 검증할 수 있음* 이 보장된다.

### Added (Bootstrap 운영 문서)
- [Bootstrap/How_To_Backport_Project_Lessons.md](Bootstrap/How_To_Backport_Project_Lessons.md) — Meta Sprint 절차 11단계 (사전 동기화 → 후보 수집 → ChatGPT 라운드 → 사용자 최종 승인 게이트 → Foundry 반영 → Semver bump → CHANGELOG → self-test → push+tag → 프로젝트 측 마무리 → 다중 프로젝트 후속). 안티-패턴 5개.
- [Bootstrap/project-meta-templates/foundry-improvement-log.md](Bootstrap/project-meta-templates/foundry-improvement-log.md) — 프로젝트 진행 중 raw 개선 아이디어 누적 템플릿. FIL-NNN ID, 8 필드 형식.
- [Bootstrap/project-meta-templates/foundry-backport-candidates.md](Bootstrap/project-meta-templates/foundry-backport-candidates.md) — Meta Sprint 정제 후보 모음. 4 분류 섹션 (승인/보류/폐기/추가검토) + Meta Sprint 운영 메타.
- [Bootstrap/project-meta-templates/decisions.md](Bootstrap/project-meta-templates/decisions.md) — 프로젝트 측 Critical Decision 시간순 로그.
- [Bootstrap/project-meta-templates/lessons-learned.md](Bootstrap/project-meta-templates/lessons-learned.md) — cycle 별 keep/change/drop 회고 (다음 cycle 행동 변화용).
- [Bootstrap/project-meta-templates/factory.yaml.template](Bootstrap/project-meta-templates/factory.yaml.template) — 프로젝트 측 `factory.yaml` 템플릿. `factory_source` / `project` / `local_modifications` / `meta_artifacts` / `foundry_paths` 5 블록.

### Changed
- [Bootstrap/How_To_Start_New_Project.md](Bootstrap/How_To_Start_New_Project.md) — 전면 개정 (v0.1.0 수동 절차 → v0.2.0+ GitHub 기반). 11단계 (사전 준비 → 시작점 확정 → 폴더 생성 → factory.yaml → Brief 우선 → meta/ 운영 정책 → 검증 → Start CP → Automated → Final CP → Meta Sprint 진입). `local_modifications` 가 `true` 로 전환되는 결정도 Human Control Point 트리거에 추가.

### Not Changed (의도적)
- `factory.version` 은 `0.2.0` frozen 상태 유지. 본 변경은 *운영 정책* 이며 *Frame / runner / hook / skill 코드* 변경 0. Semver bump 는 Meta Sprint 가 다른 실 프로젝트 데이터를 누적해 코드/Frame 변경을 동반할 때 수행한다.
- B-002 self-test 결과 그대로 유효 (변경된 코드 없음).

### 다음 단계 (운영 측)
- 사용자가 본 정책에 따라 `00-Foundry` 를 GitHub 에 push (private repo).
- 진행 중인 `12.subscription-payment-saas-platform` 프로젝트는 본 정책의 첫 적용 사례로 `factory.yaml` + `meta/` 4파일 추가 (별도 작업).
- Foundry 의 다음 frozen version (v0.3.0 후보) 은 첫 Meta Sprint 결과로 결정한다.

---

## [0.2.0] — 2026-05-08

### Decided (Critical Decisions, 2026-05-08)
- **T-B1 — runner host 언어**: **Python 3.11+** (stdlib-first, minimal-subset 자체 YAML 파싱; PyYAML 은 단일 옵션 의존성). 근거: YAML 파싱·파일 처리·shell command 실행·evidence 기록 4축에서 Python 의 안정성이 가장 높고, host 와 artifact schema 가 분리되어 있어 되돌림 비용 0.5~1일 (Reversible). PowerShell 5.1 은 native YAML 부재로 탈락, Bash+yq 는 Windows 의존성, Node.js 는 Factory 규모 대비 과함.
- **T-B8 — `schema_version` 키 도입**: **YES**, 필수 필드. 초기값 `"0.2.0"`. runner 는 키 부재·미지원 버전 모두 즉시 fail (exit 2). 이후 AC schema 변경은 **Semver**.

### Added
- **`validate-output` runner** — `4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/run.py`. Python 3.11+, stdlib-only, minimal-subset YAML 파서 내장. CLI: `python run.py --brief <path> [--out <path>] [--strict]`. exit code 분리 (0 = 전체 Pass / 1 = AC 검증 실패 / 2 = schema/parse error). method 3종 (`command`, `file_exists`, `manual`) 구현. evidence = stdout/stderr 마지막 50줄 또는 path별 exists/size 또는 confirmer+ISO date. 5종 수동 검증 통과 (Pass / schema 누락 / 미지원 schema / 일부 Fail 혼합 / 결정성 SHA-256 동일). [T-B2]
- **`verification-runner` skill** — `4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/SKILL.md`. 11개 섹션 (Purpose / When / Inputs / Outputs / Standard Procedure / Context Discipline / Subagent Conditions / Invocation / Failure Reporting / Anti-patterns / History). skill 검증 로직 0줄, runner 호출 + decision-ready summary 만 담당. subagent 임계 5개 명시. [T-B3]
- **`before-final` hook** — `4_Task_Level_Execution_Templates/claude-code/hooks/before-final.ps1` (PowerShell shim) + `before-final.cmd` (Windows cmd wrapper, ASCII-only). hook 검증 로직 0줄, runner exit code 0/1/2 passthrough. should-pass / should-block / parse-error 3 + cmd wrapper 4 케이스 검증 통과. [T-B4]
- **`NPI_Brief.md` structured AC schema** — dual-form (prose 표 + structured AC YAML). 최상위 `schema_version` 필수. 각 AC 항목 `id` / `statement` / `method` 필수. method 3종만 허용. manual 은 `manual_confirmer` + `confirm_date` 강제 (fake-pass 차단). 예시 3개 포함. [T-B5]
- **`schema_version: "0.2.0"`** — structured AC YAML 의 첫 schema. v0.2.0 runner 가 단독 지원. [T-B8]
- **회귀 fixture 2종** — `tests/fixture_pass.md` (3 method 각 1개 AC 모두 Pass), `tests/fixture_block.md` (file_exists 누락 + manual 잘못된 date 의도적 Fail).

### Changed
- **`validate-output.md` 명령** — v0.1.0 markdown 수동 절차를 폐기하고 v0.2.0 "skill ↔ runner ↔ hook 3계층 호출" 모델로 재정의. runner = single source of truth 명시. 직접 실행 / hook 경유 양쪽 명령 예시 + Subagent 권장 조건 5개 + Anti-patterns 6개 박제. [T-B6]
- **`hooks/README.md`** — v0.2.0 implementation status 섹션 추가. before-final 섹션 — 목적 / runner 와의 관계 / interface / exit code 표 / settings.json 등록 예시 (PS+cmd 양쪽) / 수동 검증 가이드.
- **`hook-candidates.md` / `skill-candidates.md`** — `Status` / `Package` 컬럼 추가. `before-final` 과 `verification-runner` 항목을 *implemented* 로 격상.
- **`B-002_NPI_Brief.md`** — structured AC YAML 최상위에 `schema_version: "0.2.0"` 추가. 하단 참고 문구 갱신.

### Released / Frozen
- **2026-05-08 — v0.2.0 released and frozen.**
- **B-002 Self-test 통과 (T-B9)**: B-002 본 Brief 의 6개 AC 를 새 runner 로 검증. `before-final.ps1 -Brief B-002_NPI_Brief.md` → **exit 0, total=6 pass=6 fail=0**. AC-1 file_exists 자동 Pass + AC-2~AC-6 manual 5개 confirmer/date Pass. 산출물: [`3_Domain_Project_Playbooks/ai-npi-platform/NPI_Verification.md`](3_Domain_Project_Playbooks/ai-npi-platform/NPI_Verification.md). Factory 가 자기 자신을 자기 도구로 검증하는 *self-application* 성립.
- 다음 단계: v0.3.0 후보 (PyYAML 단일 의존성 채택 재평가, OS-aware command matrix, 추가 verification method 확장, 다른 hook/skill candidate 의 implemented 격상).

## [0.1.0] — 2026-05-07
### Added
- 4-Layer Frame skeleton (L1 / L2 / L3 / L4 folders)
- L1 Universal Operating Principles (5 docs + ontology policy)
- L2 `_module_template.md` and 10 module placeholders
- L3 `_template/` + first instance `ai-npi-platform/`
- L4 six Factory-native templates (NPI_Brief / Blueprint / Worklist / BuildLog / Verification / Patchnote)
- `factory.yaml` (minimal machine-readable manifest)
- `MANIFEST.md`, `Glossary.md`, `Bootstrap/`
- Acceptance-Criteria-Driven Execution (ACDE) doctrine
- Minimum Human Intervention with Start / Automated / Human / Final Control Points
- Lightweight Ontology (markdown-based, PascalCase objects, no namespace in v0.1.0)
- Claude Code Harness under L4 (`claude-code/`): agents principles + candidates, 7 commands, skill candidates, hook candidates, worktree policy, MCP policy
- `factory.yaml` `harness.claude_code` block; `MANIFEST.md` harness index

### Released / Frozen
- 2026-05-07 — v0.1.0 released and frozen.
- B-002 Self-test 통과: Factory가 자기 자신을 대상으로 `scope-context` → `plan-work` → Final Control Point 사이클을 완주함.
- 산출물: `3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Brief.md`, `B-002_NPI_Blueprint.md`, `B-002_NPI_Worklist.md`.
- 다음 단계: v0.2.0 진입 전 Critical Decision (T-B1: runner host 언어 선정).
