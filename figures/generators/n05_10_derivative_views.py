"""Reproduce N05-10 local output path and Jacobian column addition."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch
BLUE,PURPLE,GREEN,ORANGE="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"n05-10-products","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def arrow(ax,start,end,col,ls="-",zorder=3):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=11,color=col,lw=2.5,linestyle=ls,shrinkA=0,shrinkB=0,zorder=zorder))
def main(output):
    fig=plt.figure(figsize=(520/72,800/72),facecolor="#F8FAFC")
    ax=fig.add_axes((.19,.26,.72,.47),facecolor="#F8FAFC");ax.grid(color="#CBD5E1",alpha=.7)
    if "jvp-path" in output.name:
        eps=np.linspace(-.7,.7,400)
        ax.plot(6+eps-eps**2,7+3*eps+eps**2,color=GREEN,lw=2.6,label="Actual output path")
        ax.plot(6+eps,7+3*eps,color=PURPLE,lw=2.6,ls="--",label="Tangent at ε = 0")
        ax.scatter([6],[7],color=ORANGE,s=65,zorder=7)
        ax.text(5.48,7.15,"(6, 7)",fontsize=25,color=ORANGE,bbox={"facecolor":"#F8FAFC","edgecolor":"none","pad":2})
        ax.set(xlim=(4.6,6.85),ylim=(5.1,9.8),xlabel="Output f₁",ylabel="Output f₂")
        ax.set_xticks([5,6]);ax.set_yticks([6,7,8,9])
        ax.legend(loc="lower left",bbox_to_anchor=(-.18,1.02),fontsize=24,frameon=False)
        fig.text(.077,.95,"Local path and its JVP tangent",fontsize=28,color="#0F172A")
        fig.text(.077,.14,"Input: (2, 3) + ε(1, −1)",fontsize=27,color=BLUE)
        fig.text(.077,.075,"Tangent rate: (1, 3) per ε",fontsize=27,color=PURPLE)
        fig.text(.077,.025,"Curvature adds (−ε², ε²).",fontsize=24,color=GREEN)
    else:
        ax.set_position((.19,.25,.72,.45));ax.set_aspect("equal")
        arrow(ax,(0,0),(3,4),BLUE,"-",6);arrow(ax,(3,4),(1,3),PURPLE,"--",5);arrow(ax,(0,0),(1,3),GREEN,"-.",7)
        ax.scatter([0],[0],color="#64748B",s=30,zorder=8)
        ax.set(xlim=(-.5,4),ylim=(-.5,4.8),xlabel="df₁ / dε",ylabel="df₂ / dε")
        ax.set_xticks([0,1,2,3]);ax.set_yticks([0,1,2,3,4])
        ax.legend(handles=[Line2D([0],[0],color=BLUE,lw=2.5,label="1 × column 1: (3, 4)"),Line2D([0],[0],color=PURPLE,lw=2.5,ls="--",label="−1 × column 2: (−2, −1)"),Line2D([0],[0],color=GREEN,lw=2.5,ls="-.",label="Sum: (1, 3)")],loc="lower left",bbox_to_anchor=(-.19,1.02),frameon=False,fontsize=23)
        fig.text(.077,.95,"JVP adds weighted columns",fontsize=29,color="#0F172A")
        fig.text(.077,.14,"Input direction r = (1, −1)",fontsize=27,color=BLUE)
        fig.text(.077,.075,"(3, 4) − (2, 1) = (1, 3)",fontsize=28,color=GREEN)
        fig.text(.077,.025,"Axes show output rates, not f(x).",fontsize=24,color="#64748B")
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
