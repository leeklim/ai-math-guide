#!/usr/bin/env python3
"""Plot Bernoulli variance against its success parameter."""
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
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 26,
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-05-bernoulli-var"})
    p = np.linspace(0, 1, 301)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(p, p * (1 - p), color="#7C3AED", linewidth=3)
    ax.scatter([0, 0.5, 1], [0, 0.25, 0], color="#7C3AED", s=85, zorder=5)
    ax.scatter([0.7], [0.21], color="#D97706", s=95, zorder=6)
    ax.annotate("p = 0.7\nVar(X) = 0.21", (0.7, 0.21), xytext=(0.42, 0.07),
                color="#9A3412", arrowprops={"arrowstyle": "-", "color": "#64748B"}, fontsize=26)
    ax.text(0.5, 0.275, "maximum\np = 0.5", ha="center", color="#5B21B6", fontsize=24)
    ax.set(xlim=(-0.04, 1.04), ylim=(-0.02, 0.31), xlabel="success probability p", ylabel="Var(X) = p(1 − p)")
    ax.set_xticks([0, 0.5, 0.7, 1]); ax.set_yticks([0, 0.21, 0.25])
    ax.grid(color="#CBD5E1", linewidth=0.7)
    ax.set_title("Bernoulli variance\nConstant at p = 0 or 1", fontsize=26, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
