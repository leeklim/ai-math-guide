#!/usr/bin/env python3
"""Positive temperature changes softmax contrast, not class order."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-15-temperature"})
    t=np.linspace(.25,4,500);z=np.array([2,1,0]);scores=z[None,:]/t[:,None];ex=np.exp(scores-scores.max(axis=1,keepdims=True));q=ex/ex.sum(axis=1,keepdims=True)
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    for k,color,style in [(0,"#2563EB","-"),(1,"#7C3AED","--"),(2,"#059669",":")]:ax.plot(t,q[:,k],color=color,linestyle=style,linewidth=3,label=f"class {k+1}; logit {z[k]}")
    ax.axhline(1/3,color="#94A3B8",linewidth=1);ax.set(xlim=(.25,4),ylim=(0,1),xlabel="positive temperature T",ylabel="class probability");ax.set_xticks([.5,1,2,4]);ax.set_title("Fixed logits (2, 1, 0)\nClass 1 remains the argmax",fontsize=25,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=24);fig.subplots_adjust(left=.2,right=.95,top=.84,bottom=.34)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
