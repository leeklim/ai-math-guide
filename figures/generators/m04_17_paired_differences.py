#!/usr/bin/env python3
"""Four paired scores with exactly the lesson's four differences."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":20,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-17-pairs"})
    b=np.array([.7,.6,.4,.2]);d=np.array([.1,.04,-.02,.08]);a=b+d;y=np.arange(4,0,-1)
    fig,axes=plt.subplots(1,2,figsize=(11,7.8),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for yi,ai,bi in zip(y,a,b):axes[0].plot([bi,ai],[yi,yi],color="#7C3AED",linewidth=2)
    axes[0].scatter(a,y,color="#D97706",s=80,marker="s",label="method A");axes[0].scatter(b,y,color="#2563EB",s=80,marker="o",label="method B");axes[0].set(xlim=(0,1),xlabel="score on the same prompt");axes[0].set_title("Common prompt difficulty remains\nin raw scores",fontsize=19,fontweight="bold");axes[0].legend(loc="upper center",bbox_to_anchor=(.5,-.16),frameon=False,fontsize=18,ncol=2)
    axes[1].hlines(y,0,d,color="#059669",linewidth=2);axes[1].scatter(d,y,color="#059669",s=80);axes[1].axvline(0,color="#64748B",linewidth=1);axes[1].axvline(d.mean(),color="#7C3AED",linestyle="--",linewidth=2,label="mean difference = .05");axes[1].set(xlim=(-.07,.14),xlabel="paired difference A−B");axes[1].set_xticks([-.04,0,.04,.08,.12]);axes[1].set_title("Pair first, then average\nD = (.10,.04,−.02,.08)",fontsize=19,fontweight="bold");axes[1].legend(loc="upper center",bbox_to_anchor=(.5,-.16),frameon=False,fontsize=18)
    for ax in axes:ax.set_ylim(.45,4.55);ax.set_yticks(y,labels=["Prompt 1","Prompt 2","Prompt 3","Prompt 4"]);ax.set_facecolor("#F8FAFC");ax.grid(axis="x",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.tick_params(labelsize=18)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
