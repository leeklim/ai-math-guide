#!/usr/bin/env python3
"""Exact K and V storage growth for the lesson's single-layer toy shape."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args();mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-n05-22-growth"})
    length=np.arange(1,5);each=4*length;fig,ax=plt.subplots(figsize=(7.2,9),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.bar(length,each,color="#2563EB",label="K",width=.55);ax.bar(length,each,bottom=each,color="#059669",label="V",width=.55)
    for i,v in zip(length,2*each):ax.text(i,v+1,str(v),ha="center",fontsize=28)
    ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False);ax.set(xlabel="cached sequence length T",ylabel="stored elements (K + V)",ylim=(0,39));ax.set_xticks(length);ax.set_yticks([0,8,16,24,32]);ax.legend(loc="upper left",frameon=False,fontsize=26);ax.set_title("Each new token adds 8 entries\nL=1, B=1, h_kv=1, dₕ=4",fontsize=24,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__=="__main__":main()
