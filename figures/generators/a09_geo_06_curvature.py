"""Reproduce curvature objects, local cylinder isometry, and projection effects."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, PURPLE, GREEN, ORANGE = "#2563EB", "#7C3AED", "#059669", "#D97706"
BG, GRID, GRAY = "#F8FAFC", "#D9E2EF", "#64748B"


def plane(ax, lim=(-1.5, 1.8), ylim=(-1.5, 1.8)):
    ax.set_xlim(*lim); ax.set_ylim(*ylim); ax.set_aspect("equal")
    ax.set_xticks(np.arange(np.ceil(lim[0]), lim[1], 1))
    ax.set_yticks(np.arange(np.ceil(ylim[0]), ylim[1], 1))
    ax.grid(color=GRID); ax.axhline(0, color=GRAY, lw=1); ax.axvline(0, color=GRAY, lw=1)


def arrow(ax, start, delta, color):
    ax.annotate("", xy=np.array(start)+np.array(delta), xytext=start,
                arrowprops={"arrowstyle": "->", "color": color, "lw": 2.8,
                            "mutation_scale": 13, "shrinkA": 0, "shrinkB": 0}, zorder=5)


def ambient(ax):
    ax.computed_zorder = False
    ax.set_xlim(-1.4,1.4); ax.set_ylim(-1.4,1.4); ax.set_zlim(-1.1,1.4)
    ax.set_xticks([-1,0,1]); ax.set_yticks([-1,0,1]); ax.set_zticks([0,1])
    ax.set_xlabel("x", fontsize=23, labelpad=10)
    ax.set_ylabel("y", fontsize=23, labelpad=10)
    ax.set_zlabel("z", fontsize=23, labelpad=10)
    ax.tick_params(labelsize=23); ax.view_init(elev=24, azim=-55)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.set_facecolor(BG); axis._axinfo["grid"]["color"] = GRID
    ax.set_box_aspect((1,1,1))


def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(); name = args.output.stem.removeprefix("A09-GEO-06-")
    plt.rcParams.update({"font.size": 26, "font.family": "DejaVu Sans", "svg.fonttype": "none",
                         "svg.hashsalt": "a09-geo-06", "axes.spines.top": False, "axes.spines.right": False})
    t = np.linspace(0,2*np.pi,160)
    if name == "plane-cylinder-sphere":
        fig = plt.figure(figsize=(16,8.5)); axes = [fig.add_subplot(1,3,i+1,projection="3d") for i in range(3)]
        fig.subplots_adjust(left=.035,right=.95,bottom=.30,top=.75,wspace=.10)
        u,v = np.meshgrid(np.linspace(-1,1,9),np.linspace(-1,1,9))
        axes[0].plot_wireframe(u,v,np.zeros_like(u),color=GRAY,lw=1)
        a,z = np.meshgrid(np.linspace(0,2*np.pi,25),np.linspace(-.7,.7,7))
        axes[1].plot_wireframe(np.cos(a),np.sin(a),z,color=GRAY,lw=1)
        a,b = np.meshgrid(np.linspace(0,2*np.pi,25),np.linspace(-np.pi/2,np.pi/2,13))
        axes[2].plot_wireframe(np.cos(a)*np.cos(b),np.sin(a)*np.cos(b),np.sin(b),color=GRAY,lw=1)
        for ax,title in zip(axes,["Plane\nK_G=0; no ambient bending","Cylinder\nK_G=0; ambient bending","Sphere\nK_G>0; ambient bending"]):
            ambient(ax); ax.set_title(title,fontsize=22,pad=30)
        fig.text(.5,.10,"Ambient bending alone does not determine intrinsic curvature.\nPlane and cylinder are locally flat; the sphere is not.",ha="center",fontsize=24)
    elif name == "unfold-cylinder":
        fig = plt.figure(figsize=(13.5,9)); ax=fig.add_subplot(121); bx=fig.add_subplot(122,projection="3d")
        fig.subplots_adjust(left=.09,right=.93,bottom=.31,top=.75,wspace=.36)
        plane(ax,(-.2,1.6),(-.2,1.6)); ax.set_xticks([0,1]); ax.set_yticks([0,1])
        ax.plot([0,1,1,0,0],[0,0,1,1,0],color=GRAY,lw=2)
        arrow(ax,(0,0),(1,0),BLUE); arrow(ax,(0,0),(0,1),GREEN)
        ax.set_xlabel("arc-length coordinate s",fontsize=22); ax.set_ylabel("height coordinate z",fontsize=22)
        ax.set_title("Flat coordinate patch\nG=I; unit sides, right angle",fontsize=23,pad=25)
        a,z=np.meshgrid(np.linspace(-.5,1.6,17),np.linspace(-.2,1.4,9))
        bx.plot_wireframe(np.cos(a),np.sin(a),z,color=GRID,lw=1)
        s=np.linspace(0,1,100)
        for height in [0,1]: bx.plot(np.cos(s),np.sin(s),np.full_like(s,height),color=BLUE,lw=3)
        for angle in [0,1]: bx.plot([np.cos(angle)]*2,[np.sin(angle)]*2,[0,1],color=GREEN,lw=3)
        ambient(bx); bx.view_init(elev=24,azim=35)
        bx.set_title("Cylinder patch, radius 1\nSame G=I and local lengths",fontsize=23,pad=25)
        fig.text(.5,.09,"Blue side: length 1 in s. Green side: length 1 in z.\nTangent lengths and right angles stay the same.\nThe embedding bends, but G=I remains.",ha="center",fontsize=23)
    elif name == "cylinder-normal-derivative":
        fig,ax=plt.subplots(figsize=(7.2,9)); fig.subplots_adjust(left=.23,right=.94,bottom=.31,top=.79)
        plane(ax,(-1.3,1.8),(-1.3,1.8))
        ax.plot(np.cos(t),np.sin(t),color=GRAY,lw=2)
        arrow(ax,(1,0),(0,1),BLUE); arrow(ax,(1,0),(-1,0),ORANGE)
        ax.scatter([1],[0],color=GREEN,s=45,zorder=6)
        ax.text(.17,1.35,"unit tangent",color=BLUE,fontsize=25)
        ax.text(0,-.25,"normal\nchange",ha="center",va="top",color=ORANGE,fontsize=25)
        ax.set_xlabel("ambient x",fontsize=25); ax.set_ylabel("ambient y",fontsize=25)
        ax.set_title("Cylinder: z=0 cross-section\nF(s,0)=(cos s,sin s,0)",fontsize=25,pad=25)
        fig.text(.5,.08,"At s=0: ∂sF=(0,1,0)\n∂s²F=(−1,0,0) is normal.\nAmbient bending ≠0; K_G=0.",ha="center",fontsize=25)
    elif name == "cylinder-periodicity":
        fig,axes=plt.subplots(1,2,figsize=(13.5,8)); fig.subplots_adjust(left=.09,right=.96,bottom=.35,top=.75,wspace=.40)
        ax,bx=axes; ax.set_xlim(-.5,7); ax.set_ylim(-1,1); ax.set_yticks([])
        ax.set_xticks([0,np.pi,2*np.pi],["0","π","2π"]); ax.spines["left"].set_visible(False)
        ax.plot([0,2*np.pi],[0,0],color=GRAY,lw=2)
        ax.scatter([0],[0],color=BLUE,s=70,zorder=5)
        ax.scatter([2*np.pi],[0],facecolors="none",edgecolors=PURPLE,s=120,lw=3,zorder=5)
        ax.set_title("Different input coordinates\n(s,z)=(0,0) and (2π,0)",fontsize=23,pad=25)
        ax.set_xlabel("unwrapped arc length s",fontsize=24)
        plane(bx,(-1.4,1.8),(-1.4,1.4)); bx.plot(np.cos(t),np.sin(t),color=GRAY,lw=2)
        bx.scatter([1],[0],color=BLUE,s=70,zorder=5)
        bx.scatter([1],[0],facecolors="none",edgecolors=PURPLE,s=200,lw=3,zorder=6)
        bx.set_title("Same cylinder point\nz=0 cross-section",fontsize=23,pad=25)
        bx.set_xlabel("ambient x",fontsize=24); bx.set_ylabel("ambient y",fontsize=24)
        fig.text(.5,.09,"F(0,0)=F(2π,0)=(1,0,0).\nLocal length preservation does not give a global one-to-one chart.",ha="center",fontsize=24)
    elif name == "tangent-two-planes":
        fig=plt.figure(figsize=(13.5,9)); axes=[fig.add_subplot(1,2,i+1,projection="3d") for i in range(2)]
        fig.subplots_adjust(left=.06,right=.92,bottom=.31,top=.75,wspace=.32)
        u,v=np.meshgrid(np.linspace(-1,1,7),np.linspace(-1,1,7))
        axes[0].plot_surface(u,v,np.zeros_like(u),color=BLUE,alpha=.10)
        axes[1].plot_surface(u,np.zeros_like(u),v,color=GREEN,alpha=.10)
        for ax,pair in zip(axes,[(np.array([1,0,0]),np.array([0,1,0])),(np.array([1,0,0]),np.array([0,0,1]))]):
            ambient(ax)
            for vector,color in zip(pair,[BLUE,PURPLE]): ax.quiver(0,0,0,*vector,color=color,lw=2.8,arrow_length_ratio=.13,zorder=8)
            ax.scatter([0],[0],[0],color=GRAY,s=35)
            ax.set_xlabel("v₁",fontsize=24); ax.set_ylabel("v₂",fontsize=24); ax.set_zlabel("v₃",fontsize=24)
        axes[0].set_title("σ₁₂=span(e₁,e₂)\nA two-plane in TₚM",fontsize=24,pad=30)
        axes[1].set_title("σ₁₃=span(e₁,e₃)\nAnother two-plane at the same p",fontsize=24,pad=30)
        fig.text(.5,.09,"Axes are tangent-vector components, not ambient positions.\nK(σ₁₂) and K(σ₁₃) may differ when dim M≥3.",ha="center",fontsize=24)
    elif name == "basis-same-plane":
        fig,ax=plt.subplots(figsize=(7.2,9)); fig.subplots_adjust(left=.23,right=.94,bottom=.31,top=.79)
        plane(ax,(-1.8,1.8),(-.4,2))
        arrow(ax,(0,0),(1,0),BLUE); arrow(ax,(0,0),(0,1),BLUE)
        arrow(ax,(0,0),(1,1),PURPLE); arrow(ax,(0,0),(-1,1),PURPLE)
        ax.text(.4,-.25,"e₁",color=BLUE,fontsize=27); ax.text(.16,1.3,"e₂",color=BLUE,fontsize=27)
        ax.text(.75,1.35,"u",color=PURPLE,fontsize=27); ax.text(-1.2,1.35,"v",color=PURPLE,fontsize=27)
        ax.set_xlabel("tangent component v₁",fontsize=24); ax.set_ylabel("tangent component v₂",fontsize=24)
        ax.set_title("Two bases, the same two-plane\nσ=span(e₁,e₂)=span(u,v)",fontsize=25,pad=25)
        fig.text(.5,.08,"u=e₁+e₂; v=−e₁+e₂\nK(σ) is unchanged by a new basis.\nFor a surface, σ=TₚM.",ha="center",fontsize=25)
    elif name == "path-not-space":
        fig,ax=plt.subplots(figsize=(7.2,9)); fig.subplots_adjust(left=.23,right=.94,bottom=.31,top=.79)
        plane(ax,(-1.5,1.5),(-1.5,1.8)); ax.plot(np.cos(t),np.sin(t),color=PURPLE,lw=3)
        ax.text(-.75,1.38,"curved path",color=PURPLE,fontsize=27)
        ax.set_xlabel("Cartesian x",fontsize=25); ax.set_ylabel("Cartesian y",fontsize=25)
        ax.set_title("A curved path in a flat plane\nThe manifold here is M=R²",fontsize=25,pad=25)
        fig.text(.5,.08,"Plane metric: G=I and K_G=0.\nOne path does not determine\nintrinsic curvature of the plane.",ha="center",fontsize=25)
    elif name == "projection-distortion":
        fig=plt.figure(figsize=(13.5,9)); ax=fig.add_subplot(121,projection="3d"); bx=fig.add_subplot(122)
        fig.subplots_adjust(left=.06,right=.95,bottom=.32,top=.75,wspace=.34)
        c=np.sqrt(15)/4; u,v=np.meshgrid(np.linspace(-1,1,7),np.linspace(-1,1,7))
        ax.plot_wireframe(u,.25*v,c*v,color=GRID,lw=1)
        ax.plot(np.cos(t),.25*np.sin(t),c*np.sin(t),color=BLUE,lw=3)
        ambient(ax); ax.quiver(0,0,0,0,.25,c,color=GREEN,lw=3,arrow_length_ratio=.13,zorder=8)
        ax.set_title("Original tilted flat plane\nUnit circle in its induced metric",fontsize=23,pad=30)
        plane(bx,(-1.4,1.4),(-1.1,1.1)); bx.plot(np.cos(t),.25*np.sin(t),color=PURPLE,lw=3)
        arrow(bx,(0,0),(0,.25),GREEN)
        bx.set_xlabel("projected x",fontsize=24); bx.set_ylabel("projected y",fontsize=24)
        bx.set_title("Orthogonal projection to x,y\nAn ellipse in the plot",fontsize=23,pad=25)
        fig.text(.5,.085,"Original unit direction (0,1/4,√15/4) → plotted (0,1/4).\nEuclidean length changes from 1 to 1/4.\nThe projected picture does not preserve the original metric.",ha="center",fontsize=23)
    else:
        raise ValueError(name)
    fig.set_facecolor(BG)
    for ax in fig.axes: ax.set_facecolor(BG)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.output,metadata={"Date":None}); plt.close(fig)


if __name__ == "__main__":
    main()
