#!/usr/bin/env python3
"""Generate function/derivative and optimization comparisons for M01-04."""
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
    name=output.stem.removeprefix("M01-04-")
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,"svg.fonttype":"none",
                         "svg.hashsalt":"mmi-m01-04-"+name})
    if name=="function-and-slopes":
        fig,axes=plt.subplots(2,1,figsize=(8.6,8.8),sharex=True)
        x=np.linspace(-2.4,3.4,300)
        points=np.array([-2,0,3])
        for ax,y,values,label in zip(axes,[x*x,2*x],[points*points,2*points],["Height f(x) = x²","Slope f′(x) = 2x"]):
            ax.plot(x,y,color="#059669" if ax is axes[0] else "#7C3AED",lw=3)
            ax.scatter(points,values,color="#D97706",s=65,zorder=5)
            for p in points:
                ax.axvline(p,color="#94A3B8",ls=":",lw=1)
            ax.axhline(0,color="#94A3B8",lw=1)
            ax.set_ylabel(label,labelpad=12)
            ax.set_facecolor("#F8FAFC")
            ax.spines[["top","right"]].set_visible(False)
            ax.grid(color="#CBD5E1",lw=.7)
        axes[0].set_title("Same input, height above and slope below",fontsize=20,pad=24)
        axes[0].set_ylim(-.8,13)
        axes[1].set_ylim(-5.5,8)
        axes[1].set(xlim=(-2.4,3.4),xticks=[-2,-1,0,1,2,3],xlabel="Input x")
        footer="At x = −2, 0, 3: slopes are −4, 0, 6."
        fig.subplots_adjust(left=.19,right=.94,bottom=.21,top=.87,hspace=.24)
    else:
        fig,ax=plt.subplots(figsize=(8.6,6.8))
        ax.set_facecolor("#F8FAFC")
        if name=="stationary-cubic":
            x=np.linspace(-1.5,1.5,300)
            ax.plot(x,x**3,color="#059669",lw=3)
            ax.plot([-.8,.8],[0,0],color="#7C3AED",ls="--",lw=2.5)
            ax.scatter([0],[0],color="#D97706",s=85,zorder=5)
            ax.set(xlim=(-1.6,1.6),ylim=(-4,4),xticks=[-1,0,1])
            title,footer="A stationary point need not be an extremum","x³ keeps increasing through 0, even though f′(0) = 0."
        elif name=="sign-test-minimum":
            x=np.linspace(-.4,4.4,300)
            ax.plot(x,(x-2)**2-1,color="#059669",lw=3)
            ax.axvline(2,color="#94A3B8",ls=":")
            ax.scatter([2],[-1],color="#D97706",s=85,zorder=5)
            ax.text(.05,5.3,"f′ < 0\ndecreasing",fontsize=16,color="#1E3A8A")
            ax.text(2.7,5.3,"f′ > 0\nincreasing",fontsize=16,color="#065F46")
            ax.set(xlim=(-.5,4.5),ylim=(-1.8,7.5),xticks=[0,1,2,3,4])
            title,footer="Derivative sign changes from minus to plus","f(x) = x² − 4x + 3 has its minimum at (2, −1)."
        elif name=="height-versus-slope":
            x=np.linspace(-2.1,1.1,300)
            ax.plot(x,x*x,color="#059669",lw=3,label="Height: x²")
            ax.plot(x,-2*x-1,color="#7C3AED",ls="--",lw=2.5,label="Tangent at −1")
            ax.axhline(0,color="#94A3B8",lw=1)
            ax.scatter([-1],[1],color="#D97706",s=85,zorder=5)
            ax.annotate("f(−1) = 1",(-1,1),xytext=(-.55,2.2),fontsize=16,
                        arrowprops={"arrowstyle":"-","color":"#64748B"})
            ax.set(xlim=(-2.2,1.2),ylim=(-2,5.5),xticks=[-2,-1,0,1])
            title,footer="Positive height can have negative slope","At x = −1: f = 1 > 0, but f′ = −2 < 0."
            ax.legend(loc="upper right",frameon=False,fontsize=16)
        elif name=="corner-minimum":
            x=np.linspace(-2,2,300)
            ax.plot(x,np.abs(x),color="#059669",lw=3)
            ax.scatter([0],[0],color="#D97706",s=85,zorder=5)
            ax.text(-1.7,1.85,"slope −1",fontsize=16,color="#1E3A8A")
            ax.text(.65,1.85,"slope +1",fontsize=16,color="#065F46")
            ax.set(xlim=(-2.2,2.2),ylim=(-.4,2.8),xticks=[-2,-1,0,1,2],yticks=[0,1,2])
            title,footer="A corner can be a local minimum","|x| has a minimum at 0, where its derivative is undefined."
        elif name=="gradient-step":
            x=np.linspace(2.1,5.7,250)
            ax.plot(x,(x-3)**2,color="#059669",lw=3)
            ax.scatter([5,4.6],[4,2.56],color=["#D97706","#2563EB"],s=85,zorder=5)
            ax.annotate("old: (5, 4)",(5,4),xytext=(3.2,5.8),fontsize=16,
                        arrowprops={"arrowstyle":"-","color":"#64748B"})
            ax.annotate("new: (4.6, 2.56)",(4.6,2.56),xytext=(2.3,3.55),fontsize=16,
                        arrowprops={"arrowstyle":"-","color":"#64748B"})
            ax.annotate("",(4.6,-.25),xytext=(5,-.25),
                        arrowprops={"arrowstyle":"->","color":"#2563EB","lw":2,"mutation_scale":10})
            ax.set(xlim=(2,5.8),ylim=(-.7,7.5),xticks=[3,4,4.6,5])
            ax.set_xlabel("Parameter θ",labelpad=14)
            title,footer="A positive slope suggests a small step left","θnew = 5 − 0.1 × 4 = 4.6; loss changes 4 → 2.56."
        else:
            raise ValueError(f"Unknown M01-04 figure: {name}")
        if name!="gradient-step":
            ax.set_xlabel("Input x",labelpad=14)
        ax.set_ylabel("Loss" if name=="gradient-step" else "Function value",labelpad=14)
        ax.set_title(title,fontsize=20,pad=24)
        ax.spines[["top","right"]].set_visible(False)
        ax.grid(color="#CBD5E1",lw=.7)
        fig.subplots_adjust(left=.17,right=.94,bottom=.24,top=.83)
    fig.patch.set_facecolor("#F8FAFC")
    fig.text(.5,.075 if name=="function-and-slopes" else .09,footer,ha="center",color="#334155",fontsize=16)
    output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"mmi"})
    plt.close(fig)


if __name__=="__main__":
    main()
