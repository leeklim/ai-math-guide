"""Draw illustrative checkpoint measurement contrasts; no model runs."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-dyn-08-measurement","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect):
    ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def main(output):
    key=output.stem.removeprefix("A09-DYN-08-");h=1600 if key in ["time-coordinate-spacing","dense-observed-checkpoints"] else 1350 if key in ["projected-update-covariance","time-order-shuffle"] else 1020;fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="time-coordinate-spacing":
        for y,x,label,ttl,rate in [(.68,[0,1,2],"Optimizer step","Equal step intervals","Rates: 1, 1 per step"),(.39,[0,100,300],"Processed tokens","Unequal token intervals","Rates: 0.01, 0.005 per token"),(.10,[0,.1,.15],"Cumulative learning rate","Unequal summed LR intervals","Rates: 10, 20 per LR unit")]:
            ax=axes(fig,(.23,y,.65,.16));ax.plot(x,[0,1,2],color=GRAY,ls="--",lw=1.6);ax.scatter(x,[0,1,2],s=85,color=BLUE,zorder=4);ax.set(xlabel=label,ylabel="Observed z",ylim=(-.15,2.25));ax.set_xticks(x);ax.set_yticks([0,1,2]);fig.text(.077,y+.20,ttl,fontsize=27);fig.text(.077,y-.064,rate,fontsize=24,color=PURPLE)
        fig.text(.077,.95,"Same displacements; different clocks",fontsize=24);fig.text(.077,.915,"Illustrative: each interval Δz = 1",fontsize=26)
    elif key=="hidden-moment-state":
        ax=axes(fig,(.23,.30,.65,.40));ax.set(xlim=(-.15,.15),ylim=(-1.45,1.45),xlabel="Observed parameter θ",ylabel="Hidden moment v");ax.set_xticks([-.1,0,.1]);ax.set_yticks([-1,0,1]);ax.axvline(0,color=GRAY,lw=1.2)
        for v,col,mark in [(1,PURPLE,"o"),(-1,GREEN,"s")]:
            ax.scatter([0],[v],s=80,color=BLUE,zorder=4);ax.annotate("",(-.09*v,.9*v),(0,v),arrowprops=dict(arrowstyle="->",color=col,lw=2.6,mutation_scale=13));ax.scatter([-.09*v],[.9*v],s=60,color=col,marker=mark,zorder=4)
        fig.text(.077,.95,"A summary can hide optimizer state",fontsize=24);fig.text(.077,.87,"Illustrative: v′ = 0.9v, gradient 0",fontsize=25);fig.text(.077,.805,"θ′ = θ − 0.1v′; start θ = 0",fontsize=27);fig.text(.077,.19,"v = +1 → next θ = −0.09",fontsize=26,color=PURPLE);fig.text(.077,.12,"v = −1 → next θ = +0.09",fontsize=26,color=GREEN);fig.text(.077,.05,"Same z = θ; different next states.",fontsize=24,color=GRAY)
    elif key=="projected-update-covariance":
        cov=.01*np.array([[4.,1.],[1.,1.]]);ang=np.linspace(0,2*np.pi,300);ell=np.linalg.cholesky(cov)@np.array([np.cos(ang),np.sin(ang)]);a=np.array([1.,1.]);sd=np.sqrt(a@cov@a);ext=cov@a/sd
        ax=axes(fig,(.23,.55,.65,.28));ax.plot(ell[0],ell[1],color=PURPLE,lw=3);ax.scatter([ext[0],-ext[0]],[ext[1],-ext[1]],color=GREEN,s=75,zorder=4);ax.set(xlim=(-.25,.25),ylim=(-.15,.15),xlabel="Update Δθ₁",ylabel="Update Δθ₂");ax.set_xticks([-.2,0,.2]);ax.set_yticks([-.1,0,.1])
        bx=axes(fig,(.23,.20,.65,.15));bx.plot([-sd,sd],[0,0],color=GREEN,lw=5);bx.scatter([-sd,sd],[0,0],s=80,color=GREEN);bx.set(xlim=(-.36,.36),ylim=(-.2,.2),xlabel="Summary Δz = Δθ₁ + Δθ₂");bx.set_yticks([]);bx.set_xticks([-sd,0,sd],["−0.265","0","0.265"])
        fig.text(.077,.95,"Project an update covariance",fontsize=27);fig.text(.077,.90,"C = [[4, 1], [1, 1]], η = 0.1",fontsize=25);fig.text(.077,.855,"Update covariance = 0.01C",fontsize=26,color=PURPLE);fig.text(.077,.41,"A = (1, 1): variance 0.07",fontsize=26,color=GREEN);fig.text(.077,.09,"Covariance-ellipse extrema: ±√0.07",fontsize=24);fig.text(.077,.045,"Covariance scales; no probability bound.",fontsize=22,color=GRAY)
    elif key=="one-direction-jvp":
        ax=axes(fig,(.23,.30,.65,.40));ax.set(xlim=(-.12,1.25),ylim=(-.12,1.25),xlabel="First component",ylabel="Second component");ax.set_xticks([0,1]);ax.set_yticks([0,1])
        for end,col,style in [((0,1),BLUE,"--"),((1,0),BLUE,"--"),((0,.6),PURPLE,"-"),((.9,0),GREEN,"-")]:
            ax.annotate("",end,(0,0),arrowprops=dict(arrowstyle="->",color=col,lw=2.6,linestyle=style,mutation_scale=13))
        ax.text(.10,.98,"e₂",color=BLUE,fontsize=28);ax.text(.10,.56,"0.6e₂",color=PURPLE,fontsize=26);ax.text(.91,.10,"e₁",color=BLUE,fontsize=28);ax.text(.60,.22,"0.9e₁",color=GREEN,fontsize=26)
        fig.text(.077,.95,"One JVP checks one direction",fontsize=27);fig.text(.077,.87,"H = diag(1, 4), η = 0.1",fontsize=27);fig.text(.077,.805,"J = I − ηH = diag(0.9, 0.6)",fontsize=25);fig.text(.077,.19,"Measured: J e₂ = 0.6e₂",fontsize=27,color=PURPLE);fig.text(.077,.12,"Other: J e₁ = 0.9e₁",fontsize=27,color=GREEN);fig.text(.077,.05,"The leading multiplier is 0.9 here.",fontsize=24,color=GRAY)
    elif key=="dense-observed-checkpoints":
        for y,ttl,mode in [(.68,"Sparse observed checkpoints","sparse"),(.39,"Added interpolation points","interp"),(.10,"Added observed checkpoints","dense")]:
            ax=axes(fig,(.23,y,.65,.16));ax.set(xlim=(-1,21),ylim=(.4,1),xlabel="Optimizer step",ylabel="Metric");ax.set_xticks([0,10,20]);ax.set_yticks([.5,.9]);ax.plot([0,10,20],[.5,.5,.9],ls="--",color=GRAY,lw=1.4);ax.scatter([0,10,20],[.5,.5,.9],s=85,color=BLUE,zorder=5)
            if mode=="interp":ax.scatter([12,14,16,18],[.58,.66,.74,.82],s=90,facecolors=BG,edgecolors=AMBER,lw=2,zorder=4)
            if mode=="dense":
                ax.axvspan(14,15,color=GREEN,alpha=.16);ax.scatter([14,15],[.5,.9],s=85,color=GREEN,zorder=5)
            else:ax.axvspan(10,20,color=AMBER,alpha=.08)
            fig.text(.077,y+.20,ttl,fontsize=26);fig.text(.077,y-.064,"Candidate (14, 15]" if mode=="dense" else "Candidate (10, 20] stays unresolved",fontsize=24,color=GREEN if mode=="dense" else AMBER)
        fig.text(.077,.95,"Observations determine resolution",fontsize=26);fig.text(.077,.915,"Illustrative values, not a model run",fontsize=24)
    elif key=="time-order-shuffle":
        for y,vals,ttl,col in [(.55,[.5,.5,.5,.9,.9,.9],"Original order",BLUE),(.17,[.9,.5,.9,.5,.9,.5],"Reordered control",AMBER)]:
            ax=axes(fig,(.23,y,.65,.23));ax.plot(range(6),vals,color=col,lw=2);ax.scatter(range(6),vals,color=col,s=80,zorder=4);ax.set(xlim=(-.25,5.25),ylim=(.4,1),xlabel="Recorded position",ylabel="Metric");ax.set_xticks([0,2,4]);ax.set_yticks([.5,.9]);fig.text(.077,y+.27,ttl,fontsize=28,color=col)
        fig.text(.077,.95,"Shuffle changes time order",fontsize=28);fig.text(.077,.90,"Same three low and three high values",fontsize=24);fig.text(.077,.08,"Order contrast needs a stated purpose.",fontsize=23);fig.text(.077,.035,"A valid test null needs extra assumptions.",fontsize=22,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
