#!/usr/bin/env python3
"""Independent fair-bit joint versus conditioning on their OR collider."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":19,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-16-collider"})
    fig,axes=plt.subplots(1,2,figsize=(11,7),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax,m,title in zip(axes,[np.full((2,2),.25),np.array([[0,1/3],[1/3,1/3]])],["Before selection: independent X,Y","Condition C=1: remove (0,0)"]):
        ax.pcolormesh(np.arange(3)-.5,np.arange(3)-.5,m,cmap="Blues",vmin=0,vmax=.5);ax.set(xlim=(-.5,1.5),ylim=(1.5,-.5));ax.set_aspect("equal");ax.set_xticks([0,1],labels=["Y=0","Y=1"]);ax.set_yticks([0,1],labels=["X=0","X=1"]);ax.set_title(title,fontsize=18,pad=22)
        for row in range(2):
            for col in range(2):ax.text(col,row,"0" if m[row,col]==0 else "1/4" if m[row,col]==.25 else "1/3",ha="center",va="center",fontsize=29,color="#1E3A8A")
    fig.suptitle("C = X OR Y: conditioning creates dependence",fontsize=23,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
