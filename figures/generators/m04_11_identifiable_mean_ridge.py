#!/usr/bin/env python3
"""Different additive parameters give the same Gaussian fitted mean."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-11-ridge"})
    a,b=np.meshgrid(np.linspace(-1,3,301),np.linspace(-1,3,301));ell=-1.5*np.log(2*np.pi)-(2+3*(a+b-2)**2)/2
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.contour(a,b,ell,levels=[-15,-10,-6,-4],colors=["#CBD5E1","#94A3B8","#7C3AED","#2563EB"],linewidths=2)
    axis=np.linspace(-1,3,200);ax.plot(axis,2-axis,color="#059669",linewidth=3,label="maxima: a + b = 2")
    ax.scatter([0,1,2],[2,1,0],color="#D97706",s=70,zorder=4)
    ax.set(xlim=(-1,3),ylim=(-1,3),xlabel="parameter a",ylabel="parameter b");ax.set_aspect("equal");ax.set_xticks([-1,0,1,2,3]);ax.set_yticks([-1,0,1,2,3]);ax.set_title("Gaussian mean μ = a + b\nData (1, 2, 3); fixed σ² = 1",fontsize=24,fontweight="bold");ax.grid(color="#E2E8F0",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=23);fig.subplots_adjust(left=.18,right=.95,top=.84,bottom=.27)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
