"""Known-SCM intervention and patch-policy views for A09-CAU-02."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-CAU-02-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"cau02-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626";muted="#475569"
def style(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
if name=="selected-versus-set-backgrounds":
 fig,axs=plt.subplots(1,3,figsize=(1440/72,1040/72),facecolor=bg);fig.subplots_adjust(left=.065,right=.96,bottom=.30,top=.78,wspace=.40)
 for k,a in enumerate(axs):
  style(a);a.set(xlim=(-.3,1.85),ylim=(-.35,1.9),xticks=[0,1],yticks=[0,1],xlabel="Z=U_Z",ylabel="U_X");a.set_aspect("equal");a.set_title(["Natural X","Condition X=2","Set X:=2"][k],fontsize=28,pad=24)
  for z in [0,1]:
   for ux in [0,1]:
    x=z+ux;y=x+z
    if k==1 and (z,ux)!=(1,1):
     a.scatter(z,ux,color="#94A3B8",marker="x",s=100,zorder=4)
    else:
     c=[blue,orange,green][k];a.scatter(z,ux,color=c,s=105,zorder=5)
     if k==2:x=2;y=x+z
     a.text(z+.10,ux+.11,f"X={x}\nY={y}",fontsize=24,color=c,ha="left",va="bottom",linespacing=1.30)
 title="Conditioning selects backgrounds; intervention keeps them"
 footer="U_Z and U_X are independent binary noises; U_Y=0.\nNatural: X=Z+U_X and Y=X+Z. Conditioning X=2 retains only (Z,U_X)=(1,1).\nUnder do(X=2), all four backgrounds retain probability 0.25."
elif name=="missing-parent-support":
 fig,ax=plt.subplots(figsize=(520/72,1000/72),facecolor=bg);fig.subplots_adjust(left=.20,right=.91,bottom=.35,top=.77)
 joint=np.array([[.25,0],[.25,.25],[0,.25]])
 ax.pcolormesh(np.arange(3)-.5,np.arange(4)-.5,joint,vmin=0,vmax=.25,cmap="Blues",rasterized=False)
 ax.set_aspect("equal");ax.set(xticks=[0,1],yticks=[0,1,2],xlabel="Z",ylabel="X")
 for x in range(3):
  for z in range(2):ax.text(z,x,f"{joint[x,z]:g}",ha="center",va="center",fontsize=30,color="white" if joint[x,z] else "#0F172A")
 ax.add_patch(Rectangle((-.5,1.5),1,1,fill=False,ec=red,lw=4));ax.text(.5,2.90,"Required (X=2,Z=0)",ha="center",fontsize=24,color=red)
 title="A required parent stratum\nhas no observed support"
 footer="P(X=2,Z=0)=0.\ndo(X=2) still includes Z=0.\nThe known SCM computes Y=2;\nthis absent cell cannot estimate\nP(Y | X=2,Z=0) from data."
else:
 fig,ax=plt.subplots(figsize=(520/72,1000/72),facecolor=bg);fig.subplots_adjust(left=.21,right=.92,bottom=.33,top=.76);style(ax)
 if name=="conditional-intervention-outcomes":
  x=np.array([2,3]);a=np.array([0,1]);b=np.array([.5,.5])
  ax.bar(x-.17,a,width=.30,color=orange,label="Condition X=2");ax.bar(x+.17,b,width=.30,color=green,hatch="//",label="do(X=2)")
  ax.set(xlim=(1.5,3.6),ylim=(0,1.45),xticks=[2,3],yticks=[0,.5,1],xlabel="Y",ylabel="Probability");ax.legend(loc="upper left",fontsize=23,frameon=False)
  for xx,y in zip(x+.17,b):ax.text(xx,y+.065,"0.5",ha="center",fontsize=25,color=green)
  ax.text(2.83,1.07,"1",ha="center",fontsize=25,color=orange)
  title="Selected and intervened\noutcome distributions"
  footer="Condition X=2: mean Y=3.\ndo(X=2): mean Y=2.5.\nComputed from the known SCM,\nnot identified from data alone."
 elif name=="source-mixture-patch-values":
  ax.bar([2,4],[.75,.25],width=.55,color=red);ax.set(xlim=(1.35,4.7),ylim=(0,1.1),xticks=[2,4],yticks=[0,.25,.5,.75,1],xlabel="First patched coordinate",ylabel="Probability")
  for xx,y in [(2,.75),(4,.25)]:ax.text(xx,y+.06,f"{y:g}",ha="center",fontsize=28,color=red)
  title="Source sampling changes\nthe patch-value distribution"
  footer="Source s1 is selected with 0.75;\nsource s2 with 0.25.\nThe same swap-and-scale map\nyields H=(2,1) or H=(4,2).\nIllustrative policy, not outputs."
 else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.95,linespacing=1.35);fig.text(.5,.042,footer,ha="center",fontsize=24 if name!="selected-versus-set-backgrounds" else 25,color=muted,linespacing=1.50)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)

