#!/usr/bin/env python3
"""The same right-tail rule applied to positive and negative observed statistics."""
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
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14, "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-10-direction"})
    z = np.linspace(-4, 4, 801)
    density = np.exp(-z*z/2)/np.sqrt(2*np.pi)
    fig, axes = plt.subplots(2, 1, figsize=(7.8, 8.4), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    for ax, observed, p_text in zip(axes, [2, -2], ["0.02275", "0.97725"]):
        ax.set_facecolor("#F8FAFC")
        ax.plot(z, density, color="#7C3AED", linewidth=2.4)
        ax.fill_between(z, 0, density, where=z>=observed, color="#059669", alpha=.25)
        ax.axvline(observed, color="#059669", linestyle="--", linewidth=1.3)
        ax.set(xlim=(-4, 4), ylim=(0, .46), xlabel="null statistic z", ylabel="density under H₀")
        ax.set_title(f"Right-sided rule; observed z = {observed}; p ≈ {p_text}", fontsize=14)
        ax.set_xticks([-2, 0, 2])
        ax.grid(color="#CBD5E1", linewidth=.7)
        ax.spines[["top", "right"]].set_visible(False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
