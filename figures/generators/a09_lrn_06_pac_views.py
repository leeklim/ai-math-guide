"""Finite-class PAC sufficient bounds and explicitly illustrative training law."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-lrn-06-pac","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,box):
    ax=fig.add_axes(box,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def log_axis(ax,which,ticks,labels):
    if which=="x":ax.set_xscale("log");ax.set_xticks(ticks,labels);ax.xaxis.set_minor_locator(NullLocator())
    else:ax.set_yscale("log");ax.set_yticks(ticks,labels);ax.yaxis.set_minor_locator(NullLocator())
def main(output):
    key=output.stem.removeprefix("A09-LRN-06-");h=1400 if key in ["risk-target-realizable-agnostic","same-input-label-noise","sample-bound-delta"] else 1100;fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="risk-target-realizable-agnostic":
        for y,best,label in [(.56,0.,"Realizable: best risk 0"),(.18,.12,"Agnostic: best risk 0.12")]:
            ax=axes(fig,(.23,y,.65,.21));ax.axhline(0,color=GRAY,lw=1);ax.scatter([best],[0],s=100,color=BLUE,zorder=4);ax.scatter([best+.03],[0],s=100,color=GREEN,marker="s",zorder=4);ax.annotate("",(best+.03,.3),(best,.3),arrowprops=dict(arrowstyle="<->",color=PURPLE,lw=2,mutation_scale=10,shrinkA=0,shrinkB=0));ax.text(best+.015,.55,"ε = 0.03",color=PURPLE,ha="center",fontsize=26);ax.set(xlim=(-.015,.18),ylim=(-.6,1),xlabel="Population risk");ax.set_xticks([0,.06,.12,.18]);ax.set_yticks([]);ax.spines["left"].set_visible(False);fig.text(.077,y+.26,label,fontsize=28)
        fig.text(.077,.96,"Same tolerance; different target risk",fontsize=24);fig.text(.077,.90,"Blue: class best; green: allowed limit",fontsize=23);fig.text(.077,.08,"Limits: 0.03 versus 0.15",fontsize=28);fig.text(.077,.035,"ε is excess risk, not absolute risk.",fontsize=24,color=GRAY)
    elif key=="same-input-label-noise":
        for y,pred in [(.56,0),(.18,1)]:
            ax=axes(fig,(.23,y,.65,.21));ax.bar([0,1],[.7,.3],color=[BLUE,AMBER],alpha=.8)
            bad=1-pred;ax.bar([bad],[.3 if bad else .7],facecolor="none",edgecolor=PURPLE,hatch="///",lw=2);ax.set(ylim=(0,.85),xlabel="Random label at the same x",ylabel="Population probability");ax.set_xticks([0,1],["0","1"]);ax.set_yticks([0,.3,.7]);fig.text(.077,y+.26,"Always predict "+str(pred)+": risk "+("0.3" if pred==0 else "0.7"),fontsize=27)
        fig.text(.077,.96,"One x; stochastic labels",fontsize=28);fig.text(.077,.90,"Hatching marks the error mass.",fontsize=26,color=PURPLE);fig.text(.077,.08,"Neither deterministic choice has risk 0.",fontsize=22);fig.text(.077,.035,"Illustrative P(Y = 1 | x) = 0.3",fontsize=26,color=GRAY)
    elif key=="bad-hypothesis-consistency-bound":
        ax=axes(fig,(.23,.29,.65,.44));n=np.arange(1,101);ax.plot(n,.88**n,color=BLUE,lw=2);ax.plot(n,np.minimum(1,10*np.exp(-.1*n)),color=PURPLE,lw=2,ls="--");ax.axhline(.05,color=AMBER,ls=":",lw=2);ax.axvline(53,color=GRAY,ls=":",lw=1.5);ax.set(xlim=(0,100),ylim=(0,1.05),xlabel="Training sample count n",ylabel="Probability or upper bound");ax.set_xticks([0,25,53,100]);ax.set_yticks([0,.25,.5,.75,1])
        fig.text(.077,.95,"A bad h may fit a finite sample",fontsize=25);fig.text(.077,.87,"One h: risk 0.12 → 0.88ⁿ",fontsize=27,color=BLUE);fig.text(.077,.80,"N = 10: min(1, 10e⁻⁰·¹ⁿ)  - -",fontsize=26,color=PURPLE);fig.text(.077,.16,"ε = 0.10; δ = 0.05; sufficient n = 53",fontsize=22);fig.text(.077,.10,"The union bound need not be tight.",fontsize=24);fig.text(.077,.05,"Union bound: no independence needed.",fontsize=24,color=GRAY)
    elif key=="sample-bound-epsilon":
        ax=axes(fig,(.23,.29,.65,.44));e=np.geomspace(.025,.5,300);r=np.ceil(np.log(200)/e);a=np.ceil(2*np.log(400)/e**2);ax.plot(e,r,color=BLUE,lw=2);ax.plot(e,a,color=PURPLE,lw=2,ls="--");log_axis(ax,"x",[.025,.1,.5],["0.025","0.1","0.5"]);log_axis(ax,"y",[10,100,1000,10000],["10","100","1000","10000"]);ax.set(xlim=(.025,.5),ylim=(10,25000),xlabel="Tolerance ε",ylabel="Sufficient sample ceiling")
        fig.text(.077,.95,"Fix class size N = 10; δ = 0.05",fontsize=25);fig.text(.077,.87,"Realizable: log(200) / ε  —",fontsize=26,color=BLUE);fig.text(.077,.80,"Agnostic: 2log(400) / ε²  - -",fontsize=25,color=PURPLE);fig.text(.077,.16,"At ε = 0.10: 53 versus 1,199",fontsize=27);fig.text(.077,.10,"Integer sample counts round up.",fontsize=26);fig.text(.077,.05,"Sufficient bounds, not exact minima.",fontsize=24,color=GRAY)
    elif key=="sample-bound-delta":
        d=np.geomspace(.001,.2,300)
        for y,real in [(.56,True),(.18,False)]:
            ax=axes(fig,(.23,y,.65,.21));v=np.ceil(np.log(10/d)/.1) if real else np.ceil(2*np.log(20/d)/.01);ax.plot(d,v,color=BLUE if real else PURPLE,lw=2,ls="-" if real else "--");log_axis(ax,"x",[.001,.01,.1],["0.001","0.01","0.1"]);ax.set(xlim=(.001,.2),xlabel="Failure target δ",ylabel="Sufficient n");ax.set_yticks([40,60,80,100] if real else [1000,1500,2000]);fig.text(.077,y+.26,"Realizable" if real else "Agnostic",fontsize=28)
        fig.text(.077,.96,"Fix N = 10; ε = 0.10",fontsize=28);fig.text(.077,.90,"Lower δ means higher confidence.",fontsize=25);fig.text(.077,.08,"Each panel has its own n scale.",fontsize=26);fig.text(.077,.035,"These are sufficient integer ceilings.",fontsize=23,color=GRAY)
    elif key=="ninety-five-percent-training-law":
        ax=axes(fig,(.23,.29,.65,.44));x=np.arange(1,21);r=np.r_[np.linspace(.121,.139,19),.22];ax.scatter(x[:19],r[:19],s=35,color=GREEN,zorder=4);ax.scatter(x[19:],r[19:],s=90,color=AMBER,marker="s",zorder=4);ax.axhline(.15,color=PURPLE,lw=2,ls="--");ax.axhline(.12,color=GRAY,lw=1.5,ls=":");ax.set(xlim=(0,21),ylim=(.10,.25),xlabel="Training outcome",ylabel="Population risk of trained h");ax.set_xticks([1,10,20]);ax.set_yticks([.12,.15,.20,.25])
        fig.text(.077,.95,"An illustrative repeated-training law",fontsize=24);fig.text(.077,.87,"Class best 0.12; ε = 0.03",fontsize=28);fig.text(.077,.80,"Pass threshold: risk ≤ 0.15",fontsize=27,color=PURPLE);fig.text(.077,.16,"20 equally likely outcomes; 19 pass",fontsize=23);fig.text(.077,.10,"Passing probability = 19/20 = 95%",fontsize=24);fig.text(.077,.05,"Not 20 measured runs; not accuracy 95%.",fontsize=22,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
