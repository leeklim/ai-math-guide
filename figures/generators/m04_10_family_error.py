#!/usr/bin/env python3
"""Exact independent all-null FWER with and without per-test correction."""
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
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 26, "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-10-family-error"})
    m = np.arange(1, 101)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(m, 1-.95**m, color="#7C3AED", linewidth=2.6, label="per-test α = 0.05")
    ax.plot(m, 1-(1-.05/m)**m, color="#059669", linewidth=2.6, label="per-test α = 0.05/m")
    ax.axhline(.05, color="#64748B", linestyle="--", linewidth=1.3)
    ax.scatter([20], [1-.95**20], color="#D97706", s=85, zorder=5)
    ax.set(xlim=(0, 100), ylim=(0, 1.05), xlabel="number of tests m", ylabel="P(at least one false positive)")
    ax.set_xticks([0, 20, 50, 100])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("All m nulls true\nIndependent tests", fontsize=26, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=24)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
