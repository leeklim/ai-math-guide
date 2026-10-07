"""Exact real-line threshold/interval illustrations and schematic uniform event."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-lrn-04-vc","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";RED="#DC2626";GRAY="#64748B";BG="#F8FAFC"
def axline(fig,y,title,points,labels,lo=None,hi=None,threshold=False):
    ax=fig.add_axes((.16,y,.73,.13),facecolor=BG);ax.set(xlim=(0,4),ylim=(-.6,.8));ax.set_yticks([]);ax.set_xticks(range(5));ax.spines["left"].set_visible(False);ax.spines["bottom"].set_position(("data",0));ax.grid(axis="x",color="#CBD5E1",alpha=.7)
    if lo is not None:
        ax.plot([lo,hi],[.12,.12],color=GREEN,lw=8,alpha=.35,zorder=2)
        for boundary in ([lo] if threshold else [lo,hi]):ax.plot([boundary,boundary],[0,.4],color=GREEN,lw=1.7,ls="--")
        if threshold:ax.annotate("",(3.97,.12),(3.55,.12),arrowprops=dict(arrowstyle="->",color=GREEN,lw=2,mutation_scale=10))
    for x,label in zip(points,labels):
        ax.scatter([x],[0],s=150,facecolors=PURPLE if label else BG,edgecolors=PURPLE,lw=2,zorder=4);ax.text(x,.50,str(label),ha="center",fontsize=28,color=PURPLE)
    fig.text(.077,y+.15,title,fontsize=26)
    return ax
def main(output):
    key=output.stem.removeprefix("A09-LRN-04-");h=1350 if key in ["threshold-two-point-patterns","interval-two-point-shattering","duplicate-threshold-outputs"] else 1100
    fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="threshold-one-point":
        fig.text(.077,.95,"One fixed point; two labelings",fontsize=27)
        for y,title,a,label in [(.60,"a = 1.5 gives label 0",1.5,0),(.25,"a = 0.5 gives label 1",.5,1)]:
            ax=axline(fig,y,title,[1],[label],a,4,threshold=True);ax.text(a,-.48,"a",fontsize=25,color=GREEN,ha="center")
        fig.text(.077,.10,"Filled 1; hollow 0; shaded x ≥ a",fontsize=24);fig.text(.077,.05,"Choose a different h for each label.",fontsize=24,color=GRAY)
    elif key=="threshold-two-point-patterns":
        fig.text(.077,.95,"Only three of four patterns",fontsize=28)
        for y,title,a,labels in [(.70,"00: a = 3",3,[0,0]),(.45,"01: a = 1.5",1.5,[0,1]),(.20,"11: a = 0.5",.5,[1,1])]:axline(fig,y,title,[1,2],labels,a,4,threshold=True)
        fig.text(.077,.09,"10 is impossible for this direction.",fontsize=24,color=RED);fig.text(.077,.045,"If x₁ is 1, then x₂ must also be 1.",fontsize=24)
    elif key=="interval-two-point-shattering":
        fig.text(.077,.96,"All four patterns on fixed points",fontsize=25)
        for y,title,lo,hi,labels in [(.74,"00: interval [3, 4]",3,4,[0,0]),(.52,"01: interval [1.5, 2.5]",1.5,2.5,[0,1]),(.30,"10: interval [0.5, 1.5]",.5,1.5,[1,0]),(.08,"11: interval [0.5, 2.5]",.5,2.5,[1,1])]:axline(fig,y,title,[1,2],labels,lo,hi)
    elif key=="interval-three-point-obstruction":
        fig.text(.077,.95,"A single interval cannot make 101",fontsize=25)
        axline(fig,.60,"Requested labels: 101",[1,2,3],[1,0,1])
        axline(fig,.25,"Cover both ends: interval [1, 3]",[1,2,3],[1,1,1],1,3)
        fig.text(.077,.10,"Containing 1 and 3 also contains 2.",fontsize=24,color=RED);fig.text(.077,.05,"The class cannot realize the request.",fontsize=24)
    elif key=="duplicate-threshold-outputs":
        fig.text(.077,.96,"Count outputs, not parameters",fontsize=28)
        for y,title,a,labels in [(.74,"a = 0.25 or 0.75: 111",.25,[1,1,1]),(.52,"a = 1.5: 011",1.5,[0,1,1]),(.30,"a = 2.5: 001",2.5,[0,0,1]),(.08,"a = 3.5: 000",3.5,[0,0,0])]:axline(fig,y,title,[1,2,3],labels,a,4,threshold=True)
    elif key=="threshold-growth-counts":
        ax=fig.add_axes((.23,.29,.65,.44),facecolor=BG);n=np.arange(1,7);ax.plot(n,n+1,"o-",color=PURPLE,lw=2);ax.plot(n,2.**n,"s--",color=AMBER,lw=2);ax.set(xlabel="Distinct input count n",ylabel="Label-vector count",ylim=(0,68));ax.set_xticks([1,2,3,4,5,6]);ax.set_yticks([0,16,32,48,64]);ax.grid(color="#CBD5E1",alpha=.7)
        fig.text(.077,.95,"Growth on ordered real-line inputs",fontsize=24);fig.text(.077,.87,"Threshold: n + 1  ○—",fontsize=28,color=PURPLE);fig.text(.077,.80,"All binary labels: 2ⁿ  □ - -",fontsize=28,color=AMBER);fig.text(.077,.16,"n = 1: 2 equals 2",fontsize=28);fig.text(.077,.10,"n = 2: 3 is smaller than 4",fontsize=28);fig.text(.077,.05,"Fixed threshold direction; VCdim = 1",fontsize=23)
    elif key=="uniform-event-selected-function":
        ax=fig.add_axes((.23,.29,.65,.44),facecolor=BG);x=np.arange(1,6);y=np.array([.02,.06,.04,.09,.03]);ax.scatter(x,y,s=100,color=PURPLE,zorder=4);ax.scatter([4],[.09],s=280,facecolors=BG,edgecolors=AMBER,lw=2.5,zorder=3);ax.axhline(.12,color=GREEN,ls="--",lw=2);ax.set(xlabel="Hypothesis index",ylabel="Absolute risk gap",ylim=(0,.15));ax.set_xticks(x);ax.set_yticks([0,.04,.08,.12]);ax.grid(color="#CBD5E1",alpha=.7)
        fig.text(.077,.95,"One event covers all h in the class",fontsize=24);fig.text(.077,.87,"Illustrative upper limit = 0.12",fontsize=26,color=GREEN);fig.text(.077,.80,"Selected h₄: gap 0.09  ○",fontsize=27,color=AMBER);fig.text(.077,.16,"The selected function is included.",fontsize=25);fig.text(.077,.10,"An upper bound is not a lower bound.",fontsize=24);fig.text(.077,.05,"Not a numerically evaluated VC bound.",fontsize=23,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
