"""Reproduce N05-13 two-pair rotations and position-dependent dot products."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch
BLUE,PURPLE,GREEN,ORANGE="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"n05-13-rope","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def arrow(ax,a,b,color,ls="-"):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=11,color=color,lw=2.5,linestyle=ls,shrinkA=0,shrinkB=0,zorder=5))
def circle_axes(fig,position):
    ax=fig.add_axes(position,facecolor="#F8FAFC");a=np.linspace(0,2*np.pi,500)
    ax.plot(np.cos(a),np.sin(a),color="#94A3B8",lw=1.6)
    ax.grid(color="#CBD5E1",alpha=.7);ax.axhline(0,color="#94A3B8",lw=1);ax.axvline(0,color="#94A3B8",lw=1)
    ax.set(xlim=(-1.3,1.3),ylim=(-1.3,1.3),xlabel="Pair coordinate 1",ylabel="Pair coordinate 2")
    ax.set_aspect("equal");ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);return ax
def main(output):
    if "pair-two-small-angle" in output.name:
        fig=plt.figure(figsize=(520/72,1100/72),facecolor="#F8FAFC")
        for position,point,col,label in [((.20,.58,.70,.29),(0,1),BLUE,"Position 0: (0, 1)"),((.20,.17,.70,.29),(-np.sin(.01),np.cos(.01)),PURPLE,"Position 1: rotation 0.01 rad")]:
            ax=circle_axes(fig,position);arrow(ax,(0,0),point,col)
            fig.text(.077,position[1]+position[3]+.035,label,fontsize=25,color=col)
        fig.text(.077,.965,"Pair 2: a true small rotation",fontsize=29,color="#0F172A")
        fig.text(.077,.075,"After: (−0.0100, 0.99995)",fontsize=27,color=PURPLE)
        fig.text(.077,.028,"Same scale; angle not exaggerated.",fontsize=24,color="#64748B")
    elif "pair-dot-contributions" in output.name:
        fig=plt.figure(figsize=(520/72,740/72),facecolor="#F8FAFC")
        ax=fig.add_axes((.19,.28,.72,.42),facecolor="#F8FAFC")
        a=np.arange(2);ax.bar(a-.18,[1,1],width=.30,color=BLUE,label="Same position")
        ax.bar(a+.18,[np.cos(1),np.cos(.01)],width=.30,color=GREEN,label="Difference = 1",hatch="//")
        ax.set(ylim=(0,1.2),ylabel="Pair dot contribution");ax.set_xticks(a,["Pair 1","Pair 2"]);ax.set_yticks([0,.5,1]);ax.grid(axis="y",color="#CBD5E1",alpha=.7)
        ax.legend(loc="lower left",bbox_to_anchor=(-.18,1.03),fontsize=24,frameon=False)
        fig.text(.077,.95,"Norms agree; dots can differ",fontsize=29,color="#0F172A")
        fig.text(.077,.16,"Same position total: 1 + 1 = 2",fontsize=27,color=BLUE)
        fig.text(.077,.092,"Relative total: 0.5403 + 0.99995",fontsize=25,color=GREEN)
        fig.text(.077,.032,"= 1.5403 (approximately)",fontsize=27,color=GREEN)
    else:
        fig=plt.figure(figsize=(520/72,810/72),facecolor="#F8FAFC")
        ax=circle_axes(fig,(.20,.30,.70,.47))
        arrow(ax,(0,0),(1,0),BLUE);arrow(ax,(0,0),(np.cos(1),np.sin(1)),PURPLE,"--")
        ax.legend(handles=[Line2D([0],[0],color=BLUE,lw=2.5,label="Before / query at p = 0"),Line2D([0],[0],color=PURPLE,lw=2.5,ls="--",label="After / key at p = 1")],loc="lower left",bbox_to_anchor=(-.21,1.02),fontsize=23,frameon=False)
        if "relative-dot-projection" in output.name:
            ax.plot([np.cos(1),np.cos(1)],[0,np.sin(1)],color=ORANGE,lw=2,ls=":")
            ax.scatter([np.cos(1)],[0],color=ORANGE,s=45,zorder=6)
            fig.text(.077,.95,"Dot reads the projected component",fontsize=27,color="#0F172A")
            fig.text(.077,.16,"q · k = cos 1 ≈ 0.5403",fontsize=28,color=ORANGE)
            fig.text(.077,.092,"Both lengths are 1.",fontsize=27,color="#0F172A")
            fig.text(.077,.032,"Content fixed; positions 0 and 1.",fontsize=24,color="#64748B")
        else:
            t=np.linspace(0,1,100);ax.plot(.43*np.cos(t),.43*np.sin(t),color=ORANGE,lw=2)
            ax.text(-1.11,.38,"1 rad",fontsize=27,color=ORANGE,bbox={"facecolor":"#F8FAFC","edgecolor":"none","pad":2})
            fig.text(.077,.95,"Pair 1 rotates by one radian",fontsize=29,color="#0F172A")
            fig.text(.077,.16,"(1, 0) → (0.5403, 0.8415)",fontsize=27,color=PURPLE)
            fig.text(.077,.092,"Both endpoints lie on the unit circle.",fontsize=24,color="#64748B")
            fig.text(.077,.032,"Pair norm stays 1.",fontsize=28,color=GREEN)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
