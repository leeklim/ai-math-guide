"""Render analytic circle geometry under I06-08's permitted transformations."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i06-08-invariance"})
fig,axs=plt.subplots(1,3,figsize=(1560/72,740/72),facecolor="#F8FAFC")
fig.subplots_adjust(left=.055,right=.97,bottom=.38,top=.80,wspace=.27)
theta=np.linspace(0,2*np.pi,361);circle=np.column_stack([np.cos(theta),np.sin(theta)])
Q=np.array([[0.,-1.],[1.,0.]])
for ax,M,label in zip(axs,[Q,3*np.eye(2),np.diag([3.,1.])],["Orthogonal Q","Uniform 3I","Unequal scales"]):
    v=circle@M
    ax.set_facecolor("#F8FAFC");ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True)
    ax.plot(circle[:,0],circle[:,1],color="#2563EB",ls="--",lw=2,label="Reference")
    ax.plot(v[:,0],v[:,1],color="#7C3AED",lw=3,label="Transformed")
    ax.scatter([v[0,0]],[v[0,1]],marker="D",s=80,color="#D97706",zorder=4)
    ax.set_aspect("equal");ax.set(xlim=(-3.4,3.4),ylim=(-3.4,3.4),xticks=[-3,0,3],yticks=[-3,0,3])
    ax.set_title(label,fontsize=28,pad=20);ax.set(xlabel="Coordinate 1",ylabel="Coordinate 2")
fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.24),ncol=2,frameon=False,fontsize=24)
fig.suptitle("Which geometry differences does linear CKA ignore?",fontsize=30,y=.95)
fig.text(.49,.15,"Rotation preserves Gram; uniform scale cancels in normalization.",fontsize=26,ha="center",color="#059669")
fig.text(.49,.08,"Unequal coordinate scaling can change alignment. Analytic circle, not model data.",fontsize=25,ha="center",color="#475569")
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
