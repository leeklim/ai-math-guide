#!/usr/bin/env python3
"""Changing a density at a null point differs from missing a positive mass region."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":17,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-13-null-region"})
    fig,axes=plt.subplots(1,2,figsize=(11,7),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax in axes:ax.set_facecolor("#F8FAFC");ax.plot([0,1],[1,1],color="#2563EB",linewidth=3,label="p: uniform [0,1]");ax.set(xlim=(-.04,1.04),ylim=(-.15,2.5),xlabel="outcome x",ylabel="density");ax.set_xticks([0,.5,1]);ax.set_yticks([0,1,2]);ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    axes[0].plot([0,1],[1,1],"--",color="#7C3AED",linewidth=2,label="q: same except x=.5");axes[0].scatter([.5],[1],s=120,facecolor="#F8FAFC",edgecolor="#7C3AED",linewidth=2,zorder=5);axes[0].scatter([.5],[0],color="#7C3AED",s=70,zorder=5);axes[0].set_title("One changed density value\nP({0.5}) = 0; same distribution",fontsize=17)
    axes[1].plot([0,.5,.5,1],[2,2,0,0],color="#7C3AED",linewidth=3,label="q: uniform [0,.5]");axes[1].fill_between([.5,1],[0,0],[1,1],color="#FFEDD5");axes[1].set_title("A missing region (.5,1]\np mass = 1/2; forward KL = ∞",fontsize=17)
    for ax in axes:ax.legend(loc="upper center",bbox_to_anchor=(.5,-.15),frameon=False,fontsize=14)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
