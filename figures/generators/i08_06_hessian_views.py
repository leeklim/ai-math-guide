"""Exact mathematical views for I08-06; no neural-model execution."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix("I08-06-")
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706"
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,
 "xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i08-06-"+name})
def setup(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True)
 ax.spines[["top","right"]].set_visible(False)
def single():
 fig,ax=plt.subplots(figsize=(520/72,820/72),facecolor=bg)
 fig.subplots_adjust(left=.23,right=.92,bottom=.38,top=.76);setup(ax)
 return fig,ax
if name=="curvature-directions":
 fig,axs=plt.subplots(1,3,figsize=(1280/72,760/72),facecolor=bg)
 fig.subplots_adjust(left=.075,right=.965,bottom=.35,top=.73,wspace=.4)
 eps=np.linspace(-1,1,201)
 for ax,lam,c in zip(axs,[4,1,-.5],[blue,purple,green]):
  setup(ax);ax.plot(eps,.5*lam*eps**2,color=c,lw=3)
  ax.axhline(0,color="#64748B",lw=1);ax.set(xlabel="Displacement ε",ylabel="Loss change",xticks=[-1,0,1],ylim=(-.5,2.2))
  ax.set_title("λ = "+str(lam),fontsize=28,pad=24)
 title="Stationary point: direction-specific curvature"
 fig.text(.5,.19,"H = diag(4, 1, −0.5);  ∇L = 0",ha="center",fontsize=26,color="#475569")
 footer="The negative-eigenvalue direction decreases loss locally."
elif name=="linear-term-matters":
 fig,ax=single();e=np.linspace(-.6,.6,301)
 ax.plot(e,2*e**2,color=purple,lw=3,label="Quadratic only")
 ax.plot(e,e+2*e**2,color=blue,lw=3,ls="--",label="Linear + quadratic")
 ax.axhline(0,color="#64748B",lw=1)
 ax.set(xlabel="Displacement ε",ylabel="Loss change",xticks=[-.5,0,.5])
 title="Positive curvature is not\na positive total change"
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.21),frameon=False,fontsize=24)
 footer="g = 1; H = 4\nSmall negative ε can lower loss."
elif name=="zero-curvature-fourth-order":
 fig,ax=single();e=np.linspace(-1,1,201)
 ax.plot(e,e**4,color=blue,lw=3,label="L(ε) = ε⁴")
 ax.plot(e,np.zeros_like(e),color=orange,lw=3,ls="--",label="L(ε) = 0")
 ax.set(xlabel="Displacement ε",ylabel="Loss change",xticks=[-1,0,1],ylim=(-.05,1.1))
 title="Zero Hessian at zero\nis not complete flatness"
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.21),frameon=False,fontsize=24)
 footer="Both have L′(0) = L″(0) = 0."
elif name=="rayleigh-weights":
 fig,ax=single();fig.subplots_adjust(left=.28);weights=np.array([1,4,1])/6
 ax.barh([2,1,0],weights,color=[blue,purple,green],height=.48)
 ax.set(yticks=[2,1,0],yticklabels=["λ = 4","λ = 1","λ = −0.5"],xlim=(0,.82),xticks=[0,.33,.67],xticklabels=["0","1/3","2/3"],xlabel="Squared-component weight")
 for y,w,lab in zip([2,1,0],weights,["1/6","4/6","1/6"]):ax.text(w+.025,y,lab,va="center",fontsize=24)
 title="Rayleigh quotient\nis a weighted average"
 footer="v = (1, 2, −1); ||v||² = 6\nR = (4 + 4 − 0.5) / 6 = 1.25"
elif name=="eigenmode-step-size":
 fig,axs=plt.subplots(1,2,figsize=(1080/72,780/72),facecolor=bg)
 fig.subplots_adjust(left=.105,right=.965,bottom=.36,top=.72,wspace=.43)
 k=np.arange(9)
 for ax,eta in zip(axs,[.4,.6]):
  setup(ax)
  for lam,c,ls in [(4,blue,"-"),(1,green,"--")]:
   r=1-eta*lam;ax.plot(k,r**k,color=c,ls=ls,lw=3,marker="o",label="λ="+str(lam)+", r="+str(round(r,1)))
  ax.set(xlabel="Update k",ylabel="Displacement component",xticks=[0,4,8])
  ax.set_title("η = "+str(eta),fontsize=28,pad=24)
  ax.legend(fontsize=22,frameon=False,loc="upper center",bbox_to_anchor=(.5,-.25))
 title="The largest positive eigenvalue controls the quadratic bound"
 footer="H = diag(4, 1); η < 2 / 4 = 0.5\nη = 0.6 destabilizes the λ = 4 component."
elif name=="power-absolute-dominance":
 fig,axs=plt.subplots(1,2,figsize=(1080/72,820/72),facecolor=bg)
 fig.subplots_adjust(left=.11,right=.965,bottom=.38,top=.72,wspace=.42)
 k=np.arange(9);raw=np.stack([3.**k,(-5.)**k],axis=1);v=raw/np.linalg.norm(raw,axis=1,keepdims=True)
 for ax in axs:setup(ax)
 axs[0].plot(k,v[:,0],lw=3,marker="o",color=blue,label="λ = 3 component")
 axs[0].plot(k,v[:,1],lw=3,marker="s",ls="--",color=green,label="λ = −5 component")
 axs[0].set(xlabel="Power step k",ylabel="Unit-vector component",xticks=[0,4,8]);axs[0].set_title("Normalize Hᵏ v₀",fontsize=28,pad=24)
 R=3*v[:,0]**2-5*v[:,1]**2
 axs[1].plot(k,R,color=purple,lw=3,marker="o");axs[1].axhline(-5,color=green,ls="--",lw=2)
 axs[1].set(xlabel="Power step k",ylabel="Rayleigh quotient",xticks=[0,4,8]);axs[1].set_title("Approaches −5, not 3",fontsize=28,pad=24)
 fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.22),ncol=2,frameon=False,fontsize=24)
 title="Power iteration favors the largest absolute eigenvalue"
 footer="H = diag(3, −5); v₀ = (1, 1) / √2\nThe dominant direction alternates sign."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.35)
fig.text(.5,.08,footer,ha="center",fontsize=24,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
