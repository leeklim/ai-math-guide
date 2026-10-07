#!/usr/bin/env python3
"""Plot normalized Gaussian densities across standard deviations."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-05-gaussian-scale"})
    x = np.linspace(-7, 7, 601)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    for std, color in [(0.5, "#2563EB"), (1, "#7C3AED"), (2, "#059669")]:
        density = np.exp(-0.5 * (x/std)**2) / (std*np.sqrt(2*np.pi))
        ax.plot(x, density, color=color, linewidth=2.8, label=f"std {std:g}, var {std**2:g}")
    ax.set(xlim=(-7, 7), ylim=(0, 1.07), xlabel="value x (mean 0)", ylabel="density")
    ax.set_xticks([-6, -3, 0, 3, 6])
    ax.grid(color="#CBD5E1", linewidth=0.7)
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.22), fontsize=24, frameon=False)
    ax.set_title("Wider density, lower peak\nTotal area stays 1", fontsize=26, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
