"""Reproduce M03-01 function-space and closure figures."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

p=ArgumentParser(); p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output; name=out.stem.removeprefix("M03-01-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                    "svg.fonttype":"none","svg.hashsalt":"mmi-m03-01-"+name})
blue,green,purple,orange="#2563EB","#059669","#7C3AED","#D97706"
bg="#F8FAFC"; fig,ax=plt.subplots(figsize=(8.6,6.8),facecolor=bg)
fig.subplots_adjust(left=.19,right=.94,bottom=.24,top=.87)
ax.set_facecolor(bg); ax.grid(color="#CBD5E1",alpha=.7,linewidth=.8)
ax.set_axisbelow(True); ax.spines[["top","right"]].set_visible(False)
ax.spines[["left","bottom"]].set_color("#64748B"); ax.tick_params(colors="#334155")
if name=="pointwise-addition":
    t=np.linspace(-1,2,300)
    ax.plot(t,1+2*t,color=blue,lw=3,label="p(t) = 1 + 2t")
    ax.plot(t,t-t*t,color=purple,lw=2,ls="--",label="q(t) = t − t²")
    ax.plot(t,1+3*t-t*t,color=green,lw=3,ls=":",label="(p+q)(t) = 1 + 3t − t²")
    ax.scatter([1.5]*3,[4,-.75,3.25],color=[blue,purple,green],zorder=5)
    ax.axvline(1.5,color="#94A3B8",ls="--",lw=1)
    ax.set(xlabel="Common function input t",ylabel="Function value",ylim=(-4,9))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="Function addition uses the same input on both curves"
    footer="At t = 1.5: p = 4, q = −0.75, p+q = 3.25."
elif name=="scalar-multiplication":
    t=np.linspace(-1,1.5,300)
    ax.plot(t,1+2*t,color=blue,lw=3,label="p(t) = 1 + 2t")
    ax.plot(t,3+6*t,color=green,lw=3,ls="--",label="(3p)(t) = 3 + 6t")
    ax.plot([1,1],[3,9],color=purple,ls=":",lw=2)
    ax.scatter([1,1],[3,9],color=orange,zorder=5)
    ax.set(xlabel="Function input t (unchanged)",ylabel="Function value",ylim=(-4,18))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="A scalar multiplies the entire function, not its input"
    footer="At t = 1: p(1) = 3 and (3p)(1) = 9."
elif name=="subspace-closure":
    x=np.linspace(-2.5,2.5,300)
    ax.plot(x,-x,color=purple,lw=2,label="S: x + y = 0")
    for point,marker,col,label in [((1,-1),"o",blue,"u = (1,−1)"),((-.5,.5),"o",blue,"v = (−0.5,0.5)"),((.5,-.5),"s",green,"u+v = (0.5,−0.5)"),((-2,2),"^",green,"−2u = (−2,2)")]:
        ax.scatter(*point,marker=marker,color=col,s=55,zorder=5,label=label)
    ax.scatter([0],[0],color=orange,s=35,zorder=5)
    ax.set(xlabel="First coordinate x",ylabel="Second coordinate y",xlim=(-3,4),ylim=(-3,4))
    ax.set_aspect("equal"); ax.legend(loc="upper right",frameon=False,fontsize=16)
    title="Adding and scaling stay on the line through the origin"
    footer="The illustrated inputs and results all satisfy x + y = 0."
elif name=="affine-not-closed":
    x=np.linspace(-1,2.5,300)
    ax.plot(x,1-x,color=purple,lw=2,label="A: x + y = 1")
    ax.scatter([1,0],[0,1],color=blue,zorder=5,label="u = (1,0), v = (0,1)")
    ax.scatter([1],[1],color=orange,marker="s",s=55,zorder=5,label="u+v = (1,1), outside A")
    ax.scatter([0],[0],color="#475569",marker="x",s=65,zorder=5,label="Zero is also outside A")
    ax.set(xlabel="First coordinate x",ylabel="Second coordinate y",xlim=(-1.4,3),ylim=(-1.4,4.8))
    ax.set_aspect("equal"); ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="A shifted line can exclude zero and fail addition closure"
    footer="For the sum, x+y = 2; for zero, x+y = 0; neither equals 1."
elif name=="zero-value-zero-function":
    t=np.linspace(-2,2,300)
    ax.plot(t,t,color=blue,lw=3,label="f(t) = t")
    ax.axhline(0,color=green,lw=3,ls="--",label="Zero function: value 0 for all t")
    ax.scatter([0],[0],color=orange,s=55,zorder=5)
    ax.set(xlabel="Function input t",ylabel="Function value",ylim=(-2.5,4.5))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="One zero value does not make a zero function"
    footer="f(0) = 0, but f(1) = 1: f is not the zero function."
elif name=="polynomial-basis-curves":
    t=np.linspace(-1.5,1.5,300)
    ax.plot(t,np.ones_like(t),color=blue,lw=3,label="First basis polynomial: 1")
    ax.plot(t,t,color=purple,lw=2,ls="--",label="Second basis polynomial: t")
    ax.plot(t,t*t,color=green,lw=3,ls=":",label="Third basis polynomial: t²")
    ax.set(xlabel="Polynomial input t",ylabel="Basis polynomial value",ylim=(-2,5.7))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="The basis objects can be functions rather than arrows"
    footer="B = (1,t,t²) spans P2; coordinates multiply these three functions."
elif name=="coefficient-reconstruction":
    t=np.linspace(-1,1.5,300)
    ax.plot(t,np.full_like(t,2),color=blue,lw=2,ls=":",label="Coefficient 2 times basis 1")
    ax.plot(t,-t,color=purple,lw=2,ls="--",label="Coefficient −1 times basis t")
    ax.plot(t,3*t*t,color=orange,lw=2,ls="-.",label="Coefficient 3 times basis t²")
    ax.plot(t,2-t+3*t*t,color=green,lw=3,label="Sum p(t) = 2 − t + 3t²")
    ax.scatter([1],[4],color=green,s=45,zorder=5)
    ax.set(xlabel="Function input t",ylabel="Weighted component and sum",ylim=(-2,14))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="Coefficients weight basis functions before addition"
    footer="Coordinates (2,−1,3) are coefficients, not sampled function values."
else:
    raise ValueError(name)
fig.suptitle(title,fontsize=20,y=.95)
fig.text(.5,.09,footer,ha="center",fontsize=16,color="#475569")
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"mmi"}); plt.close(fig)
