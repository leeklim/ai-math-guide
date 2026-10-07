"""Reproduce restricted gains and toy metric-path controls, not model results."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, PURPLE, GREEN, ORANGE = "#2563EB", "#7C3AED", "#059669", "#D97706"
BG, GRID, GRAY = "#F8FAFC", "#D9E2EF", "#64748B"


def plane(ax, lim, ylim, ticks=None):
    ax.set_xlim(*lim);ax.set_ylim(*ylim);ax.set_aspect("equal")
    if ticks is not None:ax.set_xticks(ticks);ax.set_yticks(ticks)
    ax.grid(color=GRID);ax.axhline(0,color=GRAY,lw=1);ax.axvline(0,color=GRAY,lw=1)


def arrow(ax,start,delta,color):
    ax.annotate("",xy=np.array(start)+np.array(delta),xytext=start,
                arrowprops={"arrowstyle":"->","color":color,"lw":2.8,"mutation_scale":13,
                            "shrinkA":0,"shrinkB":0},zorder=5)


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();name=args.output.stem.removeprefix("A09-GEO-08-")
    plt.rcParams.update({"font.size":26,"font.family":"DejaVu Sans","svg.fonttype":"none",
                         "svg.hashsalt":"a09-geo-08","axes.spines.top":False,"axes.spines.right":False})
    if name=="path-refinement":
        fig,ax=plt.subplots(figsize=(7.2,9));fig.subplots_adjust(left=.25,right=.94,bottom=.31,top=.79);axes=[ax]
    elif name=="permuted-path":
        fig,axes=plt.subplots(2,1,figsize=(7.2,15));fig.subplots_adjust(left=.20,right=.94,bottom=.24,top=.87,hspace=.75)
    else:
        fig,axes=plt.subplots(1,2,figsize=(13.5,9));fig.subplots_adjust(left=.115,right=.96,bottom=.34,top=.74,wspace=.40)
    if name=="restricted-gain-rank":
        t=np.linspace(0,2*np.pi,200)
        for ax,bad in zip(axes,[False,True]):
            plane(ax,(-2.6,2.6),(-1.6,1.6),[-2,0,2])
            ax.set_yticks([-1,0,1]);ax.plot(2*np.cos(t),np.zeros_like(t) if bad else np.sin(t),color=GRAY,lw=2)
            arrow(ax,(0,0),(2,0),BLUE)
            if bad:
                ax.scatter([0],[0],facecolors="none",edgecolors=ORANGE,s=150,lw=2.5,zorder=6)
                ax.text(-2.2,.8,"c₂ → output 0",fontsize=24,color=ORANGE)
            else:arrow(ax,(0,0),(0,1),PURPLE)
            ax.set_xlabel("output speed y₁",fontsize=24);ax.set_ylabel("output speed y₂",fontsize=24)
            ax.set_title("U=[e₁,e₃]\nGᵣ=diag(4,0): semidefinite" if bad else "U=[e₁,e₂]\nGᵣ=diag(4,1): positive definite",fontsize=23,pad=25)
        fig.text(.5,.085,"Same J=[[2,0,0],[0,1,0]]; only the chosen input subspace changes.\nLeft: eigenvalues 4,1 give gains 2,1. Right: gains 2,0.\nGray: images of unit circles in tangent coordinates.",ha="center",fontsize=23)
    elif name=="start-metric-sum":
        for ax,fine in zip(axes,[False,True]):
            plane(ax,(-.3,1.45),(-.55,1.6),[0,.5,1])
            xs=[0,.5,1] if fine else [0,1]
            points=np.array([[x,0] for x in xs]+[[1,1]])
            ax.plot(points[:,0],points[:,1],color=BLUE,lw=3)
            ax.scatter(points[:,0],points[:,1],color=BLUE,s=40,zorder=5)
            ax.text(1.14,.45,"1",color=GREEN,fontsize=27)
            if fine:
                ax.text(.18,-.28,"0.50",fontsize=24,color=PURPLE)
                ax.text(.68,-.28,"0.75",fontsize=24,color=PURPLE)
            else:ax.text(.45,-.28,"1.00",fontsize=25,color=PURPLE)
            ax.set_xlabel("same path x",fontsize=24);ax.set_ylabel("same path y",fontsize=24)
            ax.set_title("4 points, 3 segments\nStart-metric sum: 2.25" if fine else "3 points, 2 segments\nStart-metric sum: 2.00",fontsize=23,pad=25)
        fig.text(.5,.085,"Synthetic metric G(x,y)=diag((1+x)²,1), x≥0.\nStart-point metric sets each segment length (purple).\nMore points change the approximation, not this path.",ha="center",fontsize=23)
    elif name=="path-refinement":
        n=np.array([1,2,4,8,16]);length=2.5-.5/n
        ax=axes[0];ax.plot(np.arange(5),length,"o-",color=BLUE,lw=3,ms=7)
        ax.axhline(2.5,color=GRAY,ls="--",lw=2);ax.text(.25,2.59,"integral length: 2.5",fontsize=25,color=GRAY)
        ax.set_xlim(-.3,4.3);ax.set_ylim(1.85,2.72);ax.set_xticks(np.arange(5),[str(i) for i in n]);ax.set_yticks([2,2.25,2.5]);ax.grid(color=GRID)
        ax.set_xlabel("horizontal subdivisions n",fontsize=24);ax.set_ylabel("estimated path length",fontsize=25)
        ax.set_title("Same path, smaller intervals\nLeft-endpoint metric sums",fontsize=25,pad=25)
        fig.text(.5,.08,"L̂ₙ=2.5−1/(2n)\nn=1: 2.00; n=2: 2.25\nn=16: 2.46875 approaches 2.5.",ha="center",fontsize=25)
    elif name=="permuted-path":
        points=np.array([[0,0],[1,0],[1,1],[0,1]])
        for ax,order,color in zip(axes,[[0,1,2,3],[0,2,1,3]],[BLUE,PURPLE]):
            plane(ax,(-.4,1.5),(-.35,1.5),[0,1]);selected=points[order]
            ax.plot(selected[:,0],selected[:,1],color=color,lw=3)
            ax.scatter(points[:,0],points[:,1],color=GRAY,s=35,zorder=5)
            for p,label,offset in zip(points,"ABCD",[(-.23,-.23),(.20,-.23),(.20,.20),(-.23,.20)]):
                ax.text(*(p+offset),label,fontsize=27)
            ax.set_xlabel("x",fontsize=26);ax.set_ylabel("y",fontsize=26)
            ax.set_title("A → B → C → D\nLength: 3" if order[1]==1 else "A → C → B → D\nLength: 1+2√2",fontsize=25,pad=25)
        fig.text(.5,.06,"Same points and endpoints.\nNew order creates a new path.\nMetric G=I in both panels.",ha="center",fontsize=26)
    elif name=="alignment-versus-gain":
        for ax,output in zip(axes,[False,True]):
            plane(ax,(-.6,2.6),(-.6,1.8),[0,1,2]);ax.set_yticks([0,1])
            arrow(ax,(0,0),(2 if output else 1,0),BLUE);arrow(ax,(0,0),(0,1),PURPLE)
            ax.text(.2,1.4,"B direction",color=PURPLE,fontsize=24)
            ax.text(.3,-.37,"A direction",color=BLUE,fontsize=24)
            ax.set_xlabel("output speed y₁" if output else "ambient v₁",fontsize=24)
            ax.set_ylabel("output speed y₂" if output else "ambient v₂",fontsize=24)
            ax.set_title("Downstream J=diag(2,1)\nUnit-direction gains: 2 and 1" if output else "A=span(e₁), B=span(e₂)\nPrincipal angle: 90°",fontsize=23,pad=25)
        fig.text(.5,.085,"Alignment measures subspace orientation in the input metric.\nGain measures output speed under a fixed downstream map.\nNeither measurement alone proves semantic feature use.",ha="center",fontsize=23)
    else:raise ValueError(name)
    fig.set_facecolor(BG)
    for ax in fig.axes:ax.set_facecolor(BG)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,metadata={"Date":None});plt.close(fig)


if __name__=="__main__":main()
