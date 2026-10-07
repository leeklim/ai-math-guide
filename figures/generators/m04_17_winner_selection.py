#!/usr/bin/env python3
"""One fixed-seed noisy candidate screen and an independent confirmation draw."""
import argparse
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True,type=Path);args=parser.parse_args()
    mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":19,"svg.fonttype":"none","svg.hashsalt":"mmi-m04-17-winner"})
    rng=np.random.default_rng(1708);true=.02;estimates=rng.normal(true,.04,size=(2,24));j=int(estimates[0].argmax());heads=np.arange(1,25)
    fig,axes=plt.subplots(1,2,figsize=(11,7.8),constrained_layout=True);fig.patch.set_facecolor("#F8FAFC")
    axes[0].scatter(heads,estimates[0],color="#2563EB",s=50);axes[0].scatter(j+1,estimates[0,j],facecolors="none",edgecolors="#D97706",linewidths=3,s=200,label=f"selected head {j+1}");axes[0].set(xlim=(0,25),xlabel="candidate head");axes[0].set_xticks([1,6,12,18,24]);axes[0].set_title("Discovery selects the largest\nobserved effect",fontsize=19,fontweight="bold")
    axes[1].plot([0,1],estimates[:,j],color="#CBD5E1",linewidth=2);axes[1].scatter([0,1],estimates[:,j],color=["#D97706","#059669"],s=100);axes[1].set_xticks([0,1],labels=["Discovery","Confirmation"]);axes[1].set(xlim=(-.5,1.5),xlabel=f"same fixed head {j+1}");axes[1].set_title("New data do not preserve\nselected discovery noise",fontsize=19,fontweight="bold")
    for ax in axes:ax.axhline(true,color="#059669",linestyle="--",linewidth=2,label="true effect = .02");ax.set(ylim=(-.075,.135),ylabel="estimated effect");ax.set_facecolor("#F8FAFC");ax.grid(axis="y",color="#CBD5E1",linewidth=.7);ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper center",bbox_to_anchor=(.5,-.16),frameon=False,fontsize=17);ax.tick_params(labelsize=18)
    args.output.parent.mkdir(parents=True,exist_ok=True);fig.savefig(args.output,format="svg",metadata={"Date":None,"Creator":"mmi"});plt.close(fig)

if __name__ == "__main__":main()
