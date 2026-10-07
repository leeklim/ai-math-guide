"""Exact random-projection laws and finite deterministic diagrams; no model run."""
import argparse,math,itertools
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-rmt-02-projection","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect=(.22,.31,.66,.4)):
 ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def main(output):
 key=output.stem.removeprefix("A09-RMT-02-");fig=plt.figure(figsize=(520/72,1040/72),facecolor=BG)
 if key=="fixed-vector-norm-ratio":
  ax=axes(fig);t=np.linspace(.001,2.5,1000)
  for m,col,style in [(10,BLUE,"-"),(50,PURPLE,"--"),(200,GREEN,":")]:
   a=m/2;f=np.exp(a*np.log(m/2)+(a-1)*np.log(t)-m*t/2-math.lgamma(a));ax.plot(t,f,color=col,ls=style,lw=3)
  ax.axvline(1,color=GRAY,lw=1.4);ax.set(xlim=(0,2.3),ylim=(0,4.5),xlabel="Squared norm ratio T",ylabel="Exact projection density");ax.set_xticks([0,1,2]);ax.set_yticks([0,2,4]);fig.text(.077,.95,"One fixed v; random draws of R",fontsize=27)
  for y,m,col,sty in [(.88,10,BLUE,"—"),(.82,50,PURPLE,"- -"),(.76,200,GREEN,"···")]:fig.text(.077,y,f"Target dimension m = {m}  {sty}",fontsize=25,color=col)
  fig.text(.077,.20,"T = ‖Rv‖² / ‖v‖²",fontsize=28);fig.text(.077,.13,"E T = 1; Var T = 2 / m",fontsize=27);fig.text(.077,.06,"m counts output coordinates.",fontsize=25,color=GRAY)
 elif key=="squared-versus-distance-distortion":
  ax=axes(fig,(.31,.31,.57,.40))
  for y,a,b,col in [(1,.8,1.2,PURPLE),(0,np.sqrt(.8),np.sqrt(1.2),GREEN)]:
   ax.plot([a,b],[y,y],color=col,lw=5);ax.plot([a,a],[y-.08,y+.08],color=col,lw=2);ax.plot([b,b],[y-.08,y+.08],color=col,lw=2)
  ax.axvline(1,color=GRAY,lw=1.3,ls="--");ax.set(xlim=(.7,1.3),ylim=(-.5,1.5),xlabel="Output / input ratio");ax.set_xticks([.8,1,1.2]);ax.set_yticks([0,1],["Distance","Squared"])
  fig.text(.077,.95,"Same ε; two different ratio bounds",fontsize=24);fig.text(.077,.87,"ε = 0.2 on squared distances",fontsize=26);fig.text(.077,.79,"Purple: squared; green: distance",fontsize=24);fig.text(.077,.20,"Squared ratio: [0.8, 1.2]",fontsize=26);fig.text(.077,.13,"Distance ratio: [0.894, 1.095]",fontsize=25);fig.text(.077,.06,"Take square roots before comparing.",fontsize=23,color=GRAY)
 elif key=="all-pairs-one-embedding":
  ax=axes(fig);pts=np.array([[0,0],[1,0],[0,1],[1,1]])
  for i,j in itertools.combinations(range(4),2):ax.plot(pts[[i,j],0],pts[[i,j],1],color=GRAY,ls="--" if {i,j} in [{0,3},{1,2}] else "-",lw=2)
  ax.scatter(pts[:,0],pts[:,1],color=BLUE,s=80,zorder=4)
  for (x,y),name,dx,dy in zip(pts,["A","B","C","D"],[-.13,.09,-.13,.09],[-.12,-.12,.08,.08]):ax.text(x+dx,y+dy,name,color=BLUE,fontsize=28)
  ax.set(xlim=(-.25,1.25),ylim=(-.25,1.25),xlabel="Input coordinate 1",ylabel="Input coordinate 2");ax.set_aspect("equal");ax.set_xticks([0,1]);ax.set_yticks([0,1]);fig.text(.077,.95,"One fixed set; one shared R",fontsize=28);fig.text(.077,.87,"n = 4 points → 6 pair comparisons",fontsize=25);fig.text(.077,.79,"Every line is a distance to preserve.",fontsize=24);fig.text(.077,.20,"Failure = at least one failed pair",fontsize=25);fig.text(.077,.13,"P(any failure) ≤ sum of pair risks",fontsize=24);fig.text(.077,.06,"Pair events need not be independent.",fontsize=23,color=GRAY)
 elif key=="point-count-log-term":
  ax=axes(fig);n=np.geomspace(100,10000,300);ax.plot(n,np.log(n)/np.log(100),color=PURPLE,lw=3);ax.scatter([100,10000],[1,2],color=PURPLE,s=65,zorder=4);ax.set_xscale("log");ax.set(xlim=(80,13000),ylim=(.8,2.2),xlabel="Point count n (log scale)",ylabel="log n / log 100");ax.set_xticks([100,1000,10000],["100","1000","10⁴"]);ax.set_xticks([],minor=True);ax.set_yticks([1,1.5,2]);fig.text(.077,.95,"A hundred times more points",fontsize=27);fig.text(.077,.87,"log(10,000) / log(100) = 2",fontsize=26,color=PURPLE);fig.text(.077,.79,"Same ε and failure budget",fontsize=27);fig.text(.077,.20,"The log n term doubles.",fontsize=28);fig.text(.077,.13,"This is one term, not the minimum m.",fontsize=23);fig.text(.077,.06,"Sufficient dimension has constants.",fontsize=24,color=GRAY)
 elif key=="distortion-inverse-square":
  ax=axes(fig);eps=np.linspace(.1,.4,300);q=(.2/eps)**2;ax.plot(eps,q,color=GREEN,lw=3);ax.scatter([.1,.2,.4],[4,1,.25],color=GREEN,s=70,zorder=4);ax.set(xlim=(.08,.42),ylim=(0,4.4),xlabel="Distortion allowance ε",ylabel="Normalized ε⁻² term");ax.set_xticks([.1,.2,.4]);ax.set_yticks([0,1,4]);fig.text(.077,.95,"Half ε needs four times the order",fontsize=24);fig.text(.077,.87,"ε = 0.2 is the reference value.",fontsize=26);fig.text(.077,.79,"Relative term: (0.2 / ε)²",fontsize=28,color=GREEN);fig.text(.077,.20,"0.2 → 0.1: term 1 → 4",fontsize=28);fig.text(.077,.13,"Hold n and failure budget fixed.",fontsize=25);fig.text(.077,.06,"An order ratio, not exact dimensions",fontsize=23,color=GRAY)
 elif key=="failure-probability-log-term":
  ax=axes(fig);delta=np.geomspace(.0005,.2,300);v=np.log(1/delta)/np.log(20);ax.plot(delta,v,color=AMBER,lw=3);ax.scatter([.0005,.005,.05],np.log(1/np.array([.0005,.005,.05]))/np.log(20),color=AMBER,s=60,zorder=4);ax.set_xscale("log");ax.set(xlim=(.0004,.25),ylim=(0,2.8),xlabel="Allowed failure δ (log scale)",ylabel="log(1/δ) / log 20");ax.set_xticks([.0005,.005,.05],["0.0005","0.005","0.05"]);ax.set_xticks([],minor=True);ax.set_yticks([0,1,2]);fig.text(.077,.95,"Smaller failure budget, larger term",fontsize=24);fig.text(.077,.87,"Reference δ = 0.05",fontsize=28,color=AMBER);fig.text(.077,.79,"Hold n and ε fixed.",fontsize=28);fig.text(.077,.20,"Numerator: 2 log n + log(1/δ)",fontsize=24);fig.text(.077,.13,"Shown: only the second contribution",fontsize=23);fig.text(.077,.06,"Not a minimum-dimension estimate",fontsize=24,color=GRAY)
 elif key=="finite-set-and-null-direction":
  ax=axes(fig);ax.scatter([0,1,0],[0,0,1],s=80,color=BLUE,zorder=4);ax.scatter([0],[0],s=200,facecolors="none",edgecolors=AMBER,lw=2.5,zorder=5);ax.text(.08,.08,"A′ = D′",fontsize=26,color=AMBER);ax.text(.84,-.14,"B′",fontsize=28,color=BLUE);ax.text(-.17,.88,"C′",fontsize=28,color=BLUE);ax.plot([0,1,0,0],[0,0,1,0],color=GRAY,lw=1.8,ls="--");ax.set(xlim=(-.25,1.25),ylim=(-.25,1.25),xlabel="Output z₁",ylabel="Output z₂");ax.set_aspect("equal");ax.set_xticks([0,1]);ax.set_yticks([0,1]);fig.text(.077,.95,"R(x₁, x₂, x₃) = (x₁, x₂)",fontsize=27);fig.text(.077,.88,"A = (0,0,0); B = (1,0,0)",fontsize=26);fig.text(.077,.81,"C = (0,1,0); D = (0,0,1)",fontsize=26);fig.text(.077,.20,"A, B, C: all distances preserved",fontsize=25);fig.text(.077,.13,"A → D input distance 1; output 0",fontsize=25,color=AMBER);fig.text(.077,.06,"Deterministic map; not a Gaussian draw",fontsize=22,color=GRAY)
 else:raise ValueError(key)
 output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(output,format="svg",metadata={"Date":None});plt.close(fig)
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
