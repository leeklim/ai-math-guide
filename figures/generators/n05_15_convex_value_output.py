#!/usr/bin/env python3
"""A concrete attention row locates its output inside the value triangle."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--output",required=True,type=Path); args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-n05-15-convex"})
    values=np.array([[0.,0.],[2.,0.],[0.,2.]]); weights=np.array([.4,.27,.33]); output=weights@values
    fig,ax=plt.subplots(figsize=(7.2,9)); fig.patch.set_facecolor("#F8FAFC"); ax.set_facecolor("#F8FAFC"); ax.fill(values[:,0],values[:,1],facecolor="#DBEAFE",edgecolor="#2563EB",linewidth=1.7,alpha=.5); ax.scatter(values[:,0],values[:,1],s=110,color="#2563EB",zorder=4); ax.scatter(*output,s=130,color="#059669",marker="D",zorder=5)
    for xy,text,label_xy in [((0,0),"v₁ = (0, 0)",(-.33,-.35)),((2,0),"v₂ = (2, 0)",(.98,-.35)),((0,2),"v₃ = (0, 2)",(.13,2.28))]: ax.text(*label_xy,text,color="#1E3A8A",fontsize=24)
    ax.annotate("o = (0.54, 0.66)",output,xytext=(.8,1.55),fontsize=24,color="#065F46",arrowprops={"arrowstyle":"-","color":"#64748B"})
    ax.set(xlim=(-.55,2.7),ylim=(-.55,2.8),xlabel="value feature 1",ylabel="value feature 2"); ax.set_xticks([0,1,2]); ax.set_yticks([0,1,2]); ax.set_aspect("equal"); ax.grid(color="#CBD5E1",linewidth=.7); ax.spines[["top","right"]].set_visible(False); ax.set_title("Nonnegative weights\n0.40 + 0.27 + 0.33 = 1",fontsize=26,fontweight="bold",pad=28); fig.subplots_adjust(left=.17,right=.96,top=.82,bottom=.15)
    args.output.parent.mkdir(parents=True,exist_ok=True); fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"}); plt.close(fig)

if __name__ == "__main__": main()
