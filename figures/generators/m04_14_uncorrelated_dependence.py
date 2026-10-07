#!/usr/bin/env python3
"""Finite nonlinear dependency with zero correlation and positive mutual information."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-14-uncorrelated"})
    x=np.array([-1,0,1]);y=x*x;mi=-np.sum(np.array([1/3,2/3])*np.log([1/3,2/3]));fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    line=np.linspace(-1,1,301);ax.plot(line,line*line,linestyle="--",color="#CBD5E1",linewidth=2);ax.scatter(x,y,color="#2563EB",s=120,zorder=4,label="three pairs: mass 1/3 each")
    ax.set(xlim=(-1.25,1.25),ylim=(-.2,1.3),xlabel="X",ylabel="Y = X²");ax.set_xticks([-1,0,1]);ax.set_yticks([0,1]);ax.set_title(f"Correlation = 0\nMI = H(Y) ≈ {mi:.3f} nats",fontsize=25,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=20);fig.subplots_adjust(left=.18,right=.95,top=.84,bottom=.27)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
