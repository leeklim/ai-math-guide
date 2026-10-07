#!/usr/bin/env python3
"""Generate complementary derivative views without changing the existing pilot."""
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
    name=output.stem.removeprefix("M01-03-")
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,"svg.fonttype":"none",
                         "svg.hashsalt":"mmi-m01-03-"+name})
    fig,ax=plt.subplots(figsize=(8.6,6.8))
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    if name=="tangent-at-three":
        x=np.linspace(2.35,3.65,250)
        ax.plot(x,x*x,color="#059669",lw=3,label="Curve: x²")
        ax.plot(x,6*x-9,color="#7C3AED",lw=2.5,ls="--",label="Tangent: 6x − 9")
        ax.scatter([3],[9],color="#D97706",s=80,zorder=5)
        ax.annotate("(3, 9)",(3,9),xytext=(2.42,10.2),fontsize=16,
                    arrowprops={"arrowstyle":"-","color":"#64748B"})
        ax.set(xlim=(2.3,3.7),ylim=(4.5,14.5),xticks=[2.5,3,3.5])
        title,footer="A tangent uses a point and its slope","f(3) = 9; f′(3) = 6; y − 9 = 6(x − 3)."
        ax.legend(loc="upper left",frameon=False,fontsize=16)
    elif name=="constant-and-linear":
        x=np.linspace(-1,2,200)
        ax.plot(x,np.full_like(x,2),color="#2563EB",lw=3,label="Constant: f(x) = 2")
        ax.plot(x,2*x+1,color="#059669",lw=3,label="Line: g(x) = 2x + 1")
        ax.set(xlim=(-1.2,2.2),ylim=(-1.5,6.5),xticks=[-1,0,1,2])
        title,footer="The same slope at every base point","The constant has slope 0; the line has slope 2."
        ax.legend(loc="upper left",frameon=False,fontsize=16)
    elif name=="relu-corner":
        x=np.linspace(-2,2,401)
        ax.plot(x,np.maximum(0,x),color="#059669",lw=3)
        ax.scatter([0],[0],color="#D97706",s=80,zorder=5)
        ax.annotate("left slope = 0",(-1,0),xytext=(-1.85,.75),fontsize=16,
                    arrowprops={"arrowstyle":"-","color":"#64748B"})
        ax.annotate("right slope = 1",(1,1),xytext=(.15,2.05),fontsize=16,
                    arrowprops={"arrowstyle":"-","color":"#64748B"})
        ax.set(xlim=(-2.1,2.1),ylim=(-.5,2.7),xticks=[-2,-1,0,1,2],yticks=[0,1,2])
        title,footer="Continuous values, unequal one-sided slopes","At 0: ReLU is continuous, but its derivative is undefined."
    elif name=="zero-slope-not-constant":
        x=np.linspace(-1.5,1.5,250)
        ax.plot(x,x*x,color="#059669",lw=3,label="Curve: x²")
        ax.axhline(0,color="#7C3AED",ls="--",lw=2.5,label="Tangent at 0")
        ax.scatter([0],[0],color="#D97706",s=80,zorder=5)
        ax.scatter([-.5,.5],[.25,.25],color="#2563EB",s=60,zorder=5)
        ax.set(xlim=(-1.7,1.7),ylim=(-.3,2.9),xticks=[-1,0,1],yticks=[0,1,2])
        title,footer="Zero derivative is a local first-order statement","f′(0) = 0, but f(±0.5) = 0.25 differs from f(0)."
        ax.legend(loc="upper center",frameon=False,fontsize=16)
    else:
        raise ValueError(f"Unknown M01-03 figure: {name}")
    ax.set_xlabel("Input x",labelpad=14)
    ax.set_ylabel("Output",labelpad=14)
    ax.set_title(title,fontsize=20,pad=24)
    ax.spines[["top","right"]].set_visible(False)
    ax.grid(color="#CBD5E1",lw=.7)
    fig.text(.5,.09,footer,ha="center",color="#334155",fontsize=16)
    fig.subplots_adjust(left=.17,right=.94,bottom=.24,top=.83)
    output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"mmi"})
    plt.close(fig)


if __name__=="__main__":
    main()
