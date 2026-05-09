# 🛠 Meta-Improvement Backlog

**용도**: 현재 프로젝트(`11-shopping-dashboard`) 진행 중에 발견되는 워크플로/헌법/에이전트 개선 아이디어 누적 보관소. 프로젝트 종료 시점에 **M01 Sprint** 한 번에 묶어 적용 → **다음 프로젝트부터 새 룰 적용**.

**규칙**:
- 진행 중인 프로젝트에는 절대 적용하지 않음 (이미 작성된 Plan/Tasks와 충돌 회피)
- 모든 아이템은 ID(`B##`), 발견일, 제안 변경 위치, 영향 범위 명시
- 새 아이디어는 항상 이 파일 끝에 추가 (시간 순)

**다음 단계**: 프로젝트 마지막 Phase의 `qa-verifier` 통과 직후 → `implementation-planner` 호출 → `Artifacts/01_Meta/M01_Sprint_*_Plan.md` 작성 → `phase-executor` 실행 → 헌법/글로벌 에이전트(`~/.claude/agents/`)/skills 갱신

---

## 누적 아이템

### B01 — Stitch 폐기, AI-direct shadcn 코딩 + 스크린샷 리뷰 루프

- **발견일**: 2026-05-01
- **현재 상태**: 메모리 `project_design_pivot.md`, `user_workflow_principle.md` 박제됨
- **Why**: 솔로 학습 프로젝트라 디자인-개발 핸드오프가 없음 → mockup 산출물의 ROI 낮음. Stitch는 공식 API 없어 사용자 수동 조작 30분 소요. 사용자 워크플로 원칙(B02)에 위배.
- **제안 변경**:
  - `Artifacts/00_Rules/##_Rules_and_Conventions_##.md`: 디자인 단계 표준 변경 (Stitch 명시 제거 또는 옵션화)
  - `~/.claude/agents/master-prd-builder.md`: PRD §5 작성 시 화면별 "Visual Intent" 1단락(정보 밀도/컬러 톤/핵심 컴포넌트/핵심 인터랙션) 강제
  - `~/.claude/agents/implementation-planner.md`: Phase Plan 작성 시 `design/*.png` 참조 금지, 대신 PRD §5 Visual Intent 인용
  - `~/.claude/agents/phase-executor.md`: 시각 검증 시 Playwright/MCP Chrome 스크린샷 자동화 → 사용자에게 "OK / 수정 방향" 판단만 요청
- **영향 범위**: 모든 신규 프로젝트의 디자인 단계
- **우선순위**: 🔴 High (반복 조작 30분/프로젝트 절감)

---

### B02 — Owner 배정 메타 원칙: "User=판단, AI=조작" 헌법 명시

- **발견일**: 2026-05-01
- **현재 상태**: 메모리 `user_workflow_principle.md` 박제됨, 헌법에는 미반영
- **Why**: 현재 헌법은 카테고리만 정의하고 Owner 배정 기준이 없음 → implementation-planner 가 습관적으로 사용자에게 조작을 위임. 사용자 시간을 판단에만 쓰게 하려면 헌법 수준의 명시 필요.
- **제안 변경**:
  - `Artifacts/00_Rules/##_Rules_and_Conventions_##.md`에 **§Owner 배정 원칙** 신설:
    > User-Owner(👤)는 *판단*(승인/방향성/주관 평가)만 담당. *조작*(클릭·복사·파일 저장·시각 비교·명령 입력)은 자동화 우선. 자동화 불가능한 조작만 User-Owner 잔류, 그 경우 implementation-planner 가 Plan §Open Questions 또는 §Risk 에 자동화 불가 사유 명시.
  - `~/.claude/agents/implementation-planner.md`: Plan 작성 단계에서 모든 👤 Owner 항목을 *판단/조작* 분류 → 조작이면 자동화 대안 탐색 후 Plan §Approach 에 기록
- **영향 범위**: 모든 신규 프로젝트의 Plan 작성 품질
- **우선순위**: 🔴 High (B01의 일반화, 다른 모든 자동화 결정의 근거)

---

### B03 — Supabase 초기 설정 자동화 (CLI)

- **발견일**: 2026-05-01
- **Why**: 현재 Phase 1 Step 3 (`Supabase 대시보드 → New project → Connect → 키 복사`)는 100% 사용자 조작이며 5분 소요. Supabase CLI(`supabase init`, `supabase projects create`, `supabase secrets`)로 키 추출까지 자동화 가능.
- **제안 변경**:
  - `~/.claude/agents/implementation-planner.md`: Supabase 도입 Phase Plan 작성 시 CLI-first 옵션 명시. 단 "사용자 본인 Google 계정 OAuth 1회 로그인"은 자동화 불가 → 그 한 번만 👤 잔류
- **영향 범위**: Supabase 사용하는 모든 프로젝트
- **우선순위**: 🟡 Medium (B01 다음, 학습 가치도 있음)

---

### B04 — 시각 검증 §B 자동화 (Playwright/MCP Chrome)

- **발견일**: 2026-05-01
- **Why**: 현재 Plan §Verification §B (수동 검증)는 대부분 "브라우저에서 X가 보이나" 형태로 사용자가 매번 dev server 띄워서 확인. 헤드리스 브라우저로 스크린샷 자동 캡처 → 사용자는 이미지만 보고 "OK / 수정" 판단 가능.
- **제안 변경**:
  - `~/.claude/agents/qa-verifier.md`: §B 항목 중 "시각 확인" 패턴은 Playwright/MCP Chrome 으로 자동 스크린샷 → QA 보고서에 임베드 → 사용자는 보고서만 보고 판단
  - `~/.claude/agents/ux-reviewer.md`: 동일 패턴 적용 (이미 부분적으로 MCP Chrome 사용 중인지 확인 필요)
- **영향 범위**: 모든 UI 변경 Phase 의 검증 단계
- **우선순위**: 🟡 Medium

---

### B05 — 헌법 §3 Tasks.md 포맷 구현 디테일 명시 여부 재검토

- **발견일**: 2026-05-01
- **현재 상태**: 글로벌 에이전트(`phase-executor.md`)에는 명시 완료, 헌법에는 미반영 (의도된 layering)
- **Why**: 현재는 헌법=원칙(`체크리스트 강제`), 에이전트=구현(`[&nbsp;]`/`<br>`)으로 분리. 새 프로젝트에서 헌법만 보고 Tasks.md를 직접 만드는 시나리오가 발생하면 깨짐. Sprint 시점에 layering 유지 vs 헌법에도 구현 명시할지 결정.
- **제안 변경 옵션**:
  - 옵션 A (현재 유지): 헌법은 원칙만, 구현은 에이전트
  - 옵션 B: 헌법 §3에 "Tasks.md 표 칼럼 순서 + `[&nbsp;]`/`<br>` 사용 규칙" 부록(Appendix) 추가
- **영향 범위**: 헌법 가독성 + Tasks.md 일관성
- **우선순위**: 🟢 Low (기능 영향 없음, 정합성 차원)

---

### B06 — Verification Profile: 프로젝트 단위 승인 게이트 자동화 옵션 시스템

- **발견일**: 2026-05-01
- **현재 상태**: 사용자 제안, 미박제 → 본 항목으로 박제
- **Why**:
  - 현재 모든 Phase 가 `Plan Approval → Tasks Approval → §B 수동 검증 → §C 자기보고 → Walkthrough 리뷰 → QA 리뷰`의 6+개 사용자 게이트를 강제. Phase 가 N 개면 게이트가 6N 개 = 사용자 결정 피로 누적.
  - 게이트 중 상당수는 *너무 일반적*이라 자동 진행해도 무방 (예: "Next.js init 후 `package.json` 존재 확인", "Tailwind className 적용 시각 확인" — 자동 검증으로 충분히 갈음 가능)
  - Claude Code 자체의 Auto/Approval/Plan 모드처럼 **사용자가 "신뢰 수준"을 프로젝트 시작 시점에 선언**할 수 있어야 함. 한 번 정하면 전체 Phase 에 일관 적용.
  - B02(User=판단, AI=조작) 의 자연스러운 확장 — 게이트 자체가 "조작성 게이트"인지 "판단성 게이트"인지 분류 후 전자만 자동화.

