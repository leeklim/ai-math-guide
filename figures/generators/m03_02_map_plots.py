"""Reproduce M03-02 linearity and differentiation comparisons."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

p=ArgumentParser(); p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output; name=out.stem.removeprefix("M03-02-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                    "svg.fonttype":"none","svg.hashsalt":"mmi-m03-02-"+name})
blue,green,purple,orange="#2563EB","#059669","#7C3AED","#D97706"
bg="#F8FAFC"; fig,ax=plt.subplots(figsize=(8.6,6.8),facecolor=bg)
fig.subplots_adjust(left=.18,right=.93,bottom=.25,top=.87)
ax.set_facecolor(bg); ax.grid(color="#CBD5E1",alpha=.7,linewidth=.8)
ax.set_axisbelow(True); ax.spines[["top","right"]].set_visible(False)
ax.spines[["left","bottom"]].set_color("#64748B"); ax.tick_params(colors="#334155")
if name=="zero-is-not-linearity":
    x=np.linspace(-.25,2.25,300)
    ax.plot(x,x*x,color=purple,lw=3,label="F(x) = x²")
    ax.scatter([0,1,2],[0,1,4],color=green,zorder=5,label="Actual outputs: 0, 1, 4")
    ax.scatter([2],[2],color=orange,marker="s",s=60,zorder=5,label="Scaling would require 2F(1) = 2")
    ax.plot([2,2],[2,4],color=orange,ls=":",lw=2)
    ax.set(xlabel="Input x",ylabel="Output F(x)",ylim=(-.5,7.5))
    title="Preserving zero is not enough for linearity"
    footer="F(2·1) = 4, while 2F(1) = 2."
elif name=="kernel-lost-constants":
    t=np.linspace(-1,1.5,300)
    for c,col,ls in [(0,blue,"-"),(2,purple,"--"),(-2,orange,":")]:
        ax.plot(t,2-3*t+4*t*t+c,color=col,lw=2.8,ls=ls,label="p(t)"+(" + 2" if c==2 else " − 2" if c==-2 else ""))
    ax.set(xlabel="Polynomial input t",ylabel="Input polynomial value",ylim=(-2,16))
    title="Constant shifts give different input functions"
    footer="Here p(t) = 2 − 3t + 4t²; the shifts are in ker D."
elif name=="kernel-shared-output":
    t=np.linspace(-1,1.5,300)
    ax.plot(t,-3+8*t,color=green,lw=3,label="D(p) = D(p+2) = D(p−2)")
    ax.set(xlabel="Polynomial input t",ylabel="Derivative value",ylim=(-13,18))
    title="Differentiation removes the constant shift"
    footer="All three inputs have derivative −3 + 8t."
else:
    raise ValueError(name)
ax.legend(loc="upper left",frameon=False,fontsize=16)
fig.suptitle(title,fontsize=20,y=.95)
fig.text(.5,.09,footer,ha="center",fontsize=16,color="#475569")
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"mmi"}); plt.close(fig)
