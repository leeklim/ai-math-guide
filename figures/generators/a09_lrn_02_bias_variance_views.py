"""Exact finite illustrative bias/variance constructions at a fixed input."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-lrn-02-bias","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect):
    ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def main(output):
    key=output.stem.removeprefix("A09-LRN-02-");h=1350 if key=="prediction-and-label-centers" else 1020;fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="prediction-and-label-centers":
        for y,vals,center,ttl,col in [(.56,[-1,3],1,"Dataset-trained predictions",PURPLE),(.17,[-np.sqrt(2),np.sqrt(2)],0,"Independent new labels",AMBER)]:
            ax=axes(fig,(.23,y,.65,.23));ax.scatter(vals,[0,0],s=90,color=col,zorder=4);ax.axvline(center,color=GREEN,lw=1.7,ls="--");ax.scatter([center],[0],marker="|",s=600,color=GREEN,lw=2,zorder=5);ax.set(xlim=(-2,4),ylim=(-.3,.3),xlabel="Prediction value" if y==.56 else "Label value");ax.set_yticks([]);ax.set_xticks([-1,0,1,3] if y==.56 else [-np.sqrt(2),0,np.sqrt(2)],None if y==.56 else ["−√2","0","+√2"]);fig.text(.077,y+.28,ttl,fontsize=25)
            ax.annotate("",(vals[1],.12),(center,.12),arrowprops=dict(arrowstyle="<->",color=col,lw=2,mutation_scale=11))
            if y==.56:ax.annotate("",(1,-.13),(0,-.13),arrowprops=dict(arrowstyle="<->",color=GRAY,lw=2,mutation_scale=11))
        fig.text(.077,.95,"Bias and variance use different centers",fontsize=23);fig.text(.077,.89,"Fixed x: target f* = 0, mean f̄ = 1",fontsize=25);fig.text(.077,.08,"Predictor variance 4; label variance 2",fontsize=24);fig.text(.077,.035,"Bias = 1 − 0 = 1",fontsize=28,color=GREEN)
    elif key=="single-errors-and-mean":
        a=np.array([-1.,3.]);noise=np.array([-np.sqrt(2),np.sqrt(2)]);errors=(a[:,None]-noise[None,:])**2;ax=axes(fig,(.23,.30,.65,.40));ax.bar(range(4),errors.ravel(),color=PURPLE,alpha=.8);ax.axhline(7,color=GREEN,lw=2,ls="--");ax.set(xlim=(-.6,3.6),ylim=(0,22),xlabel="Dataset and label combination",ylabel="Squared prediction error");ax.set_xticks(range(4),["D₁−","D₁+","D₂−","D₂+"]);ax.set_yticks([0,7,14,21])
        fig.text(.077,.95,"Four outcomes; one expectation",fontsize=26);fig.text(.077,.87,"Prediction: D₁ −1, D₂ 3",fontsize=27);fig.text(.077,.805,"Independent labels: −√2, +√2",fontsize=27);fig.text(.077,.19,"Each combination has probability 1/4.",fontsize=24);fig.text(.077,.12,"Mean squared error = 7  - -",fontsize=27,color=GREEN);fig.text(.077,.05,"The four individual errors differ.",fontsize=25,color=GRAY)
    elif key=="expected-error-components":
        ax=axes(fig,(.16,.37,.75,.30));left=0
        for value,col in [(1,PURPLE),(4,BLUE),(2,AMBER)]:ax.barh([0],[value],left=left,color=col,height=.5);left+=value
        ax.set(xlim=(0,7.2),ylim=(-.9,.9),xlabel="Expected squared-error units");ax.set_xticks([0,1,5,7]);ax.set_yticks([]);ax.text(.5,0,"1",color="white",ha="center",va="center",fontsize=28);ax.text(3,0,"4",color="white",ha="center",va="center",fontsize=28);ax.text(6,0,"2",color="white",ha="center",va="center",fontsize=28)
        fig.text(.077,.95,"Add three squared-error terms",fontsize=26);fig.text(.077,.87,"Bias² = 1",fontsize=28,color=PURPLE);fig.text(.077,.805,"Predictor variance = 4",fontsize=28,color=BLUE);fig.text(.077,.74,"Noise variance = 2",fontsize=28,color=AMBER);fig.text(.077,.19,"1 + 4 + 2 = 7",fontsize=30,color=GREEN);fig.text(.077,.12,"Variance already averages squares.",fontsize=25);fig.text(.077,.05,"Do not square the variance again.",fontsize=25,color=GRAY)
    elif key in ["represented-target-biased-selection","pointwise-zero-global-mismatch"]:
        x=np.linspace(-2,2,250);target=x if key=="represented-target-biased-selection" else x*x;mean=.5*x if key=="represented-target-biased-selection" else np.zeros_like(x);ax=axes(fig,(.23,.30,.65,.40));ax.plot(x,target,color=BLUE,lw=3);ax.plot(x,mean,"--",color=PURPLE,lw=3);ax.set(xlim=(-2,2),ylim=(-2.3,2.3) if key=="represented-target-biased-selection" else (-.3,4.5),xlabel="Input x",ylabel="Prediction");ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2] if key=="represented-target-biased-selection" else [0,2,4]);ax.scatter([0],[0],color=GREEN,s=80,zorder=5)
        fig.text(.077,.95,"A representable target can have bias" if key=="represented-target-biased-selection" else "One correct point is not a global fit",fontsize=24);fig.text(.077,.87,"Target f*(x) = x  —" if key=="represented-target-biased-selection" else "Target f*(x) = x²  —",fontsize=28,color=BLUE);fig.text(.077,.805,"Mean f̄(x) = 0.5x  - -" if key=="represented-target-biased-selection" else "Mean f̄(x) = 0  - -",fontsize=28,color=PURPLE);fig.text(.077,.19,"H contains x; the mean still differs." if key=="represented-target-biased-selection" else "Bias at x = 0 is zero.",fontsize=24);fig.text(.077,.12,"Bias at x = 2: 1 − 2 = −1" if key=="represented-target-biased-selection" else "Bias at x = 2: 0 − 4 = −4",fontsize=27,color=PURPLE);fig.text(.077,.05,"Illustrative selection, not a theorem." if key=="represented-target-biased-selection" else "Affine H cannot express x² globally.",fontsize=24,color=GRAY)
    elif key=="data-seed-nested-variation":
        ax=axes(fig,(.23,.30,.65,.40));ax.scatter([0,0,1,1],[-2,0,2,4],s=90,color=BLUE,zorder=4);ax.scatter([0,1],[-1,3],marker="_",s=600,color=PURPLE,lw=3,zorder=5);ax.axhline(1,color=GREEN,lw=2,ls="--");ax.plot([0,0],[-2,0],color=GRAY,lw=1.5);ax.plot([1,1],[2,4],color=GRAY,lw=1.5);ax.set(xlim=(-.4,1.4),ylim=(-2.8,4.8),ylabel="Prediction at fixed x");ax.set_xticks([0,1],["Dataset D₁","Dataset D₂"]);ax.set_yticks([-2,0,1,3,4])
        fig.text(.077,.95,"Separate data and seed repetition",fontsize=25);fig.text(.077,.87,"Dots: two seed outcomes per dataset",fontsize=24,color=BLUE);fig.text(.077,.805,"Bars: seed means −1, 3",fontsize=27,color=PURPLE);fig.text(.077,.19,"Within-data variance 1",fontsize=28);fig.text(.077,.12,"Variance of data means 4",fontsize=27);fig.text(.077,.05,"Total variance 5; grand mean 1.",fontsize=26,color=GREEN)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
