#!/usr/bin/env python3
"""Forecast concentration and discrimination differ even under stipulated calibration."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":18,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-15-sharpness"})
    fig,axes=plt.subplots(1,3,figsize=(13.5,7),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    specs=[([.7],[1],"Population 1: prevalence .7\nConstant .7; no ranking"),([.5,.9],[.5,.5],"Same population 1\nTwo informative risk strata"),([.99],[1],"Different population 2\nPrevalence .99; constant .99\nSharp, no ranking")]
    for ax,(q,mass,title) in zip(axes,specs):
        ax.set_facecolor("#F8FAFC");ax.vlines(q,[0]*len(q),mass,color="#2563EB",linewidth=4);ax.scatter(q,mass,color="#2563EB",s=75,zorder=4);ax.set(xlim=(0,1.05),ylim=(0,1.15),xlabel="reported probability",ylabel="population prediction mass");ax.set_xticks([0,.5,1]);ax.set_title(title,fontsize=16);ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    fig.suptitle("All stipulated calibrated: true outcome rates equal each reported probability",fontsize=19,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
