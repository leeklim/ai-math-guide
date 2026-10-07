"""Mathematical metric illustrations for I08-13; not Pythia observations."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix("I08-13-")
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706"
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i08-13-"+name})
def setup(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
if name=="condition-mean-scale":
 place=np.array([[1.5,.5],[1.5,1.5],[2.5,.5],[2.5,1.5]])
 animal=np.array([[-1.5,-1.5],[-1.5,-.5],[-.5,-1.5],[-.5,-.5]])
 fig,axs=plt.subplots(1,2,figsize=(1120/72,900/72),facecolor=bg);fig.subplots_adjust(left=.10,right=.96,bottom=.38,top=.72,wspace=.38)
 for ax,scale in zip(axs,[1,2]):
  setup(ax);P=place*scale;A=animal*scale;pm=P.mean(axis=0);am=A.mean(axis=0)
  ax.scatter(P[:,0],P[:,1],color=blue,marker="o",s=70,label="Place condition");ax.scatter(A[:,0],A[:,1],color=green,marker="s",s=70,label="Animal condition")
  ax.scatter([pm[0],am[0]],[pm[1],am[1]],color=orange,marker="X",s=110,label="Condition mean",zorder=5)
  ax.annotate("",xy=pm,xytext=am,arrowprops=dict(arrowstyle="->",mutation_scale=12,lw=2.5,color=purple,shrinkA=10,shrinkB=10))
  ax.set(xlim=(-3.6,5.6),ylim=(-3.6,3.6),xticks=[-2,0,2,4],yticks=[-2,0,2],xlabel="Activation coordinate 1",ylabel="Activation coordinate 2");ax.set_aspect("equal")
  ax.set_title("Scale "+str(scale)+"; norm="+("√13" if scale==1 else "2√13"),fontsize=27,pad=24)
 fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.22),ncol=3,frameon=False,fontsize=24)
 title="Mean separation can increase under pure activation scaling"
 footer="Mathematical eight-point example; not Pythia activations\nDoubling every vector doubles the mean-difference norm, not the cosine geometry."
elif name=="first-token-nll":
 fig,ax=plt.subplots(figsize=(520/72,840/72),facecolor=bg);fig.subplots_adjust(left=.23,right=.92,bottom=.38,top=.76);setup(ax)
 p=np.linspace(.05,.95,200);ax.plot(p,-np.log(p),color=green,lw=3)
 ax.scatter([.1,.5],[-np.log(.1),-np.log(.5)],color=orange,s=65,zorder=5)
 ax.text(.18,2.40,"p = 0.1",fontsize=24,color=orange);ax.text(.57,1.02,"p = 0.5",fontsize=24,color=orange)
 ax.set(xlabel="Fixed target probability",ylabel="First-token NLL",xticks=[.1,.5,.9],yticks=[0,1,2,3],ylim=(0,3.2))
 title="Higher target probability\nmeans lower NLL"
 footer="NLL = −log p\nAverage eight prompt first-token NLLs.\nNot full-completion correctness."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.35)
fig.text(.5,.08,footer,ha="center",fontsize=24,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
