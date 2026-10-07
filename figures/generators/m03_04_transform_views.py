"""Reproduce M03-04 geometry under specified transformations."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

p=ArgumentParser(); p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output; name=out.stem.removeprefix("M03-04-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                    "svg.fonttype":"none","svg.hashsalt":"mmi-m03-04-"+name})
blue,green,purple,orange="#2563EB","#059669","#7C3AED","#D97706"
bg="#F8FAFC"; fig,ax=plt.subplots(figsize=(8.6,7.4),facecolor=bg)
fig.subplots_adjust(left=.2,right=.93,bottom=.25,top=.87)
ax.set_facecolor(bg); ax.grid(color="#CBD5E1",alpha=.7,linewidth=.8)
ax.set_axisbelow(True); ax.spines[["top","right"]].set_visible(False)
ax.spines[["left","bottom"]].set_color("#64748B"); ax.tick_params(colors="#334155")
ax.set_aspect("equal"); ax.axhline(0,color="#94A3B8",lw=1); ax.axvline(0,color="#94A3B8",lw=1)
if name in ['rotation-before','rotation-after']:
    x,y=np.array([3.,4.]),np.array([1.,-2.])
    if name=='rotation-after':
        q=np.array([[0,-1],[1,0]]); x,y=q@x,q@y
        labels=['Qx = (−4,3)','Qy = (2,1)']; title='After rotating both vectors by 90 degrees'
        positions=[(-4.7,4.25),(1.7,2.1)]
    else:
        labels=['x = (3,4)','y = (1,−2)']; title='Before rotating the two vectors'
        positions=[(1.0,4.8),(.4,-3.1)]
    for v,col,label,pos in zip([x,y],[blue,green],labels,positions):
        ax.add_patch(FancyArrowPatch((0,0),v,arrowstyle='-|>',mutation_scale=9,color=col,lw=2.5))
        ax.text(*pos,label,color=col,fontsize=16)
    ax.plot([x[0],y[0]],[x[1],y[1]],color=purple,lw=1.7,ls='--')
    ax.set(xlim=(-5,5),ylim=(-4,5.5),xlabel='First coordinate',ylabel='Second coordinate')
    footer='Lengths: 5 and √5; inner product: −5; distance: √40.'
elif name=='scaling-breaks-norm':
    ax.add_patch(FancyArrowPatch((0,0),(1,0),arrowstyle='-|>',mutation_scale=9,color=blue,lw=3))
    ax.add_patch(FancyArrowPatch((0,.18),(2,.18),arrowstyle='-|>',mutation_scale=9,color=orange,lw=3))
    ax.text(.3,-.45,'x = (1,0), length 1',color=blue)
    ax.text(.5,.62,'Ax = (2,0), length 2',color=orange)
    ax.set(xlim=(-.4,2.7),ylim=(-.9,1.3),xlabel='First coordinate',ylabel='Second coordinate')
    title='Invertibility does not preserve Euclidean norm'
    footer='A = diag(2,1); the upper arrow is offset for comparison.'
else:
    h=np.array([[0.,0.],[2.,0.],[0.,1.]])
    if name=='sample-geometry-original':
        title='Original rows: three matched samples'; col=blue; footer='rank = 2; AB = 2, AC = 1, BC = √5.'
    elif name=='sample-geometry-orthogonal':
        h=h@np.array([[0,1],[-1,0]])
        title='Orthogonal feature rotation keeps sample distances'; col=green; footer='rank = 2; AB = 2, AC = 1, BC = √5.'
    elif name=='sample-geometry-stretched':
        h=h@np.diag([2,1])
        title='Invertible feature scaling changes sample distances'; col=orange; footer='rank = 2; AB = 4, AC = 1, BC = √17.'
    else:
        raise ValueError(name)
    ax.plot(*np.vstack([h,h[0]]).T,color=col,lw=2,ls='--')
    ax.scatter(*h.T,color=col,s=60,zorder=5)
    for label,v in zip(['A','B','C'],h): ax.annotate(label,xy=v,xytext=(12,14),textcoords='offset points',color=col,fontsize=16)
    ax.set(xlim=(-2,5),ylim=(-1.2,3.5),xlabel='Feature coordinate 1',ylabel='Feature coordinate 2')
fig.suptitle(title,fontsize=20,y=.95)
fig.text(.5,.09,footer,ha='center',fontsize=16,color='#475569')
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format='svg',metadata={'Date':None,'Creator':'mmi'}); plt.close(fig)
