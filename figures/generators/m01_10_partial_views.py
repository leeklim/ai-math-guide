"""Reproduce M01-10 numeric views selected by output name."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

p = ArgumentParser(); p.add_argument("--output", type=Path, required=True)
out = p.parse_args().output
name = out.stem.removeprefix("M01-10-")
mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 16,
                    "svg.fonttype": "none", "svg.hashsalt": "mmi-m01-10-" + name})
blue, green, purple, orange = "#2563EB", "#059669", "#7C3AED", "#D97706"
bg = "#F8FAFC"
pair = name in {"coordinate-slopes", "rescaled-input", "loss-slices", "range-comparison"}
if name == "surface-and-slice":
    fig = plt.figure(figsize=(8.6, 8.8), facecolor=bg)
    ax = fig.add_subplot(111, projection="3d", proj_type="ortho")
    ax.set_facecolor(bg)
    fig.subplots_adjust(left=.08, right=.9, bottom=.18, top=.9)
    x, y = np.meshgrid(np.linspace(0, 3, 36), np.linspace(0, 4, 36))
    ax.plot_surface(x, y, x*x+x*y, color=green, alpha=.22, edgecolor="#CBD5E1", linewidth=.25)
    q = np.linspace(0, 3, 200)
    ax.plot(q, np.full_like(q, 3), q*q+3*q, color=blue, lw=4)
    ax.scatter([2], [3], [10], color=orange, s=70, depthshade=False)
    ax.set(xlabel="Input x", ylabel="Input y", zlabel="Output z", xticks=[0, 1, 2, 3], yticks=[0, 2, 4], zticks=[0, 10, 20])
    ax.xaxis.labelpad = 18; ax.yaxis.labelpad = 18; ax.zaxis.labelpad = 18
    ax.view_init(elev=22, azim=-58)
    title = "A scalar output becomes height above the input plane"
    footer = "f(x,y) = x² + xy; blue slice fixes y = 3; point (2,3,10)."
else:
    fig, axes = plt.subplots(2 if pair else 1, 1, figsize=(8.6, 8.8 if pair else 6.8), facecolor=bg)
    axs = np.atleast_1d(axes)
    fig.subplots_adjust(left=.19, right=.94, bottom=.21 if pair else .24, top=.87, hspace=.26)
    for ax in axs:
        ax.set_facecolor(bg); ax.grid(color="#CBD5E1", alpha=.7, linewidth=.8)
        ax.set_axisbelow(True); ax.spines[["top", "right"]].set_visible(False)
        ax.spines[["left", "bottom"]].set_color("#64748B"); ax.tick_params(colors="#334155")
    ax = axs[0]
    if name == "fixed-slice-family":
        x = np.linspace(-1.5, 1.5, 300)
        for y, col, sty in [(1, blue, ":"), (2, green, "--"), (3, purple, "-")]:
            ax.plot(x, y*x*x+3*y*y, color=col, lw=3, ls=sty, label=f"Fix y = {y}: f = {y}x² + {3*y*y}")
            ax.scatter([1], [y+3*y*y], color=col, zorder=5)
        ax.set(xlabel="Varying input x", ylabel="Slice output f(x,y)", ylim=(0, 49))
        ax.legend(loc="upper left", frameon=False, fontsize=16)
        title = "A fixed value is a coefficient, not a deleted variable"
        footer = "At x = 1, the x-direction slopes are 2, 4 and 6."
    elif name == "coordinate-slopes":
        x = np.linspace(.2, 1.8, 300)
        ax.plot(x, 2*x*x+12, color=blue, lw=3, label="Fix y = 2: 2x² + 12")
        ax.plot(x, 14+4*(x-1), color=purple, lw=2, ls="--", label="Tangent slope = 4")
        ax.scatter([1], [14], color=orange, zorder=5)
        ax.set(xlabel="Input x (y stays 2)", ylabel="Output", ylim=(11, 23))
        ax.legend(loc="upper left", frameon=False, fontsize=16)
        bottom = axs[1]; y = np.linspace(1.2, 2.8, 300)
        bottom.plot(y, y+3*y*y, color=green, lw=3, label="Fix x = 1: y + 3y²")
        bottom.plot(y, 14+13*(y-2), color=purple, lw=2, ls="--", label="Tangent slope = 13")
        bottom.scatter([2], [14], color=orange, zorder=5)
        bottom.set(xlabel="Input y (x stays 1)", ylabel="Output", ylim=(2, 38))
        bottom.legend(loc="upper left", frameon=False, fontsize=16)
        title = "Two slices pass through one point with different slopes"
        footer = "f(x,y) = x²y + 3y²; f(1,2) = 14; partial slopes 4 and 13."
    elif name == "rescaled-input":
        m = np.linspace(0, 2, 200)
        ax.plot(m, 4*m, color=blue, lw=3); ax.scatter([1], [4], color=orange, zorder=5)
        ax.set(xlabel="Distance coordinate (m)", ylabel="Illustrative score", ylim=(0, 10), xticks=[0, 1, 2])
        ax.text(.12, 8.5, "Slope = 4 score / m", color=blue, fontsize=17)
        bottom = axs[1]
        bottom.plot(100*m, 4*m, color=green, lw=3); bottom.scatter([100], [4], color=orange, zorder=5)
        bottom.set(xlabel="Same distance coordinate (cm)", ylabel="Same score", ylim=(0, 10), xticks=[0, 100, 200])
        bottom.text(12, 8.5, "Slope = 0.04 score / cm", color=green, fontsize=17)
        title = "Changing the coordinate unit changes the numeric slope"
        footer = "1 m and 100 cm denote the same input; both produce score 4."
    elif name == "zero-local-slope":
        x = np.linspace(-1.5, 1.5, 300)
        ax.plot(x, x*x, color=green, lw=3, label="Slice y = 0: f(x,0) = x²")
        ax.axhline(0, color=purple, ls="--", lw=2, label="Tangent slope at origin = 0")
        ax.scatter([-1, 0, 1], [1, 0, 1], color=orange, zorder=5)
        ax.set(xlabel="Input x (y = 0)", ylabel="Output f(x,y) = x² + y²", ylim=(-.3, 3.6))
        ax.legend(loc="upper left", frameon=False, fontsize=16)
        title = "A zero first-order slope does not mean a flat neighborhood"
        footer = "At (0,0), both partial slopes are 0; at (1,0), the output is 1."
    elif name == "loss-slices":
        w = np.linspace(.5, 2.5, 300)
        ax.plot(w, (2*w-4)**2, color=blue, lw=3, label="Fix b = 1: loss = (2w − 4)²")
        ax.plot(w[w <= 1.5], 4-8*(w[w <= 1.5]-1), color=purple, lw=2, ls="--", label="Tangent slope = −8")
        ax.scatter([1], [4], color=orange, zorder=5)
        ax.set(xlabel="Parameter w (b stays 1)", ylabel="Squared loss", ylim=(-1, 14))
        ax.legend(loc="upper right", frameon=False, fontsize=16)
        bottom = axs[1]; b = np.linspace(0, 4, 300)
        bottom.plot(b, (b-3)**2, color=green, lw=3, label="Fix w = 1: loss = (b − 3)²")
        q = np.linspace(0, 2.2, 120); bottom.plot(q, 4-4*(q-1), color=purple, lw=2, ls="--", label="Tangent slope = −4")
        bottom.scatter([1], [4], color=orange, zorder=5)
        bottom.set(xlabel="Parameter b (w stays 1)", ylabel="Squared loss", ylim=(-1, 14))
        bottom.legend(loc="upper right", frameon=False, fontsize=16)
        title = "Parameter partials are slopes of different loss slices"
        footer = "x = 2, target y = 5, (w,b) = (1,1): prediction 3, loss 4."
    elif name == "range-comparison":
        fig.subplots_adjust(left=.29)
        ax.barh([1, 0], [1, 100], color=[blue, green], height=.45)
        ax.set(yticks=[1, 0], yticklabels=["x slope", "y slope"], xlabel="Numeric partial slope", xlim=(0, 120))
        bottom = axs[1]; bottom.barh([1, 0], [100, 1], color=[blue, green], height=.45)
        bottom.set(yticks=[1, 0], yticklabels=["delta x = 100", "delta y = 0.01"], xlabel="Output change over stated input range", xlim=(0, 120))
        title = "Numeric slope and allowed change can rank differently"
        footer = "s(x,y) = x + 100y: output changes 100 and 1 over the stated ranges."
    else:
        raise ValueError(name)
fig.suptitle(title, fontsize=20, y=.95)
fig.text(.5, .075 if pair or name == "surface-and-slice" else .09, footer, ha="center", fontsize=16, color="#475569")
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, format="svg", metadata={"Date": None, "Creator": "mmi"})
plt.close(fig)
