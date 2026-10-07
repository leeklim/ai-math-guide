#!/usr/bin/env python3
"""Exact standard-normal two-sided p-value for the lesson's z=2 example."""
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
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 26, "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-10-two-tail"})
    z = np.linspace(-4, 4, 801)
    density = np.exp(-z*z/2)/np.sqrt(2*np.pi)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(z, density, color="#7C3AED", linewidth=2.6)
    ax.fill_between(z, 0, density, where=np.abs(z)>=2, color="#D97706", alpha=.35, label="two tails: p ≈ 0.0455")
    ax.set(xlim=(-4, 4), ylim=(0, .46), xlabel="null statistic z", ylabel="density under H₀")
    ax.set_xticks([-2, 0, 2])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Two-sided alternative\nObserved z = 2", fontsize=26, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=24)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
