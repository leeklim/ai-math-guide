"""Draw distinct state, time, and control-parameter views."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-dyn-03-portrait","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect):
    ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def phase(ax,arrows,roots,labels):
    ax.axhline(0,color=GRAY,lw=1.2);ax.set(xlim=(-1.7,1.7),ylim=(-.3,.3),xlabel="State x");ax.set_xticks([-1,0,1]);ax.set_yticks([])
    for start,end in arrows:ax.annotate("",(end,0),(start,0),arrowprops=dict(arrowstyle="->",color=PURPLE,lw=2.5,mutation_scale=12))
    for x,stable in roots:ax.scatter([x],[0],s=100,facecolors=GREEN if stable else BG,edgecolors=GREEN if stable else PURPLE,lw=2,zorder=5)
    for x,label in labels:ax.text(x,.16,label,ha="center",fontsize=24,color=GRAY)
def main(output):
    key=output.stem.removeprefix("A09-DYN-03-");h=1300 if key.endswith("phase-lines") else 980
    fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="logistic-phase-line":
        ax=axes(fig,(.17,.40,.73,.20));ax.axhline(0,color=GRAY,lw=1.2);ax.set(xlim=(-1,2.2),ylim=(-.5,.5),xlabel="State x");ax.set_xticks([0,1,2]);ax.set_yticks([])
        for start,end in [(-.2,-.8),(.2,.8),(1.9,1.3)]:ax.annotate("",(end,0),(start,0),arrowprops=dict(arrowstyle="->",color=PURPLE,lw=2.5,mutation_scale=12))
        ax.scatter([0,1],[0,0],s=100,facecolors=[BG,GREEN],edgecolors=[PURPLE,GREEN],lw=2,zorder=5);ax.text(-.5,.25,"f < 0",fontsize=25,ha="center",color=PURPLE);ax.text(.5,.25,"f > 0",fontsize=25,ha="center",color=PURPLE);ax.text(1.7,.25,"f < 0",fontsize=25,ha="center",color=PURPLE)
        fig.text(.077,.95,"Logistic state directions",fontsize=28);fig.text(.077,.865,"dx/dt = x(1 − x)",fontsize=28)
        fig.text(.077,.72,"○ x* = 0: repels nearby states",fontsize=25,color=PURPLE);fig.text(.077,.66,"● x* = 1: attracts nearby states",fontsize=25,color=GREEN)
        fig.text(.077,.22,"Basin of 1: x₀ > 0",fontsize=28,color=GREEN);fig.text(.077,.13,"x₀ = 0 stays at zero.",fontsize=27,color=GRAY);fig.text(.077,.055,"Negative states do not go to 1.",fontsize=25,color=GRAY)
    elif key=="two-dimensional-portrait":
        ax=axes(fig,(.23,.27,.65,.43));ax.set_aspect("equal");ax.set(xlim=(-1.55,1.55),ylim=(-1.55,1.55),xlabel="State x",ylabel="State y");ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.axhline(0,color=BLUE,lw=2,ls="--");ax.axvline(0,color=GRAY,lw=1)
        for x0,y0,col in [(1.3,1.2,GREEN),(-1.3,1.2,PURPLE),(1.3,-1.2,AMBER),(-1.3,-1.2,GREEN)]:
            t=np.linspace(0,3,200);ax.plot(x0*np.exp(-t),y0*np.exp(-2*t),color=col,lw=2.3);ax.scatter([x0],[y0],color=col,s=35,zorder=3)
        for x in [-1,1]:
            for y in [-1,0,1]:ax.annotate("",(x-.3*x,y-.6*y),(x,y),arrowprops=dict(arrowstyle="->",color=GRAY,lw=1.6,mutation_scale=8))
        ax.scatter([0],[0],color=GREEN,s=75,zorder=5)
        fig.text(.077,.95,"A phase portrait uses state axes",fontsize=26);fig.text(.077,.865,"dx/dt = −x; dy/dt = −2y",fontsize=27);fig.text(.077,.79,"Curves: exact example trajectories",fontsize=24,color=GRAY)
        fig.text(.077,.16,"Dashed axis y = 0 is invariant.",fontsize=25,color=BLUE);fig.text(.077,.09,"Arrows show the field direction.",fontsize=25,color=GRAY);fig.text(.077,.03,"Neither axis is time.",fontsize=26,color=GRAY)
    elif key=="logistic-basin-trajectories":
        ax=axes(fig,(.21,.25,.67,.47));t=np.linspace(0,5,250)
        for x0,col,style in [(.2,BLUE,"-"),(.8,PURPLE,"--"),(1.8,GREEN,"-.")]:ax.plot(t,x0/(x0+(1-x0)*np.exp(-t)),style,color=col,lw=3)
        ax.axhline(0,color=GRAY,lw=2,ls=":");ax.axhline(1,color=GRAY,lw=1.3);ax.set(xlim=(0,5.1),ylim=(-.1,2),xlabel="Time t",ylabel="State x(t)");ax.set_xticks([0,2,4]);ax.set_yticks([0,1,2])
        fig.text(.077,.95,"Different starts, one attractor",fontsize=27);fig.text(.077,.865,"x₀ = 0.2 —",fontsize=27,color=BLUE);fig.text(.077,.805,"x₀ = 0.8 - -",fontsize=27,color=PURPLE);fig.text(.50,.865,"x₀ = 1.8 - ·",fontsize=27,color=GREEN)
        fig.text(.077,.16,"Dotted: x₀ = 0 stays at zero.",fontsize=26,color=GRAY);fig.text(.077,.09,"Positive starts approach 1.",fontsize=27,color=GREEN);fig.text(.077,.035,"The basin is an initial-state set.",fontsize=25,color=GRAY)
    elif key in ("saddle-node-branches","pitchfork-branches"):
        ax=axes(fig,(.23,.28,.65,.43));ax.set(xlim=(-1.1,2.2),ylim=(-1.65,1.65),xlabel="Control parameter μ",ylabel="Fixed state x*");ax.set_xticks([-1,0,1,2]);ax.set_yticks([-1,0,1]);mu=np.linspace(0,2,250)
        if key=="saddle-node-branches":
            ax.plot(mu,np.sqrt(mu),color=GREEN,lw=3);ax.plot(mu,-np.sqrt(mu),"--",color=PURPLE,lw=3);ax.scatter([0],[0],facecolors=BG,edgecolors=AMBER,lw=2,s=100,zorder=5)
            fig.text(.077,.95,"Saddle-node branches",fontsize=28);fig.text(.077,.865,"Stable +√μ  —",fontsize=28,color=GREEN);fig.text(.077,.80,"Unstable −√μ  - -",fontsize=28,color=PURPLE);fig.text(.077,.16,"μ < 0: no real fixed points.",fontsize=26,color=GRAY);fig.text(.077,.09,"μ = 0: one-sided approach.",fontsize=26,color=AMBER)
        else:
            ax.plot(np.linspace(-1,0,100),np.zeros(100),color=GREEN,lw=3);ax.plot(mu,np.zeros(len(mu)),"--",color=PURPLE,lw=3);ax.plot(mu,np.sqrt(mu),color=GREEN,lw=3);ax.plot(mu,-np.sqrt(mu),color=GREEN,lw=3);ax.scatter([0],[0],color=GREEN,s=85,zorder=5)
            fig.text(.077,.95,"Supercritical pitchfork branches",fontsize=26);fig.text(.077,.865,"Stable —; unstable - -",fontsize=28);fig.text(.077,.80,"x* = 0 and x* = ±√μ",fontsize=28);fig.text(.077,.16,"μ > 0: two new stable branches.",fontsize=25,color=GREEN);fig.text(.077,.09,"μ = 0: use the nonlinear signs.",fontsize=25,color=AMBER)
        fig.text(.077,.035,"Horizontal axis is not time.",fontsize=26,color=GRAY)
    elif key=="saddle-node-phase-lines":
        phase(axes(fig,(.17,.66,.73,.12)),[(-.8,-1.4),(.6,0),(1.4,.8)],[],[]);fig.text(.077,.825,"μ = −1: no fixed point",fontsize=28)
        ax=axes(fig,(.17,.40,.73,.12));phase(ax,[(-.5,-1.2),(1.2,.5)],[],[]);ax.scatter([0],[0],s=110,facecolors=BG,edgecolors=AMBER,lw=2,zorder=5);fig.text(.077,.565,"μ = 0: f = −x²",fontsize=28,color=AMBER)
        phase(axes(fig,(.17,.14,.73,.12)),[(-1.3,-1.6),(-.6,0),(.2,.7),(1.6,1.25)],[(-1,False),(1,True)],[]);fig.text(.077,.305,"μ = 1: two fixed points",fontsize=28)
        fig.text(.077,.955,"Saddle-node state phase lines",fontsize=27);fig.text(.077,.04,"At μ = 0, both sides flow left.",fontsize=26,color=GRAY)
    elif key=="pitchfork-phase-lines":
        phase(axes(fig,(.17,.66,.73,.12)),[(-1.3,-.5),(1.3,.5)],[(0,True)],[]);fig.text(.077,.825,"μ = −1: f′(0) = −1",fontsize=28)
        phase(axes(fig,(.17,.40,.73,.12)),[(-1.3,-.5),(1.3,.5)],[(0,True)],[]);fig.text(.077,.565,"μ = 0: f′(0) = 0",fontsize=28,color=AMBER)
        phase(axes(fig,(.17,.14,.73,.12)),[(-1.6,-1.25),(-.25,-.75),(.25,.75),(1.6,1.25)],[(-1,True),(0,False),(1,True)],[]);fig.text(.077,.305,"μ = 1: origin repels",fontsize=28,color=PURPLE)
        fig.text(.077,.955,"Pitchfork state phase lines",fontsize=27);fig.text(.077,.04,"Critical does not mean unstable.",fontsize=26,color=GRAY)
    elif key=="sparse-checkpoint-observations":
        ax=axes(fig,(.23,.29,.65,.43));k=np.array([1,2,3]);score=np.array([.5,.5,.9]);ax.plot(k,score,"--",color=GRAY,lw=1.8);ax.scatter(k,score,color=BLUE,s=100,zorder=5);ax.axvspan(2,3,color=AMBER,alpha=.08);ax.set(xlim=(.8,3.2),ylim=(.35,1),xlabel="Checkpoint index",ylabel="Observed probe score");ax.set_xticks([1,2,3]);ax.set_yticks([.5,.9]);ax.text(2.5,.41,"Unresolved",ha="center",fontsize=24,color=AMBER)
        fig.text(.077,.95,"Three observations are not a flow",fontsize=26);fig.text(.077,.865,"Dots: 0.5, 0.5, 0.9",fontsize=28,color=BLUE);fig.text(.077,.80,"Dashed: interpolation only",fontsize=26,color=GRAY);fig.text(.077,.17,"Change lies between indices 2 and 3.",fontsize=24,color=AMBER);fig.text(.077,.095,"No fixed-parameter family measured.",fontsize=24,color=GRAY);fig.text(.077,.03,"No bifurcation established.",fontsize=26,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
