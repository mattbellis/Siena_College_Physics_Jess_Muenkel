import numpy as np
import matplotlib.pylab as plt
import sys
import math

import lichen.lichen as lkn
import hep_tools_text_files as hep

t0=[]       #top and decay 
t1=[]       #antitop and decay


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
    
    
def delta_R(eta,phi,m,n):
    
    a=np.abs(phi[m]-phi[n])
    while a > math.pi:
        a=a-math.pi
    
    dR=np.sqrt((np.abs(a))**2+(np.abs(eta[m]-eta[n]))**2)
    
    return dR
    
    
    

f = open(sys.argv[1])



del_R_top_antitop=[]
del_R_W_B=[]
del_R_anti_W_B=[]
del_R_b_anti_b=[]
del_R_mu_other_b=[]
del_R_mu_b=[]



print "Reading in the data...."
collisions = hep.get_collisions(f)

print len(collisions)

count = 0
for collision in collisions:

    gen_particles,ak5jets,ca8jets = hep.get_truth_particles_from_collision(collision)

    #print gen_particles
    #print ak5jets
    #print ca8jets

    #exit()

    #print "--------------------------"
    pdgs=[]
    pts=[]
    etas=[]
    phis=[]
    jet_pt=[]
    jet_eta=[]
    jet_phi=[]

    for p in gen_particles:
        pdg,status,pt,eta,phi = p
        pdgs.append(pdg)
        etas.append(eta)
        phis.append(phi)
        #print "%-5d %8.5f %12.5f %12.5f" % (pdg,pt,eta,phi)

    t0=return_top_decays(pdgs)


    #dR for top quarks
    dR_top_antitop=delta_R(etas,phis,t0[0][0],t0[1][0])
    del_R_top_antitop.append(dR_top_antitop)
    
    #dR for W and b    
    dR_W_B=delta_R(etas,phis,t0[0][1],t0[0][2])
    del_R_W_B.append(dR_W_B)
    
    #dR for W- and b-    
    dR_anti_W_B=delta_R(etas,phis,t0[1][1],t0[1][2])
    del_R_anti_W_B.append(dR_anti_W_B)
    
    #dR for b and anti b    
    dR_b_anti_b=delta_R(etas,phis,t0[0][2],t0[1][2])
    del_R_b_anti_b.append(dR_b_anti_b)
    
    #dR for e or mu and b on other side which is hadronic  
    if abs(pdgs[t0[0][3]])<6 and abs(pdgs[t0[1][3]])>6:
        if pdgs[t0[1][3]]==11 or pdgs[t0[1][3]]==13:
            dR_mu_other_b=delta_R(etas,phis,t0[0][2],t0[1][3])
            del_R_mu_other_b.append(dR_mu_other_b)            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_other_b=delta_R(etas,phis,t0[0][2],t0[1][4])
            del_R_mu_other_b.append(dR_mu_other_b) 
            
    if abs(pdgs[t0[0][3]])>6 and abs(pdgs[t0[1][3]])<6:
        if pdgs[t0[0][3]]==-11 or pdgs[t0[0][3]]==-13:
            dR_mu_other_b=delta_R(etas,phis,t0[1][2],t0[0][3])
            del_R_mu_other_b.append(dR_mu_other_b)            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_other_b=delta_R(etas,phis,t0[1][2],t0[0][4])
            del_R_mu_other_b.append(dR_mu_other_b)        


    #dR for e or mu and b on other side which is hadronic  
    if abs(pdgs[t0[0][3]])<6 and abs(pdgs[t0[1][3]])>6:
        if pdgs[t0[1][3]]==11 or pdgs[t0[1][3]]==13:
            dR_mu_b=delta_R(etas,phis,t0[1][2],t0[1][3])
            del_R_mu_b.append(dR_mu_b)            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_b=delta_R(etas,phis,t0[1][2],t0[1][4])
            del_R_mu_b.append(dR_mu_b) 
            
    if abs(pdgs[t0[0][3]])>6 and abs(pdgs[t0[1][3]])<6:
        if pdgs[t0[0][3]]==-11 or pdgs[t0[0][3]]==-13:
            dR_mu_b=delta_R(etas,phis,t0[0][2],t0[0][3])
            del_R_mu_b.append(dR_mu_b)            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_b=delta_R(etas,phis,t0[0][2],t0[0][4])
            del_R_mu_b.append(dR_mu_b)        





    
    ######################################### Delta R
    
    #print "-------"
    #for p in ca8jets:
     #   mass,pt,eta,phi = p
      #  jet_pt.append(pt)
       # jet_eta.append(eta)
        #jet_phi.append(phi)
        #print "%8.5f %8.5f %12.5f %12.5f" % (mass,pt,eta,phi)
    
    
    
    
    
    






    
    
        #print "%-5d %-5d %8.5f %12.5f %12.5f" % (pdg,status,pt,eta,phi)

    #print "-------"
    #for p in ak5jets:
        #mass,pt,eta,phi = p

        #print "%8.5f %8.5f %12.5f %12.5f" % (mass,pt,eta,phi)










plt.figure(1)
#plt.hist(del_R_top_antitop,bins=50)
lkn.hist_err(del_R_top_antitop,bins=100,range=(0,8))
#plt.axis([0, 8, 0, 8])
plt.title(r"Top and Antitop $\Delta$R")
plt.xlabel(r"$\Delta$R")

plt.figure(2)
plt.subplot(2, 1, 1)
#plt.hist(del_R_W_B,bins=50)
lkn.hist_err(del_R_W_B,bins=100,range=(0,8))
#plt.axis([0, 8, 0, 8])
plt.title(r"W and B $\Delta$R")
#plt.xlabel(r"$\Delta$R")

plt.subplot(2, 1, 2)
#plt.hist(del_R_anti_W_B,bins=50)
lkn.hist_err(del_R_anti_W_B,bins=100,range=(0,8))
#plt.axis([0, 8, 0, 8])
plt.title(r"anti W and anti b $\Delta$R")
plt.xlabel(r"$\Delta$R")

plt.figure(3)
#plt.hist(del_R_b_anti_b,bins=50)
lkn.hist_err(del_R_b_anti_b,bins=100,range=(0,8))
#plt.axis([0, 8, 0, 8])
plt.title(r"b and anti b $\Delta$R")
plt.xlabel(r"$\Delta$R")

plt.figure(4)
plt.subplot(2, 1, 1)
#plt.hist(del_R_mu_other_b,bins=50)
lkn.hist_err(del_R_mu_other_b,bins=100,range=(0,8))
#plt.axis([0, 8, 0, 8])
plt.title(r"e/mu and opposite b $\Delta$R")
#plt.xlabel(r"$\Delta$R")

plt.subplot(2, 1, 2)
#plt.hist(del_R_mu_b,bins=50)
lkn.hist_err(del_R_mu_b,bins=100,range=(0,8))
#plt.axis([0, 8, 0, 8])
plt.title(r"e/mu and same side b $\Delta$R")
plt.xlabel(r"$\Delta$R")


plt.show()