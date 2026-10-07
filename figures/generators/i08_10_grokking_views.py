"""Synthetic delayed generalization and metric-coordinate views for I08-10."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix("I08-10-")
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706"
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i08-10-"+name})
def setup(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
def single():
 fig,ax=plt.subplots(figsize=(520/72,880/72),facecolor=bg);fig.subplots_adjust(left=.23,right=.92,bottom=.40,top=.75);setup(ax);return fig,ax
steps=np.array([0,100,200,400,800,1200,1600]);train=np.array([.1,.72,.99,1,1,1,1]);test=np.array([.1,.12,.14,.18,.31,.79,.97])
if name=="observed-generalization-delay":
 fig,ax=plt.subplots(figsize=(1040/72,840/72),facecolor=bg);fig.subplots_adjust(left=.13,right=.95,bottom=.36,top=.77);setup(ax)
 ax.plot(steps,train,color=blue,lw=3,marker="o",label="Train accuracy")
 ax.plot(steps,test,color=green,lw=3,ls="--",marker="s",label="Test accuracy")
 ax.plot([200,200],[0,.99],color=blue,lw=1,ls=":");ax.plot([1600,1600],[0,.97],color=green,lw=1,ls=":")
 ax.annotate("",xy=(1600,1.12),xytext=(200,1.12),arrowprops=dict(arrowstyle="<->",mutation_scale=12,lw=2,color=purple))
 ax.text(900,1.17,"Observed delay: 1400 steps",ha="center",fontsize=25,color=purple)
 ax.set(xlabel="Training step",ylabel="Accuracy",xlim=(-80,1700),ylim=(0,1.25),xticks=[0,200,800,1600],yticks=[0,.5,1])
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.23),frameon=False,fontsize=24,ncol=2)
 title="Training fit is maintained before late test improvement"
 footer="Existing synthetic trace: τ_fit = 0.99; τ_gen = 0.9\nFirst observed t_fit = 200; t_gen = 1600."
elif name=="transient-fit-counterexample":
 fig,ax=single();k=np.arange(5)
 ax.plot(k,[.1,.99,.5,.99,.99],color=blue,lw=3,marker="o",label="Train")
 ax.plot(k,[.1,.1,.2,.2,.95],color=green,lw=3,ls="--",marker="s",label="Test")
 ax.set(xlabel="Checkpoint index",ylabel="Accuracy",xticks=[0,1,2,4],ylim=(0,1.12))
 title="A first fit crossing\ndoes not prove maintained fit"
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.24),frameon=False,fontsize=24,ncol=2)
 footer="Hypothetical train dip at index 2\nInspect fit between the crossings."
elif name=="transition-width":
 fig,ax=single()
 ax.plot([1000,1400],[.2,.8],color=green,lw=3,ls=":",marker="s")
 for t,score in [(1000,.2),(1400,.8)]:ax.plot([t,t],[0,score],color=orange,lw=1.5,ls="--")
 ax.annotate("",xy=(1400,.96),xytext=(1000,.96),arrowprops=dict(arrowstyle="<->",mutation_scale=12,lw=2,color=purple))
 ax.text(1200,1.04,"400 steps",ha="center",fontsize=25,color=purple)
 ax.set(xlabel="Training step",ylabel="Test accuracy",xlim=(800,1600),ylim=(0,1.16),xticks=[1000,1400],yticks=[0,.2,.8])
 title="Report threshold location\nand transition width"
 footer="Exercise observations: 0.2 → 0.8\nAverage change: 0.6 / 400 = 0.0015."
elif name=="raw-and-log-step":
 fig,axs=plt.subplots(1,2,figsize=(1120/72,860/72),facecolor=bg);fig.subplots_adjust(left=.10,right=.96,bottom=.38,top=.72,wspace=.38)
 for ax,log in zip(axs,[False,True]):
  setup(ax);ax.plot(steps[1:],train[1:],color=blue,lw=3,marker="o",label="Train");ax.plot(steps[1:],test[1:],color=green,lw=3,ls="--",marker="s",label="Test")
  if log:ax.set_xscale("log")
  ax.set(xlabel="Training step",ylabel="Accuracy",ylim=(0,1.1),xticks=[100,400,1600],xticklabels=["100","400","1600"])
  ax.set_title("Log step axis" if log else "Linear step axis",fontsize=28,pad=24)
 fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.23),ncol=2,frameon=False,fontsize=24)
 title="The same positive-step observations look different on a log axis"
 footer="Same synthetic train/test points in both panels\nStep 0 omitted in both: log 0 is undefined."
elif name=="margin-and-quantized-accuracy":
 fig,axs=plt.subplots(1,2,figsize=(1120/72,880/72),facecolor=bg);fig.subplots_adjust(left=.10,right=.96,bottom=.38,top=.72,wspace=.40)
 shift=np.linspace(-.2,.2,801);base=np.array([-.12,-.06,0,.06,.12])
 for ax in axs:setup(ax)
 for b in base:axs[0].plot(shift,shift+b,color=blue,lw=2,alpha=.8)
 axs[0].axhline(0,color=orange,ls="--",lw=2)
 axs[0].set(xlabel="Smooth margin shift δ",ylabel="Correct-class margin",xticks=[-.2,0,.2]);axs[0].set_title("Five smooth margins",fontsize=27,pad=24)
 accuracy=np.mean(np.round(shift[:,None]+base,12)>0,axis=1)
 axs[1].step(shift,accuracy,where="post",color=green,lw=3)
 axs[1].set(xlabel="Smooth margin shift δ",ylabel="Accuracy",xticks=[-.2,0,.2],yticks=[0,.2,.4,.6,.8,1],ylim=(-.04,1.04));axs[1].set_title("Discrete correctness",fontsize=27,pad=24)
 title="A thresholded metric can jump while its margins vary smoothly"
 footer="Mathematical example: N = 5; correct iff margin > 0\nOne prediction change moves accuracy by 1/N = 0.2."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.35)
fig.text(.5,.08,footer,ha="center",fontsize=24,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
