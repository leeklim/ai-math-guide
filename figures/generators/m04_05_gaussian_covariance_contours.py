#!/usr/bin/env python3
"""Plot genuine Gaussian equal-density contours and covariance axes."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-05-gaussian-cov"})
    mean = np.array([1.0, -0.5])
    sigma = np.array([[1.0, 0.7], [0.7, 1.0]])
    xx, yy = np.meshgrid(np.linspace(-4, 6, 201), np.linspace(-5, 4, 181))
    centered = np.stack([xx-mean[0], yy-mean[1]], axis=-1)
    quadratic = np.einsum("...i,ij,...j->...", centered, np.linalg.inv(sigma), centered)
    fig, ax = plt.subplots(figsize=(7.6, 7.4), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    contours = ax.contour(xx, yy, quadratic, levels=[1, 4, 9], colors="#7C3AED", linewidths=1.7)
    ax.clabel(contours, fmt=lambda value: f"{value:g}", fontsize=12)
    ax.scatter(*mean, color="#059669", s=75, zorder=5, label="mean (1, −0.5)")
    for direction, eigenvalue, color in [(np.array([1, 1])/np.sqrt(2), 1.7, "#2563EB"),
                                         (np.array([1, -1])/np.sqrt(2), 0.3, "#D97706")]:
        endpoint = mean + 2*np.sqrt(eigenvalue)*direction
        ax.annotate("", endpoint, xytext=mean,
                    arrowprops={"arrowstyle": "-|>", "color": color, "linewidth": 2, "mutation_scale": 7})
        ax.plot([], [], color=color, linewidth=2, label=f"level-4 semi-axis: 2√{eigenvalue:g}")
    ax.set(xlim=(-4, 6), ylim=(-5, 4), xlabel="X₁", ylabel="X₂")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(color="#CBD5E1", linewidth=0.7)
    ax.set_title("Gaussian covariance sets contour direction and scale\nΣ = [[1, 0.7], [0.7, 1]]", fontsize=15, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), frameon=False, fontsize=12)
    ax.spines[["top", "right"]].set_visible(False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
