# B-002 — NPI_Worklist

## 참조
- Source Brief: `B-002_NPI_Brief.md`
- Source Blueprint: `B-002_NPI_Blueprint.md`

본 Worklist는 두 묶음으로 구성된다.
- **A. v0.1.0 범위 — 문서 산출 작업** (B-002의 본 작업)
- **B. v0.2.0 이관 항목 — 실제 구현 작업** (별도 Brief 또는 본 Brief 후속으로 진행)

---

## A. v0.1.0 범위 — 문서 산출 작업

### T-A1 — B-002_NPI_Brief.md 작성
- **산출물**: `3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Brief.md`
- **Acceptance Criteria**:
  - 목적/배경/범위/제외 범위/AC/structured AC YAML/Affected Objects/Control Point 판단 8개 섹션이 모두 존재.
  - structured AC YAML 블록이 v0.2.0 schema와 동일 키 구조 사용.
  - Affected Objects는 `domain-ontology.md` 실재 Object만 사용.
- **Affected Objects** (선택): `Template`, `AcceptanceCriterion`
- **검증 방법**: `file_exists` + `manual` (사람 검토)
- **Status**: completed (본 작업으로 생성됨)

### T-A2 — B-002_NPI_Blueprint.md 작성
- **산출물**: `3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Blueprint.md`
- **Acceptance Criteria**:
  - "v0.2.0 validate-output 구현 방향" 단락이 존재.
  - runner/hook/skill/subagent 4개 구성 요소의 관계가 표 + 다이어그램으로 명시.
  - verification method 3종 각각의 입력 필드/통과 조건/증거 형식 정의.
  - 예상 파일 변경 목록 + 리스크/완화책 표 포함.
  - AC ↔ Blueprint 커버리지 표가 Brief의 모든 AC를 커버.
- **Affected Objects** (선택): `Template`, `WorkflowModule`, `ControlPoint`
- **검증 방법**: `file_exists` + `manual`
- **Status**: completed

### T-A3 — B-002_NPI_Worklist.md 작성 (본 파일)
- **산출물**: `3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Worklist.md`
- **Acceptance Criteria**:
  - 작업 목록(A 묶음) + 각 작업의 산출물 + 각 작업의 AC + (선택) Affected Objects 포함.
  - v0.2.0 구현 이관 항목(B 묶음)이 별도 섹션으로 분리.
- **Affected Objects** (선택): `Artifact`
- **검증 방법**: `file_exists` + `manual`
- **Status**: in_progress → completed (본 파일 저장 시점)

### T-A4 — Final Control Point 통과 (B-002 본 작업)
- **산출물**: B-002 본 작업의 Final Control Point 통과 기록 (BuildLog 항목, 본 v0.1.0에서는 사용자 확인으로 대체).
- **Acceptance Criteria**:
  - Brief의 AC-1 ~ AC-6 모두 충족.
  - manual AC의 `confirm_date` 필드가 ISO date로 채워짐.
  - 미해결 Critical Decision 없음 (R-언어는 v0.2.0 단계로 이관됨이 명시되어 있음).
- **검증 방법**: `manual` (사용자 + factory-foreman)
- **Status**: pending — 사용자 검토 대기

---

## B. v0.2.0 이관 항목 — 실제 구현 작업

> 이 항목들은 **본 B-002에서 실행하지 않는다.** v0.2.0 진입 시 별도 Brief로 분리하거나, 본 Brief의 후속 단계로 진행한다.

### T-B1 — runner host 언어 선정 (Critical Decision)
- **산출물**: 결정 기록 (`ask-chatgpt-decision.md` 패키지 또는 사용자 직접 결정).
- **Acceptance Criteria**: 후보 비교(예: PowerShell vs Bash+Python vs Node) + 선정 + 사유. 되돌림 비용 명시.
- **Affected Objects**: `WorkflowModule`, `Artifact`
- **선행 조건**: 없음 (v0.2.0 구현 시작 시 첫 단계)
- **Status**: ✅ completed (2026-05-08)
- **결정 요약**: Python 3.11+ 채택, stdlib-first, YAML은 minimal-subset 자체 파싱으로 시작(필요 시 PyYAML 단일 의존), `before-final` hook은 Windows에서 `.ps1`/`.cmd` 1줄 shim → `python run.py` 호출. (상세 근거는 `CHANGELOG.md` v0.2.0 진입 항목 참조)

