"""Reproduce example Hessian directions, critical-point sections, and coordinate scaling."""
from argparse import ArgumentParser
from pathlib import Path
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
p=ArgumentParser();p.add_argument('--output',type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix('M03-12-')
mpl.rcParams.update({'font.family':'DejaVu Sans','font.size':26,'svg.fonttype':'none','svg.hashsalt':'mmi-m03-12-'+name})
blue,green,purple,orange='#2563EB','#059669','#7C3AED','#D97706';bg='#F8FAFC'
fig,ax=plt.subplots(figsize=(7.2,9.5),facecolor=bg);fig.subplots_adjust(left=.23,right=.94,bottom=.29,top=.73)
ax.set_facecolor(bg);ax.grid(color='#CBD5E1',alpha=.5,lw=.8);ax.set_axisbelow(True);ax.spines[['top','right']].set_visible(False)
legend=False;t=np.linspace(-1,1,200)
if name=='principal-curvature-directions':
    z=np.linspace(-4,4,260);X,Y=np.meshgrid(z,z);Z=X*X+X*Y+2*Y*Y
    ax.contour(X,Y,Z,levels=[1,4,9],colors='#94A3B8',linewidths=1.5)
    vals,vec=np.linalg.eigh(np.array([[2,1],[1,4]]))
    for i,c in [(0,purple),(1,green)]:ax.add_patch(FancyArrowPatch((0,0),tuple(1.5*vec[:,i]),arrowstyle='-|>',mutation_scale=9,color=c,lw=3))
    ax.set(xlim=(-3.8,3.8),ylim=(-3.8,3.8),xlabel='Coordinate x',ylabel='Coordinate y',xticks=[-3,0,3],yticks=[-3,0,3]);ax.set_aspect('equal')
    title='Orthogonal directions\nwith different positive curvature'
    footer='Purple: 3−√2; green: 3+√2.\nContours show f = 1, 4, 9.'
elif name=='principal-direction-sections':
    ax.plot(t,.5*(3+np.sqrt(2))*t*t,color=green,lw=3,label='Higher curvature')
    ax.plot(t,.5*(3-np.sqrt(2))*t*t,color=purple,lw=3,ls='--',label='Lower curvature')
    ax.set(xlabel='Unit-direction distance t',ylabel='Function value',xlim=(-1.1,1.1),ylim=(-.2,2.7),xticks=[-1,0,1],yticks=[0,1,2]);legend=True
    title='Different curvature,\ndifferent quadratic cost'
    footer='f(t q) = ½ λ t² at the minimum.\nHessian curvature λ enters with ½.'
elif name=='saddle-sections':
    ax.plot(t,t*t,color=green,lw=3,label='Along x: t²');ax.plot(t,-t*t,color=orange,lw=3,ls='--',label='Along y: −t²')
    ax.set(xlabel='Distance t from the origin',ylabel='Function value',xlim=(-1.1,1.1),ylim=(-1.3,1.3),xticks=[-1,0,1],yticks=[-1,0,1]);legend=True
    title='A saddle rises in one direction\nand falls in another'
    footer='f = x²−y²; Hessian eigenvalues ±2.\nNeither a minimum nor a maximum.'
elif name=='zero-hessian-quartics':
    ax.plot(t,t**4,color=green,lw=3,label='x⁴: minimum');ax.plot(t,-t**4,color=orange,lw=3,ls='--',label='−x⁴: maximum')
    ax.set(xlabel='Coordinate x',ylabel='Function value',xlim=(-1.1,1.1),ylim=(-1.3,1.3),xticks=[-1,0,1],yticks=[-1,0,1]);legend=True
    title='The same zero Hessian\ndoes not decide the extremum'
    footer='At x = 0, both Hessians are zero.\nFourth-order terms decide.'
elif name=='least-squares-flat-direction':
    z=np.linspace(-2,5,260);X,Y=np.meshgrid(z,z);Z=.5*(X+2*Y-3)**2
    ax.contour(X,Y,Z,levels=[.5,2],colors='#94A3B8',linewidths=1.5)
    x=np.linspace(-1,4,120);ax.plot(x,(3-x)/2,color=green,lw=2)
    ax.add_patch(FancyArrowPatch((1,1),(3,0),arrowstyle='-|>',mutation_scale=9,color=orange,lw=3))
    ax.scatter([1],[1],color=orange,s=60,zorder=5)
    ax.set(xlim=(-1,4),ylim=(-1,3),xlabel='Parameter θ1',ylabel='Parameter θ2',xticks=[0,2,4],yticks=[-1,1,3]);ax.set_aspect('equal')
    title='A flat direction\nalong a minimum valley'
    footer='Change (2,−1) preserves θ1+2θ2.\nGreen line: loss is zero everywhere.'
elif name=='coordinate-scaled-curvature':
    x=np.linspace(-1.1,1.1,200);ax.plot(x,x*x,color=blue,lw=3,label='f(x) = x²');ax.plot(x,4*x*x,color=purple,lw=3,ls='--',label='g(z) = 4z²')
    ax.scatter([1,.5],[1,1],color=[blue,purple],s=70,zorder=5)
    ax.set(xlabel='Coordinate value x or z',ylabel='Same loss function',xlim=(-1.1,1.1),ylim=(-.2,5.3),xticks=[-1,0,1],yticks=[0,2,4]);legend=True
    title='A coordinate scale\nchanges Hessian magnitude'
    footer='x = 2z: f″ = 2, but g″ = 8.\nx = 1 and z = .5 both give value 1.'
else:raise ValueError(name)
if legend:
    fig.subplots_adjust(top=.60)
    ax.legend(loc='upper center',bbox_to_anchor=(.5,.81),bbox_transform=fig.transFigure,borderaxespad=0,fontsize=24,facecolor=bg,framealpha=1)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.5);fig.text(.5,.10,footer,ha='center',fontsize=24,color='#475569',linespacing=1.6)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format='svg',metadata={'Date':None,'Creator':'mmi'});plt.close(fig)
