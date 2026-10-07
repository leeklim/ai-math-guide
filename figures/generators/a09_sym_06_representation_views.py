"""Swap representation geometry for A09-SYM-06."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-SYM-06-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"sym06-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";red="#DC2626"
def style(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False);ax.set_aspect("equal");ax.axhline(0,color="#94A3B8",lw=1);ax.axvline(0,color="#94A3B8",lw=1)
def arrow(ax,s,e,c,ls="-"):
 ax.annotate("",xy=e,xytext=s,arrowprops={"arrowstyle":"-|>,head_length=.25,head_width=.14","mutation_scale":15,"lw":3,"color":c,"ls":ls})
wide=name=="swap-direct-sum"
if wide:
 fig,axs=plt.subplots(1,2,figsize=(1100/72,880/72),facecolor=bg);fig.subplots_adjust(left=.08,right=.96,bottom=.34,top=.77,wspace=.30);ax,ax2=axs
else:
 fig,ax=plt.subplots(figsize=(520/72,1010/72),facecolor=bg);fig.subplots_adjust(left=.21,right=.91,bottom=.37,top=.77)
style(ax)
if name=="invariant-span-not-fixed":
 t=np.linspace(-2,2,30);ax.plot(t,-t,color="#94A3B8",lw=2,ls="--");arrow(ax,(0,0),(1,-1),blue);arrow(ax,(0,0),(-1,1),purple)
 ax.text(.42,-1.52,"u−",color=blue,fontsize=28);ax.text(-1.65,.45,"Pu−",color=purple,fontsize=28)
 ax.set(xlim=(-2,2),ylim=(-2,2),xticks=[-1,0,1],yticks=[-1,0,1],xlabel="Coordinate 1",ylabel="Coordinate 2")
 title="The span is invariant;\nits vector need not be fixed";footer="u−=(1,−1)ᵀ ; Pu−=−u−\nBoth vectors lie on the same line.\nThe line is a nonzero proper subspace."
elif name=="all-actions-subspace":
 ax.axhline(0,color=blue,lw=4,alpha=.35);arrow(ax,(0,0),(1,0),blue);arrow(ax,(0,0),(0,1),red)
 ax.text(.7,-.50,"v",color=blue,fontsize=28);ax.text(.20,1.10,"Pv",color=red,fontsize=28);ax.text(-1.5,.18,"W",color=blue,fontsize=28)
 ax.set(xlim=(-1.8,1.8),ylim=(-1.8,1.8),xticks=[-1,0,1],yticks=[-1,0,1],xlabel="Coordinate 1",ylabel="Coordinate 2")
 title="One action is not\na common-subspace test";footer="G={I,P} ; W=span(1,0)ᵀ\nIv=v stays in W.\nPv=(0,1)ᵀ leaves W."
elif name=="swap-direct-sum":
 style(ax2)
 for axis,sign,end,label in [(ax,1,(3,1),"Before swap"),(ax2,-1,(1,3),"After swap")]:
  t=np.linspace(-1.5,3.7,50);axis.plot(t,t,color="#CBD5E1",ls="--",lw=1.5);axis.plot(t,-t,color="#CBD5E1",ls="--",lw=1.5)
  arrow(axis,(0,0),(2,2),blue);arrow(axis,(2,2),end,purple);arrow(axis,(0,0),end,green,"--")
  axis.text(.10,2.45,"2u+",color=blue,fontsize=28);axis.text(2.75,2.25,"u−" if sign==1 else "−u−",color=purple,fontsize=28)
  axis.text(end[0]+.13,end[1]-.43 if sign==1 else end[1]+.20,"x" if sign==1 else "Px",color=green,fontsize=28)
  axis.set(xlim=(-1.1,4.1),ylim=(-1.3,4.1),xticks=[0,2,4],yticks=[0,2,4],xlabel="Coordinate 1",ylabel="Coordinate 2");axis.set_title(label,fontsize=27,pad=22)
 title="Swap keeps the symmetric component\nand reverses the antisymmetric one"
 footer="x=(3,1)ᵀ=2u₊+u₋ ; Px=(1,3)ᵀ=2u₊−u₋\nu₊=(1,1)ᵀ ; u₋=(1,−1)ᵀ ; the coefficients are unique."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.955,linespacing=1.35);fig.text(.5,.045,footer,ha="center",fontsize=24 if not wide else 25,color="#475569",linespacing=1.55)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
