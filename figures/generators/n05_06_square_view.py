"""Reproduce the N05-06 square value and tangent figure."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"n05-06-square","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    fig=plt.figure(figsize=(520/72,710/72),facecolor="#F8FAFC")
    ax=fig.add_axes((.18,.27,.73,.49),facecolor="#F8FAFC")
    z=np.linspace(-2,2,500);ax.plot(z,z*z,color="#7C3AED",lw=2.7)
    for base,col,ls in [(-1,"#2563EB","--"),(1,"#059669","-.")]:
        t=np.linspace(base-.6,base+.6,100);ax.plot(t,1+2*base*(t-base),color=col,lw=2.4,ls=ls)
        ax.scatter([base],[1],color=col,s=65,zorder=5)
    ax.grid(color="#CBD5E1",alpha=.75);ax.set(xlim=(-2,2),ylim=(-.3,4.3),xlabel="Stored input z",ylabel="h = z²")
    ax.set_xticks([-2,-1,0,1,2]);ax.set_yticks([0,1,2,3,4])
    fig.text(.077,.95,"Same h, opposite local slopes",fontsize=28,color="#0F172A")
    fig.text(.077,.14,"z = −1: dh/dz = −2",fontsize=28,color="#2563EB")
    fig.text(.077,.08,"z = +1: dh/dz = +2",fontsize=28,color="#059669")
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
