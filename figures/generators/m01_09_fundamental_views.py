"""Reproduce M01-09 figures with their output file names."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

p = ArgumentParser()
p.add_argument("--output", type=Path, required=True)
out = p.parse_args().output
name = out.stem.removeprefix("M01-09-")
mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 16,
                    "svg.fonttype": "none", "svg.hashsalt": "mmi-m01-09-" + name})
blue, green, purple, orange = "#2563EB", "#059669", "#7C3AED", "#D97706"
bg = "#F8FAFC"
pair = name in {"accumulation-derivative", "area-endpoints", "net-change", "same-integral-paths"}
fig, axes = plt.subplots(2 if pair else 1, 1, figsize=(8.6, 8.8 if pair else 6.8), facecolor=bg)
axs = np.atleast_1d(axes)
fig.subplots_adjust(left=.19, right=.94, bottom=.21 if pair else .24,
                    top=.87, hspace=.26)
for ax in axs:
    ax.set_facecolor(bg)
    ax.grid(color="#CBD5E1", alpha=.7, linewidth=.8)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#64748B")
    ax.tick_params(colors="#334155")
ax = axs[0]

if name == "thin-strip-average":
    t = np.linspace(.3, 1.8, 300)
    ax.plot(t, t + 1, color=green, lw=3, label="f(t) = t + 1")
    q = np.linspace(1, 1.3, 80)
    ax.fill_between(q, 0, q + 1, color=blue, alpha=.18)
    ax.plot([1, 1.3, 1.3, 1, 1], [0, 0, 2, 2, 0], color=purple, lw=2, ls="--", label="Rectangle: height f(1) = 2")
    ax.axhline(2.15, color=orange, ls=":", lw=2, label="Actual average height = 2.15")
    ax.set(xlim=(.3, 1.8), ylim=(0, 4.1), xlabel="Integration input t", ylabel="Height f(t)")
    ax.legend(loc="upper left", frameon=False, fontsize=16)
    title = "A thin area divided by its width is an average height"
    footer = "x = 1, h = 0.3: added area = 0.645; area / h = 2.15."
elif name == "accumulation-derivative":
    t = np.linspace(1, 2.2, 300)
    ax.plot(t, t*t+2, color=green, lw=3)
    ax.fill_between(t[t <= 2], 0, t[t <= 2]**2+2, color=green, alpha=.18)
    ax.scatter([2], [6], color=orange, zorder=5)
    ax.set(ylabel="Integrand f(t) = t² + 2", ylim=(0, 7.4), xticks=[1, 1.5, 2])
    bottom = axs[1]
    bottom.plot(t, t**3/3+2*t-7/3, color=purple, lw=3)
    bottom.plot(t, 6*(t-2)+13/3, color=blue, ls="--", lw=2, label="Tangent at x = 2: slope 6")
    bottom.scatter([1, 2], [0, 13/3], color=orange, zorder=5)
    bottom.set(xlabel="Upper endpoint x", ylabel="Accumulation A(x)", xticks=[1, 1.5, 2], ylim=(-.6, 6.4))
    bottom.legend(loc="upper left", frameon=False, fontsize=16)
    title = "The height above becomes the slope below"
    footer = "A(x) = integral from 1 to x of (t² + 2) d t; A′(2) = f(2) = 6."
elif name == "antiderivative-family":
    x = np.linspace(-1.3, 1.8, 300)
    for c, col, style in [(2, blue, ":"), (0, green, "--"), (-1, purple, "-")]:
        ax.plot(x, x*x+c, color=col, lw=3, ls=style, label="F(x) = x² " + ("+ 2" if c == 2 else "− 1" if c == -1 else ""))
        ax.plot([.45, 1.55], [1+c-1.1, 1+c+1.1], color=col, lw=1.8, ls="-.")
    ax.scatter([1], [0], color=orange, zorder=5)
    ax.set(xlabel="Input x", ylabel="Antiderivative height", ylim=(-1.5, 7))
    ax.legend(loc="upper left", frameon=False, fontsize=16)
    title = "Vertical shifts do not change the derivative"
    footer = "All slopes at x = 1 are 2; A(1) = 0 selects A(x) = x² − 1."
elif name == "area-endpoints":
    x = np.linspace(0, 2, 300)
    ax.plot(x, 3*x*x-2*x+1, color=green, lw=3)
    ax.fill_between(x, 0, 3*x*x-2*x+1, color=green, alpha=.18)
    ax.text(1.15, 1.25, "Integral = 6", fontsize=19, color=green)
    ax.set(ylabel="f(x) = 3x² − 2x + 1", ylim=(0, 10), xticks=[0, 1, 2])
    bottom = axs[1]
    bottom.plot(x, x**3-x*x+x, color=purple, lw=3)
    bottom.scatter([0, 2], [0, 6], color=orange, zorder=5)
    bottom.axhline(0, color="#64748B", lw=1)
    bottom.axhline(6, color="#64748B", ls="--", lw=1)
    bottom.text(.1, 6.3, "F(2) = 6; F(0) = 0", fontsize=17, color=purple)
    bottom.set(xlabel="Input x", ylabel="F(x) = x³ − x² + x", ylim=(-.5, 8), xticks=[0, 1, 2])
    title = "Area above equals the change in the antiderivative below"
    footer = "Integral from 0 to 2 = F(2) − F(0) = 6 − 0."
elif name == "log-branches":
    for i, col, style in [(-1, blue, "--"), (1, green, "-")]:
        x = i*np.linspace(.1, 3, 300)
        ax.plot(x, np.log(np.abs(x)), color=col, ls=style, lw=3, label="x < 0 branch" if i < 0 else "x > 0 branch")
    ax.axvline(0, color=orange, ls=":", lw=2, label="x = 0 is excluded")
    ax.set(xlabel="Input x", ylabel="F(x) = log |x|", xlim=(-3.2, 3.2), ylim=(-2.6, 3.4))
    ax.legend(loc="upper left", frameon=False, fontsize=16)
    title = "The logarithmic primitive has two separate domains"
    footer = "F′(x) = 1 / x on each side, not across an interval containing 0."
elif name == "net-change":
    t = np.linspace(0, 2, 300)
    v = t-1
    ax.plot(t, v, color=green, lw=3)
    ax.fill_between(t, 0, v, where=t <= 1, color=blue, alpha=.18, hatch="///")
    ax.fill_between(t, 0, v, where=t >= 1, color=green, alpha=.18)
    ax.axhline(0, color="#64748B", lw=1)
    ax.set(ylabel="Illustrative velocity v(t)", ylim=(-1.3, 1.3), xticks=[0, 1, 2])
    bottom = axs[1]
    bottom.plot(t, .5*t*t-t, color=purple, lw=3)
    bottom.scatter([0, 1, 2], [0, -.5, 0], color=orange, zorder=5)
    bottom.set(xlabel="Time t", ylabel="Position p(t) − p(0)", ylim=(-.7, .35), xticks=[0, 1, 2])
    title = "Returning to the start is zero net change, not zero travel"
    footer = "Illustration: v(t) = t − 1; net change 0; total distance 1."
elif name == "same-integral-paths":
    a = np.linspace(0, 1, 300)
    ax.plot(a, np.full_like(a, 2), color=blue, lw=3, label="Path A: s′ = 2")
    ax.plot(a, 4*a, color=green, lw=3, ls="--", label="Path B: s′ = 4 alpha")
    ax.set(ylabel="Local score change rate", ylim=(0, 6.6), xticks=[0, .5, 1])
    ax.legend(loc="upper left", frameon=False, fontsize=16)
    bottom = axs[1]
    bottom.plot(a, 2*a, color=blue, lw=3, label="s = 2 alpha")
    bottom.plot(a, 2*a*a, color=green, lw=3, ls="--", label="s = 2 alpha²")
    bottom.scatter([0, 1], [0, 2], color=orange, zorder=5)
    bottom.set(xlabel="Scalar path parameter alpha", ylabel="Score with s(0) = 0", ylim=(-.2, 3.5), xticks=[0, .5, 1])
    bottom.legend(loc="upper left", frameon=False, fontsize=16)
    title = "Equal integrals do not determine the intermediate curve"
    footer = "Both integrals from 0 to 1 equal 2; the rates differ along the path."
elif name == "exponential-area":
    x = np.linspace(-.12, .95, 300)
    q = np.linspace(0, np.log(2), 120)
    ax.plot(x, np.exp(x), color=green, lw=3, label="f(x) = F(x) = exp(x)")
    ax.fill_between(q, 0, np.exp(q), color=green, alpha=.18)
    ax.scatter([0, np.log(2)], [1, 2], color=orange, zorder=5)
    ax.set(xlabel="Input x", ylabel="Exponential height", ylim=(0, 3.8), xticks=[0, np.log(2)], xticklabels=["0", "log 2"])
    ax.legend(loc="upper left", frameon=False, fontsize=16)
    ax.text(.15, .65, "Integral = 1", fontsize=20, color=green)
    title = "A curved area from an endpoint difference"
    footer = "Integral from 0 to log 2 of exp(x) = exp(log 2) − exp(0) = 1."
else:
    raise ValueError(name)
fig.suptitle(title, fontsize=20, y=.95)
fig.text(.5, .075 if pair else .09, footer, ha="center", fontsize=16, color="#475569")
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, format="svg", metadata={"Date": None, "Creator": "mmi"})
plt.close(fig)
