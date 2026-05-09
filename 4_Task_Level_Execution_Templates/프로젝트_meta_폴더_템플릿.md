# L4 Template — 프로젝트 meta 폴더 템플릿

> **Layer**: 4 — Task-level Execution Template.
> **상태**: v0.2.1 candidate (2026-05-08 도입).
> **선행 원칙**: [Non_Blocking_Execution_정책](../1_Universal_Operating_Principles/Non_Blocking_Execution_정책.md), [Copy_Paste_Zero_로드맵](../1_Universal_Operating_Principles/Copy_Paste_Zero_로드맵.md).
> **사용 workflow**: [신규_프로젝트_생성_Workflow](../2_Reusable_Workflow_Modules/신규_프로젝트_생성_Workflow.md), [Meta_Sprint_Backport_Workflow](../2_Reusable_Workflow_Modules/Meta_Sprint_Backport_Workflow.md).

## 1. 표준 폴더 구조

모든 신규 프로젝트는 다음 6 파일을 가진 `meta/` 폴더를 *반드시* 가진다.

```
<project>/
└── meta/
    ├── foundry-improvement-log.md       ← 진행 중 raw 발견 (FIL-NNN)
    ├── foundry-backport-candidates.md   ← Meta Sprint 정제 (FBC-NNN, 4 분류)
    ├── decisions.md                     ← Critical Decision 시간순 (D-NNN)
    ├── decision-queue.md                ← 작은 결정 누적 (DQ-NNN, blocker 아님)
    ├── lessons-learned.md               ← cycle 별 keep/change/drop
    └── chatgpt-decision-requests.md     ← ChatGPT 와 주고받은 결정 패키지 / 회신
```

## 2. 각 파일의 역할

### 2.1 `foundry-improvement-log.md`
- **역할**: 진행 *중* 발견한 Foundry 개선 단서를 *그 자리에서* 박제.
- **항목 ID**: `FIL-NNN`.
- **누가 쓰는가**: Claude (대부분) + 사용자 (관찰).
- **언제 쓰는가**: Foundry 룰 / 템플릿 / 도구 사용 중 어색함을 만난 그 즉시.
- **항목 형식 (8 필드)**: 발견일 / 발견자 / 발견 맥락 / 증상 / 가설 / 제안 / 영향 추정 / 임시 대응 / 참조.
- **금지**: 즉시 Foundry 원본 수정.

### 2.2 `foundry-backport-candidates.md`
- **역할**: Meta Sprint 진입 시 FIL 들을 4 분류 (승인/보류/폐기/추가검토) 로 정제.
- **항목 ID**: `FBC-NNN`.
- **누가 쓰는가**: Claude 가 1차 분류, 사용자가 §승인 섹션에서 최종 응답.
- **언제 쓰는가**: 프로젝트 종료 / 1차 마일스톤 종료 시 Meta Sprint 입구.
- **사용자 응답 형식**: `[APPROVED]` / `[DEFER]` / `[REJECT]` / `[SPLIT]`.

### 2.3 `decisions.md`
- **역할**: 본 프로젝트의 *Critical Decision* 시간순 로그.
- **항목 ID**: `D-NNN`.
- **누가 쓰는가**: Claude (사용자 승인 직후) + 사용자 (직접 박제 가능).
- **언제 쓰는가**: 다음 결정 발생 시.
  - 되돌리기 어려운 변경 / 의미 있는 스코프-예산-일정 변경 / 리스크 등급 상향 / AC 변경.
  - Foundry version 선택, `local_modifications` 전환, Meta Sprint 의 사용자 최종 승인.
- **금지**: 작은 결정을 본 파일에 (← `decision-queue.md` 가 옳다).

