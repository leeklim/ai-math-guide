"""Reproduce pullback pairings, singular stretch, and rank-zero caveats."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, PURPLE, GREEN, ORANGE = "#2563EB", "#7C3AED", "#059669", "#D97706"
BG, GRID, GRAY = "#F8FAFC", "#D9E2EF", "#64748B"


def plane(ax, lim, ylim=None):
    ax.set_xlim(*lim); ax.set_ylim(*(ylim or lim)); ax.set_aspect("equal")
    ax.set_xticks(np.arange(np.ceil(lim[0]), lim[1], 1))
    yr = ylim or lim
    ax.set_yticks(np.arange(np.ceil(yr[0]), yr[1], 1))
    ax.grid(color=GRID)
    ax.axhline(0, color=GRAY, lw=1); ax.axvline(0, color=GRAY, lw=1)


def arrow(ax, delta, color, style="-"):
    ax.annotate("", xy=delta, xytext=(0, 0),
                arrowprops={"arrowstyle": "->", "color": color, "lw": 2.8, "mutation_scale": 13,
                            "linestyle": style, "shrinkA": 0, "shrinkB": 0}, zorder=5)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    name = args.output.stem.removeprefix("A09-GEO-04-")
    plt.rcParams.update({"font.size": 26, "font.family": "DejaVu Sans",
                         "svg.fonttype": "none", "svg.hashsalt": "a09-geo-04",
                         "axes.spines.top": False, "axes.spines.right": False})
    t = np.linspace(0, 2*np.pi, 200)
    if name in {"pullback-pairing", "singular-stretch", "null-collapse"}:
        fig, axes = plt.subplots(1, 2, figsize=(13.5, 8))
        fig.subplots_adjust(left=.09, right=.96, bottom=.30, top=.75, wspace=.44)
        ax, bx = axes
    else:
        fig, ax = plt.subplots(figsize=(7.2, 9))
        fig.subplots_adjust(left=.27, right=.94, bottom=.30, top=.80)
        axes = [ax]
    if name == "pullback-pairing":
        for a in axes:
            plane(a, (-.45, 1.65))
        arrow(ax, (1, 0), BLUE); arrow(ax, (0, 1), PURPLE)
        arrow(bx, (1, 0), BLUE); arrow(bx, (1, 1), PURPLE)
        ax.set_title("Input tangent coordinates\nu=(1,0), v=(0,1)", fontsize=24, pad=25)
        bx.set_title("Output Euclidean plane\nJu=(1,0), Jv=(1,1)", fontsize=24, pad=25)
        ax.set_xlabel("z₁ velocity", fontsize=23); ax.set_ylabel("z₂ velocity", fontsize=23)
        bx.set_xlabel("x₁ velocity", fontsize=23); bx.set_ylabel("x₂ velocity", fontsize=23)
        fig.text(.5, .095, "J=[[1,1],[0,1]]   →   G_Z=JᵀJ=[[1,1],[1,2]]\nEuclidean uᵀv=0; pullback uᵀG_Zv=(Ju)ᵀ(Jv)=1.", ha="center", fontsize=23)
    elif name == "singular-stretch":
        plane(ax, (-1.5, 1.5)); plane(bx, (-2.7, 2.7), (-1.5, 1.5))
        ax.plot(np.cos(t), np.sin(t), color=GRAY, lw=2)
        bx.plot(2*np.cos(t), np.sin(t), color=GREEN, lw=2.5)
        arrow(ax, (1, 0), BLUE); arrow(ax, (0, 1), PURPLE)
        arrow(bx, (2, 0), BLUE); arrow(bx, (0, 1), PURPLE)
        ax.set_title("Euclidean unit input directions\nv₁=(1,0), v₂=(0,1)", fontsize=23, pad=25)
        bx.set_title("Image under J=diag(2,1)\nLengths σ₁=2, σ₂=1", fontsize=23, pad=25)
        ax.set_xlabel("latent velocity z₁", fontsize=22); ax.set_ylabel("latent velocity z₂", fontsize=22)
        bx.set_xlabel("output velocity x₁", fontsize=22); bx.set_ylabel("output velocity x₂", fontsize=22)
        fig.text(.5, .085, "G_Z eigenvalues: (4,1) = (σ₁²,σ₂²)\nFor F(z)=(2z₁,z₂,0), this is the output plane x₃=0.", ha="center", fontsize=24)
    elif name == "null-collapse":
        plane(ax, (-.45, 1.6), (-1.5, 1.6)); plane(bx, (-.45, 1.6))
        arrow(ax, (1, 0), BLUE); arrow(ax, (0, 1), PURPLE); arrow(ax, (1, -1), ORANGE)
        ax.set_title("Input: e₁, e₂, and e₁−e₂\nNull vector (1,−1) ≠ 0", fontsize=23, pad=25)
        arrow(bx, (1, 1), BLUE)
        bx.plot([0, 1], [0, 1], ":", color=PURPLE, lw=2.5, zorder=6)
        bx.scatter([0], [0], s=90, facecolor=BG, edgecolor=ORANGE, lw=2, zorder=7)
        bx.set_title("Equal Jacobian columns\nJe₁=Je₂=(1,1)", fontsize=23, pad=25)
        ax.set_xlabel("latent velocity z₁", fontsize=22); ax.set_ylabel("latent velocity z₂", fontsize=22)
        bx.set_xlabel("output velocity x₁", fontsize=22); bx.set_ylabel("output velocity x₂", fontsize=22)
        fig.text(.5, .085, "J=[[1,1],[1,1]]: J(e₁−e₂)=0\nA nonzero latent velocity has pullback squared length 0.", ha="center", fontsize=24)
    elif name == "cubic-first-order-null":
        z = np.linspace(-.55, .55, 200)
        ax.plot(z, z**3, color=PURPLE, lw=3)
        ax.axhline(0, color=BLUE, lw=2, linestyle="--")
        ax.scatter([0, .4], [0, .4**3], color=[BLUE, GREEN], s=55, zorder=6)
        ax.text(-.5, .13, "F(0.4)=0.064", color=GREEN, fontsize=25)
        ax.set_xlim(-.58, .58); ax.set_ylim(-.2, .2)
        ax.set_xticks([-.4, 0, .4]); ax.set_yticks([-.1, 0, .1])
        ax.grid(color=GRID)
        ax.set_xlabel("latent z", fontsize=27); ax.set_ylabel("output F(z)", fontsize=27)
        ax.set_title("F(z)=z³, F′(0)=0\nBlue tangent is horizontal", fontsize=26, pad=25)
        fig.text(.5, .075, "First-order change at 0: 0\nF(0.4)−F(0)=0.064\nThe finite output still changes.", ha="center", fontsize=25)
    elif name == "decoder-output-scale":
        plane(ax, (-4.6, 4.6), (-2.4, 2.6))
        ax.set_xticks([-4, -2, 0, 2, 4]); ax.set_yticks([-2, 0, 2])
        ax.plot(2*np.cos(t), np.sin(t), color=BLUE, lw=2)
        ax.plot(4*np.cos(t), 2*np.sin(t), color=GREEN, lw=2)
        arrow(ax, (4, 0), GREEN); arrow(ax, (2, 0), BLUE)
        ax.set_xlabel("output velocity x₁", fontsize=25); ax.set_ylabel("output velocity x₂", fontsize=25)
        ax.set_title("Same latent direction v=(1,0)\nF(z)=(2z₁,z₂), compare 2F", fontsize=25, pad=25)
        fig.text(.5, .225, "Blue: F    |    Green: 2F", ha="center", fontsize=24)
        fig.text(.5, .09, "Output velocity length: 2 → 4\nJacobian doubles; pullback matrix\nscales by 4, not by 2.", ha="center", fontsize=25)
    else:
        raise ValueError(name)
    fig.set_facecolor(BG)
    for a in fig.axes:
        a.set_facecolor(BG)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, metadata={"Date": None})
    plt.close(fig)


if __name__ == "__main__":
    main()
