# L1 Principle — Human Control Point 정책

> **Layer**: 1 — Universal Operating Principles (invariant).
> **상태**: v0.2.1 candidate (2026-05-08 도입).
> 본 정책은 [Non_Blocking_Execution_정책.md](./Non_Blocking_Execution_정책.md) 와 한 쌍을 이룬다.
> 비차단 실행은 *기본*, Human Control Point 는 *예외*.

## 1. 핵심 명제
**사람은 전달자가 아니라 최종 승인자다.** Claude Code 가 작은 결정마다 사람에게 묻는 운영은 *사람을 전달자로 격하* 시킨다. 사람의 시간은 가장 희소한 자원이며 *진짜 중요한 결정* 에만 사용된다.

## 2. Human Control Point Escalation 트리거 (하나라도 해당하면 즉시 Escalation)

| # | 트리거 | 사유 |
|---|---|---|
| 1 | **보안** | 인증·인가·세션·암호화·취약점 (예: RLS 정책, JWT 검증, secret 관리). 잘못되면 사고. |
| 2 | **결제 / 과금** | 실제 돈의 흐름. 가격, 청구, 환불, 정기결제 로직 변경. |
| 3 | **DB schema** | 한 번 배포된 schema 의 호환성 깨는 변경. 마이그레이션 비용. |
| 4 | **법률 / 컴플라이언스** | 약관, 개인정보, 결제 사업자 의무, 세금 처리. |
| 5 | **되돌리기 어려운 아키텍처** | 프레임워크 / 핵심 라이브러리 / 클라우드 provider / DB 엔진 선택. |
| 6 | **큰 범위 변경** | 본 cycle 의 In/Out Scope 를 의미 있게 넘어서는 작업. |
| 7 | **큰 비용 증가** | 외부 서비스 유료 plan 격상, 신규 SaaS 도입 (월 비용 발생). |
| 8 | **BM / 가격 정책** | Plan tier 정의·변경, 무료↔유료 경계, 트라이얼 정책. |
| 9 | **사용자 데이터 처리** | 수집·저장·전송·삭제 정책. PII / 결제정보 / 위치 등. |
| 10 | **외부 API 계약 리스크** | 결제 PG / 인증 / 알림 등 *깨지면 서비스가 멈추는* 외부 의존. SLA·rate limit·breaking change. |

## 3. Escalation 형식
Claude Code 는 트리거가 발생하면 다음 형식으로 사용자에게 *한 번에* 보고한다 (조각조각 묻지 않는다):

```markdown
## 🔴 Human Control Point — <한 줄 결정 제목>
- **트리거**: <위 10개 중 어느 것 — ID 와 이름>
- **결정 사항**: <무엇을 결정해야 하는가, 한 단락>
- **Default Action (사용자가 응답하지 않으면 Claude 가 진행할 행동)**: <기본값 또는 "결정 없이는 진행 불가">
- **옵션**: A / B / C (각각 1줄 요지 + 트레이드오프)
- **Claude 추천**: <옵션 중 하나 + 1줄 사유>
- **되돌리기 비용**: 낮음 / 중 / 높음
- **참조**: <관련 파일 / cycle / decision-queue 항목>
```

응답이 즉시 오지 않더라도 Claude 는 *그 결정에 의존하지 않는 다른 작업* 을 계속 진행한다. 차단되는 작업만 멈춘다.

## 4. 비-Escalation 트리거 (Non-Blocking 으로 처리)
다음은 Human Control Point 가 아니다 — Claude 가 *진행하면서* `meta/decision-queue.md` 에 기록만 한다 ([Decision_Queue_운영방식.md](../2_Reusable_Workflow_Modules/Decision_Queue_운영방식.md) 참조):

- 변수명 / 함수명 / 파일명 / 폴더명.
- 작은 UI 표현 (버튼 색, 마진, 마이크로카피).
- 코드 스타일 (lint 의 잿빛 영역).
- 기술적 우회 (예: TypeScript `any` 의 1회 사용 — 추후 정리 예정).
- 테스트 케이스 1~2개의 추가/제거.
- 1~2일 내 되돌릴 수 있는 라이브러리 선택 (예: 작은 utility lib 1개).

원칙: **되돌릴 수 있고 영향 작은 결정은 Claude 가 한다.**

## 5. 흐름도

```
결정 발생
   │
   ▼
[10개 트리거 중 하나라도 해당?] ─── YES ──► [§3 형식으로 Escalation] ──► 사용자 응답 대기
   │                                              ↑
   NO                                             │ (다른 비차단 작업은 계속 진행)
   │
   ▼
[비차단 결정] ──► Claude 가 결정 + meta/decision-queue.md 에 1행 기록 ──► 다음 작업 계속
```

## 6. 위반 신호
- Claude 가 1시간 작업 중 사용자에게 ≥ 3회 짧은 결정 요청.
- 사용자가 "그냥 알아서 해" 또는 "왜 이런 걸 묻냐" 응답을 반복.
- decision-queue.md 가 비어 있는데 작업 진행이 잦은 작은 멈춤.

이는 "사람을 전달자로 사용하고 있다" 는 신호. 본 정책 §4 의 비-Escalation 분류로 재조정.

## 변경 이력
- v0.2.1 candidate (2026-05-08) — 신설.
