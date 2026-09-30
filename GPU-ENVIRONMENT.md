# 로컬 GPU·Pythia 실행 환경

이 환경은 I06 이후의 실제 모델 실험에만 사용한다. 기존 `.venv`와 CPU 사이트 빌드는 이 환경이나 모델 cache에 의존하지 않는다.

## 고정 환경

| 항목 | 값 |
|---|---|
| Python | 3.12 |
| PyTorch | 2.13.0, CUDA 13.2 wheel |
| NumPy | 2.5.3 |
| Transformers | 5.17.0 |
| GPU gate | 실행 직전 가용 VRAM 6 GiB 이상 |
| 필수 모델 cache 예산 | 12 GiB |
| 실행별 artifact 상한 | 256 MiB |

`requirements-gpu-torch.txt`는 PyTorch 공식 `cu132` index를 사용하고, `requirements-gpu.txt`는 나머지 direct dependency를 고정한다. 검증한 전체 dependency는 `requirements-gpu-lock.txt`, 설치할 때마다 얻은 freeze는 `.build/gpu/requirements-freeze.txt`에 기록한다.

## 설치와 진단

```powershell
powershell -ExecutionPolicy Bypass -File scripts/setup_gpu.ps1
```

setup은 `.venv-gpu`를 만들고 CUDA matmul·autograd·결정성·peak VRAM을 검사한다. 모델은 다운로드하지 않는다.

## cache 준비

```powershell
.venv-gpu\Scripts\python.exe scripts/prepare_pythia_cache.py --model all
```

70M, 160M, 410M을 한 번에 하나씩 내려받는다. 요청 revision은 모두 `step143000`이며, Hugging Face가 반환한 immutable commit SHA를 `.build/gpu/cache-manifest.json`에 기록한다. model과 tokenizer는 같은 repository와 resolved SHA를 사용한다.

## 필수 실험

```powershell
.venv-gpu\Scripts\python.exe scripts/run_gpu_experiments.py --all
```

실행 순서는 70M smoke, 160M activation·gradient, 410M inference 비교, 160M activation patching이다. 410M은 I06-08에서 고정 prompt 8개의 160M·410M activation을 CKA와 RSA로 비교할 때만 사용한다. I07-07 patching은 160M layer 5 MLP의 마지막-token 출력만 바꾸며 모델을 학습하지 않는다. 결과는 `.build/gpu/results`, 선택 activation은 `.build/gpu/activations`에만 남는다. weight, cache, 결과와 activation은 Git에 넣지 않는다.

CPU 사이트는 실제 결과가 없으면 재현 명령과 `로컬 GPU 결과가 삽입되지 않음` 표시를 넣는다. 검증된 로컬 결과를 HTML에 넣을 때만 다음 환경변수를 사용한다.

```powershell
$env:AI_MATH_GPU_RESULTS = "1"
powershell -ExecutionPolicy Bypass -File scripts/build_site.ps1
```

## 고정 자원 상한

| 모델 | mode | sequence 상한 | peak allocated VRAM 상한 | 실행 timeout |
|---|---|---:|---:|---:|
| Pythia 70M deduped | inference | 128 | 2.5 GiB | 120초 |
| Pythia 160M deduped | selected activation gradient | 128 | 4.0 GiB | 180초 |
| Pythia 410M deduped | inference only | 64 | 6.5 GiB | 300초 |

전체 layer·token activation dump, full training, optimizer state 적재와 7B 이상 모델은 실행 범위가 아니다.
