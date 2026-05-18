# Foundry Improvement Log (FIL) — Adopted Entries

**Status**: v0.3.0 candidate ledger · Authored 2026-05-18

본 ledger 는 *Foundry 표준으로 채택된* FIL entry 만 박제한다. 각 항목은 source project 의 `meta/foundry-improvement-log.md` 의 FIL-NNN 와 같은 번호를 *그대로 보존* (cross-reference 단순화). source project 측의 FIL 은 *raw* 단계로 그 자리에 유지, 본 ledger 는 *adopted* 단계.

> source project FIL 의 *raw* 본문은 변경하지 않는다. 본 ledger 는 *Foundry 표준으로 어떻게 박제했는가* 만 기록.

---

## 누적

### FIL-008 — Windows `desktop.ini` post-merge `.git` 트리 침투 (재현 가능 패턴)

- **Adopted**: 2026-05-18 (v0.3.0 candidate)
- **Source**: `12.subscription-payment-saas-platform` `meta/foundry-improvement-log.md#FIL-008` (2026-05-12 발견, 이후 6회 이상 재발)
- **증상 요약**: Windows OS 가 `.git/refs/` / `.git/objects/` 등 폴더에 `desktop.ini` 자동 생성 → `git fetch` / `git pull` 이 `fatal: bad object refs/...` 로 차단.

#### 표준 cleanup 스크립트 (PowerShell 5.1)

```powershell
$g = (git rev-parse --git-common-dir)
Get-ChildItem $g -Recurse -Force -Filter "desktop.ini" -ErrorAction SilentlyContinue | Remove-Item -Force
```

- *어디서나* 동작: working tree 또는 worktree 안에서 실행.
- `git rev-parse --git-common-dir` 가 main repo / linked worktree 모두 정확한 `.git` common dir 을 반환.
- worktree 의 *경로 식별* (`.git/worktrees/<name>/refs/`) 까지 자동 포함 — `-Recurse` 가 그것을 커버.

#### 적용 패턴

1. **post-merge / post-pull pipeline** — `git pull --ff-only` 직전에 cleanup 1회.
2. **post-PR squash merge** — `gh pr merge --squash --delete-branch` 직후 cleanup 1회 (origin refs 동기화 시 침투 차단).
3. **agent worktree 진입 시** — `git worktree add` 직후 cleanup 1회.
4. **manual recovery** — `fatal: bad object refs/desktop.ini` 발생 시 즉시 위 스크립트.

#### 자동화 후보 (Tier 2, 본 v0.3.0 에 미포함)

- `scripts/git-cleanup.ps1` + `factory.yaml` 의 `harness.git_cleanup_hook` 등록.
- post-pull / post-merge git hook 자동 호출.
- 본 v0.3.0 = *표준 스크립트 단편 박제* 만. 자동화는 v0.3.1+ 후보.

#### 참조

- source project `meta/foundry-improvement-log.md#FIL-008` (raw)
- 본 cycle 의 Foundry main repo 자체에서도 `.git/refs/tags/desktop.ini` 침투 → fetch 차단 → 위 스크립트로 직접 해소 (재현 N=7+)

---

### FIL-NEW (FIL-014 후보) — agent worktree 의 `.env.local` 부재로 validate/test ENOENT

- **Adopted**: 2026-05-18 (v0.3.0 candidate)
- **Source**: `12.subscription-payment-saas-platform` WP-005 cycle agent worktree 운용 중 noticed (FIL ledger 미박제 신규).
- **증상 요약**: `git worktree add` 로 생성된 agent worktree 에서 `npm run validate` / `npm test` 실행 시 `.env.local` 부재로 ENOENT 또는 dotenv warning + dev SDK init 실패.

#### 원인

- `git worktree` 는 *tracked files* 만 복사. `.env.local` 은 `.gitignore` 처리되어 untracked → agent worktree 에 부재.
- 그러나 Vitest / Next dev / Supabase SDK / TossPayments SDK 등이 *runtime 평가 단계* 에서 `.env.local` (또는 placeholder) 가 필요.

#### 표준 처리 (Implementer 책임, Director Card 발급 0)

agent worktree 진입 시 main worktree 의 `.env.local` 을 *읽기-전용 복사*:

```powershell
# agent worktree 경로 = $env:AGENT_WORKTREE (또는 cwd)
# main worktree 경로 = $env:MAIN_WORKTREE
$src = Join-Path $env:MAIN_WORKTREE ".env.local"
$dst = Join-Path (Get-Location) ".env.local"
if (Test-Path $src) { Copy-Item $src $dst -Force }
```

