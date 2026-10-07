# Local GPU and Pythia execution environment

This environment is used only for real-model experiments from I06 onward. The existing `.venv` and CPU site build do not depend on this environment or the model cache.

## Pinned environment

| Item | Value |
|---|---|
| Python | 3.12 |
| PyTorch | 2.13.0, CUDA 13.2 wheel |
| NumPy | 2.5.3 |
| Transformers | 5.17.0 |
| GPU gate | At least 6 GiB of available VRAM immediately before execution |
| Required model cache budget | 12 GiB |
| Artifact limit per run | 256 MiB |

`requirements-gpu-torch.txt` uses the official PyTorch `cu132` index, and `requirements-gpu.txt` pins the other direct dependencies. The complete verified dependency set is recorded in `requirements-gpu-lock.txt`; the freeze obtained at each installation is recorded in `.build/gpu/requirements-freeze.txt`.

## Installation and diagnostics

```powershell
powershell -ExecutionPolicy Bypass -File scripts/setup_gpu.ps1
```

Setup creates `.venv-gpu` and checks CUDA matrix multiplication, autograd, determinism, and peak VRAM. It does not download models.

## Preparing the cache

```powershell
.venv-gpu\Scripts\python.exe scripts/prepare_pythia_cache.py --model all
```

The 70M, 160M, and 410M models are downloaded one at a time. All requested revisions are `step143000`, and the immutable commit SHA returned by Hugging Face is recorded in `.build/gpu/cache-manifest.json`. The model and tokenizer use the same repository and resolved SHA.

## Required experiments

```powershell
.venv-gpu\Scripts\python.exe scripts/run_gpu_experiments.py --all
```

The execution order is the 70M smoke test, 160M activations and gradients, the 410M inference comparison, 160M activation patching, and the 160M checkpoint trajectory. The 410M model is used only in I06-08 to compare 160M and 410M activations on eight fixed prompts using CKA and RSA. I07-07 patching replaces only the last-token output of the layer 5 MLP in the 160M model and does not train the model. I08-13 runs `step0`, `step1000`, `step10000`, `step50000`, `step100000`, and `step143000` sequentially in separate processes, so that only one checkpoint is loaded on the GPU at a time. Results remain in `.build/gpu/results`, and selected activations remain in `.build/gpu/activations`. Weights, caches, results, and activations are not stored in Git.

When real-model results are unavailable, the CPU site includes reproduction commands and a notice that local GPU results have not been inserted. Use the following environment variable only when inserting verified local results into the HTML.

```powershell
$env:AI_MATH_GPU_RESULTS = "1"
powershell -ExecutionPolicy Bypass -File scripts/build_site.ps1
```

## Fixed resource limits

| Model | Mode | Maximum sequence length | Maximum peak allocated VRAM | Execution timeout |
|---|---|---:|---:|---:|
| Pythia 70M deduped | Inference | 128 | 2.5 GiB | 120 seconds |
| Pythia 160M deduped | Selected activation gradients | 128 | 4.0 GiB | 180 seconds |
| Six Pythia 160M deduped checkpoints | Checkpoint probe, loaded sequentially | 128 | 4.0 GiB per checkpoint | 180 seconds per checkpoint |
| Pythia 410M deduped | Inference only | 64 | 6.5 GiB | 300 seconds |

Dumping activations for all layers and tokens, full training, loading optimizer state, and running models of 7B parameters or more are outside the execution scope.