### 2.4 `decision-queue.md`
- **역할**: *작은* 결정 누적소. *blocker 가 아님*.
- **항목 ID**: `DQ-NNN`.
- **누가 쓰는가**: Claude (대부분).
- **언제 쓰는가**: [Non_Blocking 분류 매트릭스](../1_Universal_Operating_Principles/Non_Blocking_Execution_정책.md#2-실행-분류-매트릭스) 의 *애매하지만 일반적 베스트 프랙티스 있음* 또는 *애매하고 트레이드오프 있음* 항목 결정 시.
- **표준 컬럼 (8)**: ID / Date / Topic / Decision Needed / Default Action Taken / Reversibility / Risk / Review Timing.
- **검토 시점**: `Final Review` (cycle 종료 직전) / `Meta Sprint` (프로젝트 종료) / `Next Cycle` (다음 cycle 시작 직전).

### 2.5 `lessons-learned.md`
- **역할**: cycle 별 회고. 다음 cycle 의 *행동 변화* 를 위함.
- **항목 형식**: cycle 별로 keep / change / drop 1줄씩 + 선택적 Foundry 후보 링크.
- **누가 쓰는가**: Claude + 사용자 공동.
- **언제 쓰는가**: 매 cycle 의 Final Control Point 통과 직후.
- **금지**: 추상적 다짐 ("더 잘하겠다" → ❌). 구체적 행동 변화 ("X 시작 전 Y 한다" → ✅).

### 2.6 `chatgpt-decision-requests.md`
- **역할**: ChatGPT (또는 다른 외부 AI) 와 주고받은 *결정 패키지 + 회신* 의 1대1 보관소.
- **누가 쓰는가**: Claude (대부분) — 패키지 작성 시점에 박제.
- **언제 쓰는가**: ChatGPT 호출 *4 시점* 중 하나에서 ([Copy_Paste_Zero_로드맵 §4](../1_Universal_Operating_Principles/Copy_Paste_Zero_로드맵.md#4-chatgpt-사용-시점-현재-단계--stage-1-한정)).
  - Start Control Point / Critical Decision / Final Review / Meta Sprint.
- **항목 형식**: 결정 패키지 (질문) → ChatGPT 응답 → Claude 의 통합 / 채택 결정.

## 3. 파일별 stub 템플릿 (복사해 사용)

### `foundry-improvement-log.md`
```markdown
# Foundry Improvement Log — <project-name>

> 진행 중 발견한 Foundry 개선 단서. *즉시* 박제. *원본 수정 금지*.
> 정제는 `foundry-backport-candidates.md`. Meta Sprint 입력.

## 항목 형식
\`\`\`
### FIL-NNN — <짧은 제목>
- **발견일**: YYYY-MM-DD
- **발견자**: <역할 또는 이름>
- **발견 맥락**: …
- **증상 / 관찰**: …
- **가설**: …
- **제안 (1차)**: …
- **영향 추정**: 높음 / 중간 / 낮음 + 이유
- **임시 대응**: …
- **참조**: …
\`\`\`

## 누적
(아직 없음.)
```

### `foundry-backport-candidates.md`
```markdown
# Foundry Backport Candidates — <project-name>

## 분류 정의
- **승인**: 일반화 가능, Foundry 반영 후보.
- **보류**: 1 사례 부족, N 사례 누적 후 재검토.
- **폐기**: 프로젝트 특화 / 진단 오류.
- **추가검토**: ChatGPT 외부 의견 필요.

## 승인
(아직 없음.)

## 보류
(아직 없음.)

## 폐기
(아직 없음.)

## 추가검토
(아직 없음.)

## Meta Sprint 운영 메타
- **시작일**: <YYYY-MM-DD>
- **사용자 최종 승인일**: <YYYY-MM-DD>
- **Foundry 반영 commit 범위**: `<from>..<to>`
- **Foundry version bump**: `<from> → <to>`
- **self-test 재통과**: ✅ / ❌
```

### `decisions.md`
```markdown
# Decisions — <project-name>

> 본 프로젝트의 Critical Decision 시간순.

## 항목 형식
\`\`\`
### D-NNN — <한 줄>
- **일자**: YYYY-MM-DD
- **종류**: scope | tech-stack | foundry-version | foundry-local-mod | meta-sprint-approval | …
- **결정 내용**: …
- **근거**: …
- **반대 의견**: …
- **되돌리기 비용**: 낮음 / 중 / 높음
- **승인자**: …
- **참조**: …
\`\`\`

## 누적
(아직 없음.)
```

### `decision-queue.md`
```markdown
# Decision Queue — <project-name>

> 작은 결정 누적소. **Blocker 가 아님.**
> 검토는 Final Review / Meta Sprint / Next Cycle 중 하나.

## 표준 컬럼
| ID | Date | Topic | Decision Needed | Default Action Taken | Reversibility | Risk | Review Timing |
|---|---|---|---|---|---|---|---|

## 누적
| DQ-NNN | YYYY-MM-DD | <topic> | <질문 1줄> | <Claude default + 사유> | reversible / partially / irreversible | 낮음/중/높음 | Final Review / Meta Sprint / Next Cycle |
```

### `lessons-learned.md`
```markdown
# Lessons Learned — <project-name>

## 항목 형식
\`\`\`
### Cycle: <cycle-id> (<YYYY-MM-DD>)
- **Keep**: …
- **Change**: …
- **Drop**: …
- (선택) **Foundry 후보**: foundry-improvement-log.md#FIL-NNN
\`\`\`

## 누적
(아직 없음.)
```

### `chatgpt-decision-requests.md`
```markdown
# ChatGPT Decision Requests — <project-name>

> ChatGPT 와 주고받은 결정 패키지 + 회신의 1대1 보관소.
> 호출 시점 4종: Start CP / Critical Decision / Final Review / Meta Sprint.

## 항목 형식
\`\`\`
### CDR-NNN — <한 줄 결정 제목>
- **시점**: Start CP | Critical Decision | Final Review | Meta Sprint
- **일자**: YYYY-MM-DD
- **요청 패키지**: (ask-chatgpt-decision.md 형식 — 7 섹션)
- **ChatGPT 회신**: (원문 또는 요지)
- **Claude 채택 결정**: 어떻게 통합했는가 + 사유
- **반영 위치**: `decisions.md#D-NNN` 또는 `foundry-backport-candidates.md#FBC-NNN` 등
\`\`\`

## 누적
(아직 없음.)
```

## 4. 통합 흐름

```
프로젝트 진행 중
   │
   ├─ 작은 결정 ──► decision-queue.md (DQ-NNN)
   ├─ Foundry 어색함 ──► foundry-improvement-log.md (FIL-NNN)
   ├─ Critical Decision ──► decisions.md (D-NNN)
   ├─ ChatGPT 호출 ──► chatgpt-decision-requests.md (CDR-NNN)
   └─ cycle 종료 ──► lessons-learned.md (cycle 별 keep/change/drop)

프로젝트 종료
   │
   ▼
Meta Sprint
   ├─ FIL → FBC 4 분류
   ├─ DQ 잔여 정리 → keep/되돌림/Foundry 후보 격상
   ├─ ★ 사용자 최종 승인 게이트 → decisions.md 박제
   ├─ 승인 항목 → 00-Foundry commit
   ├─ self-test 재통과
   └─ Foundry version bump + tag + push
```

## 5. 안티-패턴
- ❌ `meta/` 폴더 누락 또는 일부 파일만 생성.
- ❌ 작은 결정을 `decisions.md` 에 (← `decision-queue.md`).
- ❌ Critical Decision 을 `decision-queue.md` 에 (← `decisions.md`).
- ❌ Foundry 발견을 `decisions.md` 또는 `decision-queue.md` 에 (← `foundry-improvement-log.md`).
- ❌ ChatGPT 호출 시 패키지 / 회신을 별도 보관 안 함 (역추적 불가).
- ❌ cycle 종료 시 lessons-learned.md 작성 생략.

## 변경 이력
- v0.2.1 candidate (2026-05-08) — 신설. Bootstrap/project-meta-templates/ 의 5 템플릿 (4 + factory.yaml) 을 본 L4 layer 의 *공식 템플릿 인덱스* 로 격상 + `decision-queue.md` / `chatgpt-decision-requests.md` 신규 추가 (총 6 파일).
