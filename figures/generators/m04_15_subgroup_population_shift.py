#!/usr/bin/env python3
"""Subgroup gaps can cancel in one mixture but not after a population shift."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-15-shift"})
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC");ax.barh([3,2,1,0],[.6,1,.8,.7],height=.5,color=["#2563EB","#D97706","#059669","#7C3AED"]);ax.axvline(.8,color="#475569",linestyle="--",linewidth=2,label="all report P̂ = .8")
    ax.set(xlim=(0,1.05),ylim=(-.7,3.7),xlabel="actual positive frequency");ax.set_yticks([3,2,1,0],labels=["group A","group B","A:B=1:1","A:B=3:1"]);ax.set_xticks([0,.5,1]);ax.set_title("Same predictions; new mixture\nAggregate calibration can change",fontsize=24,fontweight="bold");ax.grid(axis="x",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=23);fig.subplots_adjust(left=.3,right=.95,top=.84,bottom=.27)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
