param([switch]$RunExamples)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $ProjectRoot ".venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $Python)) {
    throw "로컬 가상환경이 없습니다. README의 설치 명령으로 .venv를 먼저 만드십시오."
}

Push-Location $ProjectRoot
try {
    & $Python "scripts/concepts.py" check-translations --require-verified
    if ($LASTEXITCODE -ne 0) { throw "한영 전체 검토가 완료되지 않았습니다." }

    if ($env:AI_MATH_GPU_RESULTS -eq "1") {
        throw "공개용 한영 빌드에는 로컬 GPU 결과를 포함할 수 없습니다. AI_MATH_GPU_RESULTS를 0으로 설정하십시오."
    }

    & $Python "scripts/check_n05_environment.py"
    if ($LASTEXITCODE -ne 0) { throw "N05 환경 진단이 실패했습니다." }

    & $Python -m unittest discover -s tests -p "test_*.py"
    if ($LASTEXITCODE -ne 0) { throw "자동 검사 테스트가 실패했습니다." }

    if ($RunExamples) {
        foreach ($Runner in @("n05", "i06", "i07", "i08")) {
            & $Python "scripts/run_${Runner}_examples.py"
            if ($LASTEXITCODE -ne 0) { throw "$Runner 필수 예제 실행이 실패했습니다." }
        }
    }

    & $Python "scripts/figures.py" check
    if ($LASTEXITCODE -ne 0) { throw "그림 감사가 실패했습니다." }

    & $Python "scripts/concepts.py" check --require-explanations
    if ($LASTEXITCODE -ne 0) { throw "개념별 개정 대장 검사가 실패했습니다." }

    & $Python "scripts/concepts.py" check --require-verified
    if ($LASTEXITCODE -ne 0) { throw "개념별 완료 검사가 실패했습니다." }

    foreach ($Language in @("ko", "en")) {
        & $Python "scripts/site.py" audit --lang $Language
        if ($LASTEXITCODE -ne 0) { throw "$Language 원본 감사가 실패했습니다." }

        & $Python "scripts/site.py" prepare --lang $Language --isolated
        if ($LASTEXITCODE -ne 0) { throw "$Language staging 생성이 실패했습니다. 결과가 없거나 오래되었다면 -RunExamples로 다시 실행하십시오." }

        & $Python -m mkdocs build --strict --clean --config-file ".build/$Language/mkdocs.yml"
        if ($LASTEXITCODE -ne 0) { throw "$Language strict build가 실패했습니다." }
    }

    & $Python "scripts/site.py" merge
    if ($LASTEXITCODE -ne 0) { throw "한영 병합 사이트 검증이 실패했습니다." }

    foreach ($Language in @("ko", "en")) {
        & node "tests/analytics_runtime.cjs" ".build/$Language/site/index.html"
        if ($LASTEXITCODE -ne 0) { throw "$Language GA4 제거·Cloudflare 공개 주소 제한 검사가 실패했습니다." }
    }
}
finally {
    Pop-Location
}
