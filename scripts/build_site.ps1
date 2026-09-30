param()

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $ProjectRoot ".venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $Python)) {
    throw "로컬 가상환경이 없습니다. README의 설치 명령으로 .venv를 먼저 만드십시오."
}

Push-Location $ProjectRoot
try {
    & $Python "scripts/check_n05_environment.py"
    if ($LASTEXITCODE -ne 0) { throw "N05 환경 진단이 실패했습니다." }

    & $Python -m unittest discover -s tests -p "test_*.py"
    if ($LASTEXITCODE -ne 0) { throw "자동 검사 테스트가 실패했습니다." }

    & $Python "scripts/run_n05_examples.py"
    if ($LASTEXITCODE -ne 0) { throw "N05 필수 예제 실행이 실패했습니다." }

    & $Python "scripts/run_i06_examples.py"
    if ($LASTEXITCODE -ne 0) { throw "I06 필수 예제 실행이 실패했습니다." }

    & $Python "scripts/run_i07_examples.py"
    if ($LASTEXITCODE -ne 0) { throw "I07 필수 예제 실행이 실패했습니다." }

    & $Python "scripts/run_i08_examples.py"
    if ($LASTEXITCODE -ne 0) { throw "I08 필수 예제 실행이 실패했습니다." }

    & $Python "scripts/site.py" audit
    if ($LASTEXITCODE -ne 0) { throw "원본 감사가 실패했습니다." }

    & $Python "scripts/site.py" prepare
    if ($LASTEXITCODE -ne 0) { throw "사이트 staging 생성이 실패했습니다." }

    & $Python -m mkdocs build --strict --clean --config-file ".build/mkdocs.yml"
    if ($LASTEXITCODE -ne 0) { throw "MkDocs production build가 실패했습니다." }

    & $Python "scripts/site.py" validate
    if ($LASTEXITCODE -ne 0) { throw "생성 사이트 검증이 실패했습니다." }
}
finally {
    Pop-Location
}
