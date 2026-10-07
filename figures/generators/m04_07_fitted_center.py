#!/usr/bin/env python3
"""An observed sample's squared-deviation sum minimized at its own mean."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-07-fitted-center"})
    c = np.linspace(1, 7, 401)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(c, 8+3*(c-4)**2, color="#7C3AED", linewidth=2.6)
    ax.scatter([3], [11], color="#2563EB", s=75, zorder=5, label="μ = 3: sum 11")
    ax.scatter([4], [8], color="#059669", s=75, zorder=5, label="x̄ = 4: sum 8")
    ax.plot([3, 3], [8, 11], color="#D97706", linewidth=3)
    ax.text(4, 27, "Reduction\n3(4 − 3)² = 3", color="#9A3412", ha="center", fontsize=26)
    ax.set(xlim=(1, 7), ylim=(5, 38), xlabel="chosen center c", ylabel="squared-deviation sum")
    ax.set_xticks([1, 3, 4, 5, 7])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Fitting the center\nreduces the sum\nSample: 2, 4, 6", fontsize=26, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=26)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
