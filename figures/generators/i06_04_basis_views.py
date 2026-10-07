"""Plot the exact existing i06_04_neuron_basis synthetic fixture, without a model."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt

p=ArgumentParser(); p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output; name=out.stem.removeprefix("I06-04-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,
                    "xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none",
                    "svg.hashsalt":"i06-04-"+name})
blue,purple,green,bg="#2563EB","#7C3AED","#059669","#F8FAFC"
rng=np.random.default_rng(20261001)
signal=rng.normal(size=60)
a=rng.normal(scale=.25,size=(60,4)); a[:,0]+=signal
q,_=np.linalg.qr(rng.normal(size=(4,4))); rotated=a@q
before=np.linalg.norm(a[:,None,:]-a[None,:,:],axis=-1)
after=np.linalg.norm(rotated[:,None,:]-rotated[None,:,:],axis=-1)
assert np.allclose(before,after,atol=1e-12)
fig,ax=plt.subplots(figsize=(520/72,800/72),facecolor=bg)
fig.subplots_adjust(left=.23,right=.94,bottom=.29,top=.65)
ax.set_facecolor(bg); ax.spines[["top","right"]].set_visible(False)
ax.grid(color="#CBD5E1",alpha=.55); ax.set_axisbelow(True)
if name=="coordinate-correlations":
    c0=np.abs(np.corrcoef(a.T,signal)[-1,:-1])
    c1=np.abs(np.corrcoef(rotated.T,signal)[-1,:-1])
    x=np.arange(4)
    ax.bar(x-.18,c0,width=.33,color=blue,label="Original basis")
    ax.bar(x+.18,c1,width=.33,color=purple,hatch="//",label="Rotated basis")
    ax.set(xlabel="Coordinate index",ylabel="Absolute signal correlation",xticks=x,ylim=(0,1.05),yticks=[0,.5,1])
    ax.legend(loc="upper center",bbox_to_anchor=(.5,.82),bbox_transform=fig.transFigure,fontsize=24,facecolor=bg)
    title="The best coordinate can change\nwhile the space retains the signal"
    footer="60 lab inputs; 4 coordinates\nAll coordinates rotate together."
elif name=="pairwise-distance-invariance":
    ax.set_position((.23,.30,.71,.48))
    idx=np.triu_indices(60,1); u,v=before[idx],after[idx]
    limit=float(max(u.max(),v.max()))*1.05
    ax.plot([0,limit],[0,limit],color=purple,ls="--",lw=2.3,zorder=2)
    ax.scatter(u,v,color=green,s=18,alpha=.4,zorder=3)
    ax.set(xlabel="Original distance",ylabel="Rotated distance",xlim=(0,limit),ylim=(0,limit))
    ax.set_aspect("equal")
    title="Orthogonal rotation preserves\neach pairwise distance"
    footer="1,770 input pairs (60 rows)\nAll 4 coordinates enter each norm."
else:
    raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.4)
fig.text(.5,.13,footer,fontsize=24,color="#475569",ha="center",linespacing=1.65)
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
