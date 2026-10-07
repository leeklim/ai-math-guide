"""Averaging and finite-check counterexamples for A09-SYM-03."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-SYM-03-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"sym03-"+name})
bg="#F8FAFC";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626"
fig,ax=plt.subplots(figsize=(520/72,940/72),facecolor=bg);fig.subplots_adjust(left=.21,right=.91,bottom=.35,top=.76);ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
if name=="unequal-average":
 x=np.linspace(-2.5,2.5,301);ax.plot(x,x*x,color=green,lw=3,label="Uniform weights");ax.plot(x,x*x+.5*x,color=purple,lw=3,ls="--",label="Weights 3/4, 1/4")
 ax.scatter([-2,2],[3,5],color=purple,s=80,zorder=5);ax.text(-2.45,2.30,"3",color=purple,fontsize=27);ax.text(1.35,6.05,"5",color=purple,fontsize=27)
 ax.set(xlim=(-2.7,2.7),ylim=(-.6,7),xticks=[-2,0,2],yticks=[0,2,4,6],xlabel="Input x",ylabel="Average value")
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.55,.245),ncol=1,frameon=False,fontsize=24)
 title="Unequal weights\ncan break invariance"
 footer="f(x)=x+x²; sign group {+1,−1}\nUniform average: x²\nUnequal average: x²+x/2"
elif name=="finite-check-misses-violation":
 x=np.linspace(-1.6,1.6,301);delta=-2*x*(x*x-1);ax.plot(x,delta,color=red,lw=3);ax.axhline(0,color="#94A3B8",lw=1);ax.scatter([-1,0,1],[0,0,0],color=orange,s=95,zorder=5)
 ax.set(xlim=(-1.7,1.7),ylim=(-5.6,5.6),xticks=[-1,0,1],yticks=[-4,0,4],xlabel="Input x",ylabel="Invariance difference")
 title="Finite checks can miss\ninvariance violations"
 footer="f(x)=x(x²−1); Δ=f(−x)−f(x)\nChecked x: −1, 0, 1; each Δ=0.\nMathematical counterexample."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.35);fig.text(.5,.05,footer,ha="center",fontsize=24,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)

