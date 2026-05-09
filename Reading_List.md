# 📚 Reading List — M01 Meta Sprint 학습 자료

**용도**: M01 Meta Sprint 트리거 조건 (B22) — 사용자가 본 리스트의 **Tier 1·2 항목을 완료**해야 implementation-planner 가 Sprint Plan 작성 시작.

**큐레이션 원칙**:
- 표면 패턴 복제 ❌ → *왜* 그 결정을 했는지 깊이 이해 ✅
- Tier 1: 워크플로 결정의 *철학적 기반* (필수)
- Tier 2: *실무 워크플로* (필수)
- Tier 3: 다양한 관점 (권장)
- Tier 4: 깊이 추가 (선택, 시간 여유 시)

**진척도 표기**: `[&nbsp;]` 미완료 / `[x]` 완료 + 한 줄 핵심 takeaway 기록

---

## Tier 1 — 철학적 기반 (필수, ~6시간)

### A. AI 에이전트 본질 — Andrej Karpathy

근본 원리부터. Karpathy 는 ML 연구자이자 Tesla Autopilot 디렉터, OpenAI 창립멤버. 코딩 에이전트의 본질을 가장 압축적으로 설명.

- [&nbsp;] **"Software 2.0"** (2017 블로그) — https://karpathy.medium.com/software-2-0-a64152b37c35
  - 왜: 모든 AI 에이전트 사고의 출발점. 코드 = 데이터 + 가중치 패러다임 전환.
  - Takeaway:
- [&nbsp;] **"State of GPT" 강의** (2023, Microsoft Build, 40분) — https://www.youtube.com/watch?v=bZQun8Y4L2A
  - 왜: LLM 의 근본 동작·sampling·prompting·fine-tuning 통합 멘탈 모델. 에이전트 설계 결정의 근거.
  - Takeaway:
- [&nbsp;] **"Intro to LLMs"** (2023, 1시간) — https://www.youtube.com/watch?v=zjkBMFhNj_g
  - 왜: tokenization·context·tool use·multimodal 까지. *왜 LLM 이 100단계 deterministic 명령을 못 따르는지* 의 근원 설명.
  - Takeaway:
- [&nbsp;] **Karpathy 트위터/X 최근 6개월** (스레드 모드) — https://x.com/karpathy
  - 왜: 짧지만 밀도 높은 에이전트·코딩·평가 관련 인사이트 다수
  - Takeaway:

### B. Anthropic 공식 가이드 — 에이전트 설계 원칙

Claude Code 를 만든 팀의 *공식* 입장. 가장 권위있는 1차 자료.

- [&nbsp;] **"Building Effective Agents"** (Anthropic, 2024) — https://www.anthropic.com/research/building-effective-agents
  - 왜: 에이전트 vs 워크플로 구분 + 5가지 표준 패턴 (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer). 우리 헌법 §3 사이클이 어디에 해당하는지 진단 가능.
  - Takeaway:
- [&nbsp;] **"Effective context engineering for AI agents"** (Anthropic) — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - 왜: context window 가 자원이라는 관점. 우리 markdown 4-5개/Phase 의 비용 계산.
  - Takeaway:

---

## Tier 2 — 실무 워크플로 (필수, ~6시간)

### C. Boris Cherny — Claude Code Lead 본인 워크플로

이 사람이 만든 도구. 어떻게 쓰는지가 가장 신뢰할 만한 reference 패턴.

- [&nbsp;] **howborisusesclaudecode.com** (전체) — https://howborisusesclaudecode.com/
  - 왜: 5 parallel sessions + auto-accept + worktree + skill 우선. 우리가 빠뜨린 모든 것.
  - Takeaway:
- [&nbsp;] **"How Boris Cherny Uses Claude Code"** (Karo Zieminski) — https://karozieminski.substack.com/p/boris-cherny-claude-code-workflow
  - 왜: 외부 관찰자의 정리. 핵심 패턴 압축.
  - Takeaway:
- [&nbsp;] **`--worktree` 발표 스레드** — https://www.threads.com/@boris_cherny/post/DVAAnexgRUj
  - 왜: 멀티 프로젝트 정답이 git worktree 라는 *공식* 입장.
  - Takeaway:

