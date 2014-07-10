import numpy as np

import math

t0=[]       #top and decay 
t1=[]       #antitop and decay

#################################################    

def return_top_decays(pdgs):
    #print pdgs
    t0=[-999,-999,-999,-999,-999]       #top and decay 
    t1=[-999,-999,-999,-999,-999]       #antitop and decay

    found_top=False
    found_antitop=False
    
    found_W=False
    found_antiW=False
    
    found_b=False
    found_antib=False
    
    found_decay_1=False
    found_anti_decay_1=False
    
    found_decay_2=False
    found_anti_decay_2=False

    # To find the top and antitop
    for i,pdg in enumerate(pdgs):
        #print i,pdg
        if pdg==6:
            found_top=True
            t0[0] = i
        if pdg==-6:
            found_antitop=True
            t1[0] = i
    
    # To find the W and anti W
    for i,pdg in enumerate(pdgs):
        if pdg==24 and found_top==True:
            found_W=True
            t0[1] = i
        if pdg==-24 and found_antitop==True:
            found_antiW=True
            t1[1] = i
    # To find the b and anti b
    for i,pdg in enumerate(pdgs):
        if pdg==5 and found_W==True:
            found_b=True
            t0[2] = i
        if pdg==-5 and found_antiW==True:
            found_antib=True
            t1[2] = i

    #To find the first decay 
    for i,pdg in enumerate(pdgs):
        if found_decay_1==False and found_b==True and t0[2]<i:
            if pdg==2 or pdg==4:
                found_decay_1=True 
                t0[3] = i
            elif pdg==-11 or pdg==-13 or pdg==-15:
                found_decay_1=True 
                t0[3] = i
                #t0[4]=0.0
     #To find the first anti decay           
        if found_anti_decay_1==False and found_antib==True and t1[2]<i:
            if pdg==-2 or pdg==-4:
                found_anti_decay_1=True
                t1[3] = i
            elif pdg==11 or pdg==13 or pdg==15:
                found_anti_decay_1=True
                t1[3] = i
                #t1[4]=0.0
    #To find the second decay     
    for i,pdg in enumerate(pdgs):     
        if found_decay_2==False and found_decay_1==True and t0[2]<i:        
            if pdg==-1 or pdg==-3:
                found_decay_2=True
                t0[4] = i
            elif pdg==12 or pdg==14 or pdg==16:
                found_decay_2=True
                t0[4] = i
    #To find the second anti decay
        if found_anti_decay_2==False and found_anti_decay_1==True and t1[2]<i:
            if pdg==1 or pdg==3:
                found_anti_decay_2=True
                t1[4] = i 
            elif pdg==-12 or pdg==-14 or pdg==-16:
                found_anti_decay_2=True
                t1[4] = i
   
    
    
    #print t0
    #print t1
    return[t0,t1]
    
#################################################    
def delta_R(eta,phi,m,n):
    
    a=np.abs(phi[m]-phi[n])
    while a > math.pi:
        a=a-(2*math.pi)
    b=eta[m]-eta[n]
    
    dR=np.sqrt((np.abs(a))**2+(np.abs(b))**2)
    
    return [dR,a,b]
#################################################    
    
def delta_R_jet(eta1,phi1,eta2,phi2):
    a=np.abs(phi1-phi2)
    while a > math.pi:
        a=a-math.pi
    
    dR=np.sqrt((np.abs(a))**2+(np.abs(eta1-eta2))**2)
    return dR