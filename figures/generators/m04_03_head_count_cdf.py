#!/usr/bin/env python3
"""Plot the right-continuous head-count CDF for M04-03."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-03-cdf"})
    x = np.array([-0.65, 0, 1, 2, 2.65])
    cdf = np.array([0, 0.25, 0.75, 1, 1])
    fig, ax = plt.subplots(figsize=(7.6, 5.3), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    for a, b, level in zip(x[:-1], x[1:], cdf[:-1]):
        ax.plot([a, b], [level, level], color="#7C3AED", linewidth=3)
    ax.scatter([0, 1, 2], [0, 0.25, 0.75], s=90, facecolors="#F8FAFC",
               edgecolors="#7C3AED", linewidths=2, zorder=4)
    ax.scatter([0, 1, 2], [0.25, 0.75, 1], s=90, color="#7C3AED", zorder=5)
    ax.scatter([0.5], [0.25], s=100, color="#D97706", zorder=6)
    ax.annotate("F_X(0.5) = 0.25", (0.5, 0.25), xytext=(0.3, 0.49),
                color="#9A3412", arrowprops={"arrowstyle": "-", "color": "#64748B"})
    ax.set_xlim(-0.65, 2.65)
    ax.set_ylim(-0.07, 1.13)
    ax.set_xticks([0, 0.5, 1, 2])
    ax.set_yticks([0, 0.25, 0.75, 1])
    ax.set_xlabel("threshold x")
    ax.set_ylabel("F_X(x) = P(X ≤ x)")
    ax.set_title("The threshold accumulates included mass", fontsize=18, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#CBD5E1", linewidth=0.7)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
