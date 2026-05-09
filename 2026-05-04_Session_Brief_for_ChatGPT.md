# 🗂 Session Brief — 2026-05-04
## "Antigravity Workflow → Foundry" 전환 + Multi-Project AI Factory 구상

> **For ChatGPT discussion**: 본 문서는 사용자 (geonwoo.kim, LG전자 기구개발 출신, Claude Code 솔로 사용자) 가 Claude (Opus 4.7) 와 한 4시간 세션에서 자신의 AI 코딩 워크플로 전체를 재검토한 내용입니다. 다양한 관점의 추가 입력을 받기 위해 ChatGPT 에 전달합니다. **Claude 의 진단이 항상 옳다고 가정하지 마세요** — 비판적 시각 환영.

---

## 1. 사용자 페르소나 (가장 중요)

- **직업 배경**: LG전자 기구 개발 (하드웨어/메카니컬 엔지니어). 산업공학 비전공.
- **AI 시대 자기 정의**: *공장주 (Factory Owner / CEO)*. 라인 설계자.
- **도메인**: 웹 + 앱 + 향후 하드웨어 (펌웨어·PCB·기구 — AI 도구 성숙 시)
- **운영 의도**: 멀티 프로젝트 동시 가동 (현재 폴더 4개: `10·11·12·13`)
- **학습 깊이**: *CEO 수준* — 흐름·context·진척도 파악만. 신경망 디테일·산업공학 풀이론은 *알 필요 없음*.
- **핵심 가치**: 시간 자원이 가장 희소. 어텐션 보호 최우선.
- **핵심 워크플로 원칙**: User = *판단* (승인/방향성/주관 평가) 만. AI / 자동화 = *조작* (클릭·복사·시각 비교·명령 입력).

---

## 2. 현재 작동 중인 시스템 (세션 시작 전 baseline)

자체 명명한 **"Antigravity Workflow"** — 7-agent + 무거운 artifact 시스템.

### Agents (7개, 글로벌 `~/.claude/agents/`)
| 에이전트 | 책임 |
|---|---|
| master-prd-builder | PRD 인터뷰 생성 |
| implementation-planner | Phase Plan 작성 |
| phase-executor | 실행 + Walkthrough 작성 |
| qa-verifier | 공식 QA 검증 |
| hotfix-handler | 버그 RCA |
| ux-reviewer | UI 변경 검증 |
| deep-thinker | 다관점 분석 (Musk/Feynman/Adler/Munger/Huang) |

### Phase 사이클 (헌법 §3)
```
PRD → Plan → Tasks → Walkthrough → QA
       ↑       ↑          ↑           ↑
    [승인]  [승인]    [완료 후 작성]   [PASS]
```

### 산출물 — Phase 당 4-5개 markdown
- `0N_Plan.md` (Context, Goals, Approach, Verification Strategy, Approval)
- `0N_Tasks.md` (체크리스트)
- `0N_Walkthrough.md` (실제 변경 + 결과)
- `2NN_QA.md` (공식 검증)
- `2NN_UX.md` (UI 변경 시)

### Approval 게이트 — Phase 당 6+개
Plan 승인 / Tasks 승인 / §B 시각 검증 / §C 학습 자기보고 / Walkthrough 리뷰 / QA 리뷰

### 진행 상황
`11-shopping-dashboard` 프로젝트 Phase 3 진행 중. Phase 1·2 완료.

---

## 3. 세션의 주요 발견·결정 (시간순)

### 3.1 Tasks.md 룰 위반 → 글로벌 템플릿 fix
- 헌법은 "체크리스트" 명시인데 phase-executor 글로벌 템플릿이 *이모지 상태 칼럼만 있는 표* 생성 → 룰 위반
- Fix: `[ ]`/`[x]` 체크박스 강제, 칼럼 순서 (`✓ Owner # Task ...`), no-wrap (`[&nbsp;]` + `<br>`)
- 글로벌 phase-executor.md 갱신 → 다른 모든 프로젝트 자동 적용

### 3.2 핵심 워크플로 원칙 명시 (B02)
> User-Owner = *판단* 만. AI / 자동화 = *조작*.

이게 모든 후속 결정의 철학적 기반.

### 3.3 Backlog 정책 수립
- 진행 중 프로젝트에 헌법/에이전트 구조 변경 금지
- 발견된 개선 → `Backlog.md` 누적
- M01 Meta Sprint 시점에 일괄 적용
- *(이후)* **B21 부분 개정** (Compound Engineering): CLAUDE.md 한 줄 룰 추가류는 즉시 반영

