"""Reproduce metric unit sets, curve lengths, and coordinate changes."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, PURPLE, GREEN, ORANGE = "#2563EB", "#7C3AED", "#059669", "#D97706"
BG, GRID, GRAY = "#F8FAFC", "#D9E2EF", "#64748B"


def plane(ax, lim=(-1.5, 1.5), ylim=None):
    ax.set_xlim(*lim); ax.set_ylim(*(ylim or lim)); ax.set_aspect("equal")
    ax.set_xticks(np.arange(np.ceil(lim[0]), lim[1], 1))
    yr = ylim or lim
    ax.set_yticks(np.arange(np.ceil(yr[0]), yr[1], 1))
    ax.grid(color=GRID)
    ax.axhline(0, color=GRAY, lw=1)
    ax.axvline(0, color=GRAY, lw=1)


def arrow(ax, start, delta, color):
    ax.annotate("", xy=np.array(start)+np.array(delta), xytext=start,
                arrowprops={"arrowstyle": "->", "color": color, "lw": 2.8, "mutation_scale": 13,
                            "shrinkA": 0, "shrinkB": 0}, zorder=5)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    name = args.output.stem.removeprefix("A09-GEO-03-")
    plt.rcParams.update({"font.size": 26, "font.family": "DejaVu Sans",
                         "svg.fonttype": "none", "svg.hashsalt": "a09-geo-03",
                         "axes.spines.top": False, "axes.spines.right": False})
    t = np.linspace(0, 2*np.pi, 200)
    if name == "positive-definite":
        fig, axes = plt.subplots(1, 3, figsize=(15, 7.5))
        fig.subplots_adjust(left=.065, right=.97, bottom=.25, top=.70, wspace=.35)
        for ax in axes:
            plane(ax)
            ax.set_xlabel("v₁", fontsize=25); ax.set_ylabel("v₂", fontsize=25)
        axes[0].plot(.5*np.cos(t), np.sin(t), color=GREEN, lw=3)
        axes[0].set_title("G=diag(4,1)\nPositive definite", fontsize=23, pad=25)
        axes[0].text(0, 1.25, "Q(v)=1 boundary", ha="center", fontsize=21, color=GREEN, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
        axes[1].plot([-1, -1], [-1.5, 1.5], color=ORANGE, lw=2)
        axes[1].plot([1, 1], [-1.5, 1.5], color=ORANGE, lw=2)
        arrow(axes[1], (0, 0), (0, 1), BLUE)
        axes[1].set_title("G=diag(1,0)\nDegenerate: not a metric", fontsize=23, pad=25)
        axes[2].plot(np.cosh(np.linspace(-1, 1, 100)), np.sinh(np.linspace(-1, 1, 100)), color=ORANGE, lw=2)
        axes[2].plot(-np.cosh(np.linspace(-1, 1, 100)), np.sinh(np.linspace(-1, 1, 100)), color=ORANGE, lw=2)
        arrow(axes[2], (0, 0), (0, 1), BLUE)
        axes[2].set_title("G=diag(1,−1)\nIndefinite: not a metric", fontsize=23, pad=25)
        fig.text(.20, .10, "Every nonzero v: Q(v)>0", ha="center", fontsize=22)
        fig.text(.52, .10, "v=(0,1): Q(v)=0", ha="center", fontsize=22)
        fig.text(.83, .10, "v=(0,1): Q(v)=−1", ha="center", fontsize=22)
        fig.text(.5, .04, "Q(v)=vᵀGv    |    The latter two violate positive definiteness.", ha="center", fontsize=23)
    elif name == "basis-gram-matrix":
        fig, axes = plt.subplots(1, 2, figsize=(13, 8))
        fig.subplots_adjust(left=.09, right=.94, bottom=.25, top=.76, wspace=.4)
        ax, bx = axes
        plane(ax, (-.4, 2.8), (-.4, 1.8))
        arrow(ax, (0, 0), (2, 0), BLUE); arrow(ax, (0, 0), (1, 1), PURPLE)
        ax.text(.35, -.22, "b₁=(2,0)", color=BLUE, fontsize=25)
        ax.text(.4, 1.3, "b₂=(1,1)", color=PURPLE, fontsize=25)
        ax.set_xlabel("ambient x", fontsize=23); ax.set_ylabel("ambient y", fontsize=23)
        ax.set_title("Euclidean inner product\nChosen coordinate basis", fontsize=24, pad=25)
        bx.axis("off")
        table = bx.table(cellText=[[4, 2], [2, 2]], rowLabels=["b₁", "b₂"], colLabels=["b₁", "b₂"], cellLoc="center", rowLoc="center", bbox=[.14, .12, .76, .65])
        table.auto_set_font_size(False); table.set_fontsize(26)
        for cell in table.get_celld().values():
            cell.set_edgecolor(GRID); cell.set_facecolor(BG)
        bx.set_title("Gᵢⱼ=g(bᵢ,bⱼ)\nRows and columns are basis indices", fontsize=23, pad=25)
        fig.text(.5, .08, "G₁₂=G₂₁=2: symmetry    |    G=[[4,2],[2,2]]\nCoordinates c=(1,1) represent b₁+b₂=(3,1), with cᵀGc=10.", ha="center", fontsize=23)
    elif name == "weighted-norm":
        fig, axes = plt.subplots(2, 1, figsize=(7.2, 12))
        fig.subplots_adjust(left=.20, right=.94, bottom=.28, top=.86, hspace=.8)
        plane(axes[0], (-1.2, 2.6), (-1.2, 2.6))
        plane(axes[1], (-.4, 2.6), (-.4, 2.6))
        axes[0].plot(.5*np.cos(t), np.sin(t), color=GRAY, lw=2)
        arrow(axes[0], (0, 0), (1, 2), BLUE)
        axes[0].text(.15, 2.25, "v=(1,2)", color=BLUE, fontsize=27)
        axes[0].set_title("G=diag(4,1)\nMetric unit boundary in gray", fontsize=25, pad=25)
        axes[0].set_xlabel("v₁", fontsize=26); axes[0].set_ylabel("v₂", fontsize=26)
        arrow(axes[1], (0, 0), (2, 2), GREEN)
        axes[1].text(.1, 2.25, "(2v₁,v₂)=(2,2)", color=GREEN, fontsize=25)
        axes[1].set_title("Weighted Euclidean display", fontsize=25, pad=25)
        axes[1].set_xlabel("2v₁", fontsize=26); axes[1].set_ylabel("v₂", fontsize=26)
        fig.text(.5, .06, "Squared norm: 4×1²+2²=8\nNorm: √8=2√2\nFirst-axis unit length: 2.", ha="center", fontsize=26)
    elif name == "position-dependent-units":
        fig, axes = plt.subplots(1, 2, figsize=(13, 8))
        fig.subplots_adjust(left=.09, right=.95, bottom=.40, top=.75, wspace=.42)
        for ax, x in zip(axes, [0, 1]):
            plane(ax, (-1.4, 1.6))
            ax.plot(np.cos(t)/np.sqrt(1+x*x), np.sin(t), color=GRAY, lw=2)
            arrow(ax, (0, 0), (1, 0), BLUE)
            ax.set_xlabel("velocity v₁", fontsize=24); ax.set_ylabel("velocity v₂", fontsize=24)
            ax.set_title(f"Base point coordinate x={x}\nG(x)=diag(1+x²,1)", fontsize=24, pad=25)
            ax.text(-1.2, 1.16, "same v=(1,0)", color=BLUE, fontsize=24, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
        fig.text(.5, .07, "At x=0: ‖v‖g=1     |     At x=1: ‖v‖g=√2\nAxes show tangent velocities,\nnot base-point positions.", ha="center", fontsize=23)
    elif name == "path-versus-distance":
        fig, ax = plt.subplots(figsize=(7.2, 9))
        fig.subplots_adjust(left=.18, right=.96, bottom=.28, top=.81)
        plane(ax, (-.3, 2.3), (-.4, 1.65))
        a = np.linspace(np.pi, 0, 150)
        ax.plot(1+np.cos(a), np.sin(a), color=PURPLE, lw=3)
        ax.plot([0, 2], [0, 0], color=BLUE, lw=3)
        ax.scatter([0, 2], [0, 0], s=40, color=GREEN, zorder=6)
        ax.text(.37, 1.25, "arc length: π", color=PURPLE, fontsize=27)
        ax.text(.13, -.25, "straight length: 2", color=BLUE, fontsize=25)
        ax.set_title("Same endpoints, different paths\nEuclidean metric G=I", fontsize=25, pad=25)
        ax.set_xlabel("x", fontsize=27); ax.set_ylabel("y", fontsize=27)
        fig.text(.5, .09, "Curve length belongs to a path.\nDistance takes the infimum\nover paths: d((0,0),(2,0))=2.", ha="center", fontsize=25)
    elif name == "reparameterized-length":
        fig, axes = plt.subplots(2, 2, figsize=(13, 10), gridspec_kw={"height_ratios": [.7, 1.6]})
        fig.subplots_adjust(left=.095, right=.95, bottom=.25, top=.87, wspace=.33, hspace=.55)
        s = np.linspace(0, 1, 200)
        times = np.linspace(0, 1, 5)
        for col, nonlinear in enumerate([False, True]):
            upper, lower = axes[:, col]
            values = (times+times*times)/2 if nonlinear else times
            upper.set_xlim(-.12, 1.12); upper.set_ylim(-.35, .6)
            upper.plot([0, 1], [0, 0], color=GREEN, lw=3)
            upper.scatter(values, np.zeros(5), color=BLUE, s=65, zorder=4)
            upper.set_yticks([]); upper.set_xticks([0, .5, 1])
            upper.spines["left"].set_visible(False)
            upper.set_xlabel("same spatial path x∈[0,1]", fontsize=22)
            upper.set_title("γ(t)=(t,0)" if not nonlinear else "γ̃(s)=((s+s²)/2,0)", fontsize=24, pad=25)
            speed = np.ones_like(s) if not nonlinear else .5+s
            lower.plot(s, speed, color=PURPLE, lw=3)
            lower.fill_between(s, speed, color=PURPLE, alpha=.12)
            lower.set_xlim(0, 1); lower.set_ylim(0, 1.8)
            lower.set_xticks([0, .5, 1]); lower.set_yticks([1, 1.5])
            lower.set_xlabel("time t" if not nonlinear else "new time s", fontsize=24)
            lower.set_ylabel("metric speed", fontsize=24)
            lower.grid(color=GRID)
            lower.text(.12, .25, "area=1", fontsize=26, color=PURPLE)
        fig.text(.5, .06, "Five equally spaced times give different spatial spacing.\nThe speed changes, but ∫speed × d(time)=1 in both parameterizations.", ha="center", fontsize=23)
    elif name == "coordinate-versus-metric":
        fig, axes = plt.subplots(1, 3, figsize=(15, 8))
        fig.subplots_adjust(left=.065, right=.97, bottom=.26, top=.74, wspace=.39)
        configurations = [(1, [1, 1], "Original x,y", "length √2"), (2, [.25, 1], "New u=2x, v=y", "same length √2"), (2, [1, 1], "Same u,v; choose G=I", "changed length √5")]
        for ax, (x, g, title, length) in zip(axes, configurations):
            plane(ax, (-2.4, 2.8), (-1.4, 1.8))
            ax.plot(np.cos(t)/np.sqrt(g[0]), np.sin(t)/np.sqrt(g[1]), color=GRAY, lw=2)
            arrow(ax, (0, 0), (x, 1), BLUE)
            ax.set_xlabel("x" if x == 1 else "u", fontsize=25)
            ax.set_ylabel("y" if x == 1 else "v", fontsize=25)
            ax.set_title(title + "\n" + length, fontsize=22, pad=25)
            ax.text(-2.1, 1.4, "G=diag(1/4,1)" if g[0] == .25 else "G=I", fontsize=22, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
        fig.text(.5, .085, "Coordinate change: components and metric transform together.\nMetric change: keep coordinates fixed and choose a different length rule.", ha="center", fontsize=23)
    else:
        raise ValueError(name)
    fig.set_facecolor(BG)
    for ax in fig.axes:
        ax.set_facecolor(BG)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, metadata={"Date": None})
    plt.close(fig)


if __name__ == "__main__":
    main()
