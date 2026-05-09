# How to Start a New Project on AI-NPI Factory (v0.2.0+)

> **개정 (2026-05-08, [Unreleased])**: 본 절차는 v0.2.0 freeze 이후의 GitHub 기반 운영 정책을 반영한다.
> Foundry 는 GitHub 원격 저장소로 동기화되며, 각 신규 프로젝트는 Foundry 의 *특정 version + commit* 에서 시작한 *project instance* 로 기록된다.
> 프로젝트 진행 중 발견한 Foundry 개선사항은 **즉시 원본에 반영하지 않는다.** 프로젝트의 `meta/` 폴더에 누적했다가, 프로젝트 종료 시 [How_To_Backport_Project_Lessons.md](./How_To_Backport_Project_Lessons.md) 의 *Meta Sprint* 로 일괄 처리한다.

## 0. 사전 준비
- 사용자의 GitHub 계정에 `00-Foundry` 가 push 되어 있어야 한다 (private repo 권장).
- 로컬 머신에 git 이 설치되어 있고, 신규 프로젝트가 생성될 워크스페이스에 `00-Foundry/` 가 *clone* 되어 있어야 한다.
- 사용자가 여러 머신을 쓴다면: 각 머신에서 `git pull origin <branch>` 로 동기화. 머신 간 직접 폴더 복사 금지 (commit 추적 불가).

## 1. 시작점 확정 (Foundry 의 어떤 version 에서 시작할 것인가)
신규 프로젝트는 Foundry 의 *frozen version* 에서 시작한다. 일반적으로 *최신 frozen* 을 쓰지만, 의도적으로 과거 version 을 고를 수도 있다.

```powershell
# Foundry 워크스페이스에서 — 현재 frozen version 확인
git -C ../00-Foundry log --oneline -1                            # 최근 commit
Select-String -Path ../00-Foundry/factory.yaml -Pattern "^  version:|^  status:|^  frozen_on:"
```

기록 대상:
- `factory_source.repo` — Foundry 의 GitHub URL (예: `git@github.com:<owner>/00-Foundry.git`)
- `factory_source.version` — Foundry 의 Semver (예: `0.2.0`)
- `factory_source.commit` — 시작 시점의 commit SHA (full)
- `factory_source.copied_on` — 신규 프로젝트가 만들어진 날짜 (ISO 8601)

## 2. 신규 프로젝트 폴더 생성
- 프로젝트 ID 는 `<번호>.<kebab-case-name>` 형태 권장 (예: `12.subscription-payment-saas-platform/`).
- 프로젝트 폴더는 **`00-Foundry` 의 sibling** 에 둔다 (Foundry 내부에 두지 않는다 — Foundry 의 frozen 경계 보호).

```
workspace/
├── 00-Foundry/                              ← Frame, frozen, GitHub 동기화
└── 12.subscription-payment-saas-platform/   ← project instance, 별도 git repo
```

각 프로젝트는 *자신의 git repo* 를 가질 수 있다 (선택). 다중 머신 동기화가 필요하면 권장.

## 3. 프로젝트 표준 폴더 구조
```
12.your-project/
├── factory.yaml          ← 프로젝트 metadata + factory_source 기록
├── CLAUDE.md             ← agent 컨텍스트 (Foundry 참조 경로 + 프로젝트 단계 금지/허용)
├── ai-npi/               ← 모든 NPI 산출물의 단일 컨테이너
│   ├── project-brief.md
│   ├── domain-ontology.md
│   ├── NPI_Brief.md
│   ├── NPI_Blueprint.md
│   └── NPI_Worklist.md
└── meta/                 ← Foundry 개선 후보 누적소 (필수, §6 참조)
    ├── foundry-improvement-log.md
    ├── foundry-backport-candidates.md
    ├── decisions.md
    └── lessons-learned.md
```

> `meta/` 폴더는 **반드시** 생성한다. 프로젝트 종료 시 Meta Sprint 가 본 폴더를 입력으로 동작하기 때문이다.

## 4. 프로젝트 `factory.yaml` 작성
프로젝트 루트에 `factory.yaml` 을 생성한다 (Foundry 의 `factory.yaml` 과 *별개* — 프로젝트 메타 전용).
템플릿: [Bootstrap/project-meta-templates/factory.yaml.template](./project-meta-templates/factory.yaml.template).

