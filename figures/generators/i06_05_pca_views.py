"""Render existing prerequisite vectors and I06-05's squared singular-value formulas."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt

p=ArgumentParser();p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix("I06-05-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,
                    "xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none",
                    "svg.hashsalt":"i06-05-"+name})
blue,purple,green,orange,bg="#2563EB","#7C3AED","#059669","#D97706","#F8FAFC"
if name=="centering-two-vectors":
    fig,axs=plt.subplots(1,2,figsize=(1040/72,680/72),facecolor=bg)
    fig.subplots_adjust(left=.105,right=.96,bottom=.30,top=.76,wspace=.35)
    a=np.array([[1.,0.],[3.,4.]])
    for ax,values,label in zip(axs,[a,a-a.mean(axis=0)],["Original vectors","Centered vectors"]):
        ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True)
        ax.spines[["top","right"]].set_visible(False)
        ax.scatter(values[:,0],values[:,1],color=blue,s=100,zorder=4)
        ax.scatter(*values.mean(axis=0),color=orange,marker="D",s=100,zorder=5)
        ax.set_title(label,color=blue,fontsize=27,pad=22)
        ax.set(xlabel="Coordinate 1",ylabel="Coordinate 2")
    axs[0].set(xlim=(0,4),ylim=(-1,5),xticks=[0,2,4],yticks=[0,2,4])
    axs[1].set(xlim=(-2,2),ylim=(-3,3),xticks=[-2,0,2],yticks=[-2,0,2])
    fig.suptitle("Subtract the same mean from every input",fontsize=30,y=.96)
    fig.text(.5,.16,"(1,0),(3,4) → (−1,−2),(1,2)",ha="center",fontsize=28,color=green)
    fig.text(.5,.08,"Orange diamond: mean (2,2) → (0,0)",ha="center",fontsize=26,color=orange)
else:
    fig,ax=plt.subplots(figsize=(520/72,800/72),facecolor=bg)
    fig.subplots_adjust(left=.23,right=.94,bottom=.29,top=.75)
    ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.55);ax.set_axisbelow(True)
    ax.spines[["top","right"]].set_visible(False)
    if name=="squared-singular-energy":
        s=np.array([3.,2.,1.]);energy=s*s
        ax.bar([1,2,3],energy,color=[green,purple,purple],hatch=["","//","//"])
        ax.set(xlabel="Singular component",ylabel="Squared variation σ²",xticks=[1,2,3],yticks=[0,1,4,9],ylim=(0,11))
        for k,value in enumerate(energy,1):ax.text(k,value+.35,str(int(value)),ha="center",fontsize=25)
        title="Variance uses the square\nof each singular value"
        footer="σ = (3,2,1): total 9+4+1 = 14\nFirst share = 9/14"
    elif name=="retained-variation-error":
        r=np.linspace(0,1,401);error=np.sqrt(1-r)
        ax.plot(r,error,color=purple,lw=3)
        ax.scatter([.8],[np.sqrt(.2)],color=orange,s=100,zorder=4)
        ax.plot([.8,.8],[0,np.sqrt(.2)],color=orange,ls="--",lw=2)
        ax.plot([0,.8],[np.sqrt(.2),np.sqrt(.2)],color=orange,ls="--",lw=2)
        ax.set(xlabel="Retained squared fraction",ylabel="Relative norm error",xlim=(0,1),ylim=(0,1),xticks=[0,.5,.8,1],yticks=[0,.5,1])
        title="Squared variation retained\nis not the norm error"
        footer="80% retained → error √0.2 ≈ 0.447\nRequires a nonzero centered matrix."
    else:raise ValueError(name)
    fig.suptitle(title,fontsize=28,y=.94,linespacing=1.4)
    fig.text(.5,.13,footer,ha="center",fontsize=24,color="#475569",linespacing=1.65)
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
