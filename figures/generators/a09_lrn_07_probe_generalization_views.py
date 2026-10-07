"""Illustrative fixed activation geometry and exact prompt-weight calculations."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-lrn-07-probe","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,box):
    ax=fig.add_axes(box,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def main(output):
    key=output.stem.removeprefix("A09-LRN-07-");h=1400 if key=="class-relative-readout-geometry" else 1100;fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="class-relative-readout-geometry":
        for y,nonlinear in [(.56,False),(.18,True)]:
            ax=axes(fig,(.23,y,.65,.22));ax.set_aspect("equal");ax.axhline(0,color=GRAY,lw=1);ax.axvline(0,color=GRAY,lw=1)
            if nonlinear:
                ax.fill_between([0,1.5],0,1.5,color=GREEN,alpha=.16);ax.fill_between([-1.5,0],-1.5,0,color=GREEN,alpha=.16)
            else:ax.plot([-1,1],[-1,1],color=PURPLE,lw=1.6,ls="--");ax.plot([-1,1],[1,-1],color=AMBER,lw=1.6,ls=":");ax.scatter([0],[0],s=120,facecolors=BG,edgecolors=GRAY,lw=2,zorder=4)
            for x,z,label in [(-1,-1,1),(1,1,1),(-1,1,0),(1,-1,0)]:ax.scatter([x],[z],s=100,color=PURPLE if label else AMBER,marker="o" if label else "s",zorder=5)
            ax.set(xlim=(-1.5,1.5),ylim=(-1.5,1.5),xlabel="Activation coordinate 1",ylabel="Coordinate 2");ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);fig.text(.077,y+.26,"Crossing same-label segments" if not nonlinear else "Nonlinear readout: 1[x₁x₂ > 0]",fontsize=24)
        fig.text(.077,.96,"Fixed activation points; same labels",fontsize=24);fig.text(.077,.90,"1: purple circle; 0: orange square",fontsize=24);fig.text(.077,.47,"Both class-segment centers are (0, 0).",fontsize=23);fig.text(.077,.08,"Shaded quadrants predict label 1.",fontsize=25);fig.text(.077,.035,"Class-relative illustration; no probe run.",fontsize=22,color=GRAY)
    elif key=="preprocessing-test-information":
        ax=axes(fig,(.23,.29,.65,.44));ax.scatter([-1,1],[.7,.7],s=100,color=BLUE,zorder=4);ax.scatter([9,11],[.3,.3],s=100,color=GREEN,marker="s",zorder=4);ax.axvline(0,color=BLUE,lw=2,ls="--");ax.axvline(5,color=AMBER,lw=2,ls=":");ax.set(xlim=(-2,12),ylim=(0,1),xlabel="Input value");ax.set_xticks([-1,5,9,11]);ax.set_yticks([.3,.7],["Test","Train"]);ax.set_ylabel("Data subset")
        fig.text(.077,.95,"Fit the transform without test data",fontsize=25);fig.text(.077,.87,"Train: (−1, 1); mean 0  - -",fontsize=27,color=BLUE);fig.text(.077,.80,"Test: (9, 11); pooled mean 5  · ·",fontsize=24,color=AMBER);fig.text(.077,.16,"Pooling changes the fitted center.",fontsize=25);fig.text(.077,.10,"Even without using any label.",fontsize=27);fig.text(.077,.05,"Apply the fixed train-fitted rule to test.",fontsize=22,color=GRAY)
    elif key=="token-versus-prompt-weights":
        ax=axes(fig,(.23,.29,.65,.44));a=np.array([.075,.05]);b=np.array([.225,.45]);ax.bar([0,1],a,color=BLUE,alpha=.8);ax.bar([0,1],b,bottom=a,facecolor="#D1FAE5",hatch="///",edgecolor=GREEN,lw=1.4);ax.set(ylim=(0,.6),ylabel="Weighted mean loss");ax.set_xticks([0,1],["Token mean","Prompt mean"]);ax.set_yticks([0,.1,.3,.5]);ax.set_xlabel("Averaging target")
        fig.text(.077,.95,"Different lengths change the weights",fontsize=24);fig.text(.077,.87,"Illustrative P₁: 3 rows, mean loss 0.1",fontsize=23,color=BLUE);fig.text(.077,.80,"P₂: 1 row, mean loss 0.9  (hatched)",fontsize=23,color=GREEN);fig.text(.077,.16,"Token mean: (3×0.1 + 1×0.9)/4 = 0.3",fontsize=22);fig.text(.077,.10,"Prompt mean: (0.1 + 0.9)/2 = 0.5",fontsize=24);fig.text(.077,.05,"Specify the risk weighting before analysis.",fontsize=22,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
