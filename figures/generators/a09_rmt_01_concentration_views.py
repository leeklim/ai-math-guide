"""Exact Gaussian geometry and deterministic illustrations; no model experiment."""
import argparse, math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-rmt-01-concentration","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect=(.22,.31,.66,.40)):
 ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def arrow(ax,a,b,color):
 ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"-|>","lw":2.5,"color":color,"mutation_scale":10,"shrinkA":0,"shrinkB":0})
def main(output):
 key=output.stem.removeprefix("A09-RMT-01-");fig=plt.figure(figsize=(520/72,1040/72),facecolor=BG)
 if key=="squared-norm-density":
  ax=axes(fig);s=np.linspace(.001,2.1,1000)
  for d,color,style in [(50,BLUE,"-"),(200,PURPLE,"--"),(800,GREEN,":")]:
   a=d/2;f=np.exp(a*np.log(d/2)+(a-1)*np.log(s)-d*s/2-math.lgamma(a));ax.plot(s,f,color=color,ls=style,lw=3)
  ax.axvline(1,color=GRAY,lw=1.4);ax.set(xlim=(.4,1.7),ylim=(0,8.5),xlabel="Squared norm S",ylabel="Exact density");ax.set_xticks([.5,1,1.5]);ax.set_yticks([0,4,8])
  fig.text(.077,.95,"Same mean; narrower squared norm",fontsize=25)
  for y,d,sd,color,label in [(.88,50,.2,BLUE,"—"),(.82,200,.1,PURPLE,"- -"),(.76,800,.05,GREEN,"···")]:fig.text(.077,y,f"d = {d}: sd {sd:g}  {label}",fontsize=26,color=color)
  fig.text(.077,.20,"S = sum of independent xᵢ²",fontsize=27);fig.text(.077,.13,"E S = 1; Var S = 2 / d",fontsize=27);fig.text(.077,.06,"These are not norm-density curves.",fontsize=24,color=GRAY)
 elif key=="fixed-tolerance-tail-bound":
  ax=axes(fig);d=np.linspace(50,800,400);b=np.minimum(1,2/(d*.2**2));ax.plot(d,b,color=AMBER,lw=3);ax.scatter([50,200,800],[1,.25,.0625],color=AMBER,s=65,zorder=4);ax.set(xlim=(30,850),ylim=(0,1.1),xlabel="Dimension d",ylabel="Upper probability limit");ax.set_xticks([50,200,800]);ax.set_yticks([0,.5,1])
  fig.text(.077,.95,"A fixed tolerance, not a fixed draw",fontsize=24);fig.text(.077,.87,"Event: |S − 1| ≥ 0.2",fontsize=28,color=AMBER);fig.text(.077,.79,"Bound: min(1, 50 / d)",fontsize=28)
  fig.text(.077,.20,"d = 200: probability ≤ 0.25",fontsize=27);fig.text(.077,.13,"d = 800: probability ≤ 0.0625",fontsize=25);fig.text(.077,.06,"The curve is not an observed rate.",fontsize=24,color=GRAY)
 elif key=="unit-direction-cosine-density":
  ax=axes(fig);t=np.linspace(-.995,.995,1000)
  for d,color,style in [(4,BLUE,"-"),(50,PURPLE,"--"),(200,GREEN,":")]:
   f=np.exp(math.lgamma(d/2)-.5*math.log(math.pi)-math.lgamma((d-1)/2)+(d-3)/2*np.log1p(-t*t));ax.plot(t,f,color=color,ls=style,lw=3)
  ax.set(xlim=(-1,1),ylim=(0,6),xlabel="Cosine c",ylabel="Exact direction density");ax.set_xticks([-1,0,1]);ax.set_yticks([0,3,6]);ax.axvline(0,color=GRAY,lw=1.4)
  fig.text(.077,.95,"Independent unit directions",fontsize=28)
  for y,d,color,label in [(.88,4,BLUE,"—"),(.82,50,PURPLE,"- -"),(.76,200,GREEN,"···")]:fig.text(.077,y,f"d = {d}  {label}",fontsize=28,color=color)
  fig.text(.077,.20,"E c = 0; E c² = 1 / d",fontsize=28);fig.text(.077,.13,"Unit norm after normalization",fontsize=25);fig.text(.077,.06,"Near zero does not mean exact zero.",fontsize=23,color=GRAY)
 elif key=="dimension-dependent-scales":
  ax=axes(fig);d=np.geomspace(50,800,200);ax.plot(d,np.sqrt(2/d),color=PURPLE,lw=3);ax.plot(d,1/np.sqrt(d),"--",color=GREEN,lw=3);ax.scatter([200,800],[.1,.05],color=PURPLE,s=55,zorder=4);ax.scatter([200,800],[1/np.sqrt(200),1/np.sqrt(800)],color=GREEN,s=55,zorder=4);ax.set_xscale("log");ax.set(xlim=(45,900),ylim=(0,.23),xlabel="Dimension d (log scale)",ylabel="Standard deviation");ax.set_xticks([50,200,800],["50","200","800"]);ax.set_xticks([],minor=True);ax.set_yticks([0,.1,.2])
  fig.text(.077,.95,"Different summaries; same scaling",fontsize=25);fig.text(.077,.87,"Squared norm: √(2 / d)  —",fontsize=28,color=PURPLE);fig.text(.077,.79,"Inner product: 1 / √d  - -",fontsize=28,color=GREEN);fig.text(.077,.20,"d = 200: 0.1 versus ≈ 0.071",fontsize=26);fig.text(.077,.13,"Four times d halves both scales.",fontsize=25);fig.text(.077,.06,"Neither value is an angle in degrees.",fontsize=23,color=GRAY)
 elif key=="same-radius-different-directions":
  ax=axes(fig,(.20,.30,.70,.40));a=np.linspace(0,2*np.pi,361);ax.plot(np.cos(a),np.sin(a),color=GRAY,lw=1.4);u=np.arange(12)*2*np.pi/12;v=np.linspace(.13,.35,5);ax.scatter(np.cos(u),np.sin(u),s=70,facecolors="none",edgecolors=BLUE,lw=2,zorder=3);ax.scatter(np.cos(v),np.sin(v),s=100,color=GREEN,marker="+",lw=2.5,zorder=4);ax.set(xlim=(-1.3,1.3),ylim=(-1.3,1.3),xlabel="Coordinate 1",ylabel="Coordinate 2");ax.set_aspect("equal");ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
  fig.text(.077,.95,"Same radius, different directions",fontsize=25);fig.text(.077,.87,"Blue ○: twelve spaced directions",fontsize=25,color=BLUE);fig.text(.077,.79,"Green +: one short arc",fontsize=27,color=GREEN);fig.text(.077,.20,"Every point has norm 1.",fontsize=28);fig.text(.077,.13,"Radius alone does not specify clusters.",fontsize=23);fig.text(.077,.06,"Deterministic 2D illustration",fontsize=25,color=GRAY)
 elif key=="unit-radii-pair-distance":
  ax=axes(fig,(.22,.31,.66,.40));arrow(ax,(0,0),(1,0),BLUE);arrow(ax,(0,0),(0,1),GREEN);ax.plot([1,0],[0,1],"--",color=PURPLE,lw=2.5);ax.text(.65,.57,"√2",color=PURPLE,fontsize=28);ax.text(.75,-.17,"x",color=BLUE,fontsize=28);ax.text(-.17,.72,"y",color=GREEN,fontsize=28);ax.set(xlim=(-.25,1.25),ylim=(-.25,1.25),xlabel="Coordinate 1",ylabel="Coordinate 2");ax.set_aspect("equal");ax.set_xticks([0,1]);ax.set_yticks([0,1])
  fig.text(.077,.95,"Two unit radii; nonzero separation",fontsize=24);fig.text(.077,.87,"x = (1, 0); y = (0, 1)",fontsize=28);fig.text(.077,.79,"xᵀy = 0 in this exact example",fontsize=25);fig.text(.077,.20,"‖x − y‖² = 1 + 1 − 0 = 2",fontsize=26);fig.text(.077,.13,"Pair distance: √2, not zero",fontsize=26);fig.text(.077,.06,"A geometric relation, not a sample",fontsize=24,color=GRAY)
 elif key=="equal-trace-anisotropic-geometry":
  ax=axes(fig,(.22,.31,.66,.40));t=np.linspace(0,2*np.pi,361);ax.plot(np.cos(t),np.sin(t),"--",color=BLUE,lw=2.5);ax.plot(np.sqrt(200/101)*np.cos(t),np.sqrt(2/101)*np.sin(t),color=GREEN,lw=3);ax.set(xlim=(-1.6,1.6),ylim=(-1.6,1.6),xlabel="Coordinate 1",ylabel="Coordinate 2");ax.set_aspect("equal");ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
  fig.text(.077,.95,"Equal trace; different directions",fontsize=25);fig.text(.077,.87,"Isotropic covariance I₂  - -",fontsize=27,color=BLUE);fig.text(.077,.79,"Anisotropic variance ratio 100  —",fontsize=24,color=GREEN);fig.text(.077,.20,"Trace = total variance = 2",fontsize=27);fig.text(.077,.13,"Ellipse: diag(200/101, 2/101)",fontsize=25);fig.text(.077,.06,"Covariance geometry, not drawn data",fontsize=24,color=GRAY)
 else:raise ValueError(key)
 output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(output,format="svg",metadata={"Date":None});plt.close(fig)
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
