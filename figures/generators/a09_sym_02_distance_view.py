"""Raw versus permutation-aligned Euclidean distance for A09-SYM-02."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"sym-02-distance"})
bg="#F8FAFC";blue="#2563EB";green="#059669";purple="#7C3AED"
a=np.array([1,3]);b=np.array([3,1]);P=np.array([[0,1],[1,0]]);assert np.all(P@b==a)
fig,axs=plt.subplots(2,1,figsize=(520/72,1100/72),facecolor=bg);fig.subplots_adjust(left=.20,right=.91,bottom=.20,top=.81,hspace=.58)
for ax in axs:
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False);ax.set(xlim=(0,4.2),ylim=(0,4.2),xticks=[0,2,4],yticks=[0,2,4],xlabel="Coordinate 1",ylabel="Coordinate 2");ax.set_aspect("equal")
axs[0].scatter(*a,color=blue,s=90,zorder=5);axs[0].scatter(*b,color=green,marker="s",s=90,zorder=5);axs[0].plot([1,3],[3,1],color=purple,ls="--",lw=2.5)
axs[0].text(.20,3.40,"(1,3)",color=blue,fontsize=25);axs[0].text(2.40,.48,"(3,1)",color=green,fontsize=25);axs[0].text(2.30,2.85,"√8",color=purple,fontsize=27);axs[0].set_title("Raw distance = √8",fontsize=27,pad=22)
axs[1].scatter(*a,facecolors="none",edgecolors=green,s=230,lw=2.5,zorder=4);axs[1].scatter(*a,color=blue,s=45,zorder=5);axs[1].text(.2,3.55,"a = Pb = (1,3)",fontsize=24,color=green);axs[1].set_title("Aligned distance = 0",fontsize=27,pad=22)
fig.suptitle("Reordering can remove\na coordinate distance",fontsize=28,y=.94,linespacing=1.35);fig.text(.5,.05,"P swaps coordinates.\nEuclidean distance is P-invariant.\nNot a proof about arbitrary models.",ha="center",fontsize=24,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)

