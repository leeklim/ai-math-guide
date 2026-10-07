"""Reproduce I07-01 local versus finite change and target coupling."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
BLUE,PURPLE,GREEN,ORANGE="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-01-attribution","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    if "gradient-removal-units" in output.name or "target-softmax-coupling" in output.name:
        fig=plt.figure(figsize=(520/72,950/72),facecolor="#F8FAFC")
        axes=[fig.add_axes((.20,.57,.71,.25),facecolor="#F8FAFC"),fig.add_axes((.20,.15,.71,.25),facecolor="#F8FAFC")]
        if "gradient-removal-units" in output.name:
            for ax,values,title,yl,col in zip(axes,[[3,2,2],[6,6,1]],["Local gradient","Zero-baseline removal"],["Score / input unit","Score difference"],[BLUE,GREEN]):
                ax.bar(np.arange(3),values,color=col);ax.set_xticks(np.arange(3),["x₁","x₂","x₃"]);ax.set_yticks([0,1,2,3] if col==BLUE else [0,2,4,6]);ax.set(ylim=(0,3.7) if col==BLUE else (0,7.2),ylabel=yl);ax.grid(axis="y",color="#CBD5E1",alpha=.7)
                fig.text(.077,ax.get_position().y1+.035,title,fontsize=27,color=col)
            fig.text(.077,.95,"Two measures, two units",fontsize=28,color="#0F172A")
            fig.text(.077,.055,"At x = (2, 3, 1), f(x) = 7",fontsize=28,color="#0F172A")
        else:
            x=np.linspace(-1,3,400);p=np.exp(1)/(np.exp(1)+np.exp(x))
            axes[0].plot(x,np.ones_like(x),color=BLUE,lw=2.6);axes[0].set(ylim=(.5,1.5),ylabel="Target logit A");axes[0].set_yticks([1])
            axes[1].plot(x,p,color=GREEN,lw=2.6);axes[1].scatter([0,1,2],[1/(1+np.exp(-1)),.5,1/(1+np.exp(1))],color=ORANGE,s=55,zorder=5);axes[1].set(ylim=(0,1),ylabel="Target probability A");axes[1].set_yticks([0,.5,1])
            for ax in axes:ax.set(xlim=(-1,3),xlabel="Other logit B");ax.set_xticks([0,1,2]);ax.grid(color="#CBD5E1",alpha=.7)
            fig.text(.077,.95,"Hold A's logit fixed",fontsize=28,color="#0F172A")
            fig.text(.077,.90,"Probability still changes",fontsize=28,color="#0F172A")
            fig.text(.077,.065,"Illustrative two-class softmax",fontsize=26,color=BLUE)
            fig.text(.077,.025,"Fixed z_A = 1",fontsize=26,color=BLUE)
    else:
        fig=plt.figure(figsize=(520/72,810/72),facecolor="#F8FAFC");ax=fig.add_axes((.19,.27,.72,.49),facecolor="#F8FAFC")
        x=np.linspace(0,2.3,400)
        if "linear-coordinate-change" in output.name:
            ax.plot(x,3*x+1,color=GREEN,lw=2.6);ax.scatter([0,2],[1,7],color=[ORANGE,BLUE],s=65,zorder=5)
            ax.plot([0,2],[7,7],color=PURPLE,ls=":",lw=2);ax.plot([0,0],[1,7],color=ORANGE,ls="--",lw=2)
            ax.set(ylim=(0,9),xlabel="Input coordinate x₁",ylabel="Score: 3x₁ + 1");ax.set_yticks([0,1,4,7])
            fig.text(.077,.95,"Rate 3; full decrease 6",fontsize=29,color="#0F172A")
            fig.text(.077,.16,"Input change: 2 → 0",fontsize=28,color=BLUE)
            fig.text(.077,.09,"Score change: 7 → 1",fontsize=28,color=GREEN)
            fig.text(.077,.035,"Decrease: 3 × 2 = 6",fontsize=28,color=ORANGE)
        else:
            ax.plot(x,6+x*x,color=GREEN,lw=2.6,label="Actual curve");ax.plot(x,5+2*x,color=PURPLE,lw=2.6,ls="--",label="Tangent at x₃ = 1")
            ax.scatter([0,1],[6,7],color=[ORANGE,BLUE],s=65,zorder=5);ax.set(ylim=(4,12),xlabel="Input coordinate x₃",ylabel="Score: 6 + x₃²");ax.set_yticks([5,6,7,10])
            ax.legend(loc="lower left",bbox_to_anchor=(-.17,1.02),fontsize=24,frameon=False)
            fig.text(.077,.95,"A tangent is a local comparison",fontsize=27,color="#0F172A")
            fig.text(.077,.16,"At x₃ = 1: slope 2",fontsize=28,color=PURPLE)
            fig.text(.077,.09,"Remove x₃: actual score 7 → 6",fontsize=26,color=GREEN)
            fig.text(.077,.035,"Tangent at zero predicts 5.",fontsize=26,color=PURPLE)
        ax.set(xlim=(-.1,2.3));ax.set_xticks([0,1,2]);ax.grid(color="#CBD5E1",alpha=.7)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