- `.env.local` 은 *agent worktree 내에서도 .gitignore* 가 그대로 적용되므로 commit 위험 0.
- worktree 종료 시 별도 cleanup 불필요 (worktree 삭제 시 함께 사라짐).
- 만약 `.env.local` 도 부재 (신규 clone 직후 등) → Director Card *별도* 필요 (secret handoff = HCP).

#### Anti-pattern

- ❌ Director 에게 `.env.local` 을 agent worktree 에 paste 하라고 카드 발급 — Director Card 4약속 조건 B (Implementer 가 할 수 있는 step) 위반.
- ❌ Implementer 가 `.env.local` 의 값을 chat 에 echo 하여 검증 — secret 노출.
- ❌ `.env.local` 을 git tracked 로 전환 — secret commit.

#### 참조

- source project 운용 중 N=2 cycle 에서 재현 (agent worktree 도입 cycle 부터 즉시 발생).
- `2_Reusable_Workflow_Modules/신규_프로젝트_생성_Workflow.md` (worktree 정책 정합)
- `4_Task_Level_Execution_Templates/claude-code/worktree/worktree-policy.md`

---

### FIL-WP005-pattern — read-mostly cycle 의 frozen file 1-block addition Director-gated extension 패턴

- **Adopted**: 2026-05-18 (v0.3.0 candidate)
- **Source**: `12.subscription-payment-saas-platform` WP-005 Planning (D-023, 2026-05-17) — WP-003 / WP-004 frozen body 의 *확장 가능* 패턴.

#### 패턴 정의

이미 *frozen* 또는 *closed* 된 cycle 의 산출물 (Spec / Design / Worklist / migration / SECURITY DEFINER RPC bundle 등) 을 **수정** 하지 않고, **신규 1-block addition** 으로 확장하는 패턴. 핵심:

1. **frozen body 변경 0** — 기존 줄 / 함수 / RPC / 정책의 본문 0 rewrite.
2. **신규 1 block 추가** — 동일 파일 끝에 새 RPC / 새 컬럼 / 새 정책 / 새 hook 을 append.
3. **Director-gated** — 신규 block 자체는 Planning Final CP 또는 Implementation Final CP 로 새 D-NNN 박제.
4. **read-mostly cycle 친화** — 신규 cycle 이 *주로 읽기* (예: Invoice / Statement / Audit) 이면 본 패턴이 자연 fit.

#### 예시 (WP-005)

- WP-005 가 D-020 의 SECURITY DEFINER RPC bundle 패턴을 확장하여 신규 RPC `cron_create_invoice_for_cycle` 추가.
- WP-003 / WP-004 의 frozen RPC body 0 rewrite.
- D-023 으로 박제, Planning Final CP 통과.

#### Anti-pattern

- ❌ frozen body 의 *작은 fix* (예: 변수명 오타) 를 묵시적으로 끼워 넣기 — frozen 정합성 깨짐. 별도 hotfix cycle 로 분리.
- ❌ 신규 block 을 *별도 파일* 로 분리 — 책임 경계 불명. 동일 파일 append 가 발견 가능성 ↑.
- ❌ Director-gate 없이 자동 진입 — frozen 확장은 *항상* Final CP 등급.

#### 참조

- source project D-023 (WP-005 Planning Final CP)
- source project D-020 (SECURITY DEFINER RPC bundle 원 패턴)
- `2_Reusable_Workflow_Modules/Meta_Sprint_Backport_Workflow.md` (frozen + add only 정합)

---

## 미채택 (보류 / 폐기) — 참고용

본 ledger 는 *채택된 항목만* 박제. source project 의 `meta/foundry-backport-candidates.md` 의 *보류 / 폐기 / 추가검토* 분류 항목은 본 ledger 에 *진입하지 않는다*. Meta Sprint 재진입 시 재평가.

현재 source project (`12.subscription-payment-saas-platform`) 의 미채택 FIL:

- FIL-001 (partial-block HCP) — 보류, 1 사례 부족
- FIL-009 (HCP sub-category pattern) — 보류 후보, N=2 cycle 누적 (WP-002 / WP-003), 본 v0.3.0 cycle 에 미포함 (D-025 + FIL-008/NEW/WP005 우선)
- FIL-012 (HCP-CRON-SCHEDULER staging vs production 분리) — 보류, FIL-009 와 함께 N=3 누적 시 일반화
- FIL-013 (clock injection / deterministic schedule test) — 보류, 시간축 cycle 첫 instance
- FIL-002 ~ FIL-007 — 이전 cycle 누적, 일부는 v0.2.1 frozen 시점에 이미 backport candidates 분류됨

다음 Meta Sprint (v0.3.1 또는 v0.4 candidate) 시 위 항목 재평가.
