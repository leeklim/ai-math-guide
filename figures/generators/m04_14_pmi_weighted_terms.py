#!/usr/bin/env python3
"""PMI signs versus joint-weighted contributions to MI."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":20,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-14-pmi"})
    joint=np.array([[.4,.1],[.1,.4]]);pmi=np.log(joint/.25);terms=joint*pmi;fig,axes=plt.subplots(1,2,figsize=(11,7),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax,m,title in zip(axes,[pmi,terms],["PMI = log(joint / 0.25)",f"Joint-weighted terms; MI ≈ {terms.sum():.3f}"]):
        ax.pcolormesh(np.arange(3)-.5,np.arange(3)-.5,m,cmap="PuOr",vmin=-1,vmax=1);ax.set(xlim=(-.5,1.5),ylim=(1.5,-.5));ax.set_aspect("equal");ax.set_xticks([0,1],labels=["Y=0","Y=1"]);ax.set_yticks([0,1],labels=["X=0","X=1"]);ax.set_title(title,fontsize=18,pad=22)
        for row in range(2):
            for col in range(2):ax.text(col,row,f"{m[row,col]:+.3f}",ha="center",va="center",fontsize=27,color="white" if abs(m[row,col])>.7 else "#334155")
    fig.suptitle("Individual PMI may be negative; MI is its weighted sum",fontsize=21,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
