#!/usr/bin/env python3
"""Exact tail probabilities of mean versus first-observation estimators."""
from __future__ import annotations
import argparse
import math
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-07-consistency-tail"})
    n = np.arange(1, 101)
    tails = [sum(math.comb(int(size), k)*.5**int(size) for k in range(int(size)+1)
                 if abs(k/size-.5) > .25) for size in n]
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(n, tails, color="#2563EB", linewidth=2.4, label="use sample mean X̄")
    ax.plot(n, np.ones_like(n), color="#D97706", linewidth=2, linestyle="--", label="use first observation X₁")
    ax.set(xlim=(0, 100), ylim=(-.03, 1.1), xlabel="sample size n", ylabel="tail probability")
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("P(|estimate − 0.5| > 0.25)\nIid Bernoulli(0.5)", fontsize=26, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=24)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
