#!/usr/bin/env python3
"""Same predicted labels and correctness, different reported confidence."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-15-accuracy"})
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC");ax.bar([0,1],[.7,.99],color=["#2563EB","#7C3AED"],width=.5);ax.axhline(.7,color="#059669",linestyle="--",linewidth=2,label="accuracy: 7/10 for both")
    ax.set(ylim=(0,1.1),ylabel="top-label confidence");ax.set_xticks([0,1],labels=["model A","model B"]);ax.set_title("Same ten predicted labels\nSame seven correct predictions",fontsize=24,fontweight="bold");ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.15),frameon=False,fontsize=22);fig.subplots_adjust(left=.2,right=.95,top=.84,bottom=.22)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
