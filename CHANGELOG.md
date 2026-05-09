# Changelog

All notable changes to AI-NPI Factory. Versioning follows [Semver](https://semver.org/).

## [v0.2.1] — Unreleased (candidate, 2026-05-08)

> **운영정책 update — Frame/runner/hook/skill 코드 변경 0, 정책/문서 add only.**
> 본 candidate 는 Meta Sprint 절차 (실 데이터 누적 후) 를 거쳐 frozen 으로 격상된다.
> 본 update 의 핵심: GitHub 단일 동기화 + 신규 프로젝트의 Foundry 좌표 박제 + Non-Blocking Execution + Decision Queue + Copy-Paste Zero 로드맵.

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
