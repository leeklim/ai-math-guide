#!/usr/bin/env python3
"""Possible samples of independent fair bits can give different plug-in MI values."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":18,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-14-estimate"})
    fig,axes=plt.subplots(1,3,figsize=(13.5,7),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    matrices=[np.full((2,2),.25),np.array([[2,0],[0,2]]),np.ones((2,2),dtype=int)]
    titles=["Population: independent bits\nTrue MI = 0","Possible n=4 sample counts\nPlug-in MI = log 2","Another n=4 sample counts\nPlug-in MI = 0"]
    for index,(ax,m,title) in enumerate(zip(axes,matrices,titles)):
        ax.pcolormesh(np.arange(3)-.5,np.arange(3)-.5,m,cmap="Blues",vmin=0,vmax=.5 if index==0 else 2.5);ax.set(xlim=(-.5,1.5),ylim=(1.5,-.5));ax.set_aspect("equal");ax.set_xticks([0,1],labels=["Y=0","Y=1"]);ax.set_yticks([0,1],labels=["X=0","X=1"]);ax.set_title(title,fontsize=18,pad=22)
        for row in range(2):
            for col in range(2):ax.text(col,row,f"{m[row,col]:.2f}" if index==0 else str(m[row,col]),ha="center",va="center",fontsize=27,color="white" if m[row,col]>1 else "#1E3A8A")
    fig.suptitle("Constructed possible samples; not estimated population truth",fontsize=22,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
