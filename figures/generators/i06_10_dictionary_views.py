"""Render the existing I06-10 120-degree dictionary and a basis/ReLU counterexample."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output
name=out.stem.removeprefix("I06-10-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i06-10-"+name})
cols=["#2563EB","#7C3AED","#059669"];bg="#F8FAFC"
angles=np.deg2rad([0.,120.,240.]);D=np.stack([np.cos(angles),np.sin(angles)]);z=np.array([1.,0.,.8]);a=D@z;decoded=D.T@a
assert np.allclose(decoded,[.6,-.9,.3])
def axis(ax):
    ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True)
    ax.set_aspect("equal");ax.set(xlim=(-1.5,1.5),ylim=(-1.4,1.4),xticks=[-1,0,1],yticks=[-1,0,1],xlabel="Neuron 1",ylabel="Neuron 2")
def arrow(ax,start,end,col,ls="-"):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=11,lw=3,color=col,linestyle=ls,shrinkA=3,shrinkB=0))
if name=="weighted-vector-sum":
    fig,axs=plt.subplots(1,2,figsize=(1040/72,800/72),facecolor=bg)
    fig.subplots_adjust(left=.095,right=.95,bottom=.32,top=.77,wspace=.35)
    for ax in axs:axis(ax)
    for j in range(3):
        arrow(axs[0],(0,0),D[:,j],cols[j],"-" if z[j]>0 else "--")
    axs[0].text(.96,.18,"d₁",color=cols[0],fontsize=25)
    axs[0].text(-1.06,.97,"d₂: off",color=cols[1],fontsize=25)
    axs[0].text(-1.06,-1.11,"d₃",color=cols[2],fontsize=25)
    arrow(axs[1],(0,0),D[:,0],cols[0]);arrow(axs[1],D[:,0],a,cols[2]);arrow(axs[1],(0,0),a,"#D97706")
    axs[1].text(.4,.19,"d₁",color=cols[0],fontsize=25)
    axs[1].text(.96,-.51,"0.8 d₃",color=cols[2],fontsize=25)
    axs[1].text(-.18,-1.12,"a ≈ (0.6,−0.693)",color="#D97706",fontsize=25)
    axs[0].set_title("Three feature directions",fontsize=28,pad=20)
    axs[1].set_title("Two active contributions",fontsize=28,pad=20)
    title="The existing toy: z = (1,0,0.8), a = Dz"
    footer="Dashed d₂ has coefficient zero; a still has two nonzero neuron coordinates."
elif name=="dot-response-vs-code":
    fig,ax=plt.subplots(figsize=(520/72,800/72),facecolor=bg)
    fig.subplots_adjust(left=.23,right=.94,bottom=.32,top=.75)
    ax.set_facecolor(bg);ax.grid(axis="y",color="#CBD5E1",alpha=.6);ax.set_axisbelow(True)
    j=np.arange(3);ax.bar(j-.19,z,width=.36,color="#2563EB",label="True z")
    ax.bar(j+.19,decoded,width=.36,color="#D97706",edgecolor="#0F172A",hatch="//",label="Dᵀa")
    ax.set(xticks=j,xticklabels=["1","2","3"],xlabel="Feature",ylabel="Coefficient / response",ylim=(-1.2,1.35),yticks=[-1,0,1])
    ax.axhline(0,color="#475569",lw=1.5)
    fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.53,.20),ncol=2,frameon=False,fontsize=24)
    title="Dot responses mix features;\nthey are not the true code"
    footer="z=(1,0,0.8); Dᵀa=(0.6,−0.9,0.3)"
elif name=="relu-basis-order":
    fig,axs=plt.subplots(1,2,figsize=(1040/72,790/72),facecolor=bg)
    fig.subplots_adjust(left=.095,right=.95,bottom=.32,top=.77,wspace=.35)
    Q=np.array([[np.cos(angles[1]),-np.sin(angles[1])],[np.sin(angles[1]),np.cos(angles[1])]])
    left=Q@np.maximum(D[:,0],0);right=np.maximum(Q@D[:,0],0)
    for ax,v,col in zip(axs,[left,right],["#7C3AED","#059669"]):axis(ax);arrow(ax,(0,0),v,col)
    axs[0].set_title("Q ReLU(a)",fontsize=28,pad=20);axs[1].set_title("ReLU(Q a)",fontsize=28,pad=20)
    axs[0].text(-1.13,-.84,"(−0.5, √3/2)",fontsize=26,color="#7C3AED")
    axs[1].text(-.98,-.84,"(0, √3/2)",fontsize=26,color="#059669")
    title="Coordinate-wise ReLU does not commute with rotation"
    footer="Mathematical example: a=d₁, Q rotates by 120°. The order changes the output."
else:raise ValueError(name)
fig.suptitle(title,fontsize=29,y=.95,linespacing=1.4)
fig.text(.5,.09,footer,ha="center",fontsize=25,color="#475569")
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
