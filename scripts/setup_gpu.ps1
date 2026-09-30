param()

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$CpuPython = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
$GpuPython = Join-Path $ProjectRoot ".venv-gpu\Scripts\python.exe"
$FreezePath = Join-Path $ProjectRoot ".build\gpu\requirements-freeze.txt"

if (-not (Test-Path -LiteralPath $CpuPython)) {
    throw "Python 3.12 기반의 기존 .venv가 없습니다. CPU 환경을 먼저 준비하십시오."
}

Push-Location $ProjectRoot
try {
    if (-not (Test-Path -LiteralPath $GpuPython)) {
        & $CpuPython -m venv ".venv-gpu"
        if ($LASTEXITCODE -ne 0) { throw ".venv-gpu 생성에 실패했습니다." }
    }

    & $GpuPython -m pip install --upgrade pip
    if ($LASTEXITCODE -ne 0) { throw "GPU 환경의 pip 갱신에 실패했습니다." }

    & $GpuPython -m pip install -r "requirements-gpu-torch.txt"
    if ($LASTEXITCODE -ne 0) { throw "CUDA PyTorch 설치에 실패했습니다." }

    & $GpuPython -m pip install -r "requirements-gpu.txt"
    if ($LASTEXITCODE -ne 0) { throw "GPU direct dependency 설치에 실패했습니다." }

    New-Item -ItemType Directory -Force (Split-Path -Parent $FreezePath) | Out-Null
    & $GpuPython -m pip freeze --all | Set-Content -LiteralPath $FreezePath -Encoding utf8
    & $GpuPython "scripts/check_gpu_environment.py"
    if ($LASTEXITCODE -ne 0) { throw "GPU 환경 진단에 실패했습니다." }
}
finally {
    Pop-Location
}
