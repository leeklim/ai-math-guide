#!/usr/bin/env python3
"""Generate the secant-to-tangent plot used in M01-03."""

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
            "font.size": 12.5,
            "svg.fonttype": "none",
            "svg.hashsalt": "mmi-m01-03",
        }
    )
    x = np.linspace(-0.2, 3.2, 300)
    y = x**2
    a = 1.2
    h = 1.0
    tangent = a**2 + 2 * a * (x - a)
    secant_slope = ((a + h) ** 2 - a**2) / h
    secant = a**2 + secant_slope * (x - a)

    fig, ax = plt.subplots(figsize=(8.0, 4.6), constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    ax.plot(x, y, color="#334155", linewidth=2.3, label=r"$f(x)=x^2$")
    ax.plot(x, secant, color="#D97706", linewidth=2, linestyle="--", label="Secant")
    ax.plot(x, tangent, color="#2563EB", linewidth=2, label="Tangent at a")
    ax.scatter([a, a + h], [a**2, (a + h) ** 2], color=["#2563EB", "#D97706"], zorder=5)
    ax.annotate("(a, f(a))", (a, a**2), xytext=(-58, -23), textcoords="offset points")
    ax.annotate("(a+h, f(a+h))", (a + h, (a + h) ** 2), xytext=(8, 10), textcoords="offset points")
    ax.annotate("h decreases", xy=(a + 0.42, (a + 0.42) ** 2), xytext=(2.55, 1.0),
                arrowprops={"arrowstyle": "->", "color": "#475569"}, color="#475569", fontsize=11)
    ax.axhline(0, color="#94A3B8", linewidth=0.8)
    ax.axvline(0, color="#94A3B8", linewidth=0.8)
    ax.set_xlim(-0.2, 3.2)
    ax.set_ylim(-1.0, 9.8)
    ax.set_xlabel("input x")
    ax.set_ylabel("output f(x)")
    ax.legend(frameon=False, loc="upper left")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(color="#CBD5E1", linewidth=0.6, alpha=0.7)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", metadata={"Date": None, "Creator": "mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
