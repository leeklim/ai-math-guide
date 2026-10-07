#!/usr/bin/env python3
"""Compare exact Bernoulli, observed empirical and mean sampling PMFs."""
from __future__ import annotations
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-06-three-distributions"})
    fig, axes = plt.subplots(3, 1, figsize=(7.2, 9), sharex=True, constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    plots = [("Population: one draw X ~ Bernoulli(0.5)", [0, 1], [.5, .5], "#2563EB"),
             ("Empirical: one observed sample (0, 1)", [0, 1], [.5, .5], "#059669"),
             ("Sampling: X̄ from all iid size-two samples", [0, .5, 1], [.25, .5, .25], "#7C3AED")]
    for ax, (title, x, probabilities, color) in zip(axes, plots):
        ax.set_facecolor("#F8FAFC")
        ax.bar(x, probabilities, width=.15, color=color, edgecolor="#475569", zorder=3)
        ax.set(ylim=(0, .65), xlim=(-.2, 1.2), ylabel="probability mass")
        ax.set_title(title, fontsize=14)
        ax.grid(axis="y", color="#CBD5E1", linewidth=.7)
        ax.spines[["top", "right"]].set_visible(False)
    axes[-1].set_xticks([0, .5, 1])
    axes[-1].set_xlabel("value (different random object in each panel)")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
