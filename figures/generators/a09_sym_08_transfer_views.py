"""Mathematical transfer and metric examples for A09-SYM-08."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-SYM-08-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"sym08-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626"
def style(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
def arrow(ax,s,e,c,ls="-"):
 ax.annotate("",xy=e,xytext=s,arrowprops={"arrowstyle":"-|>,head_length=.25,head_width=.14","mutation_scale":15,"lw":3,"color":c,"ls":ls})
wide=name!="seed-specific-baselines"
if wide:
 fig,axs=plt.subplots(1,2,figsize=(1100/72,900/72),facecolor=bg);fig.subplots_adjust(left=.08,right=.96,bottom=.37,top=.76,wspace=.34);ax,ax2=axs;style(ax2)
else:
 fig,ax=plt.subplots(figsize=(520/72,1010/72),facecolor=bg);fig.subplots_adjust(left=.21,right=.91,bottom=.37,top=.77)
style(ax)
if name=="cka-and-coordinate-residual":
 X=np.array([[1.,0.],[-1.,0.],[0.,1.],[0.,-1.]]);c=1/np.sqrt(2);R=np.array([[c,-c],[c,c]]);Y=X@R
 raw=np.linalg.norm(X-Y)/np.sqrt(X.size)
 for axis,Z,label in [(ax,X,"Raw coordinates"),(ax2,X@R,"Fitted g=R45")]:
  for j,m in enumerate(["o","s","^","D"]):
   if axis is ax:axis.plot([Z[j,0],Y[j,0]],[Z[j,1],Y[j,1]],color="#94A3B8",lw=1.5)
   axis.scatter(*Z[j],s=160,marker=m,facecolors="none",edgecolors=blue if axis is ax else green,lw=2,zorder=4)
   axis.scatter(*Y[j],s=65,marker=m,color=orange,zorder=5)
  axis.set_aspect("equal");axis.set(xlim=(-1.5,1.5),ylim=(-1.5,1.5),xticks=[-1,0,1],yticks=[-1,0,1]);axis.set_title(label,fontsize=27,pad=24)
 title="Coordinate residual can improve while linear CKA stays the same"
 footer=f"Constructed centered X; Y=XR45.  Raw RMSE≈{raw:.3f} → aligned RMSE=0.\nXXᵀ=YYᵀ: linear CKA=1 before and after alignment.\nMarker shapes track four paired samples; orange is the target Y."
elif name=="row-to-column-direction":
 for axis,label in [(ax,"Seed a direction"),(ax2,"Seed b direction")]:
  axis.set_aspect("equal");axis.axhline(0,color="#94A3B8",lw=1);axis.axvline(0,color="#94A3B8",lw=1);axis.set(xlim=(-1.6,1.6),ylim=(-1.6,1.6),xticks=[-1,0,1],yticks=[-1,0,1]);axis.set_title(label,fontsize=27,pad=24)
 arrow(ax,(0,0),(1,0),blue);ax.text(.72,.34,"u⁽ᵃ⁾",color=blue,fontsize=29)
 arrow(ax2,(0,0),(0,-1),green);ax2.text(.27,-1.1,"gᵀu⁽ᵃ⁾",color=green,fontsize=28)
 arrow(ax2,(0,0),(0,1),red,"--");ax2.text(.26,1.12,"gu⁽ᵃ⁾",color=red,fontsize=28)
 title="Row alignment transposes when transferred to a column direction"
 footer="g=R90=[0 −1; 1 0] ; u⁽ᵃ⁾=(1,0)ᵀ\nu⁽ᵇ⁾=gᵀu⁽ᵃ⁾=(0,−1)ᵀ ; (u⁽ᵃ⁾)ᵀg=(0,−1).\nThe red dashed upward direction uses the wrong multiplication order."
elif name=="seed-specific-baselines":
 ax.bar([0,1],[2,2],width=.47,color=[blue,green]);ax.axhline(0,color="#94A3B8",lw=1);ax.text(-.12,2.30,"+2",color=blue,fontsize=29);ax.text(.88,2.30,"+2",color=green,fontsize=29)
 ax.set(xlim=(-.65,1.65),ylim=(-.3,3.4),xticks=[0,1],xticklabels=["Seed a","Seed b"],yticks=[0,1,2,3],ylabel="Within-seed ΔM")
 title="Compare each effect\nagainst its own baseline"
 footer="Illustrative numbers only\nSeed a: 12−10=+2\nSeed b: 102−100=+2"
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.955,linespacing=1.35);fig.text(.5,.045,footer,ha="center",fontsize=24 if not wide else 25,color="#475569",linespacing=1.55)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
