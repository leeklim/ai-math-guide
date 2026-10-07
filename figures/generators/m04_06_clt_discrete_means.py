#!/usr/bin/env python3
"""Exact standardized binomial masses and Gaussian interval approximations."""
from __future__ import annotations
import argparse
import math
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-06-clt-discrete"})
    p = .2
    fig, axes = plt.subplots(3, 1, figsize=(7.2, 9.5), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    for ax, n in zip(axes, [2, 8, 32]):
        k = np.arange(n+1)
        dz = 1/np.sqrt(n*p*(1-p))
        z = (k-n*p)*dz
        mass = [math.comb(n, int(j))*p**j*(1-p)**(n-j) for j in k]
        approximation = [.5*(math.erf((v+dz/2)/np.sqrt(2))-math.erf((v-dz/2)/np.sqrt(2))) for v in z]
        ax.set_facecolor("#F8FAFC")
        ax.bar(z, mass, width=.7*dz, color="#2563EB", edgecolor="#475569", label="exact mass", zorder=3)
        ax.plot(z, approximation, "o--", color="#D97706", markersize=4,
                linewidth=1.6, label="normal interval mass", zorder=4)
        ax.set(xlim=(-3.5, 4), ylim=(0, max(mass)*1.3), ylabel="probability mass")
        ax.set_title(f"n = {n}; standardized Bernoulli(0.2) mean", fontsize=14)
        ax.grid(color="#CBD5E1", linewidth=.7)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].legend(loc="upper right", frameon=False, fontsize=11)
    axes[-1].set_xlabel("z = (X̄ − p) / √(p(1 − p)/n)")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
