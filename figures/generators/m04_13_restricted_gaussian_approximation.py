#!/usr/bin/env python3
"""Forward exact optimum and reverse finite-grid Gaussian approximation to a mixture."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def density(x,mean,sd):return np.exp(-.5*((x-mean)/sd)**2)/(np.sqrt(2*np.pi)*sd)
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":17,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-13-modes"})
    x=np.linspace(-14,14,5601);p=.5*density(x,-3,.7)+.5*density(x,3,.7)
    best=(np.inf,None,None)
    for mean in np.linspace(-3,3,121):
        for sd in np.linspace(.5,3.5,61):
            q=density(x,mean,sd);logq=-.5*((x-mean)/sd)**2-np.log(np.sqrt(2*np.pi)*sd);value=np.trapezoid(q*(logq-np.log(p)),x)
            if value<best[0]-1e-10:best=(value,mean,sd)
    fig,axes=plt.subplots(1,2,figsize=(11,7),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    for ax,mean,sd,title in zip(axes,[0,best[1]],[np.sqrt(9+.49),best[2]],["Forward KL: exact Gaussian optimum","Reverse KL: finite-grid candidate"]):
        ax.set_facecolor("#F8FAFC");ax.plot(x,p,color="#2563EB",linewidth=3,label="target: two-mode mixture");ax.plot(x,density(x,mean,sd),color="#7C3AED",linewidth=3,linestyle="--",label=f"Gaussian q: μ={mean:.2f}, σ={sd:.2f}");ax.set(xlim=(-7,7),ylim=(0,.66),xlabel="outcome x",ylabel="density");ax.set_title(title,fontsize=16);ax.grid(color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.16),frameon=False,fontsize=14)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
