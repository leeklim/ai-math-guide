#!/usr/bin/env python3
"""Closed Bernoulli parameter space includes boundary MLEs."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":17,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-11-boundary"})
    p=np.linspace(0,1,401);fig,axes=plt.subplots(1,2,figsize=(11,6.5),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax,y,best,title in zip(axes,[(1-p)**4,p**4],[0,1],["Data (0, 0, 0, 0)\nMaximum at p = 0","Data (1, 1, 1, 1)\nMaximum at p = 1"]):
        ax.set_facecolor("#F8FAFC");ax.plot(p,y,color="#7C3AED",linewidth=3);ax.scatter([best],[1],color="#D97706",s=70,zorder=4);ax.set(xlim=(-.03,1.03),ylim=(-.03,1.08),xlabel="allowed p ∈ [0, 1]",ylabel="likelihood");ax.set_title(title,fontsize=18);ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
