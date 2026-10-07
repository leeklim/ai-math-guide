"""Elementary group/action illustrations for A09-SYM-01; mathematical examples."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix("A09-SYM-01-")
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626"
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"sym-01-"+name})
def setup(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
def arrow(ax,a,b,color,curve=0):
 ax.annotate("",xy=b,xytext=a,arrowprops=dict(arrowstyle="->",mutation_scale=11,lw=2.6,color=color,connectionstyle="arc3,rad="+str(curve),shrinkA=6,shrinkB=6))
if name=="integer-group-return":
 fig,ax=plt.subplots(figsize=(520/72,800/72),facecolor=bg);fig.subplots_adjust(left=.13,right=.91,bottom=.38,top=.75);ax.set_facecolor(bg);ax.set_xlim(-.5,6.5);ax.set_ylim(-1.25,1.25);ax.set_xticks(range(7));ax.set_xticklabels([]);ax.set_yticks([]);ax.spines[["top","left","right"]].set_visible(False);ax.spines["bottom"].set_position(("data",0))
 ax.scatter([2,5],[0,0],color=[blue,green],s=100,zorder=5);arrow(ax,(2,.45),(5,.45),purple,-.6);arrow(ax,(5,-.1),(2,-.1),green,-.6)
 ax.text(2.55,1.14,"+3",color=purple,fontsize=28);ax.text(2.55,-.78,"−3",color=green,fontsize=28)
 
 for n in range(7):ax.text(n,.04,str(n),ha="center",va="bottom",fontsize=22)
 ax.text(.25,-1.18,"5 + (−3) = 2",fontsize=27)
 title="Integer addition\nreturns by the inverse"
 footer="Identity: n + 0 = n\nClosure: the sum is an integer.\n(2 + 3) + 1 = 2 + (3 + 1) = 6"
elif name=="noncommuting-actions":
 fig,axs=plt.subplots(1,2,figsize=(1120/72,900/72),facecolor=bg);fig.subplots_adjust(left=.09,right=.97,bottom=.31,top=.73,wspace=.34)
 paths=[[(1,2),(1,-2),(2,1)],[(1,2),(-2,1),(-2,-1)]]
 labs=[["x=(1,2)","Sx=(1,−2)","RSx=(2,1)"],["x=(1,2)","Rx=(−2,1)","SRx=(−2,−1)"]]
 offsets=[[(.3,.35),(-2.5,-.65),(.15,.28)],[(.2,.35),(-1.0,.75),(-.8,-.6)]]
 for ax,pts,ls,off in zip(axs,paths,labs,offsets):
  setup(ax);ax.axhline(0,color="#94A3B8",lw=1);ax.axvline(0,color="#94A3B8",lw=1)
  for pt,c,l,of in zip(pts,[blue,purple,green],ls,off):ax.scatter(*pt,color=c,s=95,zorder=5);ax.text(pt[0]+of[0],pt[1]+of[1],l,color=c,fontsize=24)
  arrow(ax,pts[0],pts[1],purple);arrow(ax,pts[1],pts[2],green)
  ax.set(xlim=(-3.5,3.5),ylim=(-3.5,3.5),xticks=[-2,0,2],yticks=[-2,0,2],xlabel="Coordinate 1",ylabel="Coordinate 2");ax.set_aspect("equal")
 axs[0].set_title("S first; R second",fontsize=27,pad=24);axs[1].set_title("R first; S second",fontsize=27,pad=24)
 title="Composition order can change the endpoint"
 footer="R: counterclockwise quarter-turn; S: reflection across the horizontal axis.\nRS ≠ SR. Associativity changes parentheses, not this order."
elif name=="singular-map-collapse":
 fig,ax=plt.subplots(figsize=(520/72,870/72),facecolor=bg);fig.subplots_adjust(left=.18,right=.90,bottom=.35,top=.76);setup(ax)
 ax.axhline(0,color="#94A3B8",lw=1);ax.axvline(0,color="#94A3B8",lw=1)
 ax.scatter([1,1],[1,-1],color=blue,s=85,zorder=5);ax.scatter(1,0,color=green,marker="s",s=95,zorder=5)
 arrow(ax,(1,1),(1,0),purple);arrow(ax,(1,-1),(1,0),purple)
 ax.text(-.42,1.45,"(1, 1)",fontsize=26,color=blue);ax.text(-.42,-1.70,"(1, −1)",fontsize=26,color=blue);ax.text(1.24,.28,"(1, 0)",fontsize=26,color=green)
 ax.set(xlim=(-.65,2.8),ylim=(-2,2),xticks=[0,1,2],yticks=[-1,0,1],xlabel="Coordinate 1",ylabel="Coordinate 2");ax.set_aspect("equal")
 title="A singular map\nmerges distinct inputs"
 footer="A = diag(1, 0)\nBoth inputs have the same image.\nNo inverse recovers both inputs."
elif name=="quarter-turn-inverse":
 fig,ax=plt.subplots(figsize=(520/72,920/72),facecolor=bg);fig.subplots_adjust(left=.17,right=.90,bottom=.33,top=.74);setup(ax)
 ax.axhline(0,color="#94A3B8",lw=1);ax.axvline(0,color="#94A3B8",lw=1)
 arrow(ax,(0,0),(2,1),blue);arrow(ax,(0,0),(-1,2),green)
 ax.text(.62,-.48,"h=(2,1)",color=blue,fontsize=25);ax.text(-2.0,2.38,"Rh=(−1,2)",color=green,fontsize=25)
 angles=np.linspace(np.arctan2(1,2)+.12,np.arctan2(1,2)+np.pi/2-.12,120);arc=np.sqrt(5)*np.c_[np.cos(angles),np.sin(angles)]
 ax.plot(arc[:-6,0],arc[:-6,1],color=purple,lw=2.6)
 ax.annotate("",xy=arc[-1],xytext=arc[-8],arrowprops=dict(arrowstyle="->",mutation_scale=11,lw=2.6,color=purple,shrinkA=0,shrinkB=0))
 ax.text(.26,2.72,"+90°",color=purple,fontsize=26)
 ax.set(xlim=(-2.5,2.8),ylim=(-1.0,3.1),xticks=[-2,0,2],yticks=[0,1,2],xlabel="Coordinate 1",ylabel="Coordinate 2");ax.set_aspect("equal")
 title="Rotation and its inverse\nact on a vector"
 footer="R(a,b) = (−b,a)\nR⁻¹(−1,2) = (2,1)\nR⁻¹ R = I"
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.35)
fig.text(.5,.08,footer,ha="center",fontsize=24,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)

