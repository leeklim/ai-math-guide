#!/usr/bin/env python3
"""Plot Gaussian translation at fixed variance."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-05-gaussian-mean"})
    x = np.linspace(-4.5, 6.5, 501)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    for mean, color in [(0, "#2563EB"), (2, "#7C3AED")]:
        density = np.exp(-0.5 * (x - mean)**2) / np.sqrt(2*np.pi)
        ax.plot(x, density, color=color, linewidth=2.8, label=f"mean {mean}, var 1")
        ax.axvline(mean, color=color, linestyle=":", linewidth=1.1)
    ax.set(xlim=(-4.5, 6.5), ylim=(0, 0.52), xlabel="value x", ylabel="density")
    ax.set_xticks([-4, -2, 0, 2, 4, 6])
    ax.grid(color="#CBD5E1", linewidth=0.7)
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.22), fontsize=24, frameon=False)
    ax.set_title("Change the mean\nMove the same shape", fontsize=26, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
