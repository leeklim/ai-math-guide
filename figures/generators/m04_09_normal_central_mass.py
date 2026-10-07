#!/usr/bin/env python3
"""Standard-normal central probability and equal tails."""
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
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 26, "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-09-central-mass"})
    z = np.linspace(-4, 4, 801)
    pdf = np.exp(-z*z/2)/np.sqrt(2*np.pi)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(z, pdf, color="#7C3AED", linewidth=2.6)
    ax.fill_between(z, 0, pdf, where=np.abs(z)<=1.96, color="#059669", alpha=.25, label="central area ≈ 0.95")
    ax.fill_between(z, 0, pdf, where=np.abs(z)>1.96, color="#D97706", alpha=.35, label="each tail ≈ 0.025")
    ax.set(xlim=(-4, 4), ylim=(0, .46), xlabel="standardized error", ylabel="density")
    ax.set_xticks([-1.96, 0, 1.96], ["−1.96", "0", "1.96"])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Standard normal\nEqual probability tails", fontsize=26, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=24)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
