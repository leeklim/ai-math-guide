#!/usr/bin/env python3
"""Forward KL diverges when a positive target mass loses model support."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-13-support"})
    e=np.geomspace(1e-6,.5,500);forward=.5*np.log(.5/(1-e))+.5*np.log(.5/e);reverse=(1-e)*np.log((1-e)/.5)+e*np.log(e/.5)
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.plot(e,forward,color="#7C3AED",linewidth=3,label="KL(p ∥ q)");ax.plot(e,reverse,color="#2563EB",linewidth=3,label="KL(q ∥ p)");ax.set_xscale("log");ax.set_xticks([1e-6,1e-4,1e-2,.5],labels=["10⁻⁶","10⁻⁴",".01",".5"])
    ax.set(xlim=(1e-6,.5),ylim=(-.03,6.6),xlabel="q second-outcome mass ε",ylabel="KL divergence (nats)");ax.set_title("p = (0.5, 0.5); q = (1−ε, ε)\nε = 0 is not drawn",fontsize=23,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=24);fig.subplots_adjust(left=.2,right=.95,top=.84,bottom=.28)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
