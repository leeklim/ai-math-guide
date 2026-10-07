"""Analytic path and slice examples for I08-07; no model training."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True)
out=p.parse_args().output;name=out.stem.removeprefix("I08-07-")
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706"
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,
 "xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"i08-07-"+name})
def setup(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True)
 ax.spines[["top","right"]].set_visible(False)
def single():
 fig,ax=plt.subplots(figsize=(520/72,820/72),facecolor=bg)
 fig.subplots_adjust(left=.23,right=.92,bottom=.38,top=.76);setup(ax)
 return fig,ax
def pair(height=820):
 fig,axs=plt.subplots(1,2,figsize=(1120/72,height/72),facecolor=bg)
 fig.subplots_adjust(left=.10,right=.96,bottom=.38,top=.72,wspace=.37)
 for ax in axs:setup(ax)
 return fig,axs
a=np.linspace(0,1,401)
if name=="barrier-reference":
 fig,ax=single();L=.1+.6*np.sin(np.pi*a)**2
 ax.plot(a,L,color=blue,lw=3);ax.axhline(.1,color=orange,ls="--",lw=2,label="Endpoint max = 0.1")
 ax.annotate("",xy=(.5,.7),xytext=(.5,.1),arrowprops=dict(arrowstyle="<->",mutation_scale=12,lw=2,color=purple))
 ax.text(.56,.78,"B = 0.6",color=purple,fontsize=24)
 ax.set(xlabel="Path position α",ylabel="Loss",xlim=(0,1),ylim=(0,.82),xticks=[0,.5,1],yticks=[.1,.4,.7])
 title="Barrier is measured\nabove the endpoint maximum"
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.23),frameon=False,fontsize=24)
 footer="Analytic profile with the\nexercise endpoints and peak."
elif name=="zero-barrier-nonconstant":
 fig,ax=single();L=.5-.4*np.sin(np.pi*a)**2
 ax.plot(a,L,color=blue,lw=3);ax.axhline(.5,color=orange,ls="--",lw=2)
 ax.scatter([0,1],[.5,.5],color=orange,marker="s",s=65,zorder=5)
 ax.set(xlabel="Path position α",ylabel="Loss",xlim=(0,1),ylim=(0,.65),xticks=[0,.5,1],yticks=[.1,.3,.5])
 title="Zero barrier\nneed not mean constant loss"
 footer="Path max = endpoint max\nB = 0; the middle loss is lower."
elif name=="grid-misses-peak":
 fig,ax=single();L=.1+.6*np.exp(-((a-.25)/.055)**2)
 ax.plot(a,L,color=purple,lw=3,label="Continuous example")
 for grid,c,m,lab in [(np.array([0,.5,1]),blue,"o","Coarse grid"),(np.array([0,.25,.5,.75,1]),green,"s","Nested finer grid")]:
  vals=.1+.6*np.exp(-((grid-.25)/.055)**2)
  if m=="o":ax.scatter(grid,vals,facecolors="none",edgecolors=c,linewidths=2,marker=m,s=160,zorder=5,label=lab)
  else:ax.scatter(grid,vals,color=c,marker=m,s=45,zorder=4,label=lab)
 ax.set(xlabel="Path position α",ylabel="Loss",xlim=(-.04,1.04),ylim=(0,.82),xticks=[0,.25,.5,1],yticks=[.1,.4,.7])
 title="A sparse grid\ncan miss a narrow barrier"
 fig.legend(*ax.get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.22),frameon=False,fontsize=23)
 footer="Retaining old grid points cannot\nlower the observed maximum."
elif name=="straight-and-curved-paths":
 fig,axs=pair()
 x=np.linspace(-1.35,1.35,180);y=np.linspace(-.35,1.35,150);X,Y=np.meshgrid(x,y)
 axs[0].contour(X,Y,(X*X+Y*Y-1)**2,levels=[.1,.4,1],colors="#CBD5E1",linewidths=1)
 axs[0].plot(1-2*a,np.zeros_like(a),color=blue,lw=3,label="Straight")
 axs[0].plot(np.cos(np.pi*a),np.sin(np.pi*a),color=green,lw=3,ls="--",label="Semicircle")
 axs[0].scatter([1,-1],[0,0],color=orange,marker="s",s=90,zorder=5)
 axs[0].annotate("(1, 0)",(1,0),xytext=(.60,-.24),fontsize=24,color=orange)
 axs[0].annotate("(−1, 0)",(-1,0),xytext=(-1.29,-.24),fontsize=24,color=orange)
 axs[0].set(xlabel="Parameter x",ylabel="Parameter y",xlim=(-1.35,1.35),ylim=(-.35,1.35));axs[0].set_aspect("equal");axs[0].set_title("Same endpoints",fontsize=28,pad=25)
 lin=((1-2*a)**2-1)**2
 axs[1].plot(a,lin,color=blue,lw=3);axs[1].plot(a,np.zeros_like(a),color=green,lw=3,ls="--")
 axs[1].set(xlabel="Path position α",ylabel="Loss",xlim=(0,1),ylim=(-.07,1.1),xticks=[0,.5,1]);axs[1].set_title("Different barriers",fontsize=28,pad=25)
 fig.legend(*axs[0].get_legend_handles_labels(),loc="center",bbox_to_anchor=(.5,.23),ncol=2,frameon=False,fontsize=24)
 title="Straight-path failure is not failure of every path"
 footer="L(x, y) = (x² + y² − 1)²; barriers 1 and 0\nA constructed connection is not a recorded optimizer trajectory."
elif name=="permutation-interpolation":
 fig,axs=pair(880)
 X=np.array([-2.,-1.,0.,1.,2.]);wa=np.array([1.,-2.]);ra=np.array([3.,-1.])
 wb=wa[::-1];rb=ra[::-1]
 def net(x,w,r):return np.maximum(x[:,None]*w,0)@r
 target=net(X,wa,ra);loss=[];aligned=[]
 for alpha in a:
  loss.append(np.mean((net(X,(1-alpha)*wa+alpha*wb,(1-alpha)*ra+alpha*rb)-target)**2))
  aligned.append(0.)
 xx=np.linspace(-2,2,201)
 axs[0].plot(xx,net(xx,wa,ra),color=blue,lw=3,label="Endpoints")
 axs[0].plot(xx,net(xx,(wa+wb)/2,(ra+rb)/2),color=purple,lw=3,ls="--",label="Unaligned midpoint")
 axs[0].set(xlabel="Input x",ylabel="Output f(x)",xticks=[-2,0,2]);axs[0].set_title("Same endpoint function",fontsize=27,pad=24)
 axs[1].plot(a,loss,color=purple,lw=3,label="Unaligned path");axs[1].plot(a,aligned,color=green,lw=3,ls="--",label="Aligned path")
 axs[1].set(xlabel="Interpolation α",ylabel="MSE to endpoint function",xticks=[0,.5,1]);axs[1].set_title("Pair unit roles first",fontsize=27,pad=24)
 for ax in axs:ax.legend(loc="upper center",bbox_to_anchor=(.5,-.28),frameon=False,fontsize=22)
 title="Permuting hidden units changes a naive straight interpolation"
 footer="Two ReLU units: w = (1, −2), readout = (3, −1)\nPermute both lists; match both back before interpolation."
elif name=="slice-axis-rescaling":
 fig,axs=pair(850);grid=np.linspace(-1.4,1.4,180);A,B=np.meshgrid(grid,grid)
 for ax,scale in zip(axs,[1,2]):
  Z=((scale*A)**2+B**2-1)**2
  ax.contour(A,B,Z,levels=[.1,.4,1],colors=["#2563EB","#7C3AED","#D97706"],linewidths=2)
  phi=np.linspace(0,2*np.pi,300);ax.plot(np.cos(phi)/scale,np.sin(phi),color=green,lw=3)
  ax.set(xlabel="Slice coordinate a",ylabel="Slice coordinate b",xlim=(-1.4,1.4),ylim=(-1.4,1.4),xticks=[-1,0,1],yticks=[-1,0,1]);ax.set_aspect("equal")
  ax.set_title("x = "+str(scale)+"a; y = b",fontsize=28,pad=24)
 title="Changing direction scale changes the plotted width"
 footer="Same L(x, y) = (x² + y² − 1)²\nGreen: L = 0; other contours: 0.1, 0.4, 1\nA coordinate a now represents twice the x displacement."
else:raise ValueError(name)
fig.suptitle(title,fontsize=28,y=.94,linespacing=1.35)
fig.text(.5,.08,footer,ha="center",fontsize=24,color="#475569",linespacing=1.5)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
