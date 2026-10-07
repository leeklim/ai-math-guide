"""Reproduce kernel sections, evaluation, and representer projection sketches."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE,PURPLE,GREEN="#2563EB","#7C3AED","#059669"
GRID,GRAY="#D9E2EF","#64748B"


def arrow(ax,start,end,color,ls="-"):
    ax.annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":"->","color":color,
        "lw":2.8,"mutation_scale":12,"shrinkA":0,"shrinkB":0,"linestyle":ls},zorder=5)


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();name=args.output.stem.removeprefix("A09-KER-04-")
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none",
        "svg.hashsalt":"a09-ker-04","axes.spines.top":False,"axes.spines.right":False})
    wide=name=="kernel-relative-norm"
    if wide:
        fig,axes=plt.subplots(1,2,figsize=(14,10));fig.subplots_adjust(left=.10,right=.96,bottom=.35,top=.73,wspace=.5)
    else:
        fig,ax=plt.subplots(figsize=(7.2,11));axes=[ax];fig.subplots_adjust(left=.24,right=.94,bottom=.43,top=.77)
    x=np.linspace(-1.5,2.5,240)
    if name in {"kernel-sections","section-combination"}:
        k0=np.exp(-x*x/(2*.7**2));k1=np.exp(-(x-1)**2/(2*.7**2))
        if name=="kernel-sections":
            curves=[k0,k1];labels=["k₀(z)","k₁(z)"];colors=[BLUE,PURPLE]
            ax.set_title("Gaussian kernel sections\nx=0 or 1 fixed; σ=0.7",fontsize=25,pad=27)
            footer="Each section is a whole function of z.\nIts center x is fixed, not its output."
        else:
            fig.subplots_adjust(bottom=.48)
            curves=[2*k0,-k1,2*k0-k1];labels=["2k₀(z)","−k₁(z)","f(z)"];colors=[BLUE,PURPLE,GREEN]
            ax.set_title("f=2k₀−k₁\nCombine whole sections",fontsize=26,pad=27)
            footer="At z=0.5: f(z)≈0.775\n‖f‖²=5−4k(0,1)≈3.558"
        for curve,label,color,ls in zip(curves,labels,colors,["-","--","-."]):ax.plot(x,curve,color=color,ls=ls,lw=3,label=label)
        ax.set_xticks([-1,0,1,2]);ax.set_xlabel("free input z",fontsize=26);ax.set_ylabel("function value",fontsize=25);ax.grid(color=GRID)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.145),fontsize=25,frameon=False)
        fig.text(.5,.065,footer,ha="center",fontsize=24)
    elif name in {"reproducing-coordinates","evaluation-bound"}:
        if name=="reproducing-coordinates":
            f=np.array([1.,2.]);k=np.array([1.,1.]);proj=np.dot(f,k)/np.dot(k,k)*k
            arrow(ax,(0,0),f,BLUE);arrow(ax,(0,0),k,PURPLE);ax.plot([f[0],proj[0]],[f[1],proj[1]],":",color=GRAY,lw=2)
            ax.scatter([proj[0]],[proj[1]],color=GREEN,s=55,zorder=6)
            ax.set_xlim(-.2,2.2);ax.set_ylim(-.2,2.5);ax.set_xticks([0,1,2]);ax.set_yticks([0,1,2])
            title="k(x,z)=1+xz, f(z)=1+2z\nEvaluate at x=1"
            footer="Blue f ↔ (1,2); purple k₁ ↔ (1,1)\nf(1)=3 = (1,2)·(1,1)\nGreen point: orthogonal projection."
        else:
            t=np.linspace(0,2*np.pi,240);ax.plot(np.cos(t),np.sin(t),"--",color=GRAY,lw=2)
            arrow(ax,(0,0),(.6,.8),BLUE);arrow(ax,(0,0),(1,1),PURPLE)
            ax.set_xlim(-1.35,1.6);ax.set_ylim(-1.35,1.6);ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
            title="Blue f=(0.6,0.8): ‖f‖=1\nPurple k₁=(1,1)"
            footer="Dashed circle: ‖f‖=1\n|f(1)|=1.4 ≤ ‖f‖√k(1,1)=√2\nThe evaluation is bounded."
        ax.set_aspect("equal");ax.grid(color=GRID);ax.set_xlabel("function coefficient a",fontsize=25);ax.set_ylabel("function coefficient b",fontsize=25)
        ax.set_title(title,fontsize=24,pad=27);fig.text(.5,.11,footer,ha="center",fontsize=24)
    elif name=="representer-projection":
        arrow(ax,(0,0),(2,1),BLUE);arrow(ax,(0,0),(2,0),GREEN);arrow(ax,(2,0),(2,1),PURPLE)
        ax.axhline(0,color=GRAY,lw=1.5);ax.plot([-.2,2.7],[0,0],"--",color=GREEN,lw=2)
        ax.set_xlim(-.2,2.7);ax.set_ylim(-.45,1.65);ax.set_xticks([0,1,2]);ax.set_yticks([0,1]);ax.grid(color=GRID)
        ax.set_xlabel("coefficient a: training span",fontsize=24);ax.set_ylabel("coefficient b",fontsize=26)
        ax.set_title("k(x,z)=1+xz; train only x=0\nf(z)=2+z ↔ (2,1)",fontsize=24,pad=27)
        fig.text(.5,.12,"k₀=(1,0): horizontal training span\nGreen f∥=2; purple f⊥=z\n‖f‖²=5 → ‖f∥‖²=4; λ>0",ha="center",fontsize=24)
    elif name=="training-values-preserved":
        ax.plot(x,2+x,color=BLUE,lw=3,label="f=2+z")
        ax.plot(x,np.full_like(x,2),color=GREEN,ls="--",lw=3,label="f∥=2")
        ax.scatter([0],[2],color=PURPLE,s=70,zorder=5);ax.axvline(0,color=GRAY,ls=":")
        ax.set_xlabel("input z",fontsize=26);ax.set_ylabel("function value",fontsize=25);ax.grid(color=GRID);ax.set_xticks([-1,0,1,2])
        ax.set_title("Remove the orthogonal part\nTraining value at x=0 unchanged",fontsize=24,pad=27)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.18),fontsize=25,frameon=False)
        fig.text(.5,.09,"Same training prediction f(0)=2\nThe penalty decreases;\nother input values may change.",ha="center",fontsize=24)
    elif name=="kernel-relative-norm":
        for ax,scale in zip(axes,[1,2]):
            phi=np.linspace(-2*scale,2*scale,200);w=1/scale
            ax.plot(phi,w*phi,color=BLUE,lw=3)
            ax.scatter([.5*scale],[.5],color=GREEN,s=70,zorder=5)
            ax.set_xlabel(f"feature φ(x)={scale:g}x",fontsize=24);ax.set_ylabel("same output f(x)=x",fontsize=23)
            ax.set_xticks([-2*scale,0,2*scale]);ax.set_yticks([-2,0,2]);ax.grid(color=GRID)
            ax.set_title(f"k(x,z)={scale**2:g}xz\nw={w:g}, ‖f‖²={w*w:g}",fontsize=24,pad=27)
        fig.text(.5,.10,"Both kernels contain the same function f(x)=x.\nIts RKHS squared norm is 1 or 1/4, relative to the chosen kernel.\nGreen points use the same input x=0.5 and output 0.5.",ha="center",fontsize=23)
    else:raise ValueError(name)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,format="svg",metadata={"Date":None});plt.close(fig)


if __name__=="__main__":main()
