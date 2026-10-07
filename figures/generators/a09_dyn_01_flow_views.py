"""Draw exact scalar flows and Euler comparisons for A09-DYN-01."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-dyn-01-flow","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect):
    ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def main(output):
    key=output.stem.removeprefix("A09-DYN-01-");h=980 if key=="state-velocity" else 940
    fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="state-velocity":
        top=axes(fig,(.19,.64,.70,.20));top.set(xlim=(-2.6,2.6),ylim=(-.5,.5),xlabel="State x");top.set_xticks([-2,0,2]);top.set_yticks([]);top.axhline(0,color=GRAY,lw=1)
        top.scatter([-2,0,2],[0,0,0],s=65,color=[BLUE,GREEN,BLUE],zorder=3)
        for a,b in [(-2,-1),(2,1)]:top.annotate("",(b,0),(a,0),arrowprops=dict(arrowstyle="->",lw=2.4,color=PURPLE,mutation_scale=15))
        top.text(-2,.23,"f = 2",ha="center",fontsize=26,color=PURPLE);top.text(2,.23,"f = −2",ha="center",fontsize=26,color=PURPLE)
        ax=axes(fig,(.21,.16,.69,.30));x=np.linspace(-2.3,2.3,200);ax.plot(x,-x,color=PURPLE,lw=3);ax.scatter([-2,0,2],[2,0,-2],s=70,color=GREEN,zorder=4);ax.set(xlim=(-2.6,2.6),ylim=(-2.7,2.7),xlabel="State x",ylabel="Velocity f(x)");ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2])
        fig.text(.077,.94,"State and velocity are different",fontsize=27);fig.text(.077,.51,"Velocity rule f(x) = −x",fontsize=28,color=PURPLE);fig.text(.077,.055,"Neither horizontal axis is time.",fontsize=25,color=GRAY)
    elif key=="trajectory-time":
        ax=axes(fig,(.20,.23,.70,.49));t=np.linspace(0,3,250)
        for x0,col,style in [(2,BLUE,"-"),(1,PURPLE,"--"),(-1,GREEN,"-.")]:ax.plot(t,x0*np.exp(-t),style,color=col,lw=3);ax.scatter([0],[x0],color=col,s=65)
        ax.set(xlim=(-.1,3.15),ylim=(-1.3,2.4),xlabel="Time t",ylabel="State x(t)");ax.set_xticks([0,1,2,3]);ax.set_yticks([-1,0,1,2]);ax.axhline(0,color=GRAY,lw=1)
        fig.text(.077,.94,"Fix an initial state; vary time",fontsize=27)
        fig.text(.077,.85,"x₀ = 2  —",color=BLUE,fontsize=28);fig.text(.077,.80,"x₀ = 1  - -",color=PURPLE,fontsize=28);fig.text(.53,.85,"x₀ = −1  - ·",color=GREEN,fontsize=28)
        fig.text(.077,.11,"One curve per initial condition.",fontsize=25,color=GRAY);fig.text(.077,.055,"Exact solution x(t) = x₀ exp(−t).",fontsize=25,color=GRAY)
    elif key=="fixed-time-flow-map":
        ax=axes(fig,(.23,.25,.65,.49));x=np.linspace(-2.4,2.4,250);ax.plot(x,np.exp(-1)*x,color=GREEN,lw=3);ax.plot(x,x,"--",color=GRAY,lw=1.5)
        ax.scatter([-2,0,2],np.exp(-1)*np.array([-2,0,2]),s=70,color=BLUE,zorder=4);ax.set(xlim=(-2.6,2.6),ylim=(-1.3,1.3),xlabel="Initial state x₀",ylabel="State after t = 1");ax.set_xticks([-2,0,2]);ax.set_yticks([-1,0,1])
        fig.text(.077,.94,"Fix time; vary the initial state",fontsize=27);fig.text(.077,.85,"Φ₁(x₀) = exp(−1) x₀",color=GREEN,fontsize=28);fig.text(.077,.79,"Dashed: identity map",fontsize=25,color=GRAY)
        fig.text(.077,.14,"2 → 0.736;  −2 → −0.736",fontsize=28,color=BLUE);fig.text(.077,.065,"Slope exp(−1) ≈ 0.368.",fontsize=26,color=GRAY)
    elif key=="euler-tangent-step":
        ax=axes(fig,(.21,.27,.68,.46));t=np.linspace(0,.6,200);ax.plot(t,np.exp(-t),color=GREEN,lw=3);ax.plot(t,1-t,"--",color=PURPLE,lw=3);ax.scatter([0,.5,.5],[1,np.exp(-.5),.5],s=75,color=[BLUE,GREEN,PURPLE],zorder=5);ax.axvline(.5,color=GRAY,lw=1.3,ls=":");ax.set(xlim=(-.02,.62),ylim=(.3,1.1),xlabel="Time t",ylabel="State x");ax.set_xticks([0,.5],["0","h = 0.5"]);ax.set_yticks([.5,1])
        fig.text(.077,.94,"A finite step leaves the tangent",fontsize=27);fig.text(.077,.85,"Exact: exp(−t)",fontsize=28,color=GREEN);fig.text(.077,.79,"Euler tangent: 1 − t",fontsize=28,color=PURPLE)
        fig.text(.077,.15,"Exact end ≈ 0.607",fontsize=28,color=GREEN);fig.text(.077,.095,"Euler end = 0.5",fontsize=28,color=PURPLE);fig.text(.077,.04,"Same initial velocity −1.",fontsize=25,color=GRAY)
    elif key=="euler-alternating-sign":
        ax=axes(fig,(.21,.27,.68,.44));t=np.linspace(0,7.5,250);k=np.arange(6);ax.plot(t,np.exp(-t),color=GREEN,lw=3);ax.plot(1.5*k,(-.5)**k,"o--",color=PURPLE,lw=2.5,ms=8);ax.axhline(0,color=GRAY,lw=1.2);ax.set(xlim=(-.2,7.8),ylim=(-.7,1.2),xlabel="Time t = 1.5 k",ylabel="State x");ax.set_xticks([0,3,6]);ax.set_yticks([-.5,0,1])
        fig.text(.077,.94,"Positive flow; alternating Euler",fontsize=27);fig.text(.077,.85,"Exact flow  —",color=GREEN,fontsize=28);fig.text(.077,.79,"Euler h = 1.5  o - -",color=PURPLE,fontsize=28)
        fig.text(.077,.15,"Multiplier 1 − h = −0.5",fontsize=28,color=PURPLE);fig.text(.077,.09,"1 → −0.5 → 0.25 → −0.125",fontsize=25,color=PURPLE);fig.text(.077,.035,"Absolute values still shrink here.",fontsize=25,color=GRAY)
    elif key=="finite-time-boundary":
        ax=axes(fig,(.23,.25,.65,.49));t=np.linspace(0,.9,250);ax.plot(t,1/(1-t),color=GREEN,lw=3);ax.axvline(1,color=AMBER,lw=2,ls="--");ax.set(xlim=(-.03,1.08),ylim=(0,11),xlabel="Time t",ylabel="State x(t)");ax.set_xticks([0,.5,1]);ax.set_yticks([1,5,10]);ax.scatter([0],[1],color=BLUE,s=65)
        fig.text(.077,.94,"A local flow need not last forever",fontsize=26);fig.text(.077,.85,"dx/dt = x²; x₀ = 1",fontsize=28,color=GREEN);fig.text(.077,.79,"x(t) = 1 / (1 − t)",fontsize=28,color=GREEN)
        fig.text(.077,.14,"Forward domain: 0 ≤ t < 1",fontsize=27,color=AMBER);fig.text(.077,.07,"No finite state exists at t = 1.",fontsize=26,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
