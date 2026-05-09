# Command: validate-output (v0.2.0)

## Purpose
모든 Acceptance Criteria 가 evidence 와 함께 Pass 인지 확인하고, 작업의 실제 변경이 Brief 의
Affected Objects 와 일치하는지 점검한다. 본 명령은 *직접 검증을 수행하지 않는다.* 검증은
**`verification-runner` skill 을 통해 `run.py` runner 가 실행**한다. runner 가 본 명령의
**single source of truth** 이다.

## When to Run
- 모든 task 의 Final Control Point 직전 (필수 — `06_verification` 모듈 의무 사항).
- AC 변경 직후 회귀 확인.
- `before-final` hook 이 차단 후 사용자가 수동 재실행할 때.

## v0.2.0 변경 요지 (v0.1.0 대비)
- **폐기**: "사람이 markdown 절차를 수동으로 따라가며 표를 채운다" 식의 수동 절차.
- **신규**: skill ↔ runner ↔ hook 의 3계층 호출. 명령 본문은 호출 표준만 정의한다.
- **신규**: `NPI_Verification.md` 의 AC ↔ Verification 매핑 표는 runner 가 생성하며 사람이 직접
  채우지 않는다. 사람의 역할은 manual method AC 의 confirmer/date 인정 + 표를 *읽고 결정* 하는 것뿐.

## Inputs
| 필드 | 형태 | 비고 |
|---|---|---|
| `brief_path` | 절대 또는 프로젝트 루트 상대 경로 | `*_NPI_Brief.md`. 본 Brief 안에 `schema_version: "0.2.0"` + `acceptance_criteria` 를 가진 ` ```yaml ` 블록 필수. |
| `out_path` | 경로 (선택) | 미지정 시 Brief 와 같은 디렉토리의 `NPI_Verification.md`. |
| `strict` | bool (선택) | true 면 `factory.yaml` 미발견을 fail (exit 2) 로 격상. |

## Procedure (표준 호출)
1. **skill 진입** — 본 명령은 `verification-runner` skill 을 호출한다.
   skill 의 `§5 표준 절차` 를 그대로 따른다 (pre-flight → mode 결정 → runner 호출 → 결과 수집 → 요약 → NEXT).
2. **mode 결정** — 아래 §"Subagent 실행 권장 조건" 에 해당하면 `mode=subagent`, 아니면 `inline`.
3. **runner 호출** — skill 이 `python <skill_dir>/run.py --brief <brief_path> [--out <out_path>] [--strict]` 형태로 정확히 호출한다.
4. **결과 수집** — runner exit code + stdout + stderr + 생성된 `NPI_Verification.md` 경로.
5. **사용자에게 보고** — skill 의 §4 표준 페이로드 (RESULT/EXIT/COUNTS/ARTIFACT/SCHEMA/FAILED/WARNINGS/NEXT) 그대로.
6. **Affected Objects 점검** — 실제 touched files / 선언된 변경을 Brief 의 `Affected Objects` 와 대조.
   불일치는 사용자에게 표시. *runner 의 자동 검증 범위 외* 이므로 사람이 한 번 본다.
7. **Final Control Point 결정** — runner exit 0 *그리고* Affected Objects 정합 확인 → 진행 가능.
   하나라도 실패면 차단.

## 직접 실행 (사용자가 손으로 invoke)

```powershell
# 1) runner 직접 호출 (가장 짧은 경로)
python 4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/run.py `
  --brief 3_Domain_Project_Playbooks/<playbook>/<task>_NPI_Brief.md
```

```powershell
# 2) before-final hook 경유 (Final Control Point 자동 차단 라인과 동일 경로)
powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass `
  -File 4_Task_Level_Execution_Templates/claude-code/hooks/before-final.ps1 `
  -Brief 3_Domain_Project_Playbooks/<playbook>/<task>_NPI_Brief.md
```

```cmd
REM 3) cmd 환경
4_Task_Level_Execution_Templates\claude-code\hooks\before-final.cmd ^
  3_Domain_Project_Playbooks\<playbook>\<task>_NPI_Brief.md
```

선택 옵션:
- `--out <path>` (runner) 또는 `-Out <path>` (hook): `NPI_Verification.md` 출력 경로 지정.
- `--strict` (runner) 또는 `-Strict` (hook): `factory.yaml` 미발견을 fail 로 격상.

## Exit code 규칙

