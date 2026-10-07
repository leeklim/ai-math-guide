#!/usr/bin/env python3
"""Dimensionless residual penalties before averaging across observations."""
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
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 26,
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-08-residual-penalties"})
    e = np.linspace(-3, 3, 401)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(e, e*e, color="#7C3AED", linewidth=2.6, label="squared: e²")
    ax.plot(e, np.abs(e), color="#2563EB", linewidth=2.6, label="absolute: |e|")
    ax.set(xlim=(-3, 3), ylim=(0, 10), xlabel="dimensionless residual e", ylabel="per-record penalty")
    ax.set_xticks([-3, 0, 3])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Same residual\nDifferent penalty", fontsize=26, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=26)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
