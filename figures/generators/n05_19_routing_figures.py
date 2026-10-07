#!/usr/bin/env python3
"""Visualize an identity router's regions and probability versus hard index."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args();name=args.output.stem.removeprefix("N05-19-")
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-n05-19-"+name})
    if name=="routing-plane":
        fig,ax=plt.subplots(figsize=(7.2,9),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
        ax.fill([-2,3,3],[-2,-2,3],color="#EDE9FE",zorder=0);ax.fill([-2,-2,3],[-2,3,3],color="#DBEAFE",zorder=0);ax.plot([-2,3],[-2,3],color="#64748B",linestyle="--",linewidth=1.5)
        ax.scatter([2,-1,1],[-1,2,1],color=["#7C3AED","#2563EB","#D97706"],marker="o",s=65)
        ax.text(1.1,-1.55,"(2,−1)",fontsize=24,color="#7C3AED");ax.text(-1.8,2.45,"(−1,2)",fontsize=24,color="#2563EB");ax.annotate("tie (1,1)",(1,1),xytext=(1.3,1.9),fontsize=23,color="#D97706",arrowprops={"arrowstyle":"-","color":"#64748B"})
        ax.text(.3,-.2,"expert 0\nx₀ > x₁",fontsize=24,color="#7C3AED");ax.text(-1.8,.5,"expert 1\nx₁ > x₀",fontsize=24,color="#2563EB")
        ax.set(xlim=(-2,3),ylim=(-2,3),xlabel="logit 0 = x₀",ylabel="logit 1 = x₁");ax.set_xticks([-1,0,1,2,3]);ax.set_yticks([-1,0,1,2,3]);ax.grid(color="#CBD5E1",linewidth=.7);ax.set_axisbelow(True);ax.set_aspect("equal");ax.set_title("Top-1 routing regions\nW_r = I₂",fontsize=26,fontweight="bold")
    else:
        delta=np.linspace(-4,4,401);prob=1/(1+np.exp(-delta));index=np.where(delta>=0,0,1)
        fig,axes=plt.subplots(2,1,figsize=(7.2,10),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
        axes[0].plot(delta,prob,color="#059669",linewidth=2.5);axes[0].set_title("Probability changes smoothly",fontsize=25,fontweight="bold");axes[0].set_ylabel("p(expert 0)");axes[1].step(delta,index,where="post",color="#7C3AED",linewidth=2.5);axes[1].set_title("Hard index switches at the tie",fontsize=24,fontweight="bold");axes[1].set_ylabel("selected index");axes[1].set_xlabel("logit 0 − logit 1")
        for ax in axes:ax.set_facecolor("#F8FAFC");ax.grid(color="#CBD5E1",linewidth=.7);ax.set_axisbelow(True);ax.set(xlim=(-4,4),ylim=(-.08,1.08));ax.set_xticks([-4,0,4]);ax.set_yticks([0,.5,1] if ax is axes[0] else [0,1]);ax.axvline(0,color="#94A3B8",linestyle=":");ax.spines[["top","right"]].set_visible(False)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__=="__main__":main()
