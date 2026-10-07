"""Reproduce M01-11 geometry and numeric curves."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

p = ArgumentParser(); p.add_argument("--output", type=Path, required=True)
out = p.parse_args().output; name = out.stem.removeprefix("M01-11-")
mpl.rcParams.update({"font.family":"DejaVu Sans", "font.size":16,
                    "svg.fonttype":"none", "svg.hashsalt":"mmi-m01-11-"+name})
blue, green, purple, orange = "#2563EB", "#059669", "#7C3AED", "#D97706"
bg = "#F8FAFC"; pair = name == "input-path-and-rate"
fig, axes = plt.subplots(2 if pair else 1, 1, figsize=(8.6, 8.8 if pair else 6.8), facecolor=bg)
axs = np.atleast_1d(axes)
fig.subplots_adjust(left=.19, right=.94, bottom=.21 if pair else .24, top=.87, hspace=.26)
for ax in axs:
    ax.set_facecolor(bg); ax.grid(color="#CBD5E1", alpha=.7, linewidth=.8)
    ax.set_axisbelow(True); ax.spines[["top","right"]].set_visible(False)
    ax.spines[["left","bottom"]].set_color("#64748B"); ax.tick_params(colors="#334155")
ax = axs[0]
def arrow(a, start, end, color):
    a.annotate("", xy=end, xytext=start,
               arrowprops={"arrowstyle":"-|>","mutation_scale":14,"lw":2.5,"color":color,"shrinkA":0,"shrinkB":0})

if name == "unit-and-speed":
    theta = np.linspace(0, 2*np.pi, 360)
    ax.plot(np.cos(theta), np.sin(theta), color="#94A3B8", ls="--", label="Unit circle")
    arrow(ax, (0,0), (1.2,1.6), blue); arrow(ax, (0,0), (.6,.8), green)
    ax.scatter([0], [0], color=orange, zorder=5)
    ax.text(1.4, .2, "v = (0.6,0.8)", fontsize=17, color=green)
    ax.text(.7, 1.78, "2v = (1.2,1.6)", fontsize=17, color=blue)
    ax.set(xlabel="First input displacement", ylabel="Second input displacement", xlim=(-1.4,2.8), ylim=(-1.3,2.5))
    ax.set_aspect("equal"); ax.legend(loc="upper left", frameon=False, fontsize=16)
    title = "One direction, different distances per unit of t"
    footer = "The two lengths are 1 and 2; t v and t(2v) move at different speeds."
elif name == "input-path-and-rate":
    t = np.linspace(-.8,.8,300)
    ax.plot(1+.6*t, -1+.8*t, color=blue, lw=3)
    arrow(ax, (1,-1), (1.3,-.6), blue)
    ax.scatter([1], [-1], color=orange, zorder=5)
    ax.text(.53, -.3, "x(t) = 1 + 0.6t", fontsize=17, color=blue)
    ax.text(.53, -.52, "y(t) = −1 + 0.8t", fontsize=17, color=blue)
    ax.set(xlabel="First input x", ylabel="Second input y", xlim=(.45,1.6), ylim=(-1.8,-.05))
    bottom = axs[1]
    bottom.plot(t, 4-3.6*t+2.28*t*t, color=green, lw=3, label="g(t) = f(x(t),y(t))")
    bottom.plot(t,4-3.6*t,color=purple,ls="--",lw=2,label="Tangent at t = 0: slope −3.6")
    bottom.scatter([0],[4],color=orange,zorder=5)
    bottom.set(xlabel="Path parameter t",ylabel="Output along the path",ylim=(.8,12.4))
    bottom.legend(loc="upper right",frameon=False,fontsize=16)
    title = "A path in two inputs produces one scalar-input curve"
    footer = "Example 1: f(x,y) = x² + 3y², start (1,−1), v = (3/5,4/5)."
elif name == "gradient-components":
    arrow(ax,(0,0),(3,4),purple)
    ax.plot([0,3,3],[0,0,4],color="#64748B",ls="--",lw=1.5)
    ax.text(1.3,-.48,"First partial = 3",fontsize=17,color=blue)
    ax.text(3.3,1.55,"Second\npartial = 4",fontsize=17,color=green)
    ax.text(.08,4.9,"Gradient = (3,4); length = 5",fontsize=17,color=purple)
    ax.set(xlabel="First vector component",ylabel="Second vector component",xlim=(-.6,5.8),ylim=(-.7,5.7))
    ax.set_aspect("equal")
    title = "Coordinate partials form one gradient vector"
    footer = "A gradient is a vector; its inner product with a direction is a scalar."
elif name == "direction-angle":
    degrees = np.linspace(0,360,600); angle = np.deg2rad(degrees)
    ax.plot(degrees,3*np.cos(angle)+4*np.sin(angle),color=green,lw=3)
    a = np.rad2deg(np.arctan2(4,3))
    ax.scatter([a,a+90,a+180],[5,0,-5],color=orange,zorder=5)
    ax.axhline(0,color="#64748B",lw=1)
    ax.text(a+14,5.4,"Aligned: +5",fontsize=17,color=green)
    ax.text(a+104,-5.6,"Opposite: −5",fontsize=17,color=purple)
    ax.set(xlabel="Angle of unit direction v (degrees)",ylabel="Directional derivative",xticks=[0,90,180,270,360],ylim=(-7,7))
    title = "Direction changes the rate, with vector length fixed at one"
    footer = "Gradient (3,4), norm 5; compare unit directions through a full turn."
elif name == "step-size-risk":
    x = np.linspace(-1.7,1.7,300)
    ax.plot(x,x*x,color=green,lw=3,label="Illustrative loss L(theta) = theta²")
    ax.scatter([1,.6,-1.4],[1,.36,1.96],color=[orange,blue,purple],zorder=5)
    ax.text(.95,1.34,"Start",fontsize=17,color=orange)
    ax.annotate("Small step",xy=(.6,.36),xytext=(-.2,.9),fontsize=17,color=blue,arrowprops={"arrowstyle":"-","color":"#94A3B8"})
    ax.annotate("Large step",xy=(-1.4,1.96),xytext=(-1.65,.2),fontsize=17,color=purple,arrowprops={"arrowstyle":"-","color":"#94A3B8"})
    ax.set(xlabel="Single parameter theta",ylabel="Loss",ylim=(-.3,4.2))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title = "The local descent direction does not choose a safe step size"
    footer = "At theta = 1, gradient 2: eta 0.2 gives 0.6; eta 1.2 gives −1.4."
elif name == "saddle-slices":
    t = np.linspace(-1.5,1.5,300)
    ax.plot(t,t*t,color=blue,lw=3,label="Along x axis: f(t,0) = t²")
    ax.plot(t,-t*t,color=green,lw=3,ls="--",label="Along y axis: f(0,t) = −t²")
    ax.axhline(0,color=purple,ls=":",lw=2,label="Both tangent slopes are 0")
    ax.scatter([0],[0],color=orange,zorder=5)
    ax.set(xlabel="Signed displacement along the selected axis",ylabel="Output f(x,y) = x² − y²",ylim=(-2.6,4.7))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title = "Zero gradient, but nearby values are higher and lower"
    footer = "At the origin: increasing along one axis, decreasing along the other."
elif name == "parameter-update":
    arrow(ax,(1,-2),(.6,-1.9),blue)
    ax.scatter([1,.6],[-2,-1.9],color=[orange,blue],zorder=5)
    ax.plot([1,.6,.6],[-2,-2,-1.9],ls="--",color="#94A3B8",lw=1.5)
    ax.text(.72,-2.07,"delta theta1 = −0.4",fontsize=17,color=blue)
    ax.text(.33,-1.82,"New: (0.6,−1.9)",fontsize=17,color=blue)
    ax.text(.82,-2.17,"Start: (1,−2)",fontsize=17,color=orange)
    ax.set(xlabel="First parameter theta1",ylabel="Second parameter theta2",xlim=(.25,1.4),ylim=(-2.25,-1.65),xticks=[.4,.6,.8,1,1.2],yticks=[-2.2,-2,-1.8])
    title = "Both coordinates update from the same current gradient"
    footer = "eta = 0.1; gradient (4,−1); displacement (−0.4,+0.1)."
else:
    raise ValueError(name)
fig.suptitle(title,fontsize=20,y=.95)
fig.text(.5,.075 if pair else .09,footer,ha="center",fontsize=16,color="#475569")
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"mmi"}); plt.close(fig)
