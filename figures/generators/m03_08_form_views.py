"""Reproduce separate-slot linearity and quadratic-form level sets."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

p=ArgumentParser();p.add_argument('--output',type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix('M03-08-')
mpl.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'none','svg.hashsalt':'mmi-m03-08-'+name})
blue,green,purple,orange='#2563EB','#059669','#7C3AED','#D97706';bg='#F8FAFC'
fig,ax=plt.subplots(figsize=(8.6,7.4),facecolor=bg)
fig.subplots_adjust(left=.18,right=.93,bottom=.26,top=.87)
ax.set_facecolor(bg);ax.grid(color='#CBD5E1',alpha=.5,lw=.8);ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False);ax.spines[['left','bottom']].set_color('#64748B');ax.tick_params(colors='#334155')
if name=='one-slot-linear':
    t=np.linspace(-2,3,180)
    ax.plot(t,2*t,color=green,lw=2.7,label='Fix v = 2: B(u,2) = 2u')
    ax.scatter([0,1,2],[0,2,4],color=green,s=50)
    ax.set(xlabel='First input u',ylabel='Output B(u,2)',xlim=(-2,3),ylim=(-5,9))
    ax.legend(loc='upper left',facecolor=bg,framealpha=1)
    title='Fix one slot: the other slot is linear'
    footer='Illustration B(u,v) = uv. Doubling u doubles the output.'
elif name=='two-slots-quadratic':
    t=np.linspace(-2,2.1,180)
    ax.plot(t,2*t*t,color=purple,lw=2.7,label='B(a,2a) = 2a²')
    ax.plot(t,2*t,color=orange,lw=2.2,ls='--',label='Joint-linear prediction: 2a')
    ax.scatter([1,2],[2,8],color=purple,s=50)
    ax.set(xlabel='Shared scale a',ylabel='Output',xlim=(-2,2.2),ylim=(-5,13))
    ax.legend(loc='upper left',facecolor=bg,framealpha=1)
    title='Scaling both slots brings two factors'
    footer='At a = 2: B(2,4) = 8, not 2 B(1,2) = 4.'
else:
    bound=4 if name=='cross-term-level-set' else 3
    t=np.linspace(-bound,bound,240);X,Y=np.meshgrid(t,t)
    if name=='positive-definite':
        Z=2*X*X+2*X*Y+2*Y*Y
        cs=ax.contour(X,Y,Z,levels=[1,4,9],colors=green,linewidths=1.8)
        ax.clabel(cs,inline=True,fontsize=16,manual=[(.7,0),(1.4,0),(2.12,0)])
        ax.scatter([0],[0],color=green,s=50)
        title='Positive definite: zero only at the origin'
        footer='G = [[2,1],[1,2]]; q = x² + y² + (x+y)².'
    elif name=='positive-semidefinite':
        Z=X*X
        cs=ax.contour(X,Y,Z,levels=[0.25,1,4],colors=orange,linewidths=1.8)
        ax.clabel(cs,inline=True,fontsize=16,manual=[(.5,-2.6),(1,-2.6),(2,-2.6)])
        ax.axvline(0,color=purple,lw=2.7,label='Every (0,y) has q = 0')
        ax.scatter([0],[1],color=purple,s=60)
        ax.legend(loc='upper left',facecolor=bg,framealpha=1)
        title='Semidefinite: nonzero vectors can have zero value'
        footer='G = diag(1,0); q = x². In particular q(0,1) = 0.'
    elif name=='cross-term-level-set':
        full=2*X*X+2*X*Y+3*Y*Y;diagonal=2*X*X+3*Y*Y
        ax.contour(X,Y,full,levels=[18],colors=green,linewidths=2.7)
        ax.contour(X,Y,diagonal,levels=[18],colors=orange,linewidths=2.1,linestyles='dashed')
        ax.plot([],[],color=green,lw=2.7,label='Full q = 18, including 2xy')
        ax.plot([],[],color=orange,lw=2.1,ls='--',label='Without cross term: q = 18')
        ax.scatter([1],[2],color=blue,s=65,zorder=5)
        ax.text(.95,3.0,'x = (1,2)',color=blue,fontsize=16,ha='center')
        fig.subplots_adjust(top=.71)
        ax.legend(loc='upper center',bbox_to_anchor=(.5,1.37),facecolor=bg,framealpha=1)
        title='The cross term changes the level-set geometry'
        footer='At (1,2): full q = 18; dropping 2xy gives only 14.'
    else:raise ValueError(name)
    ax.set(xlabel='Coordinate x',ylabel='Coordinate y',xlim=(-3,3),ylim=(-3,3));ax.set_aspect('equal')
    if name=='cross-term-level-set':ax.set(xlim=(-3.8,3.8),ylim=(-3.8,3.8))
fig.suptitle(title,fontsize=20,y=.95);fig.text(.5,.09,footer,ha='center',fontsize=16,color='#475569')
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format='svg',metadata={'Date':None,'Creator':'mmi'});plt.close(fig)
