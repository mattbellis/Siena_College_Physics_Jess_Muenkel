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
        a=a-(2*math.pi)
    b=eta[m]-eta[n]
    
    dR=np.sqrt((np.abs(a))**2+(np.abs(b))**2)
    
    return [dR,a,b]
    
def delta_R_jet(eta1,phi1,eta2,phi2):
    a=np.abs(phi1-phi2)
    while a > math.pi:
        a=a-math.pi
    
    dR=np.sqrt((np.abs(a))**2+(np.abs(eta1-eta2))**2)
    return dR      
    

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

    t0=return_top_decays(pdgs)
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
    
    
    '''#dR for top quarks
    dR_top_antitop=delta_R(etas,phis,t0[0][0],t0[1][0])
    del_R_top_antitop.append(dR_top_antitop[0])
    
    #dR for W and b    
    dR_W_B=delta_R(etas,phis,t0[0][1],t0[0][2])
    del_R_W_B.append(dR_W_B[0])
    
    #dR for W- and b-    
    dR_anti_W_B=delta_R(etas,phis,t0[1][1],t0[1][2])
    del_R_anti_W_B.append(dR_anti_W_B[0])
    
    #dR for b and anti b    
    dR_b_anti_b=delta_R(etas,phis,t0[0][2],t0[1][2])
    del_R_b_anti_b.append(dR_b_anti_b[0])
    
    #dR for e or mu and b on other side which is hadronic  
    if abs(pdgs[t0[0][3]])<6 and abs(pdgs[t0[1][3]])>6:
        if pdgs[t0[1][3]]==11 or pdgs[t0[1][3]]==13:
            dR_mu_other_b=delta_R(etas,phis,t0[0][2],t0[1][3])
            del_R_mu_other_b.append(dR_mu_other_b[0])            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_other_b=delta_R(etas,phis,t0[0][2],t0[1][4])
            del_R_mu_other_b.append(dR_mu_other_b[0]) 
            
    if abs(pdgs[t0[0][3]])>6 and abs(pdgs[t0[1][3]])<6:
        if pdgs[t0[0][3]]==-11 or pdgs[t0[0][3]]==-13:
            dR_mu_other_b=delta_R(etas,phis,t0[1][2],t0[0][3])
            del_R_mu_other_b.append(dR_mu_other_b[0])            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_other_b=delta_R(etas,phis,t0[1][2],t0[0][4])
            del_R_mu_other_b.append(dR_mu_other_b[0])        


    #dR for e or mu and b on other side which is hadronic  
    if abs(pdgs[t0[0][3]])<6 and abs(pdgs[t0[1][3]])>6:
        if pdgs[t0[1][3]]==11 or pdgs[t0[1][3]]==13:
            dR_mu_b=delta_R(etas,phis,t0[1][2],t0[1][3])
            del_R_mu_b.append(dR_mu_b[0])            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_b=delta_R(etas,phis,t0[1][2],t0[1][4])
            del_R_mu_b.append(dR_mu_b[0]) 
            
    if abs(pdgs[t0[0][3]])>6 and abs(pdgs[t0[1][3]])<6:
        if pdgs[t0[0][3]]==-11 or pdgs[t0[0][3]]==-13:
            dR_mu_b=delta_R(etas,phis,t0[0][2],t0[0][3])
            del_R_mu_b.append(dR_mu_b[0])            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_b=delta_R(etas,phis,t0[0][2],t0[0][4])
            del_R_mu_b.append(dR_mu_b[0]) '''       





    
    ######################################### Top Jets
    
    
    top_pt=[]
    del_r=[]
    found=False
    founda=False
    foundr=False
    foundra=False
    
    #if abs(pdgs[t0[0][3]])<6 and abs(pdgs[t0[1][3]])<6:        
        #print "******************"
    
    if abs(pdgs[t0[0][3]])<6 or abs(pdgs[t0[1][3]])<6:

        #print "-------"
        for p in ca8jets:
           mass,pt,eta,phi = p
           jet_pt.append(pt)
           jet_eta.append(eta)
           jet_phi.append(phi)
           #print "%8.5f %8.5f %12.5f %12.5f" % (mass,pt,eta,phi)
        #print len(jet_pt)
        if abs(pdgs[t0[0][3]])<6:
            for i in range (16):
                #difference=abs(pts[t0[0][0]]-jet_pt[i])
                #top_pt.append(difference)
                del_r.append(delta_R_jet(jet_eta[i],jet_phi[i],etas[t0[0][0]],phis[t0[0][0]]))

                
            #minimal_pt=min(top_pt)
            min_dR=(min(del_r))
            #i=0
            #if top_pt[i]!=minimal_pt and found==False:
               #i=i+1
            #elif top_pt[i]==minimal_pt:
                #found=True
            j=0
            if del_r[j]!=min_dR and foundr==False:
               j=j+1
            elif del_r[j]==min_dR:
                foundr=True
            
            minimal_pt.append(abs(jet_pt[j]-pts[t0[0][0]]))
            minimal_dR.append(min(del_r))


            
        if abs(pdgs[t0[1][3]])<6:
            for i in range (16):
                #difference=abs(pts[t0[1][0]]-jet_pt[i])
                #top_pt.append(difference)
                del_r.append(delta_R_jet(jet_eta[i],jet_phi[i],etas[t0[1][0]],phis[t0[1][0]]))

                
            #minimal_pt=min(top_pt)
            min_dR=min(del_r)
            #i=0
            #if top_pt[i]!=minimal_pt and found==False:
               #i=i+1
            #elif top_pt[i]==minimal_pt:
                #found=True
            j=0
            if del_r[j]!=min_dR and foundr==False:
               j=j+1
            elif del_r[j]==min_dR:
                foundr=True
            
            minimal_dR.append(min(del_r))            
            minimal_pt.append(abs(jet_pt[j]-pts[t0[1][0]]))
            

    
    
    
    
    






    
    
        #print "%-5d %-5d %8.5f %12.5f %12.5f" % (pdg,status,pt,eta,phi)

    #print "-------"
    #for p in ak5jets:
        #mass,pt,eta,phi = p

        #print "%8.5f %8.5f %12.5f %12.5f" % (mass,pt,eta,phi)










'''plt.figure(1)
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
plt.xlabel(r"$\Delta$R")'''

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


plt.figure(8)
plt.subplot(2, 1, 1)
#plt.hist(del_R_mu_other_b,bins=50)
lkn.hist_err(minimal_dR,bins=100)
#plt.axis([0, 8, 0, 8])
plt.title("Top and Antitop")
plt.xlabel(r"Abs($\delta$R)")

plt.subplot(2, 1, 2)
#plt.hist(del_R_mu_b,bins=50)
lkn.hist_err(minimal_pt,bins=100)
plt.xlabel("Abs(pt)")





plt.show()