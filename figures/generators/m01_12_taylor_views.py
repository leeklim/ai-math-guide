"""Reproduce M01-12 approximation and residual figures."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

p = ArgumentParser(); p.add_argument("--output",type=Path,required=True)
out = p.parse_args().output; name = out.stem.removeprefix("M01-12-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                    "svg.fonttype":"none","svg.hashsalt":"mmi-m01-12-"+name})
blue, green, purple, orange = "#2563EB", "#059669", "#7C3AED", "#D97706"
bg="#F8FAFC"; pair=name == "multivariable-path-residual"
fig,axes=plt.subplots(2 if pair else 1,1,figsize=(8.6,8.8 if pair else 6.8),facecolor=bg)
axs=np.atleast_1d(axes); fig.subplots_adjust(left=.19,right=.94,bottom=.21 if pair else .24,top=.87,hspace=.26)
for ax in axs:
    ax.set_facecolor(bg); ax.grid(color="#CBD5E1",alpha=.7,linewidth=.8)
    ax.set_axisbelow(True); ax.spines[["top","right"]].set_visible(False)
    ax.spines[["left","bottom"]].set_color("#64748B"); ax.tick_params(colors="#334155")
ax=axs[0]
if name == "tangent-and-square":
    h=np.linspace(-.8,.8,300)
    ax.plot(h,(3+h)**2,color=green,lw=3,label="Actual f(3+h) = (3+h)²")
    ax.plot(h,9+6*h,color=purple,ls="--",lw=2,label="First order: 9 + 6h")
    ax.scatter([0],[9],color=orange,zorder=5)
    ax.set(xlabel="Displacement h from a = 3",ylabel="Function value",ylim=(3.4,20))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="A tangent matches value and slope, not the whole curve"
    footer="Actual minus first order = h²; at h = 0.1, the residual is 0.01."
elif name == "residual-rate":
    q=np.linspace(0,1,300)
    ax.plot(q,q*q,color=green,lw=3,label="Quadratic residual magnitude: h²")
    ax.plot(q,q,color=blue,ls="--",lw=2,label="Displacement magnitude: |h|")
    ax.set(xlabel="Displacement magnitude |h|",ylabel="Magnitude",ylim=(0,1.65))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="The residual shrinks faster than the displacement"
    footer="For f(x) = x²: |r(h)| / |h| = |h| tends to 0."
elif name == "exponential-orders":
    h=np.linspace(-1.15,1.15,300)
    ax.plot(h,np.exp(h),color=green,lw=3,label="Actual exp(h)")
    ax.plot(h,1+h,color=blue,ls="--",lw=2,label="First order: 1 + h")
    ax.plot(h,1+h+.5*h*h,color=purple,ls=":",lw=3,label="Second order: 1 + h + h²/2")
    ax.scatter([0],[1],color=orange,zorder=5)
    ax.set(xlabel="Displacement h from a = 0",ylabel="Exponential value",ylim=(-.3,5.8))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="A quadratic term models the local change in slope"
    footer="At 0: value 1, slope 1, second derivative 1."
elif name == "log-domain":
    h=np.linspace(-.97,1.5,400)
    ax.plot(h,np.log1p(h),color=green,lw=3,label="Actual log(1+h)")
    ax.plot(h,h,color=purple,ls="--",lw=2,label="First order: h")
    ax.axvline(-1,color=orange,ls=":",lw=2,label="Boundary h = −1: undefined")
    ax.scatter([0],[0],color=orange,zorder=5)
    ax.set(xlabel="Displacement h from a = 1",ylabel="Logarithmic value",xlim=(-1.1,1.6),ylim=(-3.8,4.4))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="A logarithm approximation still has a domain boundary"
    footer="log(1+h) is defined only for h > −1; the tangent is accurate near h = 0."
elif name == "multivariable-path-residual":
    t=np.linspace(0,3,300)
    ax.plot(t,3+.2*t-.01*t*t,color=green,lw=3,label="Actual f(1+0.1t, 2−0.2t)")
    ax.plot(t,3+.2*t,color=purple,ls="--",lw=2,label="Linear prediction: 3 + 0.2t")
    ax.scatter([1],[3.19],color=orange,zorder=5)
    ax.set(ylabel="Function value",ylim=(2.98,4.25),xticks=[0,1,2,3])
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    bottom=axs[1]; bottom.plot(t,-.01*t*t,color=blue,lw=3)
    bottom.scatter([1],[-.01],color=orange,zorder=5)
    bottom.axhline(0,color="#64748B",lw=1)
    bottom.set(xlabel="Multiplier t of displacement (0.1,−0.2)",ylabel="Actual minus predicted",ylim=(-.1,.01),xticks=[0,1,2,3])
    title="A linear prediction leaves an interaction residual"
    footer="Example 3: f = x² + xy; at t = 1, actual 3.19 vs predicted 3.20."
elif name == "relu-boundary":
    x=np.linspace(-.8,1.2,300)
    ax.plot(x,np.maximum(0,x),color=green,lw=3,label="Actual ReLU(x)")
    ax.plot(x,x,color=purple,ls="--",lw=2,label="Linearization at x = 0.5")
    ax.scatter([.5,-.5,-.5],[.5,0,-.5],color=[orange,green,purple],zorder=5)
    ax.plot([-.5,-.5],[-.5,0],color=blue,lw=2)
    ax.set(xlabel="Input x",ylabel="Output",ylim=(-.9,2.25))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="A finite move can cross a different linear region"
    footer="Crossing 0: the linearization predicts −0.5; ReLU gives 0."
else:
    raise ValueError(name)
fig.suptitle(title,fontsize=20,y=.95)
fig.text(.5,.075 if pair else .09,footer,ha="center",fontsize=16,color="#475569")
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"mmi"}); plt.close(fig)
