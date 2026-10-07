#!/usr/bin/env python3
"""Compare corresponding Gaussian intervals before and after standardization."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-05-standardization"})
    fig, axes = plt.subplots(2, 1, figsize=(7.6, 7.2), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    for ax, mean, std, left, right, limits, name in [(axes[0], 10, 2, 8, 13, (2, 18), "Original X: mean 10, std 2"),
                                                    (axes[1], 0, 1, -1, 1.5, (-4, 4), "Z = (X − 10)/2: mean 0, std 1")]:
        x = np.linspace(*limits, 401)
        density = np.exp(-0.5*((x-mean)/std)**2) / (std*np.sqrt(2*np.pi))
        interval = np.linspace(left, right, 121)
        height = np.exp(-0.5*((interval-mean)/std)**2) / (std*np.sqrt(2*np.pi))
        ax.set_facecolor("#F8FAFC")
        ax.plot(x, density, color="#7C3AED", linewidth=2.8)
        ax.fill_between(interval, 0, height, color="#059669", alpha=0.24)
        ax.vlines([left, right], 0, np.exp(-0.5*((np.array([left, right])-mean)/std)**2)/(std*np.sqrt(2*np.pi)),
                  color="#059669", linewidth=1.6)
        ax.set(xlim=limits, ylim=(0, 0.46), ylabel="density")
        ax.set_xticks(sorted(set([limits[0], left, mean, right, limits[1]])))
        ax.grid(color="#CBD5E1", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.set_title(name, fontsize=15)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_xlabel("original value x")
    axes[1].set_xlabel("standardized value z")
    fig.suptitle("Corresponding intervals have the same probability\n8 ≤ X ≤ 13  ↔  −1 ≤ Z ≤ 1.5", fontsize=16, fontweight="bold")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
