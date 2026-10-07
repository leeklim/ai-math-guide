"""Draw Langevin drift, density, covariance geometry, and finite-step bias."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-dyn-05-langevin","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect):
    ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def main(output):
    key=output.stem.removeprefix("A09-DYN-05-")
    h=1400 if key in ("potential-drift","isotropic-anisotropic-covariance","unconfined-window-mass") else 980
    fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="potential-drift":
        x=np.linspace(-2,2,200)
        for y,vals,lab,col in [(.56,.5*x*x,"Energy U(x)",BLUE),(.17,-x,"Drift −U′(x)",PURPLE)]:
            ax=axes(fig,(.23,y,.65,.25));ax.plot(x,vals,color=col,lw=3);ax.set(xlim=(-2.2,2.2),xlabel="State x",ylabel=lab);ax.set_xticks([-2,0,1,2])
            if col==BLUE:ax.set(ylim=(0,2.5));ax.set_yticks([0,.5,2]);ax.scatter([1],[.5],color=GREEN,s=75,zorder=4)
            else:ax.set(ylim=(-2.5,2.5));ax.set_yticks([-2,-1,0,2]);ax.scatter([1],[-1],color=GREEN,s=75,zorder=4)
        fig.text(.077,.955,"Energy value versus downhill drift",fontsize=26);fig.text(.077,.86,"U(x) = x²/2",fontsize=28,color=BLUE);fig.text(.077,.47,"−U′(x) = −x",fontsize=28,color=PURPLE);fig.text(.077,.05,"At x = 1: U = 0.5, drift = −1.",fontsize=25,color=GRAY)
    elif key=="conditional-noise-law":
        ax=axes(fig,(.23,.27,.65,.42));mean=.99;sd=.1;x=np.linspace(mean-4*sd,mean+4*sd,400);density=np.exp(-.5*((x-mean)/sd)**2)/(sd*np.sqrt(2*np.pi));ax.plot(x,density,color=GREEN,lw=3);ax.fill_between(x,0,density,where=np.abs(x-mean)<=sd,color=GREEN,alpha=.13);ax.axvline(mean,color=PURPLE,lw=2,ls="--");ax.set(xlim=(.58,1.40),ylim=(0,4.4),xlabel="Next state Xₖ₊₁",ylabel="Conditional density");ax.set_xticks([.7,.99,1.3]);ax.set_yticks([0,2,4])
        fig.text(.077,.95,"The next-state distribution",fontsize=26);fig.text(.077,.865,"Xₖ = 1; T = 0.5; h = 0.01",fontsize=26);fig.text(.077,.80,"Mean = 1 − 0.01 = 0.99",fontsize=27,color=PURPLE);fig.text(.077,.17,"Noise SD = √(2Th) = 0.1",fontsize=27,color=GREEN);fig.text(.077,.095,"Shading: mean ± one SD.",fontsize=26,color=GRAY);fig.text(.077,.035,"Not a bound on every draw.",fontsize=26,color=GRAY)
    elif key=="quadratic-temperature-density":
        ax=axes(fig,(.23,.27,.65,.43));x=np.linspace(-3,3,400)
        for temp,col,style in [(.25,GREEN,"-"),(1,PURPLE,"--")]:ax.plot(x,np.exp(-x*x/(2*temp))/np.sqrt(2*np.pi*temp),style,color=col,lw=3)
        ax.set(xlim=(-3.1,3.1),ylim=(0,.9),xlabel="State x",ylabel="Stationary density");ax.set_xticks([-2,0,2]);ax.set_yticks([0,.4,.8])
        fig.text(.077,.95,"Temperature changes the spread",fontsize=27);fig.text(.077,.865,"T = 0.25; variance 0.25  —",fontsize=26,color=GREEN);fig.text(.077,.80,"T = 1; variance 1  - -",fontsize=27,color=PURPLE);fig.text(.077,.17,"U(x) = x²/2; mean zero.",fontsize=27);fig.text(.077,.095,"Each density integrates to one.",fontsize=26,color=GRAY);fig.text(.077,.035,"Stationary does not mean stopped.",fontsize=25,color=GRAY)
    elif key=="energy-density-ratio":
        ax=axes(fig,(.23,.27,.65,.43));du=np.linspace(0,2,300)
        for temp,col,style in [(.25,GREEN,"-"),(1,PURPLE,"--")]:ax.plot(du,np.exp(-du/temp),style,color=col,lw=3);ax.scatter([.5],[np.exp(-.5/temp)],s=70,color=col,zorder=4)
        ax.set(xlim=(0,2.05),ylim=(0,1.1),xlabel="Energy difference ΔU",ylabel="Relative density");ax.set_xticks([0,.5,1,2]);ax.set_yticks([0,.5,1]);ax.axvline(.5,color=GRAY,lw=1,ls=":")
        fig.text(.077,.95,"Same energy gap, different penalty",fontsize=26);fig.text(.077,.865,"T = 0.25: exp(−ΔU/0.25)",fontsize=26,color=GREEN);fig.text(.077,.80,"T = 1: exp(−ΔU)",fontsize=27,color=PURPLE);fig.text(.077,.17,"At ΔU = 0.5: 0.135 versus 0.607",fontsize=25);fig.text(.077,.095,"Ratio p∞(x) / p∞(y).",fontsize=27,color=GRAY);fig.text(.077,.035,"The normalizer cancels in a ratio.",fontsize=25,color=GRAY)
    elif key=="unconfined-window-mass":
        for y,r in [(.57,1),(.19,3)]:
            ax=axes(fig,(.23,y,.65,.22));x=np.linspace(-3.4,3.4,400);ax.plot(x,np.ones_like(x),color=PURPLE,lw=3);ax.fill_between(x,0,1,where=np.abs(x)<=r,color=PURPLE,alpha=.16);ax.set(xlim=(-3.5,3.5),ylim=(0,1.35),xlabel="State x",ylabel="Unnormalized weight");ax.set_xticks([-3,-1,0,1,3]);ax.set_yticks([0,1]);fig.text(.077,y+.245,f"Window [−{r}, {r}]: mass {2*r}",fontsize=28,color=PURPLE)
        fig.text(.077,.955,"Flat energy: infinite total weight",fontsize=25);fig.text(.077,.885,"U = 0 → exp(−U/T) = 1",fontsize=27);fig.text(.077,.075,"Wider window, larger integral.",fontsize=26,color=GRAY);fig.text(.077,.03,"No finite normalizer on all of R.",fontsize=25,color=GRAY)
    elif key=="finite-step-variance-bias":
        ax=axes(fig,(.23,.27,.65,.43));h=np.linspace(.001,1.85,300);ax.plot(h,1/(1-h/2),color=PURPLE,lw=3);ax.axhline(1,color=GREEN,lw=2.5,ls="--");ax.axvline(2,color=AMBER,lw=2,ls=":");ax.scatter([.5,1],[4/3,2],color=PURPLE,s=75,zorder=4);ax.set(xlim=(0,2.12),ylim=(0,14),xlabel="Step size h",ylabel="Stationary variance");ax.set_xticks([0,.5,1,2]);ax.set_yticks([1,2,5,10])
        fig.text(.077,.95,"Finite steps change the variance",fontsize=25);fig.text(.077,.865,"Discrete v = 1 / (1 − h/2)",fontsize=27,color=PURPLE);fig.text(.077,.80,"Continuous variance T = 1 - -",fontsize=26,color=GREEN);fig.text(.077,.17,"h = 0.5: v = 4/3; h = 1: v = 2",fontsize=25);fig.text(.077,.095,"Formula applies only for 0 < h < 2.",fontsize=25,color=AMBER);fig.text(.077,.035,"Bias tends to zero as h → 0.",fontsize=26,color=GRAY)
    elif key=="isotropic-anisotropic-covariance":
        angle=np.linspace(0,2*np.pi,300)
        for y,sds,col,lab in [(.56,(1,1),GREEN,"Covariance I"),(.17,(2,.5),PURPLE,"Covariance diag(4, 0.25)")]:
            ax=axes(fig,(.23,y,.65,.24));ax.set_aspect("equal");ax.plot(sds[0]*np.cos(angle),sds[1]*np.sin(angle),color=col,lw=3);ax.axhline(0,color=GRAY,lw=1);ax.axvline(0,color=GRAY,lw=1);ax.set(xlim=(-2.3,2.3),ylim=(-1.3,1.3),xlabel="Noise coordinate 1",ylabel="Noise coordinate 2");ax.set_xticks([-2,0,2]);ax.set_yticks([-1,0,1]);fig.text(.077,y+.265,lab,fontsize=27,color=col)
        fig.text(.077,.955,"Covariance geometry, not samples",fontsize=25);fig.text(.077,.88,"Illustrative covariance comparison",fontsize=24,color=GRAY);fig.text(.077,.055,"Bottom: coordinate SDs 2 and 0.5.",fontsize=25,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
