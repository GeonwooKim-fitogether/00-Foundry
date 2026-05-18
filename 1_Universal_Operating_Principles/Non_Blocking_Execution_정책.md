# L1 Principle — Non-Blocking Execution 정책

> **Layer**: 1 — Universal Operating Principles (invariant).
> **상태**: v0.2.1 candidate (2026-05-08 도입).
> 본 정책은 [Human_Control_Point_정책.md](./Human_Control_Point_정책.md) 와 한 쌍.
> 둘을 합쳐 *언제 멈추고 언제 계속할지* 의 단일 결정 기준을 형성한다.

## 1. 핵심 명제
**Claude Code 는 작은 결정마다 멈추지 않는다.**
- 되돌릴 수 있는 결정은 Claude 가 진행한다.
- 애매하지만 치명적이지 않은 결정은 `meta/decision-queue.md` 에 기록하고 계속 진행한다.
- Human Control Point 트리거가 *아닌 한* 실행을 지속한다.

## 2. 실행 분류 매트릭스

| 결정의 성격 | 되돌리기 비용 | 영향 범위 | 행동 |
|---|---|---|---|
| 명백히 옳은 것 (lint, naming, 작은 정리) | 낮음 | 좁음 | Claude 가 즉시 실행, 기록 불필요 |
| 애매하지만 일반적 베스트 프랙티스 있음 | 낮음 | 좁음 | Claude 가 베스트 프랙티스 채택 + decision-queue 기록 |
| 애매하고 트레이드오프 있음 | 낮음~중 | 좁음~중 | Claude 가 *기본값* 채택 + decision-queue 기록 + Final Review 까지 보류 |
| 애매하고 비용 / 보안 / 데이터 / 아키텍처 영향 큼 | 중~높음 | 넓음 | **Human Control Point Escalation** ([Human_Control_Point_정책 §2](./Human_Control_Point_정책.md#2-human-control-point-escalation-트리거-하나라도-해당하면-즉시-escalation)) |

## 3. Default Action 패턴
Claude 가 즉시 결정할 때는 *기본값* 을 명확히 채택한다. 기본값 선택 우선순위:

1. **00-Foundry 의 명시적 룰** (L1/L2/L4 문서) → 그대로 따른다.
2. **현재 프로젝트의 `factory.yaml` 설정** → 그대로 따른다.
3. **언어/프레임워크의 일반적 관용** (예: TypeScript strict, Python PEP-8, React naming convention) → 그대로 따른다.
4. **본인 (Claude) 의 일관된 판단** — 같은 상황에서 다른 답을 내지 않도록 단일 패턴 유지.

기본값 채택은 *모두* `meta/decision-queue.md` 에 1행으로 기록 (사후 검토 가능하게).

## 4. decision-queue 와의 관계
- queue 는 *blocker 가 아니다.* 작업 진행 중에는 *기록 후 계속 진행*.
- queue 항목은 [Final Review](#) (cycle 종료 시) 또는 [Meta Sprint](../2_Reusable_Workflow_Modules/Meta_Sprint_Backport_Workflow.md) 에서 일괄 검토.
- 검토 결과 잘못된 결정으로 판명되면 *그때 되돌린다* (애초에 "되돌릴 수 있는" 만 queue 에 들어갔다).
- 자세한 운영: [Decision_Queue_운영방식.md](../2_Reusable_Workflow_Modules/Decision_Queue_운영방식.md).

## 5. ChatGPT 호출 절제
본 정책의 *부수 효과* 중 가장 중요한 것: **ChatGPT 같은 외부 동반자에 작은 결정마다 묻지 않는다.**
- 외부 호출은 비싸고 느리다 (지연·비용·context overhead).
- 작은 결정은 Claude 가 *자체적으로* 결정 → queue 에 기록 → cycle 종료 시 *묶음* 으로만 ChatGPT 검토.
- 자세한 절제 정책: [Copy_Paste_Zero_로드맵.md](./Copy_Paste_Zero_로드맵.md) §"ChatGPT 사용 시점".

## 6. 위반 신호
- Claude 가 진행 도중 한 cycle 안에서 사용자에게 5회 이상 짧은 결정 요청.
- decision-queue.md 가 비어 있는데 cycle 진행이 잦은 멈춤.
- 사용자가 "그냥 진행해" 같은 응답을 반복.
- ChatGPT 호출이 cycle 1회당 ≥ 3회 (Start / Critical / Final 외에).

→ Claude 의 분류 매트릭스 (§2) 가 너무 보수적. 비차단 분류로 재조정.

## 7. 한계 / 안전장치
본 정책이 *지나친 자율성* 을 의미하지 않는다. 다음은 항상 사람 대상:
- Human Control Point 10개 트리거 ([Human_Control_Point_정책 §2](./Human_Control_Point_정책.md#2-human-control-point-escalation-트리거-하나라도-해당하면-즉시-escalation)).
- Critical Decision (L1/01의 4가지: 되돌리기 어려운 변경 / 의미 있는 스코프-예산-일정 변경 / 리스크 등급 상향 / AC 변경).
- 파괴적 명령 (DB drop, force push, 본 정책서 §"Executing actions with care").

## 8. Next cycle 선택의 비차단 (v0.3.0 amendment, D-025)

Stage 2 reduced-copy mode (Operating Model v0.3+) 의 자연 연장: **next cycle 의 선택 자체도 Implementer 자율 default**.

- non-HCP scope 내 다음 작업 단위 진입 = Director Card 발급 0. Implementer 가 자율 진입.
- HCP gate / Final CP / scope drift 만 Director Card.
- 우선순위 휴리스틱 (동등 후보일 때만 적용): `deferred 제외` > `Foundry backport` > `planning draft` > `follow-up` > `HCP-only 카드` (마지막).
- 자세한 표준: [`4_Task_Level_Execution_Templates/Next_Cycle_Selection_Rule.md`](../4_Task_Level_Execution_Templates/Next_Cycle_Selection_Rule.md).
- 본 amendment 는 v0.2.x 일부 cycle 에서 운용되던 **D-017** ("Implementer 가 next-cycle 후보 자발 제시 금지") 를 **폐기**.

## 변경 이력
- v0.2.1 candidate (2026-05-08) — 신설.
- v0.3.0 candidate (2026-05-18) — §8 Next cycle 비차단 추가 (D-025 amendment, source: 12.subscription-payment-saas-platform Phase 1~5).
