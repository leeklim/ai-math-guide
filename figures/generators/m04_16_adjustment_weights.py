#!/usr/bin/env python3
"""Exact binary confounding example: observed versus common-population weights."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":18,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-16-adjustment"})
    fig,axes=plt.subplots(1,2,figsize=(11,7),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    axes[0].bar([0,1,2],[.8,.2,.5],color="#2563EB",width=.5,label="Z=0 mass");axes[0].bar([0,1,2],[.2,.8,.5],bottom=[.8,.2,.5],color="#D97706",width=.5,label="Z=1 mass");axes[0].set_xticks([0,1,2],labels=["X=0 group","X=1 group","target"]);axes[0].set(ylim=(0,1.1),ylabel="confounder composition");axes[0].set_title("Different observed Z weights\nSame target: p(Z)= (.5,.5)",fontsize=18)
    x=np.array([0,1]);axes[1].bar(x-.17,[.2,.7],color="#7C3AED",width=.32,label="observed means");axes[1].bar(x+.17,[.35,.55],color="#059669",width=.32,label="adjusted means");axes[1].set_xticks(x,labels=["X=0","X=1"]);axes[1].set(ylim=(0,1),ylabel="mean outcome");axes[1].set_title("Observed contrast .50\nAdjusted contrast .20",fontsize=19)
    for ax in axes:ax.set_facecolor("#F8FAFC");ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.15),frameon=False,fontsize=15)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
