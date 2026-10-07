"""Reproduce float64 central-difference error for the existing scalar graph."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
p=ArgumentParser();p.add_argument('--output',type=Path,required=True);out=p.parse_args().output
mpl.rcParams.update({'font.family':'DejaVu Sans','font.size':26,'svg.fonttype':'none','svg.hashsalt':'mmi-m03-14-difference-error'})
e=np.logspace(-15,0,160)
plus=(2+e)**2*(4-e)**2;minus=(2-e)**2*(4+e)**2
err=np.abs((plus-minus)/(2*e)-32);err[err==0]=np.nan
fig,ax=plt.subplots(figsize=(7.2,9.5),facecolor='#F8FAFC');fig.subplots_adjust(left=.24,right=.94,bottom=.29,top=.72)
ax.set_facecolor('#F8FAFC');ax.loglog(e,err,color='#059669',lw=2.6)
ax.grid(color='#CBD5E1',alpha=.5,lw=.8);ax.spines[['top','right']].set_visible(False)
ax.set(xlabel='Difference step ε',ylabel='Absolute derivative error',xticks=[1e-15,1e-10,1e-5,1],yticks=[1e-10,1e-5,1])
fig.suptitle('Finite differences:\nsmaller is not always better',fontsize=28,y=.94,linespacing=1.5)
fig.text(.5,.14,'Reference derivative: 32.',ha='center',fontsize=24,color='#475569')
fig.text(.5,.085,'Float64 central difference; zeros omitted.',ha='center',fontsize=22,color='#475569')
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format='svg',metadata={'Date':None,'Creator':'mmi'});plt.close(fig)
