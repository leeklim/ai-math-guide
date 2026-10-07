#!/usr/bin/env python3
"""Generate Riemann rectangles, signed areas, and accumulation diagrams."""
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
    name=output.stem.removeprefix("M01-08-")
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,"svg.fonttype":"none","svg.hashsalt":"mmi-m01-08-"+name})
    pair=name=="moving-endpoint"
    fig,axes=plt.subplots(2 if pair else 1,1,figsize=(8.6,8.8 if pair else 6.8),sharex=pair)
    axes=np.atleast_1d(axes)
    ax=axes[0]
    if name in {"riemann-four","riemann-refinement"}:
        n=4 if name=="riemann-four" else 16
        right=np.arange(1,n+1)/n
        ax.bar(right-1/n,right**2,width=1/n,align="edge",color="#DBEAFE",edgecolor="#2563EB",lw=1.1,label=f"{n} right-end rectangles")
        x=np.linspace(0,1,300)
        ax.plot(x,x*x,color="#059669",lw=3,label="f(x) = x²")
        ax.scatter(right,right*right,color="#D97706",s=35 if n==4 else 18,zorder=5)
        ax.set(xlim=(-.04,1.06),ylim=(0,1.65),xticks=[0,.25,.5,.75,1],ylabel="Function height")
        ax.legend(loc="upper left",frameon=False,fontsize=16)
        title="Each rectangle uses a height and a width"
        footer=f"n = {n}; width = 1/{n}; right-end sum = {np.sum(right**2)/n:.8g}."
    elif name=="signed-area":
        x=np.linspace(0,2,251)
        ax.plot(x,x-1,color="#059669",lw=3)
        ax.fill_between(x,x-1,0,where=x<=1,color="#DBEAFE",hatch="//",edgecolor="#2563EB")
        ax.fill_between(x,x-1,0,where=x>=1,color="#D1FAE5",edgecolor="#059669")
        ax.axhline(0,color="#64748B",lw=1.2)
        ax.text(.18,-.30,"−1/2",fontsize=20,color="#1E3A8A",bbox={"facecolor":"#DBEAFE","edgecolor":"none","pad":3})
        ax.text(1.62,.24,"+1/2",fontsize=20,color="#065F46")
        ax.set(xlim=(-.08,2.08),ylim=(-1.4,1.5),xticks=[0,1,2],yticks=[-1,0,1],ylabel="f(x) = x − 1")
        title,footer="Signed contributions can cancel","Signed integral = 0; sum of geometric areas = 1."
    elif name=="linearity-areas":
        x=np.linspace(0,2,250)
        ax.fill_between(x,0,1,color="#DBEAFE",label="Area from f(x) = 1")
        ax.fill_between(x,1,1+x,color="#D1FAE5",hatch="//",edgecolor="#059669",label="Added area from g(x) = x")
        ax.plot(x,1+x,color="#059669",lw=3)
        ax.axhline(1,color="#64748B",ls="--",lw=1)
        ax.set(xlim=(-.08,2.08),ylim=(0,4.8),xticks=[0,1,2],yticks=[0,1,2,3],ylabel="f(x) + g(x)")
        ax.legend(loc="upper left",frameon=False,fontsize=16)
        title,footer="Integrate a sum as two contributions","On [0, 2]: rectangle 2 + triangle 2 = total 4."
    elif name=="constant-speed":
        x=np.linspace(0,4,100)
        ax.fill_between(x,0,3,color="#D1FAE5")
        ax.plot(x,np.full_like(x,3),color="#059669",lw=3)
        ax.text(1.18,1.4,"3 m/s × 4 s",fontsize=20,color="#065F46")
        ax.set(xlim=(-.2,4.2),ylim=(0,4.5),xticks=[0,1,2,3,4],yticks=[0,1,2,3,4],ylabel="Velocity (m/s)")
        ax.set_xlabel("Time t (s)",labelpad=14)
        title,footer="Integration multiplies rate by interval width","Displacement = 12 m, not 12 m/s."
    elif name=="moving-endpoint":
        x=np.linspace(0,2.1,421)
        axes[0].plot(x,x,color="#059669",lw=3)
        axes[0].fill_between(x,0,x,where=x<=1,color="#DBEAFE",label="Common interval 0..1")
        axes[0].fill_between(x,0,x,where=(x>=1)&(x<=2),color="#D1FAE5",hatch="//",edgecolor="#059669",label="New interval 1..2")
        axes[0].set_ylabel("Integrand f(t) = t",labelpad=12)
        axes[0].set_ylim(0,3.9)
        axes[0].legend(loc="upper left",frameon=False,fontsize=16)
        axes[1].plot(x,.5*x*x,color="#7C3AED",lw=3)
        axes[1].scatter([1,2],[.5,2],color="#D97706",s=70,zorder=5)
        axes[1].set(xlim=(-.05,2.15),ylim=(0,2.6),xticks=[0,1,2],ylabel="Accumulation A(x)")
        axes[1].set_xlabel("End input x (integration variable t above)",labelpad=14)
        title,footer="Moving the endpoint changes accumulated area","A(1) = 0.5; A(2) = 2; new area = 1.5."
    elif name=="same-final-different-area":
        x=np.linspace(0,1,250)
        a=1-x
        b=(1-x)**2
        ax.fill_between(x,0,b,color="#D1FAE5")
        ax.fill_between(x,b,a,color="#DBEAFE",hatch="//",edgecolor="#2563EB")
        ax.plot(x,a,color="#2563EB",lw=3,label="Illustration A: 1 − t")
        ax.plot(x,b,color="#059669",lw=3,ls="--",label="Illustration B: (1 − t)²")
        ax.scatter([1],[0],color="#D97706",s=70,zorder=5)
        ax.set(xlim=(-.04,1.06),ylim=(-.05,1.6),xticks=[0,.5,1],yticks=[0,.5,1],ylabel="Illustrative loss")
        ax.set_xlabel("Normalized time t",labelpad=14)
        ax.legend(loc="upper right",frameon=False,fontsize=16)
        title,footer="Same final loss, different accumulated loss","Both end at 0; shaded extra area belongs only to A."
    else:
        raise ValueError(f"Unknown M01-08 figure: {name}")
    for item in axes:
        item.set_facecolor("#F8FAFC")
        item.spines[["top","right"]].set_visible(False)
        item.grid(color="#CBD5E1",lw=.7)
    if name not in {"constant-speed","moving-endpoint","same-final-different-area"}:
        axes[-1].set_xlabel("Input x",labelpad=14)
    axes[0].set_title(title,fontsize=20,pad=24)
    fig.patch.set_facecolor("#F8FAFC")
    fig.text(.5,.075 if pair else .09,footer,ha="center",color="#334155",fontsize=16)
    fig.subplots_adjust(left=.19 if pair else .17,right=.94,bottom=.21 if pair else .24,top=.87 if pair else .83,hspace=.26)
    output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"mmi"})
    plt.close(fig)


if __name__=="__main__":
    main()