### 3.4 비동기 + 모바일 워크플로 인식
사용자 통찰: *"공장이 사용자 부재 시에도 가동돼야 함, 인터럽트 비용 최소화"*

Backlog 추가:
- **B13** Async Approval Queue + Self-Pause Protocol
- **B14** Mobile Notification (Telegram MVP)
- **B15** Multi-Project Supervisor + Digest
- **B16** Phase 0 Pre-Flight (사용자 액션 프론트로딩 — Master PRD 시점에 모든 미래 사용자 액션 예측 후 batch)

### 3.5 외부 리서치 → 충격적 발견
**두 리서치 에이전트 동시 실행** (claude-code-guide + general-purpose web research).

**핵심 발견**:

1. **Boris Cherny (Claude Code lead) 공식 가이던스**: *"Don't spawn subagent for work doable in single response."* Subagent = ephemeral roles, **NOT permanent org chart** → 우리 7-agent 가 *정확히 안티패턴*.

2. **산업 컨센서스 2026** (Cursor/Devin/OpenHands/Cherny/Shipper 모두 일치): *one approval gate at plan, autonomous execution after, post-hoc PR review*. Per-step 승인 (Cline 스타일) 은 **discredited**.

3. **Anthropic이 우리 spec을 이미 출시함**:
   - **Claude Code Channels** (March 2026): Telegram/Discord/iMessage + inline Approve/Deny 버튼 — *우리 B14 spec이 이미 공식 기능*
   - **`claude --worktree`** (Oct 2026, Cherny 직접 출시): git worktree + 격리된 인스턴스 자동화 — *우리 B15 supervisor의 절반이 이미 공식*

4. **Tim de Schryver 인용**: *"LLMs cannot reliably execute hundreds of deterministic steps from memory"* — 우리 절차주의 직격.

5. **Dan Shipper (Every) Compound Engineering**: 학습을 다음 프로젝트로 이연 X, *즉시 CLAUDE.md 반영*. 우리 Backlog-defer 정책과 정면 충돌.

6. **Geoffrey Huntley "Ralph Wiggum"**: `while true` bash loop + 단일 markdown spec. 헤비 ceremony 의 반대 극단.

**Backlog 추가**:
- **B17** Subagent 7→4 통합 (planner+planner / executor+QA 병합, ux-reviewer hook+skill 로)
- **B18** Approval 6+ → 1 게이트 (industry consensus)
- **B19** Channels 공식 채택 (B14 흡수)
- **B20** --worktree 공식 채택 (B15 부분 흡수)
- **B21** Compound Engineering 즉시 반영 정책
- **B22** M01 Sprint trigger = 프로젝트 종료 + 학습 readiness

### 3.6 사용자 결정: Option A (모두 Backlog 잔류, 학습 먼저)
사용자: *"이들은 그 분야의 전문가이지만 나는 비전공자잖아... 표면 패턴 복제 위험 있음. 학습 후에 결정하고 싶음."*

→ **Reading_List.md 생성** (Karpathy + Anthropic + Cherny + Shipper + Willison + Huntley + swyx + 다른 framework 들 큐레이션, 4 Tier 25개 항목)

### 3.7 Lesson 1 시도 (Karpathy "Software 2.0") → 첫 번째 reframe

Claude가 Socratic 방식으로 Karpathy 패러다임 강의 시작.

**Software 1.0 vs 2.0**:
- 1.0 = 사람이 명시적 규칙 작성, deterministic
- 2.0 = 사람이 목표+데이터셋 지정, stochastic + emergent (LLM이 여기)

사용자가 정확히 진단:
> *"우리 워크플로는 행동은 2.0, 통제는 1.0 — 하이브리드"*

이어서:
> *"Plan을 X(계약서)처럼 말하고 게이트하면서, Y(출발 가설)처럼 행동하고 방치한다. 명시적으로 결정한 적 없음."*

이 모순이 22개 Backlog 의 *대부분 (16개)* 의 뿌리라는 진단까지 도출.

**그런데 사용자 반전 질문**:
> *"이게 비전공자인 나에게도 같은 답인가? Karpathy/Cherny 는 expert 인데 나는 학습자임."*

Claude 의 잘못된 반응: *"당신은 학습자, heavy artifact 는 학습 스캐폴딩으로 정당화된다"* → 사용자가 catch.

