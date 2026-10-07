"""Gradient geometry and the existing TracIn toy inputs for I08-12."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix("I08-12-")
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706"
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i08-12-"+name})
def setup(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
def arrow(ax,v,c,label,ls="-",head=10):
 ax.annotate("",xy=v,xytext=(0,0),arrowprops=dict(arrowstyle="->",mutation_scale=head,lw=2.5,color=c,linestyle=ls));ax.plot([],[],color=c,lw=3,ls=ls,label=label)
if name=="sgd-dot-product-sign":
 fig,axs=plt.subplots(1,3,figsize=(1320/72,880/72),facecolor=bg);fig.subplots_adjust(left=.075,right=.97,bottom=.38,top=.72,wspace=.35)
 for ax,g,title in zip(axs,[(1,1),(-1,1),(0,1)],["Dot +1: loss decreases","Dot −1: loss increases","Dot 0: first-order zero"]):
  setup(ax);arrow(ax,(1,0),blue,"g_test");arrow(ax,g,purple,"g_train");arrow(ax,-.4*np.array(g),green,"Update −η g_train",ls="--")
  ax.set(xlim=(-1.4,1.4),ylim=(-1.2,1.4),xticks=[-1,0,1],yticks=[-1,0,1],xlabel="Gradient coordinate 1",ylabel="Gradient coordinate 2");ax.set_aspect("equal")
  ax.set_title(title,fontsize=25,pad=25)
 fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.22),frameon=False,fontsize=24,ncol=3)
 title="A positive gradient dot product corresponds to test-loss decrease"
 footer="Illustrative fixed gradients; η = 0.4; ΔL_test ≈ −η g_testᵀg_train\nTracIn assigns a positive score to this decrease."
elif name=="checkpoint-gradient-pairs":
 gs=np.array([[1.,0.],[.5,.5],[-.2,1.]]);gt=np.array([[.8,.2],[.4,.6],[.1,.9]]);eta=[.1,.05,.02]
 fig,axs=plt.subplots(1,3,figsize=(1320/72,880/72),facecolor=bg);fig.subplots_adjust(left=.075,right=.97,bottom=.38,top=.72,wspace=.35)
 for i,(ax,a,b,e) in enumerate(zip(axs,gs,gt,eta)):
  setup(ax);arrow(ax,a,blue,"Training gradient");arrow(ax,b,purple,"Test gradient",ls="--")
  ax.set(xlim=(-.35,1.2),ylim=(-.2,1.2),xticks=[0,.5,1],yticks=[0,.5,1],xlabel="Parameter coordinate 1",ylabel="Parameter coordinate 2");ax.set_aspect("equal")
  ax.set_title("Checkpoint "+str(i+1)+"\nη="+str(e)+", dot="+str(round(a@b,2)),fontsize=26,pad=25)
 fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.22),frameon=False,fontsize=24,ncol=2)
 title="Pair both gradients at the same checkpoint and coordinates"
 footer="Existing two-dimensional CPU gradients; all three inner products are positive\nThe two arrows in each panel use the same parameter space."
elif name=="weighted-checkpoint-sum":
 fig,ax=plt.subplots(figsize=(520/72,820/72),facecolor=bg);fig.subplots_adjust(left=.23,right=.92,bottom=.38,top=.76);setup(ax)
 vals=np.array([.08,.025,.0176]);ax.bar(np.arange(3),vals,color=purple,width=.54)
 for i,v in enumerate(vals):ax.text(i,v+.005,str(v),ha="center",fontsize=24,color=purple)
 ax.set(xlabel="Checkpoint index",ylabel="η-weighted contribution",xticks=[0,1,2],xticklabels=["1","2","3"],ylim=(0,.105))
 title="Weight each checkpoint\nbefore adding"
 footer="η = (0.1, 0.05, 0.02)\nSum = 0.08 + 0.025 + 0.0176\nTracIn score = 0.1226."
elif name=="norm-versus-cosine-ranking":
 fig,axs=plt.subplots(1,3,figsize=(1320/72,880/72),facecolor=bg);fig.subplots_adjust(left=.075,right=.97,bottom=.38,top=.72,wspace=.36)
 for ax in axs:setup(ax)
 arrow(axs[0],(10,10),purple,"A = (10,10)");arrow(axs[0],(1,0),blue,"B = g_test = (1,0)",head=7)
 axs[0].set(xlim=(-.6,11.2),ylim=(-.6,11.2),xticks=[0,5,10],yticks=[0,5,10],xlabel="Gradient coordinate 1",ylabel="Gradient coordinate 2");axs[0].set_aspect("equal");axs[0].set_title("Magnitude vs angle",fontsize=26,pad=25)
 axs[1].bar([0,1],[10,1],color=[purple,blue],width=.55);axs[1].set(xticks=[0,1],xticklabels=["A","B"],ylabel="Raw dot product",ylim=(0,11));axs[1].set_title("Raw: A ranks higher",fontsize=26,pad=25)
 axs[2].bar([0,1],[1/np.sqrt(2),1],color=[purple,blue],width=.55);axs[2].set(xticks=[0,1],xticklabels=["A","B"],ylabel="Cosine similarity",ylim=(0,1.1));axs[2].set_title("Cosine: B ranks higher",fontsize=26,pad=25)
 fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.22),frameon=False,fontsize=24,ncol=2)
 title="Removing gradient magnitude changes the attribution estimand"
 footer="Mathematical candidates: ||A|| = √200; ||B|| = 1\nRaw dot = norm product × cosine; normalized scores need not rank the same."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.35)
fig.text(.5,.08,footer,ha="center",fontsize=24,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
