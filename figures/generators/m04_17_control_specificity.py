#!/usr/bin/env python3
"""Constructed control contrasts, not empirical neural-model measurements."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":20,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-17-controls"})
    fig,axes=plt.subplots(1,2,figsize=(11,7.8),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax,target,random,title in zip(axes,[[-8,-3],[-8,0]],[[-7,-3],[-1,0]],["Generic damage remains plausible","A more selective pattern"]):
        y=np.array([1,0]);ax.barh(y+.17,target,height=.3,color="#D97706",hatch="//",label="target direction");ax.barh(y-.17,random,height=.3,color="#2563EB",hatch="..",label="norm-matched random")
        for values,offset in [(target,.17),(random,-.17)]:
            for yi,value in zip(y,values):ax.text(value-.25 if value<0 else -.25,yi+offset,str(value),ha="right",va="center",fontsize=18,color="#334155")
        ax.set(xlim=(-10,.7),ylim=(-.65,1.65),xlabel="accuracy change (pp)");ax.set_yticks(y,labels=["Target task","Unrelated task"]);ax.set_title(title,fontsize=18,fontweight="bold",pad=24);ax.axvline(0,color="#64748B",linewidth=1);ax.set_facecolor("#F8FAFC");ax.grid(axis="x",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.tick_params(labelsize=18);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.16),frameon=False,fontsize=16)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
