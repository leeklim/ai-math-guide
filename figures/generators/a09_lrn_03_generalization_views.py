"""Exact finite and binomial illustrations for generalization measurements."""
import argparse,math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-lrn-03-gap","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect):
    ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def main(output):
    key=output.stem.removeprefix("A09-LRN-03-");h=1350 if key in ["conditional-test-sampling","paired-example-differences","same-and-shifted-populations"] else 1020;fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="retraining-versus-observed-gaps":
        ax=axes(fig,(.23,.30,.65,.40));x=np.arange(4);true=np.array([.10,.05,.05,.05]);obs=np.array([.14,0,.07,.04]);ax.scatter(x,true,s=90,color=PURPLE,zorder=5);ax.scatter(x,obs,s=95,facecolors=BG,edgecolors=AMBER,lw=2,zorder=5)
        for i in x:ax.plot([i,i],[true[i],obs[i]],color=GRAY,lw=1.5)
        ax.axhline(true.mean(),color=GREEN,lw=2,ls="--");ax.set(xlim=(-.4,3.4),ylim=(-.02,.16),xlabel="Training outcome S");ax.set_xticks(x,["S₁","S₂","S₃","S₄"]);ax.set_yticks([0,.05,.10,.15]);ax.set_ylabel("Generalization gap")
        fig.text(.077,.95,"Training repetition and test noise",fontsize=25);fig.text(.077,.87,"Filled: population − train",fontsize=26,color=PURPLE);fig.text(.077,.805,"Hollow: finite test − train",fontsize=26,color=AMBER);fig.text(.077,.19,"Four equally likely outcomes",fontsize=26);fig.text(.077,.12,"Expected gap = 0.0625  - -",fontsize=27,color=GREEN);fig.text(.077,.05,"Test sampling changes observed gaps.",fontsize=24,color=GRAY)
    elif key=="risk-level-versus-gap":
        ax=axes(fig,(.23,.30,.65,.40));q=np.linspace(0,.5,200);ax.plot(q,q,color=GRAY,ls="--",lw=2)
        for x,y,col,mark in [(.1,.16,PURPLE,"o"),(.45,.45,AMBER,"s"),(.25,.20,BLUE,"^")]:ax.scatter([x],[y],s=90,color=col,marker=mark,zorder=5)
        ax.plot([.1,.1],[.1,.16],color=PURPLE,lw=2);ax.set(xlim=(0,.5),ylim=(0,.5),xlabel="Observed train error",ylabel="Observed test error");ax.set_xticks([0,.25,.5]);ax.set_yticks([0,.25,.5])
        fig.text(.077,.95,"Risk level differs from gap",fontsize=28);fig.text(.077,.87,"Circle: (0.10, 0.16), gap +0.06",fontsize=25,color=PURPLE);fig.text(.077,.805,"Square: (0.45, 0.45), gap 0",fontsize=25,color=AMBER);fig.text(.077,.19,"Triangle: (0.25, 0.20), gap −0.05",fontsize=25,color=BLUE);fig.text(.077,.12,"Dashed line: zero observed gap",fontsize=26);fig.text(.077,.05,"Small gap alone is not low risk.",fontsize=25,color=GRAY)
    elif key=="conditional-test-sampling":
        for y,n in [(.56,25),(.17,400)]:
            k=np.arange(n+1);prob=np.array([math.comb(n,int(i))*.16**int(i)*.84**(n-int(i)) for i in k]);ax=axes(fig,(.23,y,.65,.23));ax.bar(k/n-.1,prob,width=.8/n,color=BLUE,alpha=.8);ax.axvline(.06,color=GREEN,ls="--",lw=2);ax.set(xlim=(-.11,.28),xlabel="Observed test − train gap",ylabel="Probability");ax.set_xticks([-.1,0,.1,.2]);ax.set_yticks([0,.1,.2] if n==25 else [0,.02,.04]);fig.text(.077,y+.28,"Independent test count m = "+str(n),fontsize=24)
        fig.text(.077,.95,"Test noise conditional on fixed h",fontsize=25);fig.text(.077,.89,"Fixed true p = 0.16; train 0.10",fontsize=24);fig.text(.077,.08,"Both distributions center at gap 0.06.",fontsize=24);fig.text(.077,.035,"Retraining variation is excluded.",fontsize=25,color=GRAY)
    elif key=="validation-minimum-selection":
        ax=axes(fig,(.23,.30,.65,.40));v=np.array([.23,.18,.11,.25]);ax.bar(range(4),v,color=BLUE,alpha=.8);ax.axhline(.2,color=GREEN,lw=2,ls="--");ax.scatter([2],[.11],s=200,facecolors=BG,edgecolors=AMBER,lw=2.5,zorder=5);ax.set(xlim=(-.6,3.6),ylim=(0,.31),xlabel="Candidate predictor",ylabel="0–1 risk");ax.set_xticks(range(4),["A","B","C","D"]);ax.set_yticks([0,.1,.2,.3])
        fig.text(.077,.95,"A validation minimum includes noise",fontsize=24);fig.text(.077,.87,"Illustrative equal true risks: 0.20",fontsize=25,color=GREEN);fig.text(.077,.805,"Bars: observed validation error",fontsize=26,color=BLUE);fig.text(.077,.19,"Minimum selects C with 0.11.",fontsize=27,color=AMBER);fig.text(.077,.12,"C still has population risk 0.20.",fontsize=26);fig.text(.077,.05,"Use new test data after selection.",fontsize=25,color=GRAY)
    elif key=="same-and-shifted-populations":
        for y,mode in [(.56,"weights"),(.17,"risk")]:
            ax=axes(fig,(.23,y,.65,.23))
            if mode=="weights":
                w=np.array([.9,.9,.2]);ax.bar(range(3),w,color=BLUE,alpha=.8);ax.bar(range(3),1-w,bottom=w,color=AMBER,alpha=.8);ax.set(ylim=(0,1.1),ylabel="Population mass");ax.set_yticks([0,.5,1])
            else:
                ax.bar(range(3),[.18,.18,.74],color=PURPLE,alpha=.8);ax.set(ylim=(0,1),ylabel="Risk of fixed h");ax.set_yticks([0,.5,1])
            ax.set_xticks(range(3),["Source P","Same P","Shift Q"]);fig.text(.077,y+.28,"Group A blue; group B orange" if mode=="weights" else "Same loss and predictor",fontsize=24)
        fig.text(.077,.95,"A shifted test changes the target",fontsize=26);fig.text(.077,.89,"Group errors: A 0.1, B 0.9",fontsize=27);fig.text(.077,.08,"Population risks: 0.18, 0.18, 0.74",fontsize=24);fig.text(.077,.035,"This is not an observed iid gap.",fontsize=25,color=GRAY)
    elif key=="paired-example-differences":
        a=np.array([.1,.4,.9]);b=a+.1
        ax=axes(fig,(.23,.56,.65,.23));ax.plot(range(3),a,"o-",color=PURPLE,lw=2);ax.plot(range(3),b,"s--",color=GREEN,lw=2);ax.set(xlim=(-.2,2.2),ylim=(0,1.1),xlabel="Same test example",ylabel="Loss");ax.set_xticks(range(3),["1","2","3"]);ax.set_yticks([0,.5,1])
        for i in range(3):ax.plot([i,i],[a[i],b[i]],color=GRAY,lw=1.4)
        bx=axes(fig,(.23,.17,.65,.23));vals=(a[:,None]-b[None,:]).ravel();v=np.unique(np.round(vals,8));q=np.array([np.isclose(vals,x).mean() for x in v]);bx.bar(v,q,width=.06,color=AMBER,alpha=.8);bx.axvline(-.1,color=GREEN,lw=2,ls="--");bx.set(xlim=(-1,.8),ylim=(0,.4),xlabel="Independently mixed A − B",ylabel="Probability");bx.set_xticks([-.9,-.1,.7]);bx.set_yticks([0,.2,.4])
        fig.text(.077,.95,"Pair the common example difficulty",fontsize=25);fig.text(.077,.89,"A circle; B square; illustrative losses",fontsize=22);fig.text(.077,.08,"Paired differences: −0.1, −0.1, −0.1",fontsize=24,color=GREEN);fig.text(.077,.035,"Precision gain depends on the data.",fontsize=24,color=GRAY)
    elif key=="gap-difference-training-adjustment":
        ax=axes(fig,(.23,.30,.65,.40));train=np.array([.1,.12]);test=np.array([.16,.15]);ax.scatter([0,1],train,s=100,color=BLUE,zorder=4);ax.scatter([0,1],test,s=100,color=GREEN,marker="s",zorder=4)
        for i in range(2):ax.annotate("",(i,test[i]),(i,train[i]),arrowprops=dict(arrowstyle="<->",color=PURPLE,lw=2.5,mutation_scale=11))
        ax.set(xlim=(-.4,1.4),ylim=(.08,.18),ylabel="Observed 0–1 error");ax.set_xticks([0,1],["Probe A","Probe B"]);ax.set_yticks([.1,.12,.15,.16]);fig.text(.077,.95,"A gap difference subtracts train change",fontsize=23);fig.text(.077,.87,"Train circle; test square",fontsize=28);fig.text(.077,.805,"A gap 0.06; B gap 0.03",fontsize=28);fig.text(.077,.19,"Test difference = 0.01",fontsize=28);fig.text(.077,.12,"Train difference = −0.02",fontsize=28);fig.text(.077,.05,"Gap difference = 0.01 − (−0.02) = 0.03",fontsize=23,color=PURPLE)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
