"""Illustrative population-mass and effect views for CAU07; no model runs."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-CAU-07-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"cau07-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626"
def style(a):
 a.set_facecolor(bg);a.grid(color="#CBD5E1",alpha=.55);a.set_axisbelow(True);a.spines[["top","right"]].set_visible(False)
if name=="mixture-weighted-effect-areas":
 fig,axs=plt.subplots(1,2,figsize=(1200/72,1040/72),facecolor=bg);fig.subplots_adjust(left=.08,right=.95,bottom=.28,top=.76,wspace=.4)
 for a,masses,t in zip(axs,[[.5,.5],[.2,.8]],["Source mean = 0.65","Target mean = 0.32"]):
  style(a);a.set(xlim=(0,1),ylim=(0,1.7),xticks=[0,masses[0],1],yticks=[0,.6,1.2],xlabel="Cumulative population mass",ylabel="Conditional effect");a.set_title(t,fontsize=27,pad=26)
  offset=0
  for j,(mass,e,c) in enumerate(zip(masses,[1.2,.1],[blue,green])):
   a.add_patch(Rectangle((offset,0),mass,e,facecolor=c,alpha=.18,edgecolor=c,lw=3))
   a.text(offset+mass/2,e+.18,f"{'AB'[j]}: width {mass:.1f}",ha="center",color=c,fontsize=25)
   offset+=mass
 title="Stable conditional heights, changed population widths"
 footer="Illustrative body values: A effect 1.2; B effect 0.1.\nArea is mass × effect. Source: 0.60+0.05; target: 0.24+0.08.\nA changed mixture can change the average without changing either effect."
elif name=="same-mean-different-conditional-effects":
 fig,a=plt.subplots(figsize=(520/72,1080/72),facecolor=bg);fig.subplots_adjust(left=.20,right=.94,bottom=.34,top=.76);style(a)
 x=np.arange(2);a.plot(x,[1,3],"o-",color=blue,lw=3,ms=10,label="Source");a.plot(x,[3,1],"s--",color=orange,lw=3,ms=10,label="Target");a.axhline(2,color=purple,lw=2,ls=":");a.text(.02,.63,"Both means = 2",fontsize=26,color=purple)
 a.set(xlim=(-.18,1.18),ylim=(.4,3.9),xticks=x,xticklabels=["A","B"],yticks=[1,2,3],xlabel="Context",ylabel="Conditional effect");a.legend(loc="upper center",fontsize=25,frameon=False)
 title="Same mean does not imply\nsame conditional effects"
 footer="Illustrative values,\nnot measured model effects.\nBoth populations mix A/B 0.5/0.5.\nSource: 1 and 3.\nTarget: 3 and 1.\nConditional stability fails."
elif name=="missing-target-support":
 fig,a=plt.subplots(figsize=(520/72,1100/72),facecolor=bg);fig.subplots_adjust(left=.18,right=.94,bottom=.35,top=.77);style(a);x=np.arange(3);w=.29
 a.bar(x-w/2,[.5,.5,0],w,color=blue,alpha=.7,label="Source");a.bar(x+w/2,[.2,.3,.5],w,color=green,alpha=.7,label="Target")
 a.axvspan(1.65,2.5,color=red,alpha=.05);a.annotate("No source",xy=(2-w/2,.005),xytext=(1.15,.60),fontsize=25,color=red,arrowprops={"arrowstyle":"->","lw":2,"color":red,"mutation_scale":13})
 a.set(xlim=(-.5,2.5),ylim=(0,.87),xticks=x,xticklabels=["A","B","C"],yticks=[0,.5],xlabel="Context",ylabel="Population mass");a.legend(loc="upper right",fontsize=25,frameon=False)
 title="Target-only contexts\nhave no source ratio"
 footer="Illustrative mass on C:\np_S(C)=0, p_T(C)=0.5.\nThe ratio divides by zero.\nReweighting cannot create\nthe missing conditional effect."
elif name=="large-weight-amplification-and-clipping":
 fig,axs=plt.subplots(1,2,figsize=(1240/72,1090/72),facecolor=bg);fig.subplots_adjust(left=.08,right=.95,bottom=.32,top=.74,wspace=.42)
 for a in axs:style(a)
 axs[0].bar([0,1],[.001,.010],color=[blue,red],width=.55);axs[0].set(xticks=[0,1],xticklabels=["Source","Target"],ylim=(0,.014),yticks=[0,.005,.010],ylabel="Error in mean contribution");axs[0].set_title("Ratio 10 amplifies error",fontsize=26,pad=26)
 axs[0].text(0,.0019,"0.001",ha="center",color=blue,fontsize=26);axs[0].text(1,.0109,"0.010",ha="center",color=red,fontsize=26)
 axs[1].bar([0,1],[.50,.20],color=[green,orange],width=.55);axs[1].set(xticks=[0,1],xticklabels=["Ratio 10","Clipped 4"],ylim=(0,.68),yticks=[0,.2,.5],ylabel="Unnormalized context mass");axs[1].set_title("Clipping changes weighting",fontsize=26,pad=26);axs[1].text(0,.535,"0.50",ha="center",color=green,fontsize=26);axs[1].text(1,.235,"0.20",ha="center",color=orange,fontsize=26)
 title="A rare context can dominate weighted error; clipping alters the target"
 footer="Illustrative p_S=0.05, p_T=0.50; ratio=10. Conditional estimate error=0.02.\nContribution error: 0.05×0.02=0.001 versus 0.50×0.02=0.010.\nClip ratio at 4: source mass 0.05 becomes 0.20, not target mass 0.50.\nRenormalization must be checked across all contexts; it does not undo clipping."
elif name=="subgroup-effect-difference":
 fig,a=plt.subplots(figsize=(520/72,1020/72),facecolor=bg);fig.subplots_adjust(left=.20,right=.93,bottom=.32,top=.77);style(a)
 a.scatter([0,1],[1.2,.1],s=130,color=[blue,green],zorder=4);a.plot([0,.60],[1.2,1.2],color="#94A3B8",lw=2,ls="--");a.plot([.70,1],[.1,.1],color="#94A3B8",lw=2,ls="--");a.plot([.65,.65],[.1,1.2],color=purple,lw=3);a.plot([.60,.70],[1.2,1.2],color=purple,lw=3);a.plot([.60,.70],[.1,.1],color=purple,lw=3);a.text(.02,.65,"Δ = 1.1",color=purple,fontsize=29);a.text(-.03,1.32,"A: 1.2",color=blue,fontsize=27);a.text(.78,.30,"B: 0.1",color=green,fontsize=27)
 a.set(xlim=(-.15,1.2),ylim=(0,1.6),xticks=[0,1],xticklabels=["A","B"],yticks=[0,.6,1.2],xlabel="Template",ylabel="Illustrative effect")
 title="Estimate the uncertainty\nof the difference itself"
 footer="Body difference: 1.2−0.1=1.1.\nNo uncertainty interval\nis drawn from invented data.\nMean-interval overlap alone\nis not a difference interval."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.95,linespacing=1.35);fig.text(.5,.04,footer,ha="center",fontsize=24 if name in ["same-mean-different-conditional-effects","missing-target-support","subgroup-effect-difference"] else 25,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)

