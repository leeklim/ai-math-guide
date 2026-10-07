#!/usr/bin/env python3
"""Compare one score row before and after dividing by sqrt(16)."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--output",required=True,type=Path); args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":24,"svg.fonttype":"none","svg.hashsalt":"mmi-n05-15-scale"})
    scores=np.array([0.,2.,4.,6.]); fig,axes=plt.subplots(1,2,figsize=(13.5,7.8),constrained_layout=True); fig.patch.set_facecolor("#F8FAFC")
    for ax,row,title,color in [(axes[0],scores,"Raw: (0, 2, 4, 6)","#2563EB"),(axes[1],scores/4,"Scaled: (0, 0.5, 1, 1.5)","#7C3AED")]:
        weights=np.exp(row-row.max()); weights/=weights.sum(); ax.set_facecolor("#F8FAFC"); ax.bar(np.arange(4),weights,color=color,width=.55)
        for i,p in enumerate(weights): ax.text(i,p+.025,f"{p:.3f}",ha="center",fontsize=23)
        ax.set(xlim=(-.5,3.5),ylim=(0,1.08),xlabel="key position",ylabel="attention weight"); ax.set_xticks(range(4)); ax.set_yticks([0,.5,1]); ax.grid(axis="y",color="#CBD5E1",linewidth=.7); ax.set_axisbelow(True); ax.spines[["top","right"]].set_visible(False); ax.set_title(title,fontsize=23,pad=24)
    fig.suptitle("One query row, four allowed keys\nDivide score differences by √16 = 4 before softmax",fontsize=27,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True); fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"}); plt.close(fig)

if __name__ == "__main__": main()
