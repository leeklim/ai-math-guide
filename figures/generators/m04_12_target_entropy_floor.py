#!/usr/bin/env python3
"""A fixed nondegenerate target gives a positive cross-entropy floor."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-12-floor"})
    r=np.linspace(.01,.99,500);ce=-.75*np.log(r)-.25*np.log1p(-r);h=-.75*np.log(.75)-.25*np.log(.25)
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.plot(r,ce,color="#7C3AED",linewidth=3,label="cross entropy H(p,q)");ax.axhline(h,color="#059669",linestyle="--",linewidth=2,label="target entropy ≈ 0.562");ax.fill_between(r,h,ce,color="#DBEAFE");ax.scatter([.75],[h],color="#D97706",s=70,zorder=4)
    ax.set(xlim=(0,1),ylim=(0,3.7),xlabel="model first-class mass q₁",ylabel="average loss (nats)");ax.set_xticks([0,.5,.75,1]);ax.set_title("Fix target p = (0.75, 0.25)\nBest q = p; loss remains positive",fontsize=24,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=22);fig.subplots_adjust(left=.2,right=.95,top=.84,bottom=.29)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
