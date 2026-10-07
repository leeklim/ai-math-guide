#!/usr/bin/env python3
"""Exact illustrative normal sampling density before and after half shrinkage."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-07-shrinkage-density"})
    x = np.linspace(-3, 5, 601)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    for mean, sd, color, label in [(1, 1, "#2563EB", "X̄: mean 1, var 1"),
                                    (.5, .5, "#7C3AED", "X̄/2: mean 0.5, var 0.25")]:
        ax.plot(x, np.exp(-(x-mean)**2/(2*sd**2))/(np.sqrt(2*np.pi)*sd), color=color, linewidth=2.6, label=label)
    ax.axvline(1, color="#059669", linestyle="--", linewidth=1.6)
    ax.text(1.3, .86, "μ = 1", color="#065F46", fontsize=26)
    ax.set(xlim=(-3, 5), ylim=(0, .95), xlabel="estimator value", ylabel="sampling density")
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Shrink toward zero\nNormal sampling example", fontsize=26, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=24)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
