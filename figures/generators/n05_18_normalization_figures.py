#!/usr/bin/env python3
"""Deterministic small normalization figures; no model execution."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def setup(size):
    fig,ax=plt.subplots(figsize=size,constrained_layout=True);fig.patch.set_facecolor("#F8FAFC");ax.set_facecolor("#F8FAFC");ax.grid(color="#CBD5E1",linewidth=.7);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False);return fig,ax

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);parser.add_argument("--figure",choices=["norm-components","centering-projection","rms-radius","learned-affine","epsilon-ratio","norm-intervention"]);args=parser.parse_args();args.figure=args.figure or args.output.stem.removeprefix("N05-18-")
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-n05-18-"+args.figure})
    x=np.array([1.,2.,3.]);ln=(x-x.mean())/np.sqrt(np.mean((x-x.mean())**2));rms=x/np.sqrt(np.mean(x*x))
    if args.figure=="norm-components":
        fig,axes=plt.subplots(1,3,figsize=(17,8),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
        for ax,v,title,col in zip(axes,[x,ln,rms],["Input: mean 2","LN: subtract 2, divide √(2/3)","RMS: divide √(14/3)"],["#2563EB","#7C3AED","#059669"]):
            ax.set_facecolor("#F8FAFC");ax.bar(range(3),v,color=col,width=.6);ax.axhline(0,color="#64748B",linewidth=1);ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.set_axisbelow(True);ax.set_xticks(range(3),labels=["f0","f1","f2"]);ax.set_ylim(-1.8,3.8);ax.set_title(title,fontsize=23,pad=24)
            for j,val in enumerate(v):ax.text(j,val+(.15 if val>=0 else -.35),f"{val:.3f}",ha="center",fontsize=24)
        axes[0].set_ylabel("feature value");fig.suptitle("Same vector, different normalization operations\nγ=1, β=0, ε=0",fontsize=27,fontweight="bold")
    elif args.figure in ["centering-projection","rms-radius"]:
        fig,ax=setup((7.2,9));v=np.array([1.,3.]);origin=np.zeros(2)
        ax.axhline(0,color="#94A3B8",linewidth=1);ax.axvline(0,color="#94A3B8",linewidth=1)
        if args.figure=="centering-projection":
            out=v-v.mean();ax.plot([-2,3],[2,-3],linestyle="--",color="#CBD5E1",linewidth=2)
            for a,b,col in [(origin,v,"#2563EB"),(v,out,"#7C3AED"),(origin,out,"#059669")]:ax.annotate("",b,xytext=a,arrowprops={"arrowstyle":"-|>","linewidth":2,"color":col,"mutation_scale":13})
            ax.text(1.25,3.15,"x=(1,3)",fontsize=24,color="#2563EB");ax.annotate("centered\n(−1,1)",out,xytext=(-1.85,-.35),fontsize=24,color="#059669",arrowprops={"arrowstyle":"-","color":"#64748B"});ax.text(1.35,1.4,"subtract\n(2,2)",fontsize=23,color="#7C3AED");ax.set(xlim=(-2,3),ylim=(-1.5,4));ax.set_title("Centering is a projection\nx₀ + x₁ = 0 after centering",fontsize=24,fontweight="bold")
        else:
            out=v/np.sqrt(np.mean(v*v));theta=np.linspace(0,2*np.pi,400);ax.plot(np.sqrt(2)*np.cos(theta),np.sqrt(2)*np.sin(theta),color="#CBD5E1",linewidth=2,linestyle="--")
            ax.annotate("",v,xytext=origin,arrowprops={"arrowstyle":"-|>","color":"#2563EB","linewidth":2,"mutation_scale":13});ax.annotate("",out,xytext=origin,arrowprops={"arrowstyle":"-|>","color":"#059669","linewidth":2,"mutation_scale":13})
            ax.text(1.2,3.05,"x=(1,3)",fontsize=24,color="#2563EB");ax.annotate("RMS output\n(0.447,1.342)",out,xytext=(1.2,.7),fontsize=23,color="#059669",arrowprops={"arrowstyle":"-","color":"#64748B"});ax.text(-1.7,-1.7,"norm = √2",fontsize=24,color="#64748B");ax.set(xlim=(-2,4),ylim=(-2,4));ax.set_title("RMS scales radially\nγ=1, ε=0; mean is not removed",fontsize=24,fontweight="bold")
        ax.set(xlabel="feature 0",ylabel="feature 1");ax.set_aspect("equal");ax.set_xticks([-1,0,1,2,3]);ax.set_yticks([-1,0,1,2,3])
    elif args.figure=="learned-affine":
        fig,ax=setup((7.2,9));gamma=np.array([1.,1.,2.]);beta=np.array([1.,0.,0.]);out=gamma*ln+beta
        for off,v,col,label in [(-.18,ln,"#7C3AED","normalized"),(.18,out,"#059669","after affine")]:ax.bar(np.arange(3)+off,v,width=.34,color=col,label=label)
        ax.axhline(0,color="#64748B",linewidth=1);ax.set_xticks(range(3),labels=["f0","f1","f2"]);ax.set(ylim=(-1.8,3.5),ylabel="feature value")
        ax.axhline(out.mean(),color="#059669",linestyle="--",linewidth=1.5);ax.text(-.45,out.mean()+.12,f"new mean={out.mean():.3f}",fontsize=23,color="#059669")
        ax.set_title("LayerNorm affine changes mean\nγ=(1,1,2), β=(1,0,0)",fontsize=24,fontweight="bold");ax.legend(loc="upper left",frameon=False,fontsize=24)
    elif args.figure=="epsilon-ratio":
        fig,ax=setup((7.2,9));m=np.geomspace(.0001,100,501);v=m/(m+.01);ax.semilogx(m,v,color="#7C3AED",linewidth=2.5,label="before γ");ax.semilogx(m,4*v,color="#059669",linewidth=2.5,linestyle="--",label="after γ=2");ax.axhline(1,color="#94A3B8",linestyle=":");ax.set(xlabel="input mean square",ylabel="output mean square",ylim=(0,4.4));ax.set_xticks([.0001,.01,1,100],labels=["0.0001","0.01","1","100"]);ax.set_yticks([0,1,2,3,4]);ax.set_title("RMS denominator includes ε\nε=0.01, no centering",fontsize=24,fontweight="bold");ax.legend(loc="upper left",frameon=False,fontsize=24)
    else:
        xp=x.copy();xp[0]+=1;recomputed=(xp-xp.mean())/np.sqrt(np.mean((xp-xp.mean())**2));patched=ln.copy();patched[0]+=1
        fig,axes=plt.subplots(1,3,figsize=(17,8),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
        for ax,v,title,col in zip(axes,[ln,recomputed,patched],["Original LN(1,2,3)","Input f0: 1 → 2; rerun LN","Output f0: add 1; no rerun"],["#2563EB","#DC2626","#DC2626"]):
            ax.set_facecolor("#F8FAFC");ax.bar(range(3),v,color=col,width=.55);ax.axhline(0,color="#64748B",linewidth=1);ax.set_xticks(range(3),labels=["f0","f1","f2"]);ax.set_ylim(-1.8,2);ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.set_axisbelow(True);ax.set_title(title,fontsize=23,pad=24)
            for j,val in enumerate(v):ax.text(j,val+(.15 if val>=0 else -.3),f"{val:.3f}",ha="center",fontsize=24)
            ax.text(1,1.72,f"mean={v.mean():.3f}",ha="center",fontsize=24)
        axes[0].set_ylabel("output feature value");fig.suptitle("Changing a normalization input differs from patching its output\nγ=1, β=0, ε=0",fontsize=27,fontweight="bold")
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__=="__main__":main()
