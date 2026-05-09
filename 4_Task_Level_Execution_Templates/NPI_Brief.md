# NPI_Brief — <task or project name>

> Template (v0.2.0). 필수 섹션: **Acceptance Criteria** (dual-form), **Structured AC (YAML)**, **Affected Objects**.
> 본 템플릿은 사람이 읽는 형식과 `verification-runner` (v0.2.0+) 가 기계적으로 읽는 형식을 *동시에* 담는다.

## 정체성 (Identity)
- **Project / Playbook**: <name>
- **Version**: <semver>
- **Owner**: <name or role>
- **Date**: <YYYY-MM-DD>

## 문제 (Problem)
한 단락. 누가, 어떤 통증을, 왜 지금, 그리고 *이 문제 정의가 틀렸음을 증명할 수 있는 신호*(falsification)는 무엇인가.

## 목표 (Goal)
성공한 모습이 평이한 언어로 어떻게 보이는가.

## 범위 (In Scope)
- …

## 제외 범위 (Out of Scope)
- …

## Acceptance Criteria *(필수, dual-form)*

본 섹션은 **두 형식을 병기**한다. 둘은 서로 *동일한* AC를 다르게 표현한 것이며, 변경 시 **반드시 함께 갱신**되어야 한다.

- **A. Prose / Table 형식** — 사람이 읽고 토론하기 위한 표현. Given-When-Then 권장.
- **B. Structured AC (YAML)** — `verification-runner` 가 파싱하는 단일 source of truth. 누락 시 runner는 즉시 fail.

### A. Prose / Table

| AC ID | Criterion |
|---|---|
| AC-1 | Given …, When …, Then … |
| AC-2 | … |
| AC-3 | … |

### B. Structured AC (YAML) *(필수)*

> **규칙**
> - 최상위 `schema_version` 키는 **필수**. v0.2.0에서는 `"0.2.0"` 만 지원한다. 누락·미지원 버전은 runner가 fail 처리한다.
> - 최상위 `acceptance_criteria` 는 AC 항목의 배열이며 **하나 이상** 이어야 한다.
> - 각 AC 항목은 최소 `id`, `statement`, `method` 3개 필드를 가진다.
> - `method` 는 v0.2.0에서 다음 3개만 허용: `command` | `file_exists` | `manual`.
> - `manual` method는 `manual_confirmer` 와 `confirm_date` (ISO 8601 `YYYY-MM-DD`) 두 필드를 **필수**로 가진다. 둘 중 하나라도 비면 runner는 즉시 fail (fake pass 차단).
> - 위 표(A)의 각 `AC ID` 는 본 YAML 블록의 `id` 와 1:1로 매칭되어야 한다.

```yaml
schema_version: "0.2.0"

acceptance_criteria:
  # 예시 1) command method — 외부 명령의 exit code 로 판정
  - id: AC-1
    statement: "단위 테스트 스위트가 모두 통과한다"
    method: command
    command: "npm test --silent"
    workdir: "."          # 선택, 기본 = Brief 위치 기준 프로젝트 루트
    expect_exit: 0        # 선택, 기본 0

  # 예시 2) file_exists method — 산출물 파일/경로의 존재로 판정
  - id: AC-2
    statement: "Blueprint 와 Worklist 두 산출물이 지정 경로에 생성되어 있다"
    method: file_exists
    paths:
      - 3_Domain_Project_Playbooks/<playbook>/<task>_NPI_Blueprint.md
      - 3_Domain_Project_Playbooks/<playbook>/<task>_NPI_Worklist.md
    must_be_nonempty: false   # 선택, 기본 false. true 이면 빈 파일도 fail.

  # 예시 3) manual method — 사람이 직접 확인했음을 명시적 흔적으로 박제
  - id: AC-3
    statement: "Affected Objects 가 도메인 온톨로지의 실제 Object 이름만 사용한다"
    method: manual
    manual_confirmer: <role-or-name>     # 필수
    confirm_date: <YYYY-MM-DD>           # 필수, ISO 8601
    note: "확인 근거 한 줄 (선택)"
```

## Affected Objects *(필수, structured)*

본 Playbook 의 `domain-ontology.md` 에 실재하는 **PascalCase Object 이름만** 사용한다.

```
Affected Objects:
- ObjectA
- ObjectB
```

## 리스크 (예비, Risks — preliminary)
- …

## 비고 (Notes)
실행자가 알아야 할 맥락 중 위 섹션에서 다루지 않은 것.

## History
- <date> — initial draft
- <date> — AC change (Critical Decision; reason: …)
