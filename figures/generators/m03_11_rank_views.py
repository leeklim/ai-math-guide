"""Reproduce input directions and rank-one image for the example ReLU Jacobian."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
p=ArgumentParser();p.add_argument('--output',type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix('M03-11-')
mpl.rcParams.update({'font.family':'DejaVu Sans','font.size':26,'svg.fonttype':'none','svg.hashsalt':'mmi-m03-11-'+name})
green,orange='#059669','#D97706';bg='#F8FAFC'
fig,ax=plt.subplots(figsize=(7.2,9.5),facecolor=bg);fig.subplots_adjust(left=.2,right=.94,bottom=.32,top=.77)
ax.set_facecolor(bg);ax.grid(color='#CBD5E1',alpha=.5,lw=.8);ax.spines[['top','right']].set_visible(False)
ax.set_axisbelow(True)
if name=='relu-input-directions':
    t=np.linspace(0,2*np.pi,240);ax.plot(np.cos(t),np.sin(t),color='#94A3B8',lw=1.5,ls='--')
    for v,c in [((1/np.sqrt(5),2/np.sqrt(5)),green),((-2/np.sqrt(5),1/np.sqrt(5)),orange)]:
        ax.add_patch(FancyArrowPatch((0,0),v,arrowstyle='-|>',mutation_scale=9,color=c,lw=3))
    ax.set(xlim=(-1.4,1.4),ylim=(-1.4,1.4),xlabel='Input change x',ylabel='Input change y',xticks=[-1,0,1],yticks=[-1,0,1]);ax.set_aspect('equal')
    title='Two unit directions\nof the local ReLU Jacobian'
    fig.text(.5,.19,'Green: (1,2) / √5',ha='center',fontsize=24,color=green)
    fig.text(.5,.13,'Orange: (−2,1) / √5',ha='center',fontsize=24,color=orange)
    fig.text(.5,.07,'The dashed circle marks unit inputs.',ha='center',fontsize=24,color='#475569')
elif name=='relu-rank-one-image':
    ax.plot([-np.sqrt(5),np.sqrt(5)],[0,0],color='#94A3B8',lw=8,alpha=.45)
    ax.add_patch(FancyArrowPatch((0,0),(np.sqrt(5),0),arrowstyle='-|>',mutation_scale=9,color=green,lw=3))
    ax.scatter([0],[0],color=orange,s=80,zorder=5)
    ax.set(xlim=(-2.8,2.8),ylim=(-1.4,1.4),xlabel='Output change 1',ylabel='Output change 2',xticks=[-2,0,2],yticks=[-1,0,1]);ax.set_aspect('equal')
    title='A rank-one image:\nall changes lie on one axis'
    fig.text(.5,.19,'Green direction maps to (√5,0).',ha='center',fontsize=24,color=green)
    fig.text(.5,.13,'Orange direction maps to zero.',ha='center',fontsize=24,color=orange)
    fig.text(.5,.07,'This statement is local at x = (2,1).',ha='center',fontsize=24,color='#475569')
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format='svg',metadata={'Date':None,'Creator':'mmi'});plt.close(fig)
