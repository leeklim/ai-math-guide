"""Reproduce N05-04 activation values, derivatives and composition curves."""
import argparse, math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
BLUE,PURPLE,GREEN,ORANGE="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"n05-04-activation","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    fig=plt.figure(figsize=(520/72,710/72),facecolor="#F8FAFC")
    ax=fig.add_axes((.18,.25,.73,.49),facecolor="#F8FAFC");ax.grid(color="#CBD5E1",alpha=.75)
    x=np.linspace(-4,4,801);sig=1/(1+np.exp(-x));cdf=np.array([.5*(1+math.erf(v/math.sqrt(2))) for v in x]);pdf=np.exp(-x*x/2)/math.sqrt(2*math.pi)
    if "affine" in output.name:
        x=np.linspace(-1,1,600)
        ax.plot(x,6*x+1,color=BLUE,lw=2.7,ls="--",label="No activation")
        ax.plot(x,2*np.maximum(0,3*x+1)-1,color=PURPLE,lw=3,label="With ReLU")
        ax.scatter([-1/3],[-1],color=PURPLE,s=65,zorder=5)
        ax.set(xlim=(-1,1),ylim=(-5,8),xlabel="Input x",ylabel="Output y")
        ax.set_xticks([-1,0,1]);ax.set_yticks([-4,0,4,8])
        ax.legend(loc="lower left",bbox_to_anchor=(-.16,1.04),frameon=False,fontsize=24)
        fig.text(.077,.95,"Affine versus piecewise",fontsize=30,color="#0F172A")
        fig.text(.077,.13,"No activation: y = 6x + 1",fontsize=26,color=BLUE)
        fig.text(.077,.075,"With ReLU: y = 2ReLU(3x+1) − 1",fontsize=24,color=PURPLE)
        fig.text(.077,.025,"Break at x = −1/3; slopes 0 and 6.",fontsize=24,color=PURPLE)
    elif "saturation" in output.name:
        x=np.linspace(-6,6,801);sig=1/(1+np.exp(-x));slope=sig*(1-sig)
        ax.plot(x,sig,color=BLUE,lw=2.7,label="Value")
        ax.plot(x,slope,color=PURPLE,lw=2.7,ls="--",label="Local slope")
        at4=1/(1+math.exp(-4))
        ax.scatter([4,4],[at4,at4*(1-at4)],color=[BLUE,PURPLE],s=65,zorder=5)
        ax.set(xlim=(-6,6),ylim=(-.03,1.06),xlabel="Input x",ylabel="Sigmoid")
        ax.set_xticks([-4,0,4]);ax.set_yticks([0,.5,1])
        ax.legend(loc="lower left",bbox_to_anchor=(-.16,1.04),frameon=False,fontsize=24)
        fig.text(.077,.95,"Large value, small slope",fontsize=30,color="#0F172A")
        fig.text(.077,.13,"σ(4) ≈ 0.982",fontsize=28,color=BLUE)
        fig.text(.077,.075,"σ′(4) ≈ 0.0177",fontsize=28,color=PURPLE)
    else:
        styles=[(BLUE,"-", "ReLU"),(ORANGE,":","sigmoid"),(PURPLE,"--","GELU"),(GREEN,"-.","SiLU")]
        derivative="derivative" in output.name
        ys=[np.maximum(0,x),sig,x*cdf,x*sig]
        if derivative:ys=[(x>0).astype(float),sig*(1-sig),cdf+x*pdf,sig+x*sig*(1-sig)]
        for i,(y,(col,ls,label)) in enumerate(zip(ys,styles)):
            if derivative and i==0:
                ax.plot(x[x<0],y[x<0],color=col,lw=2.7,ls=ls,label=label)
                ax.plot(x[x>0],y[x>0],color=col,lw=2.7,ls=ls)
                ax.scatter([0],[1],facecolors="#F8FAFC",edgecolors=col,s=70,zorder=7)
                ax.scatter([0],[0],color=col,s=60,zorder=7)
            else:ax.plot(x,y,color=col,lw=2.7,ls=ls,label=label)
        ax.set(xlim=(-4,4),ylim=(-.3,1.3) if derivative else (-.6,4.3),xlabel="Input x",ylabel="Local slope" if derivative else "Activation value")
        ax.set_xticks([-4,-2,0,2,4]);ax.set_yticks([0,.5,1] if derivative else [0,1,2,3,4])
        legend=ax.legend(loc="lower left",bbox_to_anchor=(-.16,1.02),frameon=False,ncol=2,fontsize=24,columnspacing=1.4)
        legend.set_zorder(10)
        fig.text(.077,.95,"Local derivatives" if derivative else "Four activation curves",fontsize=30,color="#0F172A")
        fig.text(.077,.13,"At 0: GELU′ = SiLU′ = 0.5" if derivative else "GELU and SiLU pass some negatives.",fontsize=25,color=PURPLE)
        fig.text(.077,.075,"ReLU′(0) = 0: PyTorch convention." if derivative else "Sigmoid stays between 0 and 1.",fontsize=24,color=BLUE)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
