"""Reproduce M01-13 finite differences and float64 errors."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

p=ArgumentParser(); p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output; name=out.stem.removeprefix("M01-13-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                    "svg.fonttype":"none","svg.hashsalt":"mmi-m01-13-"+name})
blue,green,purple,orange="#2563EB","#059669","#7C3AED","#D97706"
bg="#F8FAFC"; pair=name=="coordinate-samples"
fig,axes=plt.subplots(2 if pair else 1,1,figsize=(8.6,8.8 if pair else 6.8),facecolor=bg)
axs=np.atleast_1d(axes); fig.subplots_adjust(left=.19,right=.94,bottom=.21 if pair else .24,top=.87,hspace=.26)
for ax in axs:
    ax.set_facecolor(bg); ax.grid(color="#CBD5E1",alpha=.7,linewidth=.8)
    ax.set_axisbelow(True); ax.spines[["top","right"]].set_visible(False)
    ax.spines[["left","bottom"]].set_color("#64748B"); ax.tick_params(colors="#334155")
ax=axs[0]
if name in {"forward-points","backward-points","central-points"}:
    a,b={"forward-points":(2,2.1),"backward-points":(1.9,2),"central-points":(1.9,2.1)}[name]
    x=np.linspace(1.75,2.25,300)
    ax.plot(x,x*x,color=green,lw=3,label="Function f(x) = x²")
    ax.plot([a,b],[a*a,b*b],color=blue,lw=2,label=f"Selected interval: {a:g} to {b:g}")
    ax.plot([a,b,b],[a*a,a*a,b*b],color=purple,ls="--",lw=2,label="Width and output difference")
    ax.scatter([a,b],[a*a,b*b],color=orange,zorder=5)
    ax.set(xlabel="Function input",ylabel="Function value",xlim=(1.75,2.25),ylim=(2.6,8.3),xticks=[1.8,1.9,2,2.1,2.2])
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    label=name.split("-")[0].capitalize()
    title=f"{label} difference selects two evaluation points"
    footer={"forward-points":"Width h = 0.1; output difference 0.41; quotient 4.1.",
            "backward-points":"Width h = 0.1; output difference 0.39; quotient 3.9.",
            "central-points":"Width 2h = 0.2; output difference 0.80; quotient 4."}[name]
elif name == "truncation-orders":
    h=np.logspace(-4,-.3,250)
    forward=np.expm1(h)/h-1; central=np.sinh(h)/h-1
    ax.loglog(h,forward,color=blue,lw=3,label="Forward truncation error")
    ax.loglog(h,central,color=green,lw=3,ls="--",label="Central truncation error")
    ax.set(xlabel="Interval h (log scale)",ylabel="Absolute truncation error (log scale)",ylim=(1e-10,3))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="Symmetry removes the leading one-sided error"
    footer="For exp(x) at x = 0: the errors shrink like h and h² near zero."
elif name == "float64-error":
    h=np.logspace(-16,-1,230,dtype=np.float64); value=np.exp(np.float64(1))
    forward=(np.exp(1+h)-value)/h; central=(np.exp(1+h)-np.exp(1-h))/(2*h)
    for values,col,sty,label in [(forward,blue,"-","Forward difference"),(central,green,"--","Central difference")]:
        error=np.abs(values-value); mask=error>0
        ax.loglog(h[mask],error[mask],color=col,ls=sty,lw=2,label=label)
    ax.set(xlabel="Interval h (log scale)",ylabel="Absolute derivative error (log scale)",ylim=(1e-16,10))
    ax.legend(loc="upper right",frameon=False,fontsize=16)
    title="Float64 subtraction has a useful interval range"
    footer="NumPy float64, exp(x) at x = 1; zero-error samples are omitted."
elif name == "coordinate-samples":
    x=np.linspace(.8,1.2,300)
    ax.plot(x,x*x+6*x,color=blue,lw=3,label="Fix y = 2; vary x")
    ax.plot([.9,1.1],[6.21,7.81],color=purple,lw=2,ls="--",label="Samples 6.21 and 7.81: slope 8")
    ax.scatter([.9,1.1],[6.21,7.81],color=orange,zorder=5)
    ax.set(ylabel="Output f(x,2)",ylim=(5,12),xticks=[.9,1,1.1],xlabel="Input x (y stays 2)")
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    bottom=axs[1]; y=np.linspace(1.8,2.2,300)
    bottom.plot(y,1+3*y,color=green,lw=4,label="Fix x = 1; vary y")
    bottom.plot([1.9,2.1],[6.7,7.3],color=purple,lw=2,ls="--",label="Samples 6.7 and 7.3: slope 3")
    bottom.scatter([1.9,2.1],[6.7,7.3],color=orange,zorder=5)
    bottom.set(xlabel="Input y (x stays 1)",ylabel="Output f(1,y)",ylim=(6,9.3),xticks=[1.9,2,2.1])
    bottom.legend(loc="upper left",frameon=False,fontsize=16)
    title="Separate coordinate samples around one input point"
    footer="Example 2: f(x,y) = x² + 3xy, point (1,2), h = 0.1; gradient (8,3)."
elif name == "relu-three-rates":
    x=np.linspace(-.8,.8,300)
    ax.plot(x,np.maximum(0,x),color="#94A3B8",lw=5)
    ax.plot([0,.5],[0,.5],color=blue,lw=3,label="Forward rate: 1")
    ax.plot([-.5,0],[0,0],color=green,lw=3,label="Backward rate: 0")
    ax.plot([-.5,.5],[0,.5],color=purple,ls="--",lw=2,label="Central rate: 0.5")
    ax.scatter([-.5,0,.5],[0,0,.5],color=orange,zorder=5)
    ax.set(xlabel="Input x",ylabel="ReLU output",ylim=(-.2,1.5))
    ax.legend(loc="upper left",frameon=False,fontsize=16)
    title="A central quotient does not establish differentiability"
    footer="At the corner x = 0: one-sided rates differ for every h > 0."
elif name == "error-amplification":
    h=np.logspace(-12,-4,250); error=1e-12/h
    ax.loglog(h,error,color=purple,lw=3)
    ax.scatter([1e-8],[1e-4],color=orange,zorder=5)
    ax.set(xlabel="Divisor h (log scale)",ylabel="Amplified error magnitude (log scale)")
    ax.text(2e-8,.02,"h = 1e−8: error = 1e−4",fontsize=17,color=purple)
    title="Division by a small interval amplifies difference errors"
    footer="Fixed difference error 1e−12: quotient error = 1e−12 / h."
else:
    raise ValueError(name)
fig.suptitle(title,fontsize=20,y=.95)
fig.text(.5,.075 if pair else .09,footer,ha="center",fontsize=16,color="#475569")
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"mmi"}); plt.close(fig)
