#!/usr/bin/env python3
"""Fixed two-outcome entropy has deterministic endpoints and a uniform maximum."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-12-binary"})
    p=np.linspace(.001,.999,600);h=-p*np.log(p)-(1-p)*np.log1p(-p)
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC");ax.plot(np.r_[0,p,1],np.r_[0,h,0],color="#7C3AED",linewidth=3);ax.scatter([0,.5,1],[0,np.log(2),0],color="#D97706",s=75,zorder=4)
    ax.set(xlim=(-.03,1.03),ylim=(-.025,.77),xlabel="mass p on first outcome",ylabel="entropy (nats)");ax.set_xticks([0,.5,1]);ax.set_yticks([0,.2,.4,.6]);ax.set_title("Same two outcomes throughout\nUniform p = 1/2 maximizes H",fontsize=24,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    ax.text(.5,.73,"log 2 ≈ 0.693",ha="center",fontsize=24,color="#065F46");fig.subplots_adjust(left=.2,right=.95,top=.84,bottom=.16)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