### T-B2 — runner CLI 구현
- **산출물**: `4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/run.*` (선정 언어의 확장자)
- **Acceptance Criteria**:
  - structured AC YAML 블록 파싱 (없으면 명확한 에러로 종료, exit ≠ 0).
  - 3종 method 실행 (`command`, `file_exists`, `manual`).
  - `NPI_Verification.md`의 AC ↔ Verification 표를 채워서 출력.
  - 모든 Pass 행에 증거 존재; 아니면 exit ≠ 0.
  - 두 번 연속 실행 시 결정적(deterministic) 결과.
- **Affected Objects**: `Artifact`, `AcceptanceCriterion`, `WorkflowModule`
- **Status**: ✅ completed (2026-05-08)
- **결과 요약**: `verification-runner/run.py` (Python 3.11+, stdlib-only, minimal-subset YAML 자체 파싱) 구현 완료. CLI: `python run.py --brief <path> [--out <path>] [--strict]`. exit code 분리 (0/1/2). 5종 수동 검증 통과 — Pass 케이스 (3 AC 전체 Pass, exit 0), schema_version 누락 (exit 2), 미지원 schema_version `"9.9.9"` (exit 2), 일부 Fail 혼합 (Pass=1/Fail=2, exit 1), 동일 입력 2회 실행 SHA-256 동일 (결정성 확인). 산출물: `run.py`, `README.md`, `tests/fixture_pass.md`.

### T-B3 — verification-runner skill 정의 작성
- **산출물**: `4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/SKILL.md`
- **Acceptance Criteria**:
  - skill의 트리거 / 입력 / 출력 / AC 명시.
  - runner 호출 절차 표준화.
  - subagent 형태로 실행할 조건 명시 (AC 개수 임계, context 오염 우려).
- **Affected Objects**: `Template`, `WorkflowModule`
- **Status**: ✅ completed (2026-05-08)
- **결정 요약**: SKILL.md 11개 섹션(Purpose / When / Inputs / Outputs / Procedure / Context / Subagent / Invocation / Failure / Anti-patterns / History) 작성. skill 은 검증 로직 0줄, runner = single source of truth. subagent 모드 임계 5개 명시(AC≥8 / command비율≥1/3 / 단일명령 출력량 多 / 재호출 / 사용자 요청). `skill-candidates.md` 의 `verification-runner` 항목을 implemented 로 격상.

### T-B4 — before-final hook 구현
- **산출물**: `4_Task_Level_Execution_Templates/claude-code/hooks/before-final.*` + `settings.json` 등록 명세
- **Acceptance Criteria**:
  - Final Control Point 직전에 runner 호출.
  - runner exit ≠ 0이면 차단 + actionable 메시지.
  - should-block / should-pass 단위 테스트 케이스 1개씩 통과.
- **Affected Objects**: `ControlPoint`, `WorkflowModule`
- **Status**: ✅ completed (2026-05-08)
- **결정 요약**: PowerShell shim `before-final.ps1` (한글 주석/한글 README 포함, 런타임 메시지 ASCII-only) + Windows cmd wrapper `before-final.cmd` (ASCII-only — cp949 파싱 함정 회피) 작성. hook 검증 로직 0줄, runner exit code 0/1/2 passthrough. 회귀용 `fixture_block.md` 추가. 검증: PS shim 3 케이스 (pass/block/parse-error) + cmd wrapper 4 케이스 (pass/block/-Strict forwarding/usage) 모두 정확한 exit code. settings.json 등록 명세는 hooks/README.md §"Claude Code settings.json 등록 예시" 에 박제.

### T-B5 — NPI_Brief.md 템플릿 갱신
- **산출물**: `4_Task_Level_Execution_Templates/NPI_Brief.md` 수정
- **Acceptance Criteria**:
  - structured AC YAML 블록 섹션이 required로 명시됨.
  - prose AC 표는 유지 (dual-form).
  - 예시 블록 1개가 템플릿에 포함됨.
- **Affected Objects**: `Template`, `AcceptanceCriterion`

### T-B6 — validate-output 명령 본문 갱신
- **산출물**: `4_Task_Level_Execution_Templates/claude-code/commands/validate-output.md` 수정
- **Acceptance Criteria**:
  - "절차" 섹션이 markdown 절차에서 "skill/subagent를 통해 runner를 호출한다"로 갱신.
  - 사용자가 직접 runner를 invoke할 수 있는 한 줄 명령도 함께 명시.
