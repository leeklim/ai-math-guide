"""Reproduce parameter/function distance, local sensitivity, and metric comparisons."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE,PURPLE,GREEN="#2563EB","#7C3AED","#059669"
GRID,GRAY="#D9E2EF","#64748B"


def arrow(ax,start,end,color):
    ax.annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":"->","color":color,
        "lw":2.8,"mutation_scale":12,"shrinkA":0,"shrinkB":0},zorder=5)


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();name=args.output.stem.removeprefix("A09-KER-07-")
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none",
        "svg.hashsalt":"a09-ker-07","axes.spines.top":False,"axes.spines.right":False})
    normal=name=="distribution-weighting"
    if normal:
        fig,ax=plt.subplots(figsize=(7.2,11));axes=[ax];fig.subplots_adjust(left=.24,right=.94,bottom=.45,top=.74)
    elif name=="two-gram-spaces":
        fig,axes=plt.subplots(1,3,figsize=(16,10.5));fig.subplots_adjust(left=.08,right=.96,bottom=.37,top=.72,wspace=.6)
    else:
        fig,axes=plt.subplots(1,2,figsize=(14.5,10.5));fig.subplots_adjust(left=.12,right=.96,bottom=.37,top=.73,wspace=.6)
    if name=="symmetry-distance":
        ax,bx=axes;a=np.linspace(.5,10.3,240);ax.plot(a,1/a,color=GREEN,lw=3)
        ax.scatter([1,10],[1,.1],c=[BLUE,PURPLE],s=100,zorder=6)
        ax.text(1.4,1.3,"(1,1)",color=BLUE,fontsize=24);ax.text(6.8,.48,"(10,0.1)",color=PURPLE,fontsize=24)
        ax.plot([1,10],[1,.1],color=GRAY,ls="--",lw=1.6)
        ax.set_xlim(0,11);ax.set_ylim(0,2.2);ax.set_xticks([0,5,10]);ax.set_yticks([0,1,2]);ax.grid(color=GRID)
        ax.set_xlabel("parameter a",fontsize=24);ax.set_ylabel("parameter b",fontsize=24)
        ax.set_title("Level set ab=1\nSeparated parameter points",fontsize=24,pad=27)
        x=np.linspace(-1,1,120);bx.plot(x,x,color=BLUE,lw=4,label="a=b=1")
        bx.plot(x,x,color=PURPLE,ls="--",lw=2.5,label="a=10, b=0.1")
        bx.set_xlabel("input x",fontsize=24);bx.set_ylabel("output f(x)",fontsize=24);bx.grid(color=GRID)
        bx.legend(fontsize=23,frameon=False);bx.set_title("Same output function\nf(x)=x for both points",fontsize=24,pad=27)
        fig.text(.5,.10,"Parameter distance √81.81; function distance 0 under any finite-second-moment P.\nSame function does not imply the same Euclidean NTK: 2xx′ versus 100.01xx′.",ha="center",fontsize=23)
    elif name=="tangent-versus-symmetry":
        ax,bx=axes;t=np.linspace(-.55,.55,150);c=np.linspace(.45,1.7,200)
        ax.plot(c,1/c,color=GREEN,lw=3,label="symmetry (c,1/c)")
        ax.plot(1+t,1-t,color=PURPLE,ls="--",lw=3,label="straight (1+t,1−t)")
        ax.scatter([1],[1],c=BLUE,s=90,zorder=6);ax.set_xlim(.4,1.8);ax.set_ylim(.4,2.3);ax.grid(color=GRID)
        ax.set_xlabel("parameter a",fontsize=23);ax.set_ylabel("parameter b",fontsize=23)
        ax.set_title("Shared tangent at (1,1)\nDifferent finite paths",fontsize=23,pad=27)
        bx.plot(t,-t*t,color=PURPLE,lw=3,label="straight: Δf(1)=−t²")
        bx.plot(t,np.zeros_like(t),color=GREEN,ls="--",lw=3,label="symmetry: Δf(1)=0")
        bx.set_xlabel("path parameter t",fontsize=23);bx.set_ylabel("output change at x=1",fontsize=23);bx.grid(color=GRID)
        bx.set_title("First-order change is zero\nOnly the curved path preserves f",fontsize=23,pad=27)
        for a in axes:a.legend(loc="upper center",bbox_to_anchor=(.5,-.27),fontsize=22,frameon=False)
        fig.text(.5,.065,"The tangent direction (1,−1) cancels JΔθ at the reference point.\nA straight displacement still leaves a quadratic remainder.",ha="center",fontsize=23)
    elif name=="jacobian-direction-gain":
        ax,bx=axes;t=np.linspace(0,2*np.pi,220)
        for a,sx,title in [(ax,1,"Equal parameter lengths\n‖Δθ‖=1"),(bx,3,"Output changes JΔθ\nJ=diag(3,1)")]:
            a.plot(sx*np.cos(t),np.sin(t),color=GRAY,lw=2)
            arrow(a,(0,0),(sx,0),BLUE);arrow(a,(0,0),(0,1),PURPLE)
            a.set_xlim(-3.5 if sx==3 else -1.7,3.5 if sx==3 else 1.7);a.set_ylim(-1.7,1.7);a.set_aspect("equal");a.grid(color=GRID)
            a.set_xlabel("output 1" if sx==3 else "parameter 1",fontsize=23);a.set_ylabel("output 2" if sx==3 else "parameter 2",fontsize=23)
            a.set_title(title,fontsize=23,pad=27)
        fig.text(.5,.10,"Blue and purple parameter displacements both have length 1.\nTheir output lengths are 3 and 1: direction, not just parameter distance, matters.",ha="center",fontsize=23)
    elif name=="two-gram-spaces":
        j=np.array([[3,0,0],[0,1,0]]);mats=[j,j.T@j,j@j.T]
        titles=["J: 2×3\nsample × parameter","JᵀJ: 3×3\nparameter × parameter","JJᵀ: 2×2\nsample × sample"]
        for ax,m,title in zip(axes,mats,titles):
            n,d=m.shape;ax.pcolormesh(np.arange(d+1),np.arange(n+1),m,cmap="PuBu",vmin=0,vmax=9,edgecolors=GRID,lw=2)
            ax.set_aspect("equal");ax.invert_yaxis();ax.set_xticks(np.arange(d)+.5,[str(v+1) for v in range(d)],fontsize=22);ax.set_yticks(np.arange(n)+.5,[str(v+1) for v in range(n)],fontsize=22)
            ax.set_xlabel("column index",fontsize=23);ax.set_ylabel("row index",fontsize=23);ax.set_title(title,fontsize=23,pad=27)
            for i in range(n):
                for z in range(d):ax.text(z+.5,i+.5,str(m[i,z]),ha="center",va="center",fontsize=27,color="white" if m[i,z]==9 else "#0F172A")
        fig.text(.5,.10,"The positive eigenvalues 9 and 1 agree, but the vector spaces differ.\nThe third parameter direction is null; there is no third sample coordinate.",ha="center",fontsize=23)
    elif name=="reparameterized-metric":
        ax,bx=axes;t=np.linspace(0,2*np.pi,200)
        ax.plot(np.cos(t),np.sin(t),color=BLUE,lw=3,label="‖Δθ‖=1")
        bx.plot(2*np.cos(t),np.sin(t),color=PURPLE,lw=3,label="η length 1 → θ ellipse")
        bx.plot(np.cos(t),np.sin(t),color=BLUE,ls="--",lw=2,label="θ length 1")
        for a in axes:
            a.set_xlim(-2.6,2.6);a.set_ylim(-2.1,2.1);a.set_aspect("equal");a.grid(color=GRID)
            a.set_xlabel("physical displacement Δθ₁",fontsize=23);a.set_ylabel("physical displacement Δθ₂",fontsize=23)
            a.legend(loc="upper center",bbox_to_anchor=(.5,-.27),fontsize=22,frameon=False)
        ax.set_title("Original Euclidean metric\nUnit circle in θ coordinates",fontsize=23,pad=27)
        bx.set_title("θ=Bη, B=diag(2,1)\nη-unit circle mapped to θ",fontsize=23,pad=27)
        fig.text(.5,.065,"To keep the original length, use ΔηᵀBᵀBΔη=1 in the new coordinates.\nChoosing ΔηᵀΔη=1 instead selects the purple ellipse in physical θ space.",ha="center",fontsize=23)
    elif name=="reparameterized-flow":
        ax,bx=axes;x=np.linspace(-1,1,140);t=np.linspace(0,2,140)
        ax.plot(x,x,color=BLUE,lw=4,label="θ=1: fθ(x)=θx")
        ax.plot(x,x,color=PURPLE,ls="--",lw=2.5,label="η=0.5: fη(x)=2ηx")
        bx.plot(t,np.exp(-t),color=BLUE,lw=3,label="θ Euclidean flow: K=1")
        bx.plot(t,np.exp(-4*t),color=PURPLE,ls="--",lw=3,label="η Euclidean flow: K=4")
        ax.set_xlabel("input x",fontsize=23);ax.set_ylabel("initial output",fontsize=23);bx.set_xlabel("gradient-flow time t",fontsize=23);bx.set_ylabel("output at training x=1",fontsize=23)
        for a in axes:a.grid(color=GRID);a.legend(loc="upper center",bbox_to_anchor=(.5,-.27),fontsize=22,frameon=False)
        ax.set_title("Same initial function\nCoordinate relation θ=2η",fontsize=23,pad=27)
        bx.set_title("Different Euclidean gradient rules\nOne sample x=1, target 0",fontsize=23,pad=27)
        fig.text(.5,.065,"Parameter gradients at x=1 are 1 and 2, so the scalar NTKs are 1 and 4.\nExact linear-model flows for loss ½f(1)²; not a measured network run.",ha="center",fontsize=23)
    elif name=="distribution-weighting":
        pos=np.array([0,1]);ax.bar(pos-.18,[.5,.5],width=.32,color=BLUE,label="P: (0.5,0.5)")
        ax.bar(pos+.18,[1,0],width=.32,color=PURPLE,label="Q: (1,0)")
        ax.set_xticks(pos,["x₁\nΔf=0","x₂\nΔf=2"],fontsize=26);ax.set_yticks([0,.5,1]);ax.set_ylim(0,1.2);ax.grid(axis="y",color=GRID)
        ax.set_ylabel("input probability mass",fontsize=25);ax.set_title("Same two functions\nDifferent input distributions",fontsize=25,pad=27)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.19),fontsize=24,frameon=False)
        fig.text(.5,.07,"d_P²=0.5×0²+0.5×2²=2\nd_Q²=1×0²+0×2²=0\nThe second input is absent under Q.",ha="center",fontsize=24)
    elif name=="logit-shift-metrics":
        ax,bx=axes;z=np.array([1,2,0]);pos=np.arange(3);prob=np.exp(z-z.max());prob/=prob.sum()
        ax.bar(pos-.18,z,width=.32,color=BLUE,label="logits z");ax.bar(pos+.18,z+5,width=.32,color=PURPLE,label="logits z+5")
        bx.bar(pos-.18,prob,width=.32,color=BLUE,label="softmax(z)");bx.bar(pos+.18,prob,width=.32,color=PURPLE,label="softmax(z+5)")
        for a in axes:a.set_xticks(pos,["A","B","C"],fontsize=24);a.set_xlabel("same token coordinates",fontsize=23);a.grid(axis="y",color=GRID);a.legend(fontsize=22,frameon=False)
        ax.set_ylim(0,10);ax.set_ylabel("raw logit",fontsize=23);bx.set_ylim(0,1);bx.set_ylabel("probability",fontsize=23)
        ax.set_title("Raw logit distance √75\nEvery coordinate shifts by 5",fontsize=23,pad=27)
        bx.set_title("Probability distance 0\nCentered logit distance 0",fontsize=23,pad=27)
        fig.text(.5,.10,"An output metric selects which differences count.\nToken alignment is held fixed; KL direction is a separate choice.",ha="center",fontsize=23)
    else:raise ValueError(name)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,format="svg",metadata={"Date":None});plt.close(fig)


if __name__=="__main__":main()