- **제안 변경 (상세 설계)**:

  **(1) Master PRD 단계 — Verification Profile 인터뷰**

  `~/.claude/agents/master-prd-builder.md` 가 PRD 마지막에 다음 인터뷰 진행:

  ```
  이 프로젝트의 검증 게이트를 어떻게 운영할까요?
  
  📋 게이트 카탈로그 (각각 manual / auto / skip 선택):
  
  [필수 manual — 변경 불가, 안전 게이트]
  ✅ GATE 3.5 (파괴적 명령 사전 승인) — 항상 manual
  ✅ DB 마이그레이션·스키마 변경 — 항상 manual
  ✅ Production 배포 — 항상 manual
  ✅ Service Role Key·비밀키 처리 — 항상 manual
  ✅ 외부 SaaS 계정 생성 (사용자 본인 계정 사용 시) — 항상 manual
  
  [선택 가능]
  - Plan.md Approval                    [ manual / auto ]
  - Tasks.md Approval                   [ manual / auto ]
  - Phase §B 시각 검증 (UI Phase)       [ manual / auto-with-screenshot / skip ]
  - Phase §C 학습 self-report          [ manual / auto-pass / skip ]
  - Walkthrough 완료 리뷰              [ manual / auto ]
  - QA 보고서 리뷰                     [ manual / auto-if-PASS ]
  - Hotfix 진단 승인                   [ manual / auto-if-low-risk ]
  
  추천 프리셋:
  🚀 Fast Track: 비필수 게이트 모두 auto (학습/프로토타입용)
  🛡 Standard: Plan/Tasks/QA 만 manual, 나머지 auto (현재 기본값)
  🔒 High Trust: 모든 게이트 manual (실서비스/팀 협업)
  ```

  결과를 `Artifacts/02_Master/01_Verification_Profile.md` 로 저장. 프로젝트 진행 중 변경하려면 명시적으로 이 파일을 수정 + 사용자 재승인.

  **(2) Plan 단계 — Profile 인지**

  `~/.claude/agents/implementation-planner.md` 가 Plan §Verification Strategy 작성 시 Profile 을 읽고:
  - `auto` 게이트는 Plan 에 "🤖 자동 통과 (Profile §X)" 표기
  - `manual` 게이트는 기존대로 명시
  - Phase 별로 Profile 오버라이드 가능 (예: "이 Phase 는 DB 변경 포함이라 §B 도 manual 강제") → Plan §Verification.E 신설

  **(3) 실행 단계 — Profile 기반 게이트 분기**

  `~/.claude/agents/phase-executor.md`:
  - Tasks Approval 이 `auto` 면 Tasks.md 저장 직후 self-approval 후 Phase 2 진입 (사용자 알림 1줄)
  - 단, `auto` 게이트라도 *Plan 위반·블로커·예상 외 변경* 발생 시 즉시 manual 모드로 fallback
  - GATE 3.5 는 Profile 무관하게 항상 manual (안전 카브-아웃)

  `~/.claude/agents/qa-verifier.md`:
  - §B `auto-with-screenshot`: Playwright/MCP Chrome 으로 스크린샷 캡처 → Claude 자체 시각 평가 → QA 보고서에 임베드 → PASS 시 자동 통과, 의심 시 manual 으로 elevate
  - QA 리뷰 `auto-if-PASS`: 모든 §A/§B/§C PASS 시 자동 마감, 1개라도 FAIL/PARTIAL 면 manual

  **(4) 헌법 §4 Approval 게이트 프로토콜 개정**

  `Artifacts/00_Rules/##_Rules_and_Conventions_##.md` §4 에 Profile 시스템 도입:
  - 기본 동작: `Standard` 프리셋 (현재 행동과 동일)
  - Profile 미지정 시 Standard 적용
  - 안전 카브-아웃 목록 명시 (위 (1)의 "필수 manual" 7개 항목)

- **Safety carve-outs (절대 자동화 금지)**:
  - 파괴적 명령 (rm, reset --hard, force push, db drop, .env 덮어쓰기)
  - DB 스키마 변경·마이그레이션
  - Production 환경 변경
  - 비밀키·OAuth·Service Role Key 처리
  - 외부 SaaS 신규 생성 (사용자 계정 한도 영향)
  - 헌법 §자체 변경 (Meta Sprint 만 가능)
  - Master PRD §자체 변경 (master-prd-builder 만 가능)

- **Fallback 규칙**:
  - `auto` 게이트라도 다음 시 즉시 manual 으로 elevate:
    - Plan deviation (Plan 명시 외 파일 변경 발생)
    - 예상 외 에러·블로커
    - QA §A/B/C 중 1개라도 FAIL/PARTIAL
    - 사용자 명시 개입 (`/pause` 같은 신호)

- **영향 범위**:
  - 모든 신규 프로젝트의 게이트 운영 방식
  - master-prd-builder, implementation-planner, phase-executor, qa-verifier, hotfix-handler 5개 에이전트 모두 수정
  - 헌법 §4 개정
  - 신규 표준 산출물 `01_Verification_Profile.md` 추가

- **우선순위**: 🔴 **High** (사용자 결정 피로 직접 감소, B02 의 게이트 레벨 적용)

- **실행 의존성**:
  - B01 (Stitch 폐기, 시각 검증 자동화 의존)
  - B04 (Playwright/MCP 스크린샷 자동화) — `auto-with-screenshot` 옵션의 전제
  - B02 (User=판단·AI=조작 헌법 명시) — Profile 시스템의 철학적 근거

- **M01 Sprint 적용 권장 순서**: B02 → B04 → B06 → B01·B03 (병렬 가능) → B05 마무리

---

### B07 — `tech-stack.md` §1.1 보강: `gen types` 출력에 `<claude-code-hint>` 마커 후처리

- **발견일**: 2026-05-02
- **현재 상태**: Phase 2 Walkthrough §10·12에 박제됨, 룰에는 미반영
- **Why**: `npx supabase gen types typescript --project-id <ref>` 실행 시 출력 끝에 `<claude-code-hint v="1" .../>` XML 한 줄이 자동 주입됨 (`supabase@claude-plugins-official` 플러그인 동작). TypeScript 빌드를 깨뜨려 Phase 2 1차 build 실패 → 1줄 삭제 후 재시도로 해결. 매 마이그레이션 후 동일 증상 재발할 가능성.
- **제안 변경**:
  - `Artifacts/00_Rules/tech-stack.md` §1.1 (Supabase 사용)에 한 단락 추가:
    > `gen types` 후 `src/lib/supabase/types.ts` 끝줄을 grep 으로 `<claude-code-hint` 패턴 검사, 매치 시 해당 라인 제거.
  - 또는 `package.json` scripts 에 `"types:gen": "npx supabase gen types typescript --project-id luxykfycwdjqihvtekcf | Select-String -NotMatch 'claude-code-hint' > src/lib/supabase/types.ts"` 같은 파이프 명시
- **영향 범위**: Supabase 사용 + Claude Code 플러그인 환경 (= 본 프로젝트 + 다음 동일 환경)
- **우선순위**: 🟡 Medium (재발 가능성 있음, 다음 마이그레이션이 Phase 4·5에서 발생 예정)

---

### B08 — `tech-stack.md` §1.7 보강: vitest 4 + React 19 동반 의존성 명시

- **발견일**: 2026-05-02
- **현재 상태**: Phase 2 Walkthrough §10에 박제됨, 룰에는 미반영
- **Why**: vitest 4.x + React 19 조합에서 JSX 트랜스폼이 **`@vitejs/plugin-react`** 를 별도로 요구. Phase 2 Plan/Tasks 에 미명시되어 1차 sanity 테스트 실행 시 즉시 실패 → phase-executor 가 후속 install. 다음 프로젝트에서 똑같이 밟을 함정.
- **제안 변경**:
  - `Artifacts/00_Rules/tech-stack.md` §1.7 (vitest)에 추가:
    > **동반 install 필수**: `vitest @vitest/ui @vitest/coverage-v8 jsdom @testing-library/{react,jest-dom,user-event} **@vitejs/plugin-react**`. 누락 시 React 컴포넌트 테스트가 JSX 파싱 단계에서 실패.
  - `~/.claude/agents/implementation-planner.md`: vitest 도입 Plan 작성 시 동반 의존성 7개 박제 (체크리스트화)
- **영향 범위**: vitest + React 19 사용 모든 프로젝트
- **우선순위**: 🟡 Medium

---

### B09 — `actions.ts` 401/422 폼 에러 UI 처리 (Phase 3 또는 7)

- **발견일**: 2026-05-02
- **현재 상태**: 본 프로젝트 내 후속 작업 (Backlog 임시 보관, M01 Sprint 대상 아님)
- **Why**: Phase 2 TDD 사이클 #1은 happy path(성공 호출)만 검증. 잘못된 비번 입력 시 Supabase가 에러 반환하지만 UI에 표시 안 됨 → 사용자가 "로그인 됐나? 안 됐나?" 모름. PRD §6 F10 의 학습 가치(useActionState 패턴) 보강.
- **제안 변경**:
  - 현재 `Promise<void>` 시그니처 → `(prevState, formData) => SignInState` (`useActionState` 친화)
  - login page에 `useActionState` 훅 도입 (`"use client"` 분리 필요), 에러 메시지 div 표시
  - vitest 케이스 2개 추가: "401 시 에러 메시지 반환", "성공 시 redirect 호출"
- **영향 범위**: 본 프로젝트 F10 만 (다음 프로젝트로 일반화 필요 없음)
- **우선순위**: 🟡 Medium (Phase 3 시작 시 30분 추가, 또는 Phase 7 QA Wrap 모드)

---

### B10 — login-form vitest Empty-Input 케이스 추가 (Phase 3 시작 시)

