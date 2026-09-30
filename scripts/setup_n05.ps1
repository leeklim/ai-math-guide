param()

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $ProjectRoot ".venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $Python)) {
    throw "기존 .venv를 찾지 못했습니다. 먼저 README의 기본 환경 설치 절차를 실행하십시오."
}

Push-Location $ProjectRoot
try {
    & $Python -m pip install -r "requirements-n05.txt"
    if ($LASTEXITCODE -ne 0) { throw "NumPy 설치가 실패했습니다." }

    & $Python -m pip install -r "requirements-n05-torch-cpu.txt"
    if ($LASTEXITCODE -ne 0) { throw "CPU 전용 PyTorch 설치가 실패했습니다." }

    & $Python "scripts/check_n05_environment.py"
    if ($LASTEXITCODE -ne 0) { throw "N05 환경 진단이 실패했습니다." }
}
finally {
    Pop-Location
}
