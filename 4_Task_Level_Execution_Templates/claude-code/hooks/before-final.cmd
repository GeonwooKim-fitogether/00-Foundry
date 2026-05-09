@echo off
REM ============================================================================
REM  before-final.cmd - Foundry v0.2.0 Final Control Point gate (Windows cmd).
REM  Thin wrapper. Real logic lives in before-final.ps1 -> ../skills/verification-runner/run.py.
REM
REM  Usage:
REM    before-final.cmd ^<brief_path^> [-Strict] [-Out ^<out_path^>]
REM
REM  Exit codes (passed through from PowerShell shim):
REM    0 = all AC pass
REM    1 = AC verification failed
REM    2 = schema/parse error or PowerShell shim missing
REM
REM  NOTE: This file is intentionally ASCII-only. cmd.exe parses .cmd files in
REM  the system ANSI code page; non-ASCII bytes (Korean, BOM, etc.) corrupt
REM  parsing on Windows PowerShell 5.1 / cmd.exe with cp949 default.
REM ============================================================================
setlocal

set "HERE=%~dp0"
set "PS_SHIM=%HERE%before-final.ps1"

if not exist "%PS_SHIM%" (
    echo [before-final] ERROR: PowerShell shim not found: "%PS_SHIM%" 1>&2
    exit /b 2
)

if "%~1"=="" (
    echo [before-final] usage: before-final.cmd ^<brief_path^> [-Strict] [-Out ^<out_path^>] 1>&2
    exit /b 2
)

set "BRIEF=%~1"
shift

powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "%PS_SHIM%" -Brief "%BRIEF%" %1 %2 %3 %4 %5 %6
exit /b %ERRORLEVEL%
