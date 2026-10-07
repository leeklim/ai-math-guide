#!/usr/bin/env python3
"""Plot signed weighted products in the binary joint example."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-04-cov-products"})
    x = np.array([0, 0, 1, 1], dtype=float)
    y = np.array([0, 1, 0, 1], dtype=float)
    p = np.array([0.30, 0.20, 0.10, 0.40])
    dx, dy = x - np.dot(p, x), y - np.dot(p, y)
    contributions = p * dx * dy
    fig, ax = plt.subplots(figsize=(7.6, 6.0), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    for left, right, bottom, top, color in [(-0.95, 0, -0.95, 0, "#D1FAE5"),
                                            (0, 0.95, 0, 0.8, "#D1FAE5"),
                                            (-0.95, 0, 0, 0.8, "#FFEDD5"),
                                            (0, 0.95, -0.95, 0, "#FFEDD5")]:
        ax.fill([left, right, right, left], [bottom, bottom, top, top], color=color, zorder=0)
    ax.axhline(0, color="#64748B", linewidth=1.2)
    ax.axvline(0, color="#64748B", linewidth=1.2)
    ax.scatter(dx, dy, s=1500 * p, color="#2563EB", edgecolor="#1E3A8A", zorder=5)
    for xp, yp, mass, term, offset in zip(dx, dy, p, contributions,
                                         [(-66, -48), (-74, 26), (24, -48), (24, 26)]):
        ax.annotate(f"p={mass:.2f}\nterm={term:+.2f}", (xp, yp), xytext=offset,
                    textcoords="offset points", color="#334155", linespacing=1.5, fontsize=13)
    ax.set(xlim=(-0.95, 0.95), ylim=(-0.95, 0.80),
           xlabel="centered X: x − 0.50", ylabel="centered Y: y − 0.60")
    ax.set_xticks([-0.5, 0, 0.5]); ax.set_yticks([-0.6, 0, 0.4])
    ax.grid(color="#CBD5E1", linewidth=0.7)
    ax.set_title("Same signs add; opposite signs subtract\nCov = +0.09 −0.04 −0.03 +0.08 = 0.10", fontsize=17, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
