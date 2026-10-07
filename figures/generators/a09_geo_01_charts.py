"""Reproduce coordinate charts, their cuts, and sampled local neighborhoods."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, PURPLE, GREEN, ORANGE = "#2563EB", "#7C3AED", "#059669", "#D97706"
BG, GRID, GRAY = "#F8FAFC", "#D9E2EF", "#64748B"


def plane(ax):
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-1.35, 1.35)
    ax.set_aspect("equal")
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.grid(color=GRID)
    ax.axhline(0, color=GRAY, lw=1)
    ax.axvline(0, color=GRAY, lw=1)
    ax.set_xlabel("ambient x", fontsize=23)
    ax.set_ylabel("ambient y", fontsize=23)
    a = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(a), np.sin(a), "--", color=GRAY, lw=1.5)


def interval(ax, label, start=-1):
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-.7, .7)
    ax.set_yticks([])
    ax.set_xticks([-1, 0, 1])
    ax.axhline(0, color=GRAY, lw=1.5)
    ax.plot([start, 1], [0, 0], color=GREEN, lw=5)
    ax.scatter([start, 1], [0, 0], s=130, facecolor=BG, edgecolor=GREEN, lw=2.5, zorder=5)
    ax.set_xlabel(label, fontsize=25, labelpad=15)
    for spine in ["left", "top", "right"]:
        ax.spines[spine].set_visible(False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    name = args.output.stem.removeprefix("A09-GEO-01-")
    plt.rcParams.update({"font.size": 24, "font.family": "DejaVu Sans",
                         "svg.fonttype": "none", "svg.hashsalt": "a09-geo-01",
                         "axes.spines.top": False, "axes.spines.right": False})
    if name == "open-arc-coordinate":
        fig, axes = plt.subplots(1, 2, figsize=(13, 7))
        fig.subplots_adjust(left=.09, right=.95, bottom=.32, top=.78, wspace=.43)
        ax, bx = axes
        plane(ax)
        a = np.linspace(.002, np.pi - .002, 200)
        ax.plot(np.cos(a), np.sin(a), color=BLUE, lw=4)
        ax.scatter([-1, 1], [0, 0], facecolor=BG, edgecolor=BLUE, s=130, lw=2.5, zorder=5)
        ax.scatter([.6], [.8], color=PURPLE, s=90, zorder=5)
        ax.plot([.6, .6], [.8, 0], ":", color=PURPLE, lw=2)
        ax.text(-.75, 1.14, "U: y > 0", color=BLUE, fontsize=24)
        ax.text(-.9, -.25, "p=(0.6,0.8)", color=PURPLE, fontsize=23, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
        ax.set_title("Open in the circle\nd=1 inside ambient D=2", fontsize=23, pad=25)
        interval(bx, "coordinate u=x")
        bx.scatter([.6], [0], color=PURPLE, s=100, zorder=5)
        bx.text(.6, .18, "φ(p)=0.6", ha="center", color=PURPLE, fontsize=23)
        bx.set_title("Open interval (−1,1)\nOne number per point", fontsize=23, pad=25)
        fig.text(.5, .06, "φ(x,y)=x     |     φ⁻¹(u)=(u, √(1−u²))", ha="center", fontsize=25)
    elif name == "overlap-transition":
        fig, axes = plt.subplots(1, 3, figsize=(15, 7))
        fig.subplots_adjust(left=.07, right=.96, bottom=.25, top=.72, wspace=.55)
        ax, bx, cx = axes
        interval(ax, "first coordinate u=x", start=0)
        ax.scatter([.6], [0], s=100, color=BLUE, zorder=5)
        ax.text(.6, .22, "u=0.6", color=BLUE, ha="center")
        ax.set_title("φ(U∩V)=(0,1)", fontsize=22, pad=22)
        plane(bx)
        a = np.linspace(.002, np.pi / 2 - .002, 100)
        bx.plot(np.cos(a), np.sin(a), color=PURPLE, lw=5)
        bx.scatter([.6], [.8], s=100, color=PURPLE, zorder=6)
        bx.text(0, -.3, "same point p", ha="center", fontsize=22, color=PURPLE, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
        bx.set_title("U∩V: x>0, y>0", fontsize=22, pad=22)
        interval(cx, "second coordinate v=y", start=0)
        cx.scatter([.8], [0], s=100, color=GREEN, zorder=5)
        cx.text(.8, .22, "v=0.8", color=GREEN, ha="center")
        cx.set_title("ψ(U∩V)=(0,1)", fontsize=22, pad=22)
        fig.text(.35, .92, "φ⁻¹: restore p", ha="center", fontsize=24, color=BLUE)
        fig.text(.69, .92, "ψ: read y", ha="center", fontsize=24, color=GREEN)
        bx.annotate("", xy=(.43, .83), xytext=(.28, .83), xycoords="figure fraction",
                    arrowprops={"arrowstyle": "->", "color": BLUE, "lw": 2, "mutation_scale": 13})
        bx.annotate("", xy=(.80, .83), xytext=(.63, .83), xycoords="figure fraction",
                    arrowprops={"arrowstyle": "->", "color": GREEN, "lw": 2, "mutation_scale": 13})
        fig.text(.5, .06, "Transition: v=√(1−u²)     |     0.6 → 0.8", ha="center", fontsize=25)
    elif name == "angle-cut":
        fig, axes = plt.subplots(2, 1, figsize=(7.2, 11), gridspec_kw={"height_ratios": [1.9, 1]})
        fig.subplots_adjust(left=.19, right=.94, bottom=.23, top=.88, hspace=.65)
        ax, bx = axes
        plane(ax)
        delta = .12
        ax.scatter([np.cos(delta)] * 2, [np.sin(delta), -np.sin(delta)], color=[BLUE, GREEN], s=90, zorder=5)
        ax.scatter([1], [0], facecolor=BG, edgecolor=ORANGE, s=100, lw=2, zorder=4)
        ax.text(-.65, .35, "p: θ=0.12", color=BLUE, fontsize=27, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
        ax.text(-.65, -.4, "q: θ≈6.16", color=GREEN, fontsize=27, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
        ax.set_title("Nearby points on S¹\nCut at (1,0)", fontsize=27, pad=25)
        bx.set_xlim(-.35, 2 * np.pi + .35)
        bx.set_ylim(-.65, .8)
        bx.set_yticks([])
        bx.set_xticks([0, np.pi, 2 * np.pi], ["0", "π", "2π"])
        bx.axhline(0, color=GRAY, lw=2)
        bx.scatter([delta, 2 * np.pi - delta], [0, 0], color=[BLUE, GREEN], s=90, zorder=5)
        bx.text(.12, .25, "p", color=BLUE, ha="center", fontsize=28)
        bx.text(2 * np.pi - .12, .25, "q", color=GREEN, ha="center", fontsize=28)
        bx.set_title("Far apart as θ values", fontsize=27, pad=20)
        bx.set_xlabel("angle coordinate θ", fontsize=27, labelpad=15)
        bx.spines["left"].set_visible(False)
        fig.text(.5, .055, "One cut cannot cover the circle\nwith continuous coordinates.", ha="center", fontsize=25)
    elif name == "switch-chart":
        fig, axes = plt.subplots(1, 2, figsize=(13, 8))
        fig.subplots_adjust(left=.09, right=.96, bottom=.28, top=.78, wspace=.43)
        x, y = .98, np.sqrt(1 - .98 ** 2)
        for ax, coordinate, color in zip(axes, ["x", "y"], [BLUE, GREEN]):
            plane(ax)
            a = np.linspace(.001, np.pi - .001, 200) if coordinate == "x" else np.linspace(-np.pi/2 + .001, np.pi/2 - .001, 200)
            ax.plot(np.cos(a), np.sin(a), color=color, lw=4)
            ax.scatter([x], [y], color=PURPLE, s=100, zorder=6)
            ax.text(-1.12, -.3, "p≈(0.98,0.199)", color=PURPLE, fontsize=22, bbox={"facecolor": BG, "edgecolor": "none", "pad": 2})
            if coordinate == "x":
                ax.plot([x, x], [0, y], ":", color=BLUE, lw=2)
                ax.set_title("Upper arc: coordinate x\ny=√(1−x²)", fontsize=23, pad=25)
                ax.text(-1.18, 1.14, "dy/dx≈−4.92", color=BLUE, fontsize=23)
            else:
                ax.plot([0, x], [y, y], ":", color=GREEN, lw=2)
                ax.set_title("Right arc: coordinate y\nx=√(1−y²)", fontsize=23, pad=25)
                ax.text(-1.18, 1.14, "dx/dy≈−0.203", color=GREEN, fontsize=23)
        fig.text(.5, .10, "As x→1: the x-chart derivative diverges.\nThe y-chart remains regular near (1,0).", ha="center", fontsize=25)
    elif name == "cloud-neighborhoods":
        fig, axes = plt.subplots(1, 2, figsize=(13, 7.5))
        fig.subplots_adjust(left=.09, right=.96, bottom=.30, top=.79, wspace=.44)
        rng = np.random.default_rng(31)
        a = np.linspace(0, 2 * np.pi, 95, endpoint=False)
        r = 1 + rng.normal(0, .035, len(a))
        samples = np.column_stack((r * np.cos(a), r * np.sin(a)))
        for ax, radius in zip(axes, [.18, .65]):
            plane(ax)
            d = np.linalg.norm(samples - np.array([0, 1]), axis=1)
            ax.scatter(samples[:, 0], samples[:, 1], s=18, color=GRAY, zorder=3)
            ax.scatter(samples[d < radius, 0], samples[d < radius, 1], s=36, color=BLUE, zorder=4)
            c = np.linspace(0, 2 * np.pi, 160)
            ax.plot(radius * np.cos(c), 1 + radius * np.sin(c), color=ORANGE, lw=2)
            ax.set_ylim(-1.25, 1.8)
            ax.set_title(f"Same samples: radius {radius}\nSelected neighbors in blue", fontsize=23, pad=24)
        fig.text(.5, .055, "Dashed circle: proposed latent structure, not a fitted proof\nNeighborhood scale changes which points enter the analysis.", ha="center", fontsize=23)
    elif name == "sphere-local-dimension":
        fig = plt.figure(figsize=(7.2, 9))
        ax = fig.add_subplot(111, projection="3d")
        fig.subplots_adjust(left=.06, right=.94, bottom=.25, top=.85)
        longitude = np.linspace(0, 2 * np.pi, 24)
        latitude = np.linspace(-np.pi / 2, np.pi / 2, 13)
        a, b = np.meshgrid(longitude, latitude)
        ax.plot_wireframe(np.cos(b) * np.cos(a), np.cos(b) * np.sin(a), np.sin(b), color=GRAY, lw=.8, alpha=.65)
        a, b = np.meshgrid(np.linspace(.2, 1.25, 13), np.linspace(.15, .9, 12))
        ax.plot_surface(np.cos(b) * np.cos(a), np.cos(b) * np.sin(a), np.sin(b), color=BLUE, alpha=.7)
        ax.set_box_aspect([1, 1, 1])
        ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1]); ax.set_zticks([-1, 0, 1])
        ax.tick_params(labelsize=22)
        ax.set_xlabel("x", fontsize=27, labelpad=12)
        ax.set_ylabel("y", fontsize=27, labelpad=12)
        ax.set_zlabel("z", fontsize=27, labelpad=12)
        ax.set_title("Sphere: ambient D=3\nA local patch needs d=2", fontsize=26, pad=24)
        ax.view_init(elev=23, azim=42)
        fig.text(.5, .065, "Two parameters locate a patch point:\nlongitude and latitude\naway from the poles.", ha="center", fontsize=24)
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
