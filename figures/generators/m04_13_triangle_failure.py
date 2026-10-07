#!/usr/bin/env python3
"""An exact Bernoulli counterexample to a metric triangle inequality."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def kl(p,q):return p*np.log(p/q)+(1-p)*np.log((1-p)/(1-q))
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-13-triangle"})
    direct=kl(.1,.9);first=kl(.1,.5);second=kl(.5,.9)
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.barh([1],[direct],height=.36,color="#7C3AED",label="KL(p ∥ r)");ax.barh([0],[first],height=.36,color="#2563EB",label="KL(p ∥ q)");ax.barh([0],[second],left=[first],height=.36,color="#D97706",label="KL(q ∥ r)")
    ax.text(direct+.04,1,f"{direct:.3f}",va="center",fontsize=24);ax.text(first+second+.04,0,f"{first+second:.3f}",va="center",fontsize=24)
    ax.set(xlim=(0,2.2),ylim=(-.7,1.7),xlabel="KL value / sum (nats)");ax.set_yticks([0,1],labels=["sum","direct"]);ax.set_xticks([0,1,2]);ax.set_title("Bernoulli p=.1, q=.5, r=.9\nKL(p ∥ r) > KL(p ∥ q)+KL(q ∥ r)",fontsize=21,fontweight="bold");ax.grid(axis="x",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=24);fig.subplots_adjust(left=.21,right=.96,top=.82,bottom=.34)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
