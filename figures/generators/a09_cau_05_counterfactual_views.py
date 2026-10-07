"""Exact potential-outcome couplings and counterfactual toy views."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-CAU-05-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"cau05-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626"
def grid(a,joint,xlabel,ylabel):
 a.set_facecolor(bg);a.pcolormesh(np.arange(3)-.5,np.arange(3)-.5,joint,vmin=0,vmax=.5625,cmap="Blues",rasterized=False);a.set_aspect("equal");a.set(xticks=[0,1],yticks=[0,1],xlabel=xlabel,ylabel=ylabel)
 for y in range(2):
  for x in range(2):a.text(x,y,f"{joint[y,x]:g}",ha="center",va="center",fontsize=27,color="white" if joint[y,x]>.2 else "#0F172A")
def style(a):
 a.set_facecolor(bg);a.grid(color="#CBD5E1",alpha=.6);a.set_axisbelow(True);a.spines[["top","right"]].set_visible(False)
if name=="same-marginals-different-pairing":
 fig,axs=plt.subplots(2,2,figsize=(1160/72,1200/72),facecolor=bg);fig.subplots_adjust(left=.11,right=.94,bottom=.24,top=.80,hspace=.61,wspace=.42)
 for col,j in enumerate([np.diag([.5,.5]),np.array([[0,.5],[.5,0]])]):
  grid(axs[0,col],j,"Y(0)","Y(1)");axs[0,col].set_title(["Equal within each unit","Opposite within each unit"][col],fontsize=27,pad=28)
  a=axs[1,col];style(a);v=[0,1,0] if col==0 else [.5,0,.5];a.bar([-1,0,1],v,width=.45,color=green if col==0 else orange);a.set(xlim=(-1.6,1.6),ylim=(0,1.3),xticks=[-1,0,1],yticks=[0,.5,1],xlabel="τ=Y(1)−Y(0)",ylabel="Probability")
  for x,y in zip([-1,0,1],v):a.text(x,y+.06,f"{y:g}",ha="center",fontsize=27,color=green if col==0 else orange)
 title="The same potential-outcome marginals do not fix individual effects"
 footer="Each Y(0) and Y(1) marginal has P(0)=P(1)=0.5 in both couplings.\nBoth ATE values are 0; the individual-effect distributions differ.\nTop cells specify the within-unit joint pairing."
elif name=="nonpoint-background-posterior":
 fig,axs=plt.subplots(2,2,figsize=(1220/72,1220/72),facecolor=bg);fig.subplots_adjust(left=.11,right=.94,bottom=.24,top=.80,hspace=.62,wspace=.41)
 prior=np.array([[.5625,.1875],[.1875,.0625]]);post=np.array([[0,.5],[.5,0]])
 for col,j in enumerate([prior,post]):
  grid(axs[0,col],j,"U_X","U_Y");axs[0,col].set_title(["Prior backgrounds","Posterior given Y=1"][col],fontsize=28,pad=28)
  a=axs[1,col];style(a);v=[.75,.25] if col==0 else [.5,.5];a.bar([0,1],v,width=.5,color=blue if col==0 else green);a.set(xlim=(-.6,1.6),ylim=(0,1.15),xticks=[0,1],yticks=[0,.25,.5,.75,1],xlabel="Y after setting X:=0",ylabel="Probability")
  for x,y in enumerate(v):a.text(x,y+.06,f"{y:g}",ha="center",fontsize=27,color=blue if col==0 else green)
 title="Evidence may leave several backgrounds, not a single noise value"
 footer="Illustrative SCM: X=U_X, Y=X+U_Y. Independent noises have P(1)=0.25.\nEvidence Y=1 retains (1,0) and (0,1), each with posterior weight 0.5.\nAfter X:=0, keep these posterior weights instead of resampling the prior."
elif name=="cancelling-prompt-effects":
 fig,a=plt.subplots(figsize=(520/72,1000/72),facecolor=bg);fig.subplots_adjust(left=.18,right=.92,bottom=.32,top=.77);style(a);v=np.array([-2,-1,0,1,2,-2,-1,0,1,2]);x=np.arange(1,11);a.bar(x,v,width=.65,color=[red if y<0 else green for y in v]);a.scatter(x[v==0],np.zeros(2),color=orange,s=60,zorder=5);a.axhline(0,color=purple,lw=2,ls="--")
 a.set(xlim=(.3,10.7),ylim=(-2.8,2.8),xticks=[1,5,10],yticks=[-2,-1,0,1,2],xlabel="Prompt unit i",ylabel="Paired Δlogit")
 title="Average zero can conceal\nnonzero prompt effects"
 footer="Ten illustrative differences.\nΔ = ablated − original.\nSample average is 0;\npositive and negative terms cancel.\nNot measured model outputs."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.95,linespacing=1.35);fig.text(.5,.04,footer,ha="center",fontsize=24 if name=="cancelling-prompt-effects" else 25,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)

