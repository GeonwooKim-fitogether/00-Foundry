# B-002 — NPI_Brief

## 식별 정보
- **Playbook**: `ai-npi-platform`
- **Brief ID**: B-002
- **Factory 버전**: 0.1.0 → 0.2.0 (이 작업으로 0.2.0으로 진입 예정)
- **Owner**: 사용자 (Main Agent: factory-foreman)
- **작성일**: 2026-05-07
- **선행 결정**: B-002 Self-test에서 제기된 AC-format Critical Decision 승인 완료 (2026-05-07)

## 목적
v0.1.0에서 markdown 절차서로만 존재하는 `validate-output` command를 v0.2.0에서 **실제로 동작하는 검증 루프**로 진화시킨다. 이를 위한 전제 조건인 **structured Acceptance Criteria 블록**을 `NPI_Brief.md` 템플릿에 도입한다.

## 배경
- v0.1.0 Self-test(B-002)에서 Factory가 자기 자신을 대상으로 `scope-context` + `plan-work` 사이클을 무사히 수행할 수 있음을 확인했다.
- 그 과정에서 `validate-output`을 실제 동작 가능한 검증 루프로 만들려면 AC가 사람이 읽는 prose로만 존재해서는 안 되며, **machine-readable** 형태가 필요하다는 결론에 도달했다.
- Critical Decision(L1/01의 4번 트리거: AC 형식 변경)이 발생했고, 사용자 승인을 받았다.
- 현재 v0.1.0에 실제 사용 중인 Brief 인스턴스는 없어, **migration cost는 사실상 0**이다.

## 범위 (In Scope)
- `NPI_Brief.md` 템플릿에 structured AC YAML 블록 형식을 추가한다 (사람이 읽는 prose AC 표는 유지하고 그 옆에 병기).
- v0.2.0 `validate-output` 구현을 위한 **Blueprint**(설계)와 **Worklist**(작업 목록)를 산출한다.
- v0.2.0에서 허용할 verification method 3종(`command`, `file_exists`, `manual`)의 스키마를 정의한다.
- `before-final` hook, `verification-runner` skill, `verification-runner` subagent와 runner의 관계를 명세한다.

## 범위 외 (Out of Scope)
- 실제 runner 스크립트, hook 스크립트, skill package, subagent 정의 파일 작성.
- runner의 host 언어 최종 선정(Blueprint에서 후보만 제시; 최종 결정은 v0.2.0 구현 단계에서 별도 Critical Decision으로 다룬다).
- v0.3.0 이후의 verification method 확장.
- 다른 6개 command의 자동화.
- 다른 hook 후보의 구현.

## Acceptance Criteria

| AC ID | 기준 |
|---|---|
| AC-1 | B-002 산출 3개 파일(`B-002_NPI_Brief.md`, `B-002_NPI_Blueprint.md`, `B-002_NPI_Worklist.md`)이 `3_Domain_Project_Playbooks/ai-npi-platform/` 경로에 존재한다. |
| AC-2 | 본 Brief에 structured AC YAML 블록이 포함되어 있고, 그 블록은 v0.2.0에서 정의될 schema와 동일한 키 구조(`id / statement / method / (command\|path\|manual_confirmer)`)를 사용한다. |
| AC-3 | Blueprint는 runner / hook / skill / subagent 4개 구성 요소의 책임 분담과 호출 관계를 다이어그램 또는 표로 명시한다. |
| AC-4 | Blueprint는 verification method 3종(`command`, `file_exists`, `manual`) 각각에 대해 입력 필드, 통과 조건, 증거 형식을 정의한다. |
| AC-5 | Worklist는 v0.2.0 구현으로 넘기는 항목을 별도 섹션으로 분리하여 명시한다. |
| AC-6 | 본 Brief의 Affected Objects는 `ai-npi-platform/domain-ontology.md`에 실제로 존재하는 Object 이름만 사용한다. |

### Structured AC YAML 블록 (v0.2.0 schema)

