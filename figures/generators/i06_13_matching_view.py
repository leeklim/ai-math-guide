"""Exact absolute-cosine matrix and assignment from the existing I06-13 fixture."""
from argparse import ArgumentParser
from pathlib import Path
from itertools import permutations
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i06-13-matching"})
rng=np.random.default_rng(20261001);first=rng.normal(size=(7,5));first/=np.linalg.norm(first,axis=0,keepdims=True)
permutation=np.array([2,4,0,1,3]);signs=np.array([1.,-1.,1.,-1.,1.]);second=first[:,permutation]*signs+rng.normal(scale=.02,size=(7,5));second/=np.linalg.norm(second,axis=0,keepdims=True)
M=np.abs(first.T@second);order=max(permutations(range(5)),key=lambda order:sum(M[i,order[i]] for i in range(5)))
fig,ax=plt.subplots(figsize=(520/72,880/72),facecolor="#F8FAFC")
fig.subplots_adjust(left=.18,right=.91,bottom=.36,top=.77)
ax.pcolormesh(np.arange(6),np.arange(6),M,cmap="Blues",vmin=0,vmax=1,edgecolors="#CBD5E1",linewidth=1)
for i in range(5):
    for j in range(5):
        ax.text(j+.5,i+.5,f"{M[i,j]:.2f}",ha="center",va="center",fontsize=25,color="white" if M[i,j]>.65 else "#0F172A")
    ax.add_patch(Rectangle((order[i]+.05,i+.05),.9,.9,fill=False,edgecolor="#D97706",lw=2.5))
ax.set(xlim=(0,5),ylim=(5,0),xticks=np.arange(5)+.5,yticks=np.arange(5)+.5,xticklabels=np.arange(5),yticklabels=np.arange(5),xlabel="Run 2 column",ylabel="Run 1 column");ax.set_aspect("equal")
fig.suptitle("Match columns,\nnot diagonal indices",fontsize=28,y=.94,linespacing=1.4)
fig.text(.5,.22,"Orange outlines: optimal assignment\nAbsolute cosine, signed synthetic codes",ha="center",fontsize=24,color="#475569",linespacing=1.6)
fig.text(.5,.10,"Existing 7 × 5 lab, noise SD=.02\nRows/columns are feature IDs, not inputs.",ha="center",fontsize=24,color="#475569",linespacing=1.6)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
