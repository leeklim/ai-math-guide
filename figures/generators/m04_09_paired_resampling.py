#!/usr/bin/env python3
"""Exact empirical joint and single-draw difference with destroyed pairing."""
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
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14, "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-09-paired"})
    a, b = np.array([.7, .8, .5]), np.array([.6, .7, .4])
    fig, axes = plt.subplots(2, 2, figsize=(10, 8.5), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    for ax in axes.flat:
        ax.set_facecolor("#F8FAFC")
        ax.grid(color="#CBD5E1", linewidth=.7)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0, 0].scatter(a, b, color="#2563EB", s=90, zorder=4)
    aa, bb = np.meshgrid(a, b)
    axes[0, 1].scatter(aa, bb, color="#D97706", s=35, zorder=4)
    for ax in axes[0]:
        ax.set(xlim=(.45, .85), ylim=(.35, .75), xlabel="selected A score", ylabel="selected B score")
    axes[0, 0].set_title("Same index: three observed pairs", fontsize=14)
    axes[0, 1].set_title("Separate indices: nine combinations", fontsize=14)
    axes[1, 0].bar([.1], [1], width=.055, color="#2563EB", edgecolor="#475569", zorder=3)
    values, counts = np.unique(np.round((aa-bb).ravel(), 10), return_counts=True)
    axes[1, 1].bar(values, counts/9, width=.055, color="#D97706", edgecolor="#475569", zorder=3)
    for ax in axes[1]:
        ax.set(xlim=(-.25, .45), ylim=(0, 1.1), xlabel="one selected-pair difference A − B", ylabel="probability mass")
        ax.set_xticks([-.2, .1, .4])
    axes[1, 0].set_title("Always 0.1 in this example", fontsize=14)
    axes[1, 1].set_title("Invented cross-prompt differences", fontsize=14)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
