#!/usr/bin/env python3
"""Equal predictive entropy does not imply equal correctness."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":18,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-12-correctness"})
    fig,axes=plt.subplots(1,2,figsize=(11,6.5),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax,p,title in zip(axes,[[.9,.1],[.1,.9]],["Predict A: correct","Predict B: incorrect"]):
        ax.set_facecolor("#F8FAFC");ax.bar([0,1],p,color=["#2563EB","#7C3AED"],width=.5);ax.set_xticks([0,1],labels=["A (true)","B"]);ax.set(ylim=(0,1.1),ylabel="predictive probability");ax.set_title(f"{title}\nEntropy ≈ 0.325 nats",fontsize=19);ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    fig.suptitle("Same observed label A; same entropy, different correctness",fontsize=20,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
