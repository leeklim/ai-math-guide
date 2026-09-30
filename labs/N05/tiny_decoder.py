"""Small decoder-only Transformer shared by the cumulative N05 examples."""

from __future__ import annotations

from dataclasses import dataclass
import math

import torch
from torch import nn
import torch.nn.functional as functional


@dataclass(frozen=True)
class TinyDecoderConfig:
    vocabulary_size: int = 16
    model_dimension: int = 4
    feed_forward_dimension: int = 8
    attention_heads: int = 1
    layers: int = 1
    epsilon: float = 1e-6

    @property
    def head_dimension(self) -> int:
        return self.model_dimension // self.attention_heads


class RMSNorm(nn.Module):
    def __init__(self, dimension: int, epsilon: float) -> None:
        super().__init__()
        self.weight = nn.Parameter(torch.ones(dimension))
        self.epsilon = epsilon

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        mean_square = (x**2).mean(dim=-1, keepdim=True)
        return self.weight * x * torch.rsqrt(mean_square + self.epsilon)


def apply_rope(x: torch.Tensor, positions: torch.Tensor) -> torch.Tensor:
    head_dimension = x.shape[-1]
    if head_dimension % 2 != 0:
        raise ValueError("RoPE requires an even head dimension")
    frequencies = 1.0 / (
        10_000
        ** (
            torch.arange(0, head_dimension, 2, device=x.device, dtype=x.dtype)
            / head_dimension
        )
    )
    angles = positions.to(dtype=x.dtype).unsqueeze(1) * frequencies.unsqueeze(0)
    cosine = angles.cos().unsqueeze(0).unsqueeze(0)
    sine = angles.sin().unsqueeze(0).unsqueeze(0)
    even = x[..., 0::2]
    odd = x[..., 1::2]
    rotated = torch.stack(
        (even * cosine - odd * sine, even * sine + odd * cosine), dim=-1
    )
    return rotated.flatten(start_dim=-2)


class CausalSelfAttention(nn.Module):
    def __init__(self, config: TinyDecoderConfig) -> None:
        super().__init__()
        self.config = config
        self.query = nn.Linear(config.model_dimension, config.model_dimension, bias=False)
        self.key = nn.Linear(config.model_dimension, config.model_dimension, bias=False)
        self.value = nn.Linear(config.model_dimension, config.model_dimension, bias=False)
        self.output = nn.Linear(config.model_dimension, config.model_dimension, bias=False)

    def _split_heads(self, x: torch.Tensor) -> torch.Tensor:
        batch, sequence, _ = x.shape
        return x.reshape(
            batch,
            sequence,
            self.config.attention_heads,
            self.config.head_dimension,
        ).transpose(1, 2)

    def forward(
        self,
        x: torch.Tensor,
        past_key_value: tuple[torch.Tensor, torch.Tensor] | None = None,
    ) -> tuple[torch.Tensor, tuple[torch.Tensor, torch.Tensor]]:
        past_length = 0 if past_key_value is None else past_key_value[0].shape[-2]
        positions = torch.arange(
            past_length,
            past_length + x.shape[1],
            device=x.device,
        )
        query = apply_rope(self._split_heads(self.query(x)), positions)
        current_key = apply_rope(self._split_heads(self.key(x)), positions)
        current_value = self._split_heads(self.value(x))
        if past_key_value is None:
            key, value = current_key, current_value
        else:
            key = torch.cat((past_key_value[0], current_key), dim=-2)
            value = torch.cat((past_key_value[1], current_value), dim=-2)

        scores = query @ key.transpose(-2, -1) / math.sqrt(
            self.config.head_dimension
        )
        query_positions = positions.unsqueeze(1)
        key_positions = torch.arange(key.shape[-2], device=x.device).unsqueeze(0)
        future = key_positions > query_positions
        scores = scores.masked_fill(future.unsqueeze(0).unsqueeze(0), float("-inf"))
        probability = torch.softmax(scores, dim=-1)
        attended = probability @ value
        merged = attended.transpose(1, 2).reshape(
            x.shape[0], x.shape[1], self.config.model_dimension
        )
        return self.output(merged), (key, value)


class SwiGLU(nn.Module):
    def __init__(self, config: TinyDecoderConfig) -> None:
        super().__init__()
        self.gate = nn.Linear(
            config.model_dimension, config.feed_forward_dimension, bias=False
        )
        self.up = nn.Linear(
            config.model_dimension, config.feed_forward_dimension, bias=False
        )
        self.down = nn.Linear(
            config.feed_forward_dimension, config.model_dimension, bias=False
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.down(functional.silu(self.gate(x)) * self.up(x))


class DecoderBlock(nn.Module):
    def __init__(self, config: TinyDecoderConfig) -> None:
        super().__init__()
        self.attention_norm = RMSNorm(config.model_dimension, config.epsilon)
        self.attention = CausalSelfAttention(config)
        self.mlp_norm = RMSNorm(config.model_dimension, config.epsilon)
        self.mlp = SwiGLU(config)

    def forward(
        self,
        residual: torch.Tensor,
        past_key_value: tuple[torch.Tensor, torch.Tensor] | None = None,
    ) -> tuple[
        torch.Tensor,
        tuple[torch.Tensor, torch.Tensor],
        dict[str, torch.Tensor],
    ]:
        attention_input = self.attention_norm(residual)
        attention_update, new_key_value = self.attention(
            attention_input, past_key_value
        )
        residual_mid = residual + attention_update
        mlp_input = self.mlp_norm(residual_mid)
        mlp_update = self.mlp(mlp_input)
        residual_out = residual_mid + mlp_update
        trace = {
            "residual_in": residual,
            "attention_input": attention_input,
            "attention_update": attention_update,
            "residual_mid": residual_mid,
            "mlp_input": mlp_input,
            "mlp_update": mlp_update,
            "residual_out": residual_out,
        }
        return residual_out, new_key_value, trace


class TinyDecoderLM(nn.Module):
    def __init__(self, config: TinyDecoderConfig | None = None) -> None:
        super().__init__()
        self.config = config or TinyDecoderConfig()
        self.embedding = nn.Embedding(
            self.config.vocabulary_size, self.config.model_dimension
        )
        self.blocks = nn.ModuleList(
            DecoderBlock(self.config) for _ in range(self.config.layers)
        )
        self.final_norm = RMSNorm(self.config.model_dimension, self.config.epsilon)
        self.unembedding = nn.Linear(
            self.config.model_dimension, self.config.vocabulary_size, bias=False
        )

    def forward(
        self,
        input_ids: torch.Tensor,
        past_key_values: list[tuple[torch.Tensor, torch.Tensor]] | None = None,
    ) -> tuple[
        torch.Tensor,
        list[tuple[torch.Tensor, torch.Tensor]],
        dict[str, torch.Tensor],
    ]:
        residual = self.embedding(input_ids)
        trace: dict[str, torch.Tensor] = {"embedding": residual}
        new_key_values: list[tuple[torch.Tensor, torch.Tensor]] = []
        for index, block in enumerate(self.blocks):
            past = None if past_key_values is None else past_key_values[index]
            residual, key_value, block_trace = block(residual, past)
            new_key_values.append(key_value)
            trace.update(
                {f"block_{index}_{name}": value for name, value in block_trace.items()}
            )
        normalized = self.final_norm(residual)
        logits = self.unembedding(normalized)
        trace["final_norm"] = normalized
        trace["logits"] = logits
        return logits, new_key_values, trace


def parameter_count(model: nn.Module) -> int:
    return sum(parameter.numel() for parameter in model.parameters())

