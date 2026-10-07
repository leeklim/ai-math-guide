#!/usr/bin/env python3
"""Generate the evidence timeline used in I08-09."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x: np.ndarray, center: float, slope: float) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-slope * (x - center)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 26,
            "axes.labelsize": 24,
            "xtick.labelsize": 22,
            "ytick.labelsize": 22,
            "svg.fonttype": "none",
            "svg.hashsalt": "mmi-i08-09",
        }
    )
    step = np.linspace(0, 100, 300)
    curves = [
        ("Formation", sigmoid(step, 32, 0.11), "#64748B", "-"),
        ("Recoverability", sigmoid(step, 45, 0.13), "#2563EB", "-"),
        ("Use", sigmoid(step, 63, 0.15), "#DC2626", "--"),
        ("Behavior", sigmoid(step, 72, 0.12), "#059669", ":"),
    ]
    fig, ax = plt.subplots(figsize=(1040 / 72, 820 / 72))
    fig.subplots_adjust(left=.13, right=.96, bottom=.37, top=.80)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    for label, values, color, linestyle in curves:
        ax.plot(step, values, label=label, color=color, linewidth=2.2, linestyle=linestyle)
    ax.axhline(0.75, color="#475569", linewidth=1, linestyle=(0, (4, 4)))
    threshold = 0.75
    recover_crossing = 45 + np.log(threshold / (1 - threshold)) / 0.13
    use_crossing = 63 + np.log(threshold / (1 - threshold)) / 0.15
    for x, center, slope, color in ((recover_crossing, 45, .13, "#2563EB"), (use_crossing, 63, .15, "#DC2626")):
        assert np.isclose(sigmoid(np.array([x]), center, slope)[0], threshold)
        ax.plot([x, x], [0, threshold], color=color, linewidth=1.2, alpha=0.65)
        ax.scatter([x], [threshold], color=color, marker="s", s=55, zorder=5)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1.04)
    ax.set_xlabel("training step")
    ax.set_ylabel("normalized evidence")
    fig.legend(*ax.get_legend_handles_labels(), frameon=False, loc="center", bbox_to_anchor=(.54, .23), ncol=2, fontsize=24)
    fig.suptitle("Conceptual evidence curves; threshold = 0.75", fontsize=28, y=.94)
    fig.text(.5, .07, f"Recoverability crossing: {recover_crossing:.2f}; use crossing: {use_crossing:.2f}\nContinuous illustration, not checkpoint observations.", ha="center", fontsize=24, color="#475569", linespacing=1.5)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#CBD5E1", linewidth=0.6, alpha=0.65)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
