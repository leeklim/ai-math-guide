#!/usr/bin/env python3
"""Compare sum variance for aligned and opposing unit deviations."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-04-sum"})
    x = np.array([-1, 1])
    fig, axes = plt.subplots(2, 2, figsize=(8.4, 7.2), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    for col, y, name, color in [(0, x, "Aligned: Y = X", "#2563EB"),
                                (1, -x, "Opposing: Y = -X", "#7C3AED")]:
        ax = axes[0, col]
        ax.set_facecolor("#F8FAFC")
        ax.scatter(x, y, s=140, color=color, zorder=5)
        ax.set(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), xlabel="X", ylabel="Y")
        ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
        ax.set_aspect("equal", adjustable="box")
        ax.axhline(0, color="#94A3B8", linewidth=0.9)
        ax.axvline(0, color="#94A3B8", linewidth=0.9)
        ax.grid(color="#E2E8F0", linewidth=0.7)
        ax.set_title(name, color=color, fontsize=15)
        ax = axes[1, col]
        ax.set_facecolor("#F8FAFC")
        s, counts = np.unique(x + y, return_counts=True)
        ax.bar(s, counts / 2, width=0.42, color=color, edgecolor="#334155")
        var_sum = float(np.var(x + y))
        covariance = float(np.mean(x * y))
        ax.set(xlim=(-2.7, 2.7), ylim=(0, 1.22), xlabel="sum X + Y", ylabel="probability mass")
        ax.set_xticks([-2, 0, 2]); ax.set_yticks([0, 0.5, 1])
        ax.grid(axis="y", color="#E2E8F0", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.set_title(f"Cov = {covariance:g}; sum variance = {var_sum:g}", fontsize=14)
        for value, count in zip(s, counts):
            ax.text(value, count / 2 + 0.04, f"{count / 2:g}", ha="center", color=color)
    fig.suptitle("Same marginal variances (1, 1), different sum spread\nEach joint outcome has probability 1/2", fontsize=17, fontweight="bold")
    for ax in axes.flat:
        ax.spines[["top", "right"]].set_visible(False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
