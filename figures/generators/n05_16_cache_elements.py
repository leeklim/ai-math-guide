#!/usr/bin/env python3
"""Stack K and V storage for the lesson's exact small example."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-n05-16-cache"})
    counts=np.array([16,4,8]);fig,ax=plt.subplots(figsize=(7.2,9),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC");ax.bar(range(3),counts,color="#2563EB",width=.55,label="K");ax.bar(range(3),counts,bottom=counts,color="#059669",width=.55,label="V")
    for i,n in enumerate(counts):ax.text(i,2*n+1,f"{2*n}",ha="center",fontsize=28)
    ax.set(xlim=(-.6,2.6),ylim=(0,38),ylabel="stored elements (K + V)");ax.set_xticks(range(3),labels=["MHA\n4 KV","MQA\n1 KV","GQA\n2 KV"]);ax.set_yticks([0,8,16,24,32]);ax.set_title("Keep 4 query heads\nB=1, T=2, dₕ=2",fontsize=26,fontweight="bold");ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper right",frameon=False,fontsize=26)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
