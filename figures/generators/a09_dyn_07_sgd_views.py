"""Draw scalar local SGD comparisons under explicit illustrative assumptions."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-dyn-07-sgd","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect):
    ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def main(output):
    key=output.stem.removeprefix("A09-DYN-07-");h=1350 if key=="step-time-covariance" else 1020;fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="gradient-update-components":
        ax=axes(fig,(.18,.28,.73,.40));ax.set(xlim=(.2,1.15),ylim=(-.85,.95),xlabel="Parameter coordinate θ");ax.set_xticks([.5,.7,1]);ax.set_yticks([])
        for start,end,y,col,label in [(1,.7,.5,PURPLE,"Drift −0.3"),(.7,.5,0,AMBER,"Noise −0.2"),(1,.5,-.5,GREEN,"Total −0.5")]:
            ax.annotate("",(end,y),(start,y),arrowprops=dict(arrowstyle="->",color=col,lw=2.6,mutation_scale=13));ax.scatter([start],[y],s=45,color=BLUE,zorder=4);ax.text(.25,y+.20,label,color=col,fontsize=26)
        ax.axvline(.7,color=GRAY,ls=":",lw=1)
        fig.text(.077,.95,"Gradient noise becomes a displacement",fontsize=24);fig.text(.077,.87,"Mean gradient 3; batch gradient 5",fontsize=25);fig.text(.077,.805,"ξ = 2; η = 0.1; start θ = 1",fontsize=26);fig.text(.077,.17,"−ηξ = −0.2, not ξ = 2.",fontsize=27,color=AMBER);fig.text(.077,.10,"End θ = 1 − 0.3 − 0.2 = 0.5",fontsize=25);fig.text(.077,.04,"Rows show components, not time axes.",fontsize=24,color=GRAY)
    elif key=="step-time-covariance":
        eta=np.linspace(0,.25,200)
        for y,vals,lab in [(.56,4*eta**2,"Variance per step"),(.17,4*eta,"Variance per time")]:
            ax=axes(fig,(.23,y,.65,.25));ax.plot(eta,vals,color=PURPLE,lw=3);ax.set(xlim=(0,.26),xlabel="Learning rate η",ylabel=lab);ax.set_xticks([0,.1,.2])
            ax.scatter([.1],[.04 if y==.56 else .4],s=75,color=GREEN,zorder=4)
            fig.text(.077,y+.28,"η²C" if y==.56 else "ηC = (η²C) / η",fontsize=28,color=PURPLE)
        fig.text(.077,.95,"Per-step and per-time covariance",fontsize=26);fig.text(.077,.89,"Illustrative fixed C = 4",fontsize=28);fig.text(.077,.070,"η = 0.1: step variance 0.04",fontsize=26);fig.text(.077,.038,"Time variance 0.4; step lasts η.",fontsize=25,color=GRAY)
    elif key=="mean-gradient-nonlinearity":
        ax=axes(fig,(.23,.30,.65,.40));theta=np.linspace(-1.25,1.25,250);ax.plot(theta,theta**2,color=PURPLE,lw=3);ax.scatter([-1,1],[1,1],color=BLUE,s=75,zorder=4);ax.scatter([0],[1],color=GREEN,s=90,zorder=5);ax.scatter([0],[0],color=AMBER,s=90,zorder=5);ax.set(xlim=(-1.4,1.4),ylim=(-.12,1.8),xlabel="Parameter θ",ylabel="Gradient θ²");ax.set_xticks([-1,0,1]);ax.set_yticks([0,1]);ax.plot([0,0],[0,1],":",color=GRAY,lw=1.5)
        fig.text(.077,.95,"Averaging and a gradient differ",fontsize=26);fig.text(.077,.87,"Illustrative L(θ) = θ³/3",fontsize=28);fig.text(.077,.805,"θ = ±1, each with probability 1/2",fontsize=25);fig.text(.077,.19,"Green: E[gradient] = 1",fontsize=27,color=GREEN);fig.text(.077,.12,"Orange: gradient(E[θ]) = 0",fontsize=26,color=AMBER);fig.text(.077,.05,"The mean parameter is zero.",fontsize=26,color=GRAY)
    elif key=="learning-rate-batch-scale":
        ax=axes(fig,(.23,.30,.65,.40));bs=np.arange(1,65)
        for eta,col,style in [(.1,PURPLE,"-"),(.05,GREEN,"--")]:ax.loglog(bs,eta/bs,style,color=col,lw=3)
        ax.scatter([4],[.025],color=PURPLE,s=75,zorder=4);ax.set(xlim=(.9,75),ylim=(.0005,.13),xlabel="Batch size B",ylabel="Variance per time");ax.set_xticks([1,4,16,64],["1","4","16","64"]);ax.set_yticks([.001,.01,.1],[".001",".01",".1"]);ax.xaxis.set_minor_locator(NullLocator());ax.yaxis.set_minor_locator(NullLocator())
        fig.text(.077,.95,"Independent sample averaging",fontsize=28);fig.text(.077,.87,"η = 0.1: η/B  —",fontsize=28,color=PURPLE);fig.text(.077,.805,"η = 0.05: η/B  - -",fontsize=28,color=GREEN);fig.text(.077,.19,"Individual sample covariance = 1.",fontsize=25);fig.text(.077,.12,"At B = 4, η = 0.1: variance 0.025",fontsize=25);fig.text(.077,.05,"Use the square root for a coefficient.",fontsize=24,color=GRAY)
    elif key=="euler-multiplier-stability":
        ax=axes(fig,(.23,.30,.65,.40));q=np.linspace(0,3,250);ax.axvspan(0,2,color=GREEN,alpha=.08);ax.plot(q,1-q,color=PURPLE,lw=3);ax.plot(q,np.exp(-q),"--",color=GREEN,lw=3)
        for y in [-1,1]:ax.axhline(y,color=GRAY,lw=1.3,ls=":")
        ax.axhline(0,color=GRAY,lw=1);ax.scatter([0,2],[1,-1],s=75,facecolors=BG,edgecolors=AMBER,lw=2,zorder=5);ax.set(xlim=(0,3.1),ylim=(-2.2,1.3),xlabel="Dimensionless q = ηa",ylabel="One-step multiplier");ax.set_xticks([0,1,2,3]);ax.set_yticks([-2,-1,0,1])
        fig.text(.077,.95,"Convergence versus path agreement",fontsize=25);fig.text(.077,.87,"Euler: 1 − q  —",fontsize=28,color=PURPLE);fig.text(.077,.805,"Exact flow: exp(−q)  - -",fontsize=26,color=GREEN);fig.text(.077,.19,"Euler converges only for 0 < q < 2.",fontsize=25);fig.text(.077,.12,"1 < q < 2: signs alternate.",fontsize=26,color=PURPLE);fig.text(.077,.05,"The exact multiplier stays positive.",fontsize=25,color=GRAY)
    elif key=="fixed-versus-pooled-gradients":
        ax=axes(fig,(.23,.30,.65,.40));noise=np.array([-.1,0,.1]);ax.scatter(np.zeros(3),noise,color=BLUE,s=85,zorder=4);ax.scatter(np.ones(3),1+noise,color=PURPLE,s=85,zorder=4);ax.scatter(np.full(3,2),noise,color=BLUE,s=65,zorder=4);ax.scatter(np.full(3,2),1+noise,color=PURPLE,s=65,zorder=4);ax.scatter([0,1,2],[0,1,.5],marker="_",color=GRAY,s=550,lw=2,zorder=5);ax.set(xlim=(-.4,2.4),ylim=(-.25,1.25),ylabel="Batch gradient");ax.set_xticks([0,1,2],["θ = 0","θ = 1","Pooled"]);ax.set_yticks([0,.5,1])
        fig.text(.077,.95,"Do not mix changing gradient means",fontsize=25);fig.text(.077,.87,"Mean gradient = θ",fontsize=28);fig.text(.077,.805,"Same noise: −0.1, 0, 0.1",fontsize=27);fig.text(.077,.19,"Fixed-state variance ≈ 0.0067",fontsize=26);fig.text(.077,.12,"Pooled variance ≈ 0.2567",fontsize=26,color=AMBER);fig.text(.077,.05,"Pooling includes mean-state change.",fontsize=24,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
