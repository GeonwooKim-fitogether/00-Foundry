# SKILL — verification-runner (Foundry v0.2.0)

> 본 skill 은 `validate-output` 명령이 의존하는 **표준 호출 패키지**다.
> **검증 로직은 본 skill 에 *없다*.** 모든 로직은 같은 폴더의 `run.py` (single source of truth) 에만 있다.
> skill 은 (a) runner 를 일관된 방식으로 부르고, (b) 호출 전후 점검을 표준화하고, (c) 결과를
> *decision-ready summary* 로 정리해 main agent 에게 반환하는 *얇은 호출/요약 계층*이다.

## 1. 목적 (Purpose)

Brief 의 structured AC YAML 블록을 읽어 모든 AC 가 evidence 와 함께 Pass 인지 확인한 뒤,
Final Control Point 의 사람 의사결정자에게 **간결한 결정-가능한 요약**을 돌려준다.

## 2. 언제 사용할지 (When to Use)

다음 중 하나라도 해당하면 본 skill 을 사용한다.

- `validate-output` 명령이 호출되었을 때 (1차 트리거).
- Final Control Point 직전, 어떤 task 든 *AC ↔ Verification 매핑 표가 비어 있거나 갱신되지 않은 상태*일 때.
- 사용자가 명시적으로 *"검증 돌려줘 / verify / runner 돌려줘"* 를 요청했을 때.
- `before-final` hook 이 차단 신호를 보낸 직후 사람 점검을 보조해야 할 때 (T-B4 이후).

다음의 경우엔 *사용하지 않는다*:

- AC 가 아직 동결되지 않은 상태 (Brief 가 draft).
- runner 코드 자체를 디버깅 중 (직접 `python run.py` 실행이 적합).
- 검증 외 작업 (계획 수립, 코드 변경, 문서 작성).

## 3. 입력 (Inputs)

| 필드 | 형태 | 필수 | 비고 |
|---|---|---|---|
| `brief_path` | 절대 또는 프로젝트 루트 상대 경로 | 필수 | `*_NPI_Brief.md` 단일 파일. 본 Brief 안에 `schema_version`/`acceptance_criteria` 를 가진 ` ```yaml ` 블록이 *반드시* 있어야 한다. |
| `out_path` | 경로 | 선택 | 미지정 시 Brief 와 같은 디렉토리의 `NPI_Verification.md`. |
| `strict` | bool | 선택 | true 이면 `factory.yaml` 미발견을 fail 로 격상 (exit 2). |
| `mode` | `inline` \| `subagent` | 선택 | 기본 `inline`. 아래 §7 조건 하나라도 만족하면 `subagent` 권장. |

## 4. 출력 (Outputs)

본 skill 의 호출 종료 시 main agent 에게 반환되는 **표준 페이로드**:

```
RESULT:    PASS | FAIL | PARSE_ERROR
EXIT:      0 | 1 | 2
COUNTS:    total=<n> pass=<n> fail=<n>
ARTIFACT:  <out_path>            # NPI_Verification.md 절대 경로
SCHEMA:    <schema_version>      # parse 성공 시
FAILED:    [<AC ID>: <한 줄 사유>, ...]   # 없으면 빈 배열
WARNINGS:  [<stderr 한 줄>, ...]          # 없으면 빈 배열
NEXT:      <한 줄 권고>           # "Final Control Point 진행" / "AC-X 재실행" / "Brief 수정 후 재호출" 등
```

부산물 (skill 자체는 *생성하지 않는다*; runner 가 생성):
- `NPI_Verification.md` (AC ↔ Verification 매핑 표). 매핑 표 컬럼은 `AC ID | Statement | Method | Result | Evidence`.

## 5. 표준 실행 절차 (Standard Procedure)

다음 순서를 *그대로* 따른다. 분기/추측 금지.

1. **사전 점검 (Pre-flight)** — *읽기만*, 변경 금지.
   - `brief_path` 존재 여부 확인.
   - `factory.yaml` 이 Brief 위로 탐색해 발견되는지 확인. 미발견이면 `WARNINGS` 에 추가.
   - 같은 폴더의 `run.py` 가 존재하는지 확인. 없으면 즉시 `RESULT=PARSE_ERROR` 로 보고하고 절차를 종료한다.
2. **실행 모드 결정 (§7 참조)** — `inline` vs `subagent`. 의심되면 `subagent`.
3. **runner 호출** (§8 형태로 정확히).
4. **결과 수집** — exit code + stdout + stderr + 생성된 `NPI_Verification.md` 경로.
5. **요약 정리** — §4 표준 페이로드로 변환.
   - `FAILED` 항목은 `NPI_Verification.md` 매핑 표를 *grep* 해서 `Result=Fail` 행의 `AC ID` + `Evidence` 첫 80자로 채운다.
   - **raw stdout/stderr 전체를 main context 에 붙이지 않는다.** evidence 는 항상 `NPI_Verification.md` 파일 *링크*로 위임한다 (§9 금지 사항).
6. **NEXT 한 줄 권고 결정** —
   - exit 0 → `"Final Control Point 진행 가능. 사람 confirmer 가 manual AC 의 confirmer/date 를 최종 인정."`
   - exit 1 → `"NPI_Verification.md 의 Fail 행 N건 해결 후 본 skill 재호출."`
   - exit 2 → `"Brief 의 structured AC YAML 블록을 수정하고 본 skill 재호출. (자세한 사유: <runner stderr 첫 줄>)"`
7. **반환** — main agent 로 §4 페이로드만 보낸다. *그 이상은 보내지 않는다.*

## 6. context 사용 원칙 (Context Discipline)

- 본 skill 은 **`brief_path` 와 같은 디렉토리의 파일만** 읽는 것을 기본으로 한다.
- 추가로 읽어도 되는 것: `run.py` (존재 확인 목적), 생성된 `NPI_Verification.md` (요약 추출 목적).
- 읽지 않는다: 다른 Brief, Blueprint, Worklist, BuildLog, 그 외 코드/문서. *runner 가 그것을 필요로 하면 runner 의 method 가 직접 읽는다.*
- main context 에 **명령 전체 stdout/stderr 를 dump 하지 않는다.** 첫/마지막 의미 있는 줄 1개씩 외에는 버린다.
- 매핑 표 자체는 main context 에 옮기지 않는다 — `ARTIFACT` 경로로 위임한다.

## 7. subagent 사용 조건 (When to Run in a Subagent)

다음 중 *하나라도* 만족하면 `mode=subagent` 로 실행한다 (`verification-runner` subagent — `agents/agent-candidates.md` 참조).

| 조건 | 임계 | 근거 |
|---|---|---|
| AC 개수 | ≥ 8 | 매핑 표 행 수가 늘어 main context 점유율이 큼. |
| `command` method 비율 | 전체 AC 의 ≥ 1/3 | stdout/stderr 50줄 ×다수 → 토큰 폭증 위험. |
| 단일 명령 예상 출력량 | "수백~수천 줄 가능성 있음" (예: 빌드, 테스트 스위트) | 한 번의 dump 가 main context 를 흐림. |
| 동일 task 내 재호출 | 2회차 이상 | 첫 호출 결과로 main context 가 이미 부풀어 있음. |
| 사용자 명시 요청 | "isolate / 격리 / subagent 로" | 사용자 의도 우선. |

조건에 *전혀* 해당하지 않으면 `mode=inline` 로 실행해 오버헤드를 피한다 (예: AC 3~5개의 단순 file_exists / manual 위주 검증).

subagent 모드에서도 본 skill 의 §5 절차는 동일하게 적용된다. subagent 는 §4 표준 페이로드 *그대로*를
main agent 에게 반환하며, *raw 로그를 패스스루하지 않는다*.

## 8. runner 호출 방식 (Runner Invocation)

runner 는 *항상* 다음 중 하나의 형태로 호출한다.

```bash
# 기본 (inline)
python <skill_dir>/run.py --brief <brief_path>

