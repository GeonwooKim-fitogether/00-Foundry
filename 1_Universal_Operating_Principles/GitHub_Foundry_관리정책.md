# L1 Principle — GitHub Foundry 관리정책

> **Layer**: 1 — Universal Operating Principles (invariant).
> **상태**: v0.2.1 candidate (2026-05-08 도입).
> 본 원칙은 모든 프로젝트와 모든 머신에 *예외 없이* 적용된다.

## 1. 핵심 명제
**00-Foundry 는 AI-NPI Factory 의 단일 Source of Truth 다.** 다른 모든 머신·프로젝트·산출물은 Foundry 의 *어떤 commit* 에서 유래했는지 항상 답할 수 있어야 한다.

## 1A. 두 개의 행위 — 동기화 vs. Seed 복사 (★ 매우 중요)

본 정책에서 *Foundry 가 관여하는 git 행위* 는 정확히 두 종류이며, **이 둘은 서로 다른 행위다**. 혼동하면 본 정책의 의도가 깨진다.

| 구분 | **A. 00-Foundry 자체의 동기화** | **B. 신규 프로젝트의 Seed 복사** |
|---|---|---|
| **목적** | Foundry 원본을 머신 간 / 시간 간 *동일 상태로 유지* | 신규 프로젝트에 Foundry 의 *특정 시점 상태* 를 *씨앗* 으로 가져옴 |
| **방향성** | 양방향 — pull (가져옴) + commit / push (반영함) | 단방향 — Foundry → 신규 프로젝트로의 1회성 복사 |
| **허용 도구** | **GitHub clone / pull / commit / push 만** | git clone (특정 tag/commit), git archive, 또는 단순 폴더 복사 (commit 좌표만 박제하면 OK) |
| **빈도** | 작업 시작·종료 시 매번 | 신규 프로젝트 생성 시 1회 |
| **변경 후 어디로?** | Foundry 원본 ↔ GitHub 으로 commit/push | 신규 프로젝트 폴더 안에서만 자유롭게 수정 (그 변경은 Foundry 로 자동 backflow 되지 않음) |
| **결과 산출물** | `00-Foundry/` 가 항상 GitHub 의 main/tag 와 정렬됨 | 신규 프로젝트의 `factory.yaml.factory_source.{repo, version, commit, copied_on}` 박제 |
| **본 정책 §2 의 어느 규범** | §2.1 단일 동기화 채널 + §2.2 안정 version 보존 + §2.4 추적되지 않는 로컬 변경 지양 | §2.3 신규 프로젝트의 좌표 박제 |

핵심 경계:
- **A 는 절대 GitHub 외 채널을 쓰지 않는다.** USB / 클라우드 sync / 머신 간 폴더 복사 모두 금지. 추적이 끊기면 Foundry 의 `current = ?` 가 답이 안 된다.
- **B 는 단순 폴더 복사도 허용된다 — 단, 좌표 박제가 *반드시* 동반된다.** Seed 는 *어느 시점의 Foundry 인가* 가 영구 추적 가능해야 함이 본질. 폴더가 어떻게 거기 도달했는가 (clone vs zip 다운로드 vs 다른 경로) 는 부차적.
- **A 와 B 는 같은 명령처럼 보일 수 있으나 의미가 다르다.** `git clone <foundry-url>` 을 *기존 머신에 처음 Foundry 를 두기 위해* 실행하면 A. 같은 명령을 *신규 프로젝트의 seed 마련을 위해* 실행하면 B (다만 이 경우 보통 `git clone --depth 1 -b vX.Y.Z` 같은 형태가 자연스러움).

