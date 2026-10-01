#!/usr/bin/env python3
"""Generate the evidence timeline used in I08-09."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x: np.ndarray, center: float, slope: float) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-slope * (x - center)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 12,
            "svg.fonttype": "none",
            "svg.hashsalt": "mmi-i08-09",
        }
    )
    step = np.linspace(0, 100, 300)
    curves = [
        ("Formation", sigmoid(step, 32, 0.11), "#64748B", "-"),
        ("Recoverability", sigmoid(step, 45, 0.13), "#2563EB", "-"),
        ("Use", sigmoid(step, 63, 0.15), "#DC2626", "--"),
        ("Behavior", sigmoid(step, 72, 0.12), "#059669", ":"),
    ]
    fig, ax = plt.subplots(figsize=(8.0, 4.6), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    for label, values, color, linestyle in curves:
        ax.plot(step, values, label=label, color=color, linewidth=2.2, linestyle=linestyle)
    ax.axhline(0.75, color="#475569", linewidth=1, linestyle=(0, (4, 4)))
    ax.text(2, 0.775, "measurement threshold", color="#475569", fontsize=10.5)
    for x, label, color in ((45, "first observed\nrecoverability", "#2563EB"), (63, "first observed\nuse", "#DC2626")):
        ax.axvline(x, ymin=0, ymax=0.75, color=color, linewidth=0.9, alpha=0.55)
        ax.text(x + 1.5, 0.08, label, color=color, fontsize=10)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1.04)
    ax.set_xlabel("training step")
    ax.set_ylabel("normalized evidence")
    ax.legend(frameon=False, loc="lower right")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#CBD5E1", linewidth=0.6, alpha=0.65)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
