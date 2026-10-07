#!/usr/bin/env python3
"""Plot the average slopes in M01-01 for f(x)=x squared from x=1."""

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
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 16,
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m01-01-intervals"})
    endpoints = np.array([1.1, 1.5, 2.0, 3.0])
    slopes = (endpoints**2 - 1) / (endpoints - 1)
    np.testing.assert_allclose(slopes, [2.1, 2.5, 3, 4])
    x = np.linspace(1.005, 3.15, 240)
    fig, ax = plt.subplots(figsize=(8.8, 6.8))
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(x, x + 1, color="#7C3AED", linewidth=2.7)
    ax.scatter(endpoints, slopes, s=64, color="#2563EB", zorder=3)
    ax.scatter([1], [2], s=85, facecolors="#F8FAFC", edgecolors="#7C3AED",
               linewidths=2, zorder=4)
    labels = [("(1.1, 2.1)", (1.1, 2.1), (1.45, 2.04)),
              ("(1.5, 2.5)", (1.5, 2.5), (1.13, 2.71)),
              ("(2, 3)", (2, 3), (2.18, 2.79)),
              ("(3, 4)", (3, 4), (2.41, 4.08))]
    for label, point, text in labels:
        ax.annotate(label, point, xytext=text, color="#1E3A8A", fontsize=16,
                    arrowprops={"arrowstyle": "-", "color": "#64748B", "lw": 1})
    ax.set_xlim(0.88, 3.22)
    ax.set_ylim(1.87, 4.32)
    ax.set_xticks([1, 1.5, 2, 2.5, 3])
    ax.set_yticks([2, 2.5, 3, 3.5, 4])
    ax.set_xlabel("End input x₂ (start input = 1)", labelpad=12)
    ax.set_ylabel("Average rate", labelpad=12)
    ax.set_title("End input controls the average slope", fontsize=18, pad=22)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#CBD5E1", linewidth=0.7)
    fig.text(0.5, 0.16, "Slope = x₂ + 1 for x₂ ≠ 1", ha="center", color="#5B21B6", fontsize=16)
    fig.text(0.5, 0.09, "Open point (1, 2): the quotient is undefined at x₂ = 1.",
             ha="center", color="#334155", fontsize=16)
    fig.subplots_adjust(left=0.16, right=0.94, bottom=0.29, top=0.86)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
