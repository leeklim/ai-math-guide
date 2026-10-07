#!/usr/bin/env python3
"""Show the two support values across Bernoulli parameters."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-05-bernoulli"})
    fig, axes = plt.subplots(1, 3, figsize=(8.4, 4.8), constrained_layout=True, sharey=True)
    fig.patch.set_facecolor("#F8FAFC")
    for ax, p in zip(axes, [0.1, 0.5, 0.9]):
        ax.set_facecolor("#F8FAFC")
        masses = np.array([1 - p, p])
        ax.bar([0, 1], masses, width=0.43, color=["#64748B", "#2563EB"])
        for x, mass in enumerate(masses):
            ax.text(x, mass + 0.035, f"{mass:.1f}", ha="center", color="#334155")
        ax.set(xlim=(-0.65, 1.65), ylim=(0, 1.15), xlabel="outcome x")
        ax.set_xticks([0, 1]); ax.set_yticks([0, 0.5, 1])
        ax.grid(axis="y", color="#CBD5E1", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.set_title(f"p = {p:g}", fontsize=16)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("probability mass")
    fig.suptitle("Bernoulli always has support {0, 1}", fontsize=17, fontweight="bold")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
