#!/usr/bin/env python3
"""Same-center illustrative intervals separate effect and precision."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 26, "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-09-width-effect"})
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    for row, margin, color in [(2, .03, "#2563EB"), (1, .15, "#7C3AED")]:
        ax.errorbar(.05, row, xerr=margin, fmt="o", color=color, linewidth=2.8, capsize=7, markersize=7)
    ax.axvline(0, color="#64748B", linestyle="--", linewidth=1.6)
    ax.set(xlim=(-.13, .23), ylim=(.5, 2.5), xlabel="estimated effect scale")
    ax.set_xticks([-.1, 0, .1, .2])
    ax.set_yticks([1, 2], ["Wide", "Narrow"])
    ax.grid(axis="x", color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.set_title("Same point estimate: 0.05\nDifferent precision\nIllustrative intervals", fontsize=24, fontweight="bold")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
