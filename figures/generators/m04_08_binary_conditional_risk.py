#!/usr/bin/env python3
"""Conditional zero-one risks and their equal-cost decision threshold."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-08-binary-risk"})
    p = np.linspace(0, 1, 101)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(p, p, color="#2563EB", linewidth=2.6, label="predict 0: risk p")
    ax.plot(p, 1-p, color="#7C3AED", linewidth=2.6, label="predict 1: risk 1 − p")
    ax.axvline(.5, color="#64748B", linestyle="--", linewidth=1.3)
    ax.scatter([.5], [.5], color="#059669", s=85, zorder=5)
    ax.set(xlim=(0, 1), ylim=(0, 1.05), xlabel="p = P(Y = 1 | x)", ylabel="conditional error risk")
    ax.set_xticks([0, .5, 1])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Choose the lower risk\nEqual error costs", fontsize=26, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=24)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
