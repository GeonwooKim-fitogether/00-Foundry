# How to Backport Project Lessons — Meta Sprint 절차

> 프로젝트 종료 (또는 1차 마일스톤 완료) 시점에 *그 프로젝트가 발견한 Foundry 개선 후보* 를 검토하고
> *승인된 항목만* `00-Foundry` 원본 repo 에 반영하는 절차.
> 단발 cycle 형태로 운영하며 본 절차를 **Meta Sprint** 라 부른다.

## 0. 진입 조건
- 프로젝트의 모든 cycle 이 Final Control Point 를 통과했거나 명시적으로 보류·종료되었다.
- 프로젝트 폴더에 `meta/` 4개 파일이 모두 존재한다 (`foundry-improvement-log.md`, `foundry-backport-candidates.md`, `decisions.md`, `lessons-learned.md`).
- 사용자가 "이 프로젝트의 Meta Sprint 를 시작한다" 고 명시적으로 선언한다 (자동 트리거 금지 — 조용히 폴더가 생기지 않도록).

## 1. 사전 동기화
```powershell
git -C 00-Foundry pull origin main         # Foundry 최신 상태로
git -C 00-Foundry status                   # 더러운 작업트리 없는지 확인 (clean 상태 필수)
```

## 2. 후보 수집 — `meta/foundry-improvement-log.md` 정리
프로젝트 진행 중 누적된 raw 개선 아이디어를 검토한다.

각 항목별 1차 분류 — Claude Code 가 1차 패스로 작성한다 (사용자는 2차에서 승인):

| 분류 | 의미 | 액션 |
|---|---|---|
| **승인** (approve) | 명백히 Foundry 에 반영해야 함. 다른 프로젝트도 동일하게 영향. | `foundry-backport-candidates.md` 의 `## 승인` 섹션으로 이동. |
| **보류** (hold) | 가치 있으나 1개 사례만으로는 결정 부족. N 사례 더 누적 후 재검토. | `## 보류` 섹션으로 이동. 재검토 트리거 조건 명시 (예: "동일 패턴 3개 프로젝트에서 발견되면"). |
| **폐기** (reject) | Foundry 룰의 의도에 어긋남 / 본 프로젝트 특수 사정 / 잘못된 진단. | `## 폐기` 섹션으로 이동. 폐기 사유 한 줄. |
| **추가검토** (review) | Critical Decision 성격. ChatGPT 또는 외부 의견 필요. | `## 추가검토` 섹션으로 이동. `ask-chatgpt-decision` 패키지 작성 권장. |

## 3. ChatGPT 라운드 — 추가검토 항목
`## 추가검토` 의 항목은 [ask-chatgpt-decision.md](../4_Task_Level_Execution_Templates/claude-code/commands/ask-chatgpt-decision.md) 형식의 결정 패키지로 변환해 ChatGPT (또는 다른 사상가 동반자) 에게 전달한다. 회신 도착 후 *승인 / 보류 / 폐기* 중 하나로 *재분류* 한다.

## 4. 사용자 최종 승인 게이트 ★
사용자가 `foundry-backport-candidates.md` 의 `## 승인` 섹션을 1행씩 읽고 *재차* 승인한다. 이 단계가 빠지면 Meta Sprint 는 *완료되지 않은 상태* 로 본다.

```
승인 항목별로 사용자 응답 형식:
  - [APPROVED] — Foundry 에 반영 진행
  - [DEFER]    — 보류로 격하 (사유 1줄)
  - [REJECT]   — 폐기 (사유 1줄)
  - [SPLIT]    — 더 작게 쪼개서 N건으로 분할
```

승인 결과를 `meta/decisions.md` 에 박제 (시간순).

## 5. Foundry 반영 — 별도 git 작업
**승인된 항목만** `00-Foundry` 에 반영한다.

```powershell
# Foundry 워크스페이스에서
git -C 00-Foundry checkout -b meta-sprint/<project-name>-<YYYYMMDD>
# … 승인 항목 별 파일 수정 …
git -C 00-Foundry add <changed-files>
git -C 00-Foundry commit -m "meta-sprint(<project-name>): <한 줄 요약> + N approved items"
```

