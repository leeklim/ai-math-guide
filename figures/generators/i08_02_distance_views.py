"""Render the I08-02 fixed ReLU toy and analytic metric counterexamples."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt

parser = ArgumentParser()
parser.add_argument("--output", type=Path, required=True)
out = parser.parse_args().output
name = out.stem.removeprefix("I08-02-")
bg = "#F8FAFC"
blue, green, amber = "#2563EB", "#059669", "#D97706"
mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 26,
    "axes.labelsize": 24, "xtick.labelsize": 22, "ytick.labelsize": 22,
    "svg.fonttype": "none", "svg.hashsalt": "i08-02-" + name})

def prepare(ax):
    ax.set_facecolor(bg)
    ax.grid(color="#CBD5E1", alpha=.6)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)

if name == "same-output-grid":
    fig, ax = plt.subplots(figsize=(520/72, 720/72), facecolor=bg)
    fig.subplots_adjust(left=.20, right=.92, bottom=.37, top=.78)
    prepare(ax)
    grid = np.array([-2., -1., 0., 1., 2.])
    w1 = np.array([[1.], [-2.]])
    w2 = np.array([3., -1.])
    x = np.linspace(-2., 2., 201)[:, None]
    a = np.maximum(x @ w1.T, 0.) @ w2
    b = np.maximum(x @ w1[[1, 0]].T, 0.) @ w2[[1, 0]]
    assert np.allclose(a, b)
    ax.plot(x[:, 0], a, lw=4, color=blue, label="Network A")
    ax.plot(x[:, 0], b, lw=2, ls="--", color=green, label="Permuted B")
    ax.scatter(grid, np.where(grid >= 0, 3*grid, 2*grid), color=amber, s=65, zorder=4)
    ax.set(xlim=(-2.2, 2.2), ylim=(-4.8, 6.8), xticks=[-2, 0, 2], yticks=[-4, 0, 6],
           xlabel="Input x", ylabel="Output f(x)")
    title = "Different weights,\nsame output function"
    footer = "Fixed five-point grid: RMSE = 0"
    fig.legend(*ax.get_legend_handles_labels(), loc="center", bbox_to_anchor=(.55, .23),
               ncol=1, frameon=False, fontsize=24)
elif name == "distribution-support":
    fig, ax = plt.subplots(figsize=(520/72, 720/72), facecolor=bg)
    fig.subplots_adjust(left=.20, right=.92, bottom=.37, top=.78)
    prepare(ax)
    x = np.linspace(-2., 2., 401)
    a = np.zeros_like(x)
    b = np.maximum(np.abs(x)-1., 0.)
    ax.axvspan(-1., 1., color=blue, alpha=.08)
    ax.plot(x, a, lw=4, color=blue, label="f₁(x) = 0")
    ax.plot(x, b, lw=2, ls="--", color=green, label="f₂(x)")
    ax.text(-.86, .73, "P_X support", color=blue, fontsize=24)
    ax.set(xlim=(-2.2, 2.2), ylim=(-.15, 1.15), xticks=[-2, -1, 0, 1, 2],
           yticks=[0, 1], xlabel="Input x", ylabel="Output")
    title = "Zero distance on support;\ndifferent outside it"
    footer = "Analytic example, not model data"
    fig.legend(*ax.get_legend_handles_labels(), loc="center", bbox_to_anchor=(.55, .23),
               ncol=1, frameon=False, fontsize=24)
elif name == "output-metric-invariances":
    fig, axs = plt.subplots(1, 3, figsize=(1350/72, 770/72), facecolor=bg)
    fig.subplots_adjust(left=.06, right=.97, bottom=.37, top=.77, wspace=.40)
    logits = [np.array([1., 0.]), np.array([3., 2.]), np.array([2., 0.])]
    names = ["Reference", "Add the same offset", "Increase the gap"]
    probs = []
    for ax, z, heading in zip(axs, logits, names):
        prepare(ax)
        e = np.exp(z-z.max())
        prob = e/e.sum()
        probs.append(prob)
        ax.bar([0, 1], prob, color=[blue, green], width=.6)
        ax.set(ylim=(0, 1.05), xticks=[0, 1], xticklabels=["A", "B"], yticks=[0, .5, 1],
               xlabel="Token", ylabel="Probability")
        ax.set_title(heading, fontsize=27, pad=20)
        ax.text(.5, .95, "logits = " + str(tuple(int(value) for value in z)), fontsize=24,
                ha="center", transform=ax.transAxes)
    assert np.allclose(probs[0], probs[1]) and not np.allclose(probs[0], probs[2])
    title = "Logit change, probability change, and top-1 answer are different questions"
    footer = "All three choose token A. Offset preserves probabilities; a larger gap changes confidence."
    fig.text(.50, .25, "Offset: positive logit distance, zero probability difference", ha="center", fontsize=26, color=blue)
    fig.text(.50, .18, "Larger gap: positive probability difference, zero top-1 disagreement", ha="center", fontsize=26, color=green)
else:
    raise ValueError(name)
fig.suptitle(title, fontsize=28, y=.94, linespacing=1.45)
fig.text(.5, .08, footer, ha="center", fontsize=24, color="#475569")
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, format="svg", metadata={"Date": None, "Creator": "ai-math-guide"})
plt.close(fig)
