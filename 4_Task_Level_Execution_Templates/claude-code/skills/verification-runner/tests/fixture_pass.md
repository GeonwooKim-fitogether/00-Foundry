# Fixture Brief — verification-runner 자가 점검 (Pass 케이스)

> 본 파일은 `verification-runner/run.py` 가 정상 동작함을 자가 점검하기 위한 **테스트용 Brief** 이다.
> 모든 AC 가 Pass 하도록 설계되어 있으며, runner 가 exit 0 을 반환해야 한다.

## Identity
- Project: verification-runner self-test
- Date: 2026-05-08

## Acceptance Criteria *(필수, dual-form)*

### A. Prose / Table

| AC ID | Criterion |
|---|---|
| AC-1 | command method: `python --version` 이 exit 0 으로 종료한다 |
| AC-2 | file_exists method: factory.yaml 과 PRD.md 가 프로젝트 루트에 존재한다 |
| AC-3 | manual method: 본 fixture 는 사람이 한 번 검토했다 |

### B. Structured AC (YAML) *(필수)*

```yaml
schema_version: "0.2.0"

acceptance_criteria:
  - id: AC-1
    statement: "command method 가 exit 0 명령에 대해 Pass 를 반환한다"
    method: command
    command: "python --version"
    workdir: "."
    expect_exit: 0

  - id: AC-2
    statement: "file_exists method 가 실재 파일에 대해 Pass 를 반환한다"
    method: file_exists
    paths:
      - factory.yaml
      - PRD.md
    must_be_nonempty: true

  - id: AC-3
    statement: "manual method 가 두 필수 필드 충족 시 Pass 를 반환한다"
    method: manual
    manual_confirmer: factory-foreman
    confirm_date: 2026-05-08
    note: "self-test fixture 검토 완료"
```

## Affected Objects *(필수, structured)*

```
Affected Objects:
- Artifact
```
