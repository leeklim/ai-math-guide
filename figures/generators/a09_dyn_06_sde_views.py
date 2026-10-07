"""Draw small reproducible stochastic-calculus illustrations, not model experiments."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-dyn-06-sde","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def main(output):
    key=output.stem.removeprefix("A09-DYN-06-");fig=plt.figure(figsize=(520/72,1060/72),facecolor=BG);ax=fig.add_axes((.23,.30,.65,.40),facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65)
    if key=="diffusion-line-support":
        w=np.linspace(-1.1,1.1,150);ax.plot(2*w,w,color=GREEN,lw=3);ax.scatter([-2,0,2],[-1,0,1],color=BLUE,s=70,zorder=4);ax.set_aspect("equal");ax.set(xlim=(-2.5,2.5),ylim=(-1.4,1.4),xlabel="Noise change ΔX₁",ylabel="Noise change ΔX₂");ax.set_xticks([-2,0,2]);ax.set_yticks([-1,0,1])
        fig.text(.077,.95,"One noise direction, two state axes",fontsize=25);fig.text(.077,.875,"σ = (2, 1)ᵀ: shape 2 × 1",fontsize=27);fig.text(.077,.81,"ΔX = (2 ΔW, ΔW)",fontsize=28,color=GREEN);fig.text(.077,.19,"σσᵀ = [[4, 2], [2, 1]]",fontsize=27);fig.text(.077,.115,"Covariance shape: 2 × 2",fontsize=27,color=GRAY);fig.text(.077,.05,"Multiply it by Δt for the increment.",fontsize=24,color=GRAY)
    elif key=="brownian-smooth-scale":
        h=np.logspace(-3,0,300);ax.loglog(h,np.sqrt(h),color=PURPLE,lw=3);ax.loglog(h,h,"--",color=GREEN,lw=3);ax.scatter([.04,.04],[.2,.04],color=[PURPLE,GREEN],s=75,zorder=4);ax.set(xlim=(.0009,1.1),ylim=(.0008,1.2),xlabel="Interval h",ylabel="Increment scale");ax.set_xticks([.001,.01,.1,1],[".001",".01",".1","1"]);ax.set_yticks([.001,.01,.1,1],[".001",".01",".1","1"]);ax.xaxis.set_minor_locator(NullLocator());ax.yaxis.set_minor_locator(NullLocator())
        fig.text(.077,.95,"Random spread versus smooth change",fontsize=25);fig.text(.077,.875,"Brownian SD: √h  —",fontsize=28,color=PURPLE);fig.text(.077,.81,"Smooth unit velocity: h  - -",fontsize=26,color=GREEN);fig.text(.077,.19,"h = 0.04: SD 0.2, smooth 0.04",fontsize=25);fig.text(.077,.115,"Both axes use a logarithmic scale.",fontsize=24,color=GRAY);fig.text(.077,.05,"SD is not a maximum increment.",fontsize=25,color=GRAY)
    elif key=="quadratic-variation-comparison":
        ns=[16,64,256,1024,4096]
        for seed,col in [(20261001,BLUE),(20261002,PURPLE),(20261003,GREEN)]:
            fine=np.random.default_rng(seed).normal(size=4096)/64;qs=[np.sum(fine.reshape(n,4096//n).sum(1)**2) for n in ns];ax.plot(ns,qs,"o-",color=col,lw=2,ms=6)
        ax.plot(ns,1/np.array(ns),"s--",color=AMBER,lw=2,ms=6);ax.axhline(1,color=GRAY,lw=1.3,ls=":");ax.set_xscale("log");ax.set(xlim=(12,5500),ylim=(-.08,2),xlabel="Partition count n",ylabel="Sum of squared increments");ax.set_xticks(ns,[str(n) for n in ns]);ax.xaxis.set_minor_locator(NullLocator());ax.set_yticks([0,1,2])
        fig.text(.077,.95,"Squared increments need not vanish",fontsize=25);fig.text(.077,.875,"Three nested Brownian examples",fontsize=25);fig.text(.077,.81,"Reference [W]₁ = 1  · ·",fontsize=27,color=GRAY);fig.text(.077,.19,"Smooth x(t) = t: sum = 1/n",fontsize=26,color=AMBER);fig.text(.077,.115,"Finite random sums are not exactly 1.",fontsize=24,color=GRAY);fig.text(.077,.05,"Seeded examples illustrate, not prove.",fontsize=24,color=GRAY)
    elif key=="finite-square-remainder":
        delta=np.linspace(-.5,.5,250);ax.plot(delta,(1+delta)**2,color=GREEN,lw=3);ax.plot(delta,1+2*delta,"--",color=PURPLE,lw=3)
        for v in [-.3,.3]:ax.plot([v,v],[1+2*v,(1+v)**2],":",color=AMBER,lw=2);ax.scatter([v,v],[1+2*v,(1+v)**2],s=55,color=[PURPLE,GREEN],zorder=4)
        ax.set(xlim=(-.53,.53),ylim=(0,2.4),xlabel="Finite change ΔX",ylabel="f(1 + ΔX)");ax.set_xticks([-.3,0,.3]);ax.set_yticks([0,1,2])
        fig.text(.077,.95,"The quadratic remainder is visible",fontsize=25);fig.text(.077,.875,"Exact: (1 + ΔX)²  —",fontsize=27,color=GREEN);fig.text(.077,.81,"Tangent: 1 + 2 ΔX  - -",fontsize=27,color=PURPLE);fig.text(.077,.19,"ΔX = ±0.3 → remainder 0.09",fontsize=26,color=AMBER);fig.text(.077,.115,"One increment² need not equal h.",fontsize=23,color=GRAY);fig.text(.077,.05,"Itô keeps accumulated squares.",fontsize=23,color=GRAY)
    elif key=="ito-second-moment":
        t=np.linspace(0,2,200);ax.plot(t,1+t,color=GREEN,lw=3);ax.axhline(1,color=PURPLE,lw=2.5,ls="--");ax.set(xlim=(0,2.1),ylim=(.5,3.4),xlabel="Time t",ylabel="Second moment E[Xₜ²]");ax.set_xticks([0,1,2]);ax.set_yticks([1,2,3])
        fig.text(.077,.95,"Itô correction and variance growth",fontsize=24);fig.text(.077,.875,"dX = dW; X₀ = 1",fontsize=28);fig.text(.077,.81,"Correct: 1 + t  —",fontsize=28,color=GREEN);fig.text(.077,.19,"Omit correction: 1  - -",fontsize=28,color=PURPLE);fig.text(.077,.115,"Mean X stays 1; second moment grows.",fontsize=24,color=GRAY);fig.text(.077,.05,"Different targets: E[X], E[X²].",fontsize=24,color=GRAY)
    elif key=="paired-coarse-fine-increments":
        t=np.arange(5)*.01;inc=np.array([.1,-.2,.3,.05]);w=np.r_[0,np.cumsum(inc)];ax.plot(t,w,"o-",color=BLUE,lw=2.5,ms=7);ax.plot([0,.04],[0,.25],"s--",color=PURPLE,lw=2,ms=8);ax.set(xlim=(-.002,.043),ylim=(-.16,.33),xlabel="Time t",ylabel="Stored W values");ax.set_xticks([0,.02,.04]);ax.set_yticks([-.1,0,.25])
        fig.text(.077,.95,"Coarse noise is a sum, not a redraw",fontsize=25);fig.text(.077,.875,"Fine h = 0.01  o —",fontsize=28,color=BLUE);fig.text(.077,.81,"Coarse h = 0.04  □ - -",fontsize=27,color=PURPLE);fig.text(.077,.19,"0.1 − 0.2 + 0.3 + 0.05 = 0.25",fontsize=25);fig.text(.077,.115,"Same interval, same two endpoints.",fontsize=25,color=GRAY);fig.text(.077,.05,"Segments only connect stored points.",fontsize=25,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