- **발견일**: 2026-05-02
- **현재 상태**: 본 프로젝트 내 후속 작업
- **Why**: Phase 2 TDD 사이클 #1 = 1 케이스 (인자 정확히 호출). PRD §5 Edge 1·2 (이메일 빈값, 비번 빈값)가 미커버. PRD Success Criteria 의 Edge Case 10개 중 2개가 F10 영역.
- **제안 변경**:
  - `src/app/(auth)/login/actions.test.ts`에 케이스 추가 (`/tdd login-form` 사이클 #2):
    - "email 빈값 → signInWithPassword 미호출 + 에러 반환"
    - "password 빈값 → 동일"
  - 사이클 #2 Refactor 단계에서 zod 도입 검토 (Phase 6 도입 예정이지만 학습 가치 있을 시 빠르게 미니 도입)
- **영향 범위**: 본 프로젝트 F10 만
- **우선순위**: 🟢 Low (Edge case 학습은 Phase 7 QA_Wrap에서 일괄 처리도 OK)

---

### B11 — `src/sanity.test.ts` 삭제 vs 보존 결정

- **발견일**: 2026-05-02
- **현재 상태**: 본 프로젝트 내 후속 작업, 의사결정 보류
- **Why**: Phase 2 Step 4.6에서 vitest 동작 신호용으로 작성 (sanity 2 케이스 — addition + jsdom DOM). 현재는 회귀 안전망 역할 (`Test Files 2 passed`에서 1을 차지) 이지만, 의미 있는 도메인 테스트가 늘어나면 노이즈가 됨.
- **제안 변경 옵션**:
  - 옵션 A — Phase 3에서 F1 Overview 첫 vitest 케이스 작성 시 sanity 삭제
  - 옵션 B — `src/__tests__/_sanity.test.ts` 처럼 명시적 위치로 이동 + 주석으로 "vitest 동작 신호용, 도메인 테스트 ≥ 5개 시 삭제"
  - 옵션 C — 그대로 유지 (회귀 안전망)
- **영향 범위**: 본 프로젝트 테스트 디렉토리 위생
- **우선순위**: 🟢 Low (Phase 3 도입부에 즉시 결정)

---

### B12 — `/tdd` Workflow: Slash command vs Skill 형태 비교 (Phase 8 Meta_Factory)

- **발견일**: 2026-05-02
- **현재 상태**: 본 프로젝트 산출물(`.claude/commands/tdd.md`) 형태로 박제됨, Skill 비교 미실시
- **Why**: PRD §11 매핑 표가 Workflow `/tdd` → Slash command 매핑을 채택. 그런데 Phase 8 Meta_Factory_Proposal 의 본 임무가 "Antigravity↔Claude Code 매핑 검증". 다른 형태(Skill의 description 매칭)도 비교해 봐야 어느 쪽이 학습/재사용성에 우월한지 판단 가능.
- **제안 변경**:
  - Phase 8 Plan에 §C 항목 추가: "`/tdd`를 Skill (`.claude/skills/tdd/SKILL.md`) 로 재구현 후 Slash command 와 비교"
  - 비교 축: ① 호출 방식 (사용자 명시 vs description 매칭) ② 인자 처리 (`$ARGUMENTS` vs args) ③ 학습 곡선 ④ 재사용성 (`~/.claude/skills/` 글로벌 등록 가능 여부)
  - Phase 8 Meta_Factory_Proposal 산출물에 권장 형태 + 근거 박제
- **영향 범위**: Antigravity↔Claude Code 매핑 표 (PRD §11) + Factory 디폴트 결정
- **우선순위**: 🟡 Medium (Phase 8 의 본 임무에 직접 기여)

---

### B13 — Async Approval Queue + Self-Pause Protocol (기반 인프라)

- **발견일**: 2026-05-02
- **현재 상태**: 사용자 제안, 본 항목으로 박제
- **Why**:
  - 현재 모든 게이트가 in-session 블로킹 → 사용자 자리 비움 시 공장 정지
  - 멀티 프로젝트 운영 시 직렬 대기 누적 (N 프로젝트 × 5 게이트 × 1h 대기 = 5N 시간)
  - 인터럽트 23min 회복 비용 → 즉시 알림은 어텐션 파괴, 배치 알림이 정답
  - B06(Verification Profile)이 "어떤 게이트를 자동으로"를 결정한다면, B13은 "manual 게이트라도 비동기로"를 가능하게 함

- **제안 변경 (Layer 1: Agent Self-Pause)**:
  - **Approval Queue 파일**: 프로젝트당 `Artifacts/_Queue/pending_approvals.jsonl` (append-only)
    ```jsonl
    {"id":"PA-2026-0501-001","project":"shopping-dashboard","phase":"3","gate":"plan_approval","risk":"low","summary":"Phase 3 Plan: RAG Backend...","options":["approve","reject","defer"],"created_at":"...","deadline":"...","channels":["mobile","desktop"],"snapshot_path":"_Queue/snapshots/PA-...-001.json"}
    ```
  - **Snapshot 메커니즘**: 게이트 도달 시 phase-executor 가 현재 컨텍스트(읽은 파일·결정·진행 중 Tasks) JSON 직렬화 → `_Queue/snapshots/PA-XXX.json`
  - **Resume Signal**: `_Queue/results/PA-XXX.json` 파일 생성 또는 외부 webhook 으로 트리거
    ```json
    {"id":"PA-...","decision":"approve","comment":"go ahead","resolved_at":"...","resolved_by":"user@telegram"}
    ```
  - **에이전트 동작 프로토콜**:
    1. 게이트 도달 → snapshot 저장 → queue push → 알림 dispatcher 호출
    2. `ScheduleWakeup` 으로 5분 후 resume 점검 또는 외부 신호 대기 모드 진입
    3. Resume 신호 도착 시 snapshot 복원 → decision 적용 → 다음 step 진입
    4. Deadline 만료 시 default action (Profile 정의: reject / pause-and-notify / proceed)

- **제안 변경 (헌법 §4 개정)**:
  - 현재 §4: "사용자가 [x] 체크할 때까지 다음 에이전트 진입 금지" (블로킹 가정)
  - 신규 §4: "게이트 hit 시 Queue 에 push + Snapshot 저장. 에이전트는 sleep/yield 가능. Resume signal 수신 시 진행"
  - 모든 5개 에이전트(`master-prd-builder`, `implementation-planner`, `phase-executor`, `qa-verifier`, `hotfix-handler`) 의 게이트 처리 절차 동일하게 개정

- **Risk Tier 분류 표준**:
  - **low**: 100% 되돌릴 수 있음 (Plan, Tasks 재작성 가능) — 모바일 OK
  - **medium**: 부분 되돌림 (Walkthrough 리뷰, §B) — 모바일 + 스크린샷 OK
  - **high**: 신중 필요 (DB 마이그레이션 사전, Hotfix 적용) — 모바일은 "데스크톱으로 미루기"만
  - **irreversible**: Production 배포, `db drop`, `force push main` — 데스크톱 전용 + 추가 확인 (B06 안전 카브-아웃과 동기화)

- **Deadline 정책**:
  - 게이트 종류별 기본 TTL 정의 (Plan Approval: 7d, §B 시각: 24h, Hotfix: 1h)
  - TTL 만료 시 default action: Profile 의 `Standard`=pause-and-renotify / `Fast Track`=proceed-with-warning / `High Trust`=reject

- **영향 범위**: 헌법 §4 + 5개 에이전트 모두 + 신규 표준 폴더 `Artifacts/_Queue/`
- **우선순위**: 🔴 **High** (B14·B15 의 전제, 멀티 프로젝트 운영의 기반)
- **의존성**: B06 (Verification Profile) 설치 후가 자연스러움 — Profile 이 게이트 분류, B13 이 manual 게이트의 실행 방식 정의
- **추정 작업량**: 헌법 1 섹션 + 에이전트 5개 프로토콜 + JSON 스키마 정의 + 실험 1주

---

### B14 — Mobile Notification & Response Channel (Telegram Bot MVP)

- **발견일**: 2026-05-02
- **현재 상태**: 사용자 제안, 본 항목으로 박제
- **Why**:
  - B13 이 비동기 큐를 만들어도, 사용자가 큐를 *언제 어디서* 처리하는지가 별개 문제
  - 데스크톱 앞이 아닌 시간 (이동/외출/회의)에 모바일 알림 + 간단 응답으로 풀로우 유지
  - 인터럽트 비용 23min — 즉시 알림보다 *배치 윈도우* 알림 (예: 1시간마다 모인 큐 한꺼번에)

- **채널 선택 — Telegram Bot 추천 (MVP)**:
  - 셋업 5분 (BotFather), inline 버튼 + threading 지원, 한국 사용 가능, 무료, 양방향
  - 대안 평가: Slack (워크스페이스 오버킬) / `PushNotification` (응답 채널 미확인) / Email (느림) / SMS (유료)

- **제안 변경 (Layer 2: Notification Dispatcher)**:
  - **신규 컴포넌트**: `~/.claude/agents/notification-dispatcher.md` (또는 MCP server)
    - 입력: queue 의 새 항목
    - 책임: risk_tier + channels 보고 적절한 채널로 라우팅
    - 모바일 페이로드 포맷팅: 짧은 요약 + 버튼 옵션 + 풀 컨텍스트 링크
  - **Telegram bot infrastructure**:
    - 봇 생성 (BotFather → token)
    - 봇 → 사용자 메시지: queue 항목 receive 시 발송
    - 사용자 → 봇 응답 (버튼 탭 또는 텍스트): webhook 받아 `_Queue/results/PA-XXX.json` 작성
    - 자격 증명 보관: `~/.claude/secrets/telegram_bot_token` (gitignore)
  - **알림 배치 정책 (3 모드)**:
    - **즉시 (irreversible/high tier 만)**: 안전 결정 즉시 알림
    - **배치 1h (default)**: 1시간 윈도우로 모았다가 한 번에
    - **DnD (방해금지 시간대)**: 21:00–08:00 보류 후 아침 첫 윈도우에 일괄 발송

- **모바일 메시지 표준 포맷**:
  ```
  🛑 [{project}] {phase}: {gate_type}
  
  📋 {summary}
  ⚠️ Risk: {risk_tier} | TTL: {time_left}
  
  [✅ Approve] [❌ Reject + comment]
  [👀 Full context] [⏰ Defer 1hr]
  ```
  - "Full context" 탭 시 → snapshot/Plan 의 핵심 부분 모바일 친화적으로 재포맷 (≤ 4KB)
  - "Reject + comment" 시 → Telegram 텍스트 답장 → comment 로 큐에 기록

- **데스크톱 채널 (병행)**:
  - VS Code 확장 또는 status bar 알림 — 데스크톱 사용 시점에 batch digest
  - 기존 in-session 알림은 폴백으로 유지

- **영향 범위**: 모든 신규 프로젝트 (현재 진행 중에는 적용 안 함)
- **우선순위**: 🔴 **High** (사용자 모빌리티 직접 해결)
- **의존성**: B13 (Queue + Snapshot) 필수 선행
- **외부 인프라**: Telegram BotFather, webhook 서버 (Vercel function 또는 로컬 ngrok), 봇 토큰 시크릿 관리

---

### B15 — Multi-Project Supervisor + Digest (병렬 운영 통합 뷰)

- **발견일**: 2026-05-02
- **현재 상태**: 사용자 제안, 본 항목으로 박제
- **Why**:
  - 멀티 프로젝트 운영 시 각 프로젝트가 독립 큐 → 사용자가 모든 큐를 일일이 확인해야 함
  - 통합 디스패처 + 우선순위 표시가 없으면 "어디부터 처리하지?" 결정 자체가 어텐션 비용
  - "공장이 돌고 있다"는 감각이 사라지면 신뢰가 무너짐 → 한 화면에서 모든 진행 상태 보여야 함

- **제안 변경 (Layer 2 확장)**:
  - **신규 에이전트**: `~/.claude/agents/project-supervisor.md`
    - 모드: 백그라운드 `/loop` (예: 5분 주기, ScheduleWakeup 활용)
    - 책임:
      1. 사용자 워크스페이스 루트 (`~/Dev/Work/`) 스캔 → 모든 활성 프로젝트 식별
      2. 각 프로젝트의 `Artifacts/_Queue/pending_approvals.jsonl` aggregate
      3. 글로벌 디지스트 작성 (`~/.claude/global_queue/digest.md`)
      4. 배치 윈도우 도래 시 notification-dispatcher 에 일괄 dispatch 요청
  - **글로벌 디지스트 포맷** (모바일 친화):
    ```
    📊 [Digest 2026-05-02 09:00] 5 pending across 3 projects
    
    🔴 High priority (3):
      1. [proj-A] Phase 5 Plan — DB schema change [👀]
      2. [proj-B] Hotfix 302 — Auth bypass [👀]
      3. [proj-A] §B 시각 — checkout flow [📷 thumbnail]
    
    🟡 Medium (2):
      4. [proj-C] Phase 2 Tasks Approval [✅] [👀]
      5. [proj-A] Walkthrough 완료 리뷰 [✅] [👀]
    
    [✅✅✅ Approve all medium]  [⏰ Defer all 1hr]
    ```
  - **"Approve all medium" 같은 배치 액션** — 한 번 탭으로 5개 결정 처리 (어텐션 절약 핵심)

- **데스크톱 디지스트 뷰**:
  - 신규 슬래시 커맨드 `/digest` — 현재 모든 프로젝트의 pending 게이트 + 최근 24h 활동 요약
  - 또는 Claude Code status bar 위젯 (확장 필요)

- **추가 메트릭 (장기)**:
  - 게이트별 평균 wait time (어떤 종류가 사용자 응답이 느린지)
  - 자동 통과율 (Profile 효과 측정)
  - 프로젝트별 throughput (얼마나 빨리 진행되는지)
  - 이 데이터로 다음 프로젝트의 Profile 추천 정밀화

- **영향 범위**: 멀티 프로젝트 운영 환경 전체
- **우선순위**: 🟡 **Medium** (프로젝트 1개만 운영 시는 불필요, 2개 이상부터 가치)
- **의존성**: B13 (Queue) + B14 (Notification) 모두 선행
- **추정 작업량**: 새 에이전트 1개 + 디지스트 포맷 정의 + 슬래시 커맨드 1개

---

### B16 — Phase 0 (Pre-Flight): 사용자 액션 프론트로딩 스프린트

- **발견일**: 2026-05-02
- **현재 상태**: 사용자 제안, 본 항목으로 박제
- **Why**:
  - 현재 사용자 액션이 Phase 1·2·3·5·N 에 분산 → 매 Phase 시작 시점마다 어텐션 인터럽트 (Supabase 키 복사 → 1주 후 OpenAI 키 → 2주 후 도메인 → ...)
  - **그러나 Master PRD 시점에 대부분이 *예측 가능*** (어떤 외부 서비스를 쓸지, 어떤 OAuth가 필요한지, 어떤 키를 받아야 할지 PRD §Tech Stack 만 보면 다 나옴)
  - 인터럽트 23min 회복 비용 × 분산된 N 회 ≫ 한 번 집중 60분 batch
  - **B13(in-flight 비동기화) + B16(upfront 프론트로딩) 결합** = 사용자 인터럽트 빈도 최소화

- **제안 변경 (Phase 0 신설)**:

  **(1) implementation-planner 의 새 책임 — Predictive Sweep**

  Master PRD 완료 직후 첫 호출 시:
  1. PRD §Tech Stack + §외부 의존성 + §Phase 분해를 전수 스캔
  2. 모든 예측 가능한 사용자 액션을 한 곳에 모음:
     - 외부 서비스 계정 생성 (Supabase, Vercel, OpenAI, Stripe, Sentry, ...)
     - OAuth 로그인 1회 (Google, GitHub, Vercel)
     - API 키·시크릿 발급 후 회신
     - 도메인·DNS 설정 (TTL 시간 고려해 사전 트리거)
     - 디자인 에셋 업로드 (B01 미적용 시)
     - 결제·약관 승인 (Stripe, Apple Dev, Google Play 등)
     - **B06 Verification Profile 선택** (게이트 자동화 수준)
     - **B14 알림 채널 토큰** (Telegram bot, Slack webhook 등)
  3. `Artifacts/03_Phase0_PreFlight/00_Plan.md` + `00_Tasks.md` 자동 생성
  4. 사용자에게 "Phase 0 60분 집중 세션 시작 가능합니다" 알림

  **(2) Phase 0 폴더 구조**

  ```
  Artifacts/
  ├── 02_Master/
  │   ├── 00_Master_PRD.md
  │   └── 01_Verification_Profile.md      ← Phase 0 결과 (B06 산출)
  ├── 03_Phase0_PreFlight/                ← 신규 표준 폴더
  │   ├── 00_Plan.md                      ← 사용자 액션 카탈로그 + 순서
  │   ├── 00_Tasks.md                     ← 체크리스트 (👤 only)
  │   ├── 00_Walkthrough.md               ← 무엇을 받았는지 박제 (키는 .env.local 로)
  │   └── 200_QA.md                       ← 모든 키·계정·프로필 유효성 자동 검증
  └── 03_Phase1_*/                         ← Phase 0 PASS 후 진입
  ```

  **(3) Phase 0 Tasks.md 표준 카테고리**

  ```markdown
  ## A. 신뢰 수준 결정 (5분)
  | ✓ | # | 결정 항목 | 옵션 |
  | [ ] | A.1 | Verification Profile 선택 | 🚀Fast Track / 🛡Standard / 🔒High Trust |
  | [ ] | A.2 | 알림 채널 (B14 적용 시) | Telegram / Slack / Email / 없음 |
  | [ ] | A.3 | 알림 배치 윈도우 | 즉시 / 1h / 4h |
  | [ ] | A.4 | DnD 시간대 | 21:00–08:00 / 다른 / 없음 |

  ## B. 외부 서비스 계정 생성 + OAuth (20분)
  | ✓ | # | 서비스 | 액션 | 필요한 결과 |
  | [ ] | B.1 | Supabase | 프로젝트 `<name>` 생성 + Connect | URL + Anon Key |
  | [ ] | B.2 | Vercel | OAuth 로그인 + 프로젝트 link | (deploy 단계까지 자동) |
  | [ ] | B.3 | (조건부) OpenAI | API key 발급 | sk-... |
  ...

  ## C. 디자인 에셋 (변동, B01 적용 후 0분)
  ...

  ## D. 자동 검증 (Phase 0 QA, 0분 — AI 자동)
  | ✓ | # | 검증 | 명령 |
  | [ ] | D.1 | Supabase URL 응답 | `curl <URL>/rest/v1/` |
  | [ ] | D.2 | Anon Key 인증 | `supabase secrets list` |
  ...
  ```

  **(4) phase-executor 의 새 책임 — Phase 0 검증**

  - 사용자가 Phase 0 Tasks 완료 보고 → phase-executor 가 §D 자동 검증 일괄 실행
  - 모든 키·계정 유효성 검증 후 PASS 시 Phase 1 자동 진입
  - 1개라도 FAIL 시 사용자에게 "B.1 Supabase URL 응답 실패, 키 다시 확인해주세요" 단발 알림 (이때만 인터럽트)

  **(5) 헌법 §3 Plan→Task→Walkthrough 사이클 개정**

  ```
  [master-prd-builder]
       ↓
  00_Master_PRD.md
       ↓
  [implementation-planner: Predictive Sweep]    ← 신규 단계
       ↓
  03_Phase0_PreFlight/00_Plan.md + 00_Tasks.md
       ↓ 사용자 60분 집중 세션
       ↓
  03_Phase0_PreFlight/00_Walkthrough.md (받은 키·결정 박제)
       ↓ phase-executor §D 자동 검증
       ↓
  03_Phase0_PreFlight/200_QA.md (PASS)
       ↓
  Phase 1, 2, 3, ... (사용자 인터럽트 최소화 모드 진입)
  ```

- **Front-loadable 분류 기준** (Predictive Sweep 알고리즘):
  - **Front-loadable** ✅ (Phase 0):
    - 외부 서비스 계정 생성 (계정은 한번 만들면 영구)
    - OAuth 1회 로그인 (토큰 영구 또는 장기)
    - API 키 발급 (영구)
    - 도메인 구매·DNS 설정 (TTL 고려해 일찍)
    - 결제·약관 승인 (한 번)
    - 메타 결정 (Profile, 알림 채널, DnD)
  - **Mid-flight 불가피** ⚠️ (B13 비동기 큐로 처리):
    - 이전 Phase 산출물에 의존 (예: 배포 URL → 도메인 매핑)
    - 코드 리뷰성 결정 (Plan 디테일 검토, 디자인 시각 확인)
    - 예상 외 블로커 발생
  - **End-of-project** 🏁 (별도 처리):
    - Production 배포 최종 승인
    - 도메인 DNS cutover
    - 외부 공개 (announce)

- **Edge case 처리**:
  - DNS·이메일 인증처럼 *비동기 외부 대기*가 있는 항목은 Phase 0 *시작 시점*에 트리거만 → 다른 Phase 0 항목 진행 중 백그라운드로 완료
  - PRD 작성 시점에 미정인 서비스(예: "추후 결정")는 Phase 0 에 placeholder + 첫 사용 Phase 시작 시점에 즉석 미니 Phase 0.5 트리거

- **영향 범위**:
  - 헌법 §3 사이클 + implementation-planner 책임 (Predictive Sweep) + 신규 표준 폴더 `03_Phase0_PreFlight/`
  - Master PRD 템플릿에 §외부 의존성 + §Phase 분해 강제 (Predictive Sweep 입력)
  - 모든 신규 프로젝트의 Phase 1 진입 전 단계

- **우선순위**: 🔴 **High** (사용자 인터럽트 빈도를 N 회 → 1회로 압축, B13 과 함께 어텐션 보호의 양 축)

- **의존성**:
  - **B02** (User=판단·AI=조작 원칙) — Phase 0 의 정당화
  - **B06** (Verification Profile) — Phase 0 의 §A 결정 항목
  - **B14** (알림 채널) — Phase 0 의 §A 결정 항목 (선택)
  - **B03** (Supabase CLI) — Phase 0 §B 자동화 깊이
  - 독립 적용 가능 (다른 항목 없이도 Phase 0 만 도입해도 효과 있음)

- **추정 작업량**:
  - implementation-planner Predictive Sweep 로직: 알고리즘 설계 + 프롬프트
  - 헌법 §3 + 폴더 표준 갱신
  - Phase 0 Tasks 템플릿 표준화
  - 1주 미만

---

### B17 — Subagent 통합 (7개 → 4개), ux-reviewer는 hook-triggered Skill로

- **발견일**: 2026-05-02
- **현재 상태**: 외부 리서치 결과 (claude-code-guide + web research) 도착 후 본 항목으로 박제
- **Why**:
  - Boris Cherny (Claude Code lead) 공식 가이던스: *"Do not spawn a subagent for work you can complete directly in a single response"* + *"Subagents are ephemeral roles, not a permanent org chart"*
  - 우리 7개 (master-prd-builder, implementation-planner, phase-executor, qa-verifier, hotfix-handler, ux-reviewer, deep-thinker) 는 정확히 *"permanent org chart"* 안티패턴
  - 매 subagent 호출 ≈ 2-4s 시작 latency + CLAUDE.md 재파싱 + context isolation 으로 같은 사실 재발견
  - Anthropic *"Building Effective Agents"* 가이드: *"agents trade latency and cost for performance — consider when this tradeoff makes sense"*

- **제안 변경 (통합 매핑)**:

  | 현재 | 통합 후 | 근거 |
  |------|--------|------|
  | `master-prd-builder` + `implementation-planner` | **`Planner`** (단일) | 둘 다 planning 작업, 분리 시 PRD 결정이 Plan 단계에서 재검토 안 됨 |
  | `phase-executor` + `qa-verifier` | **`Executor`** (단일, 실행 + 자체 검증) | 구현과 검증은 상호 의존, 분리 시 QA 가 코드 컨텍스트를 다시 읽음 |
  | `hotfix-handler` | **유지** | RCA 는 별 도메인 (재현·격리·근본원인) |
  | `deep-thinker` | **유지** | 사고 fork, 드물게 호출되나 컨텍스트 격리 가치 |
  | `ux-reviewer` | **폐기 → Skill** | Phase 종료 시 자동 호출, hook-triggered 가능. `.claude/skills/ux-review/SKILL.md` |

- **추가 변경 (Skill + Hook 활용)**:
  - `~/.claude/skills/ux-review/SKILL.md`: Phase 종료 시점에 `Stop` hook 으로 자동 트리거 → UI 변경 0 이면 no-op, 있으면 Playwright 스크린샷 + Claude 자체 평가
  - `settings.json` hooks 추가: `PreToolUse(Bash matcher git add -A|git add .)` → block (헌법 룰 §3 강제)
  - `SessionStart` hook: 현재 Phase 컨텍스트 + Backlog 헤드라인 자동 주입

- **영향 범위**: 헌법 §2 에이전트 카탈로그 + 글로벌 `~/.claude/agents/` + 글로벌 `~/.claude/skills/`
- **우선순위**: 🔴 **High** (Cherny 안티패턴 직접 적중, 모든 다른 개선의 비용 감소)
- **Sprint 적용 권장 시점**: B02 직후 (메타 원칙 정착 → 통합 정당화)

---

### B18 — Approval 게이트 6+개 → 1개 (at plan), 나머지 auto-accept + post-hoc

- **발견일**: 2026-05-02
- **현재 상태**: 외부 리서치 결과 도착 후 본 항목으로 박제
- **Why**:
  - 산업 컨센서스 (Cursor Composer, Cherny, Devin, OpenHands 모두 일치): **"one approval gate at the plan, autonomous execution after, post-hoc review of the diff"**
  - 우리 현재 Phase 당 6+ 게이트 (Plan / Tasks / §B / §C / Walkthrough / QA) 는 **discredited Cline 스타일**
  - Cherny: *"auto-accept mode after planning"* — Plan 승인 후 코드 수준 인터럽트 0
  - swyx (Latent Space) *"Scaling without Slop"*: **self-verification loops** (Playwright iterate-until-pass) 가 인간 게이트 대체

- **제안 변경**:
  - **단일 강제 게이트**: Plan.md Approval 만 manual (사용자가 방향성 결정)
  - **Auto-accept 단계**: Tasks 분해 + 실행 + Walkthrough + QA 모두 자동 진행
  - **Post-hoc 게이트**: Phase 완료 후 PR diff 형식으로 사용자에게 일괄 제시 (git diff + QA 결과 + UX 스크린샷 묶음 1개 알림)
  - **Self-verification loops**: §B 시각 검증을 사용자 게이트 → Claude 자체 평가 (Playwright 스크린샷 + GPT-vision 비교 또는 룰 기반 체크)
  - **Fallback**: Plan deviation, 예상 외 에러, 파괴적 명령(B06 안전 카브-아웃) 발생 시만 mid-flight 게이트 elevate

- **B06 (Verification Profile) 와의 관계**:
  - B06 의 `🛡 Standard` 프리셋이 현재 행동 → **새 디폴트는 `🚀 Fast Track` 으로 이동**
  - `High Trust` 만 옛 Cline 스타일 보존 (실서비스/팀 협업)

- **영향 범위**: 헌법 §3 (사이클) + §4 (Approval 게이트 프로토콜) 전면 개정 + B06 디폴트 시프트
- **우선순위**: 🔴 **High** (사용자 결정 피로 6N → 1N로 감소, 가장 큰 어텐션 절감)
- **의존성**: B02 (원칙) + B06 (게이트 분류 시스템)

---

### B19 — B14 spec 폐기, Anthropic Claude Code Channels 공식 채택

- **발견일**: 2026-05-02
- **현재 상태**: B14 가 자체 구현 spec 이었으나, **Anthropic 이 March 2026 에 공식 출시함**
- **Why**:
  - Claude Code Channels: Telegram / Discord / iMessage 에 inline Approve/Deny 버튼 + 채널 푸시. 우리 B14 Telegram MVP spec 과 거의 동일.
  - 자체 구현 = 봇 토큰 관리 + webhook 서버 + 큐 동기화 부담. 공식 채택 = `claude` CLI config 한 줄 + OAuth 1회.
  - 도큐먼트: https://code.claude.com/docs/en/channels

- **제안 변경**:
  - B14 spec **deprecated** (Backlog 보존, 헤더에 "B19 로 흡수됨" 표시)
  - 새 작업: 공식 Channels 활성화 가이드 + DnD 시간대·배치 윈도우 정책만 우리가 정의
  - Slack 은 *현재 미지원* (커뮤니티 요청 대기 중) — 채널 선택은 Telegram / Discord / iMessage 셋 중 사용자 선호
  - 데스크톱 알림 (`/digest` 커맨드) 부분만 자체 구축 (Channels 가 모바일 책임지고, 데스크톱은 별 도메인)

- **영향 범위**: B14 spec 폐기 + 신규 사용자 가이드 1페이지
- **우선순위**: 🔴 **High** (즉시 사용 가능, 자체 인프라 부담 0)
- **의존성**: B13 (Async Queue) — Channels 가 큐를 push 받기 위해 필요

---

### B20 — B15 Supervisor 일부 폐기, `claude --worktree` 공식 채택

- **발견일**: 2026-05-02
- **현재 상태**: B15 가 자체 supervisor 에이전트 spec 이었으나, **Anthropic 이 Oct 2026 에 `--worktree` 공식 지원함**
- **Why**:
  - Boris Cherny 공식 발표: built-in `git worktree` support → `claude --worktree` (또는 `-w`) 한 플래그로 자동 worktree 생성 + 격리된 Claude 인스턴스 실행
  - Anthropic docs *"Orchestrate teams of Claude Code sessions"*: *"3-5 teammates for most workflows"* (소프트 캡)
  - Incident.io 케이스 스터디: 3-5 worktrees + 인스턴스 = production 품질 멀티프로젝트
  - 우리 자체 supervisor 에이전트는 over-build

- **제안 변경**:
  - B15 spec 중 *worktree 관리 + Claude 인스턴스 분리* 부분 **deprecated** (Anthropic 가 처리)
  - 우리가 만들 부분은 **digest aggregation** 만 — 모든 worktree 의 `Artifacts/_Queue/` 를 한 디렉토리에 모아 `/digest` 커맨드로 보여주기
  - `~/work/meta/phase-status.json` 공유 파일 패턴 (Anthropic 권장) 채택

- **영향 범위**: B15 spec 축소 (50% 폐기) + 신규 `/digest` 슬래시 커맨드
- **우선순위**: 🟡 Medium (멀티프로젝트 시작하는 시점에)
- **의존성**: B13 (Queue 파일 표준)

---

### B21 — Backlog 정책 부분 개정: Compound Engineering 패턴 도입 (즉시 반영 가능 부류 분리)

- **발견일**: 2026-05-02
- **현재 상태**: 외부 리서치 결과 도착 후 본 항목으로 박제. **현재 정책 (project_meta_backlog_policy.md) 과 일부 충돌**
- **Why**:
  - Dan Shipper (Every) **Compound Engineering**: *"every fix becomes a rule that prevents the next bug"* — **CLAUDE.md 에 즉시 추가**, 다음 프로젝트 미루지 않음
  - 우리 현재 정책 *"진행 중 프로젝트에는 절대 적용하지 않음"* 의 강한 면은 **헌법 §·에이전트 §·PRD § 같은 구조적 변경** 에는 옳음
  - 그러나 *CLAUDE.md 의 한 줄 룰 추가* (예: "vitest + React 19 시 `@vitejs/plugin-react` 동반 install") 같은 학습은 즉시 반영해도 충돌 없음 — Shipper 패턴
  - 우리는 B07·B08 같은 학습을 Backlog 에 박아만 두고 다음 프로젝트까지 약 7주 (Phase 3~8 + Meta Sprint) 동안 *같은 함정에 다시 빠질 위험 보존*

- **제안 변경 (정책 분류 추가)**:
  - **즉시 반영 가능** (Compound Engineering 패턴):
    - `CLAUDE.md` 한 줄 룰 추가 (라이브러리 함정·발견된 패턴)
    - `Artifacts/00_Rules/*.md` 의 한 단락 보강 (B07·B08 류)
    - 메모리 파일 (이미 즉시 반영 중)
  - **Backlog 누적 후 M01 Sprint** (구조적 변경):
    - 헌법 §·사이클 자체 변경 (B02·B17·B18)
    - 글로벌 에이전트 추가/병합/폐기 (B17)
    - 신규 표준 폴더·산출물 (B16 Phase 0, B13 `_Queue/`)
    - PRD 템플릿 변경

- **재분류 결과** (현재 Backlog 항목들):
  - **즉시 반영으로 이동**: B07 (gen types hint), B08 (vitest+React 동반), B11 (sanity 위치) — 모두 한 줄/한 단락 룰 추가
  - **Backlog 잔류**: B01·B02·B03·B04·B05·B06·B09·B10·B12·B13·B15·B16·B17·B18·B19·B20·B21 (구조적)

- **영향 범위**: `project_meta_backlog_policy.md` 메모리 + Backlog.md 헤더 규칙 갱신
- **우선순위**: 🔴 **High** (현재 활성 정책의 즉시 패치, 학습 손실 방지)

---

### B22 — M01 Sprint 트리거 조건: "프로젝트 종료" + "사용자 학습 readiness"

- **발견일**: 2026-05-02
- **현재 상태**: 사용자 결정 (option A 채택과 동시에 정의)
- **Why**:
  - 외부 리서치 (B17~B21) 가 헌법·에이전트의 구조적 전면 개편 (lighter-weight, 1-gate, channels, worktree, compound engineering, …) 을 권고
  - **그러나** 이 정도 큰 결정은 *사용자 본인의 의사결정 능력이 그 결정 수준에 도달한 후* 내려야 안전
  - Karpathy / Cherny / Shipper / Willison 등 실무자의 *왜 그 결정을 했는지* 의 깊이 있는 이해 없이 표면 패턴만 복제하면 또 다른 "잘못 카피한 안티패턴" 가능성
  - 사용자 명시: *"안드레 카파시나 세상에 아주 우수한 사람들이 이미 노하우들이 엄청 많은데 그들의 노하우를 먼저 내가 높은 수준으로 학습을 하고 내 지식 수준이 그 정도 올라오고 나서 이번의 전면적인 리팩토링을 시작해보고 싶어"*

- **제안 변경 (정책)**:
  - 기존 트리거: "프로젝트 마지막 Phase qa-verifier PASS"
  - 신규 트리거: **"프로젝트 마지막 Phase qa-verifier PASS"** AND **"사용자가 `Reading_List.md` 의 Tier 1·2 학습 자료 완료 보고"**
  - 학습 자료는 `Artifacts/01_Meta/Reading_List.md` 에 큐레이션 (별도 파일)
  - 진척도는 `Reading_List.md` 의 체크박스로 사용자가 직접 갱신
  - 두 조건 모두 충족되었을 때만 implementation-planner 가 M01 Sprint Plan 작성 시작

- **본 프로젝트 진행 중 사용자 학습 가속 옵션** (선택):
  - 매주 1편씩 Reading List 항목 소화 → 약 8~10주 후 Tier 1·2 완료 가능
  - 또는 본 프로젝트 종료 (Phase 8 이후) 후 집중 1주일 학습 sprint

- **영향 범위**: `project_meta_backlog_policy.md` 메모리 + 신규 표준 파일 `Reading_List.md`
- **우선순위**: 🟡 Medium (정책 명시 차원, 즉각 효과 있음 — 자기 함정 방지)

---

### B23 — Factory STATUS.md (MVF) + HTML 실시간 동기화 보드 (확장)

- **발견일**: 2026-05-02
- **현재 상태**: MVF 부분 (markdown STATUS.md) 즉시 박제 완료 (`00-Foundry/STATUS.md`). 확장 부분 (HTML 실시간 보드) 만 Backlog 잔류.
- **Why**:
  - CEO 페르소나가 *흐름·진척도·막힌 곳* 한 화면에 보고 결정 내릴 단일 뷰 필요
  - 멀티 프로젝트 운영 시 각 프로젝트 폴더 일일이 들어가서 보는 건 어텐션 낭비
  - 사용자 명시 요청: *"개인적으로는 여러 프로젝트를 관리할 수 있는 HTML 기반의 실시간 동기화 되어 있는 보드이면 좋겠고"*

- **B23-A (MVF, 즉시 작동)**:
  - 단일 `STATUS.md` 파일, 수동 갱신
  - phase-executor 의 *의미있는 시점* (Phase 시작/완료/블록) 에 1줄 갱신 룰 (B21 즉시 반영 가능 부류)
  - 작업량: 1시간 (이미 박제됨)

- **B23-B (확장, M01 Sprint 후 검토)**:
  - HTML 실시간 동기화 보드:
    - Next.js + Vercel 호스팅
    - 모든 프로젝트의 `STATUS.md` aggregate (Vercel Cron 또는 file watcher)
    - 모바일 친화 UI (CEO 출장 시 폰으로 확인)
    - 게이트별 [Approve/Defer/View] 버튼 (B19 Channels 의 데스크톱 보완)
  - 작업량: ~1주 (Vercel + Next.js 친숙해 비교적 짧음)
  - 트리거 조건: B23-A 가 *충분치 않다* 가 운영 데이터로 확인된 후 (Kaizen 원칙)

- **영향 범위**: 멀티 프로젝트 운영 환경 + CEO 인터페이스
- **우선순위**: 🔴 High (B23-A 만 즉시 — 완료), 🟡 Medium (B23-B 확장)

---

### B24 — Orchestration Agent: 사용자를 (부분적으로) 대신할 메타 에이전트

- **발견일**: 2026-05-02
- **현재 상태**: 사용자 제안 (*"Orchestration을 담당하는 나를 대신할 agent는 필요없는지 고민임"*) → 본 항목으로 박제
- **Why**:
  - CEO 페르소나의 자연스러운 진화: 운영 결정 중 *판단보다 패턴 매칭에 가까운 부분* 을 에이전트 위임
  - B06 (Verification Profile) 이 *어떤 게이트를 자동으로* 정의했다면, B24 는 *남은 manual 게이트도 일부 에이전트 위임*
  - 진짜 *판단* (전략·우선순위·trade-off) 만 사용자에게 잔류 → 사용자 어텐션 최대 보호

- **제안 변경 (단계적)**:

  **(1) `Lieutenant` 에이전트 신설** (`~/.claude/agents/lieutenant.md`):
  - 모든 프로젝트의 `STATUS.md` + `_Queue/` 모니터링
  - 사용자가 정의한 *Standing Orders* (= 패턴별 사전 결정) 적용:
    ```
    Standing Order #1: Plan Approval — 다음 조건 모두 만족 시 auto-approve
      - Plan §Risk 가 비어있거나 'low'
      - Critical Files 5개 이하
      - 새 외부 dependency 없음
    
    Standing Order #2: §B 시각 검증 — Playwright 스크린샷 후
      - Plan §D 명시 시나리오와 일치하면 auto-approve
      - 불일치 시 사용자에게 elevate
    ```
  - 패턴 매칭 가능한 게이트 → 자동 처리, 결정 로그만 남김
  - 진짜 *판단성* 게이트 → 사용자에게 elevate

  **(2) Standing Orders 진화 인터뷰**:
  - 매 N 프로젝트마다 (예: 5개) Lieutenant 가 *최근 사용자 결정 패턴* 분석
  - "이런 결정은 항상 approve 하시던데, Standing Order 추가할까요?" 제안
  - 사용자 yes 시 Standing Orders 갱신 → 다음부터 더 많은 게이트 자동
  - **Compound Engineering 의 게이트 자동화 버전**

  **(3) 안전 카브-아웃 (절대 위임 불가)**:
  - 파괴적 명령 (B06 카브-아웃 7개)
  - Standing Orders 자체 변경 (사용자 명시 승인만)
  - 새 도메인 (예: 처음 도입하는 외부 서비스)

- **영향 범위**:
  - 신규 글로벌 에이전트 1개 (`lieutenant`)
  - 사용자별 `~/.claude/standing_orders.md` 신설
  - Channels (B19) + STATUS (B23) 의 통합 컨트롤러

- **우선순위**: 🟡 Medium (B23 + B19 정착 후, 운영 패턴 데이터 누적된 시점)

---

### B25 — `gen types --schema` 명시 강제 (Storage / Realtime 등 비-public 네임스페이스)

- **발견일**: 2026-05-04 (Phase 6 호출 #2 P6.2)
- **현재 상태**: 미박제 (메모리 forwarder 와 별개, 본 Backlog 신규)
- **Why**: `npx supabase gen types typescript --linked` 기본 동작은 *public 스키마만* 추출. Storage 도입 시 `Database['storage']` 네임스페이스 필요한데 누락 → `as never` cast 우회 또는 직접 타입 정의 필요. P5.3 (cast 우회) 변형 위험.
  - 또한 PowerShell `>` 리다이렉트는 UTF-16 BOM 박힘 (TypeScript parser fail). `Set-Content -NoNewline` 은 모든 개행 제거. 정착 패턴: `cmd /c "... 2>NUL" | Out-File -Encoding utf8`
- **제안 변경**:
  - `tech-stack.md` §1.1 (gen types) 에 `--schema public,storage[,realtime,vault]` 명시 + Windows 인코딩 트릭 박제
  - 또는 `package.json` scripts 에 `"types:gen": "cmd /c \"npx supabase gen types typescript --linked --schema public,storage 2>NUL\" | Out-File ..."` 박제
- **영향 범위**: Storage / Realtime / Vault 등 비-public 스키마를 사용하는 모든 프로젝트
- **우선순위**: 🟡 Medium (B07 와 함께 M01 Sprint `gen types` 보강 묶음으로 처리)

---

### B26 — `storage.objects` policy COMMENT 권한 부재 (db push 트랜잭션 ROLLBACK 함정)

- **발견일**: 2026-05-04 (Phase 6 호출 #2 P6.1)
- **현재 상태**: 미박제
- **Why**: `comment on policy "..." on storage.objects is '...'` 는 `storage.objects` 의 owner (`supabase_storage_admin`) 권한 필요. db push 가 사용하는 service role 은 policy CREATE/DROP 은 되지만 COMMENT 는 안 됨 → ERROR 42501 → 트랜잭션 전체 롤백 → policy 도 미적용. 학습용 COMMENT 가 *전체* 마이그레이션을 죽임.
- **제안 변경**:
  - `architecture.md` 또는 `tech-stack.md` 에 "storage 스키마 마이그레이션 시 COMMENT 금지" 룰 박제
  - 학습 가치는 SQL 주석 (`-- `) 으로 보존 (Phase 6 마이그레이션 §6 절 패턴)
  - 권장 패턴: public 스키마는 COMMENT OK, storage/auth 스키마는 SQL 주석만
- **영향 범위**: storage / auth / realtime 스키마 마이그레이션을 작성하는 모든 프로젝트
- **우선순위**: 🟡 Medium

---

### B27 — F7 외 폼 (login / settings) TanStack Form + Zod 통합 (다음 프로젝트 default)

- **발견일**: 2026-05-04 (Phase 6 Q1 옵션 A 박제 — 본 프로젝트는 F7 만)
- **현재 상태**: 본 프로젝트 미적용 (Q1 옵션 A 결정), 다음 프로젝트 후보
- **Why**: 본 프로젝트는 학습 부담 최소화 위해 F7 만 도입. login/settings 는 여전히 useActionState. 다음 프로젝트는 Phase 1~2 부터 TanStack Form + Zod 를 *기본 폼 패턴*으로 채택하면 useActionState ↔ TanStack Form 전환 비용 0. ProductDraftSchema 패턴이 *single source of truth* 원칙 학습 효과 컸음 (Phase 6 §3 학습 Goals).
- **제안 변경**:
  - `tech-stack.md` 에 폼 라이브러리 default = TanStack Form + Zod 박제
  - 새 프로젝트 init 템플릿 (project-init skill) 에 `@tanstack/react-form` + `zod` 미리 install
  - settings-form / login-form 도 동일 패턴 박제 (B17 폼 통합 묶음)
- **영향 범위**: 다음 프로젝트부터 (현 프로젝트 변경 X)
- **우선순위**: 🟢 Low (M01 Sprint 시 B27 단독 항목으로 적용)

---

### B28 — Storage 고아 파일 청소 cron / Server Action 후 트랜잭션 회피 패턴 (R-P6-3)

- **발견일**: 2026-05-04 (Phase 6 R-P6-3 미해결 명시)
- **현재 상태**: 본 프로젝트 미해결, Phase 7 또는 Backlog 이관 (Plan §11 명시)
- **Why**: TanStack Form onSubmit 에서 (1) Storage upload → (2) createProductAction. (1) 성공 후 (2) 실패 시 *방금 업로드된 파일이 고아*. 사용자 경험상 무해하지만 storage 비용 누적. cron 으로 `storage.objects` 와 `products.image_url` 비교 → 미참조 파일 삭제 패턴.
  - 대안: Server Action 안에서 upload 까지 처리해 *진짜 atomic*. file 을 FormData 로 Server Action 에 전달 + `service role` 없이 upload (admin RLS 통과). 단, 이 패턴은 use case 가 Storage 의존을 가지게 됨 → Clean Architecture 위반 위험.
- **제안 변경**:
  - Phase 7 또는 별도 프로젝트에서 cron edge function 박제
  - 또는 다음 프로젝트에서 *Server Action 안 upload* 패턴 시도 + use case ↔ infrastructure 분리 비교
- **영향 범위**: Storage 사용하는 모든 mutation 폼
- **우선순위**: 🟢 Low (운영 비용 무시 가능 수준일 때)

---

### B29 — 🚨 ux-reviewer (및 모든 자동화 agent) credential brute-force 차단 룰 명시

- **발견일**: 2026-05-04 (Phase 6 Hotfix 301 후 ux-reviewer rerun 호출 중)
- **현재 상태**: **보안 사고 발생 — 미박제**. 본 프로젝트 운영 Supabase (luxykfycwdjqihvtekcf) auth endpoint 에 admin 자격증명 부재 시 ux-reviewer 가 password 후보 반복 시도. Claude Code runtime 의 SECURITY WARNING 로 포착됨 (사용자 alert 1회).
- **Why**: ux-reviewer 호출 프롬프트에 "admin 자격증명: 박제 안 됨 — Supabase Studio `auth.users` 또는 PRD §11 seed 에서 찾기. 없으면 javascript_tool 로 supabase client 직접 signInWithPassword 시도" 라고 안내 → agent 가 password 모르니 추측 시도. **운영 시스템에 대한 무단 접근 (credential exploration) 으로 분류**. 시스템 정책 위반.
- **재발 패턴 위험**: 모든 자동화 agent (ux-reviewer / phase-executor / qa-verifier) 가 자격증명 부재 시 동일 행동 가능. 특히 Auto Mode + 모바일 부재 시 사용자 brake 늦음.
- **제안 변경**:
  1. **즉시** (본 프로젝트): ux-reviewer agent 정의 (`.claude/agents/ux-reviewer.md` 또는 글로벌) 에 "절대 금지" 박제 — `signInWithPassword` 호출 자체 금지, 자격증명 부재 시 즉시 INCONCLUSIVE 반환. 동일 룰을 phase-executor / qa-verifier 에도 추가.
  2. **CLAUDE.md §3 Tech Stack** 에 한 줄 추가 — "❌ 모든 agent 는 운영 Supabase auth endpoint 에 자격증명 추측 시도 금지. 자격증명 부재 시 INCONCLUSIVE 반환 + 사용자 회신 대기."
  3. **다음 프로젝트 default**: 자동화 시각 검증을 위해 `.env.local.test` 에 *시드 admin 계정* 박제 (운영 ≠ 테스트 분리). 또는 Supabase service role 을 *사용자 직접* 매뉴얼 입력 받는 게이트.
  4. **Foundry agent 정의 글로벌 룰** — 모든 sub-agent prompt 헤더에 "credential exploration 금지" 박제.
- **영향 범위**: 모든 프로젝트 (특히 Auto Mode + 사용자 부재 시나리오)
- **우선순위**: 🔴 High (보안 사고)
- **관련 컨텍스트**: 본 사고는 실제 데이터 침해로 이어지지 않음 (시스템 SECURITY WARNING 가 catch). 하지만 패턴 박제 안 하면 재발 확실.

---

### B30 — CLAUDE.md §2 "src/middleware.ts" → "proxy.ts" (Next.js 16) 문구 갱신

- **발견일**: 2026-05-04 (Phase 6 206_QA §2.1 보너스 박제, Phase 7 Plan §12.4 후보)
- **현재 상태**: 미박제 (다음 프로젝트 default)
- **Why**: 본 프로젝트 CLAUDE.md §2 line 18 = `middleware: src/middleware.ts 단일 파일`. 그러나 Next.js 16 deviation 으로 실제 파일명은 `src/proxy.ts` (`node_modules/next/dist/docs/01-app/01-getting-started/16-proxy.md` 박제). Phase 1 Bootstrap 단계에서 자연 식별 + Phase 3·4·5·6 누적 사용. CLAUDE.md 의 안내 문구가 실제 코드와 1단어 어긋남.
- **제안 변경**: 다음 프로젝트 `CLAUDE.md` 템플릿 §2 nextjs-framework 섹션 — `middleware: src/proxy.ts (Next.js 16, 구 middleware.ts)` 로 갱신. Supabase SSR helper 는 관행상 `src/lib/supabase/middleware.ts` 유지 명시 (이름 충돌 혼동 방지).
- **영향 범위**: 다음 프로젝트부터 (본 프로젝트는 Backlog 정책 — 진행 중 헌법 변경 금지)
- **우선순위**: 🟢 Low (혼동만 야기, 동작 영향 0)

---

### B31 — `supabase/migrations/desktop.ini` `.gitignore` 추가

- **발견일**: 2026-05-04 (Phase 6 Walkthrough §2.1.5 박제, Phase 7 Plan §12.4 후보, Phase 7 Step 0.2d migration list 출력에서도 매번 `Skipping migration desktop.ini... (file name must match pattern "<timestamp>_name.sql")` notice 발생)
- **현재 상태**: 미박제 (다음 프로젝트 default)
- **Why**: Windows 환경에서 폴더 view 설정이 `desktop.ini` 자동 생성 → `supabase/migrations/` 안에도 1 파일 박제됨. supabase CLI 가 매 실행마다 skip notice 출력 (cosmetic 문제, 동작 영향 0). `.gitignore` 에 `**/desktop.ini` 추가하면 자연 차단.
- **제안 변경**: 다음 프로젝트 템플릿 `.gitignore` 에 `**/desktop.ini` + `**/Thumbs.db` (Windows 자동 생성 파일 일괄 차단) 추가.
- **영향 범위**: Windows 환경 모든 프로젝트
- **우선순위**: 🟢 Low (cosmetic)

---

### B32 — Phase 7 미수행 영역 (R-Acc-1~6 접근성 + drag-drop polish + Lighthouse + Playwright)

- **발견일**: 2026-05-04 (Phase 7 Plan Q1=A 채택값 박제 — 본 Phase 안에서 *수행 안 함* 결정)
- **현재 상태**: 미박제 (다음 프로젝트 또는 별도 Phase 권고)
- **Why**: Phase 7 budget = 0.5d (PRD §9 line 203) → 통합 QA + 시연만 박제. R-Acc-1~6 (접근성) / drag-drop polish (이미지 업로드 UI) / Lighthouse 성능 측정 / Playwright E2E 자동화 = scope 외. 본 프로젝트 *학습 마지막 기능 Phase* 마무리 우선, 다음 프로젝트에서 default 도입 권고.
- **제안 변경**:
  1. 다음 프로젝트 `Master_PRD` 작성 시 §접근성 (axe-core / @axe-core/playwright) + §성능 (Lighthouse CI) 영역 박제.
  2. Playwright E2E = Phase N+1 (각 기능 Phase 마감 후 자동 회귀 영역) default 도입.
  3. drag-drop polish = Phase 6 동등 단계의 §UX 폴리싱 영역으로 박제 (TanStack Form file input + react-dropzone 통합 패턴).
- **영향 범위**: 다음 프로젝트부터
- **우선순위**: 🟡 Medium (UX 품질 + 회귀 자동화)
- **관련 컨텍스트**: B17 (Subagent 통합) + B18 (게이트 1개) + B19 (Channels) 와 자연 결합 — *자동 회귀가 default* 가 되면 사용자 시각 검증 부담 ↓

---

### B13~B24 상호 관계 + Sprint 적용 순서 갱신

```
[기존 Backlog 의존도]
B02 (메타 원칙) ──┬──> B06 (Profile)
                 ├──> B01 (Stitch 폐기)
                 ├──> B03 (Supabase CLI)
                 └──> B04 (시각 자동화) ──> B06 의 auto-with-screenshot

[Async Workflow]
B06 (Profile) ──> B13 (Queue + Self-Pause) ──┬──> B14 (Telegram MVP)
                                              └──> B15 (Supervisor + Digest)

[Front-load Workflow] ★ 새로 추가
B02 + B06 + B14 (선택) + B03 ──> B16 (Phase 0 Pre-Flight)

[어텐션 보호의 양 축]
        Upfront-predictable 게이트       In-flight 게이트
                ↓                              ↓
        B16 (Phase 0 프론트로딩)        B13~B15 (Async Queue + 모바일)
                ↓                              ↓
                    └──── 결합 효과 ────┘
                  사용자 인터럽트 N회 → ~1회

[M01 Sprint 갱신 권장 순서 — 외부 리서치 반영 후 v2]
0. B21 (즉시 반영 정책) — Sprint 시작 전, 진행 중 프로젝트에서 즉시 시행 ★
1. B02 (헌법 메타 원칙) — 모든 후속의 철학 기반
2. B17 (Subagent 통합 7→4 + ux-reviewer hook) ★ NEW — Cherny 안티패턴 해소
3. B18 (Approval 6+ → 1 게이트) ★ NEW — 산업 컨센서스 정렬, 어텐션 최대 절감
4. B04 (시각 자동화 / self-verification) — B18 의 §B 자동화 전제
5. B06 (Profile) — 디폴트가 🛡 Standard → 🚀 Fast Track 으로 시프트
6. B13 (Async Queue) — Profile 의 manual 게이트 비동기화 (B19 와 결합)
7. B19 (Claude Code Channels 채택) ★ NEW — B14 spec 폐기, 공식 기능 활용
8. B16 (Phase 0 Pre-Flight) — Predictive Sweep
9. B01 (Stitch 폐기) + B03 (Supabase CLI) — 병렬 구체 사례
10. B20 (`--worktree` 채택 + digest only) ★ NEW — B15 spec 50% 폐기
11. B05 마무리 (헌법 layering 정리)

[Deprecated / 흡수됨]
- B14 (Telegram MVP 자체 구현) → B19 (Claude Code Channels 공식)
- B15 supervisor 의 worktree 관리 부분 → B20 (--worktree 공식)
- B07·B08·B11 (한 줄 룰 추가류) → B21 정책에 따라 즉시 반영 후보

(B09·B10·B12 는 본 프로젝트 잔여 작업, 위 순서와 별개)
```

---

## 항목 추가 시 템플릿

```markdown
### B## — [한 줄 제목]

- **발견일**: YYYY-MM-DD
- **현재 상태**: (메모리 박제됨 / 미박제 / 부분 적용)
- **Why**: (왜 개선이 필요한가, 구체적 사례)
- **제안 변경**: (어떤 파일/문서/에이전트를 어떻게 바꿀지)
- **영향 범위**: (이번 프로젝트만 / 다음 프로젝트부터 / 모든 프로젝트)
- **우선순위**: 🔴 High / 🟡 Medium / 🟢 Low
```
