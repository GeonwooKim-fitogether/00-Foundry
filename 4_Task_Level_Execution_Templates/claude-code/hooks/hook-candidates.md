# Hook Candidates (v0.1.0 base — v0.2.0 부분 implemented)

| Hook | Status | Category | Event | Behavior | Package |
|---|---|---|---|---|---|
| `on-context-expansion` | candidate | Gate | Before reading additional files beyond the current scope allowlist | Require an explicit reason; block if the reason isn't tied to current AC | — |
| **`before-final`** | **implemented (v0.2.0, 2026-05-08)** | Verify | Before declaring Final Control Point | runner (`run.py`) 를 호출해 모든 AC 가 evidence 와 함께 Pass 인지 확인. Fail/parse-error 면 차단 (exit 1/2). hook 자체는 검증 로직 0줄 — runner 호출 + exit code passthrough 만. | `before-final.ps1`, `before-final.cmd` |
| `after-code-change` | candidate | Verify | After file edit / write | Suggest or run candidate test / typecheck commands; surface failures | — |
| `on-critical-decision` | candidate | Alert | When `review-risk` flags a trigger | Emit alert; produce skeleton for `ask-chatgpt-decision` package | — |
| `before-dangerous-action` | candidate | Gate | Before delete, deploy, DB migration, or cost-incurring operation | Block until Human Control Point passes | — |
| `after-task-complete` | candidate | Verify | After Final Control Point passes | Generate candidate lessons-learned draft for `extract-lessons` | — |

## Mapping to Doctrine
- `on-context-expansion` enforces **Context Isolation Policy**.
- `before-final` enforces **ACDE** (no done without verified AC).
- `before-dangerous-action` enforces **Minimum Human Intervention** (Critical only).
- `on-critical-decision` is the bridge between automated execution and human/ChatGPT escalation.

## v0.2.0 Hook Implementation Status
- `before-final` 가 첫 implemented hook. should-pass / should-block / parse-error 3 케이스 수동 검증 통과 (T-B4, 2026-05-08).
- 다른 5개 hook 은 여전히 candidate. 각각 별도 Brief 를 통해 implemented 로 격상한다.

## Acceptance Criteria for Hook Implementation (v0.2.0 standard)
- Hook 은 검증 로직을 가지지 않는다. 외부 도구(runner 등)를 호출하는 얇은 shim 이어야 한다.
- block 시 non-zero exit + actionable 메시지.
- should-block / should-pass 단위 테스트 1쌍 이상 통과.
- `settings.json` 등록 명세를 README 에 명시.
- Windows 환경에서 cmd shim 은 ASCII-only (cp949 파싱 함정 회피).
