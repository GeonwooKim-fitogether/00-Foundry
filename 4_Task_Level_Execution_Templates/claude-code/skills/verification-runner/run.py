#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verification-runner — Foundry v0.2.0
NPI_Brief.md 의 structured AC YAML 블록을 파싱해 3종 method 를 실행하고
NPI_Verification.md 의 AC ↔ Verification 매핑 표를 생성한다.

사용:  python run.py --brief <brief_path> [--out <output_path>] [--strict]
exit: 0=전체 Pass, 1=AC 검증 실패, 2=schema/parse error.
의존성: 표준 라이브러리만 사용. Python 3.11+.
"""

from __future__ import annotations

import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# 상수
# ---------------------------------------------------------------------------

EXIT_PASS = 0
EXIT_FAIL = 1
EXIT_PARSE_ERROR = 2

SUPPORTED_SCHEMA_VERSIONS = {"0.2.0"}
ALLOWED_METHODS = {"command", "file_exists", "manual"}
EVIDENCE_LINE_LIMIT = 50
RUNNER_VERSION = "0.2.0"


# ---------------------------------------------------------------------------
# 프로젝트 루트 탐색 (factory.yaml 위로 탐색)
# ---------------------------------------------------------------------------

def find_project_root(start: Path) -> tuple[Path, bool]:
    cur = start.resolve()
    for p in [cur] + list(cur.parents):
        if (p / "factory.yaml").is_file():
            return p, True
    return Path.cwd().resolve(), False


# ---------------------------------------------------------------------------
# YAML 블록 추출 (markdown ```yaml ... ``` 펜스에서)
# ---------------------------------------------------------------------------

YAML_FENCE = re.compile(r"```yaml[ \t]*\n(.*?)\n```", re.DOTALL)


def extract_ac_yaml_block(brief_text: str) -> str | None:
    """structured AC 블록 식별 — `acceptance_criteria` 키 등장으로 판별.
    schema_version 의 유무는 추출 단계가 아니라 검증 단계(validate_schema)에서 잡는다.
    그래야 누락 시 'YAML 블록 없음' 이 아니라 'schema_version 누락' 이라는 정확한 메시지가 나온다.
    """
    for m in YAML_FENCE.finditer(brief_text):
        body = m.group(1)
        if "acceptance_criteria" in body:
            return body
    return None


# ---------------------------------------------------------------------------
# Minimal-subset YAML 파서
#   허용: 최상위 scalar 키, 최상위 list 키 (- 항목 = dict),
#         항목 내부 scalar 키, 항목 내부 simple list (- 스칼라).
#   타입: int / bool(true,false) / null(~,null) / quoted/unquoted string.
#   주석: # 부터 줄 끝까지 (따옴표 밖에 한해서).
#   탭 들여쓰기: 거부.
# ---------------------------------------------------------------------------

class YamlParseError(Exception):
    pass


def _strip_comment(line: str) -> str:
    in_s = in_d = False
    out = []
    for ch in line:
        if ch == "'" and not in_d:
            in_s = not in_s
        elif ch == '"' and not in_s:
            in_d = not in_d
        elif ch == "#" and not in_s and not in_d:
            break
        out.append(ch)
    return "".join(out).rstrip()


def _parse_scalar(s: str):
    s = s.strip()
    if s == "" or s.lower() in ("null", "~"):
        return None
    if s.lower() == "true":
        return True
    if s.lower() == "false":
        return False
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    try:
        return int(s)
    except ValueError:
        return s


def _indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


_KV_RE = re.compile(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$")


def parse_yaml_subset(text: str) -> dict:
    raw = [ln.rstrip() for ln in text.splitlines()]
    lines: list[str] = []
    for ln in raw:
        cleaned = _strip_comment(ln)
        if cleaned.strip() == "":
            continue
        if "\t" in cleaned:
            raise YamlParseError("탭 들여쓰기는 지원하지 않습니다. 공백을 사용하세요.")
        lines.append(cleaned)

    result: dict = {}
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if _indent_of(line) != 0:
            raise YamlParseError(f"최상위 키는 들여쓰기 0이어야 합니다: {line!r}")
        m = _KV_RE.match(line)
        if not m:
            raise YamlParseError(f"최상위 'key: value' 형식이 아닙니다: {line!r}")
        key, rest = m.group(1), m.group(2)
        if rest != "":
            result[key] = _parse_scalar(rest)
            i += 1
        else:
            j = i + 1
            if j >= n or _indent_of(lines[j]) == 0:
                result[key] = None
                i = j
                continue
            block_indent = _indent_of(lines[j])
            if lines[j].lstrip().startswith("- "):
                items, i = _parse_list_of_dicts(lines, j, block_indent)
                result[key] = items
            else:
                raise YamlParseError(f"키 {key!r} 의 값 블록 형태를 인식하지 못했습니다.")
    return result


def _parse_list_of_dicts(lines, start, list_indent) -> tuple[list, int]:
    items: list = []
    i, n = start, len(lines)
    while i < n:
        line = lines[i]
        ind = _indent_of(line)
        if ind < list_indent:
            break
        if ind != list_indent or not line.lstrip().startswith("- "):
            break
        first_kv = line.lstrip()[2:]
        m = _KV_RE.match(first_kv)
        if not m:
            raise YamlParseError(f"리스트 항목은 '- key: value' 형식이어야 합니다: {line!r}")
        item: dict = {}
        key, rest = m.group(1), m.group(2)
        sub_indent = list_indent + 2
        if rest != "":
            item[key] = _parse_scalar(rest)
            i += 1
        else:
            if i + 1 < n and _indent_of(lines[i + 1]) > list_indent and lines[i + 1].lstrip().startswith("- "):
                sub_list_indent = _indent_of(lines[i + 1])
                vals, new_i = _parse_simple_list(lines, i + 1, sub_list_indent)
                item[key] = vals
                i = new_i
            else:
                item[key] = None
                i += 1
        while i < n:
            ln = lines[i]
            ind2 = _indent_of(ln)
            if ind2 <= list_indent:
                break
            if ind2 != sub_indent:
                raise YamlParseError(f"항목 내부 들여쓰기 불일치: {ln!r}")
            sm = _KV_RE.match(ln.lstrip())
            if not sm:
                raise YamlParseError(f"항목 필드 형식 오류: {ln!r}")
            sk, sr = sm.group(1), sm.group(2)
            if sr != "":
                item[sk] = _parse_scalar(sr)
                i += 1
            else:
                if i + 1 < n and _indent_of(lines[i + 1]) > sub_indent and lines[i + 1].lstrip().startswith("- "):
                    sub_list_indent = _indent_of(lines[i + 1])
                    vals, new_i = _parse_simple_list(lines, i + 1, sub_list_indent)
                    item[sk] = vals
                    i = new_i
                else:
                    item[sk] = None
                    i += 1
        items.append(item)
    return items, i


def _parse_simple_list(lines, start, list_indent) -> tuple[list, int]:
    out: list = []
    i, n = start, len(lines)
    while i < n:
        ln = lines[i]
        ind = _indent_of(ln)
        if ind < list_indent:
            break
        if ind != list_indent or not ln.lstrip().startswith("- "):
            break
        out.append(_parse_scalar(ln.lstrip()[2:]))
        i += 1
    return out, i


# ---------------------------------------------------------------------------
# Schema 검증
# ---------------------------------------------------------------------------

def validate_schema(parsed: dict) -> None:
    if not isinstance(parsed, dict):
        raise YamlParseError("최상위가 매핑(dict)이 아닙니다.")
    if "schema_version" not in parsed:
        raise YamlParseError(
            "schema_version 필드가 없습니다. 최상위에 schema_version: \"0.2.0\" 를 추가하세요."
        )
    sv = parsed["schema_version"]
    if not isinstance(sv, str):
        raise YamlParseError(f"schema_version 은 문자열이어야 합니다. 현재 값: {sv!r}")
    if sv not in SUPPORTED_SCHEMA_VERSIONS:
        raise YamlParseError(
            f"지원하지 않는 schema_version: {sv!r}. 지원 목록: {sorted(SUPPORTED_SCHEMA_VERSIONS)}"
        )
    acs = parsed.get("acceptance_criteria")
    if not isinstance(acs, list) or len(acs) == 0:
        raise YamlParseError("acceptance_criteria 배열이 비어 있거나 정의되지 않았습니다.")
    seen: set[str] = set()
    for idx, ac in enumerate(acs):
        if not isinstance(ac, dict):
            raise YamlParseError(f"acceptance_criteria[{idx}] 가 dict 가 아닙니다.")
        for f in ("id", "statement", "method"):
            if f not in ac or ac[f] in (None, ""):
                raise YamlParseError(
                    f"acceptance_criteria[{idx}] 에 {f!r} 필드가 없거나 비어 있습니다."
                )
        ac_id = str(ac["id"])
        if ac_id in seen:
            raise YamlParseError(f"AC id 중복: {ac_id!r}")
        seen.add(ac_id)
        if ac["method"] not in ALLOWED_METHODS:
            raise YamlParseError(
                f"AC {ac_id}: 지원하지 않는 method {ac['method']!r}. "
                f"허용: {sorted(ALLOWED_METHODS)}"
            )


# ---------------------------------------------------------------------------
# method 실행기
# ---------------------------------------------------------------------------

def _tail_lines(s: str | None, n: int) -> str:
    if not s:
        return "(empty)"
    parts = s.splitlines()
    if len(parts) > n:
        parts = parts[-n:]
    return "\n".join(parts)


def run_command_method(ac: dict, project_root: Path) -> tuple[bool, str]:
    cmd = ac.get("command")
    if not cmd or not isinstance(cmd, str):
        return False, "command 필드가 비어 있음."
    workdir = ac.get("workdir") or "."
    expect_exit = ac.get("expect_exit", 0)
    if not isinstance(expect_exit, int):
        expect_exit = 0
    cwd = (project_root / str(workdir)).resolve()
    try:
        proc = subprocess.run(
            cmd,
            shell=True,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=600,
        )
    except subprocess.TimeoutExpired:
        return False, f"명령 timeout (>600s): `{cmd}`"
    actual_exit = proc.returncode
    passed = (actual_exit == expect_exit)
    out_tail = _tail_lines(proc.stdout, EVIDENCE_LINE_LIMIT)
    err_tail = _tail_lines(proc.stderr, EVIDENCE_LINE_LIMIT)
    evidence = (
        f"명령: `{cmd}` / workdir: `{workdir}` / "
        f"exit={actual_exit} (expect {expect_exit}). "
        f"stdout(last {EVIDENCE_LINE_LIMIT}): {out_tail!s} | "
        f"stderr(last {EVIDENCE_LINE_LIMIT}): {err_tail!s}"
    )
    return passed, evidence


def run_file_exists_method(ac: dict, project_root: Path) -> tuple[bool, str]:
    paths = ac.get("paths")
    if not paths or not isinstance(paths, list):
        return False, "paths 필드가 비어 있거나 list 가 아님."
    must_be_nonempty = bool(ac.get("must_be_nonempty", False))
    rows: list[str] = []
    all_ok = True
    for p in paths:
        ap = (project_root / str(p)).resolve()
        exists = ap.exists() and ap.is_file()
        size = ap.stat().st_size if exists else 0
        ok = exists and (not must_be_nonempty or size > 0)
        if not ok:
            all_ok = False
        rows.append(f"`{p}`→exists={exists},size={size}B,pass={ok}")
    evidence = (
        f"project_root=`{project_root}` must_be_nonempty={must_be_nonempty} | "
        + "; ".join(rows)
    )
    return all_ok, evidence


_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def run_manual_method(ac: dict, project_root: Path) -> tuple[bool, str]:
    confirmer = ac.get("manual_confirmer")
    confirm_date = ac.get("confirm_date")
    note = ac.get("note", "")
    missing: list[str] = []
    if not confirmer or not isinstance(confirmer, str) or not confirmer.strip():
        missing.append("manual_confirmer")
    cd_str = str(confirm_date) if confirm_date is not None else ""
    if not cd_str.strip():
        missing.append("confirm_date")
    elif not _ISO_DATE.match(cd_str):
        missing.append(f"confirm_date(ISO 8601 YYYY-MM-DD 형식 아님: {cd_str!r})")
    if missing:
        return False, f"manual 필수 필드 누락/형식오류: {', '.join(missing)}"
    evidence = f"manual_confirmer=`{confirmer}` confirm_date=`{cd_str}`"
    if note:
        evidence += f" note={note!s}"
    return True, evidence


METHOD_DISPATCH = {
    "command": run_command_method,
    "file_exists": run_file_exists_method,
    "manual": run_manual_method,
}


# ---------------------------------------------------------------------------
# Verification.md 렌더링
# ---------------------------------------------------------------------------

def render_verification_md(
    brief_path: Path,
    project_root: Path,
    ac_results: list[dict],
    summary: dict,
    schema_version: str,
) -> str:
    today = datetime.date.today().isoformat()
    overall = "PASS" if summary["fail"] == 0 else "FAIL"
    lines: list[str] = []
    lines.append(f"# NPI_Verification — {brief_path.name}")
    lines.append("")
    lines.append(f"- Brief: `{brief_path}`")
    lines.append(f"- Project root: `{project_root}`")
    lines.append(f"- Generated by: `verification-runner` v{RUNNER_VERSION} (Foundry v0.2.0)")
    lines.append(f"- Run date: {today}")
    lines.append(f"- schema_version: `{schema_version}`")
    lines.append("")
    lines.append("## 요약")
    lines.append(f"- 전체: {summary['total']}")
    lines.append(f"- Pass: {summary['pass']}")
    lines.append(f"- Fail: {summary['fail']}")
    lines.append(f"- 결과: **{overall}**")
    lines.append("")
    lines.append("## AC ↔ Verification 매핑")
    lines.append("")
    lines.append("| AC ID | Statement | Method | Result | Evidence |")
    lines.append("|---|---|---|---|---|")
    for r in ac_results:
        ev = r["evidence"].replace("|", "\\|").replace("\n", " ")
        stmt = str(r["statement"]).replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {r['id']} | {stmt} | `{r['method']}` | {r['result']} | {ev} |")
    lines.append("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

    parser = argparse.ArgumentParser(
        prog="verification-runner",
        description="Foundry v0.2.0 verification runner — Brief 의 structured AC YAML 블록을 실행한다.",
    )
    parser.add_argument("--brief", required=True, help="NPI_Brief.md 경로")
    parser.add_argument("--out", default=None, help="NPI_Verification.md 출력 경로 (기본: Brief 와 같은 디렉토리)")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="경고를 fail 로 격상 (예: factory.yaml 미발견 시 exit 2)",
    )
    args = parser.parse_args(argv)

    brief_path = Path(args.brief).resolve()
    if not brief_path.is_file():
        print(f"[ERROR] Brief 파일 없음: {brief_path}", file=sys.stderr)
        return EXIT_PARSE_ERROR

    project_root, found_root = find_project_root(brief_path.parent)
    if not found_root:
        print(
            "[WARN] factory.yaml 을 찾지 못했습니다. 현재 작업 디렉토리를 project_root 로 사용합니다.",
            file=sys.stderr,
        )
        if args.strict:
            print("[ERROR] --strict: factory.yaml 미발견을 fail 로 격상합니다.", file=sys.stderr)
            return EXIT_PARSE_ERROR

    try:
        brief_text = brief_path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"[ERROR] Brief 읽기 실패: {e}", file=sys.stderr)
        return EXIT_PARSE_ERROR

    yaml_block = extract_ac_yaml_block(brief_text)
    if yaml_block is None:
        print(
            "[ERROR] Brief 에서 structured AC YAML 블록을 찾지 못했습니다. "
            "```yaml ... ``` 펜스 안에 schema_version 과 acceptance_criteria 가 모두 있어야 합니다.",
            file=sys.stderr,
        )
        return EXIT_PARSE_ERROR

    try:
        parsed = parse_yaml_subset(yaml_block)
        validate_schema(parsed)
    except YamlParseError as e:
        print(f"[ERROR] structured AC 파싱/검증 실패: {e}", file=sys.stderr)
        return EXIT_PARSE_ERROR

    ac_results: list[dict] = []
    summary = {"total": 0, "pass": 0, "fail": 0}
    overall_ok = True
    for ac in parsed["acceptance_criteria"]:
        method = ac["method"]
        runner_fn = METHOD_DISPATCH[method]
        try:
            passed, evidence = runner_fn(ac, project_root)
        except Exception as e:
            passed, evidence = False, f"runner 예외: {type(e).__name__}: {e}"
        if passed and (not evidence or not str(evidence).strip()):
            passed = False
            evidence = "[runner 강제 Fail] Pass 행에 Evidence 가 비어 있습니다."
        ac_results.append({
            "id": ac["id"],
            "statement": ac["statement"],
            "method": method,
            "result": "Pass" if passed else "Fail",
            "evidence": evidence,
        })
        summary["total"] += 1
        summary["pass" if passed else "fail"] += 1
        if not passed:
            overall_ok = False

    out_path = (
        Path(args.out).resolve()
        if args.out
        else (brief_path.parent / "NPI_Verification.md")
    )
    md = render_verification_md(
        brief_path, project_root, ac_results, summary, parsed["schema_version"]
    )
    try:
        out_path.write_text(md, encoding="utf-8")
    except OSError as e:
        print(f"[ERROR] Verification 파일 쓰기 실패: {e}", file=sys.stderr)
        return EXIT_PARSE_ERROR

    print(f"[OK] verification 결과: {out_path}")
    print(f"     total={summary['total']} pass={summary['pass']} fail={summary['fail']}")
    return EXIT_PASS if overall_ok else EXIT_FAIL


if __name__ == "__main__":
    raise SystemExit(main())
