"""Reproduce explicit feature geometry and sample-indexed kernel calculations."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE,PURPLE,GREEN="#2563EB","#7C3AED","#059669"
GRID,GRAY="#D9E2EF","#64748B"


def arrow(ax,start,end,color,ls="-"):
    ax.annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":"->","color":color,
        "lw":2.8,"mutation_scale":12,"shrinkA":0,"shrinkB":0,"linestyle":ls},zorder=5)


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();name=args.output.stem.removeprefix("A09-KER-03-")
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none",
        "svg.hashsalt":"a09-ker-03","axes.spines.top":False,"axes.spines.right":False})
    normal=name in {"feature-parabola","polynomial-products","predictor-feature-sum"}
    count=3 if name=="gram-factorization" else 2
    if normal:
        fig,ax=plt.subplots(figsize=(7.2,10.5));axes=[ax]
        fig.subplots_adjust(left=.24,right=.94,bottom=.34,top=.78)
    else:
        fig,axes=plt.subplots(1,count,figsize=(7*count,10))
        fig.subplots_adjust(left=.10,right=.96,bottom=.36,top=.73,wspace=.53)
    if name=="feature-parabola":
        x=np.linspace(-1.3,1.3,150);ax.plot(x,x*x,color=PURPLE,lw=3)
        ax.scatter([-1,0,1],[1,0,1],color=BLUE,s=65,zorder=5)
        ax.set_xlim(-1.5,1.5);ax.set_ylim(-.35,2);ax.set_xticks([-1,0,1]);ax.set_yticks([0,1,2]);ax.grid(color=GRID)
        ax.set_xlabel("feature φ₁=x",fontsize=26);ax.set_ylabel("feature φ₂=x²",fontsize=26)
        ax.set_title("Scalar input → 2D feature\nφ(x)=(x,x²)",fontsize=26,pad=27)
        fig.text(.5,.12,"x=−1,0,1 maps to\n(−1,1), (0,0), (1,1).\nThe feature map need not be linear.",ha="center",fontsize=25)
    elif name=="polynomial-products":
        fig.subplots_adjust(left=.40,bottom=.36,top=.76)
        ax.barh([2,1,0],[1,4,4],color=[BLUE,PURPLE,GREEN],height=.5)
        ax.set_yticks([2,1,0],["1·1","√2·2√2","1·4"],fontsize=25)
        ax.set_xlim(0,5);ax.set_xticks([0,1,4]);ax.grid(axis="x",color=GRID)
        ax.set_xlabel("coordinate product",fontsize=25)
        ax.set_title("φ(x)=(1,√2x,x²)\nx=1, z=2",fontsize=25,pad=27)
        fig.text(.5,.13,"Inner product: 1+4+4=9\nKernel: (1+1·2)²=9\n√2 produces the middle term 2xz.",ha="center",fontsize=24)
    elif name=="predictor-feature-sum":
        arrow(ax,(0,0),(1,1),BLUE);arrow(ax,(1,1),(2,3),PURPLE)
        arrow(ax,(0,0),(2,3),GREEN);arrow(ax,(0,0),(.5,.25),GRAY)
        ax.text(.08,1.7,"½φ(2)=(1,2)",fontsize=24,color=PURPLE)
        ax.text(.95,.53,"φ(1)=(1,1)",fontsize=24,color=BLUE)
        ax.text(.45,3.35,"w=(2,3)",fontsize=26,color=GREEN)
        ax.set_xlim(-.3,2.7);ax.set_ylim(-.4,3.85);ax.set_xticks([0,1,2]);ax.set_yticks([0,1,2,3]);ax.grid(color=GRID)
        ax.set_xlabel("feature coordinate 1",fontsize=25);ax.set_ylabel("feature coordinate 2",fontsize=25)
        ax.set_title("w=φ(1)+½φ(2)\nφ(x)=(x,x²)",fontsize=26,pad=27)
        fig.text(.5,.10,"At new x=0.5: φ(x)=(0.5,0.25)\nw·φ(x)=1+0.75=1.75\nk(1,x)+½k(2,x)=0.75+1=1.75",ha="center",fontsize=24)
    elif name=="orthogonal-features":
        points=np.array([[1,1],[2,4]]);q=np.array([[0,-1],[1,0]])
        for ax,rotated in zip(axes,[False,True]):
            p=points@q.T if rotated else points
            for v,color in zip(p,[BLUE,PURPLE]):arrow(ax,(0,0),v,color)
            ax.set_xlim(-5,3);ax.set_ylim(-.5,5);ax.set_aspect("equal")
            ax.set_xticks([-4,-2,0,2]);ax.set_yticks([0,2,4]);ax.grid(color=GRID)
            ax.set_xlabel("coordinate 1",fontsize=23);ax.set_ylabel("coordinate 2",fontsize=23)
            ax.set_title("Qφ: (−1,1),(−4,2)" if rotated else "φ: (1,1),(2,4)",fontsize=23,pad=27)
        fig.text(.5,.10,"A 90° orthogonal rotation changes coordinates, not inner products.\nBlue–purple dot product: 1·2+1·4 = (−1)(−4)+1·2 = 6.",ha="center",fontsize=23)
    elif name=="centering":
        points=np.array([[1,1],[2,4],[3,9]]);mean=points.mean(axis=0)
        for ax,centered in zip(axes,[False,True]):
            p=points-mean if centered else points
            ax.scatter(p[:,0],p[:,1],color=[BLUE,PURPLE,GREEN],s=70,zorder=5)
            m=np.zeros(2) if centered else mean
            ax.scatter([m[0]],[m[1]],marker="x",s=120,color=GRAY,zorder=5)
            for i,v in enumerate(p):ax.annotate(f"x{i+1}",v,xytext=(12,-28) if i==1 else (10,10),textcoords="offset points",fontsize=23)
            ax.axhline(0,color=GRAY,lw=1);ax.axvline(0,color=GRAY,lw=1);ax.grid(color=GRID)
            ax.set_xlabel("feature 1",fontsize=23);ax.set_ylabel("feature 2",fontsize=23)
            ax.set_xlim((-.1,3.6) if not centered else (-1.6,1.6));ax.set_ylim((-.5,11) if not centered else (-5.3,5.8))
            ax.set_title("Subtract mean (2,14/3)" if centered else "Raw features (x,x²)",fontsize=23,pad=27)
        fig.text(.5,.10,"The same sample mean is subtracted from every row.\nCentering changes origin and Gram values,\nnot the order of sample identities.",ha="center",fontsize=23)
    elif name in {"gram-factorization","row-alignment"}:
        points=np.array([0,1,2]);phi=np.stack([points,points*points],axis=1);k=phi@phi.T
        if name=="gram-factorization":
            mats=[phi,phi.T,k];rows=[["x=0","x=1","x=2"],["φ₁","φ₂"],["x=0","x=1","x=2"]]
            cols=[["φ₁","φ₂"],["x=0","x=1","x=2"],["x=0","x=1","x=2"]];titles=["Φ: samples × features\n3 × 2","Φᵀ: features × samples\n2 × 3","K=ΦΦᵀ: sample pairs\n3 × 3"]
        else:
            order=[2,0,1];mats=[k,k[np.ix_(order,order)]];rows=[["A:0","B:1","C:2"],["C:2","A:0","B:1"]];cols=rows;titles=["Rows A,B,C","Rows C,A,B"]
        for ax,m,r,c,title in zip(axes,mats,rows,cols,titles):
            n,d=m.shape
            ax.pcolormesh(np.arange(d+1),np.arange(n+1),m,cmap="PuBu",vmin=0,vmax=20,edgecolors=GRID,lw=2)
            ax.set_aspect("equal");ax.invert_yaxis();ax.set_xticks(np.arange(d)+.5,c,fontsize=22);ax.set_yticks(np.arange(n)+.5,r,fontsize=22)
            ax.set_xlabel("column identity",fontsize=23);ax.set_ylabel("row identity",fontsize=23)
            for i in range(n):
                for j in range(d):ax.text(j+.5,i+.5,str(m[i,j]),ha="center",va="center",fontsize=26,color="white" if m[i,j]>=12 else "#0F172A")
            ax.set_title(title,fontsize=23,pad=27)
        footer="Multiply across features: K(1,2)=(1,1)·(2,4)=6.\nThe 3×3 matrix has n²=9 entries even though feature width is 2." if name=="gram-factorization" else "Same sample geometry, different matrix positions.\nEntry (B,C)=6 in both matrices.\nCompare matching identities, not raw row numbers."
        fig.text(.5,.10,footer,ha="center",fontsize=23)
    else:raise ValueError(name)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,format="svg",metadata={"Date":None});plt.close(fig)


if __name__=="__main__":main()
