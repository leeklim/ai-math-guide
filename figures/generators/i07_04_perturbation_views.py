"""Reproduce finite replacement comparisons and illustrative resampling geometry."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
B,P,G,O="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-04-perturb","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    n=output.name;two="replacement-comparisons" not in n
    fig=plt.figure(figsize=(520/72,(1030 if two else 850)/72),facecolor="#F8FAFC")
    if "replacement-comparisons" in n:
        ax=fig.add_axes((.20,.31,.71,.45),facecolor="#F8FAFC")
        x=np.linspace(0,4.5,150);ax.plot(x,2*x+4,color=G,lw=2.6);ax.axhline(10,color=P,ls=":",lw=2);ax.scatter([0,2,3,4],[4,8,10,12],color=[O,O,B,O],s=65,zorder=5);ax.set(xlim=(-.1,4.5),ylim=(2,14),xlabel="Replacement x₁",ylabel="Score: 2x₁ + 4");ax.set_xticks([0,2,3,4]);ax.set_yticks([4,8,10,12]);ax.grid(color="#CBD5E1",alpha=.7)
        fig.text(.077,.95,"Original minus replacement",fontsize=27,color="#0F172A")
        fig.text(.077,.87,"Original: x₁ = 3; score 10",fontsize=27,color=B)
        fig.text(.077,.20,"Replace by 0: Δ = 6",fontsize=28,color=O)
        fig.text(.077,.125,"Replace by 2: Δ = 2",fontsize=28,color=O)
        fig.text(.077,.05,"Replace by 4: Δ = −2",fontsize=28,color=O)
    else:
        axes=[fig.add_axes((.20,.58,.71,.22),facecolor="#F8FAFC"),fig.add_axes((.20,.17,.71,.22),facecolor="#F8FAFC")]
        if "lab-baseline-effects" in n:
            for ax,vals,title in zip(axes,[[9,6,.25],[4.5,4,0]],["Zero replacements","Mean-like replacements = 1"]):
                ax.bar([0,1,2],vals,color=[B,P,G]);ax.set_xticks([0,1,2],["x₁","x₂","x₃"]);ax.set(ylim=(0,10.5),ylabel="Score effect");ax.set_yticks([0,3,6,9]);ax.grid(axis="y",color="#CBD5E1",alpha=.7)
                for i,v in enumerate(vals):ax.text(i,v+.35,str(v),ha="center",fontsize=24,color="#0F172A")
                fig.text(.077,ax.get_position().y1+.035,title,fontsize=26,color="#0F172A")
            fig.text(.077,.95,"Same input; two replacements",fontsize=26,color="#0F172A")
            fig.text(.077,.055,"x = (2, 3, 1); score 9.25",fontsize=28,color="#0F172A")
        else:
            rng=np.random.default_rng(17);u=rng.normal(0,1,130);v=u+rng.normal(0,.22,130)
            for ax,draw,title,col in zip(axes,[np.linspace(-2,2,9),np.linspace(1.2,1.8,9)],["Marginal replacement","Conditional replacement"],[O,P]):
                ax.scatter(u,v,color="#64748B",alpha=.25,s=20);ax.axhline(1.5,color="#64748B",ls="--",lw=1);ax.scatter(draw,np.full(9,1.5),color=col,s=55,zorder=5);ax.set(xlim=(-2.5,2.5),ylim=(-2.5,2.5),xlabel="Replaced coordinate x₁",ylabel="Fixed x₂");ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,1.5]);ax.grid(color="#CBD5E1",alpha=.5)
                fig.text(.077,ax.get_position().y1+.035,title,fontsize=28,color=col)
            fig.text(.077,.95,"Different joint input states",fontsize=28,color="#0F172A")
            fig.text(.077,.055,"Illustrative cloud: x₂ ≈ x₁",fontsize=27,color="#64748B")
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
