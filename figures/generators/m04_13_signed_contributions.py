#!/usr/bin/env python3
"""Exact forward and reverse categorical KL contributions, including negative terms."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":17,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-13-signed"})
    p=np.array([.5,.5]);q=np.array([.75,.25]);ratio=np.log(p/q);forward=p*ratio;reverse=-q*ratio
    fig,axes=plt.subplots(2,2,figsize=(11,10),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    axes[0,0].bar(np.array([1,2])-.16,p,width=.3,color="#2563EB",label="p weights");axes[0,0].bar(np.array([1,2])+.16,q,width=.3,color="#7C3AED",label="q weights");axes[0,0].set_ylim(0,1);axes[0,0].set_title("p = (0.5, 0.5), q = (0.75, 0.25)",fontsize=17);axes[0,0].legend(frameon=False,fontsize=15)
    for ax,y,title in [(axes[0,1],ratio,"Log ratios: log(p/q)"),(axes[1,0],forward,f"p-weighted terms; sum ≈ {forward.sum():.3f}"),(axes[1,1],reverse,f"q-weighted reversed terms; sum ≈ {reverse.sum():.3f}")]:
        ax.bar([1,2],y,color=["#2563EB","#D97706"],width=.55);ax.axhline(0,color="#475569",linewidth=1);ax.set_ylim(-.6,.9);ax.set_title(title,fontsize=17)
        for x,value in zip([1,2],y):ax.text(x,value+(.04 if value>=0 else -.07),f"{value:.3f}",ha="center",va="bottom" if value>=0 else "top",fontsize=16)
    for ax in axes.flat:ax.set_facecolor("#F8FAFC");ax.set_xticks([1,2],labels=["outcome 1","outcome 2"]);ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
