"""Reproduce polar basis changes, parallel transport, and geodesic caveats."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, PURPLE, GREEN = "#2563EB", "#7C3AED", "#059669"
BG, GRID, GRAY = "#F8FAFC", "#D9E2EF", "#64748B"


def plane(ax, lim, ylim):
    ax.set_xlim(*lim); ax.set_ylim(*ylim); ax.set_aspect("equal")
    ax.set_xticks(np.arange(np.ceil(lim[0]), lim[1], 1)); ax.set_yticks(np.arange(np.ceil(ylim[0]), ylim[1], 1))
    ax.grid(color=GRID); ax.axhline(0, color=GRAY, lw=1); ax.axvline(0, color=GRAY, lw=1)
    ax.set_xlabel("Cartesian x", fontsize=24); ax.set_ylabel("Cartesian y", fontsize=24)


def arrow(ax, origin, delta, color):
    ax.annotate("", xy=np.array(origin)+np.array(delta), xytext=origin,
                arrowprops={"arrowstyle": "->", "color": color, "lw": 2.8, "mutation_scale": 13,
                            "shrinkA": 0, "shrinkB": 0}, zorder=5)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    name = args.output.stem.removeprefix("A09-GEO-05-")
    plt.rcParams.update({"font.size": 26, "font.family": "DejaVu Sans",
                         "svg.fonttype": "none", "svg.hashsalt": "a09-geo-05",
                         "axes.spines.top": False, "axes.spines.right": False})
    wide = name in {"transport-components", "geodesic-parameter", "straight-polar-trace"}
    if wide:
        fig, axes = plt.subplots(1, 2, figsize=(13.5, 8))
        fig.subplots_adjust(left=.09, right=.96, bottom=.38, top=.76, wspace=.43)
    else:
        fig, ax = plt.subplots(figsize=(7.2, 9))
        axes = [ax]
        fig.subplots_adjust(left=.25, right=.94, bottom=.31, top=.79)
    if name == "rotating-basis":
        ax = axes[0]
        plane(ax, (-1.35, 2.5), (-.45, 2.55))
        a = np.linspace(0, np.pi/2, 100)
        ax.plot(np.cos(a), np.sin(a), "--", color=GRAY, lw=2)
        for p, er, eth in [((1,0),(1,0),(0,1)), ((0,1),(0,1),(-1,0))]:
            arrow(ax, p, er, BLUE); arrow(ax, p, eth, PURPLE)
            ax.scatter([p[0]], [p[1]], color=GRAY, s=35, zorder=6)
        ax.text(1.07, 1.34, "θ=0", fontsize=26)
        ax.text(-1.25, 1.55, "θ=π/2", fontsize=26)
        ax.set_title("Polar basis on M=R²\nThe basis rotates with position", fontsize=25, pad=25)
        fig.text(.5, .08, "Blue ∂r; purple ∂θ at r=1\nY=∂r: polar components (1,0)\nare fixed; its direction changes.", ha="center", fontsize=25)
    elif name == "transport-components":
        for ax, p, label in zip(axes, [(1,0),(0,1)], ["θ=0: (Vʳ,Vᶿ)=(1,0)", "θ=π/2: (Vʳ,Vᶿ)=(0,−1)"]):
            plane(ax, (-1.3, 2.5), (-.5, 2))
            a = np.linspace(0, np.pi/2, 100)
            ax.plot(np.cos(a), np.sin(a), "--", color=GRAY, lw=2)
            arrow(ax, p, (1,0), GREEN)
            ax.scatter([p[0]], [p[1]], color=GRAY, s=35, zorder=6)
            ax.set_title(label + "\nCartesian V=(1,0)", fontsize=23, pad=25)
        fig.text(.5, .085, "Levi–Civita transport in the Euclidean plane keeps V constant.\nPolar components change because the coordinate basis rotates; ∇γ′V=0.", ha="center", fontsize=23)
    elif name == "geodesic-parameter":
        for ax, nonlinear in zip(axes, [False, True]):
            ax.set_xlim(-.12, 1.6); ax.set_ylim(-.45, .75)
            ax.set_xticks([0, .5, 1]); ax.set_yticks([])
            ax.plot([0,1], [0,0], color=GRAY, lw=3)
            time = np.array([0., .5, 1.])
            position = (time+time*time)/2 if nonlinear else time
            speed = .5+time if nonlinear else np.ones(3)
            for x, v in zip(position, speed):
                arrow(ax, (x,0), (.25*v,0), GREEN if nonlinear else BLUE)
            ax.scatter(position, np.zeros(3), color=GRAY, s=30, zorder=6)
            ax.spines["left"].set_visible(False)
            ax.set_xlabel("same line path, x∈[0,1]", fontsize=23)
            ax.set_title("x(t)=t: speed 1, x″=0" if not nonlinear else "x(s)=(s+s²)/2: x″=1", fontsize=23, pad=25)
        fig.text(.5, .10, "Cartesian Γ=0: only affine time gives zero acceleration.\nBoth trace the same segment and have length 1.\nVelocity arrows use display scale 1/4.", ha="center", fontsize=23)
    elif name == "straight-polar-trace":
        ax, bx = axes
        plane(ax, (-.3, 2.8), (-.25, 2))
        time = np.linspace(.4, 2.5, 200)
        ax.plot(time, np.ones_like(time), color=BLUE, lw=3)
        for t in [.5, 1, 2]:
            ax.plot([0,t], [0,1], ":", color=GRAY, lw=1.5)
            ax.scatter([t], [1], color=BLUE, s=35, zorder=6)
        arrow(ax, (1,1), (.5,0), GREEN)
        ax.set_title("Physical plane: γ(t)=(t,1)\nCartesian acceleration 0", fontsize=23, pad=25)
        r = np.sqrt(1+time*time); theta = np.arctan(1/time)
        bx.plot(r, theta, color=PURPLE, lw=3)
        for t in [.5, 1, 2]:
            bx.scatter([np.sqrt(1+t*t)], [np.arctan(1/t)], color=PURPLE, s=35, zorder=6)
        bx.set_xlim(1, 2.9); bx.set_ylim(.25, 1.3)
        bx.set_xticks([1,2]); bx.set_yticks([.5,1]); bx.grid(color=GRID)
        bx.set_xlabel("polar coordinate r", fontsize=23); bx.set_ylabel("polar coordinate θ", fontsize=23)
        bx.set_title("Coordinate trace (r,θ)\nA curved coordinate plot", fontsize=23, pad=25)
        fig.text(.5, .10, "r(t)=√(1+t²), θ(t)=arctan(1/t), t>0\nThe curved coordinate trace is not curvature of the plane.\nGreen velocity arrow: Cartesian (1,0), display scale 1/2.", ha="center", fontsize=23)
    elif name == "polar-acceleration-cancellation":
        ax = axes[0]
        t = np.linspace(.3, 2.5, 200)
        value = 1/(1+t*t)**1.5
        ax.plot(t, value, color=BLUE, lw=3, label="r″=1/r³")
        ax.plot(t, -value, "--", color=PURPLE, lw=3, label="−r(θ′)²")
        ax.plot(t, np.zeros_like(t), color=GREEN, lw=3, label="sum=0")
        ax.set_xlim(.25, 2.6); ax.set_ylim(-1.1, 1.1)
        ax.set_xticks([.5,1,2]); ax.set_yticks([-1,0,1]); ax.grid(color=GRID)
        ax.set_xlabel("time t", fontsize=27); ax.set_ylabel("radial acceleration term", fontsize=25)
        ax.set_title("Same Cartesian straight line\nPolar radial geodesic equation", fontsize=25, pad=25)
        ax.legend(loc="upper right", fontsize=24, frameon=False)
        fig.text(.5, .08, "At t=1: r=√2, θ′=−1/2\nr″≈0.3536; −r(θ′)²≈−0.3536\nCovariant radial acceleration: 0", ha="center", fontsize=25)
    elif name == "local-not-global-shortest":
        ax = axes[0]
        plane(ax, (-1.4,1.4), (-1.4,1.4))
        a = np.linspace(0,np.pi/2,120)
        b = np.linspace(0,-3*np.pi/2,200)
        ax.plot(np.cos(a),np.sin(a), color=BLUE, lw=3)
        ax.plot(np.cos(b),np.sin(b), "--", color=PURPLE, lw=3)
        ax.scatter([1,0],[0,1],color=GREEN,s=45,zorder=6)
        ax.text(.08,.25,"short\nπ/2",color=BLUE,fontsize=25)
        ax.text(-.85,-.35,"long\n3π/2",color=PURPLE,fontsize=25)
        ax.set_xlabel("ambient x",fontsize=25); ax.set_ylabel("ambient y",fontsize=25)
        ax.set_title("Constant-speed arcs on S¹\nBoth are geodesic segments",fontsize=25,pad=25)
        fig.text(.5,.08,"Same endpoints, induced metric\nThe long segment is not globally\nshortest: 3π/2 > π/2.",ha="center",fontsize=25)
    else:
        raise ValueError(name)
    fig.set_facecolor(BG)
    for ax in fig.axes:
        ax.set_facecolor(BG)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,metadata={"Date":None})
    plt.close(fig)


if __name__ == "__main__":
    main()
