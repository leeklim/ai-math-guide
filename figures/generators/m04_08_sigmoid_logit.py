#!/usr/bin/env python3
"""Real logit to probability mapping with the exact log-three example."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-08-sigmoid-logit"})
    z = np.linspace(-5, 5, 401)
    fig, ax = plt.subplots(figsize=(7.2, 9), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(z, 1/(1+np.exp(-z)), color="#7C3AED", linewidth=2.6)
    ax.plot([np.log(3), np.log(3), -5], [0, .75, .75], color="#059669", linestyle="--", linewidth=1.6)
    ax.scatter([np.log(3)], [.75], color="#059669", s=90, zorder=5, label="z = log(3); p = 0.75")
    ax.set(xlim=(-5, 5), ylim=(0, 1.05), xlabel="logit z", ylabel="probability σ(z)")
    ax.set_xticks([-5, 0, 5])
    ax.set_yticks([0, .5, .75, 1])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Linear log-odds\nNonlinear probability", fontsize=26, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=24)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
