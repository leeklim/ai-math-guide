#!/usr/bin/env python3
"""Standard-normal and df-nine t density, full view and enlarged tail."""
import argparse
import math
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14, "svg.fonttype": "none", "svg.hashsalt": "mmi-m04-09-t-normal"})
    fig, axes = plt.subplots(2, 1, figsize=(7.8, 8.2), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    nu = 9
    for ax, bounds in zip(axes, [(-4, 4), (1.5, 4)]):
        x = np.linspace(*bounds, 601)
        normal = np.exp(-x*x/2)/np.sqrt(2*np.pi)
        t_pdf = math.gamma((nu+1)/2)/(np.sqrt(nu*np.pi)*math.gamma(nu/2))*(1+x*x/nu)**(-(nu+1)/2)
        ax.set_facecolor("#F8FAFC")
        ax.plot(x, normal, color="#2563EB", linewidth=2.4, label="standard normal")
        ax.plot(x, t_pdf, color="#7C3AED", linewidth=2.4, label="t, degrees of freedom 9")
        ax.set(xlim=bounds, xlabel="standardized statistic", ylabel="density")
        ax.grid(color="#CBD5E1", linewidth=.7)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_title("Full density shapes", fontsize=16, fontweight="bold")
    axes[0].legend(loc="upper right", frameon=False, fontsize=11)
    axes[1].axvline(1.96, color="#2563EB", linestyle="--", linewidth=1.3)
    axes[1].axvline(2.262, color="#7C3AED", linestyle="--", linewidth=1.3)
    axes[1].set_title("Right tail enlarged; 97.5% cutoffs 1.96 and 2.262", fontsize=14)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
