"""Known mediation toy equations and support for A09-CAU-04."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-CAU-04-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"cau04-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626"
def style(a):
 a.set_facecolor(bg);a.grid(color="#CBD5E1",alpha=.6);a.set_axisbelow(True);a.spines[["top","right"]].set_visible(False)
if name=="compatible-decomposition-steps":
 fig,axs=plt.subplots(1,2,figsize=(1160/72,1060/72),facecolor=bg);fig.subplots_adjust(left=.09,right=.95,bottom=.32,top=.76,wspace=.35)
 for a,vals,t in zip(axs,[[0,1,3],[0,1,4]],["Y=a+2m","Y=a+2m+am"]):
  style(a);a.plot([0,1],vals[:2],color=purple,lw=3,marker="o",ms=9);a.plot([1,2],vals[1:],color=green,lw=3,marker="o",ms=9);a.set(xlim=(-.3,2.4),ylim=(-.4,5.1),xticks=[0,1,2],xticklabels=["Baseline","Hybrid","Treated"],yticks=[0,1,2,3,4],ylabel="Outcome Y");a.set_title(t,fontsize=28,pad=26)
  for x,y in enumerate(vals):a.text(x,y+.22,str(y),ha="center",fontsize=28,color=green)
  a.text(.12,1.32,"NDE=1",fontsize=25,color=purple);a.text(1.13,4.60,f"NIE={vals[2]-1}",fontsize=25,color=green)
 title="One shared intermediate outcome gives a compatible decomposition"
 footer="M(a)=a. States are Y(0,0), Y(1,0), Y(1,1), not times on a trajectory.\nAdditive: 3−0=(1−0)+(3−1). Interaction: 4−0=(1−0)+(4−1).\nThe middle term cancels without a no-interaction assumption."
elif name=="interaction-reference-paths":
 fig,axs=plt.subplots(1,2,figsize=(1260/72,1060/72),facecolor=bg);fig.subplots_adjust(left=.075,right=.95,bottom=.30,top=.76,wspace=.40)
 for col,a in enumerate(axs):
  style(a);a.set(xlim=(-.3,1.85),ylim=(-.4,1.65),xticks=[0,1],yticks=[0,1],xlabel="Treatment A",ylabel="Mediator M");a.set_aspect("equal");a.set_title(["Treatment first","Mediator first"][col],fontsize=28,pad=25)
  for aa in [0,1]:
   for m in [0,1]:a.scatter(aa,m,s=130,color=blue,zorder=5);a.text(aa+.06,m+.14,f"Y={aa+2*m+aa*m}",fontsize=27,color=blue)
  route=[[(.12,0),(.88,0),purple],[(1,.12),(1,.88),green]] if col==0 else [[(0,.12),(0,.88),green],[(.12,1),(.88,1),purple]]
  for start,end,c in route:a.annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":"->","color":c,"lw":3,"mutation_scale":15})
  if col==0:a.text(.18,-.28,"NDE=1",fontsize=25,color=purple);a.text(1.12,.46,"NIE=3",fontsize=25,color=green)
  else:a.text(.12,.46,"IE at A=0: 2",fontsize=25,color=green);a.text(.06,1.44,"DE at M=1: 2",fontsize=25,color=purple)
 title="Interaction changes reference-specific effects, not total difference"
 footer="Y(a,m)=a+2m+am gives Y(0,0)=0, Y(1,0)=1, Y(0,1)=2, Y(1,1)=4.\nThe two compatible paths yield 1+3=4 and 2+2=4.\nDo not combine direct and indirect terms from mismatched paths."
elif name=="natural-support-and-hybrid":
 fig,a=plt.subplots(figsize=(520/72,980/72),facecolor=bg);fig.subplots_adjust(left=.18,right=.92,bottom=.32,top=.76);style(a);a.set(xlim=(-.3,1.85),ylim=(-.4,1.7),xticks=[0,1],yticks=[0,1],xlabel="Treatment A",ylabel="Mediator M");a.set_aspect("equal")
 a.scatter([0,1],[0,1],s=140,color=green,zorder=5);a.scatter([1],[0],s=160,color=red,marker="x",zorder=5);a.text(.08,.18,"Natural",color=green,fontsize=27);a.text(.23,1.25,"Natural",color=green,fontsize=27);a.text(1.10,.13,"Hybrid",color=red,fontsize=27)
 title="Natural support and\na computable hybrid"
 footer="Toy relation M(a)=a, A binary.\nNatural states: (0,0), (1,1).\nHybrid (1,0) has no support.\nKnown Y(1,0) is still computable;\nthis is not an observed manifold."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.95,linespacing=1.35);fig.text(.5,.04,footer,ha="center",fontsize=24 if name=="natural-support-and-hybrid" else 25,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)

