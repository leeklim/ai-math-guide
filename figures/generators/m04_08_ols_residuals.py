#!/usr/bin/env python3
"""Exact least-squares fitted line and signed observed residuals."""
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
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-08-ols-residuals"})
    x, y = np.array([0., 1., 2.]), np.array([1., 3., 2.])
    beta = np.linalg.lstsq(np.column_stack([np.ones(3), x]), y, rcond=None)[0]
    fitted = beta[0]+beta[1]*x
    xx = np.linspace(-.3, 2.3, 101)
    fig, ax = plt.subplots(figsize=(7.2, 9))
    fig.subplots_adjust(left=.23, right=.95, bottom=.39, top=.82)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(xx, beta[0]+beta[1]*xx, color="#7C3AED", linewidth=2.6, label="fit: 1.5 + 0.5x")
    ax.scatter(x, y, color="#2563EB", s=90, zorder=5, label="observed target")
    ax.scatter(x, fitted, marker="s", color="#059669", s=45, zorder=5, label="fitted target")
    for value, observed, pred in zip(x, y, fitted):
        visible_endpoint = observed-np.sign(observed-pred)*.08
        ax.annotate("", (value, visible_endpoint), xytext=(value, pred),
                    arrowprops={"arrowstyle": "-|>", "color": "#D97706", "linewidth": 2.2, "mutation_scale": 7})
    ax.plot([], [], color="#D97706", linewidth=2.2, label="signed residual")
    ax.set(xlim=(-.3, 2.3), ylim=(.5, 3.5), xlabel="input x", ylabel="target / prediction")
    ax.set_xticks([0, 1, 2])
    ax.grid(color="#CBD5E1", linewidth=.7)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Residual = observed − fitted\nIllustrative OLS sample", fontsize=25, fontweight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, -.25), frameon=False, fontsize=24)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
