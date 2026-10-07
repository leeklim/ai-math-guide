#!/usr/bin/env python3
"""Top-label calibration can miss errors among nonselected classes."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":19,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-15-full"})
    fig,axes=plt.subplots(1,2,figsize=(11,7),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC");classes=np.arange(1,4)
    for ax,q,p,title in zip(axes,[[.6,.3,.1],[.6,.1,.3]],[[.6,.1,.3],[.6,.3,.1]],["Group A: same full vector","Group B: different full vector"]):
        ax.set_facecolor("#F8FAFC");ax.bar(classes,q,color="#2563EB",width=.5,label="reported q");ax.scatter(classes,p,color="#D97706",marker="D",s=85,zorder=4,label="actual class frequency");ax.set_xticks(classes);ax.set(xlabel="class k",ylabel="probability / frequency",ylim=(0,.8));ax.set_title(title,fontsize=18);ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.15),frameon=False,fontsize=15)
    fig.suptitle("Both: top class 1, confidence .6, correctness .6\nNon-top class frequencies still disagree",fontsize=20,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
