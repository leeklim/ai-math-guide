#!/usr/bin/env python3
"""The supporting line to negative log gives the Gibbs inequality ingredient."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-13-inequality"})
    u=np.linspace(.08,3.5,500);fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.fill_between(u,1-u,-np.log(u),color="#DBEAFE");ax.plot(u,-np.log(u),color="#7C3AED",linewidth=3,label="−log u");ax.plot(u,1-u,"--",color="#059669",linewidth=2,label="1 − u");ax.scatter([1],[0],color="#D97706",s=75,zorder=4);ax.set(xlim=(.05,3.5),ylim=(-2.6,2.8),xlabel="positive ratio u = q/p",ylabel="function value");ax.set_xticks([.5,1,2,3]);ax.set_title("−log u ≥ 1 − u\nEquality only at u = 1",fontsize=25,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=24);fig.subplots_adjust(left=.2,right=.95,top=.84,bottom=.28)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
