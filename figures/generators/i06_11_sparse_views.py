"""I06-11's exact soft-threshold map and fixed existing sparse-coding fixture."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output
name=out.stem.removeprefix("I06-11-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i06-11-"+name})
fig,ax=plt.subplots(figsize=(520/72,850/72),facecolor="#F8FAFC")
fig.subplots_adjust(left=.24,right=.94,bottom=.35,top=.76)
ax.set_facecolor("#F8FAFC");ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True)
ax.spines[["top","right"]].set_visible(False)
if name=="soft-threshold-curve":
    u=np.linspace(-.7,.7,401);f=np.sign(u)*np.maximum(np.abs(u)-.2,0)
    ax.plot(u,u,color="#CBD5E1",ls="--",lw=2)
    ax.plot(u,f,color="#7C3AED",lw=3)
    pts=np.array([.1,.5,-.4]);v=np.sign(pts)*np.maximum(np.abs(pts)-.2,0)
    ax.scatter(pts,v,color="#D97706",s=95,zorder=4)
    ax.set(xlabel="Input u",ylabel="Thresholded S₀.₂(u)",xlim=(-.7,.7),ylim=(-.7,.7),xticks=[-.5,0,.5],yticks=[-.5,0,.5]);ax.set_aspect("equal")
    title="Soft threshold keeps signs,\nshrinks and creates zeros"
    footer="τ = 0.2\n0.1 → 0; 0.5 → 0.3; −0.4 → −0.2"
elif name=="true-estimated-support":
    rng=np.random.default_rng(20261001);D=rng.normal(size=(5,8));D/=np.linalg.norm(D,axis=0,keepdims=True)
    true=np.zeros((24,8))
    for row in true:
        ids=rng.choice(8,2,replace=False);row[ids]=rng.normal(size=2)
    x=true@D.T;z=np.zeros_like(true);eta=1/np.linalg.norm(D,ord=2)**2
    for _ in range(100):
        u=z-eta*((z@D.T-x)@D);z=np.sign(u)*np.maximum(np.abs(u)-eta*.03,0)
    j=np.arange(8);ax.bar(j-.18,true[0],width=.34,color="#2563EB",label="True code")
    ax.bar(j+.18,z[0],width=.34,color="#D97706",edgecolor="#0F172A",hatch="//",label="ISTA code")
    ax.set(xlabel="Feature index",ylabel="Coefficient",xticks=[0,2,4,6],ylim=(min(true[0].min(),z[0].min())-.2,max(true[0].max(),z[0].max())+.3))
    ax.axhline(0,color="#475569",lw=1.5)
    fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.55,.23),frameon=False,fontsize=24,ncol=1)
    title="Similar reconstruction need not\nrecover the same support"
    footer="Existing lab, first of 24 inputs\nD: 5 × 8; λ=.03; 100 ISTA steps"
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.4)
fig.text(.5,.10,footer,ha="center",fontsize=24,color="#475569",linespacing=1.6)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
