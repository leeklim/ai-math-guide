"""Reproduce IG geometry and numerical views from I07-03."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
B,P,G,O="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-03-integral","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    n=output.name
    two="average-gradient-area" in n or "baseline-attributions" in n
    fig=plt.figure(figsize=(520/72,(1000 if two else 860)/72),facecolor="#F8FAFC")
    if two:
        axes=[fig.add_axes((.20,.58,.71,.22),facecolor="#F8FAFC"),fig.add_axes((.20,.17,.71,.22),facecolor="#F8FAFC")]
        if "average-gradient-area" in n:
            a=np.linspace(0,1,200)
            for ax,k,col,title in zip(axes,[3,2],[B,P],["g₁ = 3α; area 1.5","g₂ = g₃ = 2α; area 1"]):
                ax.plot(a,k*a,color=col,lw=2.6);ax.fill_between(a,0,k*a,color=col,alpha=.16);ax.scatter([1],[k],color=O,s=60,zorder=5);ax.set(xlim=(0,1),ylim=(0,3.4),xlabel="Path fraction α",ylabel="Gradient");ax.set_xticks([0,.5,1]);ax.set_yticks([0,1,2,3]);ax.grid(color="#CBD5E1",alpha=.7)
                fig.text(.077,ax.get_position().y1+.035,title,fontsize=27,color=col)
            fig.text(.077,.95,"Average the path gradients",fontsize=28,color="#0F172A")
            fig.text(.077,.055,"Mean g = (1.5, 1, 1)",fontsize=28,color=G)
        else:
            for ax,vals,title in zip(axes,[[3,3,1],[2,3,0]],["Zero baseline: score gap 7","One baseline: score gap 5"]):
                ax.bar([0,1,2],vals,color=[B,P,G]);ax.set_xticks([0,1,2],["x₁","x₂","x₃"]);ax.set(ylim=(0,3.6),ylabel="IG attribution");ax.set_yticks([0,1,2,3]);ax.grid(axis="y",color="#CBD5E1",alpha=.7)
                fig.text(.077,ax.get_position().y1+.035,title,fontsize=26,color="#0F172A")
            fig.text(.077,.95,"Same input, different baseline",fontsize=26,color="#0F172A")
            fig.text(.077,.055,"One baseline: Δx₃ = 0 ⇒ IG₃ = 0",fontsize=26,color=G)
    elif "average-times-displacement" in n:
        ax=fig.add_axes((.20,.52,.71,.27),facecolor="#F8FAFC");ax.bar([0,1,2],[3,3,1],color=[B,P,G]);ax.set_xticks([0,1,2],["x₁","x₂","x₃"]);ax.set(ylim=(0,3.6),ylabel="IG attribution");ax.set_yticks([0,1,2,3]);ax.grid(axis="y",color="#CBD5E1",alpha=.7)
        bx=fig.add_axes((.20,.28,.71,.10),facecolor="#F8FAFC")
        for left,val,col in zip([0,3,6],[3,3,1],[B,P,G]):bx.barh(0,val,left=left,color=col,height=.7)
        bx.set(xlim=(0,7),ylim=(-.5,.5));bx.set_yticks([]);bx.set_xticks([0,3,6,7]);bx.set_xlabel("Total score difference")
        fig.text(.077,.95,"Coordinate products form IG",fontsize=26,color="#0F172A")
        fig.text(.077,.87,"(1.5 × 2, 1 × 3, 1 × 1)",fontsize=27,color=P)
        fig.text(.077,.15,"IG = (3, 3, 1)",fontsize=28,color=G)
        fig.text(.077,.075,"3 + 3 + 1 = 7 − 0",fontsize=28,color=G)
    else:
        ax=fig.add_axes((.20,.30,.71,.46),facecolor="#F8FAFC")
        if "joint-input-path" in n:
            a=np.linspace(0,1,100);ax.plot(2*a,3*a,color=P,lw=2.6);ax.scatter([0,1,2],[0,1.5,3],color=[O,P,B],s=65,zorder=5)
            for x,y,label in [(0,0,"α = 0"),(1,1.5,"α = 1/2"),(2,3,"α = 1")]:ax.annotate(label,(x,y),xytext=(8,18),textcoords="offset points",fontsize=24,color="#0F172A")
            ax.set(xlim=(-.1,2.6),ylim=(-.1,3.6),xlabel="Coordinate x₁",ylabel="Coordinate x₂");ax.set_xticks([0,1,2]);ax.set_yticks([0,1.5,3]);ax.grid(color="#CBD5E1",alpha=.7)
            fig.text(.077,.95,"All coordinates move together",fontsize=26,color="#0F172A")
            fig.text(.077,.17,"γ(α) = (2α, 3α, α)",fontsize=28,color=P)
            fig.text(.077,.095,"Shown: x₁–x₂ projection",fontsize=27,color="#0F172A")
            fig.text(.077,.035,"Third coordinate: x₃ = α",fontsize=27,color="#0F172A")
        else:
            a=np.linspace(0,1,300);ax.plot(a,2*a,color=G,lw=2.6);edges=np.arange(4)/4;heights=2*(edges+.25);ax.bar(edges,heights,width=.25,align="edge",color=B,alpha=.2,edgecolor=B,lw=2);ax.scatter(edges+.25,heights,color=P,s=45,zorder=5)
            ax.set(xlim=(0,1),ylim=(0,2.5),xlabel="Path fraction α",ylabel="Gradient g₃");ax.set_xticks([0,.25,.5,.75,1]);ax.set_yticks([0,1,2]);ax.grid(color="#CBD5E1",alpha=.7)
            fig.text(.077,.95,"Right endpoint rectangles",fontsize=28,color="#0F172A")
            fig.text(.077,.87,"Illustrative m = 4",fontsize=26,color=B)
            fig.text(.077,.17,"Width 1/4 × height sum 5",fontsize=26,color=B)
            fig.text(.077,.095,"Approximate area = 1.25",fontsize=27,color=B)
            fig.text(.077,.035,"Exact area = 1",fontsize=27,color=G)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
