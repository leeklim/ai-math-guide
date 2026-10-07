#!/usr/bin/env python3
"""Illustrative normal mean estimates with known unit SD and practical threshold."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-17-practical"})
    means=np.array([.02,.04,.2]);n=np.array([1600,4,25]);half=1.96*.1/np.sqrt(n);y=np.array([3,2,1])
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC");ax.errorbar(means,y,xerr=half,fmt="o",color="#2563EB",linewidth=2,capsize=6,markersize=8);ax.axvline(0,color="#64748B",linewidth=1.5,linestyle=":",label="zero");ax.axvline(.1,color="#D97706",linewidth=2,linestyle="--",label="practical threshold .1");ax.set(xlim=(-.075,.29),ylim=(.55,3.5),xlabel="estimated mean effect");ax.set_xticks([0,.1,.2]);ax.set_yticks(y,labels=["n=1600","n=4","n=25"]);ax.set_title("Size and uncertainty\nanswer different questions",fontsize=24,fontweight="bold",pad=24);ax.grid(axis="x",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=20);fig.subplots_adjust(left=.28,right=.95,top=.82,bottom=.29)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
