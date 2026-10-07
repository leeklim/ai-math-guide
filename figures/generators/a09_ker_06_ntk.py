"""Reproduce parameter-gradient coupling and fixed-kernel mode dynamics."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE,PURPLE,GREEN="#2563EB","#7C3AED","#059669"
GRID,GRAY="#D9E2EF","#64748B"


def arrow(ax,start,end,color):
    ax.annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":"->","color":color,
        "lw":2.8,"mutation_scale":12,"shrinkA":0,"shrinkB":0},zorder=5)


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();name=args.output.stem.removeprefix("A09-KER-06-")
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none",
        "svg.hashsalt":"a09-ker-06","axes.spines.top":False,"axes.spines.right":False})
    wide=name in {"gradient-gram","coupled-step","current-versus-fixed"}
    if wide:
        fig,axes=plt.subplots(1,2,figsize=(14.5,10.5));fig.subplots_adjust(left=.12,right=.96,bottom=.37,top=.73,wspace=.55)
    else:
        fig,ax=plt.subplots(figsize=(7.2,11));axes=[ax];fig.subplots_adjust(left=.24,right=.94,bottom=.43,top=.77)
    if name=="gradient-features":
        for end,c in [((1,0),BLUE),((1,1),PURPLE),((-1,0),GREEN)]:arrow(ax,(0,0),end,c)
        ax.text(.13,-.3,"g₁=(1,0)",fontsize=25,color=BLUE)
        ax.text(.1,1.35,"g₂=(1,1)",fontsize=25,color=PURPLE)
        ax.text(-1.42,.3,"g₃=(−1,0)",fontsize=25,color=GREEN)
        ax.set_xlim(-1.5,1.6);ax.set_ylim(-.6,1.8);ax.set_aspect("equal");ax.set_xticks([-1,0,1]);ax.set_yticks([0,1]);ax.grid(color=GRID)
        ax.set_xlabel("gradient ∂f/∂w₁",fontsize=25);ax.set_ylabel("gradient ∂f/∂w₂",fontsize=25)
        ax.set_title("Parameter gradients as features\nLinear toy: f_w(x)=w·x",fontsize=24,pad=27)
        fig.text(.5,.12,"K₁₂=g₁·g₂=1; K₁₃=−1\nK₂₂=‖g₂‖²=2\nThese are not input-gradient vectors.",ha="center",fontsize=24)
    elif name=="gradient-gram":
        j=np.array([[1,0],[1,1],[-1,0]]);k=j@j.T
        for ax,m,cols,title in zip(axes,[j,k],[["w₁","w₂"],["s₁","s₂","s₃"]],["J: sample × parameter\n3×2","K=JJᵀ: sample × sample\n3×3"]):
            n,d=m.shape;ax.pcolormesh(np.arange(d+1),np.arange(n+1),m,cmap="PuBu",vmin=-1,vmax=2,edgecolors=GRID,lw=2)
            ax.set_aspect("equal");ax.invert_yaxis();ax.set_xticks(np.arange(d)+.5,cols,fontsize=24);ax.set_yticks(np.arange(n)+.5,["s₁","s₂","s₃"],fontsize=24)
            ax.set_xlabel("column index",fontsize=24);ax.set_ylabel("sample row",fontsize=24);ax.set_title(title,fontsize=24,pad=27)
            for i in range(n):
                for z in range(d):ax.text(z+.5,i+.5,str(m[i,z]),ha="center",va="center",fontsize=28,color="white" if m[i,z]==2 else "#0F172A")
        fig.text(.5,.10,"Row dot products can give positive, zero, or negative coupling.\nK is still PSD: cᵀKc=‖Jᵀc‖². Its indices are samples, not neurons.",ha="center",fontsize=23)
    elif name=="coupled-step":
        ax,bx=axes;arrow(ax,(0,0),(1,1),BLUE);arrow(ax,(0,0),(-1,-1),PURPLE)
        ax.set_xlim(-1.4,1.4);ax.set_ylim(-1.4,1.4);ax.set_aspect("equal");ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.grid(color=GRID)
        ax.set_xlabel("parameter change Δw₁",fontsize=23);ax.set_ylabel("parameter change Δw₂",fontsize=23)
        ax.set_title("One sample update: ηr₂=1\nBlue g₂; purple Δθ=−g₂",fontsize=23,pad=27)
        bx.bar([0,1,2],[-1,-2,1],color=GREEN);bx.axhline(0,color=GRAY,lw=1);bx.grid(axis="y",color=GRID)
        bx.set_xticks([0,1,2],["s₁\nK₁₂=1","s₂\nK₂₂=2","s₃\nK₃₂=−1"],fontsize=22);bx.set_ylim(-2.4,1.5)
        bx.set_ylabel("output change Δfᵢ",fontsize=23);bx.set_title("Each output: Δfᵢ=−Kᵢ₂\nValues (−1,−2,+1)",fontsize=23,pad=27)
        fig.text(.5,.10,"Update from sample s₂ affects other samples through gradient inner products.\nExact in this linear toy; generally a first-order coupling statement.",ha="center",fontsize=23)
    elif name=="current-versus-fixed":
        ax,bx=axes;delta=np.linspace(-.5,.5,160)
        ax.plot(delta,(1+delta)**2,color=BLUE,lw=3,label="network fθ(1)")
        ax.plot(delta,1+2*delta,color=PURPLE,ls="--",lw=3,label="linearized model")
        bx.plot(delta,4*(1+delta)**2,color=BLUE,lw=3,label="current Kθ")
        bx.plot(delta,np.full_like(delta,4),color=PURPLE,ls="--",lw=3,label="fixed K₀=4")
        for a in axes:a.set_xticks([-.5,0,.5]);a.grid(color=GRID);a.set_xlabel("parameter displacement Δθ",fontsize=23);a.legend(fontsize=22,frameon=False)
        ax.set_ylabel("output at x=1",fontsize=23);bx.set_ylabel("scalar NTK",fontsize=23)
        ax.set_title("fθ(x)=θ²x, θ₀=1\nTaylor remainder (Δθ)²",fontsize=23,pad=27)
        bx.set_title("Gradient gθ(1)=2θ\nKθ(1,1)=4θ²",fontsize=23,pad=27)
        fig.text(.5,.10,"The affine Taylor model freezes its gradient feature; the nonlinear model does not.\nThis is a parameter sweep, not a measured training trajectory.",ha="center",fontsize=23)
    elif name=="mode-decay":
        fig.subplots_adjust(bottom=.49);t=np.linspace(0,3,200)
        for lam,c,ls in [(5,BLUE,"-"),(1,PURPLE,"--"),(0,GREEN,"-.")]:ax.plot(t,np.exp(-lam*t),color=c,ls=ls,lw=3,label=f"λ={lam}")
        ax.set_xticks([0,1,2,3]);ax.set_yticks([0,.5,1]);ax.set_ylim(-.05,1.1);ax.grid(color=GRID)
        ax.set_xlabel("gradient-flow time t",fontsize=24);ax.set_ylabel("residual mode a(t)",fontsize=24)
        ax.set_title("Exactly fixed kernel\na(0)=1, a(t)=exp(−λt)",fontsize=25,pad=27)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.145),fontsize=25,frameon=False)
        fig.text(.5,.065,"Large positive λ decays faster.\nA zero-eigenvalue residual remains.",ha="center",fontsize=24)
    elif name=="discrete-step-stability":
        fig.subplots_adjust(bottom=.49)
        steps=np.arange(7)
        for eta,c,ls in [(.1,BLUE,"-"),(.5,PURPLE,"--")]:ax.plot(steps,(1-5*eta)**steps,color=c,ls=ls,marker="o",lw=2.5,label=f"η={eta}")
        ax.set_xticks([0,2,4,6]);ax.set_yticks([-5,0,5,10]);ax.set_ylim(-9,13);ax.axhline(0,color=GRAY,lw=1);ax.grid(color=GRID)
        ax.set_xlabel("discrete iteration s",fontsize=25);ax.set_ylabel("residual mode a_s",fontsize=25)
        ax.set_title("Fixed scalar eigenvalue λ=5\nSame initial residual a₀=1",fontsize=24,pad=27)
        fig.legend(loc="lower center",bbox_to_anchor=(.5,.17),fontsize=25,frameon=False)
        fig.text(.5,.065,"a_next=(1−ηλ)a\nA large step can reverse and grow.\nContinuous decay ≠ stable steps.",ha="center",fontsize=24)
    else:raise ValueError(name)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,format="svg",metadata={"Date":None});plt.close(fig)


if __name__=="__main__":main()
