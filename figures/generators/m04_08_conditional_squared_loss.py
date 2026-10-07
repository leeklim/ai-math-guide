#!/usr/bin/env python3
"""Exact squared conditional risk from the lesson's two-point example."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-08-conditional-squared"})
    a = np.linspace(-1, 7, 401)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(a, 3+(a-3)**2, color="#7C3AED", linewidth=2.6, label="conditional squared risk")
    ax.axhline(3, color="#64748B", linewidth=1.5, linestyle="--")
    ax.scatter([3], [3], color="#059669", s=90, zorder=5, label="mean 3: risk 3")
    ax.scatter([4], [4], color="#D97706", s=90, zorder=5, label="mode 4: risk 4")
    ax.set(xlim=(-1, 7), ylim=(0, 21), xlabel="prediction a", ylabel="expected squared loss")
    ax.set_xticks([0, 2, 3, 4, 6])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("One fixed input x\nP(Y = 0) = 0.25\nP(Y = 4) = 0.75", fontsize=26, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=22)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
