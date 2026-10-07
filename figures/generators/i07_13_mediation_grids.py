"""Reproduce small mediation counterfactual outcome grids in I07-13."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-13-mediation","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    key=output.stem.removeprefix("I07-13-");interaction=key.startswith("interaction");via_t0=key.endswith("via-t0");fn=(lambda t,m:t*m) if interaction else (lambda t,m:t+3*m)
    fig=plt.figure(figsize=(520/72,1120/72),facecolor="#F8FAFC");fig.text(.077,.95,"Interaction: Y = T × M" if interaction else "CPU example: Y = T + 3M",fontsize=28);fig.text(.077,.90,"M(0) = 0; M(1) = 2",fontsize=27,color="#64748B")
    ax=fig.add_axes((.20,.39,.68,.40),facecolor="#F8FAFC");ax.set(xlim=(-.3,1.3),ylim=(-.5,2.5),xlabel="Treatment T",ylabel="Mediator M");ax.set_xticks([0,1]);ax.set_yticks([0,2]);ax.grid(color="#CBD5E1",alpha=.7)
    for t,m in [(0,0),(1,0),(0,2),(1,2)]:
        ax.scatter([t],[m],s=1000,facecolors="white",edgecolors="#059669",lw=2,zorder=4);ax.text(t,m,str(fn(t,m)),ha="center",va="center",color="#059669",fontsize=28,zorder=5)
    routes=[((0,.17),(0,1.83)),((.16,2),(.84,2))] if via_t0 else [((.16,0),(.84,0)),((1,.17),(1,1.83))]
    for a,b in routes:ax.add_patch(FancyArrowPatch(a,b,arrowstyle="->",mutation_scale=12,color="#7C3AED",lw=2.6,shrinkA=0,shrinkB=0,zorder=6))
    middle=fn(0,2) if via_t0 else fn(1,0)
    if via_t0:
        lines=[("M changes at T=0: effect "+str(fn(0,2)-fn(0,0)),"#7C3AED"),("T changes at M=2: effect "+str(fn(1,2)-fn(0,2)),"#7C3AED")]
    else:
        lines=[("T changes at M=0: effect "+str(fn(1,0)-fn(0,0)),"#7C3AED"),("M changes at T=1: effect "+str(fn(1,2)-fn(1,0)),"#7C3AED")]
    for y,(s,col) in zip([.28,.21],lines):fig.text(.077,y,s,fontsize=26,color=col)
    fig.text(.077,.13,"Intermediate outcome = "+str(middle),fontsize=27,color="#64748B");fig.text(.077,.06,"Total effect = "+str(fn(1,2)-fn(0,0)),fontsize=28,color="#059669")
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
