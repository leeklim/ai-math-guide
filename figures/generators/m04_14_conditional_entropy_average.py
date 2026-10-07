#!/usr/bin/env python3
"""Conditional entropies may individually rise although their average is no larger."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def entropy(p):return -np.sum(p[p>0]*np.log(p[p>0]))
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":18,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-14-conditional"})
    joint=np.array([[.72,.08],[.1,.1]]);px=joint.sum(axis=1);py=joint.sum(axis=0);conditional=joint/py;hc=np.array([entropy(conditional[:,i]) for i in range(2)]);hx=entropy(px)
    fig,axes=plt.subplots(1,3,figsize=(13.5,6.5),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax,p,title in [(axes[0],px,f"Before observing Y\nH(X) ≈ {hx:.3f}"),(axes[1],conditional[:,0],f"Observe Y=0; mass 0.82\nH(X ∣ Y=0) ≈ {hc[0]:.3f}"),(axes[2],conditional[:,1],f"Observe Y=1; mass 0.18\nH(X ∣ Y=1) ≈ {hc[1]:.3f}")]:
        ax.set_facecolor("#F8FAFC");ax.bar([0,1],p,color=["#2563EB","#D97706"],width=.5);ax.set_xticks([0,1],labels=["X=0","X=1"]);ax.set(ylim=(0,1.05),ylabel="probability");ax.set_title(title,fontsize=17)
        for x,value in enumerate(p):ax.text(x,value+.035,f"{value:.3f}",ha="center",fontsize=16)
        ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    fig.suptitle(f"Average H(X ∣ Y) = 0.82 × {hc[0]:.3f} + 0.18 × {hc[1]:.3f} ≈ {np.dot(py,hc):.3f}",fontsize=20,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
