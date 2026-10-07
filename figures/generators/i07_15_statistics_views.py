"""Draw prompt-level pairing, exact sign flips, and candidate counts for I07-15."""
import argparse
from pathlib import Path
from itertools import product
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-15-statistics","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    key=output.stem.removeprefix("I07-15-");height=1350 if key=="task-matched-pairs" else (1450 if key=="candidate-family" else 1050);fig=plt.figure(figsize=(520/72,height/72),facecolor="#F8FAFC")
    if key=="prompt-paired-differences":
        ax=fig.add_axes((.22,.31,.65,.51),facecolor="#F8FAFC");base=[1,3,2];patch=[3,4,5]
        for i,(b,p) in enumerate(zip(base,patch)):ax.plot([i,i],[b,p],color="#64748B",lw=2);ax.scatter([i],[b],color="#2563EB",s=75,zorder=4);ax.scatter([i],[p],color="#DC2626",s=75,zorder=4);ax.text(i,p+.22,"d="+str(p-b),ha="center",fontsize=27,color="#DC2626")
        ax.set(xlim=(-.6,2.6),ylim=(0,6.2),xlabel="Prompt unit",ylabel="Metric");ax.set_xticks([0,1,2],["P1","P2","P3"]);ax.set_yticks([0,2,4,6]);ax.grid(color="#CBD5E1",alpha=.7)
        fig.text(.077,.95,"Pair within each prompt first",fontsize=28);fig.text(.077,.89,"Base ●",color="#2563EB",fontsize=26);fig.text(.50,.89,"Patched ●",color="#DC2626",fontsize=26);fig.text(.077,.20,"d = (2, 1, 3); mean = 2",fontsize=28,color="#DC2626");fig.text(.077,.11,"One difference per prompt.",fontsize=26,color="#64748B")
    elif key=="task-matched-pairs":
        task=np.array([.42,.35,.51,.39,.46,.33,.48,.41]);ctrl=np.array([.08,.11,.05,.14,.07,.10,.09,.12]);paired=task-ctrl;x=np.arange(1,9)
        top=fig.add_axes((.22,.56,.65,.28),facecolor="#F8FAFC");top.plot(x,task,"o-",color="#DC2626",lw=2);top.plot(x,ctrl,"s--",color="#D97706",lw=2);top.set(ylim=(0,.65),ylabel="Base-relative effect",xlim=(.5,8.5));top.set_xticks([1,4,8]);top.set_yticks([0,.3,.6]);top.grid(color="#CBD5E1",alpha=.7)
        bot=fig.add_axes((.22,.17,.65,.25),facecolor="#F8FAFC");bot.bar(x,paired,color="#7C3AED",width=.6);bot.set(ylim=(0,.6),xlabel="Prompt unit",ylabel="Task − control",xlim=(.5,8.5));bot.set_xticks([1,4,8]);bot.set_yticks([0,.3,.6]);bot.grid(axis="y",color="#CBD5E1",alpha=.7)
        fig.text(.077,.95,"CPU: task and matched control",fontsize=27);fig.text(.077,.90,"Task ●",color="#DC2626",fontsize=26);fig.text(.48,.90,"Control ■",color="#D97706",fontsize=26);fig.text(.077,.47,"Subtract effects for the same unit.",fontsize=26,color="#64748B");fig.text(.077,.075,"n = 8; paired mean = 0.32375",fontsize=27,color="#7C3AED")
    elif key=="exact-sign-flip":
        d=np.array([2,1,3]);means=np.array([np.mean(d*np.array(s)) for s in product([-1,1],repeat=3)]);vals,counts=np.unique(means,return_counts=True);extreme=np.isclose(np.abs(vals),2)
        ax=fig.add_axes((.23,.32,.64,.49),facecolor="#F8FAFC");ax.bar(vals,counts,width=.35,color=["#DC2626" if b else "#7C3AED" for b in extreme]);ax.set(xlim=(-2.5,2.5),ylim=(0,2.7),xlabel="Null mean",ylabel="Sign patterns");ax.set_xticks([-2,0,2]);ax.set_yticks([0,1,2]);ax.grid(axis="y",color="#CBD5E1",alpha=.7)
        fig.text(.077,.95,"Exact eight-pattern sign flip",fontsize=28);fig.text(.077,.89,"Fixed magnitudes: (2, 1, 3)",fontsize=26,color="#64748B");fig.text(.077,.22,"Observed mean = 2",fontsize=28,color="#DC2626");fig.text(.077,.145,"Two-sided extremes: −2 and +2",fontsize=26,color="#DC2626");fig.text(.077,.07,"p = 2 / 8 = 0.25",fontsize=28,color="#7C3AED")
    elif key=="candidate-family":
        for i,y in enumerate([.56,.19]):
            ax=fig.add_axes((.20,y,.68,.24),facecolor="#F8FAFC");grid=np.zeros((12,20));grid[6,3]=1 if i==0 else 0
            ax.pcolormesh(np.arange(21),np.arange(13),grid,cmap=matplotlib.colors.ListedColormap(["#F1F5F9","#7C3AED"]),vmin=0,vmax=1,edgecolors="#CBD5E1",linewidth=.5);ax.set(xlim=(0,20),ylim=(12,0),xlabel="Token index",ylabel="Layer index");ax.set_xticks([.5,9.5,19.5],["1","10","20"]);ax.set_yticks([.5,5.5,11.5],["1","6","12"]);fig.text(.077,y+.24+.025,"Component "+str(i+1)+": 12 × 20",fontsize=27,color="#7C3AED" if i==0 else "#64748B")
        fig.text(.077,.95,"The family is larger than one peak",fontsize=26);fig.text(.077,.91,"Illustrative selected cell",fontsize=26,color="#64748B");fig.text(.077,.075,"12 × 20 × 2 = 480 candidates",fontsize=28,color="#7C3AED")
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