```yaml
# 12.your-project/factory.yaml
factory_source:
  repo: git@github.com:<owner>/00-Foundry.git    # 사용자의 GitHub URL
  version: "0.2.0"                                # Foundry 의 Semver
  commit: <40자 commit SHA>                       # frozen 시점 commit
  copied_on: 2026-05-08

project:
  name: 12.your-project
  type: <project-type>     # 예: saas-platform, dashboard, agent, library

# 프로젝트 진행 중 Foundry 룰을 *국지적으로* 변경했는가?
# - true 이면 meta/foundry-improvement-log.md 에 사유와 차이를 박제해야 한다.
# - false 이면 Foundry 원본 룰을 그대로 따른다 (권장 기본값).
local_modifications: false
```

## 5. 산출물 작성 — Brief 우선
1. `ai-npi/project-brief.md` (durable, slow-changing 비전).
2. `ai-npi/domain-ontology.md` (Core Objects, PascalCase).
3. `ai-npi/NPI_Brief.md` — Foundry 의 [4_Task_Level_Execution_Templates/NPI_Brief.md](../4_Task_Level_Execution_Templates/NPI_Brief.md) (v0.2.0) 을 따라 작성:
   - dual-form AC (prose 표 + structured AC YAML)
   - 최상위 `schema_version: "0.2.0"` **필수**
   - method 는 `command` / `file_exists` / `manual` 만 허용
   - **Bootstrap cycle 한정**: 코드가 0줄이므로 `command` 사용 금지. `file_exists` + `manual` 만.
4. Blueprint / Worklist 는 Brief 승인 후 작성 (stub 으로 시작 가능).

## 6. `meta/` 폴더 운영 정책 (★ 핵심 변경)
프로젝트 진행 중 Foundry 의 부족함 / 개선 아이디어를 *발견* 했을 때:

- ✅ `meta/foundry-improvement-log.md` 에 timestamp + 발견 맥락 + 제안을 *그 자리에서* 박제한다.
- ✅ 프로젝트 자체는 *Foundry 룰을 그대로 적용한 채로* 진행한다 (원본 변경 0).
- ❌ `00-Foundry/` 의 어떤 파일도 즉시 수정하지 않는다.
- ❌ Foundry 원본의 룰을 우회한 임시 패치를 프로젝트에 반영하지 않는다 (정말 불가피하면 `local_modifications: true` 로 표시 + 사유 박제).

이유: Foundry 는 frozen 상태로 *증거 누적* 단계를 지나야 진화한다. 1개 프로젝트의 1번 사례로 즉시 룰을 바꾸면 다른 프로젝트가 그 변경에 의해 깨진다. 다수 프로젝트의 누적 데이터가 모인 후에만 변경한다.

## 7. 검증 — `00-Foundry` 의 runner 호출
프로젝트는 *Foundry 의 runner 를 직접 호출* 한다. runner 사본을 두지 않는다.

```powershell
# Final Control Point 자동 차단 라인 (PowerShell)
powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass `
  -File ../00-Foundry/4_Task_Level_Execution_Templates/claude-code/hooks/before-final.ps1 `
  -Brief ./ai-npi/NPI_Brief.md
```

```powershell
# 또는 runner 직접 호출
python ../00-Foundry/4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/run.py `
  --brief ./ai-npi/NPI_Brief.md --out ./ai-npi/NPI_Verification.md
```

exit code: 0 = Pass / 1 = AC fail / 2 = schema/parse error.

## 8. Start Control Point 통과
- 목적 / Scope / AC 정의 + 동결.
- Affected Objects 가 ontology 의 실재 객체만 사용.
- 필요 시 `ask-chatgpt-decision` 패키지로 Critical Decision 처리.

## 9. 자동 실행 단계 — Human Control Point 는 다음에만
- 되돌리기 어려운 변경
- 의미 있는 스코프 / 예산 / 일정 변경
- 리스크 등급 상향
- AC 변경
- (신규) **Foundry 룰의 국지적 우회 결정** — `local_modifications: true` 로 전환되는 결정

## 10. Final Control Point — 검증 완료
- `NPI_Verification.md` 가 runner 에 의해 자동 생성되어 있고 모든 행이 Pass.
- Affected Objects diff 가 reconcile.
- `meta/lessons-learned.md` 에 본 cycle 의 keep / change / drop 1줄씩 기록.

## 11. 프로젝트 종료 — Meta Sprint 진입
프로젝트가 종료 (또는 1차 마일스톤 완료) 되면 [How_To_Backport_Project_Lessons.md](./How_To_Backport_Project_Lessons.md) 의 절차를 그대로 따라 Foundry 백포팅을 수행한다.
승인된 항목만 `00-Foundry` 원본 repo 에 commit + push 되며, 그 시점에 Foundry 의 Semver 가 bump 된다.

## 변경 이력
- v0.1.0 (2026-05-07) — 초안 (수동 절차).
- [Unreleased] (2026-05-08) — GitHub 기반 + factory_source + meta/ 폴더 + Meta Sprint 도입.
