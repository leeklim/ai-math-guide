"""Render I06-03's existing two-vector and norm examples without model execution."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

p = ArgumentParser()
p.add_argument("--output", type=Path, required=True)
out = p.parse_args().output
name = out.stem.removeprefix("I06-03-")
mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 26,
                     "svg.fonttype": "none", "svg.hashsalt": "i06-03-" + name,
                     "axes.labelsize": 24, "xtick.labelsize": 22, "ytick.labelsize": 22})
blue, purple, green, orange = "#2563EB", "#7C3AED", "#059669", "#D97706"
bg = "#F8FAFC"
fig = plt.figure(figsize=(520/72, 800/72), facecolor=bg)
ax = fig.add_axes((.21, .29, .71, .48), facecolor=bg)
ax.grid(color="#CBD5E1", alpha=.6, lw=.9)
ax.set_axisbelow(True)
ax.spines[["top", "right"]].set_visible(False)

if name == "coordinate-mean":
    a = np.array([[1., 0.], [3., 4.]])
    mean = a.mean(axis=0)
    assert np.allclose(mean, [2, 2])
    ax.plot(a[:, 0], a[:, 1], color=purple, ls="--", lw=2)
    ax.scatter(a[:, 0], a[:, 1], color=blue, s=90, zorder=4)
    ax.scatter(*mean, color=green, marker="D", s=90, zorder=5)
    ax.text(.15, 1.60, "a₁=(1,0)", fontsize=24, color=blue)
    ax.text(1.52, 4.35, "a₂=(3,4)", fontsize=24, color=blue)
    ax.text(2.18, 1.75, "Mean", fontsize=24, color=green)
    ax.set(xlim=(0,4), ylim=(-.5,5), xticks=[0,1,2,3,4], yticks=[0,2,4], xlabel="Coordinate 1", ylabel="Coordinate 2")
    title = "Coordinate mean is\nthe midpoint of two samples"
    footer = "Mean = (2,2)\nThe mean need not be a sample."
elif name == "coordinate-variance":
    ax.remove()
    for j, values in enumerate(([1,3], [0,4])):
        panel = fig.add_axes((.21, .56-j*.27, .71, .15), facecolor=bg)
        panel.spines[["top","right","left"]].set_visible(False)
        panel.grid(axis="x", color="#CBD5E1", alpha=.6)
        panel.scatter(values, [0,0], color=blue, s=90, zorder=4)
        panel.scatter([2], [0], color=green, marker="D", s=80, zorder=5)
        panel.set(xlim=(-.5,4.5), ylim=(-.6,.6), xticks=[0,1,2,3,4], yticks=[], xlabel="Coordinate " + str(j+1))
        panel.plot([values[0],2], [.3,.3], color=orange, lw=3)
        panel.plot([2,values[1]], [.3,.3], color=orange, lw=3)
        panel.text(.5*(values[0]+2)-.2, .39, "1" if j==0 else "2", color=orange, fontsize=24)
        panel.text(.5*(values[1]+2)-.2, .39, "1" if j==0 else "2", color=orange, fontsize=24)
    assert np.allclose(np.array([[1,0],[3,4]]).var(axis=0, ddof=1), [2,8])
    fig.text(.077, .79, "Green diamonds: mean 2", color=green, fontsize=26)
    title = "Variance fixes a coordinate\nand varies the input"
    footer = "s₁² = (1²+1²)/(2−1) = 2\ns₂² = (2²+2²)/(2−1) = 8"
elif name == "norm-cancellation":
    ax.set_position((.21,.38,.71,.25))
    for end,col,ls in [((1,0),blue,"-"),((-1,0),purple,"--")]:
        ax.add_patch(FancyArrowPatch((0,0),end,arrowstyle="-|>",mutation_scale=12,color=col,lw=3,linestyle=ls,shrinkA=3,shrinkB=0))
    ax.scatter([0],[0],color=green,s=90,zorder=6)
    ax.text(-1.30,.38,"a₂=(−1,0)",color=purple,fontsize=24)
    ax.text(.30,.38,"a₁=(1,0)",color=blue,fontsize=24)
    ax.set(xlim=(-1.5,1.5),ylim=(-.6,.65),xticks=[-1,0,1],yticks=[0],xlabel="Coordinate 1",ylabel="Coordinate 2")
    title = "Directions cancel;\nindividual norms do not"
    footer = "Mean vector = (0,0): norm 0\nIndividual norms = 1 and 1\nMean of norms = 1"
elif name == "z-score-scale":
    r = np.array([1.,3.,5.])
    z = (r-r.mean())/r.std(ddof=1)
    assert np.allclose(z,[-1,0,1])
    ax.set_position((.21,.40,.71,.20))
    ax.scatter(r,[0,0,0],color=[blue,green,blue],s=100,zorder=4)
    ax.plot([1,3],[.24,.24],color=orange,lw=3)
    ax.plot([3,5],[.24,.24],color=orange,lw=3)
    ax.text(1.15,.35,"s = 2",color=orange,fontsize=24)
    ax.text(3.2,.35,"s = 2",color=orange,fontsize=24)
    ax.set(xlim=(.3,5.7),ylim=(-.3,.55),xticks=[1,3,5],yticks=[],xlabel="Norm r")
    for value,score in zip(r,z):
        ax.text(value,-.17,"z="+str(int(score)),ha="center",fontsize=24,color=purple)
    title = "A z-score measures distance\nin standard-deviation units"
    footer = "Mean norm = 3; sample SD = 2\nz = (r−3)/2\nSD = 0 needs separate handling."
else:
    raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.4)
fig.text(.5,.13,footer,ha="center",fontsize=24,color="#475569",linespacing=1.65)
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"})
plt.close(fig)
