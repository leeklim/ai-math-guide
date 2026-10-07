#!/usr/bin/env python3
"""Stacked class contributions show asymmetric roles in cross entropy."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-12-direction"})
    p=np.array([.75,.25]);q=np.array([.5,.5]);terms=np.array([-p*np.log(p),-p*np.log(q),-q*np.log(p)])
    fig,ax=plt.subplots(figsize=(7.2,9));fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.bar([0,1,2],terms[:,0],color="#2563EB",width=.55,label="first outcome contribution");ax.bar([0,1,2],terms[:,1],bottom=terms[:,0],color="#D97706",width=.55,label="second outcome contribution")
    for x,total in enumerate(terms.sum(axis=1)):ax.text(x,total+.035,f"{total:.3f}",ha="center",fontsize=25)
    ax.set(xlim=(-.5,2.5),ylim=(0,1.03),ylabel="average log-loss (nats)");ax.set_xticks([0,1,2],labels=["H(p)","H(p,q)","H(q,p)"]);ax.set_title("p = (0.75, 0.25)\nq = (0.5, 0.5)",fontsize=25,fontweight="bold");ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False)
    ax.legend(loc="upper center",bbox_to_anchor=(.5,-.16),frameon=False,fontsize=20);fig.subplots_adjust(left=.22,right=.95,top=.84,bottom=.27)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
