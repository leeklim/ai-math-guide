"""Illustrate I06-06's ridge penalty along a null direction of H."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i06-06-null-ridge"})
fig,ax=plt.subplots(figsize=(520/72,800/72),facecolor="#F8FAFC")
fig.subplots_adjust(left=.23,right=.94,bottom=.38,top=.74)
ax.set_facecolor("#F8FAFC");ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True)
ax.spines[["top","right"]].set_visible(False)
t=np.linspace(-2,2,401)
ax.plot(t,t*t,color="#7C3AED",lw=3,label="λ = 1")
ax.plot(t,np.zeros_like(t),color="#D97706",ls="--",lw=3,label="λ = 0")
ax.set(xlabel="Coefficient t along v",ylabel="Added objective cost",xlim=(-2,2),ylim=(-.3,4.3),xticks=[-2,0,2],yticks=[0,2,4])
ax.legend(fontsize=24,loc="upper center",frameon=False)
fig.suptitle("A null direction is flat\nuntil ridge adds cost",fontsize=28,y=.94,linespacing=1.4)
fig.text(.5,.15,"H v=0; ||v||=1\nw₀ · v=0 (minimum-norm base)\nAdded ridge cost: λ t²",ha="center",fontsize=24,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
