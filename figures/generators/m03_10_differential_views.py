"""Reproduce local approximation error and the partial-derivative counterexample."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
p=ArgumentParser();p.add_argument('--output',type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix('M03-10-')
mpl.rcParams.update({'font.family':'DejaVu Sans','font.size':26,'svg.fonttype':'none','svg.hashsalt':'mmi-m03-10-'+name})
blue,green,purple,orange='#2563EB','#059669','#7C3AED','#D97706';bg='#F8FAFC'
fig,ax=plt.subplots(figsize=(7.2,9.5),facecolor=bg);fig.subplots_adjust(left=.23,right=.94,bottom=.28,top=.73)
ax.set_facecolor(bg);ax.grid(color='#CBD5E1',alpha=.5,lw=.8);ax.spines[['top','right']].set_visible(False)
if name=='relative-local-error':
    s=np.logspace(-3,0,200);h1=.01*s;h2=-.02*s
    remainder=np.hypot(h1*h1+h1*h2,np.expm1(h2)-h2);ratio=remainder/np.hypot(h1,h2)
    ax.loglog(s,ratio,color=green,lw=3)
    ax.set(xlabel='Scale s',ylabel='Relative error',xticks=[.001,.01,.1,1])
    ax.set_xticklabels(['.001','.01','.1','1'])
    title='Local error shrinks\nfaster than the input change'
    footer='h = s (.01,−.02)\nError divided by ||h|| tends to zero.'
elif name=='axis-versus-diagonal':
    t=np.linspace(-.8,.8,200)
    ax.plot(t,np.abs(t)/np.sqrt(2),color=purple,lw=3,label='f(t,t)')
    ax.plot(t,np.zeros_like(t),color=blue,lw=2.5,ls='--',label='f(t,0), f(0,t)')
    ax.set(xlabel='Approach parameter t',ylabel='Function value',xlim=(-.85,.85),ylim=(-.1,.9),xticks=[-.8,0,.8],yticks=[0,.4,.8])
    fig.subplots_adjust(top=.60)
    ax.legend(loc='upper center',bbox_to_anchor=(.5,.81),bbox_transform=fig.transFigure,borderaxespad=0,fontsize=26,facecolor=bg,framealpha=1)
    title='Axes give zero;\nthe diagonal does not'
    footer='Along the diagonal, f(t,t) = |t| / √2.\nAxis partial derivatives miss this change.'
elif name=='diagonal-relative-error':
    t=np.logspace(-4,-.1,200)
    ax.semilogx(t,np.full_like(t,.5),color=orange,lw=3)
    ax.set(xlabel='Positive t toward zero',ylabel='Error / ||(t,t)||',ylim=(0,1),yticks=[0,.5,1],xticks=[.0001,.01,1])
    ax.set_xticklabels(['.0001','.01','1'])
    title='The zero linear map\ncannot approximate all paths'
    footer='|f(t,t)| / ||(t,t)|| = 1/2.\nThis ratio does not tend to zero.'
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.5)
fig.text(.5,.10,footer,ha='center',fontsize=24,color='#475569',linespacing=1.6)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format='svg',metadata={'Date':None,'Creator':'mmi'});plt.close(fig)
