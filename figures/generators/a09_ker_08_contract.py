"""Reproduce analytic kernel-diagnostic examples without a model training run."""
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
    args=parser.parse_args();name=args.output.stem.removeprefix("A09-KER-08-")
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none",
        "svg.hashsalt":"a09-ker-08","axes.spines.top":False,"axes.spines.right":False})
    normal=name in {"target-versus-residual","two-predictions","spectrum-not-fit"}
    if normal:
        fig,ax=plt.subplots(figsize=(7.2,11));axes=[ax];fig.subplots_adjust(left=.24,right=.94,bottom=.51,top=.76)
    elif name=="permutation-controls":
        fig,axes=plt.subplots(1,3,figsize=(16,11));fig.subplots_adjust(left=.12,right=.96,bottom=.4,top=.72,wspace=.9)
    else:
        fig,axes=plt.subplots(1,2,figsize=(14.5,10.5));fig.subplots_adjust(left=.12,right=.96,bottom=.4,top=.73,wspace=.6)
    if name=="target-versus-residual":
        pos=np.array([0,1]);ax.bar(pos-.24,[2,1],width=.22,color=BLUE,label="target y")
        ax.bar(pos,[1,1],width=.22,color=GRAY,label="initial f₀")
        ax.bar(pos+.24,[1,0],width=.22,color=PURPLE,label="target residual y−f₀")
        ax.set_xticks(pos,["mode 1","mode 2"],fontsize=26);ax.set_yticks([0,1,2]);ax.set_ylim(0,2.5);ax.grid(axis="y",color=GRID)
        ax.set_ylabel("mode coefficient",fontsize=25);ax.set_title("Eigenbasis U=I\ny=(2,1), f₀=(1,1)",fontsize=24,pad=27)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.17),fontsize=24,frameon=False)
        fig.text(.5,.065,"a=Uᵀy=(2,1)\nb=Uᵀ(y−f₀)=(1,0)\nMode 2 already matches its target.",ha="center",fontsize=24)
    elif name=="eigenspace-basis":
        ax,bx=axes;s=np.sqrt(.5)
        for a in axes:
            a.set_xlim(-1.7,1.7);a.set_ylim(-1.2,1.8);a.set_aspect("equal");a.grid(color=GRID);a.set_xticks([-1,0,1]);a.set_yticks([0,1])
            a.set_xlabel("ambient coordinate 1",fontsize=23);a.set_ylabel("ambient coordinate 2",fontsize=23)
            arrow(a,(0,0),(1,0),BLUE);a.text(.2,-.55,"r=(1,0)",fontsize=23,color=BLUE)
        ax.plot([-1.5,1.5],[0,0],color=PURPLE,ls="--",lw=1.5,zorder=1);ax.plot([0,0],[-1,1.5],color=PURPLE,ls="--",lw=1.5,zorder=1)
        ax.text(1.2,.25,"u₁",fontsize=25,color=PURPLE);ax.text(.15,1.45,"u₂",fontsize=25,color=PURPLE)
        arrow(bx,(0,0),(s,s),PURPLE);arrow(bx,(0,0),(-s,s),PURPLE)
        bx.text(.85,1.05,"v₁",fontsize=25,color=PURPLE);bx.text(-1.25,1.05,"v₂",fontsize=25,color=PURPLE)
        ax.set_title("Same eigenspace: K=λI\nCoefficients (1,0)",fontsize=23,pad=27)
        bx.set_title("Basis rotated by 45°\nCoefficients (1/√2,−1/√2)",fontsize=23,pad=27)
        fig.text(.5,.10,"The vector and eigenspace are unchanged; only the basis changes.\nTotal coefficient energy: 1²+0²=(1/√2)²+(−1/√2)²=1.",ha="center",fontsize=23)
    elif name=="structure-versus-scale":
        ax,bx=axes;pos=np.array([0,1]);t=np.linspace(0,2,160)
        ax.bar(pos-.18,[2,0],width=.32,color=BLUE,label="K₀ eigenvalues")
        ax.bar(pos+.18,[6,0],width=.32,color=PURPLE,label="3K₀ eigenvalues")
        ax.set_xticks(pos,["λ₊","λ₀"],fontsize=23);ax.set_ylim(0,8);ax.set_ylabel("raw eigenvalue",fontsize=23)
        ax.set_xlabel("same eigenvector basis",fontsize=23)
        bx.plot(t,np.exp(-2*t),color=BLUE,lw=3,label="K₀: exp(−2t)")
        bx.plot(t,np.exp(-6*t),color=PURPLE,ls="--",lw=3,label="3K₀: exp(−6t)")
        bx.set_xlabel("gradient-flow time t",fontsize=23);bx.set_ylabel("same initial mode amplitude",fontsize=23)
        for a in axes:a.grid(axis="y",color=GRID);a.legend(loc="upper center",bbox_to_anchor=(.5,-.3),fontsize=22,frameon=False)
        ax.set_title("K₀=[[1,−1],[−1,1]]\nCentering leaves K₀ unchanged",fontsize=23,pad=27)
        bx.set_title("Normalized kernels agree\nRaw dynamics have different rates",fontsize=23,pad=27)
        fig.text(.5,.065,"‖K₀‖F=2; ‖3K₀‖F=6. Both divide to the same normalized matrix.\nCentered normalized drift 0 does not mean identical learning speed.",ha="center",fontsize=23)
    elif name=="zero-centered-kernel":
        k=np.ones((3,3));h=np.eye(3)-np.ones((3,3))/3;centered=h@k@h;centered[np.abs(centered)<1e-14]=0
        for ax,m,title in zip(axes,[k,centered],["K: all sample features equal\nEvery entry is 1","HKH: common component removed\nEvery entry is 0"]):
            ax.pcolormesh(np.arange(4),np.arange(4),m,cmap="PuBu",vmin=0,vmax=1,edgecolors=GRID,lw=2)
            ax.set_aspect("equal");ax.invert_yaxis();ax.set_xticks(np.arange(3)+.5,["s₁","s₂","s₃"],fontsize=24);ax.set_yticks(np.arange(3)+.5,["s₁","s₂","s₃"],fontsize=24)
            ax.set_xlabel("sample column",fontsize=23);ax.set_ylabel("sample row",fontsize=23);ax.set_title(title,fontsize=23,pad=27)
            for i in range(3):
                for j in range(3):ax.text(j+.5,i+.5,str(int(m[i,j])),ha="center",va="center",fontsize=28,color="white" if m[i,j] else "#0F172A")
        fig.text(.5,.10,"H=I−11ᵀ/3; ‖HKH‖F=0. Division by this norm is undefined.\nZero denominator: normalized kernel is undefined.",ha="center",fontsize=23)
    elif name=="two-predictions":
        t=np.linspace(0,2,200);theta=1/np.sqrt(1+4*t)
        ax.plot(t,theta**2,color=BLUE,lw=3,label="nonlinear flow f(t)")
        ax.plot(t,np.exp(-4*t),color=PURPLE,ls="--",lw=3,label="fixed K₀=4 prediction")
        ax.plot(t,1+2*(theta-1),color=GREEN,ls="-.",lw=3,label="Taylor on actual θ(t)")
        ax.axhline(0,color=GRAY,lw=1);ax.set_xticks([0,1,2]);ax.set_yticks([-.5,0,.5,1]);ax.set_ylim(-.5,1.1);ax.grid(color=GRID)
        ax.set_xlabel("gradient-flow time t",fontsize=25);ax.set_ylabel("output at x=1",fontsize=25)
        ax.set_title("Analytic toy: fθ(1)=θ²\nLoss ½f², θ₀=1, target 0",fontsize=24,pad=27)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.16),fontsize=24,frameon=False)
        fig.text(.5,.055,"θ(t)=1/√(1+4t)\nKernel flow and path Taylor differ.\nNot a measured model trajectory.",ha="center",fontsize=24)
    elif name=="permutation-controls":
        mats=[np.diag([4,1]),np.diag([4,1]),np.diag([1,4])]
        labels=[["A: y=2","B: y=0"],["A: y=0","B: y=2"],["B: y=0","A: y=2"]]
        cols=[["A","B"],["A","B"],["B","A"]]
        titles=["Original matching\nK and y aligned","Label permutation null\nK stays fixed","Matched row permutation\nK and y move together"]
        for ax,m,rows,cs,title in zip(axes,mats,labels,cols,titles):
            ax.pcolormesh(np.arange(3),np.arange(3),m,cmap="PuBu",vmin=0,vmax=4,edgecolors=GRID,lw=2)
            ax.set_aspect("equal");ax.invert_yaxis();ax.set_xticks([.5,1.5],cs,fontsize=24);ax.set_yticks([.5,1.5],rows,fontsize=22)
            ax.set_xlabel("sample column",fontsize=23);ax.set_title(title,fontsize=22,pad=27)
            for i in range(2):
                for j in range(2):ax.text(j+.5,i+.5,str(m[i,j]),ha="center",va="center",fontsize=28,color="white" if m[i,j]==4 else "#0F172A")
        fig.text(.5,.10,"Coefficient energies ordered by λ=(4,1): (4,0); (0,4); (4,0), with f₀=0.\nMatched permutation preserves association; the label null changes it.",ha="center",fontsize=23)
    elif name=="spectrum-not-fit":
        t=np.linspace(0,2,180);ax.plot(t,np.exp(-4*t),color=BLUE,lw=3,label="residual r₀=(1,0)")
        ax.plot(t,np.ones_like(t),color=PURPLE,ls="--",lw=3,label="residual r₀=(0,1)")
        ax.set_xticks([0,1,2]);ax.set_yticks([0,.5,1]);ax.set_ylim(-.05,1.1);ax.grid(color=GRID)
        ax.set_xlabel("gradient-flow time t",fontsize=25);ax.set_ylabel("residual norm ‖r(t)‖",fontsize=25)
        ax.set_title("Same fixed K=diag(4,0)\nResiduals (1,0) versus (0,1)",fontsize=24,pad=27)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.19),fontsize=24,frameon=False)
        fig.text(.5,.075,"Same spectrum; different fit.\nZero-mode residual cannot decay.\nNo unseen inputs are evaluated.",ha="center",fontsize=24)
    else:raise ValueError(name)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,format="svg",metadata={"Date":None});plt.close(fig)


if __name__=="__main__":main()
