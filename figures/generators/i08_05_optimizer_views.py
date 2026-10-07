"""Render I08-05's fixed momentum list and the iid batch-noise scaling relation."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix("I08-05-")
bg="#F8FAFC";blue="#2563EB";green="#059669"
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,
 "xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i08-05-"+name})
def setup(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True)
 ax.spines[["top","right"]].set_visible(False)
if name=="iid-noise-scaling":
 fig,ax=plt.subplots(figsize=(520/72,720/72),facecolor=bg)
 fig.subplots_adjust(left=.23,right=.92,bottom=.34,top=.77);setup(ax)
 B=np.arange(1,9);ax.plot(B,1/B,lw=3,marker="o",color=blue)
 ax.set(xlim=(.7,8.3),ylim=(0,1.08),xticks=[1,2,4,8],yticks=[0,.5,1],
 xlabel="Batch size B",ylabel="Relative noise variance")
 title="Independent averaging: 1 / B"
 fig.text(.5,.19,"Fixed θ; iid example gradients.",ha="center",fontsize=24,color="#475569")
 footer="Correlated samples change the relation."
elif name=="momentum-order-path":
 gradients=[1.,-.5,2.,-1.5]
 def trajectory(gs):
  theta=0.;v=0.;thetas=[theta];vs=[v]
  for g in gs:v=.8*v+g;theta-=.1*v;thetas.append(theta);vs.append(v)
  return np.array(thetas),np.array(vs)
 f,fv=trajectory(gradients);r,rv=trajectory(gradients[::-1])
 assert np.isclose(sum(gradients),1.) and np.isclose(f[-1],-.3832) and np.isclose(r[-1],-.0552)
 fig,axs=plt.subplots(1,2,figsize=(1040/72,780/72),facecolor=bg)
 fig.subplots_adjust(left=.09,right=.96,bottom=.34,top=.72,wspace=.34)
 for ax,a,b,label in zip(axs,[f,fv],[r,rv],["Parameter θ_k","Momentum v_k"]):
  setup(ax);ax.plot(np.arange(5),a,color=blue,lw=3,marker="o",label="Forward")
  ax.plot(np.arange(5),b,color=green,lw=3,ls="--",marker="s",label="Reverse")
  ax.set(xlim=(-.1,4.1),xticks=[0,2,4],xlabel="Update k",ylabel=label)
  ax.set_title(label,fontsize=27,pad=18)
 title="The same gradient multiset makes different momentum paths"
 fig.text(.5,.82,"Fixed gradients: (1,−0.5,2,−1.5); β=0.8; η=0.1",ha="center",fontsize=27,color="#475569")
 fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.52,.21),ncol=2,frameon=False,fontsize=24)
 footer="θ₄: forward −0.3832; reverse −0.0552.\nPrescribed gradients, not a training experiment."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94)
fig.text(.5,.07,footer,ha="center",fontsize=24,color="#475569")
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