자세한 B 절차: [신규_프로젝트_생성_Workflow §3](../2_Reusable_Workflow_Modules/신규_프로젝트_생성_Workflow.md#3-절차-10단계).

## 2. 규범
1. **GitHub 단일 동기화 채널** — `00-Foundry` 는 GitHub repo (private 권장) 로만 동기화한다. clone / pull / commit / push 외의 동기화 수단 (USB, Drive, OneDrive, 직접 폴더 복사) 은 *금지*. 이유: commit 추적이 끊기면 *어디서 유래했는지* 답할 수 없어 본 원칙의 핵심 명제가 무너진다.
2. **안정 version 의 보존** — 안정 version 은 git tag (`v0.2.0`, `v0.2.1` 등) 또는 `factory.yaml.factory.status: frozen` 으로 표식한다. 한 번 frozen 된 version 은 *과거에 대해 변경되지 않는다.* 정정이 필요하면 새 patch version 으로 발행.
3. **신규 프로젝트의 좌표 박제** — 모든 신규 프로젝트는 `factory.yaml/factory_source` 블록에 4 필드 (`repo`, `version`, `commit`, `copied_on`) 를 *반드시* 기록한다. 한 번 결정되면 프로젝트 종료까지 *변경하지 않는다.* 새 version 으로 옮길 때는 별도 *Migration Critical Decision* 으로 진행.
4. **추적되지 않는 로컬 변경 지양** — clone 후 *Foundry 폴더 내부* 의 임의 수정 금지. 발견사항은 *프로젝트의 `meta/foundry-improvement-log.md`* 에만 누적. 정말 불가피하면 프로젝트 측 `factory.yaml.local_modifications: true` 박제 + 사유 명기.
5. **Meta Sprint 만이 Foundry 진화 경로** — 진행 중인 한 프로젝트의 1회 사례로 Foundry 원본을 즉시 수정하지 않는다. 누적된 증거를 [Meta_Sprint_Backport_Workflow](../2_Reusable_Workflow_Modules/Meta_Sprint_Backport_Workflow.md) 절차로 처리한 *후* 에만 원본 변경.

## 3. 다중 머신 운영
- 각 머신은 독립적으로 `git clone <foundry-repo>` 하고, *항상* 작업 시작 전 `git pull origin <branch>` 로 동기화한다.
- 머신 간 직접 파일 복사 (zip 전송 등) 금지.
- branch 전략: 단순 `main` 단일 branch + tag 기반 release 권장. 복잡한 GitFlow 불필요 (단일 사용자 모델).
- 머신 별로 진행 중 *프로젝트 폴더* 들은 각자의 git repo (또는 미관리) 로 둘 수 있다 — Foundry 는 그 어느 쪽이든 무관하지만, 본인이 다중 머신에서 같은 *프로젝트* 를 진행한다면 그 프로젝트도 별도 repo 로 두는 것을 권장.

## 4. 위반 신호 (체크리스트)
다음 신호가 보이면 본 원칙 위반 가능성:
- 두 머신의 `00-Foundry/` 가 동일 git remote 를 가리키지 않음.
- 어떤 프로젝트의 `factory.yaml` 에 `factory_source.commit` 이 비어 있거나 SHA 형식이 아님.
- `git status` 가 *진행 중인 cycle 작업 도중* `00-Foundry/` 안의 파일을 modified 로 표시 (의도적 Meta Sprint 가 아닌 한 신호).
- "다른 머신에서 PDF/문서를 직접 가져왔는데 git 추적이 안 된다" 같은 발화.

## 5. 다른 원칙과의 관계
- [Human_Control_Point_정책.md](./Human_Control_Point_정책.md) — Foundry version migration / `local_modifications` 전환은 Human Control Point.
- [Non_Blocking_Execution_정책.md](./Non_Blocking_Execution_정책.md) — *프로젝트 측* 결정 대부분은 비차단으로 진행되지만, *Foundry 변경* 은 항상 Human Control Point.
- [Copy_Paste_Zero_로드맵.md](./Copy_Paste_Zero_로드맵.md) — 본 정책은 Stage 1 ↔ Stage 5 모든 단계에서 변하지 않는 invariant.

## 변경 이력
- v0.2.1 candidate (2026-05-08) — 신설.