### D. Anthropic Claude Code 공식 문서 (선별)

- [&nbsp;] **Sub-agents** — https://code.claude.com/docs/en/sub-agents
  - 왜: 우리 7-agent 가 안티패턴인 *공식* 근거. *"context isolators, not workers"*.
  - Takeaway:
- [&nbsp;] **Hooks** — https://code.claude.com/docs/en/hooks
  - 왜: 우리가 subagent 로 처리하는 일들 중 절반이 hook 한 줄로 해결됨.
  - Takeaway:
- [&nbsp;] **Skills** — https://code.claude.com/docs/en/skills
  - 왜: Willison 이 *"bigger than MCP"* 라 한 이유. ux-reviewer 같은 에이전트의 대체.
  - Takeaway:
- [&nbsp;] **Channels** — https://code.claude.com/docs/en/channels
  - 왜: 우리 B14 spec 이 이미 공식 출시된 것의 정확한 구조.
  - Takeaway:
- [&nbsp;] **Agent Teams** — https://code.claude.com/docs/en/agent-teams
  - 왜: *"3-5 teammates for most workflows"* 소프트 캡의 근거.
  - Takeaway:

### E. Dan Shipper — Compound Engineering

매일 코딩하는 실무자가 어떻게 *학습 손실 없이* 시스템을 누적 개선하는가.

- [&nbsp;] **"Compound Engineering"** (Every) — https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents
  - 왜: B21 (즉시 반영 정책) 의 근원. 학습을 다음 프로젝트로 이연하지 않는 이유.
  - Takeaway:
- [&nbsp;] **"How I Use Claude Code to Ship Like a Team of Five"** (Every) — https://every.to/source-code/how-i-use-claude-code-to-ship-like-a-team-of-five-6f23f136-52ab-455f-a997-101c071613aa
  - 왜: 5x throughput 의 구체적 패턴. Claude Code 가 PR 100% 를 연다는 의미.
  - Takeaway:

---

## Tier 3 — 다양한 관점 (권장, ~4시간)

### F. Simon Willison — 신중한 안티패턴 비평가

가장 보수적인 관점. *manual PR review* 강조. 균형 잡기 위해.

- [&nbsp;] **"Anti-patterns: things to avoid"** — https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/
  - 왜: 우리가 빠지기 쉬운 함정 카탈로그. 짧고 강함.
  - Takeaway:
- [&nbsp;] **"Claude Skills are awesome, maybe a bigger deal than MCP"** — https://simonw.substack.com/p/claude-skills-are-awesome-maybe-a
  - 왜: Skills 시스템의 *왜 중요한가* 설명. 단일 markdown 의 위력.
  - Takeaway:
- [&nbsp;] **simonwillison.net AI 카테고리 최근 글** — https://simonwillison.net/tags/ai/
  - 왜: 매주 검증된 신호. 스레드 모드로 훑기.
  - Takeaway:

### G. Geoffrey Huntley — 극단적 자율 실험

반대 극단. 우리가 *얼마나 자율로 가도 되는가* 의 상한 측정. 꼭 따라하라는 게 아니라 *왜 어디까지 가능한지* 의 데이터 포인트.

- [&nbsp;] **"how-to-ralph-wiggum"** (GitHub) — https://github.com/ghuntley/how-to-ralph-wiggum
  - 왜: `while true` bash loop + 단일 markdown spec 으로 코드베이스 포팅. 헤비 ceremony 의 정확한 반대.
  - Takeaway:
- [&nbsp;] **"Six-month recap"** — https://ghuntley.com/six-month-recap/
  - 왜: 6개월간 무엇이 작동했고 안 했는지의 종합. 실험적 자세.
  - Takeaway:

### H. swyx — Self-verification & Quantitative Eval

*"how do you know it's working?"* 에 집착하는 관점. 우리 §B 시각 검증의 자동화 근거.

- [&nbsp;] **"Scaling without Slop"** (Latent Space) — https://www.latent.space/p/2026
  - 왜: Playwright iterate-until-pass + 수치 평가. §B 자동화 (B04) 의 깊은 근거.
  - Takeaway:

### I. Tim de Schryver — Keep Agentic AI Simple

우리 헌법의 절차주의를 가장 직접적으로 비판하는 관점.

