"""Draw zero-ablation and empty-baseline restoration in I07-12."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-12-effects","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    key=output.stem.removeprefix("I07-12-");fig=plt.figure(figsize=(520/72,1050/72),facecolor="#F8FAFC")
    if key in ("redundancy-two-starts","synergy-two-starts"):
        prod=key.startswith("synergy");fn=(lambda a,b:a*b) if prod else max
        fig.text(.077,.95,"Synergy: Y = A × B" if prod else "Redundancy: Y = max(A, B)",fontsize=27)
        fig.text(.077,.905,"Zero removal; success Y = 1",fontsize=26,color="#64748B")
        ax=fig.add_axes((.19,.36,.70,.43),facecolor="#F8FAFC");ax.set(xlim=(-.3,1.3),ylim=(-.3,1.3),xlabel="Component A",ylabel="Component B");ax.set_xticks([0,1]);ax.set_yticks([0,1]);ax.set_aspect("equal");ax.grid(color="#CBD5E1",alpha=.7)
        for a,b in [(0,0),(0,1),(1,0),(1,1)]:
            y=fn(a,b);ax.scatter([a],[b],s=1000,facecolors="white",edgecolors="#059669" if y else "#64748B",lw=2,zorder=4);ax.text(a,b,str(y),ha="center",va="center",fontsize=28,color="#059669" if y else "#64748B",zorder=5)
        ax.add_patch(FancyArrowPatch((.86,1),(.14,1),arrowstyle="->",mutation_scale=12,color="#DC2626",lw=2.5,shrinkA=0,shrinkB=0,zorder=6))
        ax.add_patch(FancyArrowPatch((.14,0),(.86,0),arrowstyle="->",mutation_scale=12,color="#7C3AED",lw=2.5,shrinkA=0,shrinkB=0,zorder=6))
        for y,s,col in [(.29,"Top: remove A from intact (1,1)","#DC2626"),(.22,"Bottom: restore A from empty (0,0)","#7C3AED"),(.14,"Necessity effect = "+str(1-fn(0,1)),"#DC2626"),(.08,"Sufficiency effect = "+str(fn(1,0)),"#7C3AED")]:fig.text(.077,y,s,fontsize=26 if y>.2 else 28,color=col)
    elif key=="improvement-versus-success":
        fig.text(.077,.95,"Improvement is not yet success",fontsize=27);fig.text(.077,.905,"Illustrative outcome; threshold 1",fontsize=26,color="#64748B")
        ax=fig.add_axes((.22,.31,.65,.51),facecolor="#F8FAFC");ax.bar([0,1],[.1,.4],color=["#64748B","#7C3AED"],width=.48);ax.axhline(1,color="#D97706",ls="--",lw=2);ax.set(ylim=(0,1.25),ylabel="Outcome Y",xlim=(-.55,1.55));ax.set_xticks([0,1],["Baseline","Restore C"]);ax.set_yticks([0,.5,1]);ax.grid(axis="y",color="#CBD5E1",alpha=.7);ax.text(.5,1.06,"Success ≥ 1",ha="center",fontsize=26,color="#D97706")
        for x,v in enumerate([.1,.4]):ax.text(x,v+.04,str(v),ha="center",fontsize=28,color="#64748B" if x==0 else "#7C3AED")
        fig.text(.077,.19,"S_C = 0.4 − 0.1 = 0.3 > 0",fontsize=28,color="#7C3AED");fig.text(.077,.11,"Restored outcome 0.4 is below 1.",fontsize=26,color="#D97706")
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
