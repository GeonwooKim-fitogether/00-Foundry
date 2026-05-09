# L2 Workflow — 신규 프로젝트 생성 Workflow

> **Layer**: 2 — Reusable Workflow Module.
> **상태**: v0.2.1 candidate (2026-05-08 도입).
> **선행 원칙**: [GitHub_Foundry_관리정책](../1_Universal_Operating_Principles/GitHub_Foundry_관리정책.md), [Human_Control_Point_정책](../1_Universal_Operating_Principles/Human_Control_Point_정책.md).
> **사용자 가이드**: [Bootstrap/How_To_Start_New_Project.md](../Bootstrap/How_To_Start_New_Project.md) (operational quick-start).

## 1. 핵심 명제
**신규 프로젝트는 Foundry 의 *특정 version + commit* 을 복사해서 시작한다.**
- 현재 단계 (v0.2.1) 에서는 thin control plane 방식 (참조만, 로컬 사본 0) 을 사용하지 않는다.
- *복사 후 프로젝트에 맞게 자유롭게 수정/삭제/추가* 한다.
- 단, *Foundry 원본의 어떤 commit 에서 유래했는지* 항상 추적 가능해야 한다.

> **⚠️ 본 행위는 *Foundry 자체의 동기화* 와 다른 행위다.**
> - Foundry *자체* 의 동기화 (다중 머신 간 원본 정렬) → GitHub clone/pull/commit/push *만* 사용. 자세한 구분: [GitHub_Foundry_관리정책 §1A](../1_Universal_Operating_Principles/GitHub_Foundry_관리정책.md#1a-두-개의-행위--동기화-vs-seed-복사--매우-중요).
> - 신규 프로젝트의 *Seed 복사* (현재 절차) → 단순 폴더 복사도 허용. 단 `factory_source.commit` 박제 *필수*.
> 둘을 혼동하면 본 정책의 의도가 깨진다.

## 2. 진입 조건
- 사용자가 새 프로젝트 시작을 명시적으로 요청.
- `00-Foundry` 가 GitHub remote 와 동기화된 상태 (`git pull` clean).
- 새 프로젝트 폴더가 *아직 없다* (덮어쓰기 방지).

## 3. 절차 (10단계)

### 3.1 시작점 식별
- Foundry 의 어떤 version 에서 시작할지 결정 (보통 최신 frozen).
- commit SHA 확보 (`git -C 00-Foundry rev-parse HEAD` 또는 `git -C 00-Foundry rev-list -n 1 v0.2.1`).
- *되돌릴 수 있는* 결정이므로 Claude 가 default = 최신 frozen 을 선택해 진행 (decision-queue 1행 기록).

### 3.2 폴더 생성
```
workspace/
├── 00-Foundry/                  ← Source of Truth
└── <NN>.<project-name>/         ← 신규, sibling
```
- 프로젝트 ID 형식: `<번호>.<kebab-case>` (예: `12.subscription-payment-saas-platform`).
- *00-Foundry 내부에 두지 않는다* — frozen 경계 보호.

### 3.3 표준 골격 생성
```
<NN>.<project-name>/
├── factory.yaml              ← § 3.4
├── CLAUDE.md                 ← agent 컨텍스트 (Foundry 참조 경로 명시)
├── ai-npi/                   ← NPI 산출물
│   ├── project-brief.md
│   ├── domain-ontology.md
│   ├── NPI_Brief.md
│   ├── NPI_Blueprint.md
│   └── NPI_Worklist.md
└── meta/                     ← § 3.5 — 필수
    ├── foundry-improvement-log.md
    ├── foundry-backport-candidates.md
    ├── decisions.md
    ├── decision-queue.md
    ├── lessons-learned.md
    └── chatgpt-decision-requests.md
```

### 3.4 `factory.yaml` 작성 — 필수
[4_Task_Level_Execution_Templates/factory_yaml_template.md](../4_Task_Level_Execution_Templates/factory_yaml_template.md) 참조. 필수 필드:
- `factory_source.{repo, version, commit, copied_on}` 4 필드 모두.
- `project.{name, type}`.
- `local_modifications` (기본 `false`).

### 3.5 `meta/` 폴더 생성 — 필수
[4_Task_Level_Execution_Templates/프로젝트_meta_폴더_템플릿.md](../4_Task_Level_Execution_Templates/프로젝트_meta_폴더_템플릿.md) 의 6 파일 모두 생성. 빈 stub 으로 시작 가능하나 *파일 자체는 반드시 존재*.

### 3.6 산출물 작성 — Brief 우선
[NPI_Brief.md](../4_Task_Level_Execution_Templates/NPI_Brief.md) (v0.2.0+ 템플릿) 을 ai-npi/NPI_Brief.md 로 복사 후 작성:
- dual-form AC + `schema_version: "0.2.0"` 필수.
- Bootstrap cycle 한정: `command` method 금지 (코드 0줄). `file_exists` + `manual` 만.

### 3.7 추적 가능성 확보
- 프로젝트 폴더가 *그 자체로 git repo* 가 될 필요는 없으나, 다중 머신 동기화가 필요하면 권장.
- 어떤 경우든 `factory.yaml.factory_source.commit` 만으로 *Foundry 의 어떤 상태에서 유래* 했는지 답할 수 있어야 한다.

### 3.8 검증 호출
00-Foundry 의 runner 를 *직접* 호출 (사본 두지 않음):
```powershell
python ../00-Foundry/4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/run.py `
  --brief ./ai-npi/NPI_Brief.md --out ./ai-npi/NPI_Verification.md
```
exit 0 + 모든 AC Pass 가 확인되어야 Bootstrap Final Control Point 통과.

### 3.9 Start Control Point — 사용자 승인
- AC-4 / AC-5 등의 manual 게이트가 사용자 승인을 요구한다.
- 응답 형식 / Critical Decision 분류는 [Human_Control_Point_정책 §3](../1_Universal_Operating_Principles/Human_Control_Point_정책.md#3-escalation-형식) 참조.

### 3.10 진입 보고
승인 통과 후:
- `meta/decisions.md` 에 D-001 박제 (factory_source.version 선택).
- `meta/decision-queue.md` 가 비어 있는지 확인 (Bootstrap 단계는 큰 결정 위주).
- 첫 feature cycle 후보 1개 추천.

## 4. 안티-패턴
- ❌ thin control plane (Foundry 사본 0, 모든 것을 참조) — 현재 단계에서는 *사용하지 않는다*. 진화 방향이지만 v0.2.1 에서는 채택 안 함.
- ❌ Foundry 원본 사본을 새 프로젝트 폴더 안에 그대로 두기 (frozen 경계 침범).
- ❌ `factory_source.commit` 미기록 또는 `HEAD` 같은 동적 참조.
- ❌ `meta/` 폴더 누락 또는 일부 파일만 생성.
- ❌ Bootstrap cycle 에서 코드 작성 / 외부 서비스 가입 / 인프라 설정 (별도 cycle).

## 5. 다른 Workflow 와의 연결
- [Decision_Queue_운영방식](./Decision_Queue_운영방식.md) — 본 workflow 진행 중 발생한 작은 결정의 누적소.
- [Meta_Sprint_Backport_Workflow](./Meta_Sprint_Backport_Workflow.md) — 프로젝트 종료 시 진입.

## 변경 이력
- v0.2.1 candidate (2026-05-08) — 신설. Bootstrap/How_To_Start_New_Project 의 operational 절차를 본 L2 layer 의 *재사용 가능 workflow* 로 정형화.
