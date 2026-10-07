"""Draw exact periodic distributions and illustrative momentum states."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-dyn-04-markov","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    key=output.stem.removeprefix("A09-DYN-04-");fig=plt.figure(figsize=(520/72,1000/72),facecolor="#F8FAFC");ax=fig.add_axes((.23,.27,.65,.43),facecolor="#F8FAFC");ax.grid(color="#CBD5E1",alpha=.65)
    if key=="periodic-distribution":
        k=np.arange(7);ax.plot(k,(k%2==0).astype(float),"o--",color="#7C3AED",lw=2.5,ms=8);ax.axhline(.5,color="#059669",lw=2.5);ax.set(xlim=(-.15,6.2),ylim=(-.1,1.1),xlabel="Step k",ylabel="Probability of state 1");ax.set_xticks([0,2,4,6]);ax.set_yticks([0,.5,1])
        fig.text(.077,.95,"Stationary exists; no convergence",fontsize=26);fig.text(.077,.865,"Start p₀ = (1, 0)  o - -",fontsize=28,color="#7C3AED");fig.text(.077,.80,"Stationary π = (1/2, 1/2) —",fontsize=26,color="#059669");fig.text(.077,.17,"P = [[0, 1], [1, 0]]",fontsize=28);fig.text(.077,.095,"The two initial laws are different.",fontsize=25,color="#64748B");fig.text(.077,.03,"A fixed distribution is not mixing.",fontsize=25,color="#64748B")
    elif key=="momentum-hidden-state":
        ax.set(xlim=(-.13,.13),ylim=(-1.25,1.25),xlabel="Parameter θ",ylabel="Velocity state v");ax.set_xticks([-.09,0,.09]);ax.set_yticks([-1,0,1]);ax.scatter([0,0],[1,-1],color="#2563EB",s=75,zorder=4);ax.scatter([-.09,.09],[.9,-.9],color="#059669",s=75,zorder=4)
        for a,b in [((0,1),(-.09,.9)),((0,-1),(.09,-.9))]:ax.annotate("",b,a,arrowprops=dict(arrowstyle="->",lw=2.5,color="#7C3AED",mutation_scale=14,shrinkB=8))
        fig.text(.077,.95,"Same θ, different next update",fontsize=27);fig.text(.077,.865,"v′ = 0.9v + g; g = 0",fontsize=28);fig.text(.077,.80,"θ′ = θ − 0.1v′",fontsize=28);fig.text(.077,.17,"Blue: (0, 1), (0, −1)",fontsize=27,color="#2563EB");fig.text(.077,.10,"Green: (−0.09, 0.9)",fontsize=26,color="#059669");fig.text(.077,.045,"and (0.09, −0.9)",fontsize=26,color="#059669")
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
