"""Constructed matching and averaging examples for A09-SYM-04."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-SYM-04-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"sym04-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";red="#DC2626"
fig,ax=plt.subplots(figsize=(520/72,1010/72),facecolor=bg);fig.subplots_adjust(left=.21,right=.91,bottom=.37,top=.77);ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
x=np.linspace(-2,2,301)
if name=="correlation-not-output":
 ax.plot(x,x,color=blue,lw=3,label="hA(x)=x");ax.plot(x,x+5,color=purple,lw=3,ls="--",label="hB(x)=x+5")
 ax.set(xlim=(-2.2,2.2),ylim=(-2.7,7.8),xticks=[-2,0,2],yticks=[-2,0,2,4,6],xlabel="Input x",ylabel="Activation / output")
 title="Perfect correlation\nneed not mean equal outputs"
 footer="Corr(hA,hB)=1 for Var(x)>0.\nWith identity readouts:\nfB(x)−fA(x)=5."
elif name=="unaligned-weight-average":
 orig=np.maximum(x,0)+2*np.maximum(-x,0);ax.plot(x,orig,color=blue,lw=6,label="Original / swapped");ax.plot(x,orig,color=green,lw=2.5,ls="--",label="Aligned average");ax.axhline(0,color=red,lw=3,label="Unaligned average")
 ax.set(xlim=(-2.2,2.2),ylim=(-.7,4.9),xticks=[-2,0,2],yticks=[0,2,4],xlabel="Input x",ylabel="Model output")
 title="Function-preserving swaps\nneed not preserve averages"
 footer="Both originals: ReLU(x)+2ReLU(−x)\nUnaligned input weights average to 0.\nA constructed two-unit example."
else:raise ValueError(name)
fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.53,.27),ncol=1,frameon=False,fontsize=24)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.35);fig.text(.5,.05,footer,ha="center",fontsize=22,color="#475569",linespacing=1.6)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
