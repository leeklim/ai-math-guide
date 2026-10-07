"""Illustrative state geometry and abstraction error views for CAU06."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-CAU-06-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"cau06-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626"
def style(a):
 a.set_facecolor(bg);a.grid(color="#CBD5E1",alpha=.6);a.set_axisbelow(True);a.spines[["top","right"]].set_visible(False)
def plane(a):
 style(a);a.set(xlim=(-3,3),ylim=(-3,3),xticks=[-2,0,2],yticks=[-2,0,2],xlabel="First coordinate",ylabel="Second coordinate");a.set_aspect("equal");a.axvline(0,color="#64748B",lw=2,ls="--");a.axhline(0,color="#64748B",lw=1)
if name=="many-states-one-label":
 fig,a=plt.subplots(figsize=(520/72,1000/72),facecolor=bg);fig.subplots_adjust(left=.19,right=.94,bottom=.32,top=.76);plane(a);a.axvspan(-3,0,color=orange,alpha=.06);a.axvspan(0,3,color=green,alpha=.06)
 a.scatter([-2,-1,-2],[-1,2,2],color=orange,s=100,marker="s");a.scatter([1,2,2],[-2,-1,2],color=green,s=100);a.text(-2.8,-2.65,"τ=−1",fontsize=28,color=orange);a.text(.45,-2.65,"τ=+1",fontsize=28,color=green)
 title="Many low-level states\nshare one abstract label"
 footer="Illustrative τ(l)=sign(l1).\nPoints differ within each class.\nl1=0 needs an exclusion or tie rule.\nA decoder does not supply\na downstream causal rule."
elif name=="discarded-coordinate-counterexample":
 fig,axs=plt.subplots(1,2,figsize=(1200/72,1000/72),facecolor=bg);fig.subplots_adjust(left=.08,right=.95,bottom=.28,top=.76,wspace=.37)
 for a in axs:plane(a);a.axvspan(-3,0,color=red,alpha=.04);a.axvspan(0,3,color=green,alpha=.04)
 for a,pts,t in zip(axs,[[(2,1),(2,-1)],[(1,2),(-1,2)]],["Before: both τ=+1","Swap coordinates: τ splits"]):
  a.set_title(t,fontsize=27,pad=25)
  for k,((x,y),c,mark) in enumerate(zip(pts,[blue,orange],["o","s"])):a.scatter(x,y,s=135,color=c,marker=mark,zorder=5);lx=x-.30 if t.startswith("Before") else x+(.25 if x>0 else -.25);a.text(lx,y+.50,f"{'AB'[k]}=({x},{y})",ha="center",fontsize=25,color=c)
 title="Discarded coordinates can matter under a permitted operation"
 footer="τ(l)=sign(l1). Before: (2,1) and (2,−1) both map to +1.\nAfter swapping coordinates: (1,2) maps to +1; (−1,2) maps to −1.\nOne original abstract label cannot determine both outcomes of this swap."
elif name=="reflection-preserves-perpendicular":
 fig,a=plt.subplots(figsize=(1100/72,1020/72),facecolor=bg);fig.subplots_adjust(left=.10,right=.92,bottom=.28,top=.77);plane(a);a.set(xlim=(-3.6,3.6),ylim=(-1.4,2.6),xticks=[-2,0,2],yticks=[-1,0,1,2]);a.axhline(1,color="#94A3B8",lw=2,ls="--")
 for xy,c in [((2,1),blue),((-2,1),red),((0,1),purple)]:a.annotate("",xy=xy,xytext=(0,0),arrowprops={"arrowstyle":"->","color":c,"lw":3,"mutation_scale":15})
 a.annotate("",xy=(.88,0),xytext=(0,0),arrowprops={"arrowstyle":"->","color":green,"lw":3,"mutation_scale":13})
 a.text(1.55,1.3,"l=(2,1)",color=blue,fontsize=28);a.text(-3.20,1.3,"l′=(−2,1)",color=red,fontsize=28);a.text(.25,1.95,"Perpendicular part: 1",color=purple,fontsize=26);a.text(1.12,-.52,"w=(1,0)",color=green,fontsize=27)
 title="Unit-direction reflection flips only the w component"
 footer="||w||=1. l′=l−2(wᵀl)w=(−2,1). Scores: wᵀl=2; wᵀl′=−2.\nThe perpendicular coordinate stays 1; l1=0 is the sign boundary.\nA changed decoder score does not guarantee the predicted verb change."
elif name=="rare-error-large-distance":
 fig,a=plt.subplots(figsize=(520/72,1000/72),facecolor=bg);fig.subplots_adjust(left=.20,right=.92,bottom=.32,top=.77);style(a);x=np.arange(1,101);d=np.zeros(100);d[-1]=10;a.plot(x[:-1],d[:-1],color=green,lw=3);a.scatter([100],[10],color=red,s=110,zorder=5);a.axhline(.1,color=purple,lw=2,ls="--");a.text(12,1.1,"Mean=0.1",color=purple,fontsize=27);a.annotate("Rare distance 10",xy=(100,10),xytext=(5,8),color=red,fontsize=25,arrowprops={"arrowstyle":"->","color":red,"lw":2,"mutation_scale":13})
 a.set(xlim=(0,108),ylim=(-.8,11.5),xticks=[1,50,100],yticks=[0,5,10],xlabel="Evaluation state index",ylabel="Nonnegative distance")
 title="A small expected error\ncan hide a large rare failure"
 footer="100 illustrative states,\neach with weight 0.01.\n99 distances are 0; one is 10.\nExpected distance is 0.1.\nNot measured model errors."
elif name=="zero-weight-outside-scope":
 fig,axs=plt.subplots(1,2,figsize=(1160/72,1010/72),facecolor=bg);fig.subplots_adjust(left=.08,right=.95,bottom=.30,top=.76,wspace=.38)
 for a in axs:style(a);a.set(xlim=(-.3,1.8),ylim=(-.15,1.5),xticks=[0,1,1.5],yticks=[0,1],xlabel="Evaluation state s");a.axvspan(1,1.8,color="#CBD5E1",alpha=.3)
 axs[0].plot([0,0,1,1],[0,1,1,0],color=blue,lw=3);axs[0].plot([1,1.8],[0,0],color="#64748B",lw=3,ls="--");axs[0].set_ylabel("Density");axs[0].set_title("Weight only on [0,1]",fontsize=27,pad=27)
 axs[1].plot([0,1],[0,0],color=green,lw=3);axs[1].plot([1,1.8],[1,1],color=red,lw=3,ls="--");axs[1].set_ylabel("Distance");axs[1].set_title("Outside error is unweighted",fontsize=27,pad=27);axs[1].text(.10,.33,"d=0 on support",color=green,fontsize=25)
 title="Zero expected distance need not cover zero-weight states"
 footer="Illustrative uniform evaluation state on [0,1].\nDistance is 0 on support and may be 1 outside it.\nThe expected distance is exactly 0, but not a whole-space guarantee."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.95,linespacing=1.35);fig.text(.5,.04,footer,ha="center",fontsize=24 if name in ["many-states-one-label","rare-error-large-distance"] else 25,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)

