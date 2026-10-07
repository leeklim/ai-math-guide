#!/usr/bin/env python3
"""Gaussian log-likelihood contours for observations 1,2,3."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-11-gaussian"})
    mean,variance=np.meshgrid(np.linspace(.8,3.2,401),np.linspace(.15,2.5,401))
    ell=-1.5*np.log(2*np.pi*variance)-(2+3*(mean-2)**2)/(2*variance)
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    cs=ax.contour(mean,variance,ell,levels=[-12,-9,-7,-6,-5,-4.5,-4],colors=["#CBD5E1","#94A3B8","#64748B","#2563EB","#7C3AED","#059669","#065F46"],linewidths=2)
    ax.scatter([2],[2/3],color="#D97706",s=95,zorder=5,label="MLE: (2, 2/3)")
    ax.set(xlim=(.8,3.2),ylim=(.15,2.5),xlabel="mean μ",ylabel="variance σ²");ax.set_xticks([1,2,3]);ax.set_yticks([.5,1,2]);ax.set_title("Gaussian log-likelihood\nData (1, 2, 3)",fontsize=25,fontweight="bold");ax.grid(color="#E2E8F0",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=24);fig.subplots_adjust(left=.2,right=.95,top=.86,bottom=.27)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
