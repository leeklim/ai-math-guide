#!/usr/bin/env python3
"""Soft teacher and argmax hard-label losses have different minima."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-12-soft"})
    r=np.linspace(.005,.999,500);soft=-.8*np.log(r)-.2*np.log1p(-r)
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.plot(r,soft,color="#7C3AED",linewidth=3,label="soft teacher (0.8, 0.2)");ax.plot(np.r_[r,1],-np.log(np.r_[r,1]),color="#2563EB",linewidth=3,label="hard target (1, 0)");ax.scatter([.8],[-.8*np.log(.8)-.2*np.log(.2)],color="#D97706",s=70,zorder=4);ax.scatter([1],[0],color="#D97706",s=70,zorder=4)
    ax.set(xlim=(0,1.03),ylim=(-.04,4.6),xlabel="student first-class mass",ylabel="cross entropy (nats)");ax.set_xticks([0,.5,.8,1]);ax.set_title("Changing target changes the goal\nSoft minimum at 0.8, hard at 1",fontsize=24,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.2),frameon=False,fontsize=22);fig.subplots_adjust(left=.2,right=.95,top=.84,bottom=.29)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
