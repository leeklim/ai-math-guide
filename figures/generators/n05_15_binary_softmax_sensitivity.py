#!/usr/bin/env python3
"""The two-key softmax derivative shrinks at extreme probabilities."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--output",required=True,type=Path); args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"svg.fonttype":"none","svg.hashsalt":"mmi-n05-15-softmax-sensitivity"})
    p=np.linspace(0,1,401); fig,ax=plt.subplots(figsize=(7.2,9),constrained_layout=True); fig.patch.set_facecolor("#F8FAFC"); ax.set_facecolor("#F8FAFC"); ax.plot(p,p*(1-p),color="#7C3AED",linewidth=3)
    ax.scatter([.01,.5,.99],[.0099,.25,.0099],color="#059669",s=100,zorder=4)
    ax.set(xlim=(-.04,1.04),ylim=(-.015,.31),xlabel="weight p",ylabel="local derivative p(1 − p)"); ax.set_xticks([0,.5,1]); ax.set_yticks([0,.1,.2,.25]); ax.grid(color="#CBD5E1",linewidth=.7); ax.spines[["top","right"]].set_visible(False)
    ax.set_title("Two-key softmax\nSensitivity to score gap",fontsize=26,fontweight="bold"); ax.text(.5,.276,"maximum 0.25",ha="center",color="#5B21B6",fontsize=24)
    args.output.parent.mkdir(parents=True,exist_ok=True); fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"}); plt.close(fig)

if __name__ == "__main__": main()
