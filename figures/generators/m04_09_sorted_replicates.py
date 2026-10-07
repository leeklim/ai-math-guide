#!/usr/bin/env python3
"""Sorted illustrative replicate list with linear-percentile convention."""
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
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 26, "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-09-sorted-replicates"})
    values = np.array([1.]*5+[2.]*10+[3.]*5)
    low, high = np.quantile(values, [.025, .975], method="linear")
    sd = values.std(ddof=1)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.axhspan(low, high, color="#059669", alpha=.12)
    ax.scatter(np.arange(1, 21), values, color="#2563EB", s=50, zorder=5)
    ax.axhline(low, color="#059669", linestyle="--", linewidth=1.7)
    ax.axhline(high, color="#059669", linestyle="--", linewidth=1.7)
    ax.set(xlim=(0, 21), ylim=(.5, 3.5), xlabel="sorted replicate rank", ylabel="bootstrap mean")
    ax.set_xticks([1, 5, 10, 15, 20])
    ax.set_yticks([1, 2, 3])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("B = 20 illustrative replicates\n5 ones; 10 twos; 5 threes", fontsize=24, fontweight="bold")
    ax.plot([], [], color="#059669", linestyle="--", label=f"percentile [{low:g}, {high:g}]")
    ax.plot([], [], color="#2563EB", marker="o", linestyle="none", label=f"replicate SD ≈ {sd:.3f}")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=24)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
