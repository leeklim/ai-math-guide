#!/usr/bin/env python3
"""Uniform entropy depends on the fixed outcome count being compared."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-12-count"})
    k=np.arange(1,9);fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.plot(k,np.log(k),"o--",color="#059669",linewidth=2,markersize=7);ax.set(xlim=(.7,8.3),ylim=(-.05,2.3),xlabel="number of outcomes K",ylabel="uniform entropy log K");ax.set_xticks([1,2,4,8]);ax.set_title("Uniform distributions\nChanging K changes the maximum",fontsize=24,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);fig.subplots_adjust(left=.22,right=.95,top=.84,bottom=.16)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
