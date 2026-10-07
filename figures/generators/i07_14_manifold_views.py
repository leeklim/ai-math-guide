"""Reproduce geometric intervention checks and the fixed CPU toy in I07-14."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-14-manifold","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE,PURPLE,GREEN,AMBER,RED,GRAY="#2563EB","#7C3AED","#059669","#D97706","#DC2626","#64748B"
def main(output):
    key=output.stem.removeprefix("I07-14-");fig=plt.figure(figsize=(520/72,1100/72),facecolor="#F8FAFC")
    ax=fig.add_axes((.20,.35,.68,.46),facecolor="#F8FAFC")
    if key=="effect-and-validity":
        pts=[(0,6,"Clean",BLUE),(0,2,"Valid",GREEN),(np.sqrt(2),-4,"Mixed",RED)]
        ax.set(xlim=(-.2,2.1),ylim=(-6,9),xlabel="Manifold distance",ylabel="CPU output Y");ax.set_xticks([0,np.sqrt(2)],["0","√2"]);ax.set_yticks([-4,0,2,6]);ax.grid(color="#CBD5E1",alpha=.7)
        for x,y,s,col in pts:ax.scatter([x],[y],color=col,s=70,zorder=4);ax.text(x+.08,y+.55,s,color=col,fontsize=27)
        title="Effect and validity are separate";lines=[("Y = h₁ + h₂ + 4h₁h₂",GRAY),("Clean 6; valid 2; mixed −4",GRAY),("Mixed-state distance = √2",RED)]
    else:
        lim=(-3.7,1.1) if key=="on-line-but-rare" else (-1.6,1.6);ax.set(xlim=lim,ylim=lim,xlabel="Coordinate h₁",ylabel="Coordinate h₂");ax.set_aspect("equal");z=np.linspace(*lim,150);ax.plot(z,z,color=GRAY,ls="--",lw=2);ax.grid(color="#CBD5E1",alpha=.7);ax.set_xticks([-3,0,1] if key=="on-line-but-rare" else [-1,0,1]);ax.set_yticks([-3,0,1] if key=="on-line-but-rare" else [-1,0,1])
        if key=="coordinate-mixing":
            for x,y,s,col,lx,ly in [(1,1,"Clean",BLUE,-.15,1.24),(-1,-1,"Valid",GREEN,-1.4,-.7),(1,-1,"Mixed",RED,.47,-1.4)]:ax.scatter([x],[y],color=col,s=70,zorder=4);ax.text(lx,ly,s,color=col,fontsize=27)
            ax.plot([1,1],[1,-1],color=RED,ls=":",lw=2);title="Coordinates can break a relation";lines=[("Line: h₁ = h₂",GRAY),("Source states: (1,1), (−1,−1)",GRAY),("Mixed coordinates: (1,−1)",RED)]
        elif key=="perpendicular-distance":
            ax.scatter([1,0],[-1,0],color=[RED,GREEN],s=80,zorder=4);ax.plot([1,0],[-1,0],color=AMBER,ls=":",lw=2.6);ax.text(.5,-1.4,"(1,−1)",color=RED,fontsize=27);ax.text(-1.3,.23,"(0,0)",color=GREEN,fontsize=27);ax.text(.64,-.21,"√2",color=AMBER,fontsize=28);title="Distance is a perpendicular residual";lines=[("Closest z = (1 + (−1))/2 = 0",GRAY),("Residual = (1,−1); norm √2",AMBER),("Original and closest points differ.",GRAY)]
        elif key=="on-line-but-rare":
            refs=np.linspace(-.5,.5,13);ax.scatter(refs,refs,color=BLUE,s=30,zorder=4);ax.scatter([-3],[-3],color=RED,s=90,zorder=5);ax.plot([-3,-.5],[-3,-.5],color=AMBER,ls=":",lw=3);ax.text(-3.3,-2.6,"P",color=RED,fontsize=28);ax.text(-2.0,.74,"Reference",color=BLUE,fontsize=26);title="On a line is not the same as common";lines=[("Illustrative z ∈ [−0.5, 0.5]",GRAY),("P = (−3,−3): line distance 0",RED),("Nearest sample: distance 2.5√2",AMBER)]
        elif key=="projection-changes-patch":
            ax.scatter([1,0],[-1,0],color=[RED,GREEN],s=85,zorder=4);ax.plot([1,0],[-1,0],color=AMBER,ls=":",lw=2.6);ax.text(.45,-1.4,"Patch",color=RED,fontsize=27);ax.text(-1.35,.25,"Projected",color=GREEN,fontsize=26);title="Projection changes both coordinates";lines=[("(1,−1) → (0,0)",AMBER),("Both h₁ and h₂ change.",GRAY),("CPU Y: −4 → 0; a new intervention",GREEN)]
        else:raise ValueError(key)
    fig.text(.077,.95,title,fontsize=26)
    for y,(s,col) in zip([.23,.16,.08],lines):fig.text(.077,y,s,fontsize=26,color=col)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
