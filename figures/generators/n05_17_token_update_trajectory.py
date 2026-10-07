#!/usr/bin/env python3
"""Plot token 0 through the lesson's two exact toy residual updates."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-n05-17-trajectory"})
    rin=np.array([1.,-1.]);wa=np.diag([.5,-.5]);wm=np.array([[0.,.25],[.25,0.]])
    mid=rin+wa@rin;out=mid+wm@mid
    fig,ax=plt.subplots(figsize=(7.2,9),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC")
    ax.axhline(0,color="#94A3B8",linewidth=1);ax.axvline(0,color="#94A3B8",linewidth=1);ax.grid(color="#CBD5E1",linewidth=.7);ax.set_axisbelow(True)
    for a,b,c in [(np.zeros(2),rin,"#2563EB"),(rin,mid,"#7C3AED"),(mid,out,"#059669")]:ax.annotate("",b,xytext=a,arrowprops={"arrowstyle":"-|>","color":c,"linewidth":2,"mutation_scale":13})
    for pt,label,pos,c in [(rin,"R_in\n(1, −1)",(.22,-1.3),"#2563EB"),(mid,"R_mid\n(1.5, −0.5)",(1.6,-.9),"#7C3AED"),(out,"R_out\n(1.375, −0.125)",(.18,.48),"#059669")]:
        ax.scatter(*pt,color=c,s=18,zorder=4);ax.annotate(label,pt,xytext=pos,color=c,fontsize=24,arrowprops={"arrowstyle":"-","color":"#64748B"})
    ax.set(xlim=(-.15,2.55),ylim=(-1.55,1.25),xlabel="feature 0",ylabel="feature 1");ax.set_xticks([0,1,2]);ax.set_yticks([-1,0,1]);ax.set_aspect("equal");ax.set_title("One token, same space\nattention then MLP",fontsize=26,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
