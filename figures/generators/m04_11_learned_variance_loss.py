#!/usr/bin/env python3
"""Learned Gaussian variance trades residual scaling against log variance."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-11-learned"})
    v=np.linspace(.4,12,500);normal=.5*np.log(2*np.pi*v);scaled=2/v
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    for values,color,label in [(normal,"#7C3AED","log normalization"),(scaled,"#2563EB","scaled residual²"),(normal+scaled,"#059669","total NLL")]:ax.plot(v,values,color=color,linewidth=3,label=label)
    ax.axvline(4,color="#D97706",linestyle="--");ax.scatter([4],[.5*np.log(8*np.pi)+.5],color="#D97706",zorder=4)
    ax.set(xlim=(.4,12),ylim=(0,6),xlabel="learned variance σ²",ylabel="loss term");ax.set_xticks([1,4,8,12]);ax.set_title("Fixed residual y − prediction = 2\nNLL minimum at σ² = 4",fontsize=24,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=24);fig.subplots_adjust(left=.18,right=.95,top=.84,bottom=.34)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
