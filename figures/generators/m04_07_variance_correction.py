#!/usr/bin/env python3
"""Expected variance-estimator ratios under iid finite-variance sampling."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-07-variance-correction"})
    n = np.arange(2, 21)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(n, (n-1)/n, "o-", color="#7C3AED", linewidth=2.5, label="divide by n: (n − 1)/n")
    ax.plot(n, np.ones_like(n), "s--", color="#059669", linewidth=2, label="divide by n − 1: 1")
    ax.set(xlim=(1.5, 20.5), ylim=(.4, 1.12), xlabel="sample size n", ylabel="expected estimate / σ²")
    ax.set_xticks([2, 5, 10, 15, 20])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Expected estimate / σ²\nIid finite-variance sampling", fontsize=26, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=24)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
