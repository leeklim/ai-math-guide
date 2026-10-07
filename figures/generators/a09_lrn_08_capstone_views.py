"""Small illustrative contract calculations; no probe/model execution."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-lrn-08-capstone","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,box):
    ax=fig.add_axes(box,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def main(output):
    key=output.stem.removeprefix("A09-LRN-08-");fig=plt.figure(figsize=(520/72,1100/72),facecolor=BG)
    if key=="norm-class-subset-not-universal-ladder":
        ax=axes(fig,(.23,.29,.65,.44));t=np.linspace(0,2*np.pi,300);ax.fill(np.cos(t),np.sin(t),color=PURPLE,alpha=.16);ax.plot(np.cos(t),np.sin(t),color=PURPLE,lw=2);ax.scatter([.3,1.5],[.4,.5],s=90,color=[PURPLE,BLUE],marker="o",zorder=5);ax.set_aspect("equal");ax.set(xlim=(-2,2),ylim=(-2,2),xlabel="Weight w₁",ylabel="Weight w₂");ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2])
        fig.text(.077,.95,"Linear weights with and without a norm",fontsize=23);fig.text(.077,.87,"Same feature map and intercept rules",fontsize=23);fig.text(.077,.80,"Bounded disk: ‖w‖₂ ≤ 1",fontsize=28,color=PURPLE);fig.text(.077,.16,"Full plane: norm-unconstrained linear",fontsize=23,color=BLUE);fig.text(.077,.10,"Constant and MLP need separate contracts.",fontsize=22);fig.text(.077,.05,"Do not assume one universal class ladder.",fontsize=22,color=GRAY)
    elif key=="iid-gap-versus-shift-contrast":
        ax=axes(fig,(.30,.29,.58,.44));risk=np.array([.1,.14,.25]);ax.scatter(risk,[2,1,0],s=110,color=[BLUE,GREEN,AMBER],marker="s",zorder=4);ax.axvline(.1,color=BLUE,ls=":",lw=1.5);ax.set(xlim=(0,.30),ylim=(-.8,2.6),xlabel="Observed evaluation risk");ax.set_xticks([0,.1,.2,.3]);ax.set_yticks([0,1,2],["Shift test","IID test","Train"]);ax.annotate("",(.14,.7),(.1,.7),arrowprops=dict(arrowstyle="<->",color=PURPLE,lw=2,mutation_scale=10,shrinkA=0,shrinkB=0));ax.annotate("",(.25,-.3),(.1,-.3),arrowprops=dict(arrowstyle="<->",color=GRAY,lw=2,mutation_scale=10,shrinkA=0,shrinkB=0))
        fig.text(.077,.95,"One fixed c; same evaluation loss",fontsize=25);fig.text(.077,.87,"Illustrative risks: 0.10, 0.14, 0.25",fontsize=24);fig.text(.077,.80,"IID contrast: Gc = 0.04",fontsize=28,color=PURPLE);fig.text(.077,.16,"Shift − train = 0.15",fontsize=28,color=GRAY);fig.text(.077,.10,"The shift contrast is not the same Gc.",fontsize=23);fig.text(.077,.05,"No probe scores were generated.",fontsize=26,color=GRAY)
    elif key=="loose-bound-observed-gap":
        ax=axes(fig,(.23,.29,.65,.44));ax.axhspan(-.08,.08,xmin=0,xmax=.8,color=GREEN,alpha=.16);ax.axhline(0,color=GRAY,lw=1);ax.scatter([.04],[0],s=100,color=PURPLE,zorder=4);ax.axvline(.8,color=GREEN,ls="--",lw=2);ax.set(xlim=(0,1),ylim=(-.6,.8),xlabel="Nonnegative gap magnitude");ax.set_xticks([0,.2,.4,.6,.8,1]);ax.set_yticks([]);ax.spines["left"].set_visible(False)
        fig.text(.077,.95,"Observed gap 0.04  ○",fontsize=28,color=PURPLE);fig.text(.077,.87,"Theoretical upper limit 0.8  - -",fontsize=27,color=GREEN);fig.text(.077,.80,"Read both on the same axis.",fontsize=27);fig.text(.077,.16,"0.04 ≤ 0.8 is not a contradiction.",fontsize=25);fig.text(.077,.10,"It does not show a tight bound.",fontsize=26);fig.text(.077,.05,"It does not prove a new-population claim.",fontsize=22,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
