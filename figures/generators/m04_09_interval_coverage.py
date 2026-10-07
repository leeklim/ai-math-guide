#!/usr/bin/env python3
"""Possible interval realizations, not an empirical coverage estimate."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 26, "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-09-coverage"})
    centers = np.array([-2.3, -1.6, -1, -.8, -.3, -.1, .1, .5, .7, 1.3, 1.8, 2.2])
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    for row, center in enumerate(centers, start=1):
        color = "#2563EB" if abs(center) <= 1.96 else "#D97706"
        ax.plot([center-1.96, center+1.96], [row, row], color=color, linewidth=2.5)
        ax.scatter([center], [row], color=color, s=25, zorder=5)
    ax.axvline(0, color="#64748B", linestyle="--", linewidth=1.8)
    ax.set(xlim=(-4.5, 4.5), ylim=(.3, 12.7), xlabel="parameter scale", ylabel="possible sample")
    ax.set_xticks([-4, 0, 4])
    ax.set_yticks([1, 4, 8, 12])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Fixed θ = 0\nIllustrative intervals\nCenter ± 1.96; SE = 1", fontsize=26, fontweight="bold")
    ax.plot([], [], color="#2563EB", linewidth=2.5, label="contains θ")
    ax.plot([], [], color="#D97706", linewidth=2.5, label="misses θ")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.23), frameon=False, fontsize=26)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
