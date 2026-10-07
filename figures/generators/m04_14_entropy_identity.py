#!/usr/bin/env python3
"""Exact two-variable entropy decomposition for a noisy fair-bit copy."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-14-identity"})
    conditional=-.8*np.log(.8)-.2*np.log(.2);information=np.log(2)-conditional
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.barh([2,1],[conditional,conditional],height=.38,color="#2563EB",label="H(X ∣ Y)");ax.barh([2,1,0],[information]*3,left=[conditional,conditional,conditional],height=.38,color="#7C3AED",label="I(X;Y)");ax.barh([2,0],[conditional,conditional],left=[conditional+information]*2,height=.38,color="#059669",label="H(Y ∣ X)")
    ax.set(xlim=(0,1.35),ylim=(-.6,2.6),xlabel="entropy / information (nats)");ax.set_yticks([0,1,2],labels=["H(Y)","H(X)","H(X,Y)"]);ax.set_xticks([0,.5,1]);ax.set_title("Fair bit; copy probability 0.8\nMI ≈ 0.193, conditional H ≈ 0.500",fontsize=23,fontweight="bold");ax.grid(axis="x",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=24);fig.subplots_adjust(left=.26,right=.95,top=.82,bottom=.33)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
