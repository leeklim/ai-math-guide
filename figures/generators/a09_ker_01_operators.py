"""Reproduce pointwise function operations and finite evaluation examples."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, PURPLE, GREEN = "#2563EB", "#7C3AED", "#059669"
GRAY, GRID = "#64748B", "#D9E2EF"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    name = args.output.stem.removeprefix("A09-KER-01-")
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 26,
                         "svg.fonttype": "none", "svg.hashsalt": "a09-ker-01",
                         "axes.spines.top": False, "axes.spines.right": False})
    normal = name in {"pointwise-combination", "evaluation-not-function"}
    if normal:
        fig, ax = plt.subplots(figsize=(7.2, 10))
        axes = [ax]
        fig.subplots_adjust(left=.23, right=.94, bottom=.42, top=.77)
    else:
        fig, axes = plt.subplots(1, 2, figsize=(14.5, 8.5))
        fig.subplots_adjust(left=.09, right=.95, bottom=.35, top=.77, wspace=.44)
    x = np.linspace(-1, 2, 160)
    if name == "pointwise-combination":
        ax.plot(x, 1+x, color=BLUE, lw=3, label="f=1+x")
        ax.plot(x, x*x, color=PURPLE, ls="--", lw=3, label="g=x²")
        ax.plot(x, 3+3*x-2*x*x, color=GREEN, ls="-.", lw=3, label="3f−2g")
        ax.axvline(1, color=GRAY, ls=":", lw=2)
        ax.scatter([1,1,1], [2,1,4], c=[BLUE,PURPLE,GREEN], s=50, zorder=5)
        ax.set_title("Add functions pointwise\nat the same input x", fontsize=26, pad=27)
        ax.set_xlabel("input x", fontsize=26); ax.set_ylabel("function value", fontsize=25)
        ax.set_xticks([-1,0,1,2]); ax.grid(color=GRID)
        fig.legend(loc="lower center", bbox_to_anchor=(.53,.14), fontsize=24, frameon=False)
        fig.text(.5,.07,"At x=1: 3·2−2·1=4\nThe green curve is one function.", ha="center", fontsize=24)
    elif name == "evaluation-not-function":
        ax.plot(x, 2-3*x, color=BLUE, lw=3)
        ax.axvline(-1,color=GRAY,ls=":"); ax.axhline(5,color=GRAY,ls=":")
        ax.scatter([-1],[5],color=GREEN,s=60,zorder=5)
        ax.set_xticks([-1,0,1,2]); ax.set_yticks([-4,0,5]); ax.grid(color=GRID)
        ax.set_xlabel("input x",fontsize=26); ax.set_ylabel("f(x)",fontsize=26)
        ax.set_title("A function is the whole rule\nE₋₁ extracts one value",fontsize=25,pad=27)
        fig.text(.5,.11,"f(x)=2−3x\ncoordinates in (1,x): (2,−3)\nevaluation E₋₁(f)=5",ha="center",fontsize=25)
    elif name == "linear-versus-square":
        ax,bx=axes
        for a in axes:
            a.set_xlabel("input x",fontsize=23); a.set_ylabel("output value",fontsize=23)
            a.set_xticks([-1,0,1,2]); a.grid(color=GRID)
        ax.plot(x,3-4*x,color=GREEN,lw=4,label="(3f−2g)′")
        ax.plot(x,3-4*x,color=PURPLE,ls="--",lw=2,label="3f′−2g′")
        ax.set_title("Differentiation is linear\nf=1+x, g=x²",fontsize=23,pad=27)
        ax.legend(fontsize=22,loc="lower left",frameon=False)
        bx.plot(x,np.full_like(x,4),color=GREEN,lw=3,label="T(2f)=4")
        bx.plot(x,np.full_like(x,2),color=PURPLE,ls="--",lw=3,label="2T(f)=2")
        bx.set_ylim(0,5); bx.set_title("Squaring is nonlinear\nf(x)=1, T(f)=f²",fontsize=23,pad=27)
        bx.legend(fontsize=22,loc="lower left",frameon=False)
        fig.text(.5,.10,"Left: combining before or after differentiation gives the same curve.\nRight: doubling a function before squaring does not double the result.",ha="center",fontsize=23)
    elif name == "parameter-versus-output":
        ax,bx=axes
        theta=np.array([[1.,2.],[2.,1.]])
        ax.scatter(theta[:,0],theta[:,1],color=[BLUE,PURPLE],s=90,zorder=5)
        ax.plot(theta[:,0],theta[:,1],"--",color=GRAY)
        ax.set_xlim(.3,2.7); ax.set_ylim(.3,2.7); ax.set_aspect("equal")
        ax.set_xticks([1,2]);ax.set_yticks([1,2]);ax.grid(color=GRID)
        ax.text(.6,2.35,"θ₁=(1,2)",fontsize=23,color=BLUE)
        ax.text(1.4,.6,"θ₂=(2,1)",fontsize=23,color=PURPLE)
        ax.set_xlabel("parameter a",fontsize=23);ax.set_ylabel("parameter b",fontsize=23)
        ax.set_title("Parameter distance √2\nf₍ₐ,ᵦ₎(x)=abx",fontsize=23,pad=27)
        bx.plot(x,2*x,color=BLUE,lw=4,label="θ₁")
        bx.plot(x,2*x,color=PURPLE,ls="--",lw=2,label="θ₂")
        bx.set_xlabel("input x",fontsize=23);bx.set_ylabel("output fθ(x)",fontsize=23)
        bx.grid(color=GRID);bx.legend(fontsize=23,frameon=False)
        bx.set_title("Same function: both 2x\nOutput difference 0",fontsize=23,pad=27)
        fig.text(.5,.10,"Different parameters can represent exactly the same function.\nThis is an explicit toy example, not a claim about every checkpoint.",ha="center",fontsize=23)
    elif name == "finite-prompts-not-equality":
        fig.subplots_adjust(left=.13, right=.97, wspace=.50)
        ax,bx=axes
        for a in axes:
            a.grid(color=GRID);a.set_xlabel("input x",fontsize=23);a.set_ylabel("output",fontsize=23)
            a.set_xticks([0,.5,1])
        ax.plot(x,np.zeros_like(x),color=BLUE,lw=3,label="f(x)=0")
        ax.plot(x,x*(x-1),color=PURPLE,ls="--",lw=3,label="g(x)=x(x−1)")
        ax.scatter([0,1],[0,0],color=GREEN,s=75,zorder=5)
        ax.set_xlim(-.2,1.2);ax.set_ylim(-.4,.4);ax.legend(fontsize=22,frameon=False,loc="upper center")
        ax.set_title("Test inputs {0,1}\nBoth outputs are 0",fontsize=23,pad=27)
        bx.plot(x,x*(x-1),color=PURPLE,lw=3)
        bx.scatter([.5],[-.25],color=GREEN,s=70,zorder=5)
        bx.set_xlim(-.2,1.2);bx.set_ylim(-.4,.4)
        bx.set_title("Untested input x=0.5\ng−f=−0.25",fontsize=23,pad=27)
        fig.text(.5,.10,"Zero difference on a finite prompt set is not equality of functions.\nWhich inputs receive weight changes the measured function difference.",ha="center",fontsize=23)
    else:
        raise ValueError(name)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,format="svg",metadata={"Date":None});plt.close(fig)


if __name__ == "__main__":
    main()
