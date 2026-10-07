param(
    [int]$Port = 8000,
    [switch]$SkipBuild
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $ProjectRoot ".venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $Python)) {
    throw "로컬 가상환경이 없습니다. README의 설치 명령으로 .venv를 먼저 만드십시오."
}

Push-Location $ProjectRoot
try {
    if (-not $SkipBuild) {
        & (Join-Path $PSScriptRoot "build_site.ps1")
        if ($LASTEXITCODE -ne 0) { throw "preview 전 build가 실패했습니다." }
    }

    & $Python "scripts/site.py" serve --port $Port
    if ($LASTEXITCODE -ne 0) { throw "한영 로컬 preview가 실패했습니다." }
}
finally {
    Pop-Location
}
