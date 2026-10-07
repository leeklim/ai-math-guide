"""Exact finite sign averages and Euclidean norm illustrations."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-lrn-05-rademacher","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,box):
    ax=fig.add_axes(box,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def main(output):
    key=output.stem.removeprefix("A09-LRN-05-");h=1400 if key in ["finite-sign-suprema","equal-norm-different-geometry","squared-loss-bounded-slope"] else 1100
    fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="finite-sign-suprema":
        x=np.arange(4);z=np.array([1,0,0,-1])
        ax=axes(fig,(.23,.57,.65,.22));ax.plot(x,z,"o-",color=BLUE,lw=2);ax.plot(x,-z,"s--",color=PURPLE,lw=2);ax.set(ylim=(-1.25,1.25),ylabel="Sign score",xlabel="Sign vector");ax.set_xticks(x,["++","+−","−+","−−"]);ax.set_yticks([-1,0,1])
        bx=axes(fig,(.23,.19,.65,.22));bx.bar(x,abs(z),color=GREEN,alpha=.8);bx.axhline(.5,color=AMBER,ls="--",lw=2);bx.set(ylim=(0,1.2),ylabel="Per-sign supremum",xlabel="Sign vector");bx.set_xticks(x,["++","+−","−+","−−"]);bx.set_yticks([0,.5,1])
        fig.text(.077,.95,"Fixed f: blue circle; −f: purple square",fontsize=22);fig.text(.077,.89,"Both fixed-function means are 0.",fontsize=25);fig.text(.077,.47,"Choose the larger score for each sign",fontsize=23);fig.text(.077,.08,"Then average: (1 + 0 + 0 + 1)/4",fontsize=24);fig.text(.077,.035,"Empirical complexity = 1/2",fontsize=27,color=AMBER)
    elif key=="unit-ball-sign-alignment":
        ax=axes(fig,(.23,.29,.65,.44));theta=np.linspace(0,2*np.pi,300);ax.plot(np.cos(theta),np.sin(theta),color=GRAY,lw=2);ax.set_aspect("equal");ax.axhline(0,color=GRAY,lw=1);ax.axvline(0,color=GRAY,lw=1);s=np.array([2.,1.]);w=s/np.linalg.norm(s)
        for v,col in [(s,BLUE),(w,PURPLE)]:ax.annotate("",v,(0,0),arrowprops=dict(arrowstyle="->",color=col,lw=2.5,mutation_scale=11,shrinkA=0,shrinkB=0))
        ax.text(1.5,1.45,"s = (2, 1)",color=BLUE,fontsize=24,ha="center");ax.text(.48,-.55,"w*",color=PURPLE,fontsize=28);ax.set(xlim=(-1.2,2.6),ylim=(-1.2,1.8),xlabel="Coordinate 1",ylabel="Coordinate 2");ax.set_xticks([-1,0,1,2]);ax.set_yticks([-1,0,1])
        fig.text(.077,.95,"Maximize w · s on a unit ball",fontsize=27);fig.text(.077,.87,"s is a fixed illustrative sign sum.",fontsize=24);fig.text(.077,.80,"B = 1; w* = s / ‖s‖₂",fontsize=28,color=PURPLE);fig.text(.077,.16,"Maximum inner product = √5",fontsize=27);fig.text(.077,.10,"The circle bounds ‖w‖₂.",fontsize=27);fig.text(.077,.05,"Divide by n; then average over signs.",fontsize=23,color=GRAY)
    elif key=="equal-norm-different-geometry":
        for y,aligned in [(.56,True),(.18,False)]:
            ax=axes(fig,(.23,y,.65,.22));ax.axhline(0,color=GRAY,lw=1);ax.axvline(0,color=GRAY,lw=1);ax.set_aspect("equal")
            pts=[(-2,0),(0,0),(2,0)] if aligned else [(-1,-1),(-1,1),(1,-1),(1,1)]
            for x,z in pts:
                ax.plot([0,x],[0,z],color=GRAY,lw=1.3,ls="--");ax.scatter([x],[z],s=170 if aligned and x==0 else 85,color=PURPLE,zorder=4)
            ax.set(xlim=(-2.3,2.3),ylim=(-1.7,1.7),xlabel="Sign-sum coordinate 1",ylabel="Coordinate 2");ax.set_xticks([-2,0,2]);ax.set_yticks([-1,0,1]);fig.text(.077,y+.265,"Aligned inputs" if aligned else "Orthogonal inputs",fontsize=28)
        fig.text(.077,.96,"B = 1; n = 2; each input norm 1",fontsize=25);fig.text(.077,.90,"Possible sums σ₁x₁ + σ₂x₂",fontsize=27);fig.text(.077,.47,"Aligned: norms 2, 0, 0, 2 → R̂ = 1/2",fontsize=22);fig.text(.077,.08,"Orthogonal: all norms √2 → R̂ = √2/2",fontsize=22);fig.text(.077,.035,"Common upper bound = 1/√2",fontsize=27,color=GREEN)
    elif key=="norm-scale-sample-bound":
        ax=axes(fig,(.23,.29,.65,.44));n=np.linspace(10,1000,300);ax.plot(n,1/np.sqrt(n),color=GREEN,lw=2);ax.plot(n,2/np.sqrt(n),color=PURPLE,lw=2,ls="--");ax.set_xscale("log");ax.set(xlim=(10,1000),ylim=(0,.7),xlabel="Sample count n",ylabel="Upper bound");ax.set_xticks([10,100,1000],["10","100","1000"]);ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator());ax.set_yticks([0,.2,.4,.6])
        fig.text(.077,.95,"Bound BC / √n, not exact complexity",fontsize=23);fig.text(.077,.87,"B = 1, C = 1  —",fontsize=28,color=GREEN);fig.text(.077,.80,"B = 2, C = 1  - -",fontsize=28,color=PURPLE);fig.text(.077,.16,"B = 1, C = 2: same dashed line",fontsize=26,color=PURPLE);fig.text(.077,.10,"Scale changes the class/sample bound.",fontsize=23);fig.text(.077,.05,"Other conditions stay fixed.",fontsize=27,color=GRAY)
    elif key=="squared-loss-bounded-slope":
        t=np.linspace(-3,3,300)
        for y,slope in [(.56,False),(.18,True)]:
            ax=axes(fig,(.23,y,.65,.22));ax.axvspan(-1,1,color=GREEN,alpha=.16);ax.plot(t,2*abs(t) if slope else t*t,color=PURPLE,lw=2);ax.set(xlim=(-3,3),xlabel="Prediction t",ylabel="Absolute slope" if slope else "Loss t²");ax.set_xticks([-3,-1,0,1,3]);ax.set_yticks([0,2,4,6] if slope else [0,3,6,9])
            if slope:ax.axhline(2,color=AMBER,ls="--",lw=2)
        fig.text(.077,.96,"Squared loss needs a prediction range",fontsize=23);fig.text(.077,.90,"Label y = 0; shaded range [−1, 1]",fontsize=24);fig.text(.077,.47,"Within the range: |2t| ≤ 2",fontsize=27,color=GREEN);fig.text(.077,.08,"Outside the range, L = 2 need not hold.",fontsize=22);fig.text(.077,.035,"No finite global slope bound.",fontsize=27,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
