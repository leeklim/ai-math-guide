#!/usr/bin/env python3
"""Expected log and Brier scores have the same truthful binary minimizer."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":18,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-15-proper"})
    q=np.linspace(.005,.995,500);p=.7;fig,axes=plt.subplots(1,2,figsize=(11,7),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax,y,title,best in [(axes[0],-p*np.log(q)-(1-p)*np.log1p(-q),"Expected log score",-p*np.log(p)-(1-p)*np.log1p(-p)),(axes[1],p*(1-p)+(q-p)**2,"Expected binary Brier",p*(1-p))]:
        ax.set_facecolor("#F8FAFC");ax.plot(q,y,color="#7C3AED",linewidth=3);ax.axhline(best,color="#059669",linestyle="--",linewidth=2);ax.axvline(p,color="#D97706",linestyle="--");ax.scatter([p],[best],color="#D97706",s=70,zorder=4);ax.set(xlim=(0,1),xlabel="reported q",ylabel="expected loss");ax.set_xticks([0,.5,.7,1]);ax.set_title(title,fontsize=20);ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    fig.suptitle("Fix true Bernoulli p = .7; unique minimum at q = p",fontsize=21,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
