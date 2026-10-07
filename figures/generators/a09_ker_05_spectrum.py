"""Reproduce measure-dependent operator modes and finite-spectrum normalization."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE,PURPLE,GREEN="#2563EB","#7C3AED","#059669"
GRID,GRAY="#D9E2EF","#64748B"


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();name=args.output.stem.removeprefix("A09-KER-05-")
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none",
        "svg.hashsalt":"a09-ker-05","axes.spines.top":False,"axes.spines.right":False})
    wide=name in {"measure-weighted-operator","eigenfunction-samples","two-point-modes"}
    if wide:
        fig,axes=plt.subplots(1,2,figsize=(14.5,10.5));fig.subplots_adjust(left=.12,right=.96,bottom=.36,top=.73,wspace=.55)
    else:
        fig,ax=plt.subplots(figsize=(7.2,11));axes=[ax];fig.subplots_adjust(left=.25,right=.94,bottom=.43,top=.77)
    x=np.linspace(-1,1,200)
    if name=="l2-point-change":
        ax.plot(x,np.zeros_like(x),color=BLUE,lw=3)
        ax.scatter([0],[0],s=100,facecolors="white",edgecolors=PURPLE,lw=2,zorder=6)
        ax.scatter([0],[1],s=75,color=PURPLE,zorder=6)
        ax.set_xlim(-1.1,1.1);ax.set_ylim(-.15,1.25);ax.set_xticks([-1,0,1]);ax.set_yticks([0,1]);ax.grid(color=GRID)
        ax.set_xlabel("input x",fontsize=26);ax.set_ylabel("function value",fontsize=25)
        ax.set_title("f=0 everywhere\ng differs only at x=0",fontsize=26,pad=27)
        fig.text(.5,.13,"μ uniform on [−1,1]: μ({0})=0\nThe two functions are one L² element.\nTheir point values at 0 still differ.",ha="center",fontsize=24)
    elif name=="constant-average":
        ax.plot(x,1+x,color=BLUE,lw=3,label="f=1+x")
        ax.plot(x,np.ones_like(x),color=GREEN,ls="--",lw=3,label="Tₖf=1")
        ax.set_xlabel("remaining input x",fontsize=25);ax.set_ylabel("function value",fontsize=25)
        ax.set_xticks([-1,0,1]);ax.set_yticks([0,1,2]);ax.grid(color=GRID)
        ax.set_title("k(x,z)=1\nμ uniform on [−1,1]",fontsize=26,pad=27)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.17),fontsize=25,frameon=False)
        fig.text(.5,.065,"Average over z: Eμ[1+Z]=1\nThe output is constant in x.",ha="center",fontsize=24)
    elif name=="measure-weighted-operator":
        ax,bx=axes;points=np.array([-1,0,1]);a=np.ones(3)/3;b=np.array([.1,.8,.1])
        ax.bar(points-.12,a,width=.23,color=BLUE,label="μ₁: uniform")
        ax.bar(points+.12,b,width=.23,color=PURPLE,label="μ₂: central mass")
        ax.set_xticks([-1,0,1]);ax.set_ylim(0,1.25);ax.set_yticks([0,.5,1]);ax.set_xlabel("input support z",fontsize=24);ax.set_ylabel("probability mass",fontsize=24)
        ax.grid(axis="y",color=GRID);ax.legend(fontsize=22,frameon=False)
        ax.set_title("Same support, different μ",fontsize=24,pad=27)
        bx.plot(x,(2/3)*x,color=BLUE,lw=3,label="μ₁: λ=2/3")
        bx.plot(x,.2*x,color=PURPLE,ls="--",lw=3,label="μ₂: λ=0.2")
        bx.set_xticks([-1,0,1]);bx.set_yticks([-.5,0,.5]);bx.grid(color=GRID);bx.legend(fontsize=22,frameon=False)
        bx.set_xlabel("remaining input x",fontsize=24);bx.set_ylabel("(Tₖf)(x)",fontsize=24)
        bx.set_title("Same k=xz and f(z)=z\nTₖf(x)=Eμ[Z²]x",fontsize=24,pad=27)
        fig.text(.5,.10,"Changing μ changes the operator and eigenvalue, although k is unchanged.\nFor f(z)=z, its L² squared norm Eμ[Z²] also changes from 2/3 to 0.2.",ha="center",fontsize=23)
    elif name=="eigenfunction-samples":
        ax,bx=axes
        psi=np.sqrt(3)*x;ax.plot(x,psi,color=BLUE,lw=3,label="ψ=√3x")
        ax.plot(x,psi/3,color=GREEN,ls="--",lw=3,label="Tψ=ψ/3")
        ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.grid(color=GRID);ax.legend(fontsize=22,frameon=False)
        ax.set_xlabel("all inputs x∈[−1,1]",fontsize=23);ax.set_ylabel("function value",fontsize=23)
        ax.set_title("k=1+xz, μ uniform\n‖ψ‖L²=1; λ=1/3",fontsize=24,pad=27)
        points=np.linspace(-1,1,5);v=points/np.linalg.norm(points)
        bx.vlines(np.arange(5),0,v,color=PURPLE,lw=3);bx.scatter(np.arange(5),v,color=PURPLE,s=50,zorder=5)
        bx.set_xticks(np.arange(5),["−1","−0.5","0","0.5","1"],fontsize=22);bx.axhline(0,color=GRAY,lw=1);bx.grid(color=GRID)
        bx.set_xlabel("five sampled inputs",fontsize=23);bx.set_ylabel("vector component",fontsize=23)
        bx.set_title("Eigenvector of K/5\nEuclidean norm 1; λ=0.5",fontsize=24,pad=27)
        fig.text(.5,.10,"An eigenfunction covers the domain; a sampled vector has five entries.\nEmpirical μ differs: eigenvalue and normalization need not match.",ha="center",fontsize=23)
    elif name=="mercer-two-modes":
        fig.subplots_adjust(bottom=.49)
        for v,color,ls,label in [(np.ones_like(x),BLUE,"-","mode 1: 1"),(.5*x,PURPLE,"--","mode 2: 0.5z"),(1+.5*x,GREEN,"-.","k(0.5,z)")]:
            ax.plot(x,v,color=color,ls=ls,lw=3,label=label)
        ax.set_xlabel("second input z",fontsize=26);ax.set_ylabel("kernel contribution",fontsize=24)
        ax.set_xticks([-1,0,1]);ax.set_yticks([-.5,0,1,1.5]);ax.grid(color=GRID)
        ax.set_title("k(x,z)=1+xz\nx=0.5; μ uniform [−1,1]",fontsize=25,pad=27)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.145),fontsize=24,frameon=False)
        fig.text(.5,.065,"λ₁=1, ψ₁=1; λ₂=1/3, ψ₂=√3x\nλ₂ψ₂(0.5)ψ₂(z)=0.5z",ha="center",fontsize=23)
    elif name=="two-point-modes":
        for ax,mode,eig,title in zip(axes,[np.array([1,1]),np.array([1,-1])],[.8,.2],["Constant mode","Contrast mode"]):
            pos=np.array([0,1]);ax.vlines(pos-.06,0,mode,color=BLUE,lw=3);ax.scatter(pos-.06,mode,color=BLUE,s=60,label="ψ",zorder=5)
            ax.vlines(pos+.06,0,eig*mode,color=GREEN,lw=3);ax.scatter(pos+.06,eig*mode,color=GREEN,marker="s",s=50,label="Tψ",zorder=5)
            ax.set_xticks([0,1],["x₁","x₂"]);ax.set_ylim(-1.3,1.4);ax.set_xlim(-.4,1.4);ax.set_yticks([-1,0,1]);ax.grid(color=GRID)
            ax.set_xlabel("two-point domain",fontsize=24);ax.set_ylabel("function value",fontsize=24);ax.legend(fontsize=23,frameon=False)
            ax.set_title(f"{title}\nTψ={eig:g}ψ",fontsize=24,pad=27)
        fig.text(.5,.10,"K=[[1,0.6],[0.6,1]], μ(x₁)=μ(x₂)=1/2: T=K/2.\nBoth input modes have L² norm 1, but Euclidean vector norm √2.",ha="center",fontsize=23)
    elif name=="gram-normalization":
        ax.bar(np.array([0,1])-.16,[1.6,.4],width=.3,color=BLUE,label="K")
        ax.bar(np.array([0,1])+.16,[.8,.2],width=.3,color=GREEN,label="K/2")
        ax.set_xticks([0,1],["constant\nmode","contrast\nmode"],fontsize=25);ax.set_ylim(0,1.9);ax.set_yticks([0,.4,.8,1.6]);ax.grid(axis="y",color=GRID)
        ax.set_ylabel("eigenvalue",fontsize=26);ax.set_title("Sum matrix versus average\nSame two-point kernel, ρ=0.6",fontsize=24,pad=27)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.19),fontsize=25,frameon=False)
        fig.text(.5,.09,"Operator weights are 1/2 each.\nK eigenvalues must be divided by n=2\nfor this empirical integral operator.",ha="center",fontsize=24)
    elif name=="effective-dimension":
        fig.subplots_adjust(bottom=.49)
        tau=np.logspace(-2,1,240);a=4/(4+tau);b=1/(1+tau)
        for v,c,ls,label in [(a,BLUE,"-","4/(4+τ)"),(b,PURPLE,"--","1/(1+τ)"),(a+b,GREEN,"-.","d_eff(τ)")]:ax.plot(tau,v,color=c,ls=ls,lw=3,label=label)
        ax.set_xscale("log");ax.set_xticks([.01,.1,1,10],["0.01","0.1","1","10"]);ax.set_yticks([0,1,2]);ax.grid(color=GRID)
        ax.scatter([1],[1.3],color=GREEN,s=60,zorder=5)
        ax.set_xlabel("regularization scale τ",fontsize=24);ax.set_ylabel("weighted dimension",fontsize=24)
        ax.set_title("Eigenvalues (4,1)\nScale-sensitive dimension",fontsize=25,pad=27)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.145),fontsize=24,frameon=False)
        fig.text(.5,.065,"At τ=1: 0.8+0.5=1.3\nNot an integer count of nonzero modes.",ha="center",fontsize=24)
    else:raise ValueError(name)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,format="svg",metadata={"Date":None});plt.close(fig)


if __name__=="__main__":main()
