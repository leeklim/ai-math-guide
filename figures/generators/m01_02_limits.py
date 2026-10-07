#!/usr/bin/env python3
"""Generate the individually selected limit diagrams for M01-02."""
from __future__ import annotations
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    output = parser.parse_args().output
    name = output.stem.removeprefix("M01-02-")
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 16,
                         "svg.fonttype": "none", "svg.hashsalt": "mmi-m01-02-" + name})
    fig, ax = plt.subplots(figsize=(8.6, 6.8))
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")
    title, footer, ylabel = "", "", "Output"
    if name == "approach-window":
        x = np.linspace(2.6, 3.4, 200)
        ax.axvspan(2.75, 3.25, color="#DBEAFE", alpha=0.8)
        ax.axhspan(6.5, 7.5, color="#D1FAE5", alpha=0.45)
        ax.plot(x, 2*x+1, color="#059669", lw=3)
        ax.axvline(3, color="#64748B", ls=":")
        ax.axhline(7, color="#7C3AED", ls="--")
        ax.scatter([3], [7], facecolor="#F8FAFC", edgecolor="#2563EB", s=90, zorder=5)
        ax.set(xlim=(2.6,3.4), ylim=(6.1,7.9), xticks=[2.75,3,3.25], yticks=[6.5,7,7.5])
        title, footer = "Nearby inputs give nearby outputs", "2.75 < x < 3.25 gives 6.5 < f(x) < 7.5."
        ylabel = "f(x) = 2x + 1"
    elif name in {"hole-and-value", "continuity-repair"}:
        x = np.linspace(0,2,160)
        ax.plot(x,x+1,color="#059669",lw=3)
        ax.axvline(1,color="#94A3B8",ls=":")
        ax.axhline(2,color="#7C3AED",ls="--")
        if name == "hole-and-value":
            ax.scatter([1],[2],facecolor="#F8FAFC",edgecolor="#059669",lw=2,s=110,zorder=5)
            ax.scatter([1],[7],color="#D97706",s=85,zorder=5)
            ax.annotate("g(1) = 7",(1,7),xytext=(1.28,6.3),fontsize=16,
                        arrowprops={"arrowstyle":"-","color":"#64748B"})
            ax.annotate("limit = 2",(1,2),xytext=(1.25,3.3),fontsize=16,
                        arrowprops={"arrowstyle":"-","color":"#64748B"})
            ax.set(xlim=(-0.05,2.15),ylim=(0,8),xticks=[0,1,2],yticks=[0,2,4,6,7])
            title, footer, ylabel = "Point value and nearby behavior differ", "The filled point does not change the limit.", "g(x)"
        else:
            ax.scatter([1],[2],color="#D97706",s=90,zorder=5)
            ax.annotate("f(1) = limit = 2",(1,2),xytext=(0.2,3.35),fontsize=16,
                        arrowprops={"arrowstyle":"-","color":"#64748B"})
            ax.set(xlim=(-0.05,2.15),ylim=(0,4),xticks=[0,1,2],yticks=[0,1,2,3])
            title, footer, ylabel = "Fill the hole with the limiting value", "Defining f(1) = 2 makes this extension continuous.", "f(x)"
    elif name == "one-sided-jump":
        ax.plot([-1.5,0],[0,0],color="#2563EB",lw=3)
        ax.plot([0,1.5],[1,1],color="#059669",lw=3)
        ax.scatter([0],[0],facecolor="#F8FAFC",edgecolor="#2563EB",lw=2,s=110,zorder=5)
        ax.scatter([0],[1],color="#D97706",s=85,zorder=5)
        ax.annotate("left limit = 0",(-.5,0),xytext=(-1.45,-.47),fontsize=16,
                    arrowprops={"arrowstyle":"-","color":"#64748B"})
        ax.annotate("right limit = 1",(.5,1),xytext=(.2,1.48),fontsize=16,
                    arrowprops={"arrowstyle":"-","color":"#64748B"})
        ax.set(xlim=(-1.65,1.65),ylim=(-.7,1.8),xticks=[-1,0,1],yticks=[0,1])
        title, footer, ylabel = "Different one-sided limits", "s(0) = 1; the two-sided limit does not exist.", "s(x)"
    elif name in {"unbounded-square", "unbounded-reciprocal"}:
        left=np.linspace(-1.1,-.075,250)
        right=np.linspace(.075,1.1,250)
        square=name=="unbounded-square"
        for x in [left,right]:
            ax.plot(x,1/(x*x) if square else 1/x,color="#059669",lw=3)
        ax.axvline(0,color="#7C3AED",ls="--")
        ax.set(xlim=(-1.2,1.2),ylim=(0,18) if square else (-12,12),xticks=[-1,0,1])
        title="Both sides grow without bound" if square else "The two sides have opposite signs"
        footer="The graph continues upward outside this window." if square else "Left: negative unbounded; right: positive unbounded."
        ylabel="1 / x²" if square else "1 / x"
    elif name == "difference-quotient":
        h=np.linspace(-.8,.8,200)
        ax.plot(h,2+h,color="#7C3AED",lw=3)
        ax.scatter([0],[2],facecolor="#F8FAFC",edgecolor="#7C3AED",lw=2,s=110,zorder=5)
        ax.scatter([-.5,-.1,.1,.5],[1.5,1.9,2.1,2.5],color="#2563EB",s=65,zorder=4)
        ax.set(xlim=(-.9,.9),ylim=(1,3),xticks=[-.5,0,.5],yticks=[1,2,3])
        ax.set_xlabel("Input interval h (base input a = 1)",labelpad=14)
        title,footer,ylabel="A function of the nonzero interval h", "For f(x) = x²: quotient = 2 + h, with h ≠ 0.", "Average rate"
    else:
        raise ValueError(f"Unknown M01-02 figure: {name}")
    if name != "difference-quotient":
        ax.set_xlabel("Input x",labelpad=14)
    ax.set_ylabel(ylabel,labelpad=14)
    ax.set_title(title,fontsize=20,pad=24)
    ax.spines[["top","right"]].set_visible(False)
    ax.grid(color="#CBD5E1",lw=.7)
    fig.text(.5,.09,footer,ha="center",color="#334155",fontsize=16)
    fig.subplots_adjust(left=.17,right=.94,bottom=.24,top=.83)
    output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"mmi"})
    plt.close(fig)


if __name__ == "__main__":
    main()