### 3.8 사용자 두 번째 reframe (Claude 진단 틀림 지적)
사용자: *"내가 원하는 건 최신 트랜드에 맞는 서비스 *생산 공장*. CEO 수준에서 흐름·context 파악. 하드웨어/기구 출신이라 시스템 사고는 익숙."*

Claude 의 *또 잘못된* 반응: Toyota Production System + Goldratt + 6단계 로드맵 + Lean / TOC 풀 도입 제안.

### 3.9 사용자 세 번째 reframe (또 over-engineering)
사용자: *"산업공학 전공도 아닌데 너무 방대함. overengineering 아닌가?"*

Claude 마침내 정확한 답: **MVF (Minimal Viable Factory)** — 단일 `STATUS.md` 파일, 1시간 작업, 그게 전부. Toyota Way 폐기.

### 3.10 메타 작업 분리 결정 (사용자 통찰)
사용자: *"이 프레임워크 개선 활동은 제품 프로젝트와 별개의 시스템 프로젝트로 만들고 싶음."*

→ 새 sibling 프로젝트 생성: **`00-AntigravityOS`** (이후 **`00-Foundry`** 로 rename — 도구 중립성 위해)

이전된 것:
- `Backlog.md` (B01-B24)
- `Reading_List.md`
- `STATUS.md` (B23-A MVF)
- `README.md` + `PRD.md`

옛 위치 (`11-shopping-dashboard/Artifacts/01_Meta/`) 에는 forwarder 만 잔류.

### 3.11 마지막 rename: AntigravityOS → Foundry
사용자: *"Antigravity 는 보조도구 정도, claude code 가 main, 발전 방향에 따라 또 바뀔 수 있음. 도구 종속 이름 안 좋음."*

→ **`Foundry`** 채택 (도구 중립, 하드웨어 친화 — 주조소 = 멀티 라인 생산 메타포).

---

## 4. 현재 commit 된 핵심 원칙 (메모리, 즉시 적용 중)

8개 메모리 박제 (Claude 향후 모든 세션이 자동 로드):

1. **feedback_tasks_checkbox.md** — Tasks.md `[ ]` 체크박스 강제, 칼럼 순서, no-wrap 룰
2. **user_workflow_principle.md** — User = 판단, AI = 조작 (B02)
3. **user_async_workflow_preference.md** — 동기 블로킹 게이트 싫어함, 비동기 + 모바일 지향
4. **user_persona_ceo_factory.md** — CEO/공장주 + LG전자 기구 출신 + AI = 노동자
5. **user_minimal_first_principle.md** — Always Minimal First → Kaizen 진화. 이론 프레임워크는 영감으로만, 구현 청사진 금지
6. **project_meta_backlog_policy.md** — 진행 중 적용 금지 + B21 즉시 반영 예외 (Compound Engineering)
7. **project_design_pivot.md** — Stitch 폐기 (다음 프로젝트부터)
8. **project_industry_consensus_2026.md** — 외부 리서치 결과 박제

---

## 5. Backlog 24개 항목 요약 (`00-Foundry/Backlog.md`)

### 진행 중 프로젝트 학습 (B07-B12)
- B07: Supabase gen types `<claude-code-hint>` 마커 후처리 룰
- B08: vitest 4 + React 19 동반 의존성 명시
- B09: actions.ts 401/422 폼 에러 UI 처리
- B10: login-form vitest Empty-Input 케이스
- B11: src/sanity.test.ts 삭제 vs 보존
- B12: /tdd Workflow Slash command vs Skill 비교

### 워크플로 구조 개선 (B01-B06, B13-B22)
- B01: Stitch 폐기 → AI-direct shadcn 코딩
- B02: User=판단·AI=조작 헌법 명시
- B03: Supabase 초기 설정 CLI 자동화
- B04: 시각 검증 §B 자동화 (Playwright)
- B05: 헌법 §3 Tasks.md 포맷 layering 재검토
- B06: Verification Profile (게이트 자동화 옵션 시스템 — 3 프리셋)
- B13: Async Approval Queue + Self-Pause Protocol
- B14: ❌ Mobile Notification → B19 흡수
- B15: ⚠️ Multi-Project Supervisor → B20 부분 흡수
- B16: Phase 0 Pre-Flight (사용자 액션 프론트로딩)
- B17: **Subagent 7→4 통합** (Cherny 안티패턴 해소)
- B18: **Approval 6+ → 1 게이트** (industry consensus)
- B19: Anthropic Channels 공식 채택
- B20: `claude --worktree` 공식 채택
- B21: Compound Engineering 즉시 반영 정책
- B22: M01 Sprint trigger = (프로젝트 종료) AND (Reading_List 학습 readiness)

