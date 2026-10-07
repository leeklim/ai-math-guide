"""Show the existing I06-09 CPU fixture's signed ranking, without sorting by label."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":25,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i06-09-ranking"})
rng=np.random.default_rng(20261001);labels=np.tile(np.array([0,1]),10);rng.shuffle(labels)
x=rng.normal(0,.7,(20,6));latent=2*labels-1;x[:,0]+=1.4*latent;x[:,1]+=.7*latent
v=np.array([1.,.5,0,0,0,0]);v/=np.linalg.norm(v);s=x@v;order=np.argsort(s)
fig,ax=plt.subplots(figsize=(1040/72,1050/72),facecolor="#F8FAFC")
fig.subplots_adjust(left=.17,right=.92,bottom=.22,top=.85)
colors=["#2563EB"]*5+["#CBD5E1"]*10+["#059669"]*5
bars=ax.barh(np.arange(20),s[order],color=colors,edgecolor=colors)
for i in range(5):
    bars[i].set_edgecolor("#0F172A");bars[i].set_hatch("//")
ax.set_facecolor("#F8FAFC");ax.grid(axis="x",color="#CBD5E1",alpha=.6);ax.set_axisbelow(True)
ax.set(xlabel="Signed feature score",ylabel="Input row ID",yticks=np.arange(20),yticklabels=order)
ax.axvline(0,color="#475569",lw=1.5)
fig.suptitle("Rank by score: top and bottom see opposite ends",fontsize=30,y=.96)
fig.text(.5,.12,"Blue hatched: bottom 5. Green: top 5. Gray: remaining inputs.",ha="center",fontsize=26,color="#475569")
fig.text(.5,.06,"Existing synthetic fixture, 20 × 6. Labels did not select the rank.",ha="center",fontsize=25,color="#475569")
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
