"""Capstone contract illustrations; no new null, bootstrap, probe, or model experiment."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-rmt-08-contract","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";RED="#DC2626";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect=(.22,.31,.66,.4)):
 ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def arrow(ax,end,color,style="-"):
 ax.annotate("",xy=end,xytext=(0,0),arrowprops={"arrowstyle":"->","color":color,"lw":2.5,"linestyle":style,"mutation_scale":11,"shrinkA":0,"shrinkB":0})
def main(output):
 key=output.stem.removeprefix("A09-RMT-08-");wide=key in ["feature-wise-whole-trajectory-permutation","scaled-coordinate-ablation-backtransform"];tall=key in ["train-scale-split-mean-distinction","participation-ratio-not-rank"];w,h=(1200,920) if key=="feature-wise-whole-trajectory-permutation" else (1200,820) if wide else (520,1400) if tall else (520,1040);fig=plt.figure(figsize=(w/72,h/72),facecolor=BG)
 if key=="token-counts-and-prompt-units":
  ax=axes(fig);ax.bar([1,2,3],[3,2,1],color=BLUE,edgecolor=GRAY,hatch="//");ax.set(xlim=(.4,3.6),ylim=(0,3.5),xlabel="Independent prompt pack",ylabel="Observed token rows");ax.set_xticks([1,2,3],["P₁","P₂","P₃"]);ax.set_yticks([0,1,2,3]);fig.text(.077,.95,"Count matrix rows and units separately.",fontsize=22);fig.text(.077,.87,"Illustration: 3, 2, 1 rows per prompt",fontsize=23);fig.text(.077,.79,"Covariance n = 6; prompt units = 3",fontsize=24);fig.text(.077,.20,"Row weights: 3/6, 2/6, 1/6",fontsize=26);fig.text(.077,.13,"Split and bootstrap whole prompts.",fontsize=24);fig.text(.077,.06,"Specify actual token-position rules.",fontsize=24,color=GRAY)
 elif key=="train-scale-split-mean-distinction":
  for rect,values,mean,title,col,lim,ticks in [((.22,.65,.66,.12),[0,2],1,"Train mean 1; scale 1",BLUE,(-.5,2.5),[0,1,2]),((.22,.29,.66,.12),[2,4],3,"Held-out after train transform",GREEN,(1.5,4.5),[2,3,4])]:
   ax=axes(fig,rect);ax.axhline(0,color=GRAY,lw=1.5);ax.scatter(values,[0,0],color=col,s=85,zorder=5);ax.scatter([mean],[0],color=AMBER,marker="x",s=95,zorder=6);ax.set(xlim=lim,ylim=(-1,1),xlabel="Feature value");ax.set_xticks(ticks);ax.set_yticks([]);ax.spines["left"].set_visible(False);ax.spines["bottom"].set_position(("data",0));ax.set_title(title,fontsize=25,pad=30)
  fig.text(.077,.96,"Fixed train scale; own split centering",fontsize=22);fig.text(.077,.90,"Raw held-out values: (3,5)",fontsize=27);fig.text(.077,.52,"Train transform gives (2,4).",fontsize=26);fig.text(.077,.475,"Held-out transformed mean = 3",fontsize=25);fig.text(.077,.18,"Gram mean: (2²+4²)/2 = 10",fontsize=26);fig.text(.077,.125,"Own centering: (−1,1); covariance 1",fontsize=22);fig.text(.077,.07,"10 = 1 + mean shift² = 1 + 9",fontsize=25);fig.text(.077,.025,"Exact one-feature illustration",fontsize=24,color=GRAY)
 elif key=="participation-ratio-not-rank":
  for rect,values,title,col in [((.22,.64,.66,.17),np.array([3,3,3,3]),"Equal values: PR = 4",BLUE),((.22,.29,.66,.17),np.array([9,1,1,1]),"Concentrated: PR = 12/7",PURPLE)]:
   ax=axes(fig,rect);ax.bar([1,2,3,4],values,color=col,edgecolor=GRAY,hatch="//");ax.set(xlim=(.4,4.6),ylim=(0,10),xlabel="Eigenvalue index",ylabel="Eigenvalue");ax.set_xticks([1,2,3,4]);ax.set_yticks([0,3,9]);ax.set_title(title,fontsize=25,pad=26)
  fig.text(.077,.96,"Same rank; different concentration",fontsize=23);fig.text(.077,.90,"Both rank 4 and total variance 12",fontsize=24);fig.text(.077,.52,"PR = (sum λ)² / sum λ²",fontsize=28);fig.text(.077,.17,"Scale multiplier cancels from PR.",fontsize=24);fig.text(.077,.115,"PR is not a task-signal count.",fontsize=26);fig.text(.077,.06,"All-zero spectrum: undefined PR",fontsize=24,color=GRAY)
 elif key=="feature-wise-whole-trajectory-permutation":
  original=np.array([[[1,11],[2,12]],[[3,13],[4,14]],[[5,15],[6,16]]]);permuted=original.copy();permuted[:,:,0]=original[[2,0,1],:,0];permuted[:,:,1]=original[[1,2,0],:,1];members=[[[0,0],[1,1],[2,2]],[[2,1],[0,2],[1,0]]]
  for i,(values,title) in enumerate([(original,"Original prompt blocks"),(permuted,"One block permutation")]):
   ax=fig.add_axes((.14+i*.49,.25,.31,.48));ax.set(xlim=(-.5,1.5),ylim=(5.5,-.5));ax.set_xticks([0,1],["Feature 1","Feature 2"]);ax.set_yticks([.5,2.5,4.5],["P₁","P₂","P₃"]);ax.set_title(title,fontsize=29,pad=27)
   for prompt in range(3):
    for feature in range(2):
     col=[BLUE,PURPLE,GREEN][members[i][prompt][feature]];ax.add_patch(plt.Rectangle((feature-.49,2*prompt-.48),.98,1.96,facecolor=col,alpha=.10,edgecolor=GRAY))
     for token in range(2):ax.text(feature,2*prompt+token,str(values[prompt,token,feature]),ha="center",va="center",color=col,fontsize=30)
   ax.spines[["top","right","bottom","left"]].set_visible(False)
  fig.text(.04,.94,"Shuffle whole trajectories with a different prompt order per feature.",fontsize=27);fig.text(.04,.84,"Each block keeps token positions t₁ above t₂; pairing across features changes.",fontsize=25);fig.text(.04,.14,"Feature 1 order: P₃,P₁,P₂; feature 2 order: P₂,P₃,P₁",fontsize=29);fig.text(.04,.07,"Exact block arrangement, not a simulated null result",fontsize=29,color=GRAY)
 elif key=="analytic-observed-simulated-order":
  ax=axes(fig,(.20,.4,.68,.20));ax.axhline(0,color=GRAY,lw=1.5)
  for value,col,mark in [(3,BLUE,"o"),(4,AMBER,"s"),(5.2,PURPLE,"^")]:ax.scatter([value],[0],color=col,marker=mark,s=85,zorder=5)
  ax.set(xlim=(2.3,5.8),ylim=(-1,1),xlabel="Eigenvalue units");ax.set_xticks([3,4,5.2],["3.0","4.0","5.2"]);ax.set_yticks([]);ax.spines["left"].set_visible(False);ax.spines["bottom"].set_position(("data",0));fig.text(.077,.95,"Two references can disagree.",fontsize=27);fig.text(.077,.88,"○ Analytic MP edge: 3.0",fontsize=27,color=BLUE);fig.text(.077,.82,"□ Observed largest value: 4.0",fontsize=25,color=AMBER);fig.text(.077,.76,"△ Matched q₀.₉₅: 5.2",fontsize=27,color=PURPLE);fig.text(.077,.27,"4 > 3, but 4 < 5.2",fontsize=30);fig.text(.077,.20,"Do not reject the matched null.",fontsize=25);fig.text(.077,.13,"Do not replace a missing q by MP.",fontsize=24);fig.text(.077,.06,"Original exercise; no new simulation",fontsize=23,color=GRAY)
 elif key=="scaled-coordinate-ablation-backtransform":
  hvec=np.array([3.,0.]);D=np.diag([3.,1.]);u=np.ones(2)/np.sqrt(2);z=np.linalg.solve(D,hvec);remaining=z-u*np.dot(u,z);raw=D@remaining;naive=hvec-u*np.dot(u,hvec)
  for i,(title,inputvec,outputvec) in enumerate([("Raw h; D = diag(3,1)",hvec,None),("Scaled z; remove U component",z,remaining),("Back to raw coordinate",None,raw)]):
   ax=axes(fig,(.09+i*.31,.29,.24,.42));ax.set(xlim=(-.4,3.5),ylim=(-1.9,2),xlabel="Coordinate 1",ylabel="Coordinate 2");ax.set_aspect("equal");ax.set_xticks([0,1,3]);ax.set_yticks([-1,0,1]);ax.set_title(title,fontsize=23,pad=27)
   if inputvec is not None:arrow(ax,inputvec,BLUE)
   if outputvec is not None:arrow(ax,outputvec,GREEN)
   if i==1:arrow(ax,u,PURPLE)
   if i==2:arrow(ax,naive,RED,"--")
  fig.text(.04,.94,"Fit U in scaled coordinates; invert the scale after ablation.",fontsize=28);fig.text(.04,.83,"Mean 0, U = (1,1)ᵀ/√2; blue input; green retained; red naive raw",fontsize=25);fig.text(.04,.14,"(3,0)ᵀ → (1,0)ᵀ → (0.5,−0.5)ᵀ → (1.5,−0.5)ᵀ",fontsize=29);fig.text(.04,.07,"Naive raw U removal gives (1.5,−1.5)ᵀ instead; no behavior measured.",fontsize=26,color=GRAY)
 else:raise ValueError(key)
 output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(output,format="svg",metadata={"Date":None});plt.close(fig)
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
