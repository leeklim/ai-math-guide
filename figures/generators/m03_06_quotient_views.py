"""Reproduce M03-06 equivalence-class and representative comparisons."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

p=ArgumentParser(); p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output; name=out.stem.removeprefix("M03-06-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                    "svg.fonttype":"none","svg.hashsalt":"mmi-m03-06-"+name})
blue,green,purple,orange="#2563EB","#059669","#7C3AED","#D97706"
bg="#F8FAFC"; fig,ax=plt.subplots(figsize=(8.6,7.4),facecolor=bg)
fig.subplots_adjust(left=.2,right=.93,bottom=.25,top=.87)
ax.set_facecolor(bg); ax.grid(color="#CBD5E1",alpha=.7,linewidth=.8)
ax.set_axisbelow(True); ax.spines[["top","right"]].set_visible(False)
ax.spines[["left","bottom"]].set_color("#64748B"); ax.tick_params(colors="#334155")
def arrow(a,b,col,ls='-'): ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=9,color=col,lw=2.5,linestyle=ls))
if name=='mod-three-partition':
    for c,col,mark in [(0,blue,'o'),(1,orange,'s'),(2,green,'^')]:
        vals=np.array([v for v in range(-3,9) if v%3==c]); ax.scatter(vals,np.full_like(vals,c),color=col,marker=mark,s=55,zorder=5)
        ax.plot(vals,np.full_like(vals,c),color=col,lw=1.2,ls=':')
    ax.scatter([1,4],[1,1],s=140,facecolors='none',edgecolors=purple,lw=2,zorder=6)
    ax.set(xlim=(-4,9),ylim=(-.5,3.5),xlabel='Integer representative',ylabel='Equivalence class')
    ax.set_xticks(range(-3,9,2)); ax.set_yticks([0,1,2],['[0]','[1]','[2]'])
    ax.text(-2,2.85,'1 and 4 name the same class',color=purple)
    title='Remainder modulo three partitions the integers'; footer='Each shown class continues indefinitely in both directions.'
elif name=='parallel-cosets':
    ax.axhline(0,color=blue,lw=2,label='U: y = 0')
    ax.axhline(3,color=green,lw=2,label='(2,3)+U: y = 3')
    ax.axhline(4,color=orange,lw=2,ls='--',label='Different coset: y = 4')
    ax.scatter([2,5],[3,3],color=green,s=55,zorder=5); ax.scatter([2],[4],color=orange,s=55,zorder=5)
    arrow((2.12,3),(4.86,3),green); arrow((2,3.1),(2,3.88),orange)
    ax.text(2,2.55,'(2,3)',color=green); ax.text(4.6,2.55,'(5,3)',color=green)
    ax.text(2.35,4.1,'(2,4)',color=orange)
    ax.set(xlim=(-1,6),ylim=(-.7,7),xlabel='First coordinate',ylabel='Second coordinate')
    ax.legend(loc='upper left',frameon=False,fontsize=16)
    title='A coset is a whole translated subspace'; footer='Horizontal difference is in U; vertical difference is not.'
elif name=='representative-independent-addition':
    ax.axhline(3,color=blue,lw=1.2,ls=':'); ax.axhline(7,color=green,lw=2)
    ax.add_patch(FancyArrowPatch((0,0),(2,3),arrowstyle='-|>',mutation_scale=12,
                                color=blue,lw=2.5,shrinkA=5,shrinkB=0,zorder=4))
    ax.add_patch(FancyArrowPatch((2,3),(1,7),arrowstyle='-|>',mutation_scale=9,
                                color=purple,lw=2.5,shrinkA=9,zorder=3))
    arrow((0,0),(5,3),blue,'--'); arrow((5,3),(7,7),purple,'--')
    ax.scatter([0],[0],color='#64748B',s=40,zorder=6)
    ax.text(-1.65,-.48,'Start (0,0)',color='#64748B')
    ax.scatter([1,7],[7,7],color=green,s=55,zorder=5)
    ax.text(.2,7.5,'(1,7)',color=green); ax.text(6.5,7.5,'(7,7)',color=green)
    ax.text(-1.5,2.5,'v',color=blue); ax.text(-1.5,1.7,'(2,3)',color=blue)
    ax.text(5,1.55,'v′ = (5,3)',color=blue)
    ax.text(-1.5,5.9,'+ w',color=purple); ax.text(-1.5,5.1,'(−1,4)',color=purple)
    ax.text(7.25,4.8,'+ w′',color=purple); ax.text(7.25,4.0,'(2,4)',color=purple)
    ax.set(xlim=(-2,9),ylim=(-1,10),xlabel='First coordinate',ylabel='Second coordinate')
    title='Changing representatives leaves the sum coset unchanged'; footer='Both result points lie on the same height-seven coset.'
elif name=='coset-scalar-multiplication':
    ax.axhline(3,color=blue,lw=2,label='Input coset: height 3'); ax.axhline(6,color=green,lw=2,label='Doubled coset: height 6')
    arrow((0,0),(2,3),blue); arrow((2,3),(4,6),green)
    ax.text(2.2,3.2,'v = (2,3)',color=blue); ax.text(4.15,6.2,'2v = (4,6)',color=green)
    ax.set(xlim=(-1,6),ylim=(-1,9),xlabel='First coordinate',ylabel='Second coordinate')
    ax.legend(loc='upper left',frameon=False,fontsize=16)
    title='Multiply the representative, then take its class'; footer='The first coordinate varies freely inside each class.'
elif name=='quotient-versus-representative':
    ax.axhline(3,color=green,lw=2,label='Entire coset: y = 3')
    ax.axhline(0,color=blue,lw=1.8,label='U: horizontal direction')
    ax.axvline(0,color=orange,lw=2,ls='--',label='Chosen U-perp')
    ax.scatter([2],[3],color=blue,s=55,zorder=5); ax.scatter([0],[3],color=orange,s=85,zorder=5)
    arrow((1.8,3),(.18,3),purple)
    ax.text(.25,3.55,'Chosen representative (0,3)',color=orange)
    ax.text(2.1,2.45,'v = (2,3)',color=blue)
    ax.set(xlim=(-1,6),ylim=(-.7,7),xlabel='First coordinate',ylabel='Second coordinate')
    ax.legend(loc='upper right',frameon=False,fontsize=16)
    title='Quotient class and selected representative differ'; footer='Euclidean projection selects one point from the whole coset.'
elif name=='derivative-class-image':
    t=np.linspace(-1,2,300)
    ax.plot(t,2+3*t+t*t,color=blue,lw=2.5,label='p(t) = 2 + 3t + t²')
    ax.plot(t,-5+3*t+t*t,color=purple,lw=2.5,ls='--',label='q(t) = −5 + 3t + t²')
    ax.plot(t,3+2*t,color=green,lw=3,ls=':',label='D(p) = D(q) = 3 + 2t')
    ax.set(xlabel='Polynomial input t',ylabel='Function value',ylim=(-9,22))
    ax.legend(loc='upper left',frameon=False,fontsize=16)
    title='One constant-shift class has one derivative image'; footer='p−q = 7 is in ker D; their output derivatives agree.'
else: raise ValueError(name)
fig.suptitle(title,fontsize=20,y=.95)
fig.text(.5,.09,footer,ha='center',fontsize=16,color='#475569')
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format='svg',metadata={'Date':None,'Creator':'mmi'}); plt.close(fig)
