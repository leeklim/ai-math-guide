"""Gauge examples drawn from the formulas in A09-SYM-05."""
from argparse import ArgumentParser
from pathlib import Path
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
p=ArgumentParser();p.add_argument("--output",type=Path,required=True);out=p.parse_args().output;name=out.stem.removeprefix("A09-SYM-05-")
mpl.rcParams.update({"font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"svg.fonttype":"none","svg.hashsalt":"sym05-"+name})
bg="#F8FAFC";blue="#2563EB";purple="#7C3AED";green="#059669";orange="#D97706";red="#DC2626"
def style(ax):
 ax.set_facecolor(bg);ax.grid(color="#CBD5E1",alpha=.6);ax.set_axisbelow(True);ax.spines[["top","right"]].set_visible(False)
def arrow(ax,start,end,color):
 ax.annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":"-|>,head_length=.25,head_width=.14","mutation_scale":15,"lw":3,"color":color})
wide=name=="curved-orbit-hessian";tall=name in ["rotated-readout","basis-geometry-change"]
if wide:
 fig,axs=plt.subplots(1,2,figsize=(1100/72,880/72),facecolor=bg);fig.subplots_adjust(left=.09,right=.96,bottom=.34,top=.75,wspace=.36);ax,ax2=axs
elif tall:
 fig,axs=plt.subplots(2,1,figsize=(520/72,1200/72),facecolor=bg);fig.subplots_adjust(left=.21,right=.91,bottom=.22,top=.83,hspace=.52);ax,ax2=axs
else:
 fig,ax=plt.subplots(figsize=(520/72,1010/72),facecolor=bg);fig.subplots_adjust(left=.21,right=.91,bottom=.37,top=.77)
style(ax)
if name=="relu-scale-sign":
 z=np.linspace(-2.2,2.2,301);ax.plot(z,np.maximum(-z,0),color=blue,lw=3,label="ReLU(−z)");ax.plot(z,-np.maximum(z,0),color=purple,lw=3,ls="--",label="−ReLU(z)")
 ax.set(xlim=(-2.4,2.4),ylim=(-2.5,2.5),xticks=[-2,0,2],yticks=[-2,0,2],xlabel="Input z",ylabel="Value");title="Negative scaling does not\ncommute with ReLU";footer="c=−1 violates the identity.\nc=0 has no inverse scaling.\nPositive homogeneity needs c>0."
elif name=="scale-orbit-norm":
 a=np.linspace(.8,8.5,301);ax.plot(a,6/a,color=purple,lw=3,label="Same product ab=6")
 for pt,col in [((2,3),blue),((8,.75),orange)]:ax.plot([0,pt[0]],[0,pt[1]],color=col,lw=2,ls="--");ax.scatter(*pt,color=col,s=100,zorder=5)
 ax.text(2.15,3.65,"(2,3)",color=blue,fontsize=25);ax.text(5.0,1.6,"(8,0.75)",color=orange,fontsize=25)
 ax.set(xlim=(0,9),ylim=(0,8),xticks=[0,4,8],yticks=[0,4,8],xlabel="Parameter a",ylabel="Parameter b");title="Same function,\ndifferent parameter norms";footer="ab=6: both functions are 6x.\nSquared norms: 13 vs 64.5625.\nA norm penalty can change."
elif name=="rotated-readout":
 style(ax2)
 for axis,h,w,label in [(ax,(1,2),(3,1),"Original coordinates"),(ax2,(-2,1),(-1,3),"After Q: 90° rotation")]:
  axis.set_aspect("equal");axis.axhline(0,color="#94A3B8",lw=1);axis.axvline(0,color="#94A3B8",lw=1);arrow(axis,(0,0),h,blue);arrow(axis,(0,0),w,green)
  axis.text(h[0]-.2,h[1]+.5,"h" if axis is ax else "Qh",color=blue,fontsize=28)
  axis.text(w[0]-.5,w[1]+.5,"w" if axis is ax else "Qw",color=green,fontsize=28)
  axis.set(xlim=(-3.4,4),ylim=(-1,4),xticks=[-2,0,2],yticks=[0,2,4]);axis.set_title(label,fontsize=26,pad=22)
 title="Rotate both hidden state\nand scalar-readout weight";footer="h=(1,2)ᵀ ; w=(3,1)ᵀ\nQh=(−2,1)ᵀ ; Qw=(−1,3)ᵀ\nwᵀh=(Qw)ᵀ(Qh)=5."
elif name=="basis-geometry-change":
 style(ax2);t=np.linspace(0,2*np.pi,401)
 for axis,d,label in [(ax,np.diag([1.,1.]),"Original: angle 90°"),(ax2,np.diag([2.,.5]),"After D: angle ≈28.1°")]:
  points=d@np.array([np.cos(t),np.sin(t)]);axis.plot(*points,color="#94A3B8",lw=2,ls="--")
  for v,col in [(np.array([1.,1.]),blue),(np.array([1.,-1.]),purple)]:w=d@v;arrow(axis,(0,0),w,col)
  axis.set_aspect("equal");axis.axhline(0,color="#CBD5E1",lw=1);axis.axvline(0,color="#CBD5E1",lw=1);axis.set(xlim=(-2.6,2.6),ylim=(-1.7,1.7),xticks=[-2,0,2],yticks=[-1,0,1]);axis.set_title(label,fontsize=26,pad=22)
 title="Invertible does not mean\nnorm- and angle-preserving";footer="D=diag(2,0.5)\nCircle → ellipse ; angle changes.\nNorm: √2 → √4.25 for either ray."
elif name=="curved-orbit-hessian":
 style(ax2);a=np.linspace(1,3.6,301);ax.plot(a,6/a,color=purple,lw=3,label="Curved orbit ab=6");s=np.linspace(-.55,.55,301);ax.plot(2+2*s,3-3*s,color=orange,lw=3,ls="--",label="Straight tangent");ax.scatter([2],[3],color=blue,s=100,zorder=5)
 ax.set(xlim=(.8,3.8),ylim=(.9,6.6),xticks=[1,2,3],yticks=[2,4,6],xlabel="Parameter a",ylabel="Parameter b")
 ax2.plot(s,np.full_like(s,6),color=purple,lw=3,label="Along orbit");ax2.plot(s,6-6*s*s,color=orange,lw=3,ls="--",label="Along tangent")
 ax2.set(xlim=(-.6,.6),ylim=(3.8,6.4),xticks=[-.5,0,.5],yticks=[4,5,6],xlabel="Path parameter",ylabel="L(a,b)=ab")
 title="Constant on a curved orbit\nneed not mean a null Hessian tangent"
 footer="θ(t)=(2eᵗ,3e⁻ᵗ): L=6 ; θ₀+s(2,−3): L=6−6s²\nAt (2,3), ∇L=(3,2)≠0.  θ̇ᵀHθ̇=−12 ; ∇Lᵀθ̈=12.\nThe two second-derivative terms cancel; this is not a stationary point."
elif name=="gauge-representative":
 a=np.linspace(.8,8.5,301);ax.plot(a,6/a,color=purple,lw=3)
 ax.axvline(1,color=green,lw=2,ls="--");ax.scatter([1],[6],color=green,s=130,zorder=6)
 for pt,end in [((2,3),(1.12,5.88)),((8,.75),(1.12,6.12))]:ax.scatter(*pt,color=blue,s=90,zorder=5);ax.annotate("",xy=end,xytext=pt,arrowprops={"arrowstyle":"-|>,head_length=.25,head_width=.14","mutation_scale":15,"lw":2,"color":green,"connectionstyle":"arc3,rad=-.22"})
 ax.text(1.45,6.25,"(1,6)",color=green,fontsize=26);ax.text(4,3.3,"a′=1",color=green,fontsize=28)
 ax.set(xlim=(0,9),ylim=(0,8),xticks=[0,4,8],yticks=[0,4,8],xlabel="Parameter a",ylabel="Parameter b")
 title="Gauge fixing selects\na comparison representative";footer="On the positive orbit ab=6:\nc=1/a gives (a′,b′)=(1,6).\nThis rule excludes a=0."
elif name=="whitening-remaining-rotation":
 t=np.linspace(0,2*np.pi,401);ax.plot(np.sqrt(2)*np.cos(t),np.sqrt(2)*np.sin(t),color="#94A3B8",lw=2,ls="--")
 pts=np.array([[np.sqrt(2),0],[-np.sqrt(2),0],[0,np.sqrt(2)],[0,-np.sqrt(2)]]);q=np.array([[1,-1],[1,1]])/np.sqrt(2);rot=pts@q.T
 ax.scatter(*pts.T,color=blue,s=110,label="Original");ax.scatter(*rot.T,color=purple,marker="x",s=150,lw=3,label="Rotated 45°")
 ax.set_aspect("equal");ax.set(xlim=(-1.9,1.9),ylim=(-1.9,1.9),xticks=[-1,0,1],yticks=[-1,0,1],xlabel="Coordinate 1",ylabel="Coordinate 2");title="Identity covariance leaves\northogonal freedom";footer="Both sets have mean 0.\n(1/4)Σ hhᵀ=I ; QIQᵀ=I.\nThe coordinates are not unique."
else:raise ValueError(name)
if wide:
 h,l=ax.get_legend_handles_labels();fig.legend(h,l,loc="center",bbox_to_anchor=(.5,.235),ncol=2,frameon=False,fontsize=24)
elif not tall:
 h,l=ax.get_legend_handles_labels()
 if h:fig.legend(h,l,loc="center",bbox_to_anchor=(.53,.265),ncol=1,frameon=False,fontsize=24)
fig.suptitle(title,fontsize=28,y=.955,linespacing=1.35);fig.text(.5,.045,footer,ha="center",fontsize=24 if not wide else 25,color="#475569",linespacing=1.55)
out.parent.mkdir(parents=True,exist_ok=True);fig.savefig(out,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
