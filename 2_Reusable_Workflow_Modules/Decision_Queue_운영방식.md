# L2 Workflow — Decision Queue 운영방식

> **Layer**: 2 — Reusable Workflow Module.
> **상태**: v0.2.1 candidate (2026-05-08 도입).
> **선행 원칙**: [Non_Blocking_Execution_정책](../1_Universal_Operating_Principles/Non_Blocking_Execution_정책.md), [Copy_Paste_Zero_로드맵](../1_Universal_Operating_Principles/Copy_Paste_Zero_로드맵.md).

## 1. 핵심 명제
**Decision Queue 는 blocker 가 아니다.**
- queue 항목이 있다고 해서 작업이 멈추지 않는다.
- queue 는 *작은 결정 누적소* — 사후 일괄 검토를 위한 archive.
- 1차 가치: 개발 중 ChatGPT 호출 *최소화*. 누적 후 *묶음* 으로 검토.

## 2. queue 의 위치
각 프로젝트의 `meta/decision-queue.md` 파일.
Foundry 자체에는 *전역 queue 가 없다* — Meta Sprint 시점에 각 프로젝트의 queue 가 *입력* 으로 사용된다.

## 3. 표준 컬럼 (8 필드)

| 컬럼 | 의미 | 예시 |
|---|---|---|
| **ID** | `DQ-NNN` 순차 ID | `DQ-007` |
| **Date** | 결정 발생일 (ISO 8601) | `2026-05-09` |
| **Topic** | 결정 영역 (1~3 단어) | `naming`, `lib-choice`, `ui-microcopy` |
| **Decision Needed** | 어떤 결정이 *필요했는가* (1줄) | "Plan code 를 'PRO' vs 'pro' 어느 케이스로?" |
| **Default Action Taken** | Claude 가 *지금 채택한* 기본값 + 사유 1줄 | "lower_snake = 'pro'. 이유: DB column 관용." |
| **Reversibility** | reversible / partially / irreversible | reversible |
| **Risk** | 낮음 / 중 / 높음 | 낮음 |
| **Review Timing** | 검토 시점 — `Final Review` / `Meta Sprint` / `Next Cycle` | Final Review |

## 4. 항목 형식 (markdown)

```markdown
| DQ-007 | 2026-05-09 | naming | Plan code 를 'PRO' vs 'pro' 어느 케이스로? | lower_snake = 'pro'. DB column 관용. | reversible | 낮음 | Final Review |
```

또는 표 대신 항목식:

```markdown
### DQ-007 — Plan code casing
- **Date**: 2026-05-09
- **Topic**: naming
- **Decision Needed**: Plan code 를 'PRO' vs 'pro' 어느 케이스로?
- **Default Action Taken**: lower_snake = 'pro'. DB column 관용.
- **Reversibility**: reversible
- **Risk**: 낮음
- **Review Timing**: Final Review
```

표 형식은 *조회/필터* 가 쉽고, 항목식은 *맥락 설명* 이 풍부하다. 프로젝트별 1개 형식만 일관되게.

## 5. 기록 시점
다음 모든 경우에 *그 자리에서* queue 에 1행 추가 (별도 승인 없이):
- Claude 가 [Non_Blocking_Execution 분류 매트릭스](../1_Universal_Operating_Principles/Non_Blocking_Execution_정책.md#2-실행-분류-매트릭스) 의 *애매하지만 일반적 베스트 프랙티스 있음* 또는 *애매하고 트레이드오프 있음* 에 해당하는 결정을 *내릴 때*.
- 외부 라이브러리 1개 채택 (작은 utility 수준).
- 코드 스타일의 잿빛 영역 결정.
- TypeScript / Python type 어노테이션의 작은 우회.

다음 경우는 queue 가 *아니다* (별도 처리):
- Human Control Point 트리거 ([10개](../1_Universal_Operating_Principles/Human_Control_Point_정책.md#2-human-control-point-escalation-트리거-하나라도-해당하면-즉시-escalation)) → 즉시 사람.
- Critical Decision (L1/01 4개 트리거) → `decisions.md`.
- Foundry 측 개선 단서 → `foundry-improvement-log.md`.

## 6. 검토 시점 (Review Timing)
queue 항목별 `Review Timing` 필드는 다음 중 하나:

### 6.1 `Final Review` — cycle 종료 직전
- 본 cycle 에 묶이는 작은 결정. cycle 종료 시 1회 검토.
- 잘못된 결정으로 판명되면 *그 자리에서* 되돌리기 (애초에 reversible 만 들어왔다).
- 검토 후 항목별로 *유지 / 되돌림 / Foundry 후보 격상* 표시.
- 검토 결과를 [lessons-learned.md](../4_Task_Level_Execution_Templates/프로젝트_meta_폴더_템플릿.md#lessons-learnedmd) 에 1줄로 반영 (큰 패턴이라면).

### 6.2 `Meta Sprint` — 프로젝트 종료 시
- 본 cycle 의 결정이지만 *다른 cycle 들과 묶어서 패턴* 을 보고 싶을 때.
- [Meta_Sprint_Backport_Workflow](./Meta_Sprint_Backport_Workflow.md) 진입 시 입력으로 사용.

### 6.3 `Next Cycle` — 다음 cycle 시작 직전
- 본 cycle 에서는 결정 후 진행했으나, *다음 cycle 의 시작 가설에* 영향이 있을 때.
- 다음 cycle 의 Brief 작성 시 본 항목 1줄로 가설 점검.

## 7. ChatGPT 호출 절제 (본 workflow 의 1차 가치)
- queue 가 있으면 ChatGPT 호출 *시점* 이 자연스럽게 *cycle 종료 시* 또는 *Meta Sprint* 로 묶인다.
- 묶음 호출은 [Copy_Paste_Zero_로드맵 Stage 2](../1_Universal_Operating_Principles/Copy_Paste_Zero_로드맵.md#3-5단계-로드맵) 의 *Decision Queue 기반 Batch Review* 의 운영 기반.
- 호출 시 [ask-chatgpt-decision.md](../4_Task_Level_Execution_Templates/claude-code/commands/ask-chatgpt-decision.md) 패키지 형식 권장.

## 8. 안티-패턴
- ❌ queue 항목 발생 시 작업 멈춤.
- ❌ Human Control Point 트리거를 queue 에 넣기 (즉시 escalation 이 옳다).
- ❌ Critical Decision 을 queue 에 넣기 (`decisions.md` 가 옳다).
- ❌ queue 가 있는데 cycle 종료 시 검토 없이 closing.
- ❌ ChatGPT 에 queue 항목 1개씩 흩어 호출 (묶음 검토가 본 workflow 의 핵심).

## 9. queue 깊이 신호
- 평균 cycle 당 queue 항목 ≤ 5: 건강. 분류 매트릭스 적정.
- 5 ~ 15: 정상 사용 패턴.
- ≥ 15: cycle 단위가 너무 크거나, [Non_Blocking 분류](../1_Universal_Operating_Principles/Non_Blocking_Execution_정책.md#2-실행-분류-매트릭스) 가 너무 보수적이어서 작은 결정이 과도하게 누적.
- = 0 (cycle 진행 중인데): Claude 가 *내가 결정해야 할 것* 을 사람에게 묻거나 결정 자체를 회피하고 있을 가능성.

## 변경 이력
- v0.2.1 candidate (2026-05-08) — 신설.
