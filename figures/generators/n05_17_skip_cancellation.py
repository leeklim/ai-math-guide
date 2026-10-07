#!/usr/bin/env python3
"""A residual identity path can be cancelled by its branch."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-n05-17-cancel"})
    x=np.linspace(-2,2,401);fig,ax=plt.subplots(figsize=(7.2,9));fig.subplots_adjust(left=.17,right=.94,bottom=.32,top=.82);fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.plot(x,x,color="#2563EB",linewidth=2,label="skip: x");ax.plot(x,-x,color="#7C3AED",linewidth=2,linestyle="--",label="branch: −x");ax.plot(x,np.zeros_like(x),color="#059669",linewidth=3,label="sum: 0")
    ax.grid(color="#CBD5E1",linewidth=.7);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False);ax.set(xlim=(-2,2),ylim=(-2.3,2.3),xlabel="input x",ylabel="value");ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2]);fig.legend(*ax.get_legend_handles_labels(),loc="lower center",bbox_to_anchor=(.5,.04),frameon=False,fontsize=24);ax.set_title("F(x) = −x\ny = x + F(x) = 0",fontsize=26,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
