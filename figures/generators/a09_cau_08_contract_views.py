"""Illustrative coordinate/control/interaction contracts for CAU08; no model runs."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-CAU-08-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"cau08-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626"
def style(a):
 a.set_facecolor(bg);a.grid(color="#CBD5E1",alpha=.6);a.set_axisbelow(True);a.spines[["top","right"]].set_visible(False)
def arrow(a,xy,c):
 a.annotate("",xy=xy,xytext=(0,0),arrowprops={"arrowstyle":"->","color":c,"lw":3,"mutation_scale":14})
if name=="subspace-reconstruction-coordinate":
 fig,a=plt.subplots(figsize=(520/72,1040/72),facecolor=bg);fig.subplots_adjust(left=.19,right=.94,bottom=.34,top=.76);style(a);a.set_aspect("equal");a.set(xlim=(-1.65,2.5),ylim=(-.6,1.85),xticks=[-1,0,1,2],yticks=[0,1],xlabel="Patched coordinate",ylabel="Retained coordinate")
 a.axhline(0,color="#64748B",lw=1);a.axvline(0,color="#64748B",lw=1);a.axhline(1,color="#94A3B8",lw=2,ls="--")
 for xy,c in [((2,1),blue),((-1,1),red),((0,1),purple)]:arrow(a,xy,c)
 a.text(1.02,1.25,"h=(2,1)",color=blue,fontsize=26);a.text(-1.55,1.25,"h′=(−1,1)",color=red,fontsize=26);fig.text(.5,.715,"Kept component: (0,1)",ha="center",color=purple,fontsize=26)
 title="Replace one coefficient,\nreconstruct the full activation"
 footer="Illustrative coordinates only.\nPatched coefficient: 2 → −1.\nRetained coefficient: 1 → 1.\nReconstructed h′=(−1,1).\nThen rerun downstream.\nNo circuit effect was measured."
elif name=="same-norm-different-direction-control":
 fig,a=plt.subplots(figsize=(520/72,1080/72),facecolor=bg);fig.subplots_adjust(left=.19,right=.94,bottom=.36,top=.77);style(a);a.set_aspect("equal");a.set(xlim=(-1.25,1.35),ylim=(-1.2,1.65),xticks=[-1,0,1],yticks=[-1,0,1],xlabel="Coordinate 1",ylabel="Coordinate 2");a.axhline(0,color="#64748B",lw=1);a.axvline(0,color="#64748B",lw=1)
 t=np.linspace(0,2*np.pi,200);a.plot(np.cos(t),np.sin(t),color="#94A3B8",lw=2,ls="--");arrow(a,(1,0),blue);arrow(a,(.6,.8),red)
 a.text(.38,-.40,"(1,0)",color=blue,fontsize=27);a.text(.22,1.23,"(0.6,0.8)",color=red,fontsize=27)
 title="Equal norm leaves\ndirection unmatched"
 footer="Illustrative control directions.\nBoth norms equal 1.\nFix layer, position and dimension.\nNorm matching alone does not\nmatch every intervention property.\nNo effects are shown."
elif name=="joint-intervention-interaction-contrast":
 fig,a=plt.subplots(figsize=(1120/72,1030/72),facecolor=bg);fig.subplots_adjust(left=.10,right=.94,bottom=.29,top=.77);style(a);v=np.array([0,1,1,3]);x=np.arange(4);a.bar(x,v,width=.52,color=[blue,green,green,red],alpha=.75);a.set(xlim=(-.5,3.65),ylim=(-.10,3.85),xticks=x,xticklabels=["Y(0,0)","Y(1,0)","Y(0,1)","Y(1,1)"],yticks=[0,1,2,3],xlabel="Specified joint intervention",ylabel="Illustrative outcome")
 for k,z in enumerate(v):a.text(k,z+.16,str(z),ha="center",fontsize=29,color=red if k==3 else green)
 a.plot([2.65,3.40],[2,2],color=purple,lw=3,ls="--");a.text(.03,2.40,"Additive prediction: 2",color=purple,fontsize=28)
 title="The joint effect need not equal the sum of isolated effects"
 footer="Illustrative rule Y(a,b)=a+b+ab, not a measured model result.\nSingles above Y(0,0): 1+1=2; joint above Y(0,0): 3.\nInteraction: Y(1,1)−Y(1,0)−Y(0,1)+Y(0,0)=3−1−1+0=1."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.95,linespacing=1.35);fig.text(.5,.04,footer,ha="center",fontsize=24 if name!="joint-intervention-interaction-contrast" else 25,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)

