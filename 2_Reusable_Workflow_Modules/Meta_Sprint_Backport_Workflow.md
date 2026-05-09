# L2 Workflow — Meta Sprint Backport Workflow

> **Layer**: 2 — Reusable Workflow Module.
> **상태**: v0.2.1 candidate (2026-05-08 도입).
> **선행 원칙**: [GitHub_Foundry_관리정책](../1_Universal_Operating_Principles/GitHub_Foundry_관리정책.md), [Human_Control_Point_정책](../1_Universal_Operating_Principles/Human_Control_Point_정책.md).
> **사용자 가이드**: [Bootstrap/How_To_Backport_Project_Lessons.md](../Bootstrap/How_To_Backport_Project_Lessons.md) (operational quick-start, 동일 의미).

## 1. 핵심 명제
**프로젝트 종료 *후* 에만 Meta Sprint 를 수행한다.**
- Meta Sprint 의 입력: 그 프로젝트의 `meta/` 폴더 *전체*.
- 산출: Foundry 에 반영할 *승인된 변경 묶음* + Semver bump 결정.
- 일반화 가능한 개선만 Foundry 반영 후보. 프로젝트 특화 내용은 *자동 반영 금지*.
- **00-Foundry 수정은 인간 승인 필수.** Claude 가 자동 commit 하지 않는다.

## 2. 진입 조건
다음 모두 충족:
- 프로젝트의 모든 cycle 이 Final Control Point 를 통과 또는 명시적 보류.
- 프로젝트의 `meta/` 6 파일이 모두 존재 ([template](../4_Task_Level_Execution_Templates/프로젝트_meta_폴더_템플릿.md)).
- `00-Foundry` 가 `git pull` clean (작업트리 깨끗).
- 사용자가 *명시적으로* "이 프로젝트의 Meta Sprint 시작" 을 선언 (자동 트리거 금지).

## 3. 절차 (11단계)

### 3.1 입력 검토 — `meta/` 전체 1차 패스 (Claude)
- `foundry-improvement-log.md` (FIL-NNN) — raw 발견.
- `foundry-backport-candidates.md` (FBC-NNN) — 진행 중 누적된 후보가 있다면.
- `decisions.md` (D-NNN) — Critical Decision 시간순.
- `decision-queue.md` (DQ-NNN) — 미해결 queue 가 있는지.
- `lessons-learned.md` — cycle 별 keep/change/drop.
- `chatgpt-decision-requests.md` — ChatGPT 와 주고받은 결정 패키지 / 회신.

### 3.2 4 분류 (Claude 1차 패스)
각 FIL 항목을 4 분류 중 하나로 격상:

| 분류 | 의미 | 액션 |
|---|---|---|
| **승인** | Foundry 반영해야 명백. *일반화 가능*. 다른 프로젝트도 영향. | `foundry-backport-candidates.md` 의 `## 승인` 섹션. |
| **보류** | 가치 있으나 1 사례로 부족. *N 사례 누적 후 재검토*. | `## 보류` + 재검토 트리거 명시. |
| **폐기** | 본 프로젝트 *특화* / 진단 오류 / Foundry 의도와 충돌. | `## 폐기` + 사유 1줄. |
| **추가검토** | Critical Decision 성격. ChatGPT 외부 의견 필요. | `## 추가검토` + ask-chatgpt-decision 패키지 작성. |

핵심: **프로젝트 특화 내용은 자동 반영 금지** — 본 단계의 *폐기* 분류가 그 1차 안전장치.

