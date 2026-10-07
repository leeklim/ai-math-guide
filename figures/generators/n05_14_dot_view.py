"""Reproduce N05-14 vector lengths versus raw dot and cosine."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch
BLUE,PURPLE,RED="#2563EB","#7C3AED","#DC2626"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"n05-14-dot","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    q=np.array([1.,2.]);k=np.array([3.,-1.])
    assert q@k==1 and q@(2*k)==2
    assert np.isclose((q@k)/(np.linalg.norm(q)*np.linalg.norm(k)),1/np.sqrt(50))
    fig=plt.figure(figsize=(520/72,830/72),facecolor="#F8FAFC")
    ax=fig.add_axes((.17,.27,.74,.45),facecolor="#F8FAFC");ax.grid(color="#CBD5E1",alpha=.7);ax.set_aspect("equal")
    for point,col,ls,z in [(2*k,RED,":",3),(k,PURPLE,"--",5),(q,BLUE,"-",6)]:
        ax.add_patch(FancyArrowPatch((0,0),point,arrowstyle="-|>",mutation_scale=11,color=col,lw=2.5,linestyle=ls,shrinkA=0,shrinkB=0,zorder=z))
    ax.set(xlim=(-.5,6.7),ylim=(-2.7,2.7),xlabel="Feature 1",ylabel="Feature 2");ax.set_xticks([0,2,4,6]);ax.set_yticks([-2,0,2])
    ax.legend(handles=[Line2D([0],[0],color=BLUE,lw=2.5,label="q₀ = (1, 2)"),Line2D([0],[0],color=PURPLE,lw=2.5,ls="--",label="k₀ = (3, −1)"),Line2D([0],[0],color=RED,lw=2.5,ls=":",label="2k₀ = (6, −2)")],loc="lower left",bbox_to_anchor=(-.15,1.02),frameon=False,fontsize=24)
    fig.text(.077,.95,"Dot also depends on vector lengths",fontsize=26,color="#0F172A")
    fig.text(.077,.17,"Same key direction; twice the length.",fontsize=24,color=RED)
    fig.text(.077,.10,"Raw dot: 1 → 2",fontsize=28,color=PURPLE)
    fig.text(.077,.04,"Cosine stays 1/√50 ≈ 0.1414.",fontsize=27,color=BLUE)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
