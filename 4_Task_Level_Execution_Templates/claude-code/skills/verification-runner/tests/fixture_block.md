# Fixture Brief — verification-runner / before-final hook 자가 점검 (Block 케이스)

> 본 파일은 runner 와 `before-final` hook 이 **AC 실패를 정확히 차단** 함을 자가 점검하기 위한 fixture 다.
> 의도적으로 Fail 하도록 설계되어 있으며, runner / hook 모두 **exit 1** 을 반환해야 한다.

## Acceptance Criteria *(필수, dual-form)*

### A. Prose / Table

| AC ID | Criterion |
|---|---|
| AC-FAIL-FILE | 의도적 Fail: 존재하지 않는 파일 경로 |
| AC-FAIL-MANUAL | 의도적 Fail: confirm_date 가 ISO 8601 형식이 아님 |

### B. Structured AC (YAML) *(필수)*

```yaml
schema_version: "0.2.0"

acceptance_criteria:
  - id: AC-FAIL-FILE
    statement: "의도적 Fail — 존재하지 않는 파일은 file_exists 가 차단해야 한다"
    method: file_exists
    paths:
      - this-path-definitely-does-not-exist-xyz.txt

  - id: AC-FAIL-MANUAL
    statement: "의도적 Fail — confirm_date 형식 불일치는 manual fake-pass 차단으로 잡혀야 한다"
    method: manual
    manual_confirmer: tester
    confirm_date: not-a-date
```

## Affected Objects *(필수, structured)*

```
Affected Objects:
- Artifact
```
