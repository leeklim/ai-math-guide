#!/usr/bin/env python3
"""Generate the exponential-logarithm inverse plot used in M00-05."""

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

    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 13,
            "svg.fonttype": "none",
            "svg.hashsalt": "mmi-m00-05",
        }
    )
    exp_x = np.linspace(-2.2, 1.42, 320)
    log_x = np.linspace(0.12, 4.2, 320)
    diagonal = np.linspace(-2.2, 4.2, 2)

    fig, ax = plt.subplots(figsize=(8.6, 5.6), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(exp_x, np.exp(exp_x), color="#2563EB", linewidth=2.7, label="y = exp(x)")
    ax.plot(log_x, np.log(log_x), color="#D97706", linewidth=2.7, label="y = log(x)")
    ax.plot(diagonal, diagonal, color="#64748B", linewidth=1.8, linestyle="--", label="y = x")

    e = float(np.e)
    ax.plot([0, 1], [1, 0], color="#94A3B8", linewidth=1.5, linestyle=":")
    ax.plot([1, e], [e, 1], color="#94A3B8", linewidth=1.5, linestyle=":")
    ax.scatter([0, 1], [1, e], s=70, color="#2563EB", marker="o", zorder=5)
    ax.scatter([1, e], [0, 1], s=70, color="#D97706", marker="s", zorder=5)
    ax.annotate("(0, 1)", (0, 1), xytext=(-54, 9), textcoords="offset points", color="#1E3A8A")
    ax.annotate("(1, 0)", (1, 0), xytext=(8, -22), textcoords="offset points", color="#9A3412")
    ax.annotate("(1, e)", (1, e), xytext=(-50, 8), textcoords="offset points", color="#1E3A8A")
    ax.annotate("(e, 1)", (e, 1), xytext=(9, -4), textcoords="offset points", color="#9A3412")

    ax.axhline(0, color="#94A3B8", linewidth=1.0)
    ax.axvline(0, color="#94A3B8", linewidth=1.0)
    ax.set_xlim(-2.2, 4.2)
    ax.set_ylim(-2.2, 4.2)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("input")
    ax.set_ylabel("output")
    ax.set_title("Exponential and logarithm swap input and output", fontsize=16, fontweight="bold")
    ax.legend(frameon=False, loc="lower right")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#CBD5E1", linewidth=0.7, alpha=0.75)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