### 3.3 ChatGPT 라운드 — 추가검토 항목만
- `ask-chatgpt-decision.md` 형식 패키지로 변환.
- 회신 도착 후 *승인 / 보류 / 폐기* 중 하나로 재분류.
- 호출 시점은 [Copy_Paste_Zero_로드맵 §4](../1_Universal_Operating_Principles/Copy_Paste_Zero_로드맵.md#4-chatgpt-사용-시점-현재-단계--stage-1-한정) 의 *Meta Sprint* 시점에 해당.

### 3.4 ★ 사용자 최종 승인 게이트
사용자가 `## 승인` 섹션을 1행씩 다시 읽고 응답:
- `[APPROVED]` — Foundry 반영.
- `[DEFER]` — 보류로 격하 (사유 1줄).
- `[REJECT]` — 폐기 (사유 1줄).
- `[SPLIT]` — 더 작게 N건으로 쪼갬.

이 게이트가 빠지면 Meta Sprint 는 *비공식 종료* 로 간주.
모든 사용자 응답은 `meta/decisions.md` 에 시간순 박제.

### 3.5 Foundry 반영 — 별도 git branch
```powershell
git -C 00-Foundry checkout -b meta-sprint/<project>-<YYYYMMDD>
# 항목별 별도 commit
git -C 00-Foundry commit -m "meta-sprint(<project>): <한 줄> + N approved items"
```

규칙:
- 승인 N 항목을 *각각* 별도 commit (또는 의미 단위 묶음). 한 commit 에 여러 무관 변경 금지.
- commit message 본문에 *어느 프로젝트 / 어느 후보 ID 에서 유래* 했는지 박제.
- runner / hook / skill 같이 *동작이 변하는* 코드 변경은 §3.8 self-test 통과 필수.

### 3.6 Semver Bump
승인 항목의 *총합 영향* 평가:

| 변경 종류 | bump |
|---|---|
| 호환성 깨는 변경 (기존 Brief / runner schema 깨짐) | major (1.0.0 이전은 minor 로 갈음) |
| 신규 기능 / 신규 method / 신규 hook (호환성 유지) | minor |
| 문서 정정 / 작은 버그 수정 / 룰 명확화 | patch |

`factory.yaml` 의 `factory.version` 갱신 + `frozen_on` 갱신 + `previous_version` 추가.

### 3.7 CHANGELOG 업데이트
- `[Unreleased]` 또는 `[Unreleased — vX.Y.Z candidate]` → `[X.Y.Z] — YYYY-MM-DD` 로 닫음.
- 5 섹션 (Decided / Added / Changed / Removed / Released-Frozen) 중 해당하는 것만.
- 항목별 `[Source: <project> / <FBC-NNN>]` 박제.

### 3.8 ★ Self-test 회귀 보호
B-002 패턴: Foundry 자체의 reference Brief 를 다시 검증.
```powershell
.\4_Task_Level_Execution_Templates\claude-code\hooks\before-final.ps1 `
  -Brief 3_Domain_Project_Playbooks\ai-npi-platform\B-002_NPI_Brief.md
```
**exit 0 + 6/6 PASS 가 나와야 Meta Sprint 공식 종료.**
실패 시 push 금지. 변경 묶음 검토 후 재시도.

### 3.9 push + tag
```powershell
git -C 00-Foundry checkout main
git -C 00-Foundry merge --no-ff meta-sprint/<project>-<YYYYMMDD>
git -C 00-Foundry tag -a v<X.Y.Z> -m "Foundry v<X.Y.Z> — Meta Sprint <project>"
git -C 00-Foundry push origin main
git -C 00-Foundry push origin v<X.Y.Z>
```

### 3.10 프로젝트 측 마무리
원본 프로젝트의 `meta/foundry-backport-candidates.md` 의 각 승인 항목 옆에 *반영 commit SHA + Foundry version* 을 박제.
역추적 가능성 보존.

### 3.11 다른 진행 중 프로젝트
- 자동 마이그레이션 0.
- 새 version 으로 옮기려면 *각 프로젝트별로* Migration Critical Decision 을 별도 cycle 로 진행.

## 4. 안티-패턴
- ❌ 프로젝트 진행 *중* 에 Foundry 원본 직접 수정.
- ❌ §3.4 사용자 최종 승인 게이트 우회.
- ❌ §3.8 self-test 생략한 채 push.
- ❌ 한 commit 에 여러 무관 후보 묶기.
- ❌ 승인 항목을 backport-candidates.md 에 기록하지 않고 직접 commit (역추적 불가).
- ❌ *프로젝트 특화* 발견을 일반화 검토 없이 Foundry 에 반영.

## 5. 다른 Workflow 와의 연결
- [신규_프로젝트_생성_Workflow](./신규_프로젝트_생성_Workflow.md) — 프로젝트 진입 / 종료 양 끝.
- [Decision_Queue_운영방식](./Decision_Queue_운영방식.md) — `decision-queue.md` 가 본 workflow 의 1차 입력 중 하나.

## 변경 이력
- v0.2.1 candidate (2026-05-08) — 신설. Bootstrap/How_To_Backport_Project_Lessons 의 operational 절차를 본 L2 layer 로 정형화.
