# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:11:08 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

h = 26.2
T = 0.07*h**0.75

SsD = 0.8
S1D = 0.45
SsM	= 1
S1M	= 0.55

Fa_D = 1
Fa_V = 1.1

SDs = Fa_D*SsD
SD1 = Fa_V*S1D
SMs = Fa_D*SsM
SM1 = Fa_V*S1M

T0_D = SD1/SDs
T0_M = SM1/SMs

def determine_Sa(T,T0_D,SDs,SD1):
    if T <= 0.2*T0_D:
        SaD = SDs*(0.4+3*(T/T0_D))
        print("first")
        
    elif T >= 0.2*T0_D and T <= T0_D:
        SaD = SDs
        print("second")
        
    elif T >= T0_D and T <= 2.5*T0_D:
        SaD = SD1/T
        print("third")
        
    elif T >= 2.5*T0_D:
        SaD = 0.4*SDs
        print("fourth")
    return SaD

SaD = determine_Sa(T,T0_D,SDs,SD1)
print("SaD = ",SaD,"\n")
SaM = determine_Sa(T,T0_M,SMs,SM1)
print("SaM = ",SaM,"\n")

fig,ax = plt.subplots()

def plot_Sa(T0_D,SD1,SDs,xlabel,ylabel,title,color,label):
    
    T = np.linspace(T0_D,2.5*T0_D,100)
    SaD_ = SD1/T
    
    ax.plot([0,0.2*T0_D],[0.4*SDs,SDs],color=color,label=label)
    ax.plot([0.2*T0_D,T0_D],[SDs,SDs],color=color)
    ax.plot(np.linspace(T0_D,2.5*T0_D,100),SaD_,color=color)
    ax.plot([2.5*T0_D,3.0*T0_D],[0.4*SDs,0.4*SDs],color=color)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # ax.set_title(title)
    ax.grid(True)
    ax.legend()
    ax.set_ylim(0,max(SaD,SDs)+max(SaD,SDs)/10)
    plt.show()
    
    return None

plot_Sa(T0_D,SD1,SDs,"T","SaD",\
        "Department of Civil Engineering  [SaD]","tab:blue","SaD")
plot_Sa(T0_M,SM1,SMs,"T","Sa",\
        "Department of Civil Engineering  [SaM]","tab:orange","SaM")

