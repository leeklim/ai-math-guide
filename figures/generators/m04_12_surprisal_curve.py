#!/usr/bin/env python3
"""Surprisal versus probability on its valid positive domain."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-12-surprisal"})
    p=np.linspace(.01,1,500);fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.plot(p,-np.log(p),color="#7C3AED",linewidth=3);ax.scatter([.25,.5,1],-np.log([.25,.5,1]),color="#D97706",s=70,zorder=4)
    ax.set(xlim=(0,1.04),ylim=(-.08,4.8),xlabel="outcome probability p",ylabel="surprisal −log p (nats)");ax.set_xticks([0,.25,.5,1]);ax.set_yticks([0,1,2,3,4]);ax.set_title("Rare outcome → larger surprisal\nProbability 0 is excluded",fontsize=24,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);fig.subplots_adjust(left=.22,right=.95,top=.84,bottom=.16)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
