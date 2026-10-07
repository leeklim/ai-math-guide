#!/usr/bin/env python3
"""Two queries sharing K and V still produce distinct weights and outputs."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":24,"svg.fonttype":"none","svg.hashsalt":"mmi-n05-16-shared-output"})
    q=np.eye(2);k=np.eye(2);v=2*np.eye(2);scores=q@k.T/np.sqrt(2);a=np.exp(scores);a/=a.sum(axis=1,keepdims=True);o=a@v
    fig,axes=plt.subplots(1,2,figsize=(13.5,8.8),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax in axes:ax.set_facecolor("#F8FAFC");ax.grid(color="#CBD5E1",linewidth=.7);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
    for j,color in [(0,"#7C3AED"),(1,"#A78BFA")]:
        xpos=np.arange(2)+(j-.5)*.32;axes[0].bar(xpos,a[:,j],width=.3,color=color,label=f"key {j}")
        for x,w in zip(xpos,a[:,j]):axes[0].text(x,w+.025,f"{w:.3f}",ha="center",fontsize=23)
    axes[0].set(ylim=(0,1),ylabel="attention weight");axes[0].set_xticks([0,1],labels=["q₀=(1,0)","q₁=(0,1)"]);axes[0].set_title("Different query rows",fontsize=25,pad=28);axes[0].legend(loc="upper center",bbox_to_anchor=(.5,-.18),frameon=False,fontsize=23)
    axes[1].plot([0,2],[2,0],color="#CBD5E1",linestyle="--");axes[1].scatter(v[:,0],v[:,1],s=110,color="#2563EB");axes[1].text(.1,2.18,"v₁=(0,2)",fontsize=23,color="#1E3A8A");axes[1].text(1.25,-.35,"v₀=(2,0)",fontsize=23,color="#1E3A8A")
    for i,marker,pos in [(0,"o",(1.3,.99)),(1,"D",(.25,2.45))]:axes[1].scatter(*o[i],marker=marker,color="#059669",s=110,zorder=4);axes[1].annotate(f"o{i}=({o[i,0]:.2f},{o[i,1]:.2f})",o[i],xytext=pos,color="#065F46",fontsize=23,arrowprops={"arrowstyle":"-","color":"#64748B"})
    axes[1].set(xlim=(-.4,2.8),ylim=(-.45,2.55),xlabel="value feature 1",ylabel="value feature 2");axes[1].set_xticks([0,1,2]);axes[1].set_yticks([0,1,2]);axes[1].set_aspect("equal");axes[1].set_title("Shared values, distinct outputs",fontsize=24,pad=28)
    fig.suptitle("One shared K/V head with two positions\nK = I₂, V = 2I₂, dₕ = 2",fontsize=27,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
