#!/usr/bin/env python3
"""Compare value shifts and scales at fixed probability masses."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-04-affine"})
    values = np.array([0, 1, 2])
    p = np.array([0.25, 0.50, 0.25])
    fig, ax = plt.subplots(figsize=(7.8, 5.5), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    for row, x, color, label in [(2, values, "#2563EB", "X: mean 1, variance 0.5"),
                                 (1, values + 3, "#7C3AED", "X+3: mean 4, variance 0.5"),
                                 (0, 2 * values, "#059669", "2X: mean 2, variance 2")]:
        mean = float(np.dot(p, x))
        ax.hlines(row, -0.5, 5.5, color="#CBD5E1", linewidth=1)
        ax.scatter(x, np.full(3, row), s=1000 * p, color=color, zorder=4)
        ax.scatter([mean], [row - 0.20], s=90, marker="D", color="#D97706", zorder=5)
        ax.text(-0.45, row + 0.35, label, color=color, fontsize=14)
    ax.set_xlim(-0.6, 5.7)
    ax.set_ylim(-0.55, 2.75)
    ax.set_xticks(np.arange(0, 6))
    ax.set_yticks([])
    ax.set_xlabel("possible value (same horizontal scale in all rows)")
    ax.set_title("Shifts preserve distances; scales multiply distances", fontsize=17, fontweight="bold")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.grid(axis="x", color="#E2E8F0", linewidth=0.8)
    ax.text(0, -0.5, "Circle area: probability; diamond: mean", fontsize=13, color="#475569")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
