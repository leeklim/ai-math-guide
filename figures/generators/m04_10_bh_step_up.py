#!/usr/bin/env python3
"""Exact BH examples: max passing rank, not first failed rank."""
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
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14, "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-10-bh"})
    rank = np.arange(1, 5)
    thresholds = rank*.05/4
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 6.5), sharey=True, constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    for ax, p, title in zip(axes, [[.001, .02, .04, .2], [.014, .02, .04, .2]], ["Lesson example", "First rank fails; second passes"]):
        p = np.array(p)
        k = rank[p <= thresholds].max()
        ax.set_facecolor("#F8FAFC")
        ax.axvspan(.7, k+.3, color="#2563EB", alpha=.1)
        ax.plot(rank, thresholds, "s--", color="#059669", linewidth=2, label="rank threshold kq/m")
        for r, value, threshold in zip(rank, p, thresholds):
            ax.scatter([r], [value], marker="o" if value<=threshold else "x", color="#2563EB" if value<=threshold else "#D97706", s=70, zorder=5)
        ax.axhline(k*.05/4, color="#7C3AED", linewidth=1.6, linestyle=":", label="final cutoff 0.025")
        ax.set(xlim=(.5, 4.5), ylim=(0, .06), xlabel="sorted p-value rank")
        ax.set_xticks(rank)
        ax.grid(color="#CBD5E1", linewidth=.7)
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_title(f"{title}\nMax passing rank k = {k}\np₄ = 0.200 is above this zoom", fontsize=13)
    axes[0].set_ylabel("p-value / threshold")
    axes[0].legend(loc="upper center", bbox_to_anchor=(.5, -.2), frameon=False, fontsize=11)
    fig.suptitle("BH step-up: m = 4, q = 0.05; shaded ranks rejected", fontsize=16, fontweight="bold")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
