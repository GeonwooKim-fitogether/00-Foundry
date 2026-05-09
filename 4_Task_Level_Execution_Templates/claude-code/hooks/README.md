# Hooks

A **Hook** is an automatic check, blocker, or alert tied to a Claude Code event (tool call, task transition, file change). Hooks are the engine that enforces ACDE and Minimum Human Intervention without humans riding shotgun.

## Status (v0.2.0)
- **`before-final` hook is now implemented** (T-B4, 2026-05-08).
  - PowerShell shim: `before-final.ps1`
  - Windows cmd wrapper: `before-final.cmd`
- 다른 hook 후보들은 여전히 `hook-candidates.md` 의 candidate 상태.

## Hook Categories
- **Gate hooks** — run before a sensitive action; can block.
- **Verify hooks** — run after a state change; check invariants.
- **Alert hooks** — emit a notification when a Critical Decision condition appears.

## Authoring Standard
각 hook 은 다음을 선언한다.
- 이벤트(s) 와 timing (pre/post).
- Pass/block 판단 기준.
- 차단 시 Claude 에게 노출할 actionable 메시지.
- runner / external 도구 의존이 있다면 그 의존성과 단일 source of truth 명시.

---

## `before-final` hook (implemented, v0.2.0)

### 목적
Final Control Point 직전, **모든 AC 가 evidence 와 함께 Pass 인지를 자동으로 검증**한다.
하나라도 Fail 또는 schema 오류면 **차단** (non-zero exit) + actionable 메시지.

### runner 와의 관계 — 매우 중요
**hook 은 검증 로직을 1줄도 가지지 않는다.** 본 hook 은:

1. 같은 저장소의 `../skills/verification-runner/run.py` 의 *경로만* 해석한다.
2. 사용자가 준 인자를 그대로 forwarding 한다 (`--brief`, `--out`, `--strict`).
3. runner 의 exit code 를 그대로 passthrough 한다.
4. 사람이 한눈에 보기 좋은 한 줄 상태 메시지(PASS/BLOCK) 만 추가 출력한다.

YAML 파싱 / AC schema 검증 / 3종 method 실행 / `NPI_Verification.md` 생성은 **전부 `run.py` 가 한다**.
hook 이 결과를 *해석* 하거나 *수정* 하면 즉시 *runner = single source of truth* 원칙 위반이다.
runner 가 미발견인 상황에서 hook 이 자체 fallback 으로 검증을 흉내내는 것 또한 금지 (즉시 exit 2).

### 인터페이스

#### PowerShell shim — `before-final.ps1`
```powershell
.\before-final.ps1 -Brief <brief_path> [-Out <out_path>] [-Strict]
```

#### Windows cmd wrapper — `before-final.cmd`
```cmd
before-final.cmd <brief_path> [-Strict] [-Out <out_path>]
```
- `.cmd` 는 `.ps1` 를 호출한다. 인자는 그대로 forwarding.
- `.cmd` 파일은 **ASCII 전용**으로 작성한다. cmd.exe 는 .cmd 파일을 시스템 ANSI 코드페이지(한국어 환경 = cp949) 로 파싱하므로 한국어/유니코드 문자가 들어가면 파싱이 깨진다.

### Exit code 처리

| Code | 의미 | hook 콘솔 메시지 |
|---|---|---|
| 0 | 모든 AC Pass | `[before-final] PASS - Final Control Point may proceed.` |
| 1 | AC 검증 실패 | `[before-final] BLOCK - Fail rows in NPI_Verification.md must be resolved, then re-run.` |
| 2 | schema/parse error 또는 runner 미발견 | `[before-final] BLOCK - Inspect the Brief's structured AC YAML block, then re-run.` |

상태 메시지는 의도적으로 **ASCII-only**. Windows PowerShell 5.1 이 BOM 없는 UTF-8 .ps1 의 한글을
스크립트 로드 시점에 cp949 로 잘못 해석하는 함정을 피하기 위함.
한국어 설명은 본 README 와 스크립트 주석에 있다 (런타임 출력에는 없음).

### Claude Code `settings.json` 등록 예시

> 본 예시는 v0.2.0 시점의 *권장 형태* 다. Claude Code 의 hook 페이로드 형식은 통합 시점에 환경변수
> 또는 stdin JSON 등으로 brief 경로가 전달된다고 가정한다. 핵심은 이 hook 이 **외부에서 호출
> 가능한 일반 CLI** 라는 점이며, 통합 형태는 등록 시 환경에 맞춰 조정한다.

```jsonc
{
  "hooks": {
    "before-final": {
      "description": "Final Control Point gate - block until all AC pass.",
      "command": "powershell.exe",
      "args": [
        "-NoProfile",
        "-NonInteractive",
        "-ExecutionPolicy", "Bypass",
        "-File", "${workspaceFolder}/4_Task_Level_Execution_Templates/claude-code/hooks/before-final.ps1",
        "-Brief", "${BRIEF_PATH}"
      ],
      "blockingExitCodes": [1, 2]
    }
  }
}
```

cmd 환경에서 호출하려면 `command` 와 `args` 를 다음으로 대체:
```jsonc
"command": "cmd.exe",
"args": [
  "/c",
  "${workspaceFolder}/4_Task_Level_Execution_Templates/claude-code/hooks/before-final.cmd",
  "${BRIEF_PATH}"
]
```

### 수동 검증 — should-pass / should-block / parse-error

세 fixture 가 `../skills/verification-runner/tests/` 에 있다.

```powershell
# 1) should-pass  ->  exit 0
.\before-final.ps1 -Brief ..\skills\verification-runner\tests\fixture_pass.md -Out $env:TEMP\h_pass.md

# 2) should-block ->  exit 1   (AC 2개 모두 의도적 Fail)
.\before-final.ps1 -Brief ..\skills\verification-runner\tests\fixture_block.md -Out $env:TEMP\h_block.md

# 3) parse-error ->  exit 2   (schema_version 누락된 Brief)
.\before-final.ps1 -Brief 3_Domain_Project_Playbooks\ai-npi-platform\B-002_NPI_Brief.md -Out $env:TEMP\h_parse.md
```

T-B4 작업 시 위 3 케이스 + `.cmd` wrapper 4 케이스 (should-pass / should-block / -Strict forwarding / usage) 모두 정확한 exit code 로 통과 확인.

### 한계 / 알려진 함정
- `.ps1` 와 `.cmd` 는 **모두 ASCII-only 콘솔 출력**. 한글 메시지는 `run.py` (Python `sys.stdout.reconfigure(encoding="utf-8")`) 가 출력한다.
- `.cmd` 는 PowerShell 을 다시 호출하므로 첫 호출 대비 약간의 추가 startup overhead. 1~2초.
- Cross-platform 미지원 (v0.2.0 범위 외). 비-Windows 환경에서는 `python run.py …` 직접 호출 또는 v0.3.0 의 `.sh` shim 추가.

---

## 다른 hook 후보 (still candidates)

`hook-candidates.md` 참조. v0.2.0 에서는 `before-final` 만 implemented.
