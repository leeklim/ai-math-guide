#!/usr/bin/env python3
"""All six equal-probability two-of-four treatment assignments."""
import argparse
from pathlib import Path
from itertools import combinations
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-16-randomize"})
    y0=np.array([1,3,5,7]);y1=y0+2;estimates=[]
    for pair in combinations(range(4),2):
        treated=np.array(pair);control=np.array([i for i in range(4) if i not in pair]);estimates.append(y1[treated].mean()-y0[control].mean())
    values,counts=np.unique(estimates,return_counts=True);fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC");ax.bar(values,counts/6,width=.75,color="#2563EB");ax.axvline(2,color="#059669",linewidth=2,linestyle="--",label="mean = sample ATE = 2")
    ax.set(xlim=(-3,7),ylim=(0,.42),xlabel="difference in observed means",ylabel="assignment probability");ax.set_xticks(values);ax.set_yticks([0,1/6,1/3],labels=["0","1/6","1/3"]);ax.set_title("Fixed four-unit potential outcomes\nUniform two-treated assignments",fontsize=23,fontweight="bold");ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=21);fig.subplots_adjust(left=.2,right=.95,top=.84,bottom=.28)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
