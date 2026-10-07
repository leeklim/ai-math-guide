"""Reproduce local component cancellation and a finite zero-ablation error."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    name = args.output.stem.removeprefix("N05-26-")
    plt.rcParams.update({"font.size": 26, "font.family": "DejaVu Sans",
                         "svg.fonttype": "none", "svg.hashsalt": "n05-26",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(7.2, 9))
    fig.subplots_adjust(left=.23, right=.97, bottom=.19, top=.83)
    if name == "component-cancellation":
        values = np.array([3 * .2, -2 * .3])
        ax.bar([0, 1], values, color=["#2563EB", "#7C3AED"], zorder=3)
        ax.scatter([2], [values.sum()], color="#059669", s=75, zorder=4)
        ax.set_xticks([0, 1, 2], ["coord 0", "coord 1", "sum"])
        ax.set_ylim(-.9, .9)
        ax.set_yticks([-.6, 0, .6])
        ax.axhline(0, color="#64748B", lw=1.5)
        ax.text(0, .66, "+0.6", ha="center", fontsize=27)
        ax.text(1, -.76, "−0.6", ha="center", fontsize=27)
        ax.text(2, .12, "0", ha="center", fontsize=27, color="#059669")
        ax.set_ylabel("predicted target change")
        ax.set_title("∇s=(3,−2), δa=(0.2,0.3)\nCoordinate effects cancel", fontsize=23, pad=22)
        ax.set_xlabel("∂s/∂aᵢ × δaᵢ", fontsize=26, labelpad=17)
        ax.grid(axis="y", color="#D9E2EF", zorder=0)
    elif name == "finite-zero-ablation":
        a = np.linspace(-.05, 1.5, 160)
        ax.plot(a, a * a, color="#7C3AED", lw=3, label="actual s=a²")
        ax.plot(a, 2 * a - 1, "--", color="#D97706", lw=2.5, label="tangent at 1")
        ax.scatter([1, 0, 0], [1, 0, -1], color=["#2563EB", "#059669", "#D97706"], s=55, zorder=5)
        ax.set_xlim(-.12, 1.56)
        ax.set_ylim(-1.5, 2.6)
        ax.set_xticks([0, 1])
        ax.set_yticks([-1, 0, 1, 2])
        ax.text(.04, .43, "actual: 0", fontsize=24, color="#059669")
        ax.text(.07, -1.28, "linear: −1", fontsize=24, color="#D97706")
        ax.text(.04, 1.33, "baseline (1,1)", fontsize=22, color="#2563EB")
        ax.set_xlabel("activation a")
        ax.set_ylabel("target s")
        ax.set_title("Zero ablation: a=1 → 0\nActual Δs=−1, linear Δs=−2", fontsize=23, pad=22)
        ax.legend(loc="upper left", fontsize=21, frameon=False)
        ax.grid(color="#D9E2EF")
    else:
        raise ValueError(name)
    fig.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, metadata={"Date": None})
    plt.close(fig)

if __name__ == "__main__":
    main()