| Code | 의미 | Final Control Point 영향 |
|---|---|---|
| **0** | 전체 Pass — 모든 AC 가 method 검증을 통과 + 각 Pass 행에 evidence 존재 | 진행 가능 |
| **1** | AC 검증 실패 — 하나 이상의 AC 가 Fail (또는 Pass 인데 evidence 비어 자동 격하) | 차단. `NPI_Verification.md` 의 Fail 행을 해결 후 재실행. |
| **2** | schema/parse error — Brief 파일 없음 / `acceptance_criteria` YAML 블록 없음 / `schema_version` 누락·미지원 / YAML 파싱 실패 / 출력 쓰기 실패 / `--strict` + factory.yaml 미발견 | 차단. Brief 의 structured AC YAML 블록을 점검 후 재실행. |

## Output

`NPI_Verification.md` — runner 가 생성한다. 컬럼은 다음으로 고정:

| AC ID | Statement | Method | Result | Evidence |
|---|---|---|---|---|

**중요 — 본 명령은 결과를 임의로 수정하지 않는다.**
- runner 가 Pass 라 했으면 Pass, Fail 이라 했으면 Fail. 명령/skill/hook 어느 계층도 자의적으로
  격상/격하하지 않는다 (fake pass 통로 차단).
- 생성된 `NPI_Verification.md` 는 사람 confirmer 의 1차 자료다. 본 명령은 이 파일을 *수정하지 않는다.*
- `manual` method AC 의 confirmer/date 는 Brief 작성 시점에 채워져 있어야 한다. 검증 시점에 비어 있으면
  runner 가 즉시 Fail 처리한다 (fake pass 차단).

## Subagent 실행 권장 조건

다음 중 *하나라도* 만족하면 `mode=subagent` 로 실행하는 것을 권장한다 (skill `§7` 참조).

- **AC 개수 ≥ 8** — 매핑 표 행 수가 늘어 main context 점유율이 큼.
- **`command` method 비율 ≥ 1/3** — stdout/stderr 50줄 ×다수 → 토큰 폭증 위험.
- **단일 명령의 예상 출력량이 큼** — 빌드, 테스트 스위트 등 수백~수천 줄 가능성.
- **동일 task 내 재검증 2회 이상** — 첫 호출 결과로 main context 가 이미 부풀어 있음.
- **사용자가 명시적으로 격리 실행을 요청** — "isolate / 격리 / subagent 로".

전혀 해당하지 않으면 `inline` (예: AC 3~5개의 단순 file_exists/manual 위주) 로 실행해 오버헤드를 피한다.

subagent 모드에서도 본 명령의 표준 절차는 동일하게 적용되며, subagent 는 §"Procedure" 5단계의
*표준 페이로드* 만 main agent 에게 반환한다 (raw 로그 패스스루 금지).

## Acceptance Criteria for this command itself
- 모든 AC 항목이 `NPI_Verification.md` 매핑 표에 1행씩 존재.
- 모든 Pass 행에 evidence 존재 (runner 가 강제).
- Affected Objects diff 가 reconcile 됨 (추가는 설명, 제거는 정당화).
- 본 명령은 검증 결과를 변형하지 않는다 (runner = single source of truth).

## Anti-patterns
- ❌ "Looks good" 검증 (runner 우회, evidence 없는 Pass 표기).
- ❌ 명령/skill/hook 이 직접 검증 로직을 흉내내기 (자체 YAML 파싱, 자체 method 실행, 자체 표 생성).
- ❌ `NPI_Verification.md` 를 runner 외 계층이 사후 수정.
- ❌ runner 미존재 시 자체 fallback 검증 (즉시 exit 2 가 옳다).
- ❌ AC 를 silent 하게 waive (waive 가 정당하면 Brief 의 AC 자체를 수정하고 변경 사유를 History 에 박제).
- ❌ 동일 자동화 (runner 자신이 산출한 artifact 만으로) 자체 검증 — 사람 confirmer 의 인정 단계를 생략.

## 변경 이력 (이 명령 문서)
- v0.1.0 (2026-05-07) — markdown 수동 절차 형태로 도입.
- v0.2.0 (2026-05-08) — skill ↔ runner ↔ hook 3계층 호출 모델로 재정의 (T-B6). 수동 절차 폐기.
  runner = single source of truth 명시. 직접 실행 / hook 실행 두 경로 제공. subagent 권장 조건 5개 박제.
