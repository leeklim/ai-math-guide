"""Reproduce illustrative nonlinear receiver context for a fixed edge change."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-09-path","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":24,"xtick.labelsize":22,"ytick.labelsize":22,"axes.spines.top":False,"axes.spines.right":False})
def main(output):
    fig=plt.figure(figsize=(520/72,1320/72),facecolor="#F8FAFC");m=np.linspace(-1,2,200)
    for y,d,col in zip([.70,.43,.16],[-2,0,2],["#2563EB","#7C3AED","#059669"]):
        ax=fig.add_axes((.20,y,.71,.17),facecolor="#F8FAFC");ax.plot(m,np.maximum(0,m+d),color=col,lw=2.6);ax.scatter([0,1],np.maximum(0,np.array([0,1])+d),color="#D97706",s=65,zorder=5);ax.set(xlim=(-1,2),ylim=(-.15,4.4),xlabel="Edge message m",ylabel="Outcome Y");ax.set_xticks([0,1]);ax.set_yticks([0,2,4]);ax.grid(color="#CBD5E1",alpha=.7);effect=max(0,1+d)-max(0,d);fig.text(.077,y+.17+.035,f"Other path d = {d}; effect {effect}",fontsize=26,color=col)
    fig.text(.077,.965,"Same edge change; different base",fontsize=26,color="#0F172A");fig.text(.077,.94,"Illustrative Y = ReLU(m + d)",fontsize=26,color="#64748B");fig.text(.077,.05,"In each panel: m changes 0 → 1",fontsize=27,color="#D97706")
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
