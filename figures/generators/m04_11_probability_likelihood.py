#!/usr/bin/env python3
"""Bernoulli probability in data direction versus likelihood in parameter direction."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":17,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-11-directions"})
    fig, axes = plt.subplots(1,2,figsize=(11,6.5),constrained_layout=True)
    fig.patch.set_facecolor("#F8FAFC")
    axes[0].bar([0,1],[.25,.75],color="#2563EB",width=.5)
    axes[0].set(xlim=(-.5,1.5),ylim=(0,1.05),xlabel="possible data x",ylabel="probability mass")
    axes[0].set_xticks([0,1]); axes[0].set_title("Fix p = 0.75\nMasses sum to 1",fontsize=18)
    p=np.linspace(0,1,201)
    axes[1].plot(p,p,color="#7C3AED",linewidth=3)
    axes[1].scatter([.75],[.75],color="#D97706",zorder=4)
    axes[1].set(xlim=(0,1),ylim=(0,1.05),xlabel="candidate parameter p",ylabel="L(p; x = 1)")
    axes[1].set_title("Fix observed x = 1\nArea over p = 1/2, not 1",fontsize=18)
    for ax in axes:
        ax.set_facecolor("#F8FAFC"); ax.grid(axis="y",color="#CBD5E1",linewidth=.7); ax.spines[["top","right"]].set_visible(False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"}); plt.close(fig)

if __name__ == "__main__": main()
