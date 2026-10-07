#!/usr/bin/env python3
"""Loss on one positive outcome: bounded Brier versus unbounded log penalty."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-15-penalty"})
    q=np.linspace(.005,1,500);fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC");ax.plot(q,-np.log(q),color="#7C3AED",linewidth=3,label="log loss: −log q");ax.plot(q,(1-q)**2,color="#2563EB",linewidth=3,label="Brier: (1 − q)²");ax.set(xlim=(0,1.03),ylim=(-.04,5.5),xlabel="reported positive probability q",ylabel="loss for realized y = 1");ax.set_xticks([0,.5,1]);ax.set_title("One realized positive outcome\nDifferent penalty shapes",fontsize=24,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=24);fig.subplots_adjust(left=.2,right=.95,top=.84,bottom=.28)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
