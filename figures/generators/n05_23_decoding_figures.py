"""Reproducible decoding plots for one fixed logit vector."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    name = args.output.stem.removeprefix("N05-23-")
    plt.rcParams.update({"font.size": 26, "font.family": "DejaVu Sans",
                         "svg.fonttype": "none", "svg.hashsalt": "n05-23",
                         "axes.spines.top": False, "axes.spines.right": False})
    z = np.array([2., 1.5, 0., -1.])
    def softmax(tau):
        e = np.exp((z - z.max()) / tau)
        return e / e.sum()
    bg = "#F8FAFC"
    if name == "temperature-distributions":
        fig, axes = plt.subplots(1, 3, figsize=(15, 7))
        fig.subplots_adjust(left=.125, right=.98, bottom=.19, top=.72, wspace=.32)
        for ax, tau in zip(axes, [.25, 1., 4.]):
            p = softmax(tau)
            n = np.searchsorted(np.cumsum(p), .75) + 1
            ax.set_facecolor(bg)
            ax.bar(np.arange(4), p, color="#7C3AED", zorder=3)
            ax.set_ylim(0, 1.04)
            ax.set_xticks(np.arange(4))
            ax.set_xlabel("token ID", fontsize=24)
            ax.set_title(f"τ={tau:g}\ntop-p=0.75 → {n} kept", fontsize=22, pad=18)
            ax.grid(axis="y", color="#D9E2EF", zorder=0)
            for i, value in enumerate(p):
                ax.text(i, value + .035, f"{value:.2f}", ha="center", fontsize=20)
        axes[0].set_ylabel("probability", fontsize=24)
        fig.suptitle("Same ordering; different concentration\nlogits = (2, 1.5, 0, −1)", fontsize=24, y=.97)
    elif name == "temperature-entropy":
        fig, ax = plt.subplots(figsize=(7.2, 9))
        fig.subplots_adjust(left=.21, right=.98, bottom=.14, top=.87)
        tau = np.geomspace(.05, 20, 180)
        entropy = [-np.sum((p := softmax(t)) * np.log(p)) for t in tau]
        ax.plot(tau, entropy, color="#7C3AED", lw=3)
        ax.axhline(np.log(4), color="#64748B", ls="--", lw=2)
        ax.text(.055, 1.31, "uniform: log 4", fontsize=23, color="#64748B")
        ax.set_xscale("log")
        ax.set_xticks([.1, 1, 10], [".1", "1", "10"])
        ax.set_ylim(0, 1.48)
        ax.set_yticks([0, .5, 1])
        ax.set_xlabel("temperature τ")
        ax.set_ylabel("entropy (nats)")
        ax.set_title("Fixed finite logits\nEntropy rises toward log 4", fontsize=24)
        ax.grid(color="#D9E2EF")
    elif name == "nucleus-cumulative":
        fig, ax = plt.subplots(figsize=(7.2, 9))
        fig.subplots_adjust(left=.21, right=.98, bottom=.17, top=.85)
        cumulative = np.cumsum(softmax(1))
        ax.plot(np.arange(1, 5), cumulative, "o-", color="#2563EB", lw=3, markersize=7)
        ax.axhline(.75, color="#D97706", ls="--", lw=2)
        ax.text(2.05, .67, "threshold 0.75", fontsize=23, color="#D97706")
        for x, val in zip(np.arange(1, 5), cumulative):
            ax.annotate(f"{val:.3f}", (x, val), xytext=(0, 15 if x < 4 else -31),
                        textcoords="offset points", ha="center", fontsize=25)
        ax.set_ylim(0, 1.12)
        ax.set_xlim(.6, 4.4)
        ax.set_xticks([1, 2, 3, 4])
        ax.set_yticks([0, .5, 1])
        ax.set_xlabel("number of top tokens", fontsize=24)
        ax.set_ylabel("original cumulative mass")
        ax.set_title("First crossing: two tokens\n0.558 < 0.75 < 0.897", fontsize=23)
        ax.grid(color="#D9E2EF")
    else:
        raise ValueError(name)
    fig.set_facecolor(bg)
    for ax in fig.axes:
        ax.set_facecolor(bg)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, metadata={"Date": None})
    plt.close(fig)

if __name__ == "__main__":
    main()
