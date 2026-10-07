"""Reproduce lightweight ablation arithmetic; no model run."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
B,P,G,O="#2563EB","#7C3AED","#059669","#D97706"
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-06-ablation","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    n=output.name;fig=plt.figure(figsize=(520/72,1000/72),facecolor="#F8FAFC")
    axes=[fig.add_axes((.20,.58,.71,.22),facecolor="#F8FAFC"),fig.add_axes((.20,.17,.71,.22),facecolor="#F8FAFC")]
    if "layernorm-propagation" in n:
        raw=np.array([[2.,0.,-1.],[1.,0.,-1.]]);z=(raw-raw.mean(axis=1,keepdims=True))/raw.std(axis=1,keepdims=True)
        for ax,vals,title in zip(axes,[raw,z],["Before LayerNorm","After LayerNorm"]):
            for i,(v,col) in enumerate(zip(vals,[B,G])):ax.bar(np.arange(3)+(i-.5)*.30,v,width=.30,color=col,label="Intact" if i==0 else "Update zero")
            ax.set_xticks([0,1,2],["1","2","3"]);ax.set(ylim=(-1.8,2.7),ylabel="Coordinate value");ax.axhline(0,color="#64748B");ax.grid(axis="y",color="#CBD5E1",alpha=.7);fig.text(.077,ax.get_position().y1+.035,title,fontsize=28,color="#0F172A")
        axes[0].legend(loc="lower left",bbox_to_anchor=(-.17,1.26),fontsize=24,frameon=False,ncol=2)
        fig.text(.077,.975,"One changed raw coordinate",fontsize=27,color="#0F172A");fig.text(.077,.055,"Illustrative ε = 0; no affine terms",fontsize=25,color="#64748B")
    elif "margin-versus-decision" in n:
        for ax,vals,title,yl in zip(axes,[[2,.2,-.1],[1,1,0]],["Logit margin","Positive-margin decision"],["Margin","Decision"]):
            ax.bar([0,1,2],vals,color=[B,P,G]);ax.set_xticks([0,1,2],["Intact","A","B"]);ax.axhline(0,color="#64748B");ax.set(ylim=(-.5,2.7) if yl=="Margin" else (0,1.3),ylabel=yl);ax.grid(axis="y",color="#CBD5E1",alpha=.7);fig.text(.077,ax.get_position().y1+.035,title,fontsize=27,color="#0F172A")
        fig.text(.077,.95,"Score and choice differ",fontsize=28,color="#0F172A");fig.text(.077,.055,"Illustrative threshold: margin > 0",fontsize=25,color="#64748B")
    else:
        sample=np.array([[1,1,1],[1,.8,-1],[.7,1,.5]]);means=sample.mean(axis=0)*[1,1,.2];joint=float(means[:2].sum())
        axes[0].bar([0,1,2],means,color=[B,P,G]);axes[0].set_xticks([0,1,2],["h₁","h₂","h₃"]);axes[0].set(ylim=(0,1.2),ylabel="Mean single effect");axes[0].set_yticks([0,.5,1])
        for i,v in enumerate(means):axes[0].text(i,v+.08,f"{v:.4f}",ha="center",fontsize=22,color="#0F172A")
        axes[1].bar([0,1],[joint,joint],color=[P,G]);axes[1].set_xticks([0,1],["Sum 1+2","Joint 1+2"]);axes[1].set(ylim=(0,2.3),ylabel="Mean effect");axes[1].set_yticks([0,1,2])
        fig.text(.077,.95,"Additivity in this linear lab",fontsize=27,color="#0F172A");fig.text(.077,.86,"Y = h₁ + h₂ + 0.2h₃",fontsize=28,color="#0F172A");fig.text(.077,.055,"0.9 + 0.9333 = 1.8333",fontsize=28,color=G)
        for ax in axes:ax.grid(axis="y",color="#CBD5E1",alpha=.7)
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
