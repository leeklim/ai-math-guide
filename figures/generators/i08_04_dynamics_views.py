"""Render exact quadratic dynamics and checkpoint sampling counterexamples for I08-04."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser(); p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix("I08-04-")
bg="#F8FAFC";blue="#2563EB";green="#059669";amber="#D97706"
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,
 "xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i08-04-"+name})
def setup(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True)
 ax.spines[["top","right"]].set_visible(False)
if name=="discrete-versus-flow":
 fig,ax=plt.subplots(figsize=(520/72,770/72),facecolor=bg)
 fig.subplots_adjust(left=.20,right=.92,bottom=.39,top=.78);setup(ax)
 k=np.arange(21);t=.1*k;gd=2*.9**k;dense=np.linspace(0,2,201)
 ax.plot(dense,2*np.exp(-dense),lw=3,ls="--",color=green,label="Flow")
 ax.plot(t,gd,lw=2,marker="o",ms=4,color=blue,label="Discrete")
 ax.set(xlim=(0,2.1),ylim=(0,2.15),xticks=[0,1,2],yticks=[0,1,2],
        xlabel="Matched time t = 0.1 k",ylabel="Parameter θ")
 title="Match time before comparing"
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.53,.28),ncol=2,frameon=False,fontsize=24)
 fig.text(.5,.19,"k=20: θ ≈ 0.2432",ha="center",fontsize=25,color=blue)
 fig.text(.5,.13,"t=2: θ ≈ 0.2707",ha="center",fontsize=25,color=green)
 footer="Existing toy: λ=1, θ₀=2, η=0.1"
elif name=="quadratic-stability-regimes":
 fig,axs=plt.subplots(1,4,figsize=(1600/72,750/72),facecolor=bg)
 fig.subplots_adjust(left=.05,right=.98,bottom=.32,top=.74,wspace=.37)
 k=np.arange(9)
 for ax,eta,name2 in zip(axs,[.5,1.5,2.,2.2],["Same-sign decay","Alternating decay","No decay","Growing oscillation"]):
  setup(ax);r=1-eta;theta=r**k
  ax.plot(k,theta,lw=2,marker="o",ms=5,color=blue)
  ax.axhline(0,color="#475569",lw=1)
  ax.set(xlim=(-.2,8.2),ylim=(-4.5,4.5),xticks=[0,4,8],yticks=[-4,0,4],xlabel="Update k",ylabel="θ_k")
  ax.set_title("η="+str(eta)+"\nr="+str(round(r,1)),fontsize=27,pad=20)
  ax.text(.5,-.30,name2,ha="center",transform=ax.transAxes,fontsize=24,color="#475569")
 title="The multiplier r = 1 − η λ determines quadratic stability"
 fig.text(.5,.12,"λ=1, θ₀=1: convergence requires |r| < 1; η=2 is the boundary.",ha="center",fontsize=27,color=green)
 footer="Exact mathematical sequences, not neural-network measurements"
elif name=="sparse-checkpoints-hide-path":
 fig,ax=plt.subplots(figsize=(520/72,730/72),facecolor=bg)
 fig.subplots_adjust(left=.21,right=.93,bottom=.42,top=.78);setup(ax)
 step=np.linspace(0,1000,501)
 ax.plot(step,np.zeros_like(step),lw=3,color=blue,label="Constant")
 ax.plot(step,np.sin(2*np.pi*step/1000),lw=3,ls="--",color=green,label="Excursion")
 ax.scatter([0,1000],[0,0],color=amber,s=85,zorder=5)
 ax.set(xlim=(-50,1050),ylim=(-1.25,1.25),xticks=[0,1000],yticks=[-1,0,1],xlabel="Step",ylabel="Metric")
 title="Two snapshots hide the interval"
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.54,.26),ncol=1,frameon=False,fontsize=24)
 footer="Analytic paths with identical endpoints"
elif name=="decreasing-loss-curved-path":
 fig,ax=plt.subplots(figsize=(520/72,850/72),facecolor=bg)
 fig.subplots_adjust(left=.20,right=.93,bottom=.38,top=.79);setup(ax)
 t=np.linspace(0,2,401);x=2*np.exp(-t);y=2*np.exp(-4*t)
 ax.plot([x[0],x[-1]],[y[0],y[-1]],color="#64748B",ls="--",lw=2,label="Endpoint line")
 ax.plot(x,y,color=blue,lw=3,label="Exact flow")
 ax.scatter([x[0],x[-1]],[y[0],y[-1]],color=amber,s=80,zorder=5)
 ax.text(1.47,2.12,"t=0",fontsize=24,color=amber)
 ax.text(.52,.09,"t=2",fontsize=24,color=amber)
 ax.set_aspect("equal");ax.set(xlim=(-.1,2.35),ylim=(-.1,2.35),xticks=[0,1,2],yticks=[0,1,2],
 xlabel="Parameter x",ylabel="Parameter y")
 title="Decreasing loss, curved path"
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.55,.24),ncol=1,frameon=False,fontsize=24)
 fig.text(.5,.13,"L=(x²+4y²)/2: 10 → 0.0366",ha="center",fontsize=24,color=green)
 footer="Analytic flow, not a model experiment"
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94)
fig.text(.5,.055,footer,ha="center",fontsize=24,color="#475569")
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
