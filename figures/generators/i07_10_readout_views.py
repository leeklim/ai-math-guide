"""Reproduce readout accounting and its normalization boundary from I07-10."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-10-readout","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
BLUE,PURPLE,GREEN,AMBER,GRAY="#2563EB","#7C3AED","#059669","#D97706","#64748B"
def arrow(ax,a,b,col,dash=False):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="->",mutation_scale=12,lw=2.5,color=col,linestyle="--" if dash else "-",shrinkA=0,shrinkB=0,zorder=4))
def axes(fig,pos,xlim,ylim):
    ax=fig.add_axes(pos,facecolor="#F8FAFC");ax.set(xlim=xlim,ylim=ylim,xlabel="Coordinate 1",ylabel="Coordinate 2");ax.grid(color="#CBD5E1",alpha=.7);ax.set_aspect("equal");return ax
def main(output):
    key=output.stem.removeprefix("I07-10-");fig=plt.figure(figsize=(520/72,1050/72),facecolor="#F8FAFC")
    if key=="readout-inner-products":
        fig.text(.077,.95,"One direction, additive readout",fontsize=27);ax=axes(fig,(.18,.37,.70,.47),(-.3,3.7),(-.3,4.7));ax.set_xticks([0,1,2,3]);ax.set_yticks([0,2,4])
        for v,col in [((1,0),BLUE),((0,2),PURPLE),((1,2),GREEN),((3,4),AMBER)]:arrow(ax,(0,0),v,col)
        for x,y,s,col in [(1.15,.02,"r₁",BLUE),(.13,2.16,"r₂",PURPLE),(1.13,2.08,"r",GREEN),(2.65,4.18,"u",AMBER)]:ax.text(x,y,s,color=col,fontsize=28)
        for y,s,col in [(.23,"u · r₁ = 3",BLUE),(.17,"u · r₂ = 8",PURPLE),(.10,"u · (r₁ + r₂) = 11",GREEN)]:fig.text(.077,y,s,color=col,fontsize=28)
        fig.text(.077,.05,"Vectors add before the same readout.",fontsize=25,color=GRAY)
    elif key=="target-minus-foil":
        fig.text(.077,.95,"Subtract readout directions",fontsize=28);ax=axes(fig,(.19,.35,.70,.48),(-.3,2.8),(-1.5,2.8));ax.set_xticks([0,1,2]);ax.set_yticks([-1,0,1,2])
        arrow(ax,(0,0),(2,1),BLUE);arrow(ax,(0,0),(1,-1),GRAY);arrow(ax,(0,0),(1,2),PURPLE);arrow(ax,(1,-1),(2,1),PURPLE,True)
        for x,y,s,col in [(1.7,1.15,"u_y",BLUE),(1.12,-1.15,"u_q",GRAY),(.34,2.19,"u_y − u_q",PURPLE)]:ax.text(x,y,s,color=col,fontsize=26)
        for y,s in [(.23,"u_y = (2, 1); u_q = (1, −1)",),(.16,"Difference direction = (1, 2)",),(.09,"Logit gap adds one bias gap.",)]:fig.text(.077,y,s,fontsize=26,color=PURPLE if y==.16 else GRAY)
    elif key=="cpu-contribution-waterfall":
        fig.text(.077,.95,"Readout accounting: CPU example",fontsize=26);fig.text(.077,.91,"u = (1, 2, −1); no final norm",fontsize=25,color=GRAY)
        ax=fig.add_axes((.23,.31,.65,.51),facecolor="#F8FAFC");vals=[.5,3.5,-1.5];starts=np.array([0,.5,4]);names=["Embed","Attn","MLP"]
        for i,(v,b,col) in enumerate(zip(vals,starts,[BLUE,PURPLE,GREEN])):ax.bar(i,v,bottom=b,color=col,alpha=.8,width=.6);ax.text(i,b+v+(0.17 if v>0 else -.48),f"{v:+.1f}",ha="center",fontsize=26,color=col)
        for i in range(2):ax.plot([i+.3,i+.7],[starts[i]+vals[i]]*2,color=GRAY,ls="--",lw=1.6)
        ax.axhline(2.5,color=AMBER,ls=":",lw=2);ax.set(ylim=(-.5,5.1),ylabel="Cumulative logit",xlim=(-.6,2.7));ax.set_xticks(range(3),names);ax.set_yticks([0,2,4]);ax.grid(axis="y",color="#CBD5E1",alpha=.7)
        for y,s in [(.20,"0 + 0.5 + 3.5 − 1.5 = 2.5"),(.13,"r = (1.5, 1, 1)"),(.065,"u · r = 2.5; bias counted once")]:fig.text(.077,y,s,fontsize=27,color=AMBER if y==.20 else GRAY)
    elif key=="normalize-sum-or-parts":
        fig.text(.077,.95,"Normalize the sum, not each part",fontsize=26);ax=axes(fig,(.19,.33,.70,.49),(-.1,1.3),(-.1,1.4));ax.set_xticks([0,1]);ax.set_yticks([0,1])
        a=np.array([1,2])/np.sqrt(5);arrow(ax,(0,0),a,GREEN);arrow(ax,(0,0),(1,1),AMBER);t=np.linspace(0,np.pi/2,120);ax.plot(np.cos(t),np.sin(t),ls=":",color=GRAY,lw=1.8)
        ax.text(.12,1.20,"N(r₁+r₂)",color=GREEN,fontsize=26);ax.text(.84,1.20,"Parts",color=AMBER,fontsize=26)
        for y,s,col in [(.22,"Raw parts: (1, 0), (0, 2)",GRAY),(.16,"Sum first: (1, 2) / √5",GREEN),(.10,"Parts first: (1, 1)",AMBER)]:fig.text(.077,y,s,fontsize=27,color=col)
    elif key=="shared-scale-accounting":
        fig.text(.077,.95,"One shared scale for this run",fontsize=28);ax=axes(fig,(.19,.33,.70,.49),(-.1,1.3),(-.1,1.4));ax.set_xticks([0,1]);ax.set_yticks([0,1]);a=1/np.sqrt(5);b=2/np.sqrt(5)
        arrow(ax,(0,0),(a,0),BLUE);arrow(ax,(a,0),(a,b),PURPLE);arrow(ax,(0,0),(a,b),GREEN)
        ax.text(.61,.12,"r₁ / √5",color=BLUE,fontsize=27);ax.text(.61,.43,"r₂ / √5",color=PURPLE,fontsize=27);ax.text(.09,1.08,"N(r₁+r₂)",color=GREEN,fontsize=27)
        for y,s,col in [(.22,"Same √5 for both components",GRAY),(.15,"Their sum = (1, 2) / √5",GREEN),(.08,"Removal changes the denominator.",AMBER)]:fig.text(.077,y,s,fontsize=26,color=col)
    elif key=="direct-versus-recomputed-removal":
        fig.text(.077,.95,"Fixed accounting ≠ removal effect",fontsize=26);fig.text(.077,.91,"N(r) = r / ‖r‖; u = (3, 4)",fontsize=26,color=GRAY)
        ax=fig.add_axes((.20,.33,.70,.46),facecolor="#F8FAFC");values=[8/np.sqrt(5),11/np.sqrt(5)-3];ax.bar([0,1],values,color=[PURPLE,GREEN],width=.5);ax.set(ylim=(0,4.5),ylabel="Logit amount",xlim=(-.55,1.55));ax.set_xticks([0,1],["Fixed\nscale","Recompute\nnorm"]);ax.set_yticks([0,2,4]);ax.grid(axis="y",color="#CBD5E1",alpha=.7)
        for x,v in enumerate(values):ax.text(x,v+.12,f"{v:.3f}",ha="center",fontsize=27,color=[PURPLE,GREEN][x])
        for y,s,col in [(.20,"Original logit: 11/√5 ≈ 4.919",GRAY),(.14,"Remove r₂: N(1,0) → logit 3",GREEN),(.08,"Drop ≈ 1.919, not 8/√5",AMBER)]:fig.text(.077,y,s,fontsize=26,color=col)
    else:raise ValueError(key)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
