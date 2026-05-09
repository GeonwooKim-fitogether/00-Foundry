# B-002 — NPI_Blueprint

## 참조
- Source Brief: `3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Brief.md`
- AC 적용 범위: AC-1 ~ AC-6 (Brief의 모든 AC 항목)
- 대상 Command: `4_Task_Level_Execution_Templates/claude-code/commands/validate-output.md`
- 대상 Module: `2_Reusable_Workflow_Modules/06_verification/`
- 대상 Template: `4_Task_Level_Execution_Templates/NPI_Brief.md`, `NPI_Verification.md`

## v0.2.0 validate-output 구현 방향

### 한 문단 요약
v0.2.0의 `validate-output`은 **세 가지 작은 구성 요소의 합**으로 만든다. (1) Brief의 structured AC YAML 블록을 읽어 verification method를 실행하고 `NPI_Verification.md`의 AC ↔ Verification 표를 채우는 **runner**, (2) runner를 호출하고 미충족 시 Final Control Point를 차단하는 **`before-final` hook**, (3) AC 개수가 많거나 main context를 오염시킬 우려가 있을 때 runner를 격리 실행해 decision-ready summary만 main agent에 반환하는 **`verification-runner` skill / subagent**. runner가 단일 source of truth이며 hook과 skill은 얇은 호출 계층이다.

## runner / hook / skill / subagent 관계

| 구성 요소 | 종류 | 책임 | 입력 | 출력 |
|---|---|---|---|---|
| **runner** | 실행 가능 스크립트 (CLI) | structured AC 파싱, 3종 method 실행, 증거 수집, 매핑 표 작성, exit code 반환 | Brief 경로, (옵션) 출력 경로 | `NPI_Verification.md`, exit code (0 = 전체 Pass + 증거 완비, 그 외 = 차단) |
| **`before-final` hook** | thin shim | Final Control Point 직전 runner 호출, 차단 메시지 사용자에게 노출 | 현재 작업 컨텍스트 | 통과/차단 신호 |
| **`verification-runner` skill** | 재사용 가능 패키지 | runner 호출을 표준 절차로 묶음, 호출 전후 점검 | Brief 경로 | runner 결과 + 요약 |
| **`verification-runner` subagent** | context-isolated 실행 컨테이너 | AC 수가 많을 때 main context 보호, 결과를 decision-ready summary로 반환 | 좁힌 path 화이트리스트 + AC 목록 | 1단락 요약 + Pass/Fail 카운트 + 매핑 표 링크 |

### 호출 관계도 (텍스트)
```
사용자 / Main Agent
        │
        ▼
   /validate-output  ← (Command)
        │
        ▼
 verification-runner skill   ────► (옵션) verification-runner subagent
        │                              │
        ▼                              ▼
       runner (CLI) ◄─── 동일한 runner 호출 ───┘
        │
        │ 읽기: NPI_Brief.md (structured AC block)
        │ 쓰기: NPI_Verification.md
        ▼
   exit 0 / non-zero
        ▲
        │
   before-final hook (Final Control Point 차단/통과 결정)
```

핵심 원칙: **runner만이 검증 로직을 가진다.** hook/skill/subagent는 호출/격리/요약만 담당한다.

## AC schema 초안

### 위치
`NPI_Brief.md` 안의 fenced YAML 블록. prose AC 표는 그대로 유지하고 그 아래에 병기한다.

### 최상위 키
```yaml
acceptance_criteria:        # 리스트
  - id: ...                 # 필수
    statement: ...          # 필수, prose AC와 의미 일치
    method: ...             # 필수, [command | file_exists | manual] 중 하나
    # 이하 method별 추가 필드
```

### 공통 규칙
- `id`는 prose AC 표의 ID와 1:1로 일치한다(`AC-1`, `AC-2`, …).
- `statement`는 측정 가능·검증 가능 원칙을 따른다 (L1/02 ACDE).
- 코드/기능 작업은 `statement`에 Given-When-Then 권장.
- v0.2.0에서 schema 버전 키 `schema_version: 1`을 최상위에 둘지 여부는 구현 단계의 작은 결정으로 미룬다 (Worklist에 항목으로 등록).

## verification method 3종 정의

### 1. `command`
실제 명령을 실행해 exit code로 판정한다.

```yaml
- id: AC-?
  statement: "..."
  method: command
  command: "npm test -- --grep AC-?"
  workdir: "."          # 선택
  expect_exit: 0        # 선택, 기본 0
```

| 항목 | 내용 |
|---|---|
| 입력 필드 | `command` (필수), `workdir` (선택), `expect_exit` (선택, 기본 0) |
| 통과 조건 | 실행 결과 exit code == `expect_exit` |
| 증거 형식 | 명령 문자열 + exit code + stdout/stderr 마지막 N줄 (예: 50줄) |
| 비고 | 셸 차이는 v0.2.0 범위 외. 명령은 그대로 호출하며 host OS 의존성은 사용자 책임. |

### 2. `file_exists`
파일/경로의 존재 여부로 판정한다.

```yaml
- id: AC-?
  statement: "..."
  method: file_exists
  paths:
    - path/to/expected/file.md
    - dist/output.json
  must_be_nonempty: false   # 선택, 기본 false
```

| 항목 | 내용 |
|---|---|
| 입력 필드 | `paths` (필수, 1개 이상), `must_be_nonempty` (선택, 기본 false) |
| 통과 조건 | 모든 `paths` 항목이 존재 (옵션 시 비어있지 않음) |
| 증거 형식 | 각 path별 존재/크기 |

### 3. `manual`
사람이 직접 확인했음을 명시적 흔적으로 남긴다.

