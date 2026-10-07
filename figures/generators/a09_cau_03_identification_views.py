"""Exact finite confounding and identification views for A09-CAU-03."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-CAU-03-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"cau03-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626"
def grid(ax,joint,xlabel,ylabel,ceiling=.5):
 ax.set_facecolor(bg);nr,nc=joint.shape;ax.pcolormesh(np.arange(nc+1)-.5,np.arange(nr+1)-.5,joint,vmin=0,vmax=ceiling,cmap="Blues",rasterized=False);ax.set_aspect("equal");ax.set(xticks=list(range(nc)),yticks=list(range(nr)),xlabel=xlabel,ylabel=ylabel)
 for row in range(nr):
  for col in range(nc):ax.text(col,row,f"{joint[row,col]:g}",ha="center",va="center",fontsize=30,color="white" if joint[row,col]>.3*ceiling else "#0F172A")
def style(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
if name=="collider-selection-mass":
 fig,axs=plt.subplots(1,2,figsize=(1100/72,1000/72),facecolor=bg);fig.subplots_adjust(left=.09,right=.95,bottom=.29,top=.76,wspace=.42)
 for a,j,t in zip(axs,[np.full((2,2),.25),np.array([[0,.5],[.5,0]])],["Original independent joint","Select C=X+Y=1"]):grid(a,j,"X","Y");a.set_title(t,fontsize=27,pad=32)
 title="Selecting a common effect creates an association"
 footer="Before selection: P(X=x,Y=y)=0.25 for all four pairs.\nAfter C=1: only (0,1) and (1,0) remain, each with probability 0.5.\nThe selected sample obeys Y=1−X without changing either cause."
elif name=="stratum-weighted-areas":
 fig,axs=plt.subplots(1,2,figsize=(1400/72,1000/72),facecolor=bg);fig.subplots_adjust(left=.065,right=.965,bottom=.32,top=.76,wspace=.35)
 for a,weights,t in zip(axs,[(.5,.5),(.1,.9)],["Population weights: 0.5 / 0.5","Selected X=x: 0.1 / 0.9"]):
  a.set_facecolor(bg);a.set(xlim=(0,1),ylim=(0,1.12),xticks=[0,weights[0],1],yticks=[0,.2,.8,1],xlabel="Cumulative stratum weight",ylabel="Outcome probability");a.set_title(t,fontsize=27,pad=28)
  cursor=0
  for z,(w,q,c) in enumerate(zip(weights,[.2,.8],[blue,green])):
   a.add_patch(Rectangle((cursor,0),w,1,facecolor=c,alpha=.07,edgecolor="#CBD5E1",lw=2))
   a.add_patch(Rectangle((cursor,0),w,q,facecolor=c,alpha=.70,edgecolor=c,lw=2,hatch="//" if z==1 else None))
   if w>.2:a.text(cursor+w/2,q/2,f"Area {w*q:.2f}",ha="center",va="center",fontsize=27,color="white")
   else:a.annotate("Area 0.02",xy=(.05,.1),xytext=(.20,.60),fontsize=25,color=blue,arrowprops={"arrowstyle":"->","lw":2,"color":blue},bbox={"facecolor":bg,"edgecolor":"none","pad":5})
   cursor+=w
  a.text(.08,1.03,"Z=0: height 0.2",fontsize=24,color=blue);a.text(.55,1.03,"Z=1: height 0.8",fontsize=24,color=green)
 title="The same conditional rates, with different averaging weights"
 footer="Filled area = stratum weight × conditional success probability.\nPopulation: 0.5×0.2 + 0.5×0.8 = 0.50.\nSelected group: 0.1×0.2 + 0.9×0.8 = 0.74."
elif name=="positivity-missing-stratum":
 fig,ax=plt.subplots(figsize=(520/72,980/72),facecolor=bg);fig.subplots_adjust(left=.19,right=.91,bottom=.33,top=.76)
 joint=np.array([[.5,.5],[0,1]])
 grid(ax,joint,"X","Z",ceiling=1);ax.add_patch(Rectangle((-.5,.5),1,1,fill=False,ec=red,lw=4));ax.text(.5,1.85,"P(X=0 | Z=1)=0",ha="center",fontsize=25,color=red)
 title="Missing treatment support\nin a required stratum"
 footer="Each row sums to 1.\nThese are P(X | Z), not outcomes.\nAn X=0 intervention needs\nthe Z=1 outcome conditional\nthat this sample cannot supply."
elif name=="matched-observation-distinct-intervention":
 fig,axs=plt.subplots(2,2,figsize=(1160/72,1220/72),facecolor=bg);fig.subplots_adjust(left=.11,right=.94,bottom=.24,top=.79,hspace=.63,wspace=.40)
 for col in range(2):
  grid(axs[0,col],np.diag([.5,.5]),"X","Y");axs[0,col].set_title(["Model A observed","Model B observed"][col],fontsize=28,pad=25)
  a=axs[1,col];style(a);v=[0,1] if col==0 else [.5,.5];a.bar([0,1],v,width=.5,color=green if col==0 else orange);a.set(xlim=(-.6,1.6),ylim=(0,1.32),xticks=[0,1],yticks=[0,.5,1],xlabel="Y under do(X=1)",ylabel="Probability")
  for x,y in enumerate(v):a.text(x,y+.06,f"{y:g}",ha="center",fontsize=28,color=green if col==0 else orange)
 title="Observed joint law agrees; interventional law does not"
 footer="A: X=U, Y=X. B: X=U, Y=U. P(U=0)=P(U=1)=0.5.\nBoth observed laws are exact, not finite-sample estimates.\nMore observational samples cannot distinguish these allowed structures."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.95,linespacing=1.35);fig.text(.5,.04,footer,ha="center",fontsize=24 if name=="positivity-missing-stratum" else 25,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)