### CEO Factory 인프라 (B23-B24)
- B23: STATUS.md (MVF — *완료*) + HTML 실시간 동기화 보드 (확장)
- B24: Lieutenant Orchestration Agent (사용자 대신 Standing Orders 적용)

### Sprint 적용 권장 순서 (현재)
0. B21 (즉시 반영 정책) — 즉시
1. B02 (헌법 메타 원칙)
2. B17 (Subagent 통합 7→4)
3. B18 (Approval 1 게이트)
4. B04 (시각 자동화)
5. B06 (Verification Profile)
6. B13 (Async Queue)
7. B19 (Channels 채택)
8. B16 (Phase 0)
9. B01 + B03 (병렬)
10. B20 (--worktree)
11. B05 (마무리)

---

## 6. Reading_List 학습 자료 큐레이션 (`00-Foundry/Reading_List.md`)

| Tier | 내용 | 시간 |
|---|---|---|
| 1 (필수) | Karpathy (Software 2.0, State of GPT, Intro to LLMs) + Anthropic (Building Effective Agents, Context Engineering) | ~6h |
| 2 (필수) | Cherny (howborisusesclaudecode) + Claude Code 공식 docs (sub-agents, hooks, skills, channels, agent-teams) + Shipper (Compound Engineering) | ~6h |
| 3 (권장) | Willison (anti-patterns) + Huntley (Ralph Wiggum) + swyx (scaling without slop) + Tim de Schryver | ~4h |
| 4 (선택) | 다른 에이전트 프레임워크 (Aider, Cline, Cursor, Devin, OpenHands) + Anthropic Engineering 블로그 deep dive | ~6h |

**M01 Sprint 트리거**: Tier 1 + Tier 2 = 14개 모두 완료 + 자가 점검 5문항 답변 가능

---

## 7. 미해결 질문 / ChatGPT 와 논의하고 싶은 것

### 7.1 큰 질문 (전략)

1. **CEO Operator vs Coding Learner 페르소나 분리가 정당한가?**
   - Karpathy/Cherny의 lighter pattern은 expert 에게는 맞지만 비전공자에게도 같은 답인가?
   - 학습 스캐폴딩으로 무거운 워크플로를 *temporary* 유지하는 게 long-run 도움인가, 발목인가?

2. **Industry consensus 2026 채택 vs 자기 스타일 유지의 trade-off**
   - 1-gate-at-plan + auto-accept = production 효율 ↑, 학습 가치 ↓
   - 솔로 학습 컨텍스트의 정확한 균형점은?

3. **Compound Engineering vs Backlog defer**
   - 즉시 적용 = 학습 보존 + churn 위험
   - 어디까지 즉시 / 어디부터 defer 의 명확한 기준?

4. **Lieutenant Orchestration Agent 도입 시점·안전성**
   - 사용자 대신 Standing Orders 적용 = strong delegation
   - 어떤 게이트는 절대 위임 불가 (B06 안전 카브-아웃 7개) — 충분한가?

### 7.2 중간 질문 (구현)

5. **Multi-project HTML real-time board 구현**
   - Vercel + Next.js + STATUS.md aggregation = 적절한 스택?
   - 모바일 친화 UI design pattern?

6. **하드웨어 라인 통합 시점·방식**
   - 펌웨어는 Claude Code 가능, PCB/CAD 는 미성숙
   - "soft" 도메인과 "hard" 도메인을 같은 Foundry 안에서 관리?

7. **Sprint trigger 학습 readiness 평가**
   - 자가 점검 5문항으로 충분한가?
   - 더 정밀한 평가 방식?

### 7.3 작은 질문 (디테일)

8. **Backlog 24개 우선순위**
   - 진짜 critical / nice-to-have / 폐기 후보 분류
   - 데이터 없이 우선순위 매기는 게 가능한가?

9. **헌법 §3 layering 결정 (B05)**
   - 헌법 = 원칙, 에이전트 = 구현 (현재) vs 헌법에도 부록으로 구현 명시
   - Long-term 유지보수에 유리한 쪽?

10. **Agents 7개 → 4개 통합 시 실제 작업 흐름**
    - PRD-builder + Planner 병합 시 인터뷰 ↔ Plan 작성 mode switching?
    - Executor + QA 병합 시 self-evaluation 의 객관성?

---

