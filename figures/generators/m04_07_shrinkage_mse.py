#!/usr/bin/env python3
"""Two targets show that fixed shrinkage does not always lower MSE."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-07-shrinkage-mse"})
    a = np.linspace(0, 1, 301)
    fig, axes = plt.subplots(2, 1, figsize=(7.8, 8.2), sharex=True, constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    for ax, mu in zip(axes, [1, 3]):
        variance = a*a
        bias2 = (a-1)**2*mu*mu
        ax.set_facecolor("#F8FAFC")
        ax.plot(a, variance, color="#2563EB", linewidth=2, label="variance")
        ax.plot(a, bias2, color="#D97706", linewidth=2, label="bias squared")
        ax.plot(a, variance+bias2, color="#7C3AED", linewidth=2.7, label="MSE")
        ax.scatter([.5, 1], [.25+.25*mu*mu, 1], color="#059669", s=40, zorder=5)
        ax.axvline(.5, color="#64748B", linewidth=1, linestyle="--")
        ax.set(xlim=(0, 1), ylim=(0, 1.2*mu*mu), ylabel="squared error")
        ax.set_title(f"Target μ = {mu}; original mean variance σ²/n = 1", fontsize=14)
        ax.grid(color="#CBD5E1", linewidth=.7)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].legend(loc="upper center", frameon=False, fontsize=11, ncol=3)
    axes[-1].set_xlabel("fixed shrinkage coefficient a")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
