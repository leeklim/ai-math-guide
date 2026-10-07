#!/usr/bin/env python3
"""Generate exponential, logarithmic, and probability-sensitivity views."""
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
    name=output.stem.removeprefix("M01-07-")
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,"svg.fonttype":"none",
                         "svg.hashsalt":"mmi-m01-07-"+name})
    pair=name in {"log-and-slope","logsumexp-and-probability"}
    fig,axes=plt.subplots(2 if pair else 1,1,figsize=(8.6,8.8 if pair else 6.8),sharex=pair)
    axes=np.atleast_1d(axes)
    if name=="exp-height-slope":
        ax=axes[0]
        x=np.linspace(-1.8,1.6,250)
        ax.plot(x,np.exp(x),color="#059669",lw=3,label="exp(x): value = derivative")
        ax.plot(x,1+x,color="#7C3AED",ls="--",lw=2.5,label="Tangent at 0: 1 + x")
        ax.scatter([0],[1],color="#D97706",s=80,zorder=5)
        ax.set(xlim=(-1.9,1.7),ylim=(-1,6),xticks=[-1,0,1],ylabel="Output")
        title,footer="The exponential matches its local slope","At x = 0: value 1 and tangent slope 1."
        ax.legend(loc="upper left",frameon=False,fontsize=16)
    elif name=="base-and-direction":
        ax=axes[0]
        x=np.linspace(-2,2,250)
        ax.plot(x,2.**x,color="#059669",lw=3,label="2ˣ: log 2 > 0")
        ax.plot(x,.5**x,color="#2563EB",lw=3,ls="--",label="0.5ˣ: log 0.5 < 0")
        ax.scatter([0],[1],color="#D97706",s=80,zorder=5)
        ax.set(xlim=(-2.2,2.2),ylim=(0,5.5),xticks=[-2,-1,0,1,2],ylabel="aˣ")
        title,footer="The base determines the derivative sign","Both values equal 1 at 0; their slopes have opposite signs."
        ax.legend(loc="upper center",frameon=False,fontsize=16)
    elif name=="log-and-slope":
        x=np.linspace(.08,3.3,300)
        axes[0].plot(x,np.log(x),color="#059669",lw=3)
        axes[1].plot(x,1/x,color="#7C3AED",lw=3)
        for ax,values,label in zip(axes,[[np.log(.2),0,np.log(3)],[5,1,1/3]],["Value log x","Slope 1/x"]):
            ax.scatter([.2,1,3],values,color="#D97706",s=60,zorder=5)
            for p in [.2,1,3]:
                ax.axvline(p,color="#94A3B8",ls=":",lw=1)
            ax.set_ylabel(label,labelpad=12)
        axes[0].set_ylim(-3,1.6)
        axes[1].set(xlim=(0,3.4),ylim=(0,13),xticks=[0,1,2,3])
        title,footer="Small positive inputs have steep logarithms","At x = 0.2, 1, 3: slopes are 5, 1, 1/3."
    elif name=="negative-log-sensitivity":
        ax=axes[0]
        p=np.geomspace(.006,1,300)
        ax.plot(p,1/p,color="#7C3AED",lw=3)
        ax.scatter([.01,.5],[100,2],color="#D97706",s=70,zorder=5)
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set(xlim=(.006,1.2),ylim=(.8,200),xticks=[.01,.1,.5,1],xticklabels=["0.01","0.1","0.5","1"],yticks=[1,2,10,100],yticklabels=["1","2","10","100"],ylabel="Magnitude |d loss / dp| = 1/p")
        ax.annotate("100 at p = 0.01",(.01,100),xytext=(.035,110),fontsize=16,
                    arrowprops={"arrowstyle":"-","color":"#64748B"})
        ax.annotate("2 at p = 0.5",(.5,2),xytext=(.02,2.2),fontsize=16,
                    arrowprops={"arrowstyle":"-","color":"#64748B"})
        title,footer="Small p amplifies probability sensitivity","The derivative is negative; this plot shows its magnitude."
        ax.set_xlabel("Correct-class probability p (log scale)",labelpad=14)
    elif name=="logsumexp-and-probability":
        x=np.linspace(-5,5,300)
        axes[0].plot(x,np.logaddexp(x,0),color="#059669",lw=3)
        axes[1].plot(x,1/(1+np.exp(-x)),color="#7C3AED",lw=3)
        axes[0].scatter([0],[np.log(2)],color="#D97706",s=70,zorder=5)
        axes[1].scatter([0],[.5],color="#D97706",s=70,zorder=5)
        axes[0].set_ylabel("F(x) = log(exp(x) + 1)",labelpad=12)
        axes[1].set_ylabel("F′(x): class probability",labelpad=12)
        axes[0].set_ylim(-.3,6)
        axes[1].axhline(.5,color="#94A3B8",ls=":")
        axes[1].set(xlim=(-5.2,5.2),ylim=(-.1,1.1),yticks=[0,.5,1],xticks=[-4,-2,0,2,4])
        title,footer="A log-sum-exp slope is a softmax ratio","Other logit fixed at 0; F′(0) = 1/2."
    else:
        raise ValueError(f"Unknown M01-07 figure: {name}")
    for ax in axes:
        ax.set_facecolor("#F8FAFC")
        ax.spines[["top","right"]].set_visible(False)
        ax.grid(color="#CBD5E1",lw=.7)
    axes[0].set_title(title,fontsize=20,pad=24)
    if name!="negative-log-sensitivity":
        axes[-1].set_xlabel("Input x",labelpad=14)
    fig.patch.set_facecolor("#F8FAFC")
    fig.text(.5,.075 if pair else .09,footer,ha="center",color="#334155",fontsize=16)
    fig.subplots_adjust(left=.2 if pair else .18,right=.94,bottom=.21 if pair else .24,top=.87 if pair else .83,hspace=.26)
    output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"mmi"})
    plt.close(fig)


if __name__=="__main__":
    main()
