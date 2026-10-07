"""Fixed synthetic paired-design and trajectory examples for I08-11."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix("I08-11-")
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706"
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i08-11-"+name})
def setup(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
def single():
 fig,ax=plt.subplots(figsize=(520/72,820/72),facecolor=bg);fig.subplots_adjust(left=.23,right=.92,bottom=.38,top=.76);setup(ax);return fig,ax
rng=np.random.default_rng(20261001);seed_effect=rng.normal(0,.03,size=8);effect=.08+rng.normal(0,.01,size=8);B=.70+seed_effect;A=B+effect
paired=A-B;paired_se=paired.std(ddof=1)/np.sqrt(8);unpaired_se=np.sqrt(A.var(ddof=1)/8+B.var(ddof=1)/8)
assert paired_se<unpaired_se
if name=="paired-seed-outcomes":
 fig,axs=plt.subplots(1,2,figsize=(1120/72,860/72),facecolor=bg);fig.subplots_adjust(left=.11,right=.96,bottom=.38,top=.72,wspace=.42)
 for ax in axs:setup(ax)
 r=np.arange(1,9);axs[0].plot(r,A,color=blue,lw=3,marker="o",label="Method A");axs[0].plot(r,B,color=green,lw=3,ls="--",marker="s",label="Method B")
 axs[0].set(xlabel="Independent seed index",ylabel="Outcome",xticks=[1,4,8]);axs[0].set_title("Shared seed variation",fontsize=27,pad=24)
 axs[1].plot(r,paired,color=purple,lw=3,marker="o");axs[1].set(xlabel="Independent seed index",ylabel="Paired difference A − B",xticks=[1,4,8],ylim=(0,.12));axs[1].set_title("Difference within each seed",fontsize=26,pad=24)
 fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.23),ncol=2,frameon=False,fontsize=24)
 title="Pair first, then average the method differences"
 footer="Existing synthetic CPU experiment: eight independent seed units\nShared initialization-like noise cancels in each within-seed difference."
elif name=="paired-standard-error":
 fig,ax=single();fig.subplots_adjust(left=.36)
 ax.barh([1,0],[paired_se,unpaired_se],color=[purple,orange],height=.45)
 ax.set(yticks=[1,0],yticklabels=["Paired","Ignore pairs"],xlabel="Standard error",xlim=(0,unpaired_se*1.45))
 for y,val in [(1,paired_se),(0,unpaired_se)]:ax.text(val+unpaired_se*.04,y,f"{val:.4f}",va="center",fontsize=24)
 title="The same eight pairs\ngive different error estimates"
 footer="Shared positive covariance\nHere, paired differences vary less."
elif name=="covariance-condition":
 fig,ax=single();rho=np.linspace(-1,1,101)
 ax.plot(rho,2-2*rho,color=purple,lw=3);ax.axhline(2,color=orange,ls="--",lw=2)
 ax.set(xlabel="Correlation ρ",ylabel="Variance of A − B",xticks=[-1,0,1],yticks=[0,2,4],ylim=(-.2,4.2))
 title="Pairing helps precision\nonly with the right covariance"
 footer="Illustration: Var(A) = Var(B) = 1\nVar(A − B) = 2 − 2ρ."
elif name=="mean-hides-transition":
 fig,axs=plt.subplots(1,2,figsize=(1120/72,840/72),facecolor=bg);fig.subplots_adjust(left=.10,right=.96,bottom=.37,top=.72,wspace=.4)
 for ax in axs:setup(ax)
 k=np.array([0,1000,5000,6000]);f=np.array([0,1,1,1]);g=np.array([0,0,1,1])
 axs[0].step(k,f,where="post",color=blue,lw=3,label="Seed 1");axs[0].step(k,g,where="post",color=green,lw=3,ls="--",label="Seed 2")
 axs[1].step(k,(f+g)/2,where="post",color=purple,lw=3)
 for ax in axs:ax.set(xlabel="Training step",ylabel="Metric",xticks=[0,1000,5000],yticks=[0,.5,1],ylim=(-.07,1.12))
 axs[0].set_title("Individual transitions",fontsize=27,pad=24);axs[1].set_title("Pointwise mean",fontsize=27,pad=24)
 fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.23),ncol=2,frameon=False,fontsize=24)
 title="A mean of abrupt transitions can contain an intermediate plateau"
 footer="Existing text example: transitions at 1000 and 5000\nBetween them, the mean is 0.5; neither seed has metric 0.5."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.35)
fig.text(.5,.08,footer,ha="center",fontsize=24,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