- **Affected Objects**: `WorkflowModule`
- **Status**: ✅ completed (2026-05-08)
- **결정 요약**: validate-output.md 를 v0.1.0 수동 절차 → v0.2.0 "skill ↔ runner ↔ hook 3계층 호출" 모델로 전면 재정의. runner = single source of truth 명시. 직접 실행 (Python runner) + hook 경유 (`.ps1`/`.cmd`) 양쪽 명령 예시 제공. exit code 0/1/2 규칙 / NPI_Verification.md 컬럼 / subagent 권장 조건 5개 / Anti-patterns 6개 박제. 변경 이력 섹션에 v0.1.0→v0.2.0 전환 기록.

### T-B7 — factory.yaml + MANIFEST.md + CHANGELOG.md 갱신
- **산출물**: 세 파일 동시 수정 (+ README.md 도 status 1줄 갱신)
- **Acceptance Criteria**:
  - `factory.version` → `0.2.0`.
  - `harness.claude_code.skills` 와 `hooks`가 `planned` → `implemented`.
  - MANIFEST에 새 파일 인덱싱.
  - CHANGELOG에 v0.2.0 항목.
- **Affected Objects**: `Project`, `Layer`
- **Status**: ✅ completed (2026-05-08)
- **결정 요약**: factory.yaml `factory.version 0.1.0→0.2.0` + `status: frozen` + `frozen_on: 2026-05-08`, `harness.claude_code.skills/hooks: implemented`, `commands_list` 가 객체형으로 확장되어 `validate-output` 만 `implemented (v0.2.0)`, `runner.validate_output.status: implemented` + `self_test` 블록 (6/6 Pass). MANIFEST 11개 파일 인덱싱 (run.py / SKILL.md / verification-runner README / fixture 2종 / before-final.ps1+.cmd / hooks README / validate-output.md / NPI_Brief.md / NPI_Verification.md / B-002 3종 + 1종). CHANGELOG `[Unreleased]` → `[0.2.0] — 2026-05-08` 닫음, Decided/Added/Changed/Released 4섹션. README status 1줄 갱신. **v0.2.0 frozen.**

### T-B8 — schema_version 키 도입 여부 결정
- **산출물**: 결정 기록 (1줄 결정 + 사유)
- **Acceptance Criteria**: YES/NO + 미래 호환성 시나리오에 대한 한 줄 평가.
- **선행 조건**: T-B2 시작 전 (runner가 처음 schema를 마주치기 전).
- **Status**: ✅ completed (2026-05-08)
- **결정 요약**: **YES** — `schema_version` 필드 필수 도입, 초기값 `"0.2.0"`, v0.2.0 runner는 `"0.2.0"`만 지원하며 키 부재·미지원 버전 모두 fail. 이후 AC schema 변경은 Semver. (상세는 `CHANGELOG.md` v0.2.0 진입 항목 참조)

### T-B9 — Self-test (B-002 후속 검증)
- **산출물**: B-002 본 Brief의 AC 6개를 v0.2.0 runner로 다시 검증한 `NPI_Verification.md`.
- **Acceptance Criteria**:
  - runner가 본 Brief의 YAML 블록을 읽어 6개 행을 자동으로 채움.
  - 모든 Pass 행에 증거 존재.
  - manual 행은 confirmer + ISO date로 채워짐.
- **Affected Objects**: `Artifact`, `AcceptanceCriterion`, `ControlPoint`
- **Status**: ✅ completed (2026-05-08)
- **결과 요약**: B-002 Brief 에 `schema_version: "0.2.0"` 1줄 추가 → `before-final.ps1 -Brief B-002_NPI_Brief.md` 실행 → exit 0, total=6 pass=6 fail=0. 산출물 `3_Domain_Project_Playbooks/ai-npi-platform/NPI_Verification.md` (AC-1 file_exists 자동 Pass + AC-2~AC-6 manual 5개 confirmer/date Pass). Factory 가 자기 자신을 검증하는 self-application 성립.

---

## Out-of-Scope 발견 사항
본 B-002 작업 진행 중 **추가로 발견되었으나 절대 흡수하지 않을** 항목들. 이후 별도 Brief로 다룬다.

- L4의 다른 6개 command를 동일한 "실제 동작" 수준으로 진화시키는 작업.
- Worktree 자동 생성/종료 스크립트.
- MCP 연결 정책의 실제 connector 등록.
- 자동 스캐폴딩 CLI (`How_To_Start_New_Project.md`의 자동화).
