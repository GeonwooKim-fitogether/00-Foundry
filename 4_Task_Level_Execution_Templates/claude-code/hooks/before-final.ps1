<#
.SYNOPSIS
    before-final hook — Foundry v0.2.0 Final Control Point gate.

.DESCRIPTION
    얇은 shim. 실제 검증 로직은 ../skills/verification-runner/run.py 에만 있다.
    본 스크립트는 (1) runner 경로 해석, (2) 인자 forwarding, (3) exit code passthrough 만 한다.
    YAML 파싱 / AC 검증 / NPI_Verification.md 생성 / 결과 해석은 *전부* runner 가 한다.

.PARAMETER Brief
    NPI_Brief.md 의 경로 (필수).

.PARAMETER Out
    NPI_Verification.md 출력 경로 (선택, 기본 = Brief 와 같은 디렉토리).

.PARAMETER Strict
    factory.yaml 미발견을 fail (exit 2) 로 격상.

.EXAMPLE
    .\before-final.ps1 -Brief "3_Domain_Project_Playbooks/foo/T1_NPI_Brief.md"

.NOTES
    Exit codes (runner passthrough):
      0 = 전체 Pass — Final Control Point 진행 가능
      1 = AC 검증 실패 — NPI_Verification.md 의 Fail 행 해결 후 재실행
      2 = schema/parse error 또는 runner 미발견
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$Brief,
    [string]$Out,
    [switch]$Strict
)

$here   = Split-Path -Parent $MyInvocation.MyCommand.Path
$runner = Join-Path $here '..\skills\verification-runner\run.py'

if (-not (Test-Path -LiteralPath $runner)) {
    Write-Host "[before-final] ERROR: runner not found at $runner" -ForegroundColor Red
    Write-Host "[before-final] Hook contains no verification logic. Aborting since runner is missing." -ForegroundColor Red
    exit 2
}

$argList = @('--brief', $Brief)
if ($Out)    { $argList += @('--out', $Out) }
if ($Strict) { $argList += '--strict' }

Write-Host "[before-final] python `"$runner`" $($argList -join ' ')" -ForegroundColor DarkGray
& python $runner @argList
$code = $LASTEXITCODE

# NOTE: Status messages are kept ASCII-only to avoid Windows PowerShell 5.1
# script-load encoding pitfalls (BOM-less UTF-8 vs cp949). Korean explanation
# lives in README.md and comments, not in runtime output.
switch ($code) {
    0 { Write-Host "[before-final] PASS - Final Control Point may proceed." -ForegroundColor Green }
    1 { Write-Host "[before-final] BLOCK - Fail rows in NPI_Verification.md must be resolved, then re-run." -ForegroundColor Yellow }
    2 { Write-Host "[before-final] BLOCK - Inspect the Brief's structured AC YAML block, then re-run." -ForegroundColor Yellow }
    default { Write-Host "[before-final] Unknown exit code: $code" -ForegroundColor Red }
}

exit $code
