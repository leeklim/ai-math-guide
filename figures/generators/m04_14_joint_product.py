#!/usr/bin/env python3
"""Actual noisy-copy joint table and independence table with identical marginals."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":20,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-14-joint"})
    joint=np.array([[.4,.1],[.1,.4]]);product=np.outer(joint.sum(axis=1),joint.sum(axis=0));fig,axes=plt.subplots(1,2,figsize=(11,7.5),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax,m,title in zip(axes,[joint,product],["Actual joint p(X,Y)","Marginal product p(X)p(Y)"]):
        ax.pcolormesh(np.arange(3)-.5,np.arange(3)-.5,m,cmap="Blues",vmin=0,vmax=.5);ax.set(xlim=(-.5,1.5),ylim=(1.5,-.5));ax.set_aspect("equal");ax.set_xticks([0,1],labels=["Y=0","Y=1"]);ax.set_yticks([0,1],labels=["X=0","X=1"]);ax.set_title(title,fontsize=20,pad=24)
        for row in range(2):
            for col in range(2):ax.text(col,row,f"{m[row,col]:.2f}",ha="center",va="center",fontsize=27,color="white" if m[row,col]>.3 else "#1E3A8A")
        ax.set_xlabel("Each Y marginal = 0.5",labelpad=20);ax.set_ylabel("Each X marginal = 0.5",labelpad=12)
    fig.suptitle("Same marginals; different pairing dependence",fontsize=23,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
