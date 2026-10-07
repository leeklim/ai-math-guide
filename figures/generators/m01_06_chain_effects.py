#!/usr/bin/env python3
"""Generate scalar path products and a smooth-composition example."""
from __future__ import annotations
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",required=True,type=Path)
    output=parser.parse_args().output
    name=output.stem.removeprefix("M01-06-")
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,"svg.fonttype":"none",
                         "svg.hashsalt":"mmi-m01-06-"+name})
    fig,ax=plt.subplots(figsize=(8.6,6.8))
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    if name=="depth-products":
        depth=np.arange(1,9)
        ax.plot(depth,.5**depth,"o-",color="#2563EB",lw=2.5,label="Each local slope: 0.5")
        ax.plot(depth,2.**depth,"s--",color="#7C3AED",lw=2.5,label="Each local slope: 2")
        ax.set_yscale("log",base=2)
        ax.set(xlim=(.6,8.4),xticks=[1,2,4,6,8],yticks=[1/256,1/16,1,16,256],yticklabels=["1/256","1/16","1","16","256"])
        ax.set_xlabel("Number of stages",labelpad=14)
        ax.set_ylabel("Path derivative (log scale)",labelpad=14)
        title,footer="Repeated local slopes multiply along the path","One scalar path; no claim about a whole neural network."
        ax.legend(loc="upper left",frameon=False,fontsize=16)
    elif name=="smooth-composite":
        x=np.linspace(-1.6,1.6,250)
        ax.plot(x,np.abs(x),color="#2563EB",lw=3,label="Inner: |x|")
        ax.plot(x,x*x,color="#059669",lw=3,ls="--",label="Composite: (|x|)² = x²")
        ax.scatter([0],[0],color="#D97706",s=80,zorder=5)
        ax.set(xlim=(-1.7,1.7),ylim=(-.3,3.5),xticks=[-1,0,1])
        ax.set_xlabel("Input x",labelpad=14)
        ax.set_ylabel("Function value",labelpad=14)
        title,footer="An inner corner can disappear after composition","At 0: |x| is not differentiable, but (|x|)² is."
        ax.legend(loc="upper center",frameon=False,fontsize=16)
    else:
        raise ValueError(f"Unknown M01-06 figure: {name}")
    ax.set_title(title,fontsize=20,pad=24)
    ax.spines[["top","right"]].set_visible(False)
    ax.grid(color="#CBD5E1",lw=.7)
    fig.text(.5,.09,footer,ha="center",color="#334155",fontsize=16)
    fig.subplots_adjust(left=.19,right=.94,bottom=.24,top=.83)
    output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"mmi"})
    plt.close(fig)


if __name__=="__main__":
    main()
