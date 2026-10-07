#!/usr/bin/env python3
"""Illustrative effect size and standard error change different inferential quantities."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 26, "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-10-effect-precision"})
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.errorbar(.05, 2, xerr=1.96*.01, fmt="o", color="#2563EB", linewidth=2.6, capsize=6, label="small: p < 0.001")
    ax.errorbar(.20, 1, xerr=1.96*.20, fmt="o", color="#7C3AED", linewidth=2.6, capsize=6, label="large: p ≈ 0.317")
    ax.axvline(0, color="#64748B", linestyle="--", linewidth=1.5)
    ax.set(xlim=(-.25, .65), ylim=(.5, 2.5), xlabel="effect estimate scale")
    ax.set_yticks([1, 2], ["Large", "Small"])
    ax.set_xticks([-.2, 0, .2, .4, .6])
    ax.grid(axis="x", color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.set_title("Effect size ≠ significance\nIllustrative 95% z intervals", fontsize=24, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=24)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
