"""Reproduce coordinate gradients and exact ReLU scaling examples without model execution."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
p=ArgumentParser();p.add_argument('--output',type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix('M03-15-')
mpl.rcParams.update({'font.family':'DejaVu Sans','font.size':26,'svg.fonttype':'none','svg.hashsalt':'mmi-m03-15-'+name})
blue,green,purple,orange='#2563EB','#059669','#7C3AED','#D97706';bg='#F8FAFC'
fig,ax=plt.subplots(figsize=(7.2,9.5),facecolor=bg);fig.subplots_adjust(left=.23,right=.94,bottom=.29,top=.73)
ax.set_facecolor(bg);ax.grid(color='#CBD5E1',alpha=.5,lw=.8);ax.set_axisbelow(True);ax.spines[['top','right']].set_visible(False)
legend=False
if name in {'old-coordinate-gradient','new-coordinate-gradient'}:
    old=name=='old-coordinate-gradient';x=np.linspace(.1,3 if old else 1.7,220);base=2 if old else 1;scale=1 if old else 4;slope=4 if old else 8
    ax.plot(x,scale*x*x,color=blue if old else purple,lw=3)
    z=np.linspace(base-.45,base+.45,80);ax.plot(z,4+slope*(z-base),color=orange,ls='--',lw=2.4)
    ax.scatter([base],[4],color=green,s=80,zorder=5)
    ax.set(xlabel='Old coordinate θ' if old else 'New coordinate φ',ylabel='Loss value',xlim=(0,3.1 if old else 1.8),ylim=(0,12),xticks=[0,1,2,3] if old else [0,.5,1,1.5],yticks=[0,4,8,12])
    title='Old coordinates:\nL(θ) = θ²' if old else 'New coordinates:\nθ = 2φ, L tilde = 4φ²'
    footer='At θ = 2: value 4, gradient 4.' if old else 'At φ = 1: value 4, gradient 8.'
elif name=='scaled-hidden-activation':
    x=np.linspace(-1.2,1.2,220);h=np.maximum(2*x+1,0)
    ax.plot(x,h,color=blue,lw=3,label='ReLU(2x+1)');ax.plot(x,4*h,color=purple,lw=3,ls='--',label='ReLU(8x+4)')
    ax.set(xlabel='Input x',ylabel='Hidden activation',xlim=(-1.2,1.2),ylim=(-.5,15),xticks=[-1,0,1],yticks=[0,5,10,15]);legend=True
    title='Scaling changes\nthe hidden activation'
    footer='Hidden activation becomes fourfold.'
elif name=='same-output-function':
    x=np.linspace(-1.2,1.2,220);original=3*np.maximum(2*x+1,0);scaled=.75*np.maximum(8*x+4,0)
    ax.plot(x,original,color=blue,lw=4,label='Original output');ax.plot(x,scaled,color=purple,lw=2.5,ls='--',label='Scaled output')
    ax.set(xlabel='Input x',ylabel='Model output',xlim=(-1.2,1.2),ylim=(-.5,12),xticks=[-1,0,1],yticks=[0,4,8,12]);legend=True
    title='The output function\nis exactly unchanged'
    footer='Outgoing weight: 3 becomes 3/4.'
elif name=='symmetry-curve-versus-tangent':
    t=np.linspace(-.6,.6,200)
    exact=np.full_like(t,4.5);straight=.5*((3-3*t)*np.maximum(1+t,0))**2
    ax.plot(t,exact,color=green,lw=3,label='Exact scaling path');ax.plot(t,straight,color=orange,lw=3,ls='--',label='Straight tangent path')
    ax.set(xlabel='Path parameter t',ylabel='One-sample loss',xlim=(-.65,.65),ylim=(1.5,5.1),xticks=[-.5,0,.5],yticks=[2,3,4,5]);legend=True
    title='A flat symmetry curve\nand a nonflat tangent line'
    footer='At x = 0, target 0: L = ½ f(0)².\nThe paths agree only to first order.'
else:raise ValueError(name)
if legend:
    fig.subplots_adjust(top=.60)
    ax.legend(loc='upper center',bbox_to_anchor=(.5,.81),bbox_transform=fig.transFigure,borderaxespad=0,fontsize=24,facecolor=bg,framealpha=1)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.5);fig.text(.5,.10,footer,ha='center',fontsize=24,color='#475569',linespacing=1.6)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format='svg',metadata={'Date':None,'Creator':'mmi'});plt.close(fig)
