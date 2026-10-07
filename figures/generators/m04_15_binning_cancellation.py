#!/usr/bin/env python3
"""Average-then-absolute can hide opposite signed gaps when bins merge."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-15-cancellation"})
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC");ax.bar([0,1],[-.1,.1],color=["#2563EB","#D97706"],width=.55);ax.scatter([2],[0],color="#059669",s=90,zorder=4);ax.axhline(0,color="#475569",linewidth=1)
    ax.set(xlim=(-.5,2.5),ylim=(-.15,.15),ylabel="accuracy − confidence");ax.set_xticks([0,1,2],labels=["bin 1","bin 2","merged"]);ax.set_yticks([-.1,0,.1]);ax.set_title("Same predictions; different bins\nSplit ECE = 0.10; merged ECE = 0",fontsize=23,fontweight="bold");ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    fig.text(.5,.16,"split: (|−.1| + |+.1|)/2 = .1\nmerged: |(−.1 + .1)/2| = 0",ha="center",fontsize=22,color="#334155");fig.subplots_adjust(left=.23,right=.95,top=.84,bottom=.3)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
