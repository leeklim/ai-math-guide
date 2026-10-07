# N05 execution environment

## Supported setup

The required N05 labs use Windows PowerShell, Python 3.12, and CPU-only PyTorch. They do not use the CUDA toolkit, GPU wheels, Jupyter, browser-based Python, or external models.

Direct dependencies are pinned to the following versions.

| Package | Version | Installation location |
|---|---:|---|
| Python | 3.12 | Existing `.venv` |
| NumPy | 2.5.3 | `requirements-n05.txt` |
| PyTorch CPU | 2.13.0 | `requirements-n05-torch-cpu.txt` |

PyTorch is installed only from the official CPU wheel index. The two requirements files are separate because NumPy is obtained from PyPI, whereas PyTorch is obtained from the CPU-only index.

## Installation

Run the following command from the project root.

```powershell
.\scripts\setup_n05.ps1
```

The script is written so that reinstalling the pinned versions in the existing `.venv` produces the same setup. An ordinary build does not install packages or change the environment.

## Environment diagnostics

```powershell
.\.venv\Scripts\python.exe scripts\check_n05_environment.py
```

The check verifies the Python, PyTorch, and NumPy versions, the CPU build, device, matrix multiplication, autograd, the fixed seed, and PyTorch thread counts. On failure, it returns a nonzero exit code and prints recovery commands.

## Examples and the full build

To rerun only the required examples, use the following command.

```powershell
.\.venv\Scripts\python.exe scripts\run_n05_examples.py
```

Run the full set of checks with:

```powershell
.\scripts\build_site.ps1
```

Example results are stored in `.build/n05/results`. This directory contains generated artifacts and is not tracked in Git. Before inserting code and execution results into the HTML, the site generator compares the source hash in each result file with the current `.py` source.

## Resource budget

| Item | Maximum |
|---|---:|
| Batch size | 2 |
| Sequence length | 32 |
| Model dimension | 64 |
| Transformer layers | 2 |
| Attention heads | 4 |
| Vocabulary size | 256 |
| Total parameters | 250,000 |
| Training steps | 50 |
| DataLoader workers | 0 |
| PyTorch intra-op and inter-op threads | 1 each |
| Hard timeout per example | 10 seconds |
| Hard timeout for all examples | 120 seconds |
| Target total execution time | 30 seconds |

The required examples do not use multiprocessing. The runner rejects examples that exceed the limits before computation starts and records the PyTorch import time separately from the example computation time.
