# Lessons Learned — `<project-name>`

> 매 cycle 의 Final Control Point 통과 직후 작성.
> 본 프로젝트 *내부* 의 회고 (다음 cycle 이 더 잘 되기 위함).
> Foundry 측 개선 후보는 본 문서가 아닌 [foundry-improvement-log.md](./foundry-improvement-log.md) 에.

## 작성 규칙
- cycle 별로 *keep / change / drop* 1줄씩 (3줄). 길이 제한.
- 추상적 다짐 금지 ("더 잘하겠다" → ❌). 구체적 행동 변화 ("X 시작 전에 Y 를 한다" → ✅).
- 중복 / 모호 항목은 다음 cycle 이전에 통합 / 폐기.

## 항목 형식

```markdown
### Cycle: <cycle-id> (<YYYY-MM-DD>)
- **Keep**: 잘 작동한 행동 / 패턴 (한 줄, 다음 cycle 에서도 반복).
- **Change**: 다음 cycle 에서 *행동 변화* 가 필요한 항목 (한 줄, 무엇을 어떻게 다르게 할지).
- **Drop**: 멈출 행동 / 폐기할 패턴 (한 줄).
- **(선택) Foundry 후보**: 본 cycle 에서 발견한 Foundry 개선 단서 → `foundry-improvement-log.md#FIL-NNN` 으로 박제한 것 1~N 개.
```

## 누적 회고 (이 아래에 cycle 별로 추가)

### Cycle: Bootstrap (YYYY-MM-DD)
- **Keep**: …
- **Change**: …
- **Drop**: …
- **(선택) Foundry 후보**: …
