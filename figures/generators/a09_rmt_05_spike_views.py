"""Rank-one Gaussian covariance formula illustrations; no new experiment."""
import argparse,math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-rmt-05-spike","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect=(.22,.31,.66,.4)):
 ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def arrow(ax,end,color,style="-"):
 ax.annotate("",xy=end,xytext=(0,0),arrowprops={"arrowstyle":"->","color":color,"lw":2.5,"linestyle":style,"mutation_scale":11,"shrinkA":0,"shrinkB":0})
def leading(beta,gamma):
 result=np.full_like(beta,(1+np.sqrt(gamma))**2);above=beta>np.sqrt(gamma);result[above]=(1+beta[above])*(1+gamma/beta[above]);return result
def main(output):
 key=output.stem.removeprefix("A09-RMT-05-");wide=key=="spectral-gap-versus-alignment";w,h=(1200,820) if wide else (520,1040);fig=plt.figure(figsize=(w/72,h/72),facecolor=BG)
 if key=="rank-one-covariance-action":
  ax=axes(fig);ax.set(xlim=(-.3,3.8),ylim=(-.35,1.85),xlabel="Coordinate v₁",ylabel="Coordinate v₂");ax.set_xticks([0,1,2,3]);ax.set_yticks([0,1]);ax.set_aspect("equal")
  for end,col in [((1,1),BLUE),((2,0),AMBER),((3,1),GREEN)]:arrow(ax,end,col)
  ax.text(.50,1.36,"v",fontsize=28,color=BLUE);ax.text(2.6,1.36,"Σv",fontsize=28,color=GREEN);ax.text(2.3,.23,"βuuᵀv",fontsize=26,color=AMBER)
  fig.text(.077,.95,"Rank-one addition; full-rank Σ",fontsize=25);fig.text(.077,.87,"u = e₁, β = 2; v = (1, 1)ᵀ",fontsize=26);fig.text(.077,.79,"Σ = diag(3, 1)",fontsize=28);fig.text(.077,.20,"Added term: (2, 0)ᵀ",fontsize=27,color=AMBER);fig.text(.077,.13,"Total output: (3, 1)ᵀ",fontsize=27,color=GREEN);fig.text(.077,.06,"The orthogonal coordinate remains.",fontsize=23,color=GRAY)
 elif key=="one-spike-full-population-spectrum":
  ax=axes(fig);ax.bar(np.arange(1,6),[3,1,1,1,1],color=[PURPLE,BLUE,BLUE,BLUE,BLUE],edgecolor=GRAY,hatch="//");ax.set(xlim=(.3,5.7),ylim=(0,3.4),xlabel="Population eigenvalue index",ylabel="Population eigenvalue");ax.set_xticks([1,2,3,4,5]);ax.set_yticks([0,1,3]);fig.text(.077,.95,"One spike; no zero eigenvalues",fontsize=25);fig.text(.077,.87,"Original exercise: d = 5, β = 2",fontsize=25);fig.text(.077,.79,"Purple: u; blue: orthogonal",fontsize=26);fig.text(.077,.20,"One eigenvalue 3; four values 1",fontsize=24);fig.text(.077,.13,"All five variances stay positive.",fontsize=25);fig.text(.077,.06,"Only the added covariance is rank 1.",fontsize=23,color=GRAY)
 elif key=="zero-mean-extra-variance":
  x=np.linspace(-5,5,501);ax=axes(fig)
  for variance,col,style in [(1,BLUE,"-"),(2,PURPLE,"--"),(3,GREEN,":")]:ax.plot(x,np.exp(-x*x/(2*variance))/np.sqrt(2*np.pi*variance),color=col,ls=style,lw=3)
  ax.set(xlim=(-5,5),ylim=(0,.45),xlabel="Value along u",ylabel="Gaussian density");ax.set_xticks([-4,0,4]);ax.set_yticks([0,.2,.4]);fig.text(.077,.95,"Independent addition changes width",fontsize=23);fig.text(.077,.88,"Noise: variance 1  —",fontsize=27,color=BLUE);fig.text(.077,.82,"Signal: variance 2  - -",fontsize=27,color=PURPLE);fig.text(.077,.76,"Sum: variance 3  ···",fontsize=27,color=GREEN);fig.text(.077,.20,"All three means are zero.",fontsize=27);fig.text(.077,.13,"Var(g∥ + √2a) = 1 + 2 = 3",fontsize=25);fig.text(.077,.06,"Exact densities; not sampled data",fontsize=24,color=GRAY)
 elif key=="population-spike-and-sample-branch":
  beta=np.linspace(.02,2,501);ax=axes(fig);ax.plot(beta,1+beta,color=BLUE,lw=3);ax.plot(beta,leading(beta,.25),color=PURPLE,lw=3,ls="--");ax.axhline(2.25,color=GREEN,lw=2,ls=":");ax.axvline(.5,color=GRAY,lw=2,ls=":");ax.scatter([1,1],[2,2.5],color=[BLUE,PURPLE],s=55,zorder=5);ax.set(xlim=(0,2.05),ylim=(1,3.5),xlabel="Spike strength β",ylabel="Eigenvalue");ax.set_xticks([0,.5,1,2]);ax.set_yticks([1,2,2.25,3.5],["1","2","2.25","3.5"]);fig.text(.077,.95,"Population and sample differ.",fontsize=26);fig.text(.077,.88,"γ = 0.25; threshold β = 0.5",fontsize=25);fig.text(.077,.82,"Population 1 + β  —",fontsize=27,color=BLUE);fig.text(.077,.76,"Sample limit - -; edge ···",fontsize=25,color=PURPLE);fig.text(.077,.20,"At β = 1: population 2",fontsize=27,color=BLUE);fig.text(.077,.13,"Sample 2.5 > edge 2.25",fontsize=27,color=PURPLE);fig.text(.077,.06,"Outlier formula only above threshold",fontsize=22,color=GRAY)
 elif key=="aspect-ratio-separation-region":
  gamma=np.linspace(0,1,401);boundary=np.sqrt(gamma);ax=axes(fig);ax.fill_between(gamma,boundary,1.5,color=GREEN,alpha=.13);ax.fill_between(gamma,0,boundary,color=BLUE,alpha=.10);ax.plot(gamma,boundary,color=PURPLE,lw=3);ax.scatter([.25,.0625],[.5,.25],s=65,color=AMBER,zorder=4);ax.set(xlim=(0,1.02),ylim=(0,1.5),xlabel="Aspect ratio γ = d/n",ylabel="Spike strength β");ax.set_xticks([0,.25,1]);ax.set_yticks([0,.5,1,1.5]);ax.text(.3,1.15,"Separated",fontsize=26,color=GREEN);ax.text(.45,.20,"Attached",fontsize=26,color=BLUE);fig.text(.077,.95,"Separation requires β > √γ.",fontsize=26);fig.text(.077,.87,"Above purple curve: separated",fontsize=24);fig.text(.077,.79,"Boundary: asymptotic, not a p-value",fontsize=23);fig.text(.077,.20,"Fixed d: n → 4n",fontsize=28);fig.text(.077,.13,"γ: 0.25 → 0.0625",fontsize=27);fig.text(.077,.06,"Threshold β: 0.5 → 0.25",fontsize=27,color=AMBER)
 elif key=="spectral-gap-versus-alignment":
  beta=np.linspace(.02,3,501);gap=leading(beta,.25)-2.25;alignment=np.zeros_like(beta);above=beta>.5;alignment[above]=(1-.25/beta[above]**2)/(1+.25/beta[above])
  for rect,vals,label,col,ylim,mark,title in [((.10,.29,.31,.42),gap,"Sample limit minus edge",PURPLE,(0,2.3),.25,"Eigenvalue separation"),((.63,.29,.31,.42),alignment,"Squared alignment",GREEN,(0,1.05),.6,"Direction recovery")]:
   ax=axes(fig,rect);ax.plot(beta,vals,color=col,lw=3);ax.axvline(.5,color=GRAY,lw=2,ls=":");ax.scatter([1],[mark],s=75,color=AMBER,zorder=5);ax.set(xlim=(0,3.1),ylim=ylim,xlabel="Spike strength β",ylabel=label);ax.set_xticks([0,.5,1,3]);ax.set_yticks([0,1,2] if col==PURPLE else [0,.5,1]);ax.set_title(title,fontsize=28,pad=27)
  fig.text(.04,.94,"Gaussian γ = 0.25: outlier size and alignment are separate",fontsize=29);fig.text(.04,.83,"β = 1: edge gap 0.25; squared alignment 0.6",fontsize=29,color=AMBER);fig.text(.04,.14,"A nonzero alignment need not be perfect recovery (alignment 1).",fontsize=28);fig.text(.04,.07,"Alignment formula restricted here to Gaussian 0 < γ < 1",fontsize=28,color=GRAY)
 elif key=="alignment-sign-invariance":
  theta=np.linspace(0,2*np.pi,361);ax=axes(fig);ax.plot(np.cos(theta),np.sin(theta),color=GRAY,lw=1.5,ls=":");ax.set(xlim=(-1.3,1.3),ylim=(-1.3,1.3),xlabel="Coordinate x₁",ylabel="Coordinate x₂");ax.set_aspect("equal");ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);arrow(ax,(1,0),GREEN);arrow(ax,(np.sqrt(.6),np.sqrt(.4)),PURPLE);arrow(ax,(-np.sqrt(.6),-np.sqrt(.4)),PURPLE,"--");ax.text(.97,-.32,"u",fontsize=28,color=GREEN);ax.text(.65,.9,"û",fontsize=28,color=PURPLE);ax.text(-1.07,-.9,"−û",fontsize=28,color=PURPLE);fig.text(.077,.95,"Sign reversal keeps the same line.",fontsize=24);fig.text(.077,.87,"u = e₁; û = (√0.6, √0.4)ᵀ",fontsize=26);fig.text(.077,.79,"All directions have unit length.",fontsize=26);fig.text(.077,.20,"uᵀû = √0.6; uᵀ(−û) = −√0.6",fontsize=23);fig.text(.077,.13,"Both squared alignments = 0.6",fontsize=25);fig.text(.077,.06,"Deterministic coordinate illustration",fontsize=23,color=GRAY)
 elif key=="same-plane-rotated-bases":
  theta=np.linspace(0,2*np.pi,361);ax=axes(fig);ax.plot(np.cos(theta),np.sin(theta),color=GRAY,lw=1.5,ls=":");ax.set(xlim=(-1.35,1.35),ylim=(-1.35,1.35),xlabel="Coordinate x₁",ylabel="Coordinate x₂");ax.set_aspect("equal");ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
  for end in [(1,0),(0,1)]:arrow(ax,end,BLUE)
  for end in [(np.sqrt(3)/2,.5),(-.5,np.sqrt(3)/2)]:arrow(ax,end,GREEN,"--")
  ax.text(1.0,-.32,"e₁",fontsize=26,color=BLUE);ax.text(.18,1.07,"e₂",fontsize=26,color=BLUE);ax.text(.82,.74,"b₁",fontsize=26,color=GREEN);ax.text(-.92,1.03,"b₂",fontsize=26,color=GREEN);fig.text(.077,.95,"Different bases; the same plane",fontsize=25);fig.text(.077,.87,"R³: signal plane z = 0",fontsize=27);fig.text(.077,.79,"Green basis rotated by 30°",fontsize=26);fig.text(.077,.20,"Individual squared overlap: 3/4",fontsize=24);fig.text(.077,.13,"Both span the full z = 0 plane.",fontsize=25);fig.text(.077,.06,"Illustration, not split-stability data",fontsize=23,color=GRAY)
 else:raise ValueError(key)
 output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(output,format="svg",metadata={"Date":None});plt.close(fig)
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
