from __future__ import annotations

import numpy as np
import torch
from torch import nn

from labs.I06.common import SEED, emit


class SparseAutoencoder(nn.Module):
    def __init__(self, input_dim: int, latent_dim: int) -> None:
        super().__init__()
        self.encoder = nn.Linear(input_dim, latent_dim)
        self.decoder = nn.Linear(latent_dim, input_dim)

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        features = torch.relu(self.encoder(x))
        return self.decoder(features), features


def run() -> dict[str, object]:
    torch.manual_seed(SEED)
    rng = np.random.default_rng(SEED)
    true_dictionary = rng.normal(size=(10, 6)).astype(np.float32)
    true_dictionary /= np.linalg.norm(true_dictionary, axis=1, keepdims=True)
    codes = np.zeros((128, 10), dtype=np.float32)
    for row in codes:
        indices = rng.choice(10, size=2, replace=False)
        row[indices] = rng.uniform(0.5, 1.5, size=2)
    inputs = torch.from_numpy(codes @ true_dictionary)
    model = SparseAutoencoder(input_dim=6, latent_dim=12)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.03)
    for _ in range(50):
        reconstruction, features = model(inputs)
        loss = torch.mean((inputs - reconstruction) ** 2) + 0.02 * torch.mean(features)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    with torch.no_grad():
        reconstruction, features = model(inputs)
        dead = torch.sum(torch.max(features, dim=0).values <= 1e-6)
        return {
            "parameter_count": sum(parameter.numel() for parameter in model.parameters()),
            "training_steps": 50,
            "reconstruction_mse": float(torch.mean((inputs - reconstruction) ** 2)),
            "mean_l0": float(torch.mean(torch.sum(features > 1e-3, dim=1).float())),
            "dead_features": int(dead),
        }


if __name__ == "__main__":
    emit(run())
