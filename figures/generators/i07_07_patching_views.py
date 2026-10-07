"""Reproduce ratio geometry and the existing CPU full-vector toy patch."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
B,P,G,O="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-07-patch","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    fig=plt.figure(figsize=(520/72,870/72),facecolor="#F8FAFC");ax=fig.add_axes((.20,.31,.71,.44),facecolor="#F8FAFC")
    if "small-denominator" in output.name:
        gap=np.linspace(.01,1,600);ax.plot(gap,.1/gap,color=P,lw=2.6);ax.scatter([.01,.1,1],[10,1,.1],color=O,s=55,zorder=5);ax.set(xlim=(0,1.06),ylim=(0,11.2),xlabel="Clean−corrupt gap",ylabel="Recovery");ax.set_xticks([.1,.5,1]);ax.set_yticks([0,1,5,10])
        fig.text(.077,.95,"Small gap, large ratio",fontsize=28,color="#0F172A");fig.text(.077,.87,"Fixed patch effect = 0.1",fontsize=27,color=P);fig.text(.077,.20,"Gap 1 → recovery 0.1",fontsize=28,color=O);fig.text(.077,.125,"Gap 0.1 → recovery 1",fontsize=28,color=O);fig.text(.077,.05,"Gap 0.01 → recovery 10",fontsize=28,color=O)
    else:
        win=np.array([[1.,-.5],[.5,1.]]);wout=np.array([1.2,-.4]);hc=np.tanh(win@np.array([2.,.5]));hr=np.tanh(win@np.array([-1.,.5]))
        ax.scatter(*hr,color=O,s=65,zorder=5);ax.scatter(*hc,color=G,s=65,zorder=5);ax.add_patch(FancyArrowPatch(hr,hc,arrowstyle="-|>",mutation_scale=12,color=P,lw=2.6,shrinkA=8,shrinkB=8));ax.set(xlim=(-1.1,1.25),ylim=(-.2,1.3),xlabel="Hidden coordinate 1",ylabel="Hidden coordinate 2");ax.set_xticks([-1,0,1]);ax.set_yticks([0,.5,1])
        fig.text(.077,.95,"CPU full-vector replacement",fontsize=28,color="#0F172A");fig.text(.077,.87,"Corrupt → clean hidden",fontsize=27,color=P);fig.text(.077,.20,f"Corrupt score: {wout@hr:.4f}",fontsize=27,color=O);fig.text(.077,.125,f"Clean = patched: {wout@hc:.4f}",fontsize=27,color=G);fig.text(.077,.05,"Full-vector recovery = 1",fontsize=28,color=P)
    ax.grid(color="#CBD5E1",alpha=.7);fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
