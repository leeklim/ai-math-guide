"""Reproduce M03-07 covector measurements and metric gradients."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

p=ArgumentParser(); p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output; name=out.stem.removeprefix("M03-07-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                    "svg.fonttype":"none","svg.hashsalt":"mmi-m03-07-"+name})
blue,green,purple,orange="#2563EB","#059669","#7C3AED","#D97706"
bg="#F8FAFC"; fig,ax=plt.subplots(figsize=(8.6,7.4),facecolor=bg)
fig.subplots_adjust(left=.18,right=.93,bottom=.25,top=.87)
ax.set_facecolor(bg); ax.grid(color="#CBD5E1",alpha=.5,linewidth=.8)
ax.set_axisbelow(True); ax.spines[["top","right"]].set_visible(False)
ax.spines[["left","bottom"]].set_color("#64748B"); ax.tick_params(colors="#334155")
if name=='metric-gradient-pair':
    x=np.linspace(-2,9,160); y=np.linspace(-3,5,160); X,Y=np.meshgrid(x,y)
    cs=ax.contour(X,Y,8*X+3*Y,levels=[-10,-2,0,10,20,40,60,80],colors='#94A3B8',linewidths=.9)
    ax.clabel(cs,inline=True,fontsize=16,manual=[(-.31,-2.5),(-1.6,3.6),(-1.6,4.27),(-.44,4.5),(.81,4.5),(3.31,4.5),(5.81,4.5),(8.31,4.5)])
    for v,col,label in [((8,3),green,'Euclidean gradient (8,3)'),((2,3),purple,'G-gradient (2,3)'),((-1,2),blue,'v = (−1,2)')]:
        ax.add_patch(FancyArrowPatch((0,0),v,arrowstyle='-|>',mutation_scale=9,color=col,lw=2.7,label=label))
    ax.legend(loc='lower right',facecolor=bg,framealpha=1,fontsize=16)
    ax.set(xlabel='Change in x',ylabel='Change in y',xlim=(-2,9),ylim=(-3,5))
    title='Same differential, different metric gradients'
    footer='Fixed df = [8,3], v = (−1,2).\nBoth appropriate metric pairings give −2.'
else:
    x=np.linspace(-2,5.2,180); y=np.linspace(-2.2,5.2,180); X,Y=np.meshgrid(x,y)
    if name=='covector-measurement':
        Z=2*X-Y; levels=[-4,0,2,4,6,8]
        title='A covector assigns one scalar to each vector'
        footer='At v = (4,2), phi(v) = 2·4 − 2 = 6.'
        positions=[(-1.8,.4),(-.8,-1.6),(.2,-1.6),(1.2,-1.6),(2.2,-1.6),(3.2,-1.6)]
    elif name=='dual-first-coefficient':
        Z=(X+Y)/2; levels=[-1,0,1,2,3,4]
        title='First dual-basis coefficient'
        footer='beta one = (x+y)/2; beta one(v) = 3.'
        positions=[(-.35,-1.65),(1.65,-1.65),(3.65,-1.65),(0,4),(2,4),(4,4)]
    elif name=='dual-second-coefficient':
        Z=(X-Y)/2; levels=[-2,-1,0,1,2,3]
        title='Second dual-basis coefficient'
        footer='beta two = (x−y)/2; beta two(v) = 1.'
        positions=[(-1.65,2.35),(-1.65,.35),(-1.65,-1.65),(.35,-1.65),(2.35,-1.65),(4.35,-1.65)]
    else: raise ValueError(name)
    cs=ax.contour(X,Y,Z,levels=levels,colors='#94A3B8',linewidths=1.2)
    ax.clabel(cs,inline=True,fontsize=16,manual=positions)
    ax.add_patch(FancyArrowPatch((0,0),(4,2),arrowstyle='-|>',mutation_scale=9,color=green,lw=2.7))
    ax.scatter([1,1],[1,-1],color=[blue,orange],s=50,zorder=5)
    ax.scatter([],[],color=blue,label='b1 = (1,1)'); ax.scatter([],[],color=orange,label='b2 = (1,−1)')
    ax.plot([],[],color=green,lw=2.7,label='v = 3b1 + b2 = (4,2)')
    ax.legend(loc='upper left',facecolor=bg,framealpha=1,fontsize=16)
    ax.set(xlabel='Standard coordinate x',ylabel='Standard coordinate y',xlim=(-2,5.2),ylim=(-2.2,7))
    ax.set_aspect('equal')
fig.suptitle(title,fontsize=20,y=.95)
fig.text(.5,.09,footer,ha='center',fontsize=16,color='#475569',linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format='svg',metadata={'Date':None,'Creator':'mmi'}); plt.close(fig)
