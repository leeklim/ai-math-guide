"""Exact small linear maps, covariance geometry, and quadratic losses; no model/eigensolver run."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-rmt-07-spectra","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect=(.22,.31,.66,.4)):
 ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def arrow(ax,end,color):
 ax.annotate("",xy=end,xytext=(0,0),arrowprops={"arrowstyle":"->","color":color,"lw":2.5,"mutation_scale":11,"shrinkA":0,"shrinkB":0})
def contour(ax,covariance,color):
 eig,basis=np.linalg.eigh(covariance);theta=np.linspace(0,2*np.pi,361);points=basis@np.diag(np.sqrt(eig))@np.array([np.cos(theta),np.sin(theta)]);ax.plot(points[0],points[1],color=color,lw=3);major=basis[:,-1]*np.sqrt(eig[-1]);ax.plot([-major[0],major[0]],[-major[1],major[1]],color=color,lw=2,ls="--")
def main(output):
 key=output.stem.removeprefix("A09-RMT-07-");wide=key in ["weight-map-circle-to-ellipse","zero-spectral-radius-nonzero-amplification"];tall=key in ["input-output-gram-zero-counts","activation-values-and-directional-variance","feature-standardization-rotates-axes"];w,h=(1200,820) if wide else (520,1400) if tall else (520,1040);fig=plt.figure(figsize=(w/72,h/72),facecolor=BG)
 if key=="weight-map-circle-to-ellipse":
  theta=np.linspace(0,2*np.pi,361)
  for i,(sx,sy,title,xlabel,ylabel,lim,col) in enumerate([(1,1,"Unit input circle","Input x₁","Input x₂",1.5,BLUE),(3,1,"Output plane y₃ = 0","Output y₁","Output y₂",3.7,GREEN)]):
   ax=axes(fig,(.10+i*.52,.29,.31,.42));ax.plot(sx*np.cos(theta),sy*np.sin(theta),color=col,lw=3);arrow(ax,(sx,0),col);arrow(ax,(0,sy),PURPLE);ax.set(xlim=(-lim,lim),ylim=(-lim,lim),xlabel=xlabel,ylabel=ylabel);ax.set_aspect("equal");ax.set_xticks([-1,0,1] if i==0 else [-3,0,3]);ax.set_yticks([-1,0,1] if i==0 else [-3,0,3]);ax.set_title(title,fontsize=28,pad=27)
  fig.text(.04,.94,"W = [[3,0],[0,1],[0,0]] maps between different index spaces.",fontsize=28);fig.text(.04,.83,"Input unit directions → output lengths s₁ = 3 and s₂ = 1",fontsize=29);fig.text(.04,.14,"Singular values measure linear-map length amplification.",fontsize=29);fig.text(.04,.07,"Not an activation sample covariance or parameter curvature",fontsize=28,color=GRAY)
 elif key=="input-output-gram-zero-counts":
  for rect,values,label,title,col in [((.22,.65,.66,.16),[9,1],"Input Gram index","WᵀW: 2×2",BLUE),((.22,.28,.66,.16),[9,1,0],"Output Gram index","WWᵀ: 3×3",GREEN)]:
   ax=axes(fig,rect);ax.bar(np.arange(1,len(values)+1),values,color=col,edgecolor=GRAY,hatch="//");ax.scatter(np.arange(1,len(values)+1),values,color=col,s=55,zorder=5);ax.set(xlim=(.4,len(values)+.6),ylim=(-.4,10.2),xlabel=label,ylabel="Eigenvalue s²");ax.set_xticks(np.arange(1,len(values)+1));ax.set_yticks([0,9]);ax.set_title(title,fontsize=28,pad=25)
  fig.text(.077,.96,"Same nonzero values; extra zero",fontsize=25);fig.text(.077,.90,"W is 3×2; singular values 3, 1",fontsize=25);fig.text(.077,.51,"Nonzero eigenvalues: 9 and 1",fontsize=26);fig.text(.077,.15,"Different shape and coordinate spaces",fontsize=22);fig.text(.077,.095,"No sample interpretation or 1/n factor",fontsize=22);fig.text(.077,.04,"Zero marks the unused output direction.",fontsize=22,color=GRAY)
 elif key=="zero-spectral-radius-nonzero-amplification":
  theta=np.linspace(0,2*np.pi,361)
  for i,title in enumerate(["Unit input circle","Output image: a segment"]):
   ax=axes(fig,(.10+i*.52,.29,.31,.42));ax.set(xlim=(-3.5,3.5) if i else (-1.5,1.5),ylim=(-3.5,3.5) if i else (-1.5,1.5),xlabel="Output y₁" if i else "Input x₁",ylabel="Output y₂" if i else "Input x₂");ax.set_aspect("equal");ax.set_xticks([-3,0,3] if i else [-1,0,1]);ax.set_yticks([-3,0,3] if i else [-1,0,1]);ax.set_title(title,fontsize=27,pad=27)
   if i:ax.plot(3*np.sin(theta),np.zeros_like(theta),color=GREEN,lw=4);arrow(ax,(3,0),AMBER)
   else:ax.plot(np.cos(theta),np.sin(theta),color=BLUE,lw=3);arrow(ax,(0,1),AMBER)
  fig.text(.04,.94,"W = [[0,3],[0,0]]: zero eigenvalues, nonzero amplification",fontsize=28);fig.text(.04,.83,"Highlighted v = (0,1)ᵀ → Wv = (3,0)ᵀ",fontsize=29,color=AMBER);fig.text(.04,.14,"Spectral radius ρ(W) = 0; largest singular value = 3",fontsize=29);fig.text(.04,.07,"Eigenvalue size does not bound every input-direction gain.",fontsize=28,color=GRAY)
 elif key=="compensated-layer-rescaling":
  before=np.array([3,1,3]);after=np.array([6,.5,3]);ax=axes(fig);x=np.arange(3);ax.bar(x-.17,before,width=.34,color=BLUE,edgecolor=GRAY);ax.bar(x+.17,after,width=.34,color=GREEN,edgecolor=GRAY,hatch="//");ax.set(xlim=(-.6,2.6),ylim=(0,6.7),xlabel="Linear map",ylabel="Largest singular value");ax.set_xticks(x,["W₁","W₂","W₂W₁"]);ax.set_yticks([0,3,6]);fig.text(.077,.95,"Rescale layers; keep their product.",fontsize=23);fig.text(.077,.87,"W₁ = diag(3,1); W₂ = I₂",fontsize=27);fig.text(.077,.79,"Blue: before; green: after",fontsize=26);fig.text(.077,.20,"After: W₁′ = 2W₁; W₂′ = W₂/2",fontsize=24);fig.text(.077,.13,"W₂′W₁′ = W₂W₁",fontsize=28);fig.text(.077,.06,"Exact two-linear-layer example",fontsize=24,color=GRAY)
 elif key=="activation-values-and-directional-variance":
  points=np.array([[-1,-1],[1,-1],[0,2]]);ax=axes(fig,(.22,.58,.66,.24));ax.scatter(points[:,0],points[:,1],color=BLUE,s=70,zorder=5);ax.set(xlim=(-1.5,1.5),ylim=(-1.5,2.5),xlabel="Hidden feature h₁",ylabel="Hidden feature h₂");ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,2]);ax.set_aspect("equal");ax.set_title("Three centered observations",fontsize=24,pad=25)
  ax=axes(fig,(.22,.26,.66,.18));ax.scatter([1,2,3],points[:,1],color=PURPLE,s=85,zorder=5);ax.axhline(0,color=GRAY,lw=1.5);ax.set(xlim=(.5,3.5),ylim=(-1.5,2.5),xlabel="Observation index",ylabel="Projection H_cv");ax.set_xticks([1,2,3]);ax.set_yticks([-1,0,2]);ax.set_title("Direction v = e₂",fontsize=27,pad=25);fig.text(.077,.96,"Variance averages observed squares.",fontsize=23);fig.text(.077,.90,"n = 3; fixed hidden observations",fontsize=24);fig.text(.077,.14,"vᵀC_hv = ((−1)² + (−1)² + 2²)/3",fontsize=22);fig.text(.077,.09,"= 6/3 = 2",fontsize=28,color=PURPLE);fig.text(.077,.04,"Observed variance, not arbitrary gain",fontsize=22,color=GRAY)
 elif key=="feature-standardization-rotates-axes":
  raw=np.array([[9,2],[2,1]]);scaled=np.diag([1/3,1])@raw@np.diag([1/3,1])
  for rect,cov,title,limit,col in [((.22,.62,.66,.22),raw,"Raw covariance",3.7,BLUE),((.22,.27,.66,.22),scaled,"Standardized covariance",1.8,GREEN)]:
   ax=axes(fig,rect);contour(ax,cov,col);ax.set(xlim=(-limit,limit),ylim=(-limit,limit),xlabel="Feature coordinate 1",ylabel="Feature coordinate 2");ax.set_aspect("equal");ax.set_xticks([-3,0,3] if col==BLUE else [-1,0,1]);ax.set_yticks([-3,0,3] if col==BLUE else [-1,0,1]);ax.set_title(title,fontsize=27,pad=25)
  fig.text(.077,.96,"Feature-wise scale can rotate axes.",fontsize=24);fig.text(.077,.90,"Divide feature scales by 3 and 1",fontsize=25);fig.text(.077,.15,"Dashed major direction changes.",fontsize=25);fig.text(.077,.095,"Geometry: xᵀC⁻¹x = 1",fontsize=27);fig.text(.077,.04,"Not an observed density contour",fontsize=24,color=GRAY)
 elif key=="stationary-loss-curvature-signs":
  t=np.linspace(-1.2,1.2,361);ax=axes(fig)
  for eig,col,style in [(2,GREEN,"-"),(0,GRAY,"--"),(-1,PURPLE,":")]:ax.plot(t,eig*t*t/2,color=col,ls=style,lw=3)
  ax.set(xlim=(-1.2,1.2),ylim=(-.9,1.6),xlabel="Parameter perturbation t",ylabel="Loss change ΔL");ax.set_xticks([-1,0,1]);ax.set_yticks([-.5,0,1]);fig.text(.077,.95,"Stationary point: gradient = 0",fontsize=25);fig.text(.077,.88,"λ = 2: positive curvature  —",fontsize=25,color=GREEN);fig.text(.077,.82,"λ = 0: quadratic term flat  - -",fontsize=24,color=GRAY);fig.text(.077,.76,"λ = −1: negative curvature  ···",fontsize=23,color=PURPLE);fig.text(.077,.20,"Directional ΔL = λt²/2",fontsize=28);fig.text(.077,.13,"Curvature is not feature variance.",fontsize=24);fig.text(.077,.06,"Exact quadratic examples",fontsize=26,color=GRAY)
 elif key=="constant-loss-curve-nonnull-tangent":
  t=np.linspace(-1.2,1.2,361);ax=axes(fig)
  for loss in [-.5,.5]:ax.plot(t,t*t+loss,color=GRAY,ls=":",lw=1.5)
  ax.plot(t,t*t,color=PURPLE,lw=3);arrow(ax,(1,0),BLUE);ax.scatter([0],[0],color=AMBER,s=70,zorder=5);ax.set(xlim=(-1.4,1.4),ylim=(-.55,1.7),xlabel="Parameter θ₁",ylabel="Parameter θ₂");ax.set_xticks([-1,0,1]);ax.set_yticks([0,1]);ax.set_aspect("equal");fig.text(.077,.95,"Constant loss along a curved path",fontsize=23);fig.text(.077,.87,"L(θ₁, θ₂) = θ₂ − θ₁²",fontsize=27);fig.text(.077,.79,"Purple: L = 0; blue: tangent e₁",fontsize=24);fig.text(.077,.20,"At origin: gradient = (0,1)ᵀ",fontsize=25);fig.text(.077,.13,"Hessian e₁ = −2e₁ ≠ 0",fontsize=28);fig.text(.077,.06,"Nonstationary; tangent not Hessian null",fontsize=22,color=GRAY)
 elif key=="coordinate-rescaling-changes-curvature":
  x=np.linspace(-1.1,1.1,361);ax=axes(fig);ax.plot(x,.5*x*x,color=BLUE,lw=3);ax.plot(x,2*x*x,color=GREEN,ls="--",lw=3);ax.set(xlim=(-1.1,1.1),ylim=(0,2.6),xlabel="Coordinate value: θ or η",ylabel="Loss value");ax.set_xticks([-1,0,1]);ax.set_yticks([0,1,2]);fig.text(.077,.95,"Same loss; different coordinate scale",fontsize=22);fig.text(.077,.88,"Blue L(θ) = θ²/2; Hessian 1",fontsize=25,color=BLUE);fig.text(.077,.80,"Green L(η) = 2η²; Hessian 4",fontsize=25,color=GREEN);fig.text(.077,.20,"Reparameterize θ = 2η.",fontsize=28);fig.text(.077,.13,"θ = 1 and η = 1 are not the same.",fontsize=23);fig.text(.077,.06,"Linear congruence: H_η = BᵀH_θB",fontsize=24,color=GRAY)
 elif key=="one-hvp-does-not-fix-the-spectrum":
  ax=axes(fig);ax.plot([1,2],[-4,2],color=BLUE,marker="o",ms=7,lw=2.5);ax.plot([1,2],[-4,10],color=GREEN,ls="--",marker="s",ms=7,lw=2.5);ax.axhline(0,color=GRAY,lw=1.5);ax.set(xlim=(.7,2.3),ylim=(-5,11),xlabel="Eigen-direction index",ylabel="Hessian eigenvalue");ax.set_xticks([1,2]);ax.set_yticks([-4,0,2,10]);fig.text(.077,.95,"One product does not fix all values.",fontsize=23);fig.text(.077,.87,"H₁ = diag(−4,2)  —",fontsize=27,color=BLUE);fig.text(.077,.79,"H₂ = diag(−4,10)  - -",fontsize=27,color=GREEN);fig.text(.077,.20,"Both H₁e₁ and H₂e₁ = −4e₁.",fontsize=25);fig.text(.077,.13,"Unqueried direction has 2 or 10.",fontsize=24);fig.text(.077,.06,"Exact matrices; no eigensolver run",fontsize=24,color=GRAY)
 elif key=="power-magnitude-versus-positive-eigenvalue":
  k=np.arange(0,7);neg=1/(1+4.**(-k));ax=axes(fig);ax.plot(k,neg,color=PURPLE,marker="o",ms=6,lw=3);ax.plot(k,1-neg,color=GREEN,ls="--",marker="s",ms=6,lw=3);ax.set(xlim=(-.3,6.3),ylim=(-.05,1.05),xlabel="Power k",ylabel="Squared direction fraction");ax.set_xticks([0,2,4,6]);ax.set_yticks([0,.5,1]);fig.text(.077,.95,"Power favors the negative axis.",fontsize=23);fig.text(.077,.88,"H = diag(−4,2); v₀ ∝ (1,1)ᵀ",fontsize=25);fig.text(.077,.81,"Purple: −4; green: +2",fontsize=27);fig.text(.077,.20,"Direction of Hᵏv₀ after normalization",fontsize=22);fig.text(.077,.13,"−4 fraction = 1/(1 + 4⁻ᵏ)",fontsize=27);fig.text(.077,.06,"Algebraic powers; not a solver run",fontsize=24,color=GRAY)
 else:raise ValueError(key)
 output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(output,format="svg",metadata={"Date":None});plt.close(fig)
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
