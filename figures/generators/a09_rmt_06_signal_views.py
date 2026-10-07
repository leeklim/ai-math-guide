"""Small deterministic spectral comparison calculations; no null or bootstrap execution."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-rmt-06-signal","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect=(.22,.31,.66,.4)):
 ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def arrow(ax,end,color,style="-"):
 ax.annotate("",xy=end,xytext=(0,0),arrowprops={"arrowstyle":"->","color":color,"lw":2.5,"linestyle":style,"mutation_scale":11,"shrinkA":0,"shrinkB":0})
def main(output):
 key=output.stem.removeprefix("A09-RMT-06-");wide=key in ["row-and-column-permutation-grams","matched-amount-projection-ablations"];tall=key in ["overlap-as-average-projection","large-subspaces-overlap-without-matching"];w,h=(1200,930) if key=="row-and-column-permutation-grams" else (1200,820) if wide else (520,1400) if tall else (520,1040);fig=plt.figure(figsize=(w/72,h/72),facecolor=BG)
 if key=="quantile-and-observed-value":
  ax=axes(fig,(.20,.40,.68,.20));ax.axhline(0,color=GRAY,lw=2);ax.scatter([4.2,5],[0,0],s=90,color=[GREEN,AMBER],zorder=5);ax.set(xlim=(3.4,5.5),ylim=(-1,1),xlabel="Eigenvalue units");ax.set_xticks([4.2,5],["4.2","5.0"]);ax.set_yticks([]);ax.spines["left"].set_visible(False);ax.spines["bottom"].set_position(("data",0));fig.text(.077,.95,"Probability selects a location.",fontsize=26);fig.text(.077,.87,"1,000 matched nulls: stated q₀.₉₅",fontsize=24);fig.text(.077,.79,"95%: probability level",fontsize=27,color=PURPLE);fig.text(.077,.70,"q = 4.2; observed = 5.0",fontsize=27);fig.text(.077,.28,"Difference: 5.0 − 4.2 = 0.8",fontsize=26);fig.text(.077,.20,"The difference is not a p-value.",fontsize=25);fig.text(.077,.13,"Spectrum test ≠ task relevance",fontsize=26);fig.text(.077,.06,"No null distribution was fabricated.",fontsize=23,color=GRAY)
 elif key=="ordered-ranks-across-null-runs":
  ax=axes(fig);values=[[4,2,1],[3.8,2.3,.8],[4.2,1.9,1.1]]
  for vals,col,style,mark in zip(values,[BLUE,PURPLE,GREEN],["-","--",":"],["o","s","^"]):ax.plot([1,2,3],vals,color=col,ls=style,lw=2.5,marker=mark,ms=6)
  ax.set(xlim=(.7,3.3),ylim=(0,4.7),xlabel="Ordered eigenvalue rank j",ylabel="Illustrative eigenvalue");ax.set_xticks([1,2,3]);ax.set_yticks([0,2,4]);fig.text(.077,.95,"Collect the same rank across runs.",fontsize=24);fig.text(.077,.87,"Three fixed illustrative spectra",fontsize=25);fig.text(.077,.79,"Each line: one sorted spectrum",fontsize=25);fig.text(.077,.20,"Rank 1 values: 4.0, 3.8, 4.2",fontsize=26);fig.text(.077,.13,"Do not pool ranks 1, 2, 3.",fontsize=27);fig.text(.077,.06,"Not new simulation or null quantiles",fontsize=23,color=GRAY)
 elif key=="row-and-column-permutation-grams":
  original=np.array([[1,4],[2,5],[3,6]]);common=original[[2,0,1]];column=original.copy();column[:,1]=original[[1,2,0],1]
  for i,(matrix,title,ids) in enumerate([(original,"Original X",[[0,0],[1,1],[2,2]]),(common,"Common row shuffle",[[2,2],[0,0],[1,1]]),(column,"Only column 2 shuffled",[[0,1],[1,2],[2,0]])]):
   left=.09+i*.30;ax=fig.add_axes((left,.48,.23,.31));ax.set_xlim(-.5,1.5);ax.set_ylim(2.5,-.5);ax.set_xticks([0,1],["x₁","x₂"]);ax.set_yticks([]);ax.set_title(title,fontsize=26,pad=24)
   colors=[BLUE,PURPLE,GREEN]
   for r in range(3):
    for col in range(2):
     ax.add_patch(plt.Rectangle((col-.5,r-.5),1,1,facecolor=colors[ids[r][col]],alpha=.10,edgecolor=GRAY));ax.text(col,r,str(matrix[r,col]),ha="center",va="center",color=colors[ids[r][col]],fontsize=29)
   ax.spines[["top","right","bottom","left"]].set_visible(False);center=matrix-matrix.mean(0);gram=center.T@center;gax=fig.add_axes((left,.17,.23,.18));gax.set_xlim(-.5,1.5);gax.set_ylim(1.5,-.5);gax.set_xticks([]);gax.set_yticks([]);gax.set_title("Centered XᵀX",fontsize=26,pad=20)
   for r in range(2):
    for col in range(2):gax.add_patch(plt.Rectangle((col-.5,r-.5),1,1,fill=False,edgecolor=GRAY));gax.text(col,r,f"{gram[r,col]:.0f}",ha="center",va="center",fontsize=29)
   gax.spines[["top","right","bottom","left"]].set_visible(False)
  fig.text(.04,.95,"Paired rows preserve the Gram; separate column shuffles need not.",fontsize=27);fig.text(.04,.88,"Cell colors and row positions track original pair membership.",fontsize=27);fig.text(.04,.075,"Same marginals; different feature pairing in the right matrix",fontsize=29);fig.text(.04,.025,"Exact small matrices, not a prompt-preserving null generator",fontsize=25,color=GRAY)
 elif key=="overlap-as-average-projection":
  top=axes(fig,(.22,.65,.66,.12));top.axhline(0,color=GRAY,lw=1);arrow(top,(1,0),BLUE);top.set(xlim=(-.1,1.2),ylim=(-.5,.5),xlabel="Shared coordinate x₁");top.set_xticks([0,1]);top.set_yticks([])
  ax=axes(fig,(.22,.27,.66,.27));ax.set(xlim=(-.15,1.25),ylim=(-.55,1.3),xlabel="Coordinate x₂",ylabel="Coordinate x₃");ax.set_aspect("equal");ax.set_xticks([0,.5,1]);ax.set_yticks([0,1]);arrow(ax,(1,0),BLUE);arrow(ax,(.5,np.sqrt(3)/2),PURPLE);arrow(ax,(.5,0),AMBER);ax.plot([.5,.5],[0,np.sqrt(3)/2],color=GRAY,ls=":",lw=2);ax.text(.35,1.03,"u₂ᴮ",fontsize=27,color=PURPLE);ax.text(.76,-.31,"u₂ᴬ",fontsize=27,color=BLUE);ax.text(.03,-.31,"proj",fontsize=24,color=AMBER)
  fig.text(.077,.96,"Overlap averages squared projections.",fontsize=23);fig.text(.077,.90,"k = 2 in R³",fontsize=28);fig.text(.077,.83,"Shared u₁: squared projection 1",fontsize=24);fig.text(.077,.59,"Second u₂: projection length 1/2",fontsize=24);fig.text(.077,.17,"O = (1 + (1/2)²)/2 = 5/8",fontsize=27);fig.text(.077,.11,"One direction shared; one partly shared.",fontsize=22);fig.text(.077,.055,"Exact coordinate example, not a split",fontsize=22,color=GRAY)
 elif key=="rotation-invariant-overlap-matrix":
  angle=np.pi/6;rotation=np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]]);squared=rotation**2;ax=fig.add_axes((.22,.31,.66,.4));ax.set(xlim=(-.5,1.5),ylim=(1.5,-.5));ax.set_aspect("equal");ax.set_xticks([0,1],["u₁ᴮ","u₂ᴮ"]);ax.set_yticks([0,1],["u₁ᴬ","u₂ᴬ"]);ax.set_xlabel("Columns of U_B",fontsize=24);ax.set_ylabel("Columns of U_A",fontsize=24)
  for r in range(2):
   for col in range(2):ax.add_patch(plt.Rectangle((col-.5,r-.5),1,1,facecolor="#2171B5" if r==col else "#C6DBEF",edgecolor=BG));ax.text(col,r,"3/4" if r==col else "1/4",ha="center",va="center",color=BG if r==col else BLUE,fontsize=29)
  fig.text(.077,.95,"Same span; a rotated basis",fontsize=27);fig.text(.077,.87,"Squared entries of U_AᵀU_B",fontsize=27);fig.text(.077,.79,"Basis rotation: 30°",fontsize=28);fig.text(.077,.20,"All four entries sum to 2.",fontsize=26);fig.text(.077,.13,"Subspace O = 2/k = 1, k = 2",fontsize=26);fig.text(.077,.06,"Diagonal-only averaging gives 3/4.",fontsize=23,color=GRAY)
 elif key=="large-subspaces-overlap-without-matching":
  for k,rect in [(2,(.17,.65,.75,.14)),(6,(.17,.40,.75,.14)),(8,(.17,.15,.75,.14))]:
   ax=fig.add_axes(rect,facecolor=BG);ax.set(xlim=(-.5,7.5),ylim=(-.6,1.6));ax.set_xticks(np.arange(8),[str(i) for i in range(1,9)]);ax.set_yticks([1,0],["A","B"]);ax.tick_params(axis="both",labelsize=22)
   for j in range(8):
    for y,selected,col,hatch in [(1,j<k,BLUE,""),(0,j>=8-k,GREEN,"//")]:ax.add_patch(plt.Rectangle((j-.48,y-.42),.96,.84,facecolor=col if selected else "white",alpha=.45 if selected else 1,edgecolor=GRAY,hatch=hatch if selected else None))
   ax.set_title(f"k = {k}: shared {max(0,2*k-8)} of {k}",fontsize=26,pad=25);ax.set_xlabel("Ambient coordinate (d = 8)",fontsize=23);ax.spines[["top","right","bottom","left"]].set_visible(False)
  fig.text(.077,.96,"Large subspaces can overlap broadly.",fontsize=23);fig.text(.077,.90,"A: first k axes; B: last k axes",fontsize=25);fig.text(.077,.84,"O = shared axis count / k",fontsize=26);fig.text(.077,.06,"O: 0, 2/3, 1 — not a random-null law",fontsize=22,color=GRAY)
 elif key=="matched-amount-projection-ablations":
  hvec=np.array([2.,1.])
  for i,(u,title) in enumerate([(np.array([1.,0.]),"Target u = e₁"),(np.array([.6,.8]),"Control u = (0.6, 0.8)ᵀ")]):
   removed=u*np.dot(u,hvec);retained=hvec-removed;ax=axes(fig,(.10+i*.52,.29,.31,.42));ax.set(xlim=(-.3,2.8),ylim=(-1.15,2.15),xlabel="Coordinate h₁",ylabel="Coordinate h₂");ax.set_aspect("equal");ax.set_xticks([0,1,2]);ax.set_yticks([-1,0,1,2]);arrow(ax,hvec,BLUE);arrow(ax,removed,AMBER);arrow(ax,retained,GREEN);ax.plot([removed[0],hvec[0]],[removed[1],hvec[1]],color=GRAY,ls=":",lw=2);ax.text(2.05,1.25,"h",fontsize=27,color=BLUE);ax.text(.95,1.90,"Removed" if i else "",fontsize=24,color=AMBER);ax.set_title(title,fontsize=27,pad=27)
  fig.text(.04,.94,"Same rank 1 and removal norm; different residual directions",fontsize=28);fig.text(.04,.83,"Blue h; amber UUᵀh; green h − UUᵀh",fontsize=29);fig.text(.04,.14,"Both remove norm 2 and retain norm 1; residuals (0,1)ᵀ and (0.8,−0.6)ᵀ.",fontsize=25);fig.text(.04,.07,"Fixed comparison, not random-control sampling or behavior evidence",fontsize=27,color=GRAY)
 else:raise ValueError(key)
 output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(output,format="svg",metadata={"Date":None});plt.close(fig)
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
