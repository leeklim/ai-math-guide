#!/usr/bin/env python3
"""Coincident Gaussian observations have unbounded likelihood as variance shrinks."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-11-unbounded"})
    v=np.geomspace(.001,1,400);ell=-1.5*np.log(2*np.pi*v)
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.plot(v,ell,color="#7C3AED",linewidth=3);ax.set_xscale("log");ax.set_xticks([.001,.01,.1,1],labels=[".001",".01",".1","1"]);ax.set(xlim=(.001,1),xlabel="positive variance σ²",ylabel="log-likelihood")
    ax.set_title("Data (2, 2, 2); fix μ = 2\nNo positive-variance maximum",fontsize=24,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    ax.annotate("σ² ↓ 0",xy=(.0012,ell[10]),xytext=(.012,ell[10]),fontsize=24,arrowprops={"arrowstyle":"->","color":"#D97706","mutation_scale":7},color="#9A3412")
    fig.subplots_adjust(left=.2,right=.95,top=.84,bottom=.15)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
