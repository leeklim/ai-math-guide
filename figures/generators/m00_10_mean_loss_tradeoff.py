#!/usr/bin/env python3
"""Plot a mean-loss decrease despite one sample-loss increase for M00-10."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m00-10-mean"})
    losses = [np.array([2.0, 2.0]), np.array([3.0, 0.5])]
    fig, axes = plt.subplots(1, 2, figsize=(8.0, 5.3), sharey=True,
                             constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    for ax, values, label in zip(axes, losses, ["Before", "After"]):
        ax.set_facecolor("#F8FAFC")
        ax.bar([1, 2], values, width=0.55, color=["#DBEAFE", "#F3E8FF"],
               edgecolor=["#2563EB", "#7C3AED"], linewidth=2, zorder=3)
        mean = float(np.mean(values))
        ax.axhline(mean, color="#059669", linestyle="--", linewidth=2.4,
                   zorder=4)
        ax.set_title(f"{label}: mean = {mean:g}", fontsize=17, fontweight="bold")
        ax.set_ylim(0, 3.8)
        ax.set_xlim(0.5, 2.5)
        ax.set_xticks([1, 2], ["sample 1", "sample 2"])
        ax.set_xlabel("sample")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", color="#CBD5E1", linewidth=0.7, alpha=0.8, zorder=0)
        for i, value in enumerate(values, 1):
            ax.annotate(f"{value:g}", (i, value), xytext=(0, 12),
                        textcoords="offset points", ha="center", fontsize=15,
                        bbox={"facecolor": "#F8FAFC", "edgecolor": "none", "pad": 2})
    axes[0].set_ylabel("sample loss")
    fig.suptitle("Sample 1 worsens while the mean falls", fontsize=19,
                 fontweight="bold")
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
