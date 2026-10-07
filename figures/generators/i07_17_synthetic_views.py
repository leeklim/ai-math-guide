"""Draw the known synthetic circuit and same-input summaries of I07-17."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-17-circuit","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    key=output.stem.removeprefix("I07-17-");h=1350 if key=="signed-and-absolute-means" else 1050;fig=plt.figure(figsize=(520/72,h/72),facecolor="#F8FAFC")
    if key=="cancelling-path-removals":
        ax=fig.add_axes((.21,.33,.70,.46),facecolor="#F8FAFC");ys=[0,-1,1,0];cols=["#059669","#DC2626","#DC2626","#64748B"];ax.bar(range(4),ys,color=cols,width=.55);ax.scatter([0,3],[0,0],s=100,facecolors="white",edgecolors=["#059669","#64748B"],lw=2,zorder=5)
        ax.set(xlim=(-.65,3.6),ylim=(-1.5,1.6),ylabel="Synthetic score m");ax.set_xticks(range(4),["Intact","No\ncopy","No\ngate","Neither"]);ax.set_yticks([-1,0,1]);ax.axhline(0,color="#64748B",lw=1);ax.grid(axis="y",color="#CBD5E1",alpha=.7)
        for i,y in enumerate(ys):ax.text(i,y+(.12 if y>=0 else -.29),str(y),ha="center",fontsize=28,color=cols[i])
        fig.text(.077,.95,"Two nonzero paths can cancel",fontsize=27);fig.text(.077,.90,"Same input x = (1, −1)",fontsize=28,color="#64748B");fig.text(.077,.22,"Copy effect size 1; gate size 1",fontsize=27,color="#DC2626");fig.text(.077,.145,"Joint effect size 0, not 1 + 1",fontsize=27,color="#64748B");fig.text(.077,.07,"Size means absolute output change.",fontsize=25,color="#64748B")
    elif key=="signed-and-absolute-means":
        rng=np.random.default_rng(20261001);x=rng.choice(np.array([-1.,1.]),size=(64,2));delta=np.stack([x[:,0],x[:,0]*x[:,1],x[:,0]+x[:,0]*x[:,1]],axis=1);signed=delta.mean(0);absolute=np.abs(delta).mean(0)
        for y,vals,label in [(.56,signed,"Mean signed change"),(.19,absolute,"Mean absolute change")]:
            ax=fig.add_axes((.21,y,.70,.24),facecolor="#F8FAFC");ax.bar(range(3),vals,color=["#2563EB","#7C3AED","#059669"],width=.52);ax.set(xlim=(-.6,2.6),ylim=(-.6,1.5),ylabel="Effect metric");ax.set_xticks(range(3),["Copy","Gate","Joint"]);ax.set_yticks([0,1]);ax.axhline(0,color="#64748B",lw=1);ax.grid(axis="y",color="#CBD5E1",alpha=.7)
            for i,v in enumerate(vals):ax.text(i,v+(.08 if v>=0 else -.22),f"{v:.3f}",ha="center",fontsize=26,color=["#2563EB","#7C3AED","#059669"][i])
            fig.text(.077,y+.24+.025,label,fontsize=27,color="#64748B")
        fig.text(.077,.95,"Same 64 fixed synthetic inputs",fontsize=28);fig.text(.077,.90,"Δ = intact score − ablated score",fontsize=26,color="#64748B");fig.text(.077,.065,"Mean(|Δ|) ≠ |mean(Δ)|",fontsize=28,color="#D97706")
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
