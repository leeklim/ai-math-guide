"""Reproduce M03-05 subspace and decomposition geometry."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

p=ArgumentParser(); p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output; name=out.stem.removeprefix("M03-05-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                    "svg.fonttype":"none","svg.hashsalt":"mmi-m03-05-"+name})
blue,green,purple,orange="#2563EB","#059669","#7C3AED","#D97706"
bg="#F8FAFC"; fig=plt.figure(figsize=(8.6,7.4),facecolor=bg)
if name=='activation-orthogonal-decomposition':
    fig.set_size_inches(8.6,8.8)
    ax=fig.add_subplot(111,projection='3d'); fig.subplots_adjust(left=.09,right=.92,bottom=.20,top=.68)
    u=np.array([2.,2.,0.]); h=np.array([3.,1.,2.]); r=h-u
    a=np.linspace(-1,3,30); ax.plot(a,a,np.zeros_like(a),color=blue,lw=2,label='U: span(1,1,0)')
    for v,col,label in [(h,green,'h = (3,1,2)'),(u,blue,'hU = (2,2,0)'),(r,orange,'Residual = (1,−1,2)')]:
        ax.quiver(0,0,0,*v,color=col,lw=2,arrow_length_ratio=.08,label=label)
    ax.plot(*np.vstack([u,h]).T,color=orange,ls='--',lw=2)
    ax.set(xlim=(-1,3.8),ylim=(-1.8,3.8),zlim=(0,3.8),xlabel='x1',ylabel='x2',zlabel='x3')
    ax.set_xticks([0,2]); ax.set_yticks([0,2]); ax.set_zticks([0,2])
    ax.view_init(elev=24,azim=-57)
    fig.legend(loc='upper left',bbox_to_anchor=(.12,.88),frameon=False,fontsize=16)
    title='Activation and orthogonal components'; footer='hU · residual = 0; squared lengths: 8 + 6 = 14.'
else:
    ax=fig.add_subplot(111); fig.subplots_adjust(left=.18,right=.93,bottom=.25,top=.87)
    ax.set_facecolor(bg); ax.grid(color='#CBD5E1',alpha=.7,linewidth=.8)
    ax.set_axisbelow(True); ax.spines[['top','right']].set_visible(False)
    ax.spines[['left','bottom']].set_color('#64748B'); ax.tick_params(colors='#334155')
    ax.set_aspect('equal'); ax.set(xlim=(-.5,5),ylim=(-.8,4.2),xlabel='First coordinate',ylabel='Second coordinate')
    def arrow(a,b,col): ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=9,color=col,lw=2.5))
    ax.axhline(0,color=blue,lw=2); ax.text(4.6,.25,'U',color=blue)
    if name=='sum-not-union':
        ax.axvline(0,color=purple,lw=2); ax.text(.25,3.7,'W',color=purple)
        arrow((0,0),(2,0),blue); arrow((2,0),(2,1),purple); arrow((0,0),(2,1),green)
        ax.scatter([2],[1],color=green,s=45,zorder=5)
        ax.text(1.6,1.5,'(2,1) ∈ U+W',color=green); ax.text(1.0,3.0,'Neither axis contains (2,1)',color='#475569')
        title='The sum contains mixed directions beyond the union'; footer='U is the horizontal line; W is the vertical line.'
    elif name=='overlap-nonunique':
        ax.set_facecolor('#FFF7ED'); ax.text(.8,3.1,'W is the whole plane',color=orange)
        arrow((0,0),(1,0),blue); ax.scatter([1],[0],s=110,facecolors='none',edgecolors=orange,lw=2,zorder=5)
        ax.text(.8,1.9,'e1 belongs to both U and W',color='#475569')
        ax.text(.8,1.2,'e1 + 0 = 0 + e1',color=purple)
        title='A shared nonzero direction prevents uniqueness'; footer='U ∩ W = U, so the sum is not direct.'
    elif name in ['vertical-complement','diagonal-complement']:
        v=np.array([3.,2.]); orth=name=='vertical-complement'
        u=np.array([3.,0.]) if orth else np.array([1.,0.]); w=v-u
        if orth:
            ax.axvline(0,color=purple,lw=2); ax.text(.25,3.6,'W1',color=purple)
            title='Choose the vertical complement'; footer='(3,2) = (3,0) + (0,2); this complement is orthogonal.'
        else:
            t=np.linspace(-.5,4.2,100); ax.plot(t,t,color=purple,lw=2); ax.text(3.25,3.65,'W2',color=purple)
            title='Choose the diagonal complement'; footer='(3,2) = (1,0) + (2,2); direct need not mean orthogonal.'
        arrow((0,0),u,blue); arrow(u,v,purple); arrow((0,0),v,green)
        ax.text(3.15,2.2,'v = (3,2)',color=green)
        ax.text(2.7,-.55,'U part: (3,0)' if orth else 'U part: (1,0)',color=blue)
        ax.text(.5,2.85,'W part: (0,2)' if orth else 'W part: (2,2)',color=purple)
    else: raise ValueError(name)
fig.suptitle(title,fontsize=20,y=.95)
fig.text(.5,.09,footer,ha='center',fontsize=16,color='#475569')
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,format='svg',metadata={'Date':None,'Creator':'mmi'}); plt.close(fig)
