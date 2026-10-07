"""Reproduce N05-07 exact sample gradients, loss surface and one-step predictions."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch
BLUE,PURPLE,GREEN,ORANGE="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"n05-07-gd","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def arrow(ax,start,end,col,ls="-",zorder=3):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=12,color=col,lw=2.5,linestyle=ls,shrinkA=4,shrinkB=0,zorder=zorder))
def main(output):
    fig=plt.figure(figsize=(520/72,800/72),facecolor="#F8FAFC")
    ax=fig.add_axes((.20,.26,.71,.42),facecolor="#F8FAFC");ax.grid(color="#CBD5E1",alpha=.75)
    if "sample-gradients" in output.name:
        pairs=[((-6,-6),BLUE,"-","Sample 1: (−6, −6)"),((-20,-10),PURPLE,"--","Sample 2: (−20, −10)"),((-13,-8),GREEN,"-.","Mean: (−13, −8)")]
        for point,col,ls,label in pairs:arrow(ax,(0,0),point,col,ls)
        ax.scatter([0],[0],color="#64748B",s=40,zorder=6)
        ax.set(xlim=(-22,2),ylim=(-12,2),xlabel="dL / dw",ylabel="dL / db")
        ax.set_xticks([-20,-10,0]);ax.set_yticks([-10,-5,0])
        ax.legend(handles=[Line2D([0],[0],color=col,lw=2.5,ls=ls,label=label) for _,col,ls,label in pairs],loc="lower left",bbox_to_anchor=(-.20,1.02),frameon=False,fontsize=23)
        fig.text(.077,.95,"Gradients at the same θ",fontsize=29,color="#0F172A")
        fig.text(.077,.13,"All evaluated at (w, b) = (0, 0).",fontsize=26,color="#0F172A")
        fig.text(.077,.075,"Mean = (gradient 1 + gradient 2)/2",fontsize=24,color=GREEN)
    elif "loss-step" in output.name:
        ax.set_position((.20,.26,.71,.58))
        w,b=np.meshgrid(np.linspace(-.5,3.2,400),np.linspace(-.5,2.2,350));loss=((w+b-3)**2+(2*w+b-5)**2)/2
        cs=ax.contour(w,b,loss,levels=[1,4,9,17],colors="#94A3B8",linewidths=1.2)
        ax.clabel(cs,inline=True,fontsize=22,fmt="%g")
        arrow(ax,(0,0),(1.3,.8),PURPLE)
        ax.scatter([0,1.3,2],[0,.8,1],color=[BLUE,GREEN,ORANGE],s=70,zorder=6)
        ax.text(-.30,-.28,"θ₀",color=BLUE,fontsize=28)
        ax.text(.85,1.11,"θ₁",color=GREEN,fontsize=28,bbox={"facecolor":"#F8FAFC","edgecolor":"none","pad":2})
        ax.text(2.16,1.22,"(2, 1)",color=ORANGE,fontsize=25,bbox={"facecolor":"#F8FAFC","edgecolor":"none","pad":2})
        ax.set(xlim=(-.5,3.2),ylim=(-.5,2.2),xlabel="Weight w",ylabel="Bias b");ax.set_xticks([0,1,2,3]);ax.set_yticks([0,1,2])
        fig.text(.077,.95,"One step on this batch loss",fontsize=29,color="#0F172A")
        fig.text(.077,.13,"θ₁ = θ₀ − 0.1(−13, −8)",fontsize=27,color=PURPLE)
        fig.text(.077,.075,"L: 17 → 1.685",fontsize=28,color=GREEN)
    elif "predictions" in output.name:
        x=np.linspace(0,2.4,300)
        ax.plot(x,0*x,color=BLUE,lw=2.5,ls="--",label="Before: 0")
        ax.plot(x,1.3*x+.8,color=GREEN,lw=2.5,label="After: 1.3x + 0.8")
        ax.scatter([1,2],[3,5],color=ORANGE,s=85,zorder=5,label="Targets")
        for xv,yhat,target in [(1,2.1,3),(2,3.4,5)]:ax.plot([xv,xv],[yhat,target],color=PURPLE,ls=":",lw=2.5)
        ax.set(xlim=(0,2.4),ylim=(-.3,5.6),xlabel="Input x",ylabel="Prediction / target y");ax.set_xticks([0,1,2]);ax.set_yticks([0,2,4])
        ax.legend(loc="lower left",bbox_to_anchor=(-.20,1.01),frameon=False,fontsize=23)
        fig.text(.077,.95,"Prediction changes after update",fontsize=28,color="#0F172A")
        fig.text(.077,.13,"Predictions: (2.1, 3.4)",fontsize=28,color=GREEN)
        fig.text(.077,.075,"Residuals: (−0.9, −1.6)",fontsize=28,color=PURPLE)
    else:
        arrow(ax,(0,0),(2.6,1.6),PURPLE,"--",2)
        arrow(ax,(0,0),(1.3,.8),GREEN,"-",5)
        ax.scatter([0],[0],color="#64748B",s=45,zorder=6)
        ax.scatter([1.3,2.6],[.8,1.6],color=[GREEN,PURPLE],s=45,zorder=4)
        ax.set(xlim=(-.2,3),ylim=(-.2,2),xlabel="Weight w",ylabel="Bias b");ax.set_xticks([0,1,2,3]);ax.set_yticks([0,1,2])
        ax.legend(handles=[Line2D([0],[0],color=GREEN,lw=2.5,label="Mean, η = 0.1"),Line2D([0],[0],color=PURPLE,lw=2.5,ls="--",label="Sum, η = 0.1")],loc="lower left",bbox_to_anchor=(-.20,1.03),frameon=False,fontsize=23)
        fig.text(.077,.95,"Reduction changes step size",fontsize=29,color="#0F172A")
        fig.text(.077,.13,"Mean: (1.3, 0.8)",fontsize=28,color=GREEN)
        fig.text(.077,.075,"Sum: (2.6, 1.6)",fontsize=28,color=PURPLE)
        fig.text(.077,.025,"Sum with η = 0.05 matches mean.",fontsize=25,color="#0F172A")
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
