"""Synthetic checkpoint and threshold illustrations for I08-09."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix("I08-09-")
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706"
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i08-09-"+name})
def setup(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
if name=="separate-observed-events":
 k=np.arange(6);R=np.array([.50,.52,.61,.86,.91,.93]);U=np.array([0,.01,.02,.03,.19,.24]);B=np.array([.48,.51,.55,.62,.81,.88])
 fig,axs=plt.subplots(1,3,figsize=(1320/72,820/72),facecolor=bg);fig.subplots_adjust(left=.07,right=.97,bottom=.34,top=.72,wspace=.36)
 for ax,vals,tau,c,title in zip(axs,[R,U,B],[.8,.1,.8],[blue,purple,green],["Recoverability","Ablation effect","Behavior score"]):
  setup(ax);ax.plot(k,vals,color=c,lw=2,ls=":",marker="o",markersize=7)
  idx=np.flatnonzero(vals>=tau)[0];ax.scatter([idx],[vals[idx]],color=c,marker="s",s=110,zorder=5)
  ax.axhline(tau,color=orange,ls="--",lw=2);ax.plot([idx,idx],[ax.get_ylim()[0],vals[idx]],color=c,lw=1)
  ax.set(xlabel="Checkpoint index",ylabel=title,xticks=[0,3,4,5]);ax.set_title(title+"\nτ="+str(tau)+", first="+str(idx),fontsize=26,pad=25)
 title="Different questions need different measurement thresholds"
 footer="Existing synthetic CPU values; first observed indices 3, 4, 4\nDotted segments guide the eye; they are not unobserved measurements."
elif name=="observed-versus-first-ever":
 fig,ax=plt.subplots(figsize=(520/72,900/72),facecolor=bg);fig.subplots_adjust(left=.23,right=.92,bottom=.42,top=.75);setup(ax)
 t=np.linspace(0,4,401);hyp=np.interp(t,[0,1,2,3,4],[.2,.9,.2,.9,.9])
 mono=np.interp(t,[0,2,4],[.2,.2,.9])
 ax.plot(t,hyp,color=purple,ls="--",lw=3,label="Earlier unseen excursion")
 ax.plot(t,mono,color=green,lw=3,label="Monotone alternative")
 ax.scatter([0,2,4],[.2,.2,.9],color=blue,marker="s",s=100,zorder=5,label="Shared observations")
 ax.axhline(.8,color=orange,ls=":",lw=2)
 ax.set(xlabel="Training time",ylabel="Recoverability",xticks=[0,2,4],ylim=(0,1))
 title="First observed crossing\nis not necessarily first ever"
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.24),frameon=False,fontsize=23)
 footer="Threshold 0.8; first observed t = 4\nThe dashed path is hypothetical."
elif name=="threshold-rule-sensitivity":
 k=np.arange(6);R=np.array([.50,.52,.61,.86,.91,.93])
 fig,axs=plt.subplots(1,4,figsize=(1480/72,820/72),facecolor=bg);fig.subplots_adjust(left=.085,right=.98,bottom=.34,top=.72,wspace=.43)
 for ax,tau in zip(axs,[.7,.8,.9,.95]):
  setup(ax);ax.plot(k,R,color=blue,lw=3,marker="o");ax.axhline(tau,color=orange,ls="--",lw=2)
  hits=np.flatnonzero(R>=tau);cross=str(hits[0]) if len(hits) else "not reached"
  if len(hits):ax.scatter([hits[0]],[R[hits[0]]],color=green,marker="s",s=100,zorder=5)
  ax.set(xlabel="Checkpoint index",ylabel="Recoverability",xticks=[0,3,5],yticks=[.5,.75,1],ylim=(.45,1.03))
  ax.set_title("τ="+str(tau)+"\nfirst: "+cross,fontsize=26,pad=25)
 title="The same measured trajectory gives rule-dependent emergence"
 footer="Same six synthetic recoverability values; no smoothing\nA non-crossing trajectory stays non-crossing, not assigned its final step."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.35)
fig.text(.5,.08,footer,ha="center",fontsize=24,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