```yaml
- id: AC-?
  statement: "..."
  method: manual
  manual_confirmer: factory-foreman
  confirm_date: 2026-05-07
  note: "확인 근거 한 줄"
```

| 항목 | 내용 |
|---|---|
| 입력 필드 | `manual_confirmer` (필수), `confirm_date` (필수, ISO 8601 `YYYY-MM-DD`), `note` (선택) |
| 통과 조건 | 두 필수 필드 모두 채워져 있음 + Final Control Point 시점에 confirmer가 본인임을 인정 |
| 증거 형식 | confirmer + date + note (있으면) |
| 안전장치 | 둘 중 하나라도 비어 있으면 runner는 즉시 Fail 처리 (fake pass 차단). |

## 예상 파일 변경 목록 (v0.2.0 구현 시)

| 경로 | 변경 종류 | 비고 |
|---|---|---|
| `4_Task_Level_Execution_Templates/NPI_Brief.md` | 수정 | structured AC YAML 블록 섹션 추가 (required) |
| `4_Task_Level_Execution_Templates/NPI_Verification.md` | 수정 (소폭) | runner가 채우는 표의 컬럼 명세 명확화 |
| `4_Task_Level_Execution_Templates/claude-code/commands/validate-output.md` | 수정 | "스크립트 호출" 절차로 본문 갱신 |
| `4_Task_Level_Execution_Templates/claude-code/hooks/hook-candidates.md` | 수정 | `before-final` 항목을 candidate에서 implemented로 격상 |
| `4_Task_Level_Execution_Templates/claude-code/hooks/before-final.*` | 신규 | hook 스크립트 (호스트 언어는 v0.2.0 구현 단계에서 결정) |
| `4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/SKILL.md` | 신규 | skill 정의 |
| `4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/run.*` | 신규 | runner 본체 (단일 source of truth) |
| `factory.yaml` | 수정 | `harness.claude_code.skills`/`hooks`를 `planned` → `implemented`로, `factory.version`을 `0.2.0`으로 |
| `MANIFEST.md` | 수정 | runner / hook / skill 신규 항목 인덱싱 |
| `CHANGELOG.md` | 수정 | v0.2.0 항목 추가 |
| `1_Universal_Operating_Principles/02_Quality_and_Safety.md` | 수정 (선택) | "AC는 dual-form" 한 줄 보강 |

## 리스크와 완화책

| ID | 리스크 | 가능성 | 영향 | 완화책 |
|---|---|---|---|---|
| R-언어 | runner host 언어 선정 실수 (이식성·의존성) | 중 | 중 | v0.2.0 구현 시작 시 별도 Critical Decision으로 다룬다. 후보: PowerShell 또는 Bash + Python. 기준: 사용자의 Windows 환경 + 외부 의존성 최소화. |
| R-fakepass | manual method가 "fake pass" 통로가 됨 | 중 | 고 | 두 필수 필드 미충족 시 즉시 Fail. 모든 manual 항목은 verification 결과 요약에서 별도로 카운트되어 가시화. |
| R-스키마이동 | v0.3.0+ method 확장 시 schema 깨짐 | 중 | 중 | 최상위 `schema_version` 키 도입(v0.2.0 구현 단계 소결정). runner는 미지원 버전을 만나면 명확한 에러로 거부. |
| R-OS차이 | `command` method의 OS 의존성 | 중 | 중 | runner는 명령을 그대로 호출. 사용자가 cross-platform 명령 작성 책임. v0.3.0에서 OS-aware 매트릭스 검토. |
| R-도구중복 | runner / hook / skill / subagent 책임 모호화 | 낮음 | 중 | 본 Blueprint의 호출 관계도를 단일 진실로 못박음. runner만 로직, 나머지는 호출/격리/요약. |
| R-자기참조 | Factory 자체가 Brief 형식을 바꾸면서 v0.1.0 인스턴스(B-002 본 Brief)가 새 형식과 충돌 | 매우 낮음 | 낮음 | 본 Brief가 이미 v0.2.0 schema를 미리 준수하도록 작성됨 (마이그레이션 0). |
| R-skill중복 | skill과 subagent 둘 다 verification-runner 이름을 공유 | 낮음 | 낮음 | 의도된 정렬임을 `agent-candidates.md` / `skill-candidates.md`에 이미 명시. 패키지 경로로 구분. |

리스크 완화 후 High 잔여 위험은 없다. **추가 Human Control Point는 v0.2.0 구현 단계의 R-언어 결정 시점에 한 번 발생할 수 있다.**

## AC ↔ Blueprint 커버리지

| AC ID | 본 Blueprint에서 다루는 위치 |
|---|---|
| AC-1 | 본 파일과 자매 파일 2종(Brief/Worklist)이 동일 디렉토리에 생성됨으로써 충족 (Final Control Point에서 `file_exists`로 확인). |
| AC-2 | Brief에 이미 schema 미리보기 YAML이 포함됨. 본 Blueprint §"AC schema 초안"이 동일 키 구조를 정의. |
| AC-3 | §"runner / hook / skill / subagent 관계" 표 + 호출 관계도. |
| AC-4 | §"verification method 3종 정의"의 3개 하위 절. |
| AC-5 | Worklist의 §"v0.2.0 구현 이관 항목" (자매 파일에서 충족). |
| AC-6 | Affected Objects는 Brief에 명시되어 있고, 본 Blueprint §"예상 파일 변경 목록"도 동일 ontology 어휘를 사용. |

## 열린 질문 (v0.2.0 구현 단계로 이관)
1. runner host 언어 (R-언어).
2. `schema_version` 키 도입 여부.
3. `before-final` hook과 runner의 wiring을 `settings.json`으로 할지, 별도 wrapper 스크립트로 할지.
4. subagent 정의 파일 표준 (현재 v0.1.0에는 표준이 없음).
