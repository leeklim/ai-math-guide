#!/usr/bin/env python3
"""One-hot target selects exactly the observed class log-loss contribution."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":17,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-11-categorical"})
    p=np.array([.1,.8,.1]);q=np.array([0,1,0]);classes=np.arange(1,4)
    fig,axes=plt.subplots(1,2,figsize=(11,6.5),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    axes[0].bar(classes,p,color=["#CBD5E1","#2563EB","#CBD5E1"],width=.6);axes[0].set(ylim=(0,1),ylabel="predicted probability");axes[0].set_title("Observed class y = 2\np = (0.1, 0.8, 0.1)",fontsize=18)
    axes[1].bar(classes,-q*np.log(p),color="#059669",width=.6);axes[1].set(ylim=(0,.3),ylabel="−qₖ log pₖ");axes[1].set_title("One-hot q = (0, 1, 0)\nOnly class 2 contributes ≈ 0.223",fontsize=18)
    for ax in axes:ax.set_facecolor("#F8FAFC");ax.set_xticks(classes);ax.set_xlabel("class k");ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
