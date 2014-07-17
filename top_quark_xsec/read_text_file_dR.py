import numpy as np
import matplotlib.pylab as plt
import sys
import math
import decay_tools as d_tools

import lichen.lichen as lkn
import hep_tools_text_files as hep

t0=[]       #top and decay 
      
    

f = open(sys.argv[1])


top_eta_test=[]
antitop_eta_test=[]
top_phi_test=[]
antitop_phi_test=[]
d_phi=[]
d_eta=[]



del_R_top_antitop=[]
del_R_W_B=[]
del_R_anti_W_B=[]
del_R_b_anti_b=[]
del_R_mu_other_b=[]
del_R_mu_b=[]



minimal_dR=[]
minimal_pt=[]



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
        pts.append(pt)
        etas.append(eta)
        phis.append(phi)
        #print "%-5d %8.5f %12.5f %12.5f" % (pdg,pt,eta,phi)

    t0=d_tools.return_top_decays(pdgs)
###########Sanity Check
    '''top_eta_test.append(etas[t0[0][0]])
    antitop_eta_test.append(etas[t0[1][0]])

    top_phi_test.append(phis[t0[0][0]])
    antitop_phi_test.append(phis[t0[1][0]])
    
    dR_top_antitop=delta_R(etas,phis,t0[0][0],t0[1][0])
    d_phi.append(dR_top_antitop[1])
    d_eta.append(dR_top_antitop[2]) 
    
    #del_R_top_antitop.append(dR_top_antitop[0])'''

####################################
    
    
    #dR for top quarks
    dR_top_antitop=d_tools.delta_R(etas,phis,t0[0][0],t0[1][0])
    del_R_top_antitop.append(dR_top_antitop[0])
    
    #dR for W and b    
    dR_W_B=d_tools.delta_R(etas,phis,t0[0][1],t0[0][2])
    del_R_W_B.append(dR_W_B[0])
    
    #dR for W- and b-    
    dR_anti_W_B=d_tools.delta_R(etas,phis,t0[1][1],t0[1][2])
    del_R_anti_W_B.append(dR_anti_W_B[0])
    
    #dR for b and anti b    
    dR_b_anti_b=d_tools.delta_R(etas,phis,t0[0][2],t0[1][2])
    del_R_b_anti_b.append(dR_b_anti_b[0])
    
    #dR for e or mu and b on other side which is hadronic  
    if abs(pdgs[t0[0][3]])<6 and abs(pdgs[t0[1][3]])>6:
        if pdgs[t0[1][3]]==11 or pdgs[t0[1][3]]==13:
            dR_mu_other_b=d_tools.delta_R(etas,phis,t0[0][2],t0[1][3])
            del_R_mu_other_b.append(dR_mu_other_b[0])            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_other_b=d_tools.delta_R(etas,phis,t0[0][2],t0[1][4])
            del_R_mu_other_b.append(dR_mu_other_b[0]) 
            
    if abs(pdgs[t0[0][3]])>6 and abs(pdgs[t0[1][3]])<6:
        if pdgs[t0[0][3]]==-11 or pdgs[t0[0][3]]==-13:
            dR_mu_other_b=d_tools.delta_R(etas,phis,t0[1][2],t0[0][3])
            del_R_mu_other_b.append(dR_mu_other_b[0])            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_other_b=d_tools.delta_R(etas,phis,t0[1][2],t0[0][4])
            del_R_mu_other_b.append(dR_mu_other_b[0])        


    #dR for e or mu and b on other side which is hadronic  
    if abs(pdgs[t0[0][3]])<6 and abs(pdgs[t0[1][3]])>6:
        if pdgs[t0[1][3]]==11 or pdgs[t0[1][3]]==13:
            dR_mu_b=d_tools.delta_R(etas,phis,t0[1][2],t0[1][3])
            del_R_mu_b.append(dR_mu_b[0])            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_b=d_tools.delta_R(etas,phis,t0[1][2],t0[1][4])
            del_R_mu_b.append(dR_mu_b[0]) 
            
    if abs(pdgs[t0[0][3]])>6 and abs(pdgs[t0[1][3]])<6:
        if pdgs[t0[0][3]]==-11 or pdgs[t0[0][3]]==-13:
            dR_mu_b=d_tools.delta_R(etas,phis,t0[0][2],t0[0][3])
            del_R_mu_b.append(dR_mu_b[0])            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_b=d_tools.delta_R(etas,phis,t0[0][2],t0[0][4])
            del_R_mu_b.append(dR_mu_b[0])        








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

'''##############################Sanity Check
plt.figure(5)
plt.subplot(2, 1, 1)
#plt.hist(del_R_mu_other_b,bins=50)
lkn.hist_err(top_phi_test,bins=100,range=(-8,8))
#plt.axis([0, 8, 0, 8])
plt.title("Top")
plt.xlabel("Phi")

plt.subplot(2, 1, 2)
#plt.hist(del_R_mu_b,bins=50)
lkn.hist_err(top_eta_test,bins=100,range=(-8,8))
#plt.axis([0, 8, 0, 8])
#plt.title(r"e/mu and same side b $\Delta$R")
plt.xlabel("Eta")

plt.figure(6)
plt.subplot(2, 1, 1)
#plt.hist(del_R_mu_other_b,bins=50)
lkn.hist_err(antitop_phi_test,bins=100,range=(-8,8))
#plt.axis([0, 8, 0, 8])
plt.title("AntiTop")
plt.xlabel("Phi")

plt.subplot(2, 1, 2)
#plt.hist(del_R_mu_b,bins=50)
lkn.hist_err(antitop_eta_test,bins=100,range=(-8,8))
plt.xlabel("Eta")


plt.figure(7)
plt.subplot(2, 1, 1)
#plt.hist(del_R_mu_other_b,bins=50)
lkn.hist_err(d_phi,bins=100,range=(-8,8))
#plt.axis([0, 8, 0, 8])
plt.title(r"$\delta$ $\phi$")
#plt.xlabel("Phi")

plt.subplot(2, 1, 2)
#plt.hist(del_R_mu_b,bins=50)
lkn.hist_err(d_eta,bins=100,range=(-8,8))
plt.title(r"$\delta$ $\eta$")'''
#####################################







plt.show()