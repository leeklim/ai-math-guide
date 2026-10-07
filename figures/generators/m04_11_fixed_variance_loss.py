#!/usr/bin/env python3
"""Common fixed Gaussian variance preserves the squared-error minimizer."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-11-fixed"})
    prediction=np.linspace(0,6,400);error=(3-prediction)**2
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.plot(prediction,error,color="#2563EB",linewidth=3,label="squared error")
    ax.plot(prediction,error/4+.5*np.log(4*np.pi),color="#7C3AED",linewidth=3,label="NLL; fixed σ² = 2")
    ax.axvline(3,color="#D97706",linestyle="--");ax.set(xlim=(0,6),ylim=(0,10),xlabel="predicted mean",ylabel="loss");ax.set_xticks([0,3,6]);ax.set_title("Target y = 3\nSame minimizing prediction",fontsize=25,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=24);fig.subplots_adjust(left=.18,right=.95,top=.85,bottom=.29)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
