#!/usr/bin/env python3
"""Exact two-bin example: opposite calibration gap directions."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-15-reliability"})
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC");ax.plot([.5,1],[.5,1],linestyle="--",color="#64748B",linewidth=2,label="accuracy = confidence")
    for x,y,color,label in [(.7,.6,"#2563EB","bin 1: overconfidence"),(.9,1,"#D97706","bin 2: underconfidence")]:ax.plot([x,x],[x,y],color=color,linewidth=3);ax.scatter([x],[x],facecolor="#F8FAFC",edgecolor=color,s=90,zorder=4);ax.scatter([x],[y],color=color,s=90,zorder=4,label=label)
    ax.set(xlim=(.5,1.04),ylim=(.5,1.04),xlabel="mean top confidence",ylabel="bin accuracy");ax.set_xticks([.7,.9,1]);ax.set_yticks([.5,.7,.9,1]);ax.set_aspect("equal");ax.set_title("Reliability diagram\nTwo equal-size bins",fontsize=25,fontweight="bold");ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.25),frameon=False,fontsize=20);fig.subplots_adjust(left=.22,right=.95,top=.84,bottom=.35)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