```yaml
schema_version: "0.2.0"

acceptance_criteria:
  - id: AC-1
    statement: "B-002 산출 3개 파일이 ai-npi-platform 경로에 존재한다"
    method: file_exists
    paths:
      - 3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Brief.md
      - 3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Blueprint.md
      - 3_Domain_Project_Playbooks/ai-npi-platform/B-002_NPI_Worklist.md

  - id: AC-2
    statement: "본 Brief에 structured AC YAML 블록이 포함되어 있고 v0.2.0 schema와 동일한 키를 사용한다"
    method: manual
    manual_confirmer: factory-foreman
    confirm_date: 2026-05-07

  - id: AC-3
    statement: "Blueprint가 runner/hook/skill/subagent 4개 구성요소의 관계를 표로 명시한다"
    method: manual
    manual_confirmer: factory-foreman
    confirm_date: 2026-05-07

  - id: AC-4
    statement: "Blueprint가 verification method 3종에 대해 입력 필드/통과 조건/증거 형식을 정의한다"
    method: manual
    manual_confirmer: factory-foreman
    confirm_date: 2026-05-07

  - id: AC-5
    statement: "Worklist에 v0.2.0 구현 이관 항목 섹션이 존재한다"
    method: manual
    manual_confirmer: factory-foreman
    confirm_date: 2026-05-07

  - id: AC-6
    statement: "Affected Objects가 ai-npi-platform/domain-ontology.md의 실제 Object만 사용한다"
    method: manual
    manual_confirmer: factory-foreman
    confirm_date: 2026-05-07
```

> 참고: 본 YAML 블록은 v0.2.0 runner (`verification-runner/run.py`) 가 그대로 파싱한다. T-B9 Self-test (2026-05-08) 에서 본 Brief 를 입력으로 hook → runner 가 실행되어 6개 AC 가 모두 Pass 함을 확인했다.

## Affected Objects
`3_Domain_Project_Playbooks/ai-npi-platform/domain-ontology.md`의 Core Objects에서 인용:

```
Affected Objects:
- Template
- Artifact
- AcceptanceCriterion
- ControlPoint
- WorkflowModule
```

각 Object에 미치는 영향:
- **Template**: `NPI_Brief.md`에 structured AC YAML 블록이라는 새 required section이 추가됨 (v0.2.0).
- **Artifact**: `NPI_Verification.md`가 향후 runner가 자동 채우는 산출물이 됨.
- **AcceptanceCriterion**: prose-only에서 dual-form(prose + YAML)으로 진화.
- **ControlPoint**: Final Control Point가 v0.2.0부터 자동 게이트(`before-final` hook)로 강화됨.
- **WorkflowModule**: `06_verification`이 실행 가능한 backing을 갖게 됨.

## Control Point 판단

| 트리거 (L1/01) | 발생 여부 | 비고 |
|---|---|---|
| 되돌리기 어려운 변경 | 부분적 | Template 변경은 되돌릴 수 있으나, 도입 후 작성될 Brief들은 새 형식을 따르게 됨. 현재 wild에 인스턴스가 없어 실제 비용 0. |
| 의미 있는 스코프/예산/일정 변경 | 아니오 | v0.2.0 범위 내. |
| 리스크 등급 상향 | 아니오 | 새로 등록된 High 리스크 없음. |
| **Acceptance Criteria 변경** | **예** | AC가 진술되는 형식이 prose → dual-form으로 바뀜. |

**Critical Decision 처리 결과**: 사용자 승인 완료 (2026-05-07). 본 Brief 작성은 그 승인을 전제로 진행되었다. 추가 Human Control Point는 v0.2.0 구현 단계에서 **runner host 언어 선정**(Blueprint §리스크 R-언어 참조) 시점에 한 번 더 발생할 수 있다.

## 위험 (preliminary)
상세는 Blueprint §리스크에서 다룬다. 본 Brief 단계의 핵심 우려:
- v0.2.0 schema가 v0.3.0 이후 method 확장 시 깨질 가능성 (스키마 버전 키 도입으로 대비).
- manual method가 "fake pass" 통로가 될 위험 (manual_confirmer + ISO date 강제로 차단).

## 변경 이력
- 2026-05-07 — 초안 작성 (B-002 Self-test 승인 직후).
- 2026-05-07 — B-002 Final Control Point 통과. manual AC confirm_date 확정.
