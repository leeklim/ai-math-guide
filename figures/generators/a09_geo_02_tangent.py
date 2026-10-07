"""Reproduce tangent velocities, coordinate components, and covector pairing."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, PURPLE, GREEN, ORANGE = "#2563EB", "#7C3AED", "#059669", "#D97706"
BG, GRID, GRAY = "#F8FAFC", "#D9E2EF", "#64748B"


def arrow(ax, origin, delta, color, style="-"):
    end = np.asarray(origin) + np.asarray(delta)
    ax.annotate("", xy=end, xytext=origin,
                arrowprops={"arrowstyle": "->", "color": color, "lw": 2.8,
                            "linestyle": style, "mutation_scale": 14, "shrinkA": 0, "shrinkB": 0}, zorder=6)


def plane(ax, xlim, ylim):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.set_xticks(np.arange(np.ceil(xlim[0]), xlim[1], 1))
    ax.set_yticks(np.arange(np.ceil(ylim[0]), ylim[1], 1))
    ax.grid(color=GRID)
    ax.axhline(0, color=GRAY, lw=1)
    ax.axvline(0, color=GRAY, lw=1)
    ax.set_xlabel("ambient x", fontsize=25)
    ax.set_ylabel("ambient y", fontsize=25)


def circle(ax):
    a = np.linspace(0, 2 * np.pi, 250)
    ax.plot(np.cos(a), np.sin(a), color=GRAY, lw=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    name = args.output.stem.removeprefix("A09-GEO-02-")
    plt.rcParams.update({"font.size": 26, "font.family": "DejaVu Sans",
                         "svg.fonttype": "none", "svg.hashsalt": "a09-geo-02",
                         "axes.spines.top": False, "axes.spines.right": False})
    wide = name in {"point-specific-tangents", "coordinate-components", "metric-gradients", "decoder-velocity"}
    if wide:
        fig, axes = plt.subplots(1, 2, figsize=(13.5, 8))
        fig.subplots_adjust(left=.09, right=.96, bottom=.27, top=.76, wspace=.43)
    else:
        fig, ax = plt.subplots(figsize=(7.2, 9))
        axes = [ax]
        fig.subplots_adjust(left=.20, right=.95, bottom=.35, top=.81)
    if name == "circle-velocity":
        ax = axes[0]
        plane(ax, (-1.4, 2.4), (-1.4, 1.65)); circle(ax)
        ax.plot([1, 1], [-1.3, 1.4], "--", color=BLUE, lw=1.8)
        arrow(ax, (1, 0), (0, 1), BLUE)
        arrow(ax, (1, 0), (1, 0), ORANGE, "--")
        ax.scatter([1], [0], color=PURPLE, s=45, zorder=7)
        ax.text(.2, 1.35, "v=(0,1)", color=BLUE, fontsize=27)
        ax.text(-.85, -.45, "p=(1,0)", color=PURPLE, fontsize=26, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
        ax.set_title("γ(t)=(cos t, sin t)\nVelocity at t=0", fontsize=27, pad=28)
        fig.text(.5, .105, "Blue line: TₚS¹ = span{(0,1)}\nOrange radial direction (1,0)\nis not tangent to the circle.", ha="center", fontsize=25)
    elif name == "velocity-not-chord":
        ax = axes[0]
        plane(ax, (-.45, 1.45), (-.3, 1.45)); circle(ax)
        t = .7
        p = np.array([1., 0.]); q = np.array([np.cos(t), np.sin(t)])
        a = np.linspace(0, t, 70)
        ax.plot(np.cos(a), np.sin(a), color=PURPLE, lw=4)
        arrow(ax, p, (0, 1), BLUE)
        arrow(ax, p, q - p, GREEN)
        ax.scatter([1], [0], color=PURPLE, s=40, zorder=7)
        ax.scatter([q[0]], [q[1]], facecolor=BG, edgecolor=GREEN, lw=2, s=65, zorder=7)
        ax.text(.08, 1.23, "velocity (0,1)", color=BLUE, fontsize=26)
        ax.text(-.37, .55, "q=γ(0.7)", color=GREEN, fontsize=25)
        ax.text(.57, -.2, "p=γ(0)", color=PURPLE, fontsize=25)
        ax.set_title("Instantaneous velocity\nversus a finite chord", fontsize=27, pad=28)
        fig.text(.5, .075, "q−p≈(−0.235,0.644)\nChord points into the circle.\nVelocity follows the tangent.", ha="center", fontsize=25)
    elif name == "point-specific-tangents":
        fig.subplots_adjust(bottom=.38)
        for ax, p, v, label in zip(axes, [(1, 0), (0, 1)], [(0, 1), (-1, 0)], ["p=(1,0)", "q=(0,1)"]):
            plane(ax, (-1.5, 1.5), (-1.5, 1.5)); circle(ax)
            if p[0] == 1:
                ax.plot([1, 1], [-1.4, 1.4], "--", color=BLUE, lw=2)
            else:
                ax.plot([-1.4, 1.4], [1, 1], "--", color=GREEN, lw=2)
            color = BLUE if p[0] == 1 else GREEN
            arrow(ax, p, v, color)
            ax.scatter([p[0]], [p[1]], color=PURPLE, s=40, zorder=7)
            ax.set_title(label + ("\nTₚS¹: vertical" if p[0] == 1 else "\nTqS¹: horizontal"), fontsize=25, pad=28)
        fig.text(.5, .09, "Tangent spaces belong to different base points.\nHere the chosen embedding displays both in the same ambient plane.", ha="center", fontsize=23)
    elif name == "coordinate-components":
        fig.set_size_inches(13.5, 10.5)
        fig.subplots_adjust(bottom=.37, top=.76)
        for ax, scaled in zip(axes, [False, True]):
            plane(ax, (-.3, 1.65), (-.3, 1.65))
            ax.set_xlabel("chosen ambient display x", fontsize=22)
            ax.set_ylabel("chosen ambient display y", fontsize=22)
            arrow(ax, (0, 0), (1, 1), GREEN)
            if scaled:
                arrow(ax, (0, 0), (.5, 0), BLUE)
                arrow(ax, (.5, 0), (.5, 0), BLUE)
                ax.text(.05, -.18, "2 × eᵤ", color=BLUE, fontsize=24)
                ax.set_title("Coordinates u=2x, v=y\nComponents (2,1)", fontsize=24, pad=28)
            else:
                arrow(ax, (0, 0), (1, 0), BLUE)
                ax.text(.16, -.18, "1 × eₓ", color=BLUE, fontsize=24)
                ax.set_title("Coordinates x,y\nComponents (1,1)", fontsize=24, pad=28)
            arrow(ax, (1, 0), (0, 1), PURPLE)
            ax.text(1.14, .4, "1 × eᵧ" if not scaled else "1 × eᵥ", color=PURPLE, fontsize=23, rotation=90)
            ax.text(.12, 1.28, "same vector (1,1)", color=GREEN, fontsize=23)
        fig.text(.5, .095, "New basis: eᵤ=(1/2,0), eᵥ=(0,1)\n2eᵤ+eᵥ = eₓ+eᵧ = (1,1)", ha="center", fontsize=25)
    elif name == "covector-levels":
        ax = axes[0]
        plane(ax, (-.4, 1.8), (-.4, 2.7))
        x, y = np.meshgrid(np.linspace(-.4, 1.8, 150), np.linspace(-.4, 2.7, 150))
        levels = ax.contour(x, y, 2*x-y, levels=[0, 1], colors=[GRAY], linewidths=1.8)
        ax.clabel(levels, fmt={0: "f=0", 1: "f=1"}, fontsize=24, manual=[(1.15, 2.3), (1.3, 1.6)])
        arrow(ax, (0, 0), (1, 1), BLUE)
        arrow(ax, (0, 0), (1, 2), GREEN)
        ax.text(.92, .68, "v=(1,1)", color=BLUE, fontsize=25, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
        ax.text(.04, 2.4, "w=(1,2)", color=GREEN, fontsize=25)
        ax.set_xlabel("x", fontsize=27); ax.set_ylabel("y", fontsize=27)
        ax.set_title("f(x,y)=2x−y\ndf reads a velocity", fontsize=27, pad=28)
        fig.text(.5, .095, "df(v)=2×1−1=1\ndf(w)=2×1−2=0\nw runs along a level set.", ha="center", fontsize=26)
    elif name == "metric-gradients":
        fig.subplots_adjust(bottom=.38)
        a = np.array([2., -1.])
        for ax, diagonal in zip(axes, [[1., 1.], [4., 1.]]):
            plane(ax, (-1.3, 2.7), (-1.6, 1.5))
            diagonal = np.array(diagonal)
            t = np.linspace(0, 2*np.pi, 200)
            ax.plot(np.cos(t)/np.sqrt(diagonal[0]), np.sin(t)/np.sqrt(diagonal[1]), color=GRAY, lw=2)
            w = a / diagonal
            arrow(ax, (0, 0), w, GREEN)
            title = "G=I" if diagonal[0] == 1 else "G=diag(4,1)"
            ax.set_title(title + f"\ngrad f=({w[0]:g},−1)", fontsize=25, pad=28)
            ax.text(-1.1, 1.12, "g(v,v)=1 boundary", color=GRAY, fontsize=22, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
        fig.text(.5, .08, "Same differential coefficients a=(2,−1): G·grad f=a\nFor test v=(1,1), both metrics give g(grad f,v)=df(v)=1.", ha="center", fontsize=23)
    elif name == "decoder-velocity":
        ax, bx = axes
        ax.set_xlim(-.1, 1.2); ax.set_ylim(-.7, 1)
        ax.axhline(0, color=GRAY, lw=2); ax.set_yticks([]); ax.set_xticks([0, .5, 1])
        arrow(ax, (.5, 0), (.5, 0), BLUE)
        ax.scatter([.5], [0], color=PURPLE, s=40, zorder=7)
        ax.text(.49, .32, "u=0.5", color=BLUE, fontsize=25)
        ax.text(.5, -.3, "z=0.5", ha="center", color=PURPLE, fontsize=25)
        ax.set_xlabel("latent z", fontsize=26)
        ax.set_title("Latent curve γ(t)=0.5+0.5t\nInput velocity u∈R¹", fontsize=23, pad=28)
        ax.spines["left"].set_visible(False)
        plane(bx, (-.15, 1.3), (-.15, 1.5))
        z = np.linspace(0, 1.2, 150)
        bx.plot(z, z*z, color=GRAY, lw=2)
        p = (.5, .25)
        arrow(bx, p, (.5, .5), BLUE)
        arrow(bx, p, (.5, .75), ORANGE, "--")
        bx.scatter([.5], [.25], color=PURPLE, s=40, zorder=7)
        bx.text(.03, 1.28, "instant: (0.5,0.5)", color=BLUE, fontsize=22, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
        bx.text(.03, 1.07, "finite: (0.5,0.75)", color=ORANGE, fontsize=22, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
        bx.set_xlabel("output x", fontsize=23); bx.set_ylabel("output y", fontsize=23)
        bx.set_title("Decoder F(z)=(z,z²)\nJ_F(0.5)u=(0.5,0.5)", fontsize=23, pad=28)
        fig.text(.5, .08, "J_F(0.5)=[1,1]ᵀ: R¹ → R²\nThe finite step from z=0.5 to z=1 adds a nonlinear remainder.", ha="center", fontsize=23)
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
