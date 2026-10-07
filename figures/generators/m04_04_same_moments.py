#!/usr/bin/env python3
"""Compare distinct distributions with the same mean and variance."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-04-moments"})
    fig, axes = plt.subplots(2, 1, figsize=(7.6, 7.0), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    distributions = [(np.array([-1, 1]), np.array([0.5, 0.5]), "#2563EB", "Two possible values"),
                     (np.array([-np.sqrt(2), 0, np.sqrt(2)]), np.array([0.25, 0.5, 0.25]), "#7C3AED", "Three possible values")]
    for ax, (x, p, color, title) in zip(axes, distributions):
        ax.set_facecolor("#F8FAFC")
        ax.bar(x, p, width=0.18, color=color, edgecolor="#334155")
        for value, mass in zip(x, p):
            ax.text(value, mass + 0.035, f"{mass:.2f}", ha="center", color=color)
        ax.axvline(0, color="#94A3B8", linestyle=":", linewidth=1.1)
        ax.set(xlim=(-2, 2), ylim=(0, 0.73), ylabel="probability mass")
        ax.set_xticks([-np.sqrt(2), -1, 0, 1, np.sqrt(2)], ["−√2", "−1", "0", "1", "√2"])
        ax.set_yticks([0, 0.25, 0.5])
        ax.grid(axis="y", color="#CBD5E1", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.set_title(title + ": mean = 0, variance = 1", fontsize=14)
        ax.spines[["top", "right"]].set_visible(False)
    axes[-1].set_xlabel("value")
    fig.suptitle("Equal first and second moments do not fix the distribution", fontsize=16, fontweight="bold")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
