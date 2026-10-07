#!/usr/bin/env python3
"""Show an exact discrete dependent pair with zero covariance."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-04-zero-cov"})
    x = np.array([-1, 0, 1])
    y = x ** 2
    curve = np.linspace(-1.12, 1.12, 151)
    fig, ax = plt.subplots(figsize=(7.6, 6.6), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(curve, curve ** 2, color="#94A3B8", linestyle="--", linewidth=1.7,
            label="function rule Y = X²")
    ax.scatter(x, y, s=160, color="#7C3AED", zorder=5, label="possible outcomes: each mass 1/3")
    ax.axhline(2/3, color="#059669", linewidth=1.3, linestyle=":", label="mean Y = 2/3")
    ax.axvline(0, color="#64748B", linewidth=1)
    ax.annotate("negative term: −1/9", (-1, 1), xytext=(-1.08, 1.39), color="#9A3412", fontsize=13)
    ax.annotate("positive term: +1/9", (1, 1), xytext=(0.16, 1.39), color="#065F46", fontsize=13)
    ax.set(xlim=(-1.35, 1.35), ylim=(-0.14, 1.6), xlabel="X", ylabel="Y = X²")
    ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 2/3, 1])
    ax.grid(color="#CBD5E1", linewidth=0.7)
    ax.set_title("Zero covariance can conceal exact dependence", fontsize=17, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.19), frameon=False, fontsize=12)
    ax.spines[["top", "right"]].set_visible(False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