규칙:
- 승인된 N개 항목을 *각각* 별도 commit 으로 (또는 의미 단위 묶음). 한 commit 에 여러 무관 변경 금지.
- commit 메시지 본문에 *어느 프로젝트의 어떤 후보 ID 에서 유래* 했는지 박제 (예: `Source: 12.subscription-payment-saas-platform/meta/foundry-backport-candidates.md#FBC-003`).
- runner / hook / skill 처럼 *동작* 이 변하는 코드 변경은 본 Meta Sprint 종료 *전* 에 self-test (B-002 패턴) 을 다시 한 번 통과해야 한다.

## 6. Semver Bump 결정
승인 항목의 *총합 영향* 을 평가해 Foundry 의 다음 version 을 결정한다.

| 변경 종류 | bump 위치 |
|---|---|
| 호환성 깨는 변경 (기존 Brief / runner schema 가 깨짐) | **major** (1.0.0 이전 단계에서는 minor 로 갈음) |
| 신규 기능 / 신규 method / 신규 hook 추가 (기존 호환성 유지) | **minor** |
| 문서 정정 / 버그 수정 / 룰 명확화 | **patch** |

`factory.yaml` 의 `factory.version` 을 수정 + `factory.status: frozen` + `frozen_on` 갱신.

## 7. CHANGELOG 업데이트
`CHANGELOG.md` 의 `[Unreleased]` 섹션을 `[<new-version>] — <YYYY-MM-DD>` 로 닫는다.
구조: `Decided` / `Added` / `Changed` / `Removed` / `Released-Frozen` 5섹션 (필요한 것만).
각 항목 옆에 *유래 프로젝트* 표기 (예: `[Source: 12.subscription-payment-saas-platform / FBC-003]`).

## 8. self-test 재통과 (★ 회귀 방지)
변경된 Foundry 가 *자기 자신을 여전히 검증할 수 있는가* 를 확인한다.

```powershell
# B-002 패턴: Foundry 자체의 reference Brief 를 다시 검증
.\4_Task_Level_Execution_Templates\claude-code\hooks\before-final.ps1 `
  -Brief 3_Domain_Project_Playbooks\ai-npi-platform\B-002_NPI_Brief.md
```
exit 0 + 6/6 PASS 가 나와야 Meta Sprint 가 *공식 종료* 된다.

## 9. push + tag
```powershell
git -C 00-Foundry checkout main
git -C 00-Foundry merge --no-ff meta-sprint/<project-name>-<YYYYMMDD>
git -C 00-Foundry tag -a v<new-version> -m "Foundry v<new-version> — Meta Sprint <project-name>"
git -C 00-Foundry push origin main
git -C 00-Foundry push origin v<new-version>
```

## 10. 프로젝트 측 마무리
원본 프로젝트의 `meta/foundry-backport-candidates.md` 에 각 승인 항목 옆에 *반영된 commit SHA + version* 을 기록한다 (역추적 가능성 보존).

## 11. 다중 프로젝트 후속 진행
다른 진행 중 프로젝트들은 *각자의 진입 시점 factory_source* 를 그대로 유지한다. *자동으로* 새 version 을 적용하지 않는다. 새 version 으로 옮길 때는 명시적 *Migration Decision* 을 별도 cycle 로 진행한다 (Critical Decision).

## 안티-패턴
- ❌ 프로젝트 진행 *중* 에 Foundry 원본을 직접 수정.
- ❌ Meta Sprint 의 사용자 승인 게이트 (§4) 우회.
- ❌ 한 commit 에 여러 무관 후보 묶기.
- ❌ self-test (§8) 생략한 채 push.
- ❌ 승인 항목을 backport-candidates.md 에 기록하지 않고 직접 commit (역추적 불가).

## 변경 이력
- [Unreleased] (2026-05-08) — 초안 도입. GitHub 기반 운영 정책 + Meta Sprint 절차 정의.
