#!/usr/bin/env python3
"""Plot interval area versus one-point width for M04-03."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-03-pdf"})
    x = np.linspace(0.2, 0.5, 101)
    fig, ax = plt.subplots(figsize=(7.6, 5.3), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot([-0.12, 0], [0, 0], color="#7C3AED", linewidth=3)
    ax.plot([0, 1], [1, 1], color="#7C3AED", linewidth=3)
    ax.plot([1, 1.12], [0, 0], color="#7C3AED", linewidth=3)
    ax.fill_between(x, 0, 1, color="#059669", alpha=0.22, hatch="///",
                    edgecolor="#059669", linewidth=0.8)
    ax.vlines([0.2, 0.5], 0, 1, color="#059669", linewidth=1.7)
    ax.scatter([0.8], [1], color="#D97706", s=90, zorder=5)
    ax.annotate("Area = 0.3 × 1 = 0.3", (0.35, 0.5), xytext=(0.39, 1.27),
                ha="center", color="#065F46",
                arrowprops={"arrowstyle": "-", "color": "#64748B"})
    ax.annotate("One point: width 0\nP(X = 0.8) = 0", (0.8, 1), xytext=(0.62, 0.35),
                color="#9A3412", linespacing=1.6,
                arrowprops={"arrowstyle": "-", "color": "#64748B"})
    ax.set_xlim(-0.12, 1.12)
    ax.set_ylim(-0.1, 1.48)
    ax.set_xticks([0, 0.2, 0.5, 0.8, 1])
    ax.set_yticks([0, 1])
    ax.set_xlabel("value x")
    ax.set_ylabel("density f_X(x)")
    ax.set_title("Probability is area, not density height", fontsize=18, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#CBD5E1", linewidth=0.7)
    ax.set_axisbelow(True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
