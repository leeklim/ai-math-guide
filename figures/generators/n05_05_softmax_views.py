"""Reproduce N05-05 numerical logit, probability, loss and gradient figures."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
BLUE,PURPLE,GREEN,ORANGE="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"n05-05-softmax","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def softmax(z):
    e=np.exp(z-np.max(z));return e/e.sum()
def main(output):
    z=np.array([2.,1.,0.]);p=softmax(z)
    tall="logit-probability" in output.name
    fig=plt.figure(figsize=(520/72,(900 if tall else 710)/72),facecolor="#F8FAFC")
    if tall:
        fig.text(.077,.96,"Scores versus probabilities",fontsize=29,color="#0F172A")
        for ypos,values,label,col,ylim in [(.59,z,"Logit z",BLUE,(0,2.6)),(.17,p,"Probability p",GREEN,(0,1))]:
            ax=fig.add_axes((.18,ypos,.73,.27),facecolor="#F8FAFC");ax.grid(axis="y",color="#CBD5E1",alpha=.75);ax.bar([1,2,3],values,color=col,alpha=.22,edgecolor=col,lw=2)
            ax.set(ylim=ylim,xlim=(.4,3.6),xlabel="Class",ylabel=label);ax.set_xticks([1,2,3])
            for k,v in enumerate(values):ax.text(k+1,v+ylim[1]*.05,str(int(v)) if col==BLUE else f"{v:.4f}",ha="center",color=col,fontsize=26)
        fig.text(.077,.065,"Probability mass: sum p = 1",fontsize=27,color=GREEN)
    else:
        ax=fig.add_axes((.18,.26,.73,.49),facecolor="#F8FAFC");ax.grid(color="#CBD5E1",alpha=.75)
        if "target-loss" in output.name:
            x=np.linspace(.02,1,500);ax.plot(x,-np.log(x),color=PURPLE,lw=2.7)
            loss=-np.log(p[0]);ax.scatter([p[0]],[loss],color=GREEN,s=70,zorder=5)
            ax.plot([p[0],p[0]],[0,loss],color=GREEN,ls=":",lw=2)
            ax.set(xlim=(0,1),ylim=(0,4),xlabel="Target probability p",ylabel="Loss −log p")
            ax.set_xticks([0,.5,1]);ax.set_yticks([0,1,2,3,4])
            fig.text(.077,.95,"Target probability to loss",fontsize=29,color="#0F172A")
            fig.text(.077,.13,f"p = {p[0]:.4f}",fontsize=28,color=GREEN)
            fig.text(.077,.075,f"L = {loss:.4f}",fontsize=28,color=PURPLE)
        elif "logit-gradient" in output.name:
            grad=p-np.array([1,0,0])
            ax.axhline(0,color="#64748B",lw=1.2)
            ax.bar([1,2,3],grad,color=[BLUE,GREEN,GREEN],alpha=.24,edgecolor=[BLUE,GREEN,GREEN],lw=2)
            for k,v in enumerate(grad):ax.text(k+1,v+(.035 if v>0 else -.055),f"{v:.4f}",ha="center",color=BLUE if v<0 else GREEN,fontsize=25)
            ax.set(xlim=(.4,3.6),ylim=(-.45,.35),xlabel="Class",ylabel="dL / dz")
            ax.set_xticks([1,2,3]);ax.set_yticks([-.4,-.2,0,.2])
            fig.text(.077,.95,"Logit derivatives: p − target",fontsize=29,color="#0F172A")
            fig.text(.077,.13,"Class 1 is the target.",fontsize=28,color=BLUE)
            fig.text(.077,.075,"Sum of all three derivatives = 0",fontsize=25,color="#0F172A")
        else:
            if "same-argmax" in output.name:
                q=softmax(np.array([1.,.5,0.]))
                labels=["z = (2, 1, 0)","z = (1, 0.5, 0)"];title="Same top class, different loss"
                footer=[f"Target 1: L = {-np.log(p[0]):.4f}",f"Target 1: L = {-np.log(q[0]):.4f}"]
            else:
                q=softmax(p);labels=["softmax(z)","softmax(softmax(z))"];title="A second softmax changes p"
                footer=["Input is already a probability.", "This example becomes flatter."]
            pos=np.arange(1,4);ax.bar(pos-.18,p,width=.32,color=BLUE,alpha=.22,edgecolor=BLUE,lw=2,label=labels[0]);ax.bar(pos+.18,q,width=.32,color=PURPLE,alpha=.22,edgecolor=PURPLE,lw=2,hatch="//",label=labels[1])
            ax.set(xlim=(.4,3.6),ylim=(0,.8),xlabel="Class",ylabel="Probability");ax.set_xticks([1,2,3]);ax.set_yticks([0,.4,.8])
            ax.legend(loc="lower left",bbox_to_anchor=(-.16,1.01),frameon=False,fontsize=23)
            fig.text(.077,.95,title,fontsize=28,color="#0F172A")
            fig.text(.077,.13,footer[0],fontsize=26 if "same-argmax" in output.name else 24,color=BLUE)
            fig.text(.077,.075,footer[1],fontsize=26 if "same-argmax" in output.name else 23,color=PURPLE)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
