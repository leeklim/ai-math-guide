#!/usr/bin/env python3
"""Entropy separates probability weights, surprisal, and contributions."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":17,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-12-weights"})
    p=np.array([.75,.25]);surprise=-np.log(p)
    fig,axes=plt.subplots(1,3,figsize=(13,6),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax,values,title,label in zip(axes,[p,surprise,p*surprise],["Weights p(x)","Surprisal −log p(x)","Contributions\np × surprisal"],["probability","nats per outcome","weighted nats"]):
        ax.set_facecolor("#F8FAFC");ax.bar([1,2],values,color=["#2563EB","#D97706"],width=.6);ax.set_xticks([1,2],labels=["common","rare"]);ax.set_ylabel(label);ax.set_title(title,fontsize=18);ax.set_ylim(0,values.max()*1.35)
        for x,y in zip([1,2],values):ax.text(x,y+.035*values.max(),f"{y:.3f}",ha="center",va="bottom",fontsize=17)
        ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    fig.suptitle(f"p = (0.75, 0.25); entropy = sum of contributions ≈ {(p*surprise).sum():.3f}",fontsize=20,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
