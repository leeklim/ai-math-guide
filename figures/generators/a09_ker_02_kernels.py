"""Reproduce finite Gram, PSD, and bandwidth geometry examples."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE,PURPLE,GREEN,RED="#2563EB","#7C3AED","#059669","#DC2626"
GRAY,GRID="#64748B","#D9E2EF"


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();name=args.output.stem.removeprefix("A09-KER-02-")
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none",
        "svg.hashsalt":"a09-ker-02","axes.spines.top":False,"axes.spines.right":False})
    normal=name in {"null-direction","gaussian-bandwidth"}
    count=3 if name in {"quadratic-signs","kernel-profiles"} else 2
    if normal:
        fig,ax=plt.subplots(figsize=(7.2,10));axes=[ax]
        fig.subplots_adjust(left=.25,right=.93,bottom=.38,top=.76)
    else:
        fig,axes=plt.subplots(1,count,figsize=(7*count,8.8))
        fig.subplots_adjust(left=.08 if count==3 else .12,right=.96,bottom=.34,top=.74,wspace=.55)
    if name in {"gram-samples","duplicate-input"}:
        samples=[[1,2],[-1,1]] if name=="gram-samples" else [[1,2],[1,1]]
        for ax,points in zip(axes,samples):
            k=np.outer(points,points)
            ax.pcolormesh(np.arange(3),np.arange(3),k,cmap="PuBu",vmin=-1,vmax=4,edgecolors=GRID,lw=2)
            ax.set_aspect("equal");ax.invert_yaxis()
            ax.set_xticks([.5,1.5],[f"x₁={points[0]}",f"x₂={points[1]}"])
            ax.set_yticks([.5,1.5],[f"x₁={points[0]}",f"x₂={points[1]}"])
            ax.set_xlabel("column input",fontsize=23);ax.set_ylabel("row input",fontsize=23)
            for i in range(2):
                for j in range(2):ax.text(j+.5,i+.5,str(k[i,j]),ha="center",va="center",fontsize=28,color="white" if k[i,j]>=3 else "#0F172A")
            ax.set_title(f"Same k(x,z)=xz\nsamples {points}",fontsize=23,pad=25)
        if name=="gram-samples":
            footer="Change the sample, not the kernel: each entry is a row–column product.\nNegative off-diagonal values can still come from a PSD kernel."
        else:
            footer="Repeated input gives repeated rows and columns.\nFor the right matrix, c=(1,−1) ≠ 0 gives cᵀKc=0: not strictly PD."
        fig.text(.5,.10,footer,ha="center",fontsize=23)
    elif name=="quadratic-signs":
        theta=np.linspace(0,2*np.pi,400);c=np.stack([np.cos(theta),np.sin(theta)],axis=1)
        matrices=[np.array([[1,-1],[-1,1]]),np.array([[1,2],[2,1]]),np.array([[1,2],[2,4]])]
        titles=["Negative entries, PSD\nK=[[1,−1],[−1,1]]","Positive entries, NOT PSD\nK=[[1,2],[2,1]]","Rank-one PSD\nK=[[1,2],[2,4]]"]
        for ax,k,title in zip(axes,matrices,titles):
            q=np.einsum("ni,ij,nj->n",c,k,c)
            ax.plot(theta,q,color=RED if np.min(q)<-.1 else GREEN,lw=3)
            ax.axhline(0,color=GRAY,lw=1.5);ax.set_ylim(-1.5,5.5)
            ax.set_xticks([0,np.pi,2*np.pi],["0","π","2π"]);ax.grid(color=GRID)
            ax.set_xlabel("coefficient angle θ",fontsize=23);ax.set_ylabel("cᵀKc",fontsize=23)
            ax.set_title(title,fontsize=23,pad=25)
        fig.text(.5,.10,"c=(cos θ,sin θ): test all unit coefficient directions in this 2D example.\nPSD constrains the whole quadratic form, not the sign of each entry.",ha="center",fontsize=23)
    elif name=="null-direction":
        c1,c2=np.meshgrid(np.linspace(-3,3,160),np.linspace(-2,2,160))
        q=(c1+2*c2)**2
        ax.contour(c1,c2,q,levels=[1,4,9],colors=[BLUE,PURPLE,GREEN],linewidths=2)
        ax.plot([-3,3],[1.5,-1.5],"--",color=GRAY,lw=2)
        ax.annotate("",xy=(2,-1),xytext=(0,0),arrowprops={"arrowstyle":"->","lw":3,"color":GREEN,"mutation_scale":13,"shrinkA":0,"shrinkB":0})
        ax.set_xlim(-3,3);ax.set_ylim(-2,2);ax.set_aspect("equal");ax.grid(color=GRID)
        ax.set_xlabel("coefficient c₁",fontsize=26);ax.set_ylabel("coefficient c₂",fontsize=26)
        ax.set_title("K=[[1,2],[2,4]]\nq(c)=(c₁+2c₂)²",fontsize=26,pad=25)
        fig.text(.5,.14,"Green c=(2,−1) lies on q=0.\nDashed line: every point has q=0.\nEigenvalues 0,5: PSD, not strictly PD.",ha="center",fontsize=24)
    elif name=="gaussian-bandwidth":
        fig.subplots_adjust(bottom=.44)
        d=np.linspace(-2,2,220)
        for sigma,color,ls in [(.25,BLUE,"-"),(1,PURPLE,"--")]:
            ax.plot(d,np.exp(-d*d/(2*sigma*sigma)),color=color,ls=ls,lw=3,label=f"σ={sigma}")
        ax.set_ylim(-.05,1.12);ax.set_xticks([-2,-1,0,1,2]);ax.set_yticks([0,.5,1]);ax.grid(color=GRID)
        ax.set_xlabel("displacement z−x",fontsize=26);ax.set_ylabel("Gaussian k(x,z)",fontsize=25)
        ax.set_title("Same displacement,\ndifferent bandwidth",fontsize=26,pad=25)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.17),fontsize=25,frameon=False)
        fig.text(.5,.075,"Both peak at 1 when z=x.\nSmall σ concentrates similarity\nnear the anchor input.",ha="center",fontsize=24)
    elif name=="kernel-profiles":
        z=np.linspace(-2,2,250)
        vals=[z,(1+z)**2,np.exp(-(z-1)**2/2)]
        titles=["Linear: k(1,z)=z","Polynomial: (1+z)²","Gaussian: σ=1, x=1"]
        for ax,value,title in zip(axes,vals,titles):
            ax.plot(z,value,color=PURPLE,lw=3);ax.axhline(0,color=GRAY,lw=1)
            ax.set_xticks([-2,0,1,2]);ax.grid(color=GRID)
            ax.set_xlabel("second input z",fontsize=23);ax.set_ylabel("kernel value",fontsize=23)
            ax.set_title(title,fontsize=23,pad=25)
        fig.text(.5,.10,"One anchor x=1, three different geometries.\nPolynomial includes feature products; Gaussian depends on distance, not raw dot product.",ha="center",fontsize=23)
    else:raise ValueError(name)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,format="svg",metadata={"Date":None});plt.close(fig)


if __name__=="__main__":main()
