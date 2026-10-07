"""Reproduce N05-09 representable float32 neighbors around one hundred million."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"n05-09-float","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    center=np.float32(1e8)
    left=np.nextafter(center,np.float32(-np.inf));right=np.nextafter(center,np.float32(np.inf))
    offsets=np.array([float(left)-1e8,0.,float(right)-1e8])
    assert np.array_equal(offsets,[-8,0,8])
    assert np.float32(center+np.float32(1))==center
    fig=plt.figure(figsize=(520/72,620/72),facecolor="#F8FAFC")
    ax=fig.add_axes((.17,.38,.74,.33),facecolor="#F8FAFC");ax.spines["left"].set_visible(False);ax.spines["bottom"].set_position(("data",0));ax.set_yticks([])
    ax.set(xlim=(-9,9),ylim=(-.3,1.6),xlabel="Offset from 10⁸");ax.set_xticks([-8,0,8])
    ax.scatter(offsets,[0,0,0],color="#2563EB",s=70,zorder=5)
    ax.scatter([1],[.9],marker="D",facecolors="none",edgecolors="#D97706",s=80,zorder=5)
    ax.plot([1,1],[0,.9],color="#D97706",ls=":",lw=2)
    ax.add_patch(FancyArrowPatch((1,.65),(0,.65),arrowstyle="-|>",mutation_scale=9,color="#7C3AED",lw=2.2,shrinkA=0,shrinkB=0))
    ax.text(-5,1.25,"Requested +1",color="#D97706",fontsize=28)
    fig.text(.077,.95,"Float32 neighbors near 10⁸",fontsize=29,color="#0F172A")
    fig.text(.077,.22,"Representable offsets: −8, 0, +8",fontsize=25,color="#2563EB")
    fig.text(.077,.14,"10⁸ + 1 rounds back to 10⁸.",fontsize=26,color="#7C3AED")
    fig.text(.077,.065,"This spacing changes with magnitude.",fontsize=24,color="#64748B")
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
