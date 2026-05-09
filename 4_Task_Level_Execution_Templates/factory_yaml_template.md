# L4 Template — 프로젝트 factory.yaml 템플릿

> **Layer**: 4 — Task-level Execution Template.
> **상태**: v0.2.1 candidate (2026-05-08 도입).
> **선행 원칙**: [GitHub_Foundry_관리정책](../1_Universal_Operating_Principles/GitHub_Foundry_관리정책.md).
> **사용 workflow**: [신규_프로젝트_생성_Workflow §3.4](../2_Reusable_Workflow_Modules/신규_프로젝트_생성_Workflow.md#34-factoryyaml-작성--필수).

## 1. 위치
신규 프로젝트의 *루트* 에 `factory.yaml` 로 둔다.
**00-Foundry 의 `factory.yaml` 과는 별개의 *프로젝트 메타 전용* 파일이다.**

```
<NN>.<project-name>/
├── factory.yaml          ← 본 템플릿이 채워지는 위치
├── CLAUDE.md
├── ai-npi/
└── meta/
```

## 2. 최소 필수 필드 — 본 v0.2.1 spec

다음 3 블록은 *반드시* 존재한다 (사용자 요청 spec 그대로):

```yaml
factory_source:
  repo: <github-repo-url>          # 예: git@github.com:<owner>/00-Foundry.git
  version: 0.2.0                    # Foundry 의 Semver — frozen version
  commit: <commit-sha>              # 40-char SHA, 시작 시점 commit
  copied_on: <YYYY-MM-DD>           # 신규 프로젝트 생성일

project:
  name: <project-name>              # 폴더명과 동일 권장
  type: <project-type>              # 예: saas-platform, dashboard, agent, library, …

local_modifications: true           # 또는 false
```

> **주의**: `local_modifications` 의 *기본 권장값* 은 `false`.
> 본 템플릿이 `true` 로 되어 있는 이유는 사용자 요청 spec 의 명시적 값을 보존하기 위함.
> 실제 신규 프로젝트는 *기본값 false* 로 시작하며, *국지적 Foundry 룰 우회 결정* 이 발생할 때만 `true` 로 전환 (Human Control Point 트리거 — [Human_Control_Point_정책 §2](../1_Universal_Operating_Principles/Human_Control_Point_정책.md#2-human-control-point-escalation-트리거-하나라도-해당하면-즉시-escalation)).

## 3. 권장 확장 필드 (선택)

```yaml
factory_source:
  repo: git@github.com:<owner>/00-Foundry.git
  version: 0.2.0
  commit: 0123456789abcdef0123456789abcdef01234567
  copied_on: 2026-05-08

project:
  name: 12.subscription-payment-saas-platform
  type: saas-platform
  owner: project-owner
  started_on: 2026-05-08

local_modifications: false

# 권장 확장 ↓
meta_artifacts:
  improvement_log: meta/foundry-improvement-log.md
  backport_candidates: meta/foundry-backport-candidates.md
  decisions: meta/decisions.md
  decision_queue: meta/decision-queue.md
  lessons_learned: meta/lessons-learned.md
  chatgpt_requests: meta/chatgpt-decision-requests.md

ai_npi_root: ai-npi/

foundry_paths:
  runner: ../00-Foundry/4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/run.py
  hook_ps1: ../00-Foundry/4_Task_Level_Execution_Templates/claude-code/hooks/before-final.ps1
  hook_cmd: ../00-Foundry/4_Task_Level_Execution_Templates/claude-code/hooks/before-final.cmd
  brief_template: ../00-Foundry/4_Task_Level_Execution_Templates/NPI_Brief.md

history:
  - date: 2026-05-08
    note: "프로젝트 초기 생성. factory_source 박제."
```

## 4. 필드 의미

### `factory_source.{repo, version, commit, copied_on}` — 4 필수
- **`repo`**: Foundry 의 GitHub URL (https 또는 ssh).
- **`version`**: Foundry 의 Semver. 시작 시점에 *frozen* 인 것 권장.
- **`commit`**: 40-char SHA. 한 번 결정되면 *프로젝트 종료까지 변경 금지*.
  - 새 version 으로 옮기려면 별도 *Migration Critical Decision* (Human Control Point).
  - 갱신은 [Meta_Sprint_Backport_Workflow §3.11](../2_Reusable_Workflow_Modules/Meta_Sprint_Backport_Workflow.md#311-다른-진행-중-프로젝트) 의 *명시적 Migration cycle* 에서만.
- **`copied_on`**: ISO 8601 YYYY-MM-DD.

### `project.{name, type}` — 2 필수
- **`name`**: 프로젝트 ID (폴더명과 동일 권장).
- **`type`**: 자유 어휘. 권장: `saas-platform` / `dashboard` / `agent` / `library` / `meta-tooling` / `playground`.

### `local_modifications` — 1 필수
- `false` (권장 기본값): Foundry 원본 룰 그대로 따른다.
- `true`: 국지적 Foundry 룰 우회. 반드시 `meta/foundry-improvement-log.md` 에 사유와 차이 박제.

### 권장 확장 필드 — 선택
- **`meta_artifacts`**: 6 파일 경로 매핑. tool 이 자동으로 찾기 쉽게.
- **`ai_npi_root`**: NPI 산출물 디렉토리 (보통 `ai-npi/`).
- **`foundry_paths`**: 자주 쓰는 Foundry 파일 경로의 *프로젝트 기준 상대 경로*. 사본 두지 말 것 — *참조 only*.
- **`history`**: 본 factory.yaml 자체의 변경 이력 (선택).

## 5. 검증 (간단)
runner 가 본 파일을 *직접* 검증하지는 않는다 (현재 v0.2.1 단계). 대신:
- Brief 의 AC 에서 `factory.yaml` 존재를 `file_exists` 로 검사.
- Brief 의 manual AC 에서 `factory_source.commit` 이 SHA 형식으로 채워졌는지 사람 검토.

향후 v0.3.0 에서 runner 의 추가 검증 method (예: `yaml_field_exists`, `regex_match`) 도입 후보.

## 6. 안티-패턴
- ❌ 4 필수 (`factory_source.{repo, version, commit, copied_on}`) 중 하나라도 누락 또는 placeholder 그대로 둠.
- ❌ `commit` 에 `HEAD` / `main` 같은 *동적 참조* (좌표가 흔들린다).
- ❌ `local_modifications: true` 인데 사유 미박제.
- ❌ Foundry 원본의 `factory.yaml` 을 그대로 복사해서 신규 프로젝트에 둠 (의미가 다르다).
- ❌ 본 템플릿을 *Foundry 원본 갱신* 시 자동으로 따라 갱신 (각 프로젝트는 시작 시점 좌표 보존).

## 7. 변경 이력 (본 템플릿)
- v0.2.1 candidate (2026-05-08) — 신설. Bootstrap/project-meta-templates/factory.yaml.template 의 *공식 L4 layer* 등록.
