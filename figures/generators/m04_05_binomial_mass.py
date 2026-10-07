#!/usr/bin/env python3
"""Plot a success-count PMF under independent equal-p trials."""
from __future__ import annotations
import argparse
from math import comb
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-05-binomial"})
    n = 5
    s = np.arange(n + 1)
    fig, axes = plt.subplots(2, 1, figsize=(7.6, 6.8), constrained_layout=True, sharex=True)
    fig.patch.set_facecolor("#F8FAFC")
    for ax, p, color in zip(axes, [0.2, 0.5], ["#2563EB", "#7C3AED"]):
        mass = np.array([comb(n, int(k)) * p**k * (1-p)**(n-k) for k in s])
        ax.set_facecolor("#F8FAFC")
        ax.bar(s, mass, width=0.5, color=color, edgecolor="#334155")
        ax.set(ylim=(0, 0.55), ylabel="probability mass")
        ax.set_yticks([0, 0.25, 0.5])
        ax.grid(axis="y", color="#CBD5E1", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.set_title(f"n = 5, p = {p:g}; mean count np = {n*p:g}", fontsize=15)
        ax.spines[["top", "right"]].set_visible(False)
    axes[-1].set_xticks(s)
    axes[-1].set_xlabel("number of successes s")
    fig.suptitle("Binomial outcomes count successes, not trial order", fontsize=16, fontweight="bold")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
