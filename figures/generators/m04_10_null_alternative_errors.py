#!/usr/bin/env python3
"""One rejection region with null alpha and specific-alternative beta/power."""
import argparse
import math
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14, "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-10-errors"})
    x = np.linspace(-4, 6, 1001)
    cutoff = 1.644853626951
    beta = .5*(1+math.erf((cutoff-2.5)/np.sqrt(2)))
    fig, axes = plt.subplots(2, 1, figsize=(7.8, 8.4), sharex=True, constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    for ax, mean in zip(axes, [0, 2.5]):
        pdf = np.exp(-(x-mean)**2/2)/np.sqrt(2*np.pi)
        ax.set_facecolor("#F8FAFC")
        ax.plot(x, pdf, color="#7C3AED", linewidth=2.4)
        ax.axvline(cutoff, color="#64748B", linestyle="--", linewidth=1.5)
        ax.set(xlim=(-4, 6), ylim=(0, .46), ylabel="density")
        ax.grid(color="#CBD5E1", linewidth=.7)
        ax.spines[["top", "right"]].set_visible(False)
    null_pdf = np.exp(-x*x/2)/np.sqrt(2*np.pi)
    alt_pdf = np.exp(-(x-2.5)**2/2)/np.sqrt(2*np.pi)
    axes[0].fill_between(x, 0, null_pdf, where=x>=cutoff, color="#D97706", alpha=.35)
    axes[0].set_title("H₀: N(0,1); Type I error area α = 0.05", fontsize=15)
    axes[1].fill_between(x, 0, alt_pdf, where=x<cutoff, color="#D97706", alpha=.35, label=f"Type II β ≈ {beta:.3f}")
    axes[1].fill_between(x, 0, alt_pdf, where=x>=cutoff, color="#059669", alpha=.25, label=f"power ≈ {1-beta:.3f}")
    axes[1].set_title("Specific H₁: N(2.5,1); same rejection cutoff", fontsize=15)
    axes[1].set_xlabel("statistic; reject to the right of 1.645")
    axes[1].legend(loc="upper right", frameon=False, fontsize=11)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
