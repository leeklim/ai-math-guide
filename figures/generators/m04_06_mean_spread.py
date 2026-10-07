#!/usr/bin/env python3
"""Exact Gaussian sampling densities with unchanged observation variance."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-06-mean-spread"})
    x = np.linspace(-3.5, 3.5, 601)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    for n, color in [(1, "#2563EB"), (4, "#7C3AED"), (16, "#059669")]:
        se = 1/np.sqrt(n)
        ax.plot(x, np.exp(-x*x/(2*se*se))/(np.sqrt(2*np.pi)*se), color=color,
                linewidth=2.6, label=f"n = {n}, SE = {se:g}")
    ax.set(xlim=(-3.5, 3.5), ylim=(0, 1.8), xlabel="sample mean", ylabel="density")
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("The mean narrows\nIid Xᵢ ~ N(0, 1)", fontsize=26, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.22), frameon=False, fontsize=24)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
