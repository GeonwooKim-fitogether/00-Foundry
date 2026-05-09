# L1 Principle — Copy-Paste Zero 로드맵

> **Layer**: 1 — Universal Operating Principles (invariant 명제 + 진화 로드맵).
> **상태**: v0.2.1 candidate (2026-05-08 도입).
> 본 문서는 Foundry 의 *장기 진화 방향* 을 박제한다. 단기 의사결정은 [Non_Blocking_Execution_정책.md](./Non_Blocking_Execution_정책.md) + [Human_Control_Point_정책.md](./Human_Control_Point_정책.md) 가 좌우한다.

## 1. 핵심 명제 (장기, invariant)
**사람은 Claude Code 와 ChatGPT 사이의 *전달자가 아니라 승인자* 다.**
- 전달자: 두 AI 의 출력물을 손으로 복사·붙여넣어 다른 AI 에게 전하는 사람.
- 승인자: 두 AI 가 *자동으로 주고받은* 결과를 *최종 인정* 하는 사람.

장기 목표는 사람의 일이 *전달* 에서 *승인* 으로 *온전히* 이동하는 것. 이를 *Copy-Paste Zero* 라 부른다.

## 2. 현재 단계 (v0.2.1 candidate, 2026-05-08)
**Stage 1 — 표준화된 수동 질문 패키지** 단계.
- ChatGPT 호출은 *수동* 으로 수행 (사람이 패키지를 복사·붙여넣음).
- 그러나 패키지 *형식* 은 표준화되어 있다 ([ask-chatgpt-decision.md](../4_Task_Level_Execution_Templates/claude-code/commands/ask-chatgpt-decision.md)).
- 호출 시점도 표준화되어 있다 (§4 참조).
- decision-queue 에 작은 결정을 누적해 *호출 빈도* 를 줄이는 것이 본 단계의 1차 가치.

## 3. 5단계 로드맵

| Stage | 이름 | 사람의 역할 | Claude↔ChatGPT 인터페이스 | 진입 조건 |
|---|---|---|---|---|
| **1** | **표준화된 수동 질문 패키지** | 패키지 작성 트리거 + 복사·붙여넣기 + 응답 다시 가져오기 | 형식 표준 (ask-chatgpt-decision.md), 시점 표준 (§4) | *현재 단계*. v0.2.1 도달 시점에 진입. |
| **2** | **Decision Queue 기반 Batch Review** | cycle 또는 Meta Sprint 종료 시 1회 일괄 ChatGPT 호출 | 사람이 queue 묶음을 한 번에 전달 → 한 번에 회신 받음 | decision-queue 운영이 안정화되어 평균 cycle 당 ChatGPT 호출 1회 이하로 수렴할 때. |
| **3** | **반자동 Claude↔ChatGPT handoff** | 패키지 작성·전송 자동, 응답 검토만 수동 | Claude 가 형식화된 markdown 패키지 생성 + 사람이 1클릭으로 전송 (또는 cron) | Stage 2 의 패키지 형식이 *완전히 안정화* 되어 사람의 수정 빈도가 1% 미만으로 떨어졌을 때. |
| **4** | **API 기반 A2A** | 결과 *승인 게이트* 만 | Claude 가 OpenAI API / ChatGPT API 를 직접 호출, 응답을 자동 파싱, decision-queue 에 1행 추가, 사용자에게 보고만 | 보안·비용·속도 균형점이 명확해졌고, API 응답 품질이 수동 호출과 동등 이상. |
| **5** | **Copy-Paste Zero** | 결과 *최종 인정* 만 (한 cycle 당 ≤ 1회 응답) | Claude↔ChatGPT 가 *백그라운드* 에서 자동 협업, 사람은 *결정 사항 보고서* 만 검토 | Stage 4 가 ≥ 90 cycles 무사고 운영, Critical Decision 자동 분류 정확도 ≥ 95%. |

각 stage 는 *한꺼번에* 도약하지 않는다. Stage N 의 *데이터* 가 누적되어 Stage N+1 의 *진입 조건* 을 만족한 후에만 다음 단계.

## 4. ChatGPT 사용 시점 (현재 단계 — Stage 1 한정)
ChatGPT 는 다음 4 시점에만 호출한다 (다른 시점 호출 = 본 정책 위반):

1. **Start Control Point** — 새 cycle 시작 시 Brief 의 핵심 가설을 외부 시각으로 점검 (선택).
2. **Critical Decision** — Human Control Point 10개 트리거 ([Human_Control_Point_정책 §2](./Human_Control_Point_정책.md#2-human-control-point-escalation-트리거-하나라도-해당하면-즉시-escalation)) 발생 시 결정 패키지 생성·전달.
3. **Final Review** — cycle 종료 직전 decision-queue 의 누적 항목을 *묶음* 으로 검토 (Stage 2 진입 신호의 1차 패턴).
4. **Meta Sprint** — 프로젝트 종료 시 Foundry 백포트 후보의 *추가검토* 분류 항목만 ([Meta_Sprint_Backport_Workflow.md §3](../2_Reusable_Workflow_Modules/Meta_Sprint_Backport_Workflow.md)).

## 5. 측정 지표 (각 단계 진입 판단)
- **Stage 1 → 2**: cycle 당 평균 ChatGPT 호출 ≤ 1회. decision-queue 평균 깊이 ≥ 5 개 (한 번에 묶어 처리할 만한 양).
- **Stage 2 → 3**: 패키지 형식 수정률 ≤ 1%. 사람이 패키지를 *읽지 않고* 그대로 전달하는 비율 ≥ 95%.
- **Stage 3 → 4**: API 호출 단위 비용 / 단위 응답 품질이 수동 호출과 동등 이상. Critical Decision 자동 분류 정확도 ≥ 90%.
- **Stage 4 → 5**: ≥ 90 cycles 무사고. Critical Decision 자동 분류 정확도 ≥ 95%.

## 6. 안티-패턴
- ❌ Stage 진입 조건 미충족 상태에서 다음 stage 도구 도입 (예: Stage 1 인데 API 자동화부터 시작).
- ❌ 측정 지표 없이 "느낌으로" stage 격상.
- ❌ Stage 5 의 자동성을 사람이 결과 *검토* 하지 않는 핑계로 사용 (Copy-Paste Zero ≠ 검토 Zero).
- ❌ ChatGPT 를 §4 의 4 시점 외에 호출 (작은 결정 분산 호출 = Stage 1 의 핵심 비효율).

## 7. 다른 원칙과의 관계
- [GitHub_Foundry_관리정책.md](./GitHub_Foundry_관리정책.md) — 모든 stage 에서 invariant.
- [Human_Control_Point_정책.md](./Human_Control_Point_정책.md) — Stage 5 까지 invariant. *어떤 stage 에서도* 10개 트리거는 사람.
- [Non_Blocking_Execution_정책.md](./Non_Blocking_Execution_정책.md) — Stage 1~5 모두에서 *작은 결정 비차단* invariant. 본 로드맵은 *큰 결정의 사람-AI 인터페이스* 진화일 뿐.

## 변경 이력
- v0.2.1 candidate (2026-05-08) — 신설. Stage 1 진입.
