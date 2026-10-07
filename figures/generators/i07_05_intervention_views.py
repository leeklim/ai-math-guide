"""Reproduce original and node-intervened toy outcomes."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
B,P,G,O="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-05-intervene","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    fig=plt.figure(figsize=(520/72,870/72),facecolor="#F8FAFC");ax=fig.add_axes((.19,.30,.72,.43),facecolor="#F8FAFC")
    if "observed-versus-fixed-h" in output.name:
        x=np.linspace(.3,2.3,120);ax.plot(x,3*x,color=B,lw=2.6,label="Original: H = 2X");ax.plot(x,x+2,color=P,lw=2.6,ls="--",label="Intervene: H = 2");ax.scatter([1,2,2],[3,6,4],color=[O,B,P],s=65,zorder=5);ax.set(xlim=(.3,2.3),ylim=(0,7.4),xlabel="Input X",ylabel="Outcome Y");ax.set_xticks([1,2]);ax.set_yticks([0,3,4,6]);ax.legend(loc="lower left",bbox_to_anchor=(-.17,1.02),fontsize=24,frameon=False)
        fig.text(.077,.95,"Different comparisons",fontsize=28,color="#0F172A");fig.text(.077,.19,"Observe X: 1 → 2; ΔY = +3",fontsize=26,color=B);fig.text(.077,.11,"Fix X = 2; H: 4 → 2",fontsize=27,color=P);fig.text(.077,.035,"Intervention: ΔY = −2",fontsize=28,color=P)
    else:
        for x,col,style in zip([.5,1,2],[B,P,G],["-","--",":"]):ax.plot([0,1],[3*x,x+2],color=col,ls=style,lw=2.6,marker="o",ms=6,label=f"X = {x}")
        ax.set(xlim=(-.12,1.12),ylim=(0,7),ylabel="Outcome Y");ax.set_xticks([0,1],["Intact","do(H = 2)"]);ax.set_yticks([0,2,4,6]);ax.legend(loc="lower left",bbox_to_anchor=(-.17,1.02),fontsize=24,frameon=False)
        fig.text(.077,.95,"Pair conditions within each X",fontsize=26,color="#0F172A");fig.text(.077,.19,"Paired changes: +1, 0, −2",fontsize=27,color="#0F172A");fig.text(.077,.11,"Mean: (1 + 0 − 2) / 3 = −1/3",fontsize=25,color=O);fig.text(.077,.035,"Illustrative set of three inputs",fontsize=25,color="#64748B")
    ax.grid(color="#CBD5E1",alpha=.7);fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
