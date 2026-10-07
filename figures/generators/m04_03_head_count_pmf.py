#!/usr/bin/env python3
"""Plot the equal-outcome head-count PMF for M04-03."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-03-pmf"})
    x = np.array([0, 1, 2])
    p = np.array([0.25, 0.50, 0.25])
    fig, ax = plt.subplots(figsize=(7.6, 5.3), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.bar(x, p, width=0.42, color=["#2563EB", "#059669", "#2563EB"],
           edgecolor="#334155", linewidth=1.3)
    for value, mass, outcomes in zip(x, p, ["TT", "HT + TH", "HH"]):
        ax.text(value, mass + 0.025, f"{mass:.2f}\n{outcomes}", ha="center",
                va="bottom", color="#334155", linespacing=1.6)
    ax.set_xlim(-0.6, 2.6)
    ax.set_ylim(0, 0.72)
    ax.set_xticks(x)
    ax.set_yticks([0, 0.25, 0.50])
    ax.set_xlabel("head count x")
    ax.set_ylabel("probability mass p_X(x)")
    ax.set_title("Outcome masses collect at each value", fontsize=18, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#CBD5E1", linewidth=0.7)
    ax.set_axisbelow(True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
