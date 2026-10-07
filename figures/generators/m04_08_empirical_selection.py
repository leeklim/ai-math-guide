#!/usr/bin/env python3
"""Exact finite-population risks versus one observed training subset."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-08-empirical-selection"})
    x = np.linspace(0, 3, 101)
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 6.6), sharex=True, sharey=True, constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    for ax in axes:
        ax.set_facecolor("#F8FAFC")
        ax.plot(x, x, color="#7C3AED", linewidth=2.4, label="f(x) = x")
        ax.plot(x, np.full_like(x, .5), color="#059669", linewidth=2.4, linestyle="--", label="g(x) = 0.5")
        ax.set(xlim=(-.2, 3.2), ylim=(-.3, 3.5), xlabel="input x")
        ax.set_xticks([0, 1, 2, 3])
        ax.grid(color="#CBD5E1", linewidth=.7)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].scatter([0, 1], [0, 1], color="#2563EB", s=90, zorder=5)
    axes[1].scatter([0, 1, 2, 3], [0, 1, 0, 1], color="#2563EB", s=90, zorder=5)
    axes[0].set_title("Observed training pairs\nMean loss: f = 0; g = 0.25", fontsize=15)
    axes[1].set_title("Four equally weighted population pairs\nRisk: f = 2; g = 0.25", fontsize=15)
    axes[0].set_ylabel("target / prediction")
    axes[0].legend(loc="upper left", frameon=False, fontsize=12)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