- [&nbsp;] **"Keep Agentic AI Simple"** — https://timdeschryver.dev/blog/keep-agentic-ai-simple-a-practical-workflow-for-software-development
  - 왜: *"LLMs cannot reliably execute hundreds of deterministic steps from memory"* 인용의 출처. 우리 절차 카탈로그가 왜 fragile 한지.
  - Takeaway:

---

## Tier 4 — 깊이 추가 (선택, ~6시간)

### J. 다른 에이전트 프레임워크 (비교 학습)

같은 문제를 *다른 답*으로 푼 사례들. 우리 답의 상대화.

- [&nbsp;] **Aider 문서 + 핵심 패턴** — https://aider.chat/docs/usage.html
  - 왜: 단일 conversation + diff approval. 가장 미니멀.
- [&nbsp;] **Cline (구 Claude Dev) 문서** — https://docs.cline.bot/
  - 왜: 우리가 비슷한 패턴을 가진 *것을 들킨* 도구. 무엇을 다르게 했는지.
- [&nbsp;] **Cursor Composer Plan Mode 문서** — https://www.cursor.com/docs/agent
  - 왜: *one gate at plan* 의 정착된 패턴.
- [&nbsp;] **Devin (Cognition Labs) 공개 정보** — https://cognition.ai/blog
  - 왜: 가장 자율적인 상용 에이전트의 게이트 정책.

### K. Anthropic Engineering & Research 블로그 deep dive

- [&nbsp;] **anthropic.com/engineering 전체** (지난 6개월) — https://www.anthropic.com/engineering
  - 왜: 1차 자료. context engineering·MCP·hooks 의 진화 추적.
- [&nbsp;] **"How Claude Code Works"** — https://code.claude.com/docs/en/how-claude-code-works
  - 왜: 자동 컴팩션·skill 부착·subagent 격리의 *내부 동작*. 결정 비용 정확히 계산 가능.

---

## 학습 진행 가이드

### 추천 순서 (8~10주, 주 1~2 항목)

1. **Week 1-2**: Tier 1 A (Karpathy Software 2.0 + State of GPT) — 멘탈 모델 정립
2. **Week 3**: Tier 1 B (Anthropic 공식) — 설계 원칙
3. **Week 4**: Tier 2 C (Cherny) — 실무 reference
4. **Week 5-6**: Tier 2 D (Claude Code 공식 docs) — 도구 깊이 이해
5. **Week 7**: Tier 2 E (Shipper) — 누적 학습 패턴
6. **Week 8**: Tier 3 F·G·H·I (다양한 관점, 각 1편씩) — 균형
7. **(선택) Week 9-10**: Tier 4 — 깊이 더하기

### 학습 효과 자가 점검

각 항목 완료 시 위 체크박스 옆 한 줄 takeaway 기록. M01 Sprint 시작 시점에 사용자가 다음 질문에 답할 수 있어야 함:

- [&nbsp;] *"왜 7-agent 가 안티패턴인지 Cherny 의 근거 + 내 동의/반대 입장"*
- [&nbsp;] *"왜 1-gate-at-plan 이 산업 컨센서스인지 + 우리 솔로 학습 컨텍스트에서 이 결론이 유지되는지"*
- [&nbsp;] *"Compound Engineering vs Backlog-defer 의 trade-off + 우리 컨텍스트의 정답"*
- [&nbsp;] *"Channels·worktree·hooks·skills 4가지를 우리 헌법에 어떻게 통합할지의 구체 설계"*
- [&nbsp;] *"내 워크플로의 어떤 부분은 산업 컨센서스와 다른 길을 가고, 그 이유는 무엇인가"*

마지막 질문이 가장 중요. *"왜 다르게 가는가"* 의 명확한 답이 없으면 industry consensus 따라가는 게 안전.

---

## 진척도 요약

- Tier 1 (필수): 0 / 6 완료
- Tier 2 (필수): 0 / 8 완료
- Tier 3 (권장): 0 / 5 완료
- Tier 4 (선택): 0 / 6 완료

**M01 Sprint 트리거**: Tier 1 + Tier 2 = 14개 모두 `[x]` + 학습 효과 자가 점검 5개 모두 `[x]` 완료 시
