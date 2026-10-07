#!/usr/bin/env python3
"""Plot the probability-to-loss relation for M00-10."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m00-10-nll"})
    p = np.linspace(0.02, 1.0, 400)
    fig, ax = plt.subplots(figsize=(7.6, 5.3), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(p, -np.log(p), color="#7C3AED", linewidth=2.8, label="loss = -log(p)")
    points = [0.1, 0.9]
    colors = ["#D97706", "#059669"]
    ax.scatter(points, -np.log(points), c=colors, s=85, zorder=5)
    ax.annotate("p = 0.1: loss = 2.303", (0.1, -np.log(0.1)),
                xytext=(70, 26), textcoords="offset points", color="#9A3412",
                arrowprops={"arrowstyle": "-", "color": "#64748B"})
    ax.annotate("p = 0.9: loss = 0.105", (0.9, -np.log(0.9)),
                xytext=(-190, 72), textcoords="offset points", color="#065F46",
                arrowprops={"arrowstyle": "-", "color": "#64748B"})
    ax.set_xlim(0, 1.04)
    ax.set_ylim(-0.12, 4.15)
    ax.set_xticks(np.arange(0, 1.01, 0.2))
    ax.set_xlabel("probability of the correct class p")
    ax.set_ylabel("sample loss")
    ax.set_title("Smaller correct-class probability, larger loss",
                 fontsize=18, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#CBD5E1", linewidth=0.7, alpha=0.8)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
