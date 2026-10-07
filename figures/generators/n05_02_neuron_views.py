"""Reproduce N05-02 affine and ReLU numerical figures."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

BLUE, PURPLE, GREEN, ORANGE = "#2563EB", "#7C3AED", "#059669", "#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"n05-02-neuron","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    fig=plt.figure(figsize=(520/72,660/72),facecolor="#F8FAFC")
    ax=fig.add_axes((.19,.27,.72,.51),facecolor="#F8FAFC")
    ax.grid(color="#CBD5E1",alpha=.75)
    if "affine" in output.name:
        s=np.linspace(-.5,1.4,300)
        ax.plot(s,2.5*s,color=BLUE,lw=2.5,label="Linear")
        ax.plot(s,2.5*s-.5,color=PURPLE,lw=2.5,ls="--",label="Affine")
        ax.scatter([0,1],[-.5,2],color=PURPLE,s=42,zorder=5)
        ax.annotate("b = −0.5",(0,-.5),xytext=(.20,-1.40),color=PURPLE,fontsize=26,arrowprops={"arrowstyle":"-","color":PURPLE})
        ax.annotate("z = 2",(1,2),xytext=(.45,3.25),color=PURPLE,fontsize=26,arrowprops={"arrowstyle":"-","color":PURPLE})
        ax.set(xlim=(-.5,1.4),ylim=(-2,4),xlabel="Input scale s",ylabel="z")
        ax.set_xticks([0,.5,1]);ax.set_yticks([-2,0,2,4])
        ax.legend(loc="lower left",bbox_to_anchor=(-.16,1.01),frameon=False,ncol=2,fontsize=24)
        fig.text(.077,.94,"Linear and affine",fontsize=30,color="#0F172A")
        fig.text(.077,.13,"x(s) = s(2, −1)",fontsize=28,color="#0F172A")
        fig.text(.077,.07,"z(s) = 2.5s − 0.5",fontsize=28,color=PURPLE)
    else:
        z=np.linspace(-2.2,3,300)
        ax.plot(z,np.maximum(0,z),color=PURPLE,lw=3)
        ax.scatter([-.5,2],[0,2],color=[BLUE,GREEN],s=70,zorder=5)
        ax.plot([-.5,-.5],[-.5,0],ls=":",color=BLUE,lw=2)
        ax.plot([2,2],[0,2],ls=":",color=GREEN,lw=2)
        ax.annotate("(−0.5, 0)",(-.5,0),xytext=(-1.95,.65),color=BLUE,fontsize=26,arrowprops={"arrowstyle":"-","color":BLUE})
        ax.annotate("(2, 2)",(2,2),xytext=(.45,2.7),color=GREEN,fontsize=26,arrowprops={"arrowstyle":"-","color":GREEN})
        ax.set(xlim=(-2.2,3),ylim=(-.7,3.2),xlabel="Pre-activation z",ylabel="Post-activation a")
        ax.set_xticks([-2,0,2]);ax.set_yticks([0,1,2,3])
        fig.text(.077,.94,"ReLU before and after",fontsize=30,color="#0F172A")
        fig.text(.077,.13,"Negative z values share a = 0.",fontsize=26,color=BLUE)
        fig.text(.077,.07,"Positive z keeps a = z.",fontsize=26,color=GREEN)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"})
    plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True)
    main(p.parse_args().output)
