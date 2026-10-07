#!/usr/bin/env python3
"""Generate product-rule and mean-gradient comparisons for M01-05."""
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
    name=output.stem.removeprefix("M01-05-")
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,"svg.fonttype":"none",
                         "svg.hashsalt":"mmi-m01-05-"+name})
    fig,ax=plt.subplots(figsize=(8.6,6.8))
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    if name=="product-rule-versus-wrong":
        x=np.linspace(-1.5,2.5,200)
        ax.plot(x,2*x,color="#7C3AED",lw=3,label="Correct: (x · x)′ = 2x")
        ax.axhline(1,color="#64748B",lw=2,ls="--",label="Wrong: x′ · x′ = 1")
        ax.set(xlim=(-1.6,2.6),ylim=(-3.5,6.5),xticks=[-1,0,1,2])
        ax.set_xlabel("Input x",labelpad=14)
        ax.legend(loc="upper left",frameon=False,fontsize=16)
        title,footer="Two varying factors require two contributions","The two formulas agree at only x = 0.5 here."
    elif name=="mean-cancellation":
        ax.bar([0,1],[4,-4],color="#D97706",width=.5)
        ax.scatter([2],[0],color="#7C3AED",s=90,zorder=5)
        ax.axhline(0,color="#64748B",lw=1.3)
        ax.set(xlim=(-.6,2.6),ylim=(-5.2,5.2),xticks=[0,1,2],xticklabels=["Sample 1","Sample 2","Mean"],yticks=[-4,0,4])
        ax.text(0,4.35,"+4",ha="center",fontsize=16)
        ax.text(1,-4.85,"−4",ha="center",fontsize=16)
        ax.text(2,.6,"0",ha="center",fontsize=16,color="#5B21B6")
        title,footer="Opposite sample gradients cancel in the mean","Mean derivative = (4 − 4) / 2 = 0."
    else:
        raise ValueError(f"Unknown M01-05 figure: {name}")
    ax.set_ylabel("Derivative value",labelpad=14)
    ax.set_title(title,fontsize=20,pad=24)
    ax.spines[["top","right"]].set_visible(False)
    ax.grid(axis="y",color="#CBD5E1",lw=.7)
    fig.text(.5,.09,footer,ha="center",color="#334155",fontsize=16)
    fig.subplots_adjust(left=.17,right=.94,bottom=.24,top=.83)
    output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"mmi"})
    plt.close(fig)


if __name__=="__main__":
    main()
