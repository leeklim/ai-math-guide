"""Constructed alignment-class and identifiability views for A09-SYM-07."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-SYM-07-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"sym07-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626"
def style(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
def arrow(ax,s,e,c,ls="-"):
 ax.annotate("",xy=e,xytext=s,arrowprops={"arrowstyle":"-|>,head_length=.25,head_width=.14","mutation_scale":15,"lw":3,"color":c,"ls":ls})
wide=name in ["transformation-geometries","unobserved-direction-freedom"]
if name=="transformation-geometries":
 fig,axs=plt.subplots(1,3,figsize=(1330/72,870/72),facecolor=bg);fig.subplots_adjust(left=.065,right=.97,bottom=.35,top=.76,wspace=.38)
elif wide:
 fig,axs=plt.subplots(1,2,figsize=(1100/72,870/72),facecolor=bg);fig.subplots_adjust(left=.08,right=.96,bottom=.35,top=.76,wspace=.34)
else:
 fig,ax=plt.subplots(figsize=(520/72,1010/72),facecolor=bg);fig.subplots_adjust(left=.21,right=.91,bottom=.37,top=.77);style(ax)
if name=="transformation-geometries":
 X=np.eye(2);c=1/np.sqrt(2);R=np.array([[c,-c],[c,c]])
 for axis,g,label in zip(axs,[np.array([[0.,1.],[1.,0.]]),R,np.array([[1.,1.],[0.,1.]])],["Permutation","Orthogonal rotation","Invertible shear"]):
  style(axis);Z=X@g
  axis.plot([0,1,0,0],[0,0,1,0],color=blue,lw=2,ls="--",alpha=.55)
  axis.plot([0,Z[0,0],Z[1,0],0],[0,Z[0,1],Z[1,1],0],color=purple,lw=3)
  for j,m in enumerate(["o","s"]):
   if label!="Permutation":axis.scatter(*X[j],s=140,marker=m,facecolors="none",edgecolors=blue,lw=2,zorder=4)
   axis.scatter(*Z[j],s=95,marker=m,color=purple,zorder=5)
  axis.text(1.12,-.35,"A",color=blue,fontsize=26);axis.text(-.38,1.14,"B",color=blue,fontsize=26)
  offsets=[(.12,.14),(.12,.17)] if label=="Permutation" else [(.12,-.25),(.12,.14)] if label=="Orthogonal rotation" else [(.12,.17),(.12,.14)]
  for j,(dx,dy) in enumerate(offsets):axis.text(Z[j,0]+dx,Z[j,1]+dy,"AB"[j],color=purple,fontsize=26)
  axis.set_aspect("equal");axis.set(xlim=(-.8,1.6),ylim=(-1.1,1.6),xticks=[0,1],yticks=[-1,0,1]);axis.set_title(label,fontsize=26,pad=25)
 title="Transformation classes remove different coordinate information"
 footer="Row convention: each sample x maps to xg.\nBlue dashed: original triangle ; purple solid: transformed triangle.\nCircle: sample A ; square: sample B.  Shear need not preserve distances."
elif name=="unattained-infimum":
 g=np.linspace(-1.2,1.2,501);ax.plot(g,np.abs(g),color=purple,lw=3)
 ax.scatter([0],[0],s=140,facecolors=bg,edgecolors=red,lw=3,zorder=6)
 seq=np.array([1,.5,.25,.125]);ax.scatter(seq,seq,color=orange,s=70,zorder=5)
 ax.set(xlim=(-1.3,1.3),ylim=(-.15,1.4),xticks=[-1,0,1],yticks=[0,.5,1],xlabel="Nonzero scalar g",ylabel="Residual |g|")
 title="Infimum zero,\nno invertible minimizer";footer="X=1 ; Y=0 ; g≠0\nThe open point g=0 is excluded.\nInfimum 0 is never attained."
elif name=="unobserved-direction-freedom":
 for axis,g,label in zip(axs,[np.eye(2),np.diag([1.,-1.])],["ĝ₁=I","ĝ₂=diag(1,−1)"]):
  style(axis);axis.set_aspect("equal");axis.axhline(0,color="#94A3B8",lw=1);axis.axvline(0,color="#94A3B8",lw=1)
  axis.scatter([1,2],[0,0],color=blue,s=100,zorder=6);arrow(axis,(0,0),np.array([0.,1.])@g,purple,"--")
  axis.set(xlim=(-.8,2.6),ylim=(-1.6,1.6),xticks=[0,1,2],yticks=[-1,0,1]);axis.set_title(label,fontsize=27,pad=22)
 title="Example rows cannot determine\nan unobserved direction"
 footer="Example data X=Y: rows (1,0), (2,0).  Both fitted residuals are zero.\nDashed purple: probe (0,1), not a model measurement.\nThe two optimal maps disagree off the observed subspace."
elif name=="zero-alignment-different-output":
 x=np.linspace(-2,2,301);ax.plot(x,x,color=blue,lw=3,label="Output A: x");ax.plot(x,2*x,color=orange,lw=3,ls="--",label="Output B: 2x")
 ax.set(xlim=(-2.2,2.2),ylim=(-4.6,4.6),xticks=[-2,0,2],yticks=[-4,0,4],xlabel="Input x",ylabel="Model output")
 title="Zero activation residual\ndoes not fix the readout"
 footer="X=(x,2x) ; Y=(2x,x) ; XP=Y\nBoth use the first coordinate.\nTheir functions still differ."
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.53,.265),ncol=1,frameon=False,fontsize=24)
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.955,linespacing=1.35);fig.text(.5,.045,footer,ha="center",fontsize=24 if not wide else 25,color="#475569",linespacing=1.55)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
