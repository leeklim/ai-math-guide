"""Illustrative finite-class risk calculations; no learning experiment."""
import argparse,math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-lrn-01-risk","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect):
    ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def main(output):
    key=output.stem.removeprefix("A09-LRN-01-");h=1350 if key in ["fixed-versus-selected-risk","error-comparison-targets"] else 1020;fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="affine-candidates-selected":
        ax=axes(fig,(.23,.30,.65,.40));x=np.linspace(-1,2,200)
        for w,b in [(-1,0),(0,1),(.3,-.3),(1.3,-.8),(-.5,1.5)]:ax.plot(x,w*x+b,color=GRAY,alpha=.3,lw=1.4)
        ax.plot(x,x,color=PURPLE,lw=3);ax.plot(x,.5*x+1,"--",color=GREEN,lw=3);ax.set(xlim=(-1,2),ylim=(-1.5,2.8),xlabel="Input x",ylabel="Prediction h(x)");ax.set_xticks([-1,0,1,2]);ax.set_yticks([-1,0,1,2])
        fig.text(.077,.95,"A class contains functions",fontsize=28);fig.text(.077,.87,"A: h(x) = x  —",fontsize=28,color=PURPLE);fig.text(.077,.805,"B: h(x) = 0.5x + 1  - -",fontsize=27,color=GREEN);fig.text(.077,.19,"Both selected functions lie in H.",fontsize=25);fig.text(.077,.12,"Gray: more candidate affine functions",fontsize=23,color=GRAY);fig.text(.077,.05,"A few lines do not exhaust the class.",fontsize=24,color=GRAY)
    elif key=="population-label-probability":
        ax=axes(fig,(.23,.30,.65,.40));p=np.linspace(0,1,200);ax.plot(p,p,color=PURPLE,lw=3);ax.plot(p,1-p,"--",color=GREEN,lw=3);ax.set(xlim=(0,1),ylim=(0,1.1),xlabel="Population p = P(Y = 1)",ylabel="Population 0–1 risk");ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1]);ax.scatter([.5],[.5],s=65,color=GRAY,zorder=4)
        fig.text(.077,.95,"Population p changes the ranking",fontsize=25);fig.text(.077,.87,"h₀: risk p  —",fontsize=28,color=PURPLE);fig.text(.077,.805,"h₁: risk 1 − p  - -",fontsize=28,color=GREEN);fig.text(.077,.19,"Sample fraction: 7 / 10",fontsize=28);fig.text(.077,.12,"Observed training risk of h₁: 0.3",fontsize=25);fig.text(.077,.05,"The population p remains unknown.",fontsize=25,color=GRAY)
    elif key=="fixed-versus-selected-risk":
        k=np.arange(11);prob=np.array([math.comb(10,int(i))/2**10 for i in k]);fixed=k/10;selected=np.minimum(k,10-k)/10;mean=np.sum(selected*prob)
        for y,values,lab in [(.56,fixed,"Fixed classifier h₁"),(.17,selected,"Choose best constant per sample")]:
            ax=axes(fig,(.23,y,.65,.23));v=np.unique(values);q=np.array([prob[np.isclose(values,a)].sum() for a in v]);ax.bar(v,q,width=.07,color=BLUE if y==.56 else PURPLE,alpha=.8);ax.set(xlim=(-.08,1.05),ylim=(0,.45),xlabel="Training 0–1 risk",ylabel="Probability");ax.set_xticks([0,.5,1]);ax.set_yticks([0,.2,.4]);ax.axvline(.5 if y==.56 else mean,color=GREEN,lw=2,ls="--");fig.text(.077,y+.28,lab,fontsize=24)
        fig.text(.077,.95,"Selection changes the training mean",fontsize=24);fig.text(.077,.89,"Illustrative: p = 0.5, n = 10",fontsize=28);fig.text(.077,.08,"Fixed mean 0.5; selected mean ≈ 0.377",fontsize=23);fig.text(.077,.035,"Population risk stays 0.5 for both.",fontsize=24,color=GREEN)
    elif key=="error-comparison-targets":
        for y,vals,labels,ttl in [(.56,[.1,.2,.35],["All","H","Chosen"],"Population risk comparisons"),(.17,[.05,.08],["Min.","Actual"],"Training objective comparison")]:
            ax=axes(fig,(.23,y,.65,.23));ax.scatter(vals,np.zeros(len(vals)),s=90,color=PURPLE,zorder=4);ax.set(xlim=(0,.4 if y==.56 else .1),ylim=(-.2,.2),xlabel="Population risk" if y==.56 else "Training objective");ax.set_yticks([]);ax.set_xticks(vals);fig.text(.077,y+.28,ttl,fontsize=25)
            for v,label in zip(vals,labels):ax.text(v,.10,label,fontsize=22,ha="center")
            ax.plot([vals[0],vals[-1]],[0,0],color=GRAY,lw=1.3)
            for left,right in zip(vals[:-1],vals[1:]):ax.annotate("",(right,-.06),(left,-.06),arrowprops=dict(arrowstyle="<->",color=AMBER,lw=2,mutation_scale=11))
        fig.text(.077,.95,"Different errors use different targets",fontsize=23);fig.text(.077,.89,"Illustrative attained minima",fontsize=28);fig.text(.077,.08,"Separate objectives; separate gaps.",fontsize=26);fig.text(.077,.035,"No assumed three-term risk sum.",fontsize=26,color=GRAY)
    elif key=="population-weighted-risk":
        ax=axes(fig,(.23,.30,.65,.40));w=np.linspace(0,1,200);ax.plot(w,.9-.8*w,color=PURPLE,lw=3);ax.scatter([.5,.9],[.5,.18],color=GREEN,s=80,zorder=4);ax.set(xlim=(0,1),ylim=(0,1),xlabel="Population weight w of group A",ylabel="Risk of the same h");ax.set_xticks([0,.5,.9]);ax.set_yticks([0,.5,1])
        fig.text(.077,.95,"Population weights change the mean",fontsize=24);fig.text(.077,.87,"Group mean losses: A 0.1, B 0.9",fontsize=25);fig.text(.077,.805,"R = 0.1w + 0.9(1 − w)",fontsize=28);fig.text(.077,.19,"w = 0.5 → R = 0.5",fontsize=28,color=GREEN);fig.text(.077,.12,"w = 0.9 → R = 0.18",fontsize=28,color=GREEN);fig.text(.077,.05,"The predictor and loss stay fixed.",fontsize=25,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
