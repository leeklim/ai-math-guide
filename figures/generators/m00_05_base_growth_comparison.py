#!/usr/bin/env python3
"""Plot increasing and decreasing exponential bases for M00-05."""

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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m00-05-base-growth"})
    x = np.linspace(-3, 3, 361)
    fig, ax = plt.subplots(figsize=(7.6, 5.4), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(x, np.power(2.0, x), color="#2563EB", linewidth=2.8,
            label="y = 2^x: increasing")
    ax.plot(x, np.power(0.5, x), color="#D97706", linewidth=2.8,
            linestyle="--", label="y = (1/2)^x: decreasing")
    ax.axhline(0, color="#64748B", linewidth=1.2)
    ax.axvline(0, color="#94A3B8", linewidth=1.2)
    ax.scatter([0], [1], color="#059669", s=85, zorder=5)
    ax.annotate("shared (0, 1)", (0, 1), xytext=(76, 80),
                textcoords="offset points", ha="center", color="#065F46",
                arrowprops={"arrowstyle": "-", "color": "#64748B"})
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-0.35, 8.8)
    ax.set_xticks(np.arange(-3, 4))
    ax.set_yticks([0, 1, 2, 4, 6, 8])
    ax.set_xlabel("input x")
    ax.set_ylabel("output")
    ax.set_title("Opposite directions, positive outputs", fontsize=18, fontweight="bold")
    ax.legend(frameon=True, loc="upper center", fontsize=13,
              facecolor="#F8FAFC", edgecolor="#F8FAFC", framealpha=1)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#CBD5E1", linewidth=0.7, alpha=0.8)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
