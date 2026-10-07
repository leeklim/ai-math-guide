"""Reproduce exactly the existing I07-08 toy implementation's late-patch map."""
import argparse
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","svg.hashsalt":"i07-08-trace","font.family":"DejaVu Sans","font.size":26,"axes.labelsize":26,"xtick.labelsize":24,"ytick.labelsize":24})
def score(tokens,patch=None):
    s=np.zeros((3,2));s[0]=tokens;s[1]=[s[0,0],.5*s[0,0]+s[0,1]];s[2]=[s[1,0],s[1].sum()]
    if patch is not None:
        layer,token,value=patch;s[layer,token]=value
        if layer<=1:s[2]=[s[1,0],s[1].sum()]
    return float(s[2,1])
def main(output):
    clean=np.array([2.,1.]);corrupt=np.array([-1.,1.]);mc=score(clean);mr=score(corrupt)
    values={(0,0):2.,(0,1):1.,(1,0):2.,(1,1):2.};h=np.zeros((2,2))
    for key,v in values.items():h[key]=(score(corrupt,(*key,v))-mr)/(mc-mr)
    fig=plt.figure(figsize=(520/72,820/72),facecolor="#F8FAFC");ax=fig.add_axes((.24,.30,.61,.48),facecolor="#F8FAFC")
    ax.pcolormesh(np.arange(3)-.5,np.arange(3)-.5,h,cmap="Blues",vmin=0,vmax=1,shading="flat");ax.set(xlim=(-.5,1.5),ylim=(1.5,-.5),aspect="equal");ax.set_xticks([0,1],["Token 0","Token 1"]);ax.set_yticks([0,1],["Layer 0","Layer 1"]);ax.tick_params(length=0,pad=14)
    for row in range(2):
        for col in range(2):ax.text(col,row,["0","1/3","2/3"][0 if h[row,col]==0 else (1 if h[row,col]<.5 else 2)],ha="center",va="center",fontsize=32,color="#0F172A" if h[row,col]<.5 else "white")
    fig.text(.077,.95,"CPU recovery map",fontsize=29,color="#0F172A");fig.text(.077,.86,"Fixed code recomputation scope",fontsize=25,color="#64748B")
    fig.text(.077,.20,"Clean 4; corrupt −0.5",fontsize=28,color="#0F172A");fig.text(.077,.125,"Peak: layer 1, token 0",fontsize=28,color="#059669");fig.text(.077,.05,"Layer 0 is patched after layer 1.",fontsize=24,color="#D97706")
    fig.savefig(output,format="svg",metadata={"Date":None,"Creator":"ai-math-guide"});plt.close(fig)
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);main(p.parse_args().output)
