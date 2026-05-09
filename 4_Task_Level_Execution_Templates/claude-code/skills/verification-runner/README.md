# verification-runner (Foundry v0.2.0)

> NPI_Brief.md 의 **structured AC YAML 블록**을 읽어 3종 verification method 를 실행하고
> NPI_Verification.md 의 AC ↔ Verification 매핑 표를 생성하는 단일 CLI.
>
> Blueprint 원칙: **runner 는 single source of truth**. hook / skill / subagent 는 본 runner 를
> 호출·격리·요약하는 얇은 계층일 뿐이다.

## 요구사항

- Python 3.11 이상
- 외부 의존성 없음 (Python 표준 라이브러리만 사용 — `stdlib-first` 정책)
- 호출 측은 `verification-runner/run.py` 를 직접 실행

## 사용법

```bash
# 기본 실행 (출력은 Brief 와 같은 디렉토리에 NPI_Verification.md)
python run.py --brief 3_Domain_Project_Playbooks/<playbook>/<task>_NPI_Brief.md

# 출력 경로 지정
python run.py --brief <brief_path> --out <output_path>

# 경고를 fail 로 격상 (예: factory.yaml 미발견 시 exit 2)
python run.py --brief <brief_path> --strict
```

`run.py` 는 어디서 실행해도 무방하다. **프로젝트 루트는 Brief 위치에서 위로 탐색해 `factory.yaml` 을
찾은 디렉토리**로 자동 결정된다. `factory.yaml` 을 찾지 못하면 현재 작업 디렉토리를 fallback 으로
사용하고 stderr 에 경고를 출력한다 (`--strict` 시 fail).

## Exit code 규칙

| Code | 의미 |
|---|---|
| 0 | 모든 AC 가 Pass (각 Pass 행에 Evidence 존재) |
| 1 | 하나 이상의 AC 가 Fail |
| 2 | schema_version 누락/미지원 / YAML 파싱 실패 / Brief 파일 없음 / 출력 쓰기 실패 등 입력측 오류 |

## Brief 입력 형식

`NPI_Brief.md` 안에 **단 하나의** ` ```yaml ... ``` ` 펜스가 있어야 하며,
그 블록은 `schema_version` 과 `acceptance_criteria` 두 키를 모두 포함해야 한다.

```yaml
schema_version: "0.2.0"          # 필수, v0.2.0 runner 는 "0.2.0" 만 지원
acceptance_criteria:             # 필수, 1개 이상의 AC 항목
  - id: AC-1                     # 필수
    statement: "..."             # 필수
    method: command              # 필수, command|file_exists|manual 중 하나
    command: "npm test"          # method=command 일 때 필수
    workdir: "."                 # 선택, 기본 "."
    expect_exit: 0               # 선택, 기본 0
```

자세한 method 별 필드 정의는 `4_Task_Level_Execution_Templates/NPI_Brief.md` 템플릿 참조.

## 검증 method 3종

| method | 통과 조건 | 필수 필드 | 선택 필드 |
|---|---|---|---|
| `command` | `subprocess.run(shell=True)` 의 exit code == `expect_exit` | `command` | `workdir`(기본 `.`), `expect_exit`(기본 0) |
| `file_exists` | 모든 `paths` 항목이 파일로 존재. `must_be_nonempty=true` 면 빈 파일도 fail | `paths`(1개 이상) | `must_be_nonempty`(기본 false) |
| `manual` | 두 필수 필드가 모두 채워져 있고 `confirm_date` 가 `YYYY-MM-DD` ISO 8601 형식 | `manual_confirmer`, `confirm_date` | `note` |

`manual` method 의 안전장치: 필수 필드 누락 또는 ISO date 형식 불일치 시 즉시 Fail (fake pass 차단).

### `command` method 신뢰 경계 — 보안 주의

본 runner 는 `subprocess.run(cmd, shell=True)` 로 명령을 실행한다. 이는 **Brief 작성자가 신뢰
경계 안에 있다**는 가정 하에 채택된 정책이다 (T-B2 결정, 2026-05-08).

- **사용해도 되는 입력**: Foundry 사용자 본인이 직접 작성한 Brief.
- **사용하면 안 되는 입력**: 외부 네트워크/팀원이 작성해 검증 없이 받은 Brief, 자동 생성 Brief.

`shell=True` 채택 이유: Windows 에서 `npm`, `pytest`, `.cmd`, `.bat` shim 호출 호환성.
cross-platform 명령 작성은 Brief 작성자 책임 (Blueprint §"R-OS차이").

## 입력 측 제약 (v0.2.0 minimal-subset YAML 파서)

본 runner 는 의존성 0 정책을 위해 **표준 라이브러리만으로 동작하는 minimal-subset YAML 파서**를
내장한다. 일반 YAML 의 부분집합만 지원한다.

지원:
- 최상위 `key: value` (scalar) / 최상위 `key:` 다음 `- ` 리스트
- 리스트 항목은 dict 만 허용 (각 항목 `- id: ...` 로 시작)
- 항목 내부 scalar 키, 항목 내부 simple list (`paths:` 다음 `- 문자열`)
- 타입: int, bool(`true`/`false`), null(`null`/`~`), 따옴표 문자열, 따옴표 없는 문자열
- 주석: `#` 이후 (따옴표 밖에 한해서)
- 들여쓰기: **공백만** (탭 거부)

지원하지 않음 (사용 시 파싱 에러):
- 다중 문서 (`---`)
- anchor / alias (`&`, `*`)
- 단일 라인 flow 형식 (`[a, b]`, `{k: v}`)
- 멀티라인 스칼라 (`|`, `>`)
- 깊이 3단계 이상 중첩

이런 기능이 필요해지면 v0.3.0 에서 PyYAML 단일 의존성 채택을 재평가한다.

## evidence 캡처 정책

- `command`: stdout / stderr 각각 **마지막 50줄** + exit code + 명령 + workdir
- `file_exists`: 각 path 별 `exists / size / pass`
- `manual`: confirmer + ISO date + note(있으면)

설정화는 v0.3.0 이후로 미룬다 (T-B2 결정).

## 자가 점검 (수동 실행)

```bash
# Pass 케이스: 같은 폴더의 fixture
python run.py --brief tests/fixture_pass.md
# → exit 0, NPI_Verification.md 가 tests/ 에 생성됨

# Schema 미준수 케이스: schema_version 이 없는 Brief 를 임의로 만들면 exit 2 가 나와야 한다.
```

## 한계

- 단일 Brief 단일 YAML 블록 가정. 여러 ` ```yaml ` 블록이 있고 둘 다 schema 키를 포함하면 *첫 번째*만 사용.
- 셸 차이는 v0.2.0 범위 외. 명령은 그대로 호출되며 OS 의존성은 사용자 책임.
- `command` 는 600초 timeout. 더 긴 작업은 v0.2.0 범위 외.

## 변경 이력

- 2026-05-08 — v0.2.0 첫 구현 (T-B2). host=Python 3.11+, stdlib-first, schema_version="0.2.0" 단일 지원.
