"""Small structural-causal-model distributions for A09-CAU-01."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-CAU-01-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"cau01-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626"
def style(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
if name=="joint-noise-output-law":
 fig,axs=plt.subplots(2,2,figsize=(1160/72,1200/72),facecolor=bg);fig.subplots_adjust(left=.12,right=.93,bottom=.23,top=.81,hspace=.62,wspace=.44)
 joints=[np.full((2,2),.25),np.diag([.5,.5])]
 for col,(joint,label) in enumerate(zip(joints,["Independent joint","Paired joint"])):
  a=axs[0,col];a.set_facecolor(bg);a.pcolormesh(np.arange(3)-.5,np.arange(3)-.5,joint,vmin=0,vmax=.5,cmap="Blues",shading="flat",rasterized=False);a.set_aspect("equal");a.set(xticks=[0,1],yticks=[0,1],xlabel="U_M",ylabel="U_Y");a.set_title(label,fontsize=28,pad=27)
  for row in range(2):
   for k in range(2):a.text(k,row,f"{joint[row,k]:g}",ha="center",va="center",fontsize=29,color="white" if joint[row,k]>.3 else "#0F172A")
  probs=np.array([joint[0,0],joint[0,1]+joint[1,0],joint[1,1]])
  a=axs[1,col];style(a);a.bar([0,1,2],probs,color=green,width=.50);a.set(xlim=(-.65,2.65),ylim=(0,.67),xticks=[0,1,2],yticks=[0,.25,.5],xlabel="Y=U_M+U_Y",ylabel="Probability")
  for k,v in enumerate(probs):a.text(k,v+.045,f"{v:g}",ha="center",fontsize=27,color=green)
 title="Same noise marginals, different observational outcomes"
 footer="X=U_X=0; U_M and U_Y each have P(0)=P(1)=0.5.\nTop cells give joint probabilities, not marginal probabilities.\nThe equations stay fixed while the joint background law changes."
else:
 fig,ax=plt.subplots(figsize=(520/72,980/72),facecolor=bg);fig.subplots_adjust(left=.19,right=.92,bottom=.31,top=.77);style(ax)
 if name=="possible-edge-zero-sample":
  z=np.linspace(-1,2,101);ax.plot(z,z,color=purple,lw=3,label="t=1");ax.plot(z,np.zeros_like(z),color=green,lw=3,ls="--",label="t=0")
  ax.set(xlim=(-1.2,2.2),ylim=(-1.6,2.5),xticks=[-1,0,1,2],yticks=[-1,0,1,2],xlabel="z",ylabel="f(z,t)=zt");ax.legend(loc="upper left",fontsize=24,frameon=False)
  title="Possible influence\ncan vanish in one sample"
  footer="Illustrative product f(z,t)=zt.\nChanging z has no effect at t=0.\nParent use is possible at t=1."
 elif name=="same-graph-different-effect":
  x=np.linspace(0,1.15,121);ax.plot(x,3*x,color=green,lw=3,label="M=2X");ax.plot(x,5*x,color=orange,lw=3,ls="--",label="M=4X")
  ax.set(xlim=(-.08,1.22),ylim=(-.35,6.2),xticks=[0,.5,1],yticks=[0,2,4,6],xlabel="X",ylabel="Y=M+X");ax.legend(loc="upper left",fontsize=24,frameon=False)
  ax.scatter([1,1],[3,5],color=[green,orange],s=75,zorder=5);ax.text(.62,1.0,"Y=3X",color=green,fontsize=27);ax.text(.38,4.65,"Y=5X",color=orange,fontsize=27)
  title="Same parent graph\nwith slopes 3 and 5"
  footer="U_M=U_Y=0 in both models.\nOnly M's coefficient changes.\nEdges stay X→M, M→Y, X→Y."
 else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.955,linespacing=1.35);fig.text(.5,.045,footer,ha="center",fontsize=25 if name=="joint-noise-output-law" else 24,color="#475569",linespacing=1.55)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
