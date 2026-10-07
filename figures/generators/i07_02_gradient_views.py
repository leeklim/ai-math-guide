"""Reproduce the manuscript's signed gradient, Taylor, scale and saturation views."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
B,P,G,O="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-02-gradient","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    name=output.name
    two="signed-versus-saliency" in name or "unit-rescaling" in name
    fig=plt.figure(figsize=(520/72,(950 if two else 850)/72),facecolor="#F8FAFC")
    if two:
        axes=[fig.add_axes((.21,.57,.70,.25),facecolor="#F8FAFC"),fig.add_axes((.21,.15,.70,.25),facecolor="#F8FAFC")]
        if "signed-versus-saliency" in name:
            for ax,val,title,col in zip(axes,[[2,-4],[2,4]],["Signed gradient","Absolute saliency"],[B,G]):
                ax.bar([0,1],val,color=col);ax.axhline(0,color="#64748B");ax.set_xticks([0,1],["x₁","x₂"]);ax.set(ylim=(-5,3) if col==B else (0,5),ylabel="Score / input unit");ax.set_yticks([-4,0,2] if col==B else [0,2,4]);ax.grid(axis="y",color="#CBD5E1",alpha=.7)
                fig.text(.077,ax.get_position().y1+.035,title,fontsize=28,color=col)
            fig.text(.077,.95,"Magnitude loses the direction",fontsize=27,color="#0F172A")
            fig.text(.077,.055,"s = 2x₁ − x₂²; x = (3, 2)",fontsize=27,color="#0F172A")
        else:
            for ax,factor,unit,col in zip(axes,[1,100],["m","cm"],[B,G]):
                xx=np.linspace(0,1.4*factor,100);ax.plot(xx,3*xx/factor,color=col,lw=2.6);ax.scatter([factor],[3],color=O,s=65,zorder=5);ax.set(xlim=(0,1.4*factor),ylim=(0,4.2),xlabel=f"Input ({unit})",ylabel="Score");ax.set_xticks([0,factor]);ax.set_yticks([0,3]);ax.grid(color="#CBD5E1",alpha=.7)
                fig.text(.077,ax.get_position().y1+.035,"Slope "+("3 / m" if factor==1 else "0.03 / cm"),fontsize=28,color=col)
            fig.text(.077,.95,"Same function, new input unit",fontsize=27,color="#0F172A")
            fig.text(.077,.055,"1 × 3 = 100 × 0.03 = 3",fontsize=28,color="#0F172A")
    else:
        ax=fig.add_axes((.19,.29,.72,.46),facecolor="#F8FAFC")
        if "current-tangent-gap" in name:
            t=np.linspace(0,1.2,300);ax.plot(t,7*t*t,color=G,lw=2.6,label="Actual score");ax.plot(t,14*t-7,color=P,lw=2.6,ls="--",label="Current tangent");ax.scatter([0,1],[0,7],color=[O,B],s=65,zorder=5);ax.set(xlim=(-.05,1.2),ylim=(-8,11),xlabel="Path fraction t",ylabel="Score");ax.set_xticks([0,1]);ax.set_yticks([-7,0,7]);ax.axhline(0,color="#64748B",lw=.8)
            fig.text(.077,.95,"Current tangent to baseline",fontsize=28,color="#0F172A")
            fig.text(.077,.18,"Path: s(tx) = 7t²",fontsize=28,color=G)
            fig.text(.077,.11,"Tangent change: 14",fontsize=28,color=P)
            fig.text(.077,.045,"Actual change: 7",fontsize=28,color=O)
        else:
            x=np.linspace(-3,8,400);sig=1/(1+np.exp(-x));p=1/(1+np.exp(-6));g=p*(1-p)
            ax.plot(x,sig,color=G,lw=2.6,label="Sigmoid");ax.plot([3,8],[p+g*(3-6),p+g*(8-6)],color=P,lw=2.6,ls="--",label="Tangent at x = 6");ax.scatter([0,6],[.5,p],color=[O,B],s=65,zorder=5);ax.set(xlim=(-3,8),ylim=(0,1.12),xlabel="Input x",ylabel="Score σ(x)");ax.set_xticks([0,3,6]);ax.set_yticks([0,.5,1])
            fig.text(.077,.95,"Large change, small local slope",fontsize=26,color="#0F172A")
            fig.text(.077,.18,"Baseline score: 0.5",fontsize=28,color=O)
            fig.text(.077,.11,"Score at 6: 0.9975",fontsize=28,color=B)
            fig.text(.077,.045,"Local slope: 0.00247",fontsize=28,color=P)
        ax.grid(color="#CBD5E1",alpha=.7);ax.legend(loc="lower left",bbox_to_anchor=(-.17,1.02),fontsize=24,frameon=False)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
