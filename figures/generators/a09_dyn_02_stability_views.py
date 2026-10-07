"""Visualize fixed-point tests and distinct stability questions."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"a09-dyn-02-stability","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#2563EB";PURPLE="#7C3AED";GREEN="#059669";AMBER="#D97706";GRAY="#64748B";BG="#F8FAFC"
def axes(fig,rect):
    ax=fig.add_axes(rect,facecolor=BG);ax.grid(color="#CBD5E1",alpha=.65);return ax
def main(output):
    key=output.stem.removeprefix("A09-DYN-02-")
    h=1250 if key=="fixed-point-checks" else 1650 if key=="cubic-localization" else 1000 if key=="boundary-cubic-directions" else 960
    fig=plt.figure(figsize=(520/72,h/72),facecolor=BG)
    if key=="fixed-point-checks":
        x=np.linspace(-1.2,1.2,200)
        ax=axes(fig,(.23,.57,.65,.25));ax.plot(x,-3*x,color=PURPLE,lw=3);ax.axhline(0,color=GRAY,lw=1.3);ax.scatter([0],[0],color=GREEN,s=100,zorder=5);ax.set(xlim=(-1.3,1.3),ylim=(-4,4),xlabel="State x",ylabel="Velocity f(x)");ax.set_xticks([-1,0,1]);ax.set_yticks([-3,0,3])
        ax=axes(fig,(.23,.16,.65,.25));ax.plot(x,.5*x,color=GREEN,lw=3);ax.plot(x,x,"--",color=GRAY,lw=2);ax.scatter([0],[0],color=BLUE,s=100,zorder=5);ax.set(xlim=(-1.3,1.3),ylim=(-1.3,1.3),xlabel="Input state x",ylabel="Next state F(x)");ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
        fig.text(.077,.95,"Two fixed-point conditions",fontsize=28);fig.text(.077,.865,"Continuous: f(x*) = 0",fontsize=28,color=PURPLE);fig.text(.077,.465,"Discrete: F(x*) = x*",fontsize=28,color=GREEN);fig.text(.077,.43,"Dashed: identity",fontsize=24,color=GRAY);fig.text(.077,.055,"Stopping is not a stability proof.",fontsize=26,color=GRAY)
    elif key=="cubic-localization":
        delta=np.linspace(-.3,.3,200)
        for y,xstar,col in [(.68,-1,BLUE),(.40,0,PURPLE),(.12,1,GREEN)]:
            ax=axes(fig,(.23,y,.65,.18));x=xstar+delta;a=1-3*xstar*xstar;ax.plot(delta,x-x**3,color=col,lw=3);ax.plot(delta,a*delta,"--",color=GRAY,lw=2);ax.scatter([0],[0],s=70,color=col,zorder=4);ax.set(xlim=(-.32,.32),ylim=(-.9,.9),xlabel="Displacement δx",ylabel="Velocity");ax.set_xticks([-.3,0,.3]);ax.set_yticks([-.6,0,.6]);fig.text(.077,y+.20,f"x* = {xstar}; A = {a}",fontsize=28,color=col)
        fig.text(.077,.965,"Same displacement, local slopes",fontsize=27);fig.text(.077,.925,"f(x) = x − x³",fontsize=28);fig.text(.077,.04,"Dashed: A δx; solid: exact velocity.",fontsize=24,color=GRAY)
    elif key=="continuous-eigenmodes":
        ax=axes(fig,(.22,.25,.66,.44));t=np.linspace(0,1.2,250);ax.plot(t,np.exp(-t),color=GREEN,lw=3);ax.plot(t,np.exp(2*t),"--",color=PURPLE,lw=3);ax.set(xlim=(0,1.25),ylim=(0,12),xlabel="Time t",ylabel="Mode coefficient c(t)");ax.set_xticks([0,.5,1]);ax.set_yticks([0,1,5,10]);ax.scatter([0],[1],s=70,color=BLUE,zorder=4)
        fig.text(.077,.95,"Continuous modes: exp(λt)",fontsize=28);fig.text(.077,.855,"λ = −1: exp(−t)  —",color=GREEN,fontsize=28);fig.text(.077,.79,"λ = 2: exp(2t)  - -",color=PURPLE,fontsize=28);fig.text(.077,.13,"A = diag(−1, 2); c(0) = 1",fontsize=26);fig.text(.077,.06,"One growing mode makes a saddle.",fontsize=25,color=GRAY)
    elif key=="discrete-eigenmodes":
        ax=axes(fig,(.22,.26,.67,.43));k=np.arange(9)
        for lam,col,style in [(.5,GREEN,"o-"),(-.5,PURPLE,"s--"),(1.2,AMBER,"^-.")]:ax.plot(k,lam**k,style,color=col,lw=2.5,ms=6)
        ax.set(xlim=(-.2,8.3),ylim=(-1,4.6),xlabel="Step k",ylabel="Mode coefficient cₖ");ax.set_xticks([0,2,4,6,8]);ax.set_yticks([0,1,2,4]);ax.axhline(0,color=GRAY,lw=1)
        fig.text(.077,.95,"Discrete modes: λᵏ",fontsize=28);fig.text(.077,.87,"λ = 0.5  o —",fontsize=28,color=GREEN);fig.text(.077,.81,"λ = −0.5  □ - -",fontsize=28,color=PURPLE);fig.text(.077,.75,"λ = 1.2  △ - ·",fontsize=28,color=AMBER)
        fig.text(.077,.13,"Same initial coefficient c₀ = 1.",fontsize=26);fig.text(.077,.065,"Decay uses |λ| < 1, not λ < 0.",fontsize=25,color=GRAY)
    elif key in ("continuous-stability-region","discrete-stability-region"):
        ax=axes(fig,(.23,.30,.65,.43));ax.set_aspect("equal");ax.set(xlim=(-1.65,1.65),ylim=(-1.65,1.65),xlabel="Real part Re λ",ylabel="Imaginary part Im λ");ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.axhline(0,color=GRAY,lw=1.2)
        if key=="continuous-stability-region":
            ax.axvspan(-1.65,0,facecolor=GREEN,alpha=.12);ax.axvline(0,color=AMBER,lw=2,ls="--");ax.text(-.82,1.25,"Re < 0",ha="center",fontsize=26,color=GREEN)
            fig.text(.077,.95,"Continuous strict decay region",fontsize=27);fig.text(.077,.86,"Magnitude ∝ exp(Re(λ) t)",fontsize=27,color=GREEN);fig.text(.077,.16,"Dashed: Re λ = 0 boundary",fontsize=26,color=AMBER);fig.text(.077,.08,"Imaginary part may be nonzero.",fontsize=26,color=GRAY)
        else:
            circ=plt.Circle((0,0),1,facecolor=GREEN,edgecolor=AMBER,lw=2,ls="--",alpha=.15);ax.add_patch(circ);theta=np.linspace(0,2*np.pi,300);ax.plot(np.cos(theta),np.sin(theta),"--",color=AMBER,lw=2);ax.scatter([.5],[.5],color=BLUE,s=90,zorder=4)
            fig.text(.077,.95,"Discrete strict decay region",fontsize=27);fig.text(.077,.86,"Magnitude ∝ |λ|ᵏ",fontsize=28,color=GREEN);fig.text(.077,.80,"Dot: 0.5 + 0.5i",fontsize=27,color=BLUE);fig.text(.077,.16,"Inside disk: |λ| < 1",fontsize=28,color=GREEN);fig.text(.077,.08,"Positive real part can still decay.",fontsize=25,color=GRAY)
    elif key=="transient-norm-growth":
        b=np.array([[.5,3],[0,.5]]);x=np.array([0.,1.]);norms=[np.linalg.norm(x)]
        for _ in range(12):x=b@x;norms.append(np.linalg.norm(x))
        ax=axes(fig,(.22,.26,.66,.43));ax.plot(range(13),norms,"o-",color=PURPLE,lw=2.8,ms=7);ax.axhline(1,color=GRAY,ls="--",lw=1.3);ax.set(xlim=(-.3,12.3),ylim=(0,3.6),xlabel="Step k",ylabel="Euclidean norm");ax.set_xticks([0,3,6,9,12]);ax.set_yticks([0,1,2,3])
        fig.text(.077,.95,"Transient growth before decay",fontsize=27);fig.text(.077,.865,"B = [[0.5, 3], [0, 0.5]]",fontsize=27);fig.text(.077,.80,"δx₀ = (0, 1); both λ = 0.5",fontsize=26);fig.text(.077,.15,"‖δx₁‖ = √9.25 ≈ 3.04",fontsize=27,color=PURPLE);fig.text(.077,.07,"Not every step shrinks the norm.",fontsize=25,color=GRAY)
    elif key=="boundary-cubic-directions":
        for y,sign,col in [(.59,-1,GREEN),(.25,1,PURPLE)]:
            ax=axes(fig,(.18,y,.72,.15));ax.set(xlim=(-1.5,1.5),ylim=(-.3,.3),xlabel="State x");ax.set_xticks([-1,0,1]);ax.set_yticks([]);ax.axhline(0,color=GRAY,lw=1.2);ax.scatter([0],[0],s=80,color=col,zorder=4)
            for start,end in ([(-1.2,-.5),(.5,1.2)] if sign==1 else [(-1.2,-.5),(1.2,.5)]):
                if sign==1 and start<0:start,end=-.5,-1.2
                ax.annotate("",(end,0),(start,0),arrowprops=dict(arrowstyle="->",color=col,lw=2.7,mutation_scale=15))
            fig.text(.077,y+.20,"dx/dt = "+("−x³" if sign==-1 else "x³"),fontsize=28,color=col)
        fig.text(.077,.95,"Same zero slope, opposite flow",fontsize=27);fig.text(.077,.88,"At x* = 0, both f′(0) = 0.",fontsize=28);fig.text(.077,.08,"Higher-order signs decide here.",fontsize=26,color=GRAY)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
