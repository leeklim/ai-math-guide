"""Shared limits and serialization helpers for the three N05 pilot examples."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import torch


SEED = 20261001
RTOL = 1e-6
ATOL = 1e-7


@dataclass(frozen=True)
class ResourceSpec:
    batch_size: int
    sequence_length: int
    model_dimension: int
    transformer_layers: int
    attention_heads: int
    vocabulary_size: int
    parameter_count: int
    training_steps: int
    dataloader_workers: int = 0
    uses_multiprocessing: bool = False

    def to_dict(self) -> dict[str, int | bool]:
        return asdict(self)


LIMITS = ResourceSpec(
    batch_size=2,
    sequence_length=32,
    model_dimension=64,
    transformer_layers=2,
    attention_heads=4,
    vocabulary_size=256,
    parameter_count=250_000,
    training_steps=50,
)


def configure_runtime() -> None:
    """Apply the required deterministic single-thread CPU settings."""
    torch.set_num_threads(1)
    if torch.get_num_interop_threads() != 1:
        torch.set_num_interop_threads(1)
    torch.manual_seed(SEED)
    torch.use_deterministic_algorithms(True)


def assert_within_limits(spec: ResourceSpec) -> None:
    for field in (
        "batch_size",
        "sequence_length",
        "model_dimension",
        "transformer_layers",
        "attention_heads",
        "vocabulary_size",
        "parameter_count",
        "training_steps",
    ):
        actual = getattr(spec, field)
        maximum = getattr(LIMITS, field)
        if actual > maximum:
            raise ValueError(f"resource limit exceeded: {field}={actual}, maximum={maximum}")
    if spec.dataloader_workers != 0:
        raise ValueError("resource limit exceeded: dataloader_workers must be zero")
    if spec.uses_multiprocessing:
        raise ValueError("resource limit exceeded: multiprocessing is not allowed")


def tensor_values(tensor: torch.Tensor) -> Any:
    return tensor.detach().cpu().tolist()


def tensor_shape(tensor: torch.Tensor) -> list[int]:
    return list(tensor.shape)
