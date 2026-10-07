"""Exact toy influence geometry and the existing ridge inputs, for I08-08."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix("I08-08-")
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706"
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i08-08-"+name})
def setup(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
def arrow(ax,end,color,label,ls="-"):
 ax.annotate("",xy=end,xytext=(0,0),arrowprops=dict(arrowstyle="->",mutation_scale=12,lw=2.5,color=color,linestyle=ls))
 ax.plot([],[],color=color,lw=3,ls=ls,label=label)
def single(height=850):
 fig,ax=plt.subplots(figsize=(520/72,height/72),facecolor=bg);fig.subplots_adjust(left=.23,right=.92,bottom=.40,top=.75);setup(ax);return fig,ax
if name=="inverse-curvature-displacement":
 fig,ax=single(950)
 arrow(ax,(1,1),blue,"Training gradient g")
 arrow(ax,(-1,-1),orange,"−g without curvature","--")
 arrow(ax,(-.25,-1),green,"−H⁻¹g")
 ax.set(xlim=(-1.4,1.4),ylim=(-1.4,1.4),xticks=[-1,0,1],yticks=[-1,0,1],xlabel="Parameter coordinate 1",ylabel="Parameter coordinate 2");ax.set_aspect("equal")
 title="Inverse curvature changes\nthe displacement direction"
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.24),frameon=False,fontsize=24)
 footer="H = diag(4, 1); g = (1, 1)\ndθ/dε = (−0.25, −1)"
elif name=="test-gradient-projection":
 fig,axs=plt.subplots(1,3,figsize=(1320/72,860/72),facecolor=bg);fig.subplots_adjust(left=.065,right=.97,bottom=.38,top=.72,wspace=.34)
 d=np.array([-.25,-1.])
 for ax,q,lab in zip(axs,[(1,1),(-1,-1),(1,-.25)],["I = −1.25: decreases","I = 1.25: increases","I = 0: first-order zero"]):
  setup(ax);arrow(ax,d,green,"dθ/dε");arrow(ax,q,purple,"Test gradient")
  ax.set(xlim=(-1.45,1.45),ylim=(-1.45,1.45),xticks=[-1,0,1],yticks=[-1,0,1],xlabel="Parameter coordinate 1",ylabel="Parameter coordinate 2");ax.set_aspect("equal")
  ax.set_title(lab,fontsize=26,pad=25)
 fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.22),ncol=2,frameon=False,fontsize=24)
 title="Test-loss influence is the projection onto the test gradient"
 footer="Fixed dθ/dε = (−0.25, −1); I = g_testᵀ dθ/dε\nSigns refer to positive upweighting, not removal."
elif name=="upweight-removal-sign":
 fig,ax=single();fig.subplots_adjust(left=.34)
 ax.barh([1,0],[-.125,.125],color=[purple,green],height=.45)
 ax.axvline(0,color="#64748B",lw=1.5);ax.set(yticks=[1,0],yticklabels=["ε = +0.1","ε = −0.1"],xlabel="Approximate change\nin test loss",xlim=(-.17,.17),xticks=[-.125,0,.125],xticklabels=["−0.125","0","0.125"])
 title="Changing the data weight\nchanges the sign"
 footer="Fixed I_up,loss = −1.25\nΔL_test ≈ ε I_up,loss"
elif name=="damping-changes-response":
 fig,ax=single();lam=np.linspace(0,2,201)
 ax.plot(lam,1/(4+lam),color=blue,lw=3,label="H eigenvalue 4")
 ax.plot(lam,1/(1+lam),color=green,lw=3,ls="--",label="H eigenvalue 1")
 ax.set(xlabel="Damping λ",ylabel="Inverse-response magnitude",xticks=[0,1,2],ylim=(0,1.1))
 title="Damping changes\nthe inverse response"
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.24),frameon=False,fontsize=24)
 footer="H = diag(4, 1); v = (1, 1)\nSolve (H + λI)u = v, not Hu = v."
elif name=="ridge-removal-comparison":
 x=np.array([-2.,-1.,1.,2.,3.]);y=np.array([-4.1,-1.8,2.2,3.9,8.5]);reg=.2;n=len(x)
 fit=lambda xx,yy:float((xx@yy)/(xx@xx+len(xx)*reg))
 theta=fit(x,y);H=np.mean(x*x)+reg;g=(theta*x-y)*x
 approx=g/((n-1)*H);adjusted=(g+reg*theta)/((n-1)*H)
 exact=np.array([fit(np.delete(x,i),np.delete(y,i))-theta for i in range(n)])
 fig,axs=plt.subplots(1,2,figsize=(1120/72,880/72),facecolor=bg);fig.subplots_adjust(left=.10,right=.96,bottom=.38,top=.72,wspace=.40)
 for ax,pred,label in zip(axs,[approx,adjusted],["Existing simplified code","Normalized first-order formula"]):
  setup(ax);idx=np.arange(1,6)
  ax.plot(idx,exact,color=orange,lw=3,marker="s",label="Exact normalized refit")
  ax.plot(idx,pred,color=purple,lw=3,marker="o",ls="--",label="First-order estimate")
  ax.set(xlabel="Removed example index",ylabel="Parameter change Δθ",xticks=idx,ylim=(-.48,.14));ax.set_title(label,fontsize=25,pad=25)
 fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.22),frameon=False,fontsize=24)
 title="Refitting tests a different error from the solve residual"
 footer="Same five ridge-regression inputs; λ = 0.2\nThe right numerator adds λθ; finite-removal error remains."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.35)
fig.text(.5,.08,footer,ha="center",fontsize=24,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
