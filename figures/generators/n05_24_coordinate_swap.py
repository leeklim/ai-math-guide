"""Plot the coordinate swap from N05-24 without claiming a physical trajectory."""
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
    plt.rcParams.update({"font.size": 26, "font.family": "DejaVu Sans",
                         "svg.fonttype": "none", "svg.hashsalt": "n05-24",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(7.2, 9))
    fig.subplots_adjust(left=.18, right=.96, bottom=.17, top=.79)
    ax.set_aspect("equal")
    ax.set_xlim(0, 2.8)
    ax.set_ylim(0, 2.8)
    ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 1, 2])
    ax.grid(color="#D9E2EF")
    ax.plot([0, 2.8], [0, 2.8], "--", color="#64748B", lw=1.5)
    ax.scatter([1], [2], color="#2563EB", s=45, zorder=4)
    ax.scatter([2], [1], color="#7C3AED", s=45, zorder=4)
    ax.annotate("", (2, 1), (1, 2), arrowprops={"arrowstyle": "->",
                "color": "#64748B", "lw": 2, "mutation_scale": 14,
                "shrinkA": 0, "shrinkB": 0}, zorder=5)
    ax.text(.45, 2.33, "A: (1,2)", fontsize=26, color="#2563EB")
    ax.text(1.27, .63, "B: (2,1)", fontsize=26, color="#7C3AED")
    ax.set_xlabel("first coordinate")
    ax.set_ylabel("second coordinate")
    ax.set_title("A coordinate swap\nDifferent numbers, same output\nwhen W is matched", fontsize=23, pad=24)
    fig.text(.5, .052, "Coordinate relation, not a token trajectory.", ha="center", fontsize=21, color="#64748B")
    fig.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, metadata={"Date": None})
    plt.close(fig)

if __name__ == "__main__":
    main()