# 출력 경로 지정
python <skill_dir>/run.py --brief <brief_path> --out <out_path>

# 엄격 모드 (factory.yaml 미발견을 fail 로 격상)
python <skill_dir>/run.py --brief <brief_path> --strict
```

여기서 `<skill_dir>` = `4_Task_Level_Execution_Templates/claude-code/skills/verification-runner/` (본 SKILL.md 파일이 위치한 디렉토리).

규칙:
- runner 의 인자/플래그를 **변형하지 않는다.** 예: `--strict` 는 *명시적으로 요구된 경우에만* 추가.
- 호출 *전*에 작업 디렉토리를 임의로 바꾸지 않는다. project root 탐색은 runner 가 한다.
- 호출 *후* 생성된 `NPI_Verification.md` 를 절대 다시 *수정*하지 않는다 (사람 confirmer 가 다음 단계에서 본다).
- 호출 *대신* 본 skill 이 직접 method 를 흉내내지 않는다 (예: 자체적으로 `subprocess.run` 또는 파일 존재 검사). **그 행위는 runner = single source of truth 원칙 위반.**

## 9. 실패 시 보고 방식 (Failure Reporting)

skill 이 main agent 에게 돌려보내는 실패 보고는 *항상* §4 표준 페이로드 + 다음 추가 규칙을 따른다.

- `RESULT=FAIL` (exit 1) — `FAILED` 배열은 *최대 10개*까지만 포함. 11개 이상이면 처음 10개 + `"…그 외 N건 (NPI_Verification.md 참조)"` 한 줄.
- `RESULT=PARSE_ERROR` (exit 2) — `FAILED` 는 빈 배열, 대신 `WARNINGS` 첫 항목에 runner stderr 의 첫 의미 있는 줄.
- 어떤 경우에도 raw stdout/stderr 전체를 본문으로 옮기지 않는다.
- `NEXT` 한 줄은 *행동 지향*으로 작성한다. ("확인하세요" 금지. "AC-3 의 paths 항목을 수정한 뒤 본 skill 을 재호출하세요." 가 옳음.)

main agent 는 본 페이로드를 받은 즉시 사용자에게 표준 형태로 그대로 노출하면 된다.

## 10. 금지 사항 (Anti-patterns / Forbidden)

- ❌ runner 가 하는 일을 skill 이 흉내내기 (자체 YAML 파싱, 자체 method 실행, 자체 매핑 표 작성).
- ❌ runner 의 stdout/stderr 전체를 main context 에 붙이기.
- ❌ 생성된 `NPI_Verification.md` 를 skill 이 *수정* 하기 (사람 confirmer 의 검토 대상이다).
- ❌ runner 가 fail 했는데 skill 이 자의적으로 Pass 판정 격상하기 (fake pass 통로).
- ❌ runner 가 Pass 했는데 skill 이 추가 *간접* 점검을 들이대 Fail 로 격하하기 (runner = single truth 위반).
- ❌ skill 이 Brief 를 *수정* 하기 (입력은 read-only).
- ❌ subagent 모드인데 raw 로그를 그대로 패스스루하기 (§7 마지막 단락).
- ❌ runner 미설치/미존재 상황에서 자체 fallback 으로 검증 흉내내기. → 즉시 `PARSE_ERROR` 로 보고.

## 11. 변경 이력

- 2026-05-08 — v0.2.0 첫 정의 (T-B3). T-B1 (host=Python), T-B8 (schema_version 필수), T-B2 (`run.py` 구현 + 5종 검증 통과) 결과 위에 정렬.
