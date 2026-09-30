#!/usr/bin/env python3
"""Check the pinned CPU-only environment used by N05 examples."""

from __future__ import annotations

import platform
import sys
import time


EXPECTED_PYTHON = (3, 12)
EXPECTED_TORCH = "2.13.0"
EXPECTED_NUMPY = "2.5.3"
SETUP_COMMAND = ".\\scripts\\setup_n05.ps1"


def fail(message: str) -> int:
    print(f"N05 environment check failed: {message}", file=sys.stderr)
    print(f"Repair command: {SETUP_COMMAND}", file=sys.stderr)
    return 1


def main() -> int:
    if sys.version_info[:2] != EXPECTED_PYTHON:
        return fail(
            f"Python {EXPECTED_PYTHON[0]}.{EXPECTED_PYTHON[1]} is required; "
            f"found {platform.python_version()}."
        )

    import_started = time.perf_counter()
    try:
        import numpy as np
        import torch
    except ImportError as error:
        return fail(f"a required package cannot be imported: {error}")
    import_seconds = time.perf_counter() - import_started

    if np.__version__ != EXPECTED_NUMPY:
        return fail(f"NumPy {EXPECTED_NUMPY} is required; found {np.__version__}.")
    torch_version = torch.__version__.split("+")[0]
    if torch_version != EXPECTED_TORCH:
        return fail(f"PyTorch {EXPECTED_TORCH} is required; found {torch.__version__}.")
    if torch.version.cuda is not None:
        return fail(
            "the installed PyTorch build exposes CUDA; install the pinned CPU wheel instead."
        )

    torch.set_num_threads(1)
    if torch.get_num_interop_threads() != 1:
        try:
            torch.set_num_interop_threads(1)
        except RuntimeError as error:
            return fail(f"cannot set PyTorch inter-op threads to one: {error}")

    left = torch.tensor([[1.0, 2.0]], dtype=torch.float32)
    right = torch.tensor([[3.0], [4.0]], dtype=torch.float32)
    product = left @ right
    torch.testing.assert_close(product, torch.tensor([[11.0]]), rtol=1e-6, atol=1e-7)

    x = torch.tensor([2.0], dtype=torch.float32, requires_grad=True)
    loss = (x * x).sum()
    loss.backward()
    torch.testing.assert_close(x.grad, torch.tensor([4.0]), rtol=1e-6, atol=1e-7)

    torch.manual_seed(20261001)
    first = torch.rand(4)
    torch.manual_seed(20261001)
    second = torch.rand(4)
    torch.testing.assert_close(first, second, rtol=0.0, atol=0.0)

    print(f"Python: {platform.python_version()}")
    print(f"PyTorch: {torch.__version__}")
    print(f"NumPy: {np.__version__}")
    print("Device: cpu")
    print("PyTorch build: CPU-only")
    print(f"PyTorch intra-op threads: {torch.get_num_threads()}")
    print(f"PyTorch inter-op threads: {torch.get_num_interop_threads()}")
    print(f"Package import seconds: {import_seconds:.6f}")
    print("Tensor and matrix multiplication: passed")
    print("Autograd: passed")
    print("Deterministic seed: passed")
    print("N05 lab readiness: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
