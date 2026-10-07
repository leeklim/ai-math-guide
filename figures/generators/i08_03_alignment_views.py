"""Render analytic point configurations for the I08-03 alignment definitions."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
parser = ArgumentParser(); parser.add_argument("--output", type=Path, required=True)
out = parser.parse_args().output; name = out.stem.removeprefix("I08-03-")
bg = "#F8FAFC"; blue = "#2563EB"; green = "#059669"; purple = "#7C3AED"
mpl.rcParams.update({"font.family":"DejaVu Sans", "font.size":26, "axes.labelsize":24,
    "xtick.labelsize":22, "ytick.labelsize":22, "svg.fonttype":"none", "svg.hashsalt":"i08-03-"+name})
X = np.array([[-1.,0.],[0.,1.],[1.,-1.]])
assert np.allclose(X.mean(axis=0), 0.)
def axis(ax, lim=1.6):
    ax.set_facecolor(bg); ax.grid(color="#CBD5E1", alpha=.6); ax.set_axisbelow(True)
    ax.spines[["top","right"]].set_visible(False); ax.set_aspect("equal")
    ax.set(xlim=(-lim,lim), ylim=(-lim,lim), xticks=[-1,0,1], yticks=[-1,0,1],
           xlabel="Feature 1", ylabel="Feature 2")
def points(ax, P, color, label, ls="-", ids=True):
    closed=np.vstack([P,P[0]])
    ax.plot(closed[:,0], closed[:,1], color=color, lw=2, ls=ls, label=label)
    ax.scatter(P[:,0],P[:,1],color=color,s=75,zorder=4)
    if ids:
        for text, row in zip(["A","B","C"],P):
            dx = -24 if row[0] < -.5 else (10 if row[0] > .5 else -8)
            dy = -24 if row[1] < -.5 else (13 if row[1] > .5 else 6)
            ax.annotate(text,row,xytext=(dx,dy),textcoords="offset points",fontsize=24,color=color)
if name == "centering-removes-mean":
    fig,ax=plt.subplots(figsize=(520/72,780/72),facecolor=bg)
    fig.subplots_adjust(left=.18,right=.94,bottom=.37,top=.77)
    axis(ax);ax.set(xlim=(-2.,5.),ylim=(-2.,4.),xticks=[-1,0,3,4],yticks=[-1,0,2,3])
    shifted=X+np.array([3.,2.])
    points(ax,shifted,blue,"Before",ids=False);points(ax,X,green,"Centered","--",ids=False)
    ax.scatter([3,0],[2,0],marker="D",s=80,color=purple,zorder=5)
    ax.add_patch(FancyArrowPatch((3.,2.),(0.,0.),arrowstyle="-|>",mutation_scale=15,lw=3,color=purple,shrinkA=6,shrinkB=13))
    ax.text(.8,3.45,"mean = (3,2)",color=purple,fontsize=24)
    title="Center each feature column"
    fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.53,.25),ncol=2,frameon=False,fontsize=24)
    fig.text(.5,.17,"Subtract the same mean from each row.",ha="center",fontsize=24,color=purple)
    footer="Analytic three-row example"
elif name == "orthogonal-alignment":
    Q=np.array([[0.,-1.],[1.,0.]])
    Xt=X@Q;U,_,Vt=np.linalg.svd(Xt.T@X);alignment=U@Vt
    assert np.allclose(Xt@alignment,X)
    fig,axs=plt.subplots(1,3,figsize=(1350/72,710/72),facecolor=bg)
    fig.subplots_adjust(left=.065,right=.97,bottom=.30,top=.76,wspace=.38)
    for ax,P,c,heading in zip(axs,[X,Xt,Xt@alignment],[blue,purple,green],["Reference X_s","Rotated X_t","Aligned X_t Q★"]):
        axis(ax);points(ax,P,c,heading);ax.set_title(heading,fontsize=28,pad=20)
    title="One shared orthogonal map aligns the same input rows"
    footer="Analytic example: row IDs A/B/C and pairwise distances are preserved."
    fig.text(.5,.18,"Q★ = U Vᵀ from the SVD of X_tᵀ X_s; aligned error = 0.",ha="center",fontsize=27,color=green)
elif name == "cka-versus-scale-error":
    Y=2*X;G=X@X.T;K=Y@Y.T;cka=(G*K).sum()/np.sqrt((G*G).sum()*(K*K).sum())
    U,_,Vt=np.linalg.svd(Y.T@X);error=np.linalg.norm(X-Y@(U@Vt),"fro")
    assert np.isclose(cka,1.) and np.isclose(error,2.)
    fig,ax=plt.subplots(figsize=(520/72,800/72),facecolor=bg)
    fig.subplots_adjust(left=.20,right=.92,bottom=.42,top=.76)
    axis(ax,2.6);ax.set(xticks=[-2,0,2],yticks=[-2,0,2])
    points(ax,X,blue,"X",ids=False);points(ax,Y,green,"2X","--",ids=False)
    title="Scale changes alignment error"
    fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.54,.31),ncol=2,frameon=False,fontsize=25)
    fig.text(.5,.23,"Linear CKA = 1",ha="center",fontsize=27,color=blue)
    fig.text(.5,.16,"Min Frobenius error = 2 > 0",ha="center",fontsize=25,color=green)
    footer="Orthogonal Q cannot halve the lengths."
else: raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94)
fig.text(.5,.07,footer,ha="center",fontsize=24,color="#475569")
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
