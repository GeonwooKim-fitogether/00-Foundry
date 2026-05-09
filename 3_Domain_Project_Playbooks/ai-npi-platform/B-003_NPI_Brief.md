# B-003 — NPI_Brief — Foundry v0.2.1 운영정책 candidate 검증

## 식별 정보
- **Playbook**: `ai-npi-platform`
- **Brief ID**: B-003
- **Factory 버전**: v0.2.0 (frozen) → v0.2.1 candidate
- **Owner**: 사용자 + factory-foreman (Claude)
- **작성일**: 2026-05-08

## 목적
Foundry v0.2.1 운영정책 candidate 의 9 신규 문서 + 3 갱신 파일이 정확한 위치에 존재함을 *코드 변경 0* 단위로 검증한다.
본 Brief 의 통과 = v0.2.1 candidate 의 *문서 산출물* 정합성 확인. *frozen 격상* 은 별도 Meta Sprint 에서 결정.

## 범위 (In Scope)
- 9 신규 문서 (L1 4 + L2 3 + L4 2) 의 존재 + 비어있지 않음 검증.
- CHANGELOG.md 에 v0.2.1 표기 존재 검증.
- 본 Brief 자체의 v0.2.0 dual-form AC schema 준수.

## 범위 외 (Out of Scope)
- v0.2.1 의 *frozen 격상* (Meta Sprint 후 결정).
- runner / hook / skill 코드 변경 (본 candidate 는 정책 변경이며 코드 0).
- B-002 self-test 의 재실행 (코드 변경 0이므로 회귀 위험 없음).

## Acceptance Criteria

| AC ID | 기준 |
|---|---|
| AC-1 | `1_Universal_Operating_Principles/GitHub_Foundry_관리정책.md` 존재 + 비어있지 않음. |
| AC-2 | `2_Reusable_Workflow_Modules/신규_프로젝트_생성_Workflow.md` 존재 + 비어있지 않음. |
| AC-3 | `4_Task_Level_Execution_Templates/프로젝트_meta_폴더_템플릿.md` 존재 + 비어있지 않음. |
| AC-4 | `4_Task_Level_Execution_Templates/factory_yaml_template.md` 존재 + 비어있지 않음. |
| AC-5 | `2_Reusable_Workflow_Modules/Decision_Queue_운영방식.md` 존재 + 비어있지 않음. |
| AC-6 | `2_Reusable_Workflow_Modules/Meta_Sprint_Backport_Workflow.md` 존재 + 비어있지 않음. |
| AC-7 | `CHANGELOG.md` 에 `v0.2.1` 문자열 존재 (cross-platform Python 검증). |
| AC-8 | `README.md` 에 `v0.2.1` 문자열 존재 (status 라인에 candidate 표기). |
| AC-9 | `MANIFEST.md` 에 `v0.2.1` 문자열 존재 (인덱스에 candidate 항목 표기). |

### Structured AC YAML 블록

```yaml
schema_version: "0.2.0"

acceptance_criteria:
  - id: AC-1
    statement: "GitHub Foundry 관리정책 존재"
    method: file_exists
    paths:
      - 1_Universal_Operating_Principles/GitHub_Foundry_관리정책.md
    must_be_nonempty: true

  - id: AC-2
    statement: "신규 프로젝트 생성 Workflow 존재"
    method: file_exists
    paths:
      - 2_Reusable_Workflow_Modules/신규_프로젝트_생성_Workflow.md
    must_be_nonempty: true

  - id: AC-3
    statement: "프로젝트 meta 폴더 템플릿 존재"
    method: file_exists
    paths:
      - 4_Task_Level_Execution_Templates/프로젝트_meta_폴더_템플릿.md
    must_be_nonempty: true

  - id: AC-4
    statement: "factory.yaml template 존재"
    method: file_exists
    paths:
      - 4_Task_Level_Execution_Templates/factory_yaml_template.md
    must_be_nonempty: true

  - id: AC-5
    statement: "Decision Queue 운영방식 존재"
    method: file_exists
    paths:
      - 2_Reusable_Workflow_Modules/Decision_Queue_운영방식.md
    must_be_nonempty: true

  - id: AC-6
    statement: "Meta Sprint Backport Workflow 존재"
    method: file_exists
    paths:
      - 2_Reusable_Workflow_Modules/Meta_Sprint_Backport_Workflow.md
    must_be_nonempty: true

  - id: AC-7
    statement: "CHANGELOG에 v0.2.1 존재 (cross-platform Python 검증)"
    method: command
    # 사용자 spec 의도: grep -q 'v0.2.1' CHANGELOG.md
    # cross-platform 채택 — Foundry 가 다중 머신/OS 환경에서 사용될 수 있으므로 Python 으로 통일
    # (runner host 가 Python 3.11+ 이므로 추가 의존성 0).
    # 양성 → exit 0, 음성 → exit 1 (grep -q 동일 semantics).
    command: python -c "import sys, pathlib; sys.exit(0 if 'v0.2.1' in pathlib.Path('CHANGELOG.md').read_text(encoding='utf-8') else 1)"
    expect_exit: 0

  - id: AC-8
    statement: "README에 v0.2.1 존재 (cross-platform Python 검증)"
    method: command
    command: python -c "import sys, pathlib; sys.exit(0 if 'v0.2.1' in pathlib.Path('README.md').read_text(encoding='utf-8') else 1)"
    expect_exit: 0

  - id: AC-9
    statement: "MANIFEST에 v0.2.1 존재 (cross-platform Python 검증)"
    method: command
    command: python -c "import sys, pathlib; sys.exit(0 if 'v0.2.1' in pathlib.Path('MANIFEST.md').read_text(encoding='utf-8') else 1)"
    expect_exit: 0
```

## Affected Objects

```
Affected Objects:
- Layer
- WorkflowModule
- Template
- Project
- AcceptanceCriterion
```

각 Object 영향:
- **Layer**: L1 / L2 / L4 에 9 신규 파일 추가.
- **WorkflowModule**: L2 에 3 신규 workflow 추가.
- **Template**: L4 에 2 신규 template 추가.
- **Project**: 신규 프로젝트의 factory.yaml + meta/ 의무화.
- **AcceptanceCriterion**: 본 Brief 가 첫 `command` method 사용 사례 (이전 B-002 는 file_exists+manual 만).

## Control Point 판단

| 트리거 | 발생 여부 | 비고 |
|---|---|---|
| 되돌리기 어려운 변경 | 아니오 | 정책 문서 add only. 폐기 시 9 파일 삭제로 회복 가능. |
| 의미 있는 스코프 변경 | **부분** | Foundry 운영 모델이 단일 머신·단발 → 다중 머신·다중 프로젝트로 진화. 단 코드 0 변경. |
| 리스크 등급 상향 | 아니오 | 정책은 *위험 완화* 방향 (잘못된 즉시 반영 차단). |
| AC 변경 | 아니오 | 기존 Brief 들의 AC schema 그대로 유지 (`schema_version: "0.2.0"`). |

→ **Critical Decision 은 v0.2.1 candidate → frozen 격상 시점** 에 Meta Sprint 입력으로 발생. 본 Brief 는 *문서 산출물 검증* 만 다룬다.

## 변경 이력
- 2026-05-08 — 초안. 7 AC 박제. v0.2.1 candidate 의 첫 검증용 Brief.
