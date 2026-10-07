"""Small reproducible covariance examples, independent of model/lab results."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-rmt-03-covariance","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect=(.22,.31,.66,.4)):
 ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def samples():
 out=[]
 for d in [20,200]:
  x=np.random.default_rng(4100+d).normal(size=(400,d));xc=x-x.mean(axis=0);s=xc.T@xc/400;ev=np.linalg.eigvalsh(s);mask=~np.eye(d,dtype=bool);rms=np.sqrt(np.mean(s[mask]**2));out.append((d,ev,rms))
 return out
def main(output):
 key=output.stem.removeprefix("A09-RMT-03-");wide=key in ["sample-mean-centering","feature-and-sample-gram-spectra"];w,h=(1060,790) if wide else (520,1040);fig=plt.figure(figsize=(w/72,h/72),facecolor=BG)
 if key=="sample-mean-centering":
  x=np.array([[2,1],[4,1],[3,4]]);xc=x-x.mean(axis=0)
  for xx,rect,title,limits,mean in [(x,(.09,.25,.35,.46),"Original X",((1,5),(0,5)),(3,2)),(xc,(.60,.25,.35,.46),"Centered Xc",((-2,2),(-2,3)),(0,0))]:
   ax=axes(fig,rect);ax.scatter(xx[:,0],xx[:,1],s=85,color=BLUE,zorder=4)
   for (a,b),lab in zip(xx,["P₁","P₂","P₃"]):ax.text(a+.10,b+.15,lab,color=BLUE,fontsize=26)
   ax.scatter(*mean,s=180,color=AMBER,marker="+",lw=2.5,zorder=5);ax.axhline(0,color=GRAY,lw=1.1);ax.axvline(0,color=GRAY,lw=1.1);ax.set(xlim=limits[0],ylim=limits[1],xlabel="Feature 1",ylabel="Feature 2");ax.set_xticks([2,3,4] if title=="Original X" else [-1,0,1]);ax.set_yticks([1,2,4] if title=="Original X" else [-1,0,2]);ax.set_title(title,fontsize=28,pad=25)
  fig.text(.045,.94,"Subtract the sample mean (3, 2) from every row",fontsize=30);fig.text(.045,.84,"Same three rows; orange + is the sample mean",fontsize=28,color=AMBER);fig.text(.045,.10,"Xc rows: (−1,−1), (1,−1), (0,2); each column sums to 0.",fontsize=28)
 elif key=="unit-direction-variance":
  ax=axes(fig);theta=np.linspace(0,180,361);r=np.deg2rad(theta);var=2/3*np.cos(r)**2+2*np.sin(r)**2;ax.plot(theta,var,color=PURPLE,lw=3);ax.scatter([0,90,180],[2/3,2,2/3],color=PURPLE,s=65,zorder=4);ax.set(xlim=(-8,188),ylim=(0,2.3),xlabel="Direction angle θ (degrees)",ylabel="Sample variance vᵀSv");ax.set_xticks([0,90,180]);ax.set_yticks([0,1,2])
  fig.text(.077,.95,"One covariance; many unit directions",fontsize=24);fig.text(.077,.87,"S = diag(2/3, 2)",fontsize=28,color=PURPLE);fig.text(.077,.79,"v = (cos θ, sin θ); ‖v‖ = 1",fontsize=26);fig.text(.077,.20,"0° / 180°: variance 2/3",fontsize=27);fig.text(.077,.13,"90°: variance 2",fontsize=28);fig.text(.077,.06,"A squared projection average ≥ 0",fontsize=24,color=GRAY)
 elif key=="denominator-eigenvalue-rescaling":
  ax=axes(fig);ax.plot([1,2],[2/3,2],color=BLUE,lw=2.5,marker="o",ms=8);ax.plot([1,2],[1,3],"--",color=GREEN,lw=2.5,marker="s",ms=8);ax.set(xlim=(.75,2.25),ylim=(0,3.4),xlabel="Same feature directions",ylabel="Sample eigenvalue");ax.set_xticks([1,2],["e₁","e₂"]);ax.set_yticks([0,1,2,3]);fig.text(.077,.95,"Change denominator, not direction",fontsize=25);fig.text(.077,.87,"Blue ○: divide by n = 3  —",fontsize=27,color=BLUE);fig.text(.077,.79,"Green □: divide by n−1 = 2  - -",fontsize=25,color=GREEN);fig.text(.077,.20,"Eigenvalue ratio: 3 / 2 = 1.5",fontsize=26);fig.text(.077,.13,"2/3 → 1 and 2 → 3",fontsize=28);fig.text(.077,.06,"Same eigenvectors, rescaled spectrum",fontsize=23,color=GRAY)
 elif key=="feature-and-sample-gram-spectra":
  x=np.random.default_rng(403100).normal(size=(40,100));xc=x-x.mean(axis=0);s=np.linalg.svd(xc,compute_uv=False);positive=np.sort(s[s>1e-10]**2/40);assert positive.size==39
  for zeros,count,rect,title,col in [(61,100,(.10,.28,.35,.43),"Feature S: 100×100",BLUE),(1,40,(.61,.28,.35,.43),"Sample Gram: 40×40",PURPLE)]:
   ev=np.r_[np.zeros(zeros),positive];ax=axes(fig,rect);ax.scatter(np.arange(1,count+1),ev,s=25,color=col,zorder=4);ax.axhline(0,color=GRAY,lw=1);ax.set(xlim=(0,count+2),ylim=(-.25,max(7,float(np.ceil(positive.max())+.5))),xlabel="Sorted eigenvalue index",ylabel="Eigenvalue");ax.set_xticks(sorted({1,zeros,count}));ax.set_yticks([0,3,6]);ax.set_title(title,fontsize=27,pad=25);fig.text(rect[0],.15,f"{zeros} "+("zero" if zeros==1 else "zeros")+"; 39 positive",fontsize=27,color=col)
  fig.text(.045,.94,"Same nonzero values; different zero counts and spaces",fontsize=28);fig.text(.045,.84,"Illustrative iid Gaussian X, then centered: Xc (40 × 100)",fontsize=28);fig.text(.045,.07,"Population covariance I₁₀₀ is full rank despite sample zeros.",fontsize=28,color=GRAY)
 elif key=="aspect-ratio-sample-spread":
  ax=axes(fig)
  for d,ev,rms in samples():ax.plot(np.linspace(0,1,d),ev,color=BLUE if d==20 else PURPLE,ls="-" if d==20 else "--",lw=2.5,marker="o" if d==20 else None,ms=4)
  ax.axhline(1,color=AMBER,ls=":",lw=2);ax.set(xlim=(-.02,1.02),ylim=(0,3.2),xlabel="Sorted order fraction",ylabel="Sample eigenvalue");ax.set_xticks([0,.5,1]);ax.set_yticks([0,1,2,3]);fig.text(.077,.95,"Identity population; sample spread",fontsize=25);fig.text(.077,.87,"d = 20, n = 400: γ = 0.05  —",fontsize=25,color=BLUE);fig.text(.077,.79,"d = 200, n = 400: γ = 0.5  - -",fontsize=25,color=PURPLE);fig.text(.077,.20,"Orange ···: population eigenvalue 1",fontsize=23,color=AMBER);fig.text(.077,.13,"Two reproducible illustrative samples",fontsize=23);fig.text(.077,.06,"Not an asymptotic-law proof",fontsize=25,color=GRAY)
 elif key=="entrywise-versus-directional-error":
  vals=samples();ax=axes(fig)
  ax.bar(np.array([0,1])-.17,[rms for d,ev,rms in vals],width=.28,color=BLUE);ax.bar(np.array([0,1])+.17,[ev.max()-1 for d,ev,rms in vals],width=.28,color=PURPLE,hatch="//",edgecolor="#3B136F");ax.set(xlim=(-.5,1.5),ylim=(0,2.2),xlabel="Dimension (n = 400 fixed)",ylabel="Error-summary magnitude");ax.set_xticks([0,1],["d = 20","d = 200"]);ax.set_yticks([0,1,2]);fig.text(.077,.95,"Entry noise and spectral distortion",fontsize=24);fig.text(.077,.87,"Blue: RMS off-diagonal entries",fontsize=25,color=BLUE);fig.text(.077,.79,"Purple //: largest eigenvalue − 1",fontsize=24,color=PURPLE);fig.text(.077,.20,"Same samples as the spectrum plot",fontsize=24);fig.text(.077,.13,"Different summaries of covariance error",fontsize=23);fig.text(.077,.06,"Finite illustration, not a uniform bound",fontsize=22,color=GRAY)
 else:raise ValueError(key)
 output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(output,format="svg",metadata={"Date":None});plt.close(fig)
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
