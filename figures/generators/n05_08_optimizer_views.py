"""Reproduce N05-08 history weights and correctly scaled AdamW displacements."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
BLUE,PURPLE,GREEN,ORANGE="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"n05-08-state","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def arrow(ax,start,end,col):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=12,color=col,lw=2.5,shrinkA=3,shrinkB=0))
def main(output):
    if "displacements" in output.name:
        fig=plt.figure(figsize=(520/72,850/72),facecolor="#F8FAFC")
        fig.text(.077,.95,"AdamW: two displacements",fontsize=29,color="#0F172A")
        for pos,lim,ticks,start,end,title,col in [(.59,(1.89,2.01),[1.9,1.95,2.0],2,1.9,"Adaptive part: −0.1",PURPLE),(.22,(1.897,1.901),[1.898,1.900],1.9,1.898,"Zoom: decay part −0.002",ORANGE)]:
            ax=fig.add_axes((.16,pos,.76,.18),facecolor="#F8FAFC")
            ax.spines["left"].set_visible(False);ax.spines["bottom"].set_position(("data",0));ax.set_yticks([])
            ax.set(xlim=lim,ylim=(-.35,1));ax.set_xticks(ticks);ax.ticklabel_format(axis="x",style="plain",useOffset=False)
            ax.set_xlabel("Parameter θ",labelpad=15)
            arrow(ax,(start,.5),(end,.5),col)
            ax.plot([start,start],[0,.5],color=col,ls=":",lw=1.5);ax.plot([end,end],[0,.5],color=col,ls=":",lw=1.5)
            ax.scatter([start,end],[0,0],color=col,s=45,zorder=5)
            fig.text(.077,pos+.24,title,fontsize=27,color=col)
        fig.text(.077,.08,"Decay uses θ₀ = 2: 0.1 × 0.01 × 2.",fontsize=24,color=ORANGE)
        fig.text(.077,.03,"Final θ₁ = 2 − 0.1 − 0.002 = 1.898",fontsize=24,color=GREEN)
    else:
        fig=plt.figure(figsize=(520/72,760/72),facecolor="#F8FAFC")
        ax=fig.add_axes((.18,.27,.73,.47),facecolor="#F8FAFC")
        idx=np.arange(1,6);weights=.9**(5-idx)
        if "correction" in output.name:
            raw=.1*weights;corrected=raw/(1-.9**5)
            ax.bar(idx-.16,raw,width=.28,color=BLUE,alpha=.24,edgecolor=BLUE,label="Before correction")
            ax.bar(idx+.16,corrected,width=.28,color=PURPLE,alpha=.24,edgecolor=PURPLE,hatch="//",label="After correction")
            ax.set(ylim=(0,.29),ylabel="Gradient weight",xlabel="Gradient step s");ax.set_yticks([0,.1,.2]);ax.set_xticks(idx)
            ax.legend(loc="lower left",bbox_to_anchor=(-.16,1.02),frameon=False,fontsize=23)
            fig.text(.077,.95,"Bias correction rescales weights",fontsize=28,color="#0F172A")
            fig.text(.077,.14,"t = 5, β₁ = 0.9, m₀ = 0",fontsize=28,color="#0F172A")
            fig.text(.077,.085,"Before: weight sum = 0.40951",fontsize=25,color=BLUE)
            fig.text(.077,.035,"After: weight sum = 1",fontsize=27,color=PURPLE)
        else:
            ax.bar(idx,weights,color=BLUE,alpha=.24,edgecolor=BLUE)
            ax.set(ylim=(0,1.2),ylabel="Weight in u₅",xlabel="Gradient step s");ax.set_yticks([0,.5,1]);ax.set_xticks(idx)
            fig.text(.077,.95,"Older gradients fade in u₅",fontsize=29,color="#0F172A")
            fig.text(.077,.14,"u₅ = μ⁴g₁ + μ³g₂ + μ²g₃",fontsize=26,color=BLUE)
            fig.text(.077,.085,"       + μg₄ + g₅,    μ = 0.9",fontsize=26,color=BLUE)
            fig.text(.077,.035,"The latest gradient has weight 1.",fontsize=25,color="#0F172A")
        ax.grid(axis="y",color="#CBD5E1",alpha=.75)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
