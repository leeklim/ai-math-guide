#!/usr/bin/env python3
"""Plot exact projected probability masses along two unit directions."""
from __future__ import annotations
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-04-direction"})
    points = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    p = np.array([0.30, 0.20, 0.10, 0.40])
    centered = points - np.sum(p[:, None] * points, axis=0)
    sigma = centered.T @ (p[:, None] * centered)
    fig, axes = plt.subplots(2, 1, figsize=(7.6, 7.2), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    for ax, v, color, name in zip(axes, [np.array([1, 1])/np.sqrt(2), np.array([1, -1])/np.sqrt(2)],
                                 ["#2563EB", "#7C3AED"], ["v = (1, 1)/√2", "v = (1, −1)/√2"]):
        values = np.round(centered @ v, 12)
        support = np.unique(values)
        mass = np.array([np.sum(p[values == value]) for value in support])
        variance = float(v @ sigma @ v)
        ax.set_facecolor("#F8FAFC")
        ax.bar(support, mass, width=0.10, color=color, edgecolor="#334155")
        ax.axvline(0, color="#94A3B8", linestyle=":", linewidth=1.2)
        for value, probability in zip(support, mass):
            ax.text(value, probability + 0.045, f"{probability:.2f}", ha="center", color=color)
        ax.set(xlim=(-1, 1), ylim=(0, 0.9), ylabel="probability mass")
        ax.set_xticks([-1, -0.5, 0, 0.5, 1]); ax.set_yticks([0, 0.5])
        ax.grid(axis="y", color="#CBD5E1", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.set_title(f"{name}:  vᵀΣv = {variance:.3f}", fontsize=15)
        ax.spines[["top", "right"]].set_visible(False)
    axes[-1].set_xlabel("projected centered value t = vᵀ(X − mean)")
    fig.suptitle("Covariance summarizes directional spread\nΣ = [[0.25, 0.10], [0.10, 0.24]]", fontsize=16, fontweight="bold")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
