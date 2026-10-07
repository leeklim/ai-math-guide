#!/usr/bin/env python3
"""Four exact illustrative sampling densities with separate bias and variance."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-07-bias-variance"})
    fig, axes = plt.subplots(2, 2, figsize=(10, 7.8), sharex=True, sharey=True, constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    x = np.linspace(-3, 4, 501)
    for ax, (mean, sd) in zip(axes.flat, [(0, 1), (1, 1), (0, .4), (1, .4)]):
        ax.set_facecolor("#F8FAFC")
        ax.plot(x, np.exp(-(x-mean)**2/(2*sd**2))/(np.sqrt(2*np.pi)*sd), color="#7C3AED", linewidth=2.6)
        ax.axvline(0, color="#2563EB", linewidth=1.8, linestyle="--", label="target θ = 0")
        if mean != 0:
            ax.axvline(mean, color="#059669", linewidth=1.8, linestyle=":", label="estimator mean = 1")
        ax.set_title(f"Bias {mean:g}; variance {sd**2:g}", fontsize=15, fontweight="bold")
        ax.set(xlim=(-3, 4), ylim=(0, 1.12))
        ax.grid(color="#CBD5E1", linewidth=.7)
        ax.spines[["top", "right"]].set_visible(False)
    for ax in axes[-1]:
        ax.set_xlabel("estimator value")
    for ax in axes[:, 0]:
        ax.set_ylabel("sampling density")
    axes[0, 1].legend(loc="upper left", frameon=False, fontsize=10)
    fig.suptitle("Illustrative sampling distributions; same fixed target", fontsize=17, fontweight="bold")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
