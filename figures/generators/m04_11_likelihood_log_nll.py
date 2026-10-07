#!/usr/bin/env python3
"""Same Bernoulli optimum across likelihood, log-likelihood, and NLL."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--output",required=True,type=Path); args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-11-log"})
    p=np.linspace(.002,.998,700); ell=3*np.log(p)+np.log1p(-p)
    fig,axes=plt.subplots(1,3,figsize=(13,5.8),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax,values,title,color in zip(axes,[np.exp(ell),ell,-ell],["L: maximize","log L: maximize","−log L: minimize"],["#2563EB","#7C3AED","#059669"]):
        optimum=3*np.log(.75)+np.log(.25)
        best=np.exp(optimum) if title.startswith("L:") else optimum if title.startswith("log") else -optimum
        ax.set_facecolor("#F8FAFC");ax.plot(p,values,color=color,linewidth=2.5);ax.axvline(.75,color="#D97706",linestyle="--");ax.scatter([.75],[best],color="#D97706",zorder=4)
        ax.set(xlim=(0,1),xlabel="parameter p");ax.set_xticks([0,.5,.75,1]);ax.set_title(title,fontsize=18);ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    fig.suptitle("Observed data (1, 0, 1, 1): same optimum p = 0.75",fontsize=20,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
