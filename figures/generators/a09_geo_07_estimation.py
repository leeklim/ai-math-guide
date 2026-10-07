"""Reproduce finite-sample, scale, noise, and projection pitfalls with toy data."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

BLUE, PURPLE, GREEN, ORANGE = "#2563EB", "#7C3AED", "#059669", "#D97706"
BG, GRID, GRAY = "#F8FAFC", "#D9E2EF", "#64748B"


def plane(ax, lim, ylim, xticks=None, yticks=None):
    ax.set_xlim(*lim); ax.set_ylim(*ylim); ax.set_aspect("equal")
    if xticks is not None: ax.set_xticks(xticks)
    if yticks is not None: ax.set_yticks(yticks)
    ax.grid(color=GRID); ax.axhline(0,color=GRAY,lw=1); ax.axvline(0,color=GRAY,lw=1)


def arrow(ax, start, delta, color):
    ax.annotate("",xy=np.array(start)+np.array(delta),xytext=start,
                arrowprops={"arrowstyle":"->","color":color,"lw":2.7,"mutation_scale":13,
                            "shrinkA":0,"shrinkB":0},zorder=5)


def covariance(points):
    centered=points-points.mean(axis=0)
    return centered,np.linalg.eigh(centered.T@centered/(len(points)-1))


def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args(); name=args.output.stem.removeprefix("A09-GEO-07-")
    plt.rcParams.update({"font.size":26,"font.family":"DejaVu Sans","svg.fonttype":"none",
                         "svg.hashsalt":"a09-geo-07","axes.spines.top":False,"axes.spines.right":False})
    normal=name in {"semicircle-covariance","noise-eigenvalues","branch-neighbors"}
    if normal:
        fig,ax=plt.subplots(figsize=(7.2,9)); axes=[ax]
        fig.subplots_adjust(left=.24,right=.94,bottom=.31,top=.79)
    elif name=="scale-signal-noise":
        fig,axes=plt.subplots(1,3,figsize=(16,9)); fig.subplots_adjust(left=.125,right=.965,bottom=.34,top=.74,wspace=.56)
    elif name=="k-versus-radius":
        fig,axes=plt.subplots(2,2,figsize=(13.5,11)); fig.subplots_adjust(left=.095,right=.96,bottom=.29,top=.86,wspace=.38,hspace=1.20)
    elif name=="projection-neighbor-flip":
        fig=plt.figure(figsize=(13.5,9)); axes=[fig.add_subplot(121,projection="3d"),fig.add_subplot(122)]
        fig.subplots_adjust(left=.07,right=.95,bottom=.32,top=.74,wspace=.34)
    else:
        fig,axes=plt.subplots(1,2,figsize=(13.5,9)); fig.subplots_adjust(left=.09,right=.96,bottom=.33,top=.75,wspace=.40)
    if name=="finite-samples-not-manifold":
        samples=np.array([[-1,0],[0,1],[1,0]]); a=np.linspace(0,2*np.pi,200)
        for ax in axes:
            plane(ax,(-1.5,1.5),(-1.5,1.5),[-1,0,1],[-1,0,1])
            ax.scatter(samples[:,0],samples[:,1],color=BLUE,s=65,zorder=5)
            ax.set_xlabel("ambient x",fontsize=24);ax.set_ylabel("ambient y",fontsize=24)
        axes[0].plot(np.cos(a),np.sin(a),"--",color=GRAY,lw=2)
        axes[1].add_patch(plt.Rectangle((-1.5,-1.5),3,3,color=GRAY,alpha=.05))
        axes[0].set_title("Candidate M=S¹\nLocal manifold dimension 1",fontsize=23,pad=25)
        axes[1].set_title("Candidate M=R²\nLocal manifold dimension 2",fontsize=23,pad=25)
        fig.text(.5,.085,"The same three observed points lie in both candidates.\nFinite samples alone do not identify a unique smooth manifold.",ha="center",fontsize=24)
    elif name=="pca-centering":
        theta=np.linspace(-.25,.25,17);points=np.column_stack([np.cos(theta),np.sin(theta)])
        centered,(values,vectors)=covariance(points)
        ax,bx=axes;plane(ax,(.78,1.28),(-.31,.31),[.8,1,1.2],[-.2,0,.2])
        plane(bx,(-.31,.31),(-.31,.31),[-.2,0,.2],[-.2,0,.2])
        ax.scatter(points[:,0],points[:,1],color=BLUE,s=40,zorder=4)
        ax.scatter(*points.mean(axis=0),color=ORANGE,s=65,zorder=6)
        bx.scatter(centered[:,0],centered[:,1],color=BLUE,s=40,zorder=4)
        arrow(bx,(0,0),(0,.25),GREEN);arrow(bx,(0,0),(.25,0),PURPLE)
        ax.set_title("Observed neighborhood\nOrange: sample mean μ",fontsize=23,pad=25)
        bx.set_title("Centering: xᵢ−μ\nVertical variance dominates",fontsize=23,pad=25)
        ax.set_xlabel("ambient x",fontsize=24);ax.set_ylabel("ambient y",fontsize=24)
        bx.set_xlabel("centered x",fontsize=24);bx.set_ylabel("centered y",fontsize=24)
        fig.text(.5,.085,f"Sample eigenvalues: λ₁={values[1]:.4f}, λ₂={values[0]:.5f}.\nUnit eigenvectors give directions, not manifold proof.\nArrow display scale 1/4.",ha="center",fontsize=23)
    elif name=="k-versus-radius":
        dense=np.array([-.65,-.4,-.15,-.08,.08,.15,.4,.65])
        sparse=np.array([-.9,-.75,-.6,-.3,.3,.6,.75,.9])
        for row in range(2):
            for col,points in enumerate([dense,sparse]):
                ax=axes[row,col];plane(ax,(-1,1),(-.72,.72),[-1,0,1],[0])
                radius=.15 if col==0 else .6
                radius=radius if row==0 else .2
                selected=np.abs(points)<=radius+1e-10
                ax.scatter(points,np.zeros(len(points)),color=GRAY,s=40,zorder=3)
                ax.scatter(points[selected],np.zeros(selected.sum()),color=BLUE,s=60,zorder=4)
                ax.scatter([0],[0],color=ORANGE,s=60,zorder=5)
                ax.add_patch(Circle((0,0),radius,fill=False,color=PURPLE,lw=2,linestyle="--"))
                title=(f"k=4: radius {radius:.2f}" if row==0 else f"radius 0.20: {selected.sum()} neighbors")
                ax.set_title(("Dense region\n" if col==0 else "Sparse region\n")+title,fontsize=23,pad=20)
                ax.set_xlabel("same Euclidean x",fontsize=23)
        fig.text(.5,.06,"The orange anchor is excluded from the neighbor count.\nFixed k changes radius; fixed radius changes the sample count.",ha="center",fontsize=24)
    elif name=="scale-signal-noise":
        for i,(ax,width) in enumerate(zip(axes,[.03,.25,1.2])):
            rng=np.random.default_rng(43+i);theta=np.linspace(-width,width,31)
            true=np.column_stack([np.cos(theta),np.sin(theta)])
            points=true+rng.normal(0,.015,true.shape)
            centered,(values,vectors)=covariance(points);mean=points.mean(axis=0)
            bound=1.25*max(.065,width*.9,2*np.sqrt(values[1])+abs(mean[1]))+.01
            plane(ax,(mean[0]-bound,mean[0]+bound),(-bound,bound))
            ax.plot(true[:,0],true[:,1],color=GRAY,lw=2)
            ax.scatter(points[:,0],points[:,1],color=BLUE,s=22,zorder=4)
            for j,color in [(1,GREEN),(0,PURPLE)]:
                vector=2*np.sqrt(values[j])*vectors[:,j]
                ax.plot([mean[0]-vector[0],mean[0]+vector[0]],[mean[1]-vector[1],mean[1]+vector[1]],color=color,lw=3)
            ax.set_xticks([round(mean[0],2)]);ax.set_yticks([-round(bound,2),0,round(bound,2)])
            ax.set_xlabel("ambient x",fontsize=22);ax.set_ylabel("ambient y",fontsize=22)
            ax.set_title(["Very small\nNoise-sensitive","Intermediate\nTangent-dominated","Large\nDirections mix"][i]+f"\nhalf-width {width}",fontsize=22,pad=25)
            ax.text(.5,-.32,f"λmin/λmax={values[0]/values[1]:.3f}",transform=ax.transAxes,ha="center",fontsize=22)
        fig.text(.5,.075,"Synthetic unit circle: 31 samples per panel; noise σ=0.015; seeds 43–45.\nVariance axes have half-length 2√λ. Axis ranges differ between panels.",ha="center",fontsize=23)
    elif name=="semicircle-covariance":
        points=np.array([[-1,0],[0,1],[1,0]]);centered,_=covariance(points)
        ax=axes[0];plane(ax,(-1.45,1.6),(-.75,1.45),[-1,0,1],[0,1])
        a=np.linspace(0,np.pi,150);ax.plot(np.cos(a),np.sin(a)-1/3,"--",color=GRAY,lw=2)
        ax.scatter(centered[:,0],centered[:,1],color=BLUE,s=60,zorder=6)
        arrow(ax,(0,0),(1,0),GREEN);arrow(ax,(0,0),(0,1),PURPLE)
        ax.set_xlabel("centered x",fontsize=25);ax.set_ylabel("centered y",fontsize=25)
        ax.set_title("Centered semicircle samples\nOne curve; two PCA directions",fontsize=24,pad=25)
        fig.text(.5,.08,"Original mean μ=(0,1/3)\nSample covariance: diag(1,1/3)\nPCA rank: 2. Curve dimension: 1.",ha="center",fontsize=25)
    elif name=="noise-eigenvalues":
        fig.subplots_adjust(bottom=.39)
        ax=axes[0];index=np.arange(3);a=np.array([1,.1,0]);b=a+.04
        ax.bar(index-.18,a,width=.32,color=BLUE,label="signal")
        ax.bar(index+.18,b,width=.32,color=PURPLE,label="signal + noise")
        for i in range(3):
            ax.text(i-.18,a[i]+.05,f"{a[i]:g}",ha="center",fontsize=25,color=BLUE)
            ax.text(i+.18,b[i]+.18,f"{b[i]:g}",ha="center",fontsize=25,color=PURPLE)
        ax.set_xticks(index,["axis 1","axis 2","axis 3"]);ax.set_ylim(0,1.55);ax.set_yticks([0,.5,1])
        ax.set_ylabel("population eigenvalue",fontsize=25);ax.grid(axis="y",color=GRID)
        ax.set_title("Isotropic noise, independent\nEach axis gains σ²=0.04",fontsize=24,pad=25)
        fig.legend(loc="center",bbox_to_anchor=(.5,.285),fontsize=22,frameon=False,ncols=2)
        fig.text(.5,.08,"Signal covariance: diag(1,0.1,0)\nWith noise: diag(1.04,0.14,0.04)\nExtra variance is not a new signal.",ha="center",fontsize=25)
    elif name=="projection-neighbor-flip":
        ax,bx=axes;ax.computed_zorder=False
        ax.plot([0,0],[0,0],[0,2],color=PURPLE,lw=3);ax.plot([0,1],[0,0],[0,0],color=BLUE,lw=3)
        for p,color in [((0,0,0),GREEN),((0,0,2),PURPLE),((1,0,0),BLUE)]:ax.scatter(*p,color=color,s=50,zorder=5)
        ax.text(0,0,2.5,"B",fontsize=25,color=PURPLE);ax.text(1.45,0,-.25,"C",fontsize=25,color=BLUE);ax.text(-.55,0,-.4,"A",fontsize=25,color=GREEN)
        ax.set_xlim(-.5,1.7);ax.set_ylim(-.7,.7);ax.set_zlim(-.2,2.6)
        ax.set_xticks([0,1]);ax.set_yticks([0]);ax.set_zticks([0,1,2]);ax.tick_params(labelsize=23)
        ax.set_xlabel("x",fontsize=24,labelpad=10);ax.set_ylabel("y",fontsize=24,labelpad=10);ax.set_zlabel("z",fontsize=24,labelpad=10)
        ax.view_init(elev=20,azim=-60);ax.set_title("Original R³\nAB=2; AC=1",fontsize=24,pad=30)
        for axis in (ax.xaxis,ax.yaxis,ax.zaxis):axis.pane.set_facecolor(BG);axis._axinfo["grid"]["color"]=GRID
        plane(bx,(-.4,1.6),(-.7,.7),[0,1],[0]);bx.plot([0,1],[0,0],color=BLUE,lw=3)
        bx.scatter([0],[0],color=GREEN,s=60,zorder=5);bx.scatter([0],[0],facecolors="none",edgecolors=PURPLE,s=220,lw=3,zorder=6)
        bx.scatter([1],[0],color=BLUE,s=60,zorder=5);bx.text(-.2,.35,"A=B",fontsize=25);bx.text(.9,.35,"C",fontsize=25)
        bx.set_xlabel("projected x",fontsize=24);bx.set_ylabel("projected y",fontsize=24)
        bx.set_title("Projection drops z\nAB=0; AC=1",fontsize=24,pad=25)
        fig.text(.5,.085,"Original nearest point to A: C. Plotted nearest point: B.\nProjection deletes a direction and can change neighborhoods.",ha="center",fontsize=24)
    elif name=="branch-neighbors":
        ax=axes[0];plane(ax,(-.55,1.45),(-.75,.75),[0,1],[0])
        x=np.linspace(-.55,1,150);a=np.linspace(0,np.pi,100)
        ax.plot(x,np.full_like(x,.12),color=BLUE,lw=3);ax.plot(1+.12*np.sin(a),.12*np.cos(a),color=GRAY,lw=2)
        ax.plot(x,np.full_like(x,-.12),color=PURPLE,lw=3)
        ax.scatter([0,0,.3],[.12,-.12,.12],color=[ORANGE,PURPLE,BLUE],s=55,zorder=6)
        ax.plot([0,0],[.12,-.12],":",color=GRAY,lw=2)
        ax.add_patch(Circle((0,.12),.25,fill=False,color=ORANGE,lw=2,linestyle="--"))
        ax.text(-.35,.5,"radius 0.25",fontsize=25,color=ORANGE)
        ax.set_xlabel("ambient x",fontsize=25);ax.set_ylabel("ambient y",fontsize=25)
        ax.set_title("Nearby in ambient distance\nFar along the hairpin curve",fontsize=25,pad=25)
        fig.text(.5,.08,"Across branches: Euclidean 0.24\nAlong the curve: 2+0.12π≈2.38\nSame-branch point: distance 0.30.",ha="center",fontsize=25)
    elif name=="label-shuffle":
        points=np.array([[-1,-.15],[-.9,.1],[-.8,-.05],[.8,.05],[.9,-.1],[1,.15]])
        for ax,labels,title in zip(axes,[np.array([0,0,0,1,1,1]),np.array([0,1,1,0,1,0])],["Original condition labels","Shuffled condition labels"]):
            plane(ax,(-1.3,1.3),(-.7,.7),[-1,0,1],[0])
            for label,color,marker in [(0,BLUE,"o"),(1,PURPLE,"s")]:
                selected=labels==label;ax.scatter(points[selected,0],points[selected,1],color=color,marker=marker,s=65,label="A" if label==0 else "B")
            ax.set_title(title+"\nThe coordinates do not move",fontsize=23,pad=25)
            ax.set_xlabel("same ambient x",fontsize=24);ax.set_ylabel("same ambient y",fontsize=24)
            ax.legend(loc="upper center",fontsize=23,frameon=False,ncols=2)
        fig.text(.5,.085,"Label-free neighborhoods and covariance stay the same.\nShuffle tests association with conditions, not intrinsic dimension itself.",ha="center",fontsize=24)
    else:
        raise ValueError(name)
    fig.set_facecolor(BG)
    for ax in fig.axes:ax.set_facecolor(BG)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,metadata={"Date":None});plt.close(fig)


if __name__=="__main__":
    main()
