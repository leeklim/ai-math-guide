# N05 실행 환경

## 지원 범위

N05 필수 실습은 Windows PowerShell, Python 3.12와 CPU 전용 PyTorch를 기준으로 한다. CUDA toolkit, GPU wheel, Jupyter, 브라우저 Python과 외부 모델은 사용하지 않는다.

직접 사용하는 패키지는 다음 버전으로 고정한다.

| 패키지 | 버전 | 설치 위치 |
|---|---:|---|
| Python | 3.12 | 기존 `.venv` |
| NumPy | 2.5.3 | `requirements-n05.txt` |
| PyTorch CPU | 2.13.0 | `requirements-n05-torch-cpu.txt` |

PyTorch는 공식 CPU wheel index에서만 설치한다. 두 requirements 파일을 따로 둔 이유는 NumPy는 PyPI에서 받고 PyTorch는 CPU 전용 index에서 받기 위해서다.

## 설치

프로젝트 루트에서 다음 명령을 실행한다.

```powershell
.\scripts\setup_n05.ps1
```

script는 기존 `.venv`에 고정 버전을 다시 설치해도 같은 상태가 되도록 작성됐다. 일반 build는 패키지를 설치하거나 환경을 바꾸지 않는다.

## 환경 진단

```powershell
.\.venv\Scripts\python.exe scripts\check_n05_environment.py
```

진단은 Python·PyTorch·NumPy 버전, CPU build, device, 행렬곱, autograd, 고정 seed와 PyTorch thread 수를 확인한다. 실패하면 0이 아닌 종료 코드와 복구 명령을 출력한다.

## 예제와 전체 build

필수 예제만 다시 실행하려면 다음 명령을 사용한다.

```powershell
.\.venv\Scripts\python.exe scripts\run_n05_examples.py
```

전체 검사는 다음 명령으로 실행한다.

```powershell
.\scripts\build_site.ps1
```

예제 결과는 `.build/n05/results`에 저장된다. 이 디렉터리는 생성물이며 Git에 추적하지 않는다. 사이트 생성기는 결과 파일의 source hash를 현재 `.py` 원본과 대조한 뒤 코드와 실행 결과를 HTML에 넣는다.

## 자원 예산

| 항목 | 상한 |
|---|---:|
| batch size | 2 |
| sequence length | 32 |
| model dimension | 64 |
| Transformer layer | 2 |
| attention head | 4 |
| vocabulary size | 256 |
| 전체 parameter | 250,000 |
| 학습 step | 50 |
| DataLoader worker | 0 |
| PyTorch intra-op·inter-op thread | 각각 1 |
| 개별 예제 hard timeout | 10초 |
| 전체 예제 hard timeout | 120초 |
| 전체 실행시간 목표 | 30초 |

필수 예제는 multiprocessing을 사용하지 않는다. 실행기는 상한을 넘은 예제를 계산하기 전에 실패시키고, PyTorch import 시간과 예제 계산시간을 나누어 기록한다.