## 8. 메타 — Claude (Opus 4.7) 가 이번 세션에서 보인 패턴

**중요 데이터** — ChatGPT 가 Claude 의 진단을 평가할 때 참고:

Claude 가 over-engineering 한 횟수: **2번 (한 세션 내)**

1. *학습 스캐폴딩 정당화*: 사용자가 lighter 가자고 했는데 "학습 가치" 명목으로 무거운 시스템 유지 옹호
2. *Toyota Factory 6단계 로드맵*: 사용자가 CEO 수준 답을 원한다고 reframe 했는데 산업공학 풀 이론 도입 제안

매번 사용자 catch → Claude 새 무거운 답으로 교체 → 사용자 다시 catch → 마침내 minimal.

이게 시사하는 것:
- LLM (Claude) 은 누적 컨텍스트 안에서 *추가* 하는 방향 편향
- *제거·압축·minimal* 방향 결정은 인간이 강제해야 함
- 사용자의 *minimal first* 메모리 룰은 이 패턴 방지용

ChatGPT 도 같은 함정에 빠질 수 있으니 의식 권장.

---

## 9. ChatGPT 에게 던지면 좋을 seed 질문 (제안)

골라서 사용 가능:

> ① *"내 페르소나 (CEO/공장주, 하드웨어 출신, 산업공학 비전공) 와 위 컨텍스트를 보고, **너라면 어디서 가장 다르게 갈까?** Claude 의 추천 (B17·B18·B19·B20 기반 lightweight 리팩토링) 이 valid 한지, 더 나은 길이 있는지 비판적으로."*

> ② *"Karpathy Software 2.0 관점과 내 워크플로의 모순 (행동 2.0 / 통제 1.0) 에 대해, Claude 는 *명시적 결정 안 함이 모든 secondary 문제의 뿌리* 라고 진단했어. 너는 동의해? 다른 진단이 있어?"*

> ③ *"Backlog 24개 중에 '이건 진짜 중요', '이건 over-engineering 같음' 어떤 게 있나? 솔로 비전공자 CEO 페르소나 기준으로 평가해줘. 폐기 권고 항목도 알려줘."*

> ④ *"Foundry 라는 메타 프로젝트 구조 자체가 over-engineering 인가, 자연스러운 진화인가? Cline·Cursor·Devin 사용자들은 이런 메타 구조 없이도 운영하는데, 우리만 이게 필요한 이유 / 안 필요한 이유?"*

> ⑤ *"Claude 가 한 세션에서 두 번 over-engineering 한 패턴 (8장 참조) 을 보면, LLM 워크플로 컨설팅의 한계가 뭐고, 사용자가 어떤 self-defense 룰을 가져야 할까? 너도 같은 함정에 빠질 가능성에 대해 honest 하게."*

> ⑥ *"Reading_List 25개 항목 중 비전공자 CEO 가 *진짜로* 8주 안에 소화 가능한 핵심 5개만 골라줘. 나머지는 폐기 권장 사유와 함께."*

---

## 10. 첨부 — 현재 폴더 구조

```
~/Dev/Work/안티그래비티 완벽가이드/
├── 00-Foundry/                  ← 메타 프레임워크 프로젝트 (이 문서 위치)
│   ├── README.md
│   ├── PRD.md                   ← v0.1 minimal
│   ├── Backlog.md               ← B01-B24 모두 여기
│   ├── Reading_List.md
│   ├── STATUS.md                ← MVF (수동 갱신)
│   └── 2026-05-04_Session_Brief_for_ChatGPT.md  ← 본 문서
├── 10. 쇼핑 리뷰 분석 챗봇 만들기/
├── 11-shopping-dashboard/       ← 현재 진행 중 (Phase 3)
│   └── Artifacts/01_Meta/
│       ├── Backlog.md           → forwarder
│       └── Reading_List.md      → forwarder
├── 12. 구독 결제 SaaS 플랫폼 만들기/
└── 13. LLM wiki_Git_Obsidian/
```

---

**문서 끝**.

ChatGPT 와 함께 토론하실 때 위 컨텍스트 기준으로 답해주세요. 가장 중요한 것: 사용자는 ***minimal first 원칙***을 강하게 선호하고 ***over-engineering*** 을 피하고 싶어합니다. Toyota/TPS 풀 이론·Karpathy 신경망 디테일·Goldratt 등 *학문적 깊이* 는 사용자에게 oversize 입니다. *실무적·사용자 시간 보호* 관점이 우선.
