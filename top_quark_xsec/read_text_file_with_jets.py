import numpy as np
import matplotlib.pylab as plt
import sys
import math

import lichen.lichen as lkn
import hep_tools_text_files as hep

t0=[]       #top and decay 
t1=[]       #antitop and decay


def return_top_decays(pdgs):
    print pdgs
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
   
    
    
    print t0
    print t1
    return[t0,t1]
    
    
def delta_R(eta,phi,m,n):
    
    a=np.abs(phi[m]-phi[n])
    while a > math.pi:
        a=a-math.pi
    
    dR=np.sqrt((np.abs(a))**2+(np.abs(eta[m]-eta[n]))**2)
    
    return dR
    
    
    

f = open(sys.argv[1])



del_R=[]
test=[]
top_pt=[]
W_pt=[]
bottom_pt=[]

muon_pt=[]
electron_pt=[]
neutrino_pt=[]
quarks_pt=[]

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

    print "--------------------------"
    pdgs=[]
    pts=[]
    etas=[]
    phis=[]


    for p in gen_particles:
        pdg,status,pt,eta,phi = p
        pdgs.append(pdg)
        etas.append(eta)
        phis.append(phi)
        
    t0=return_top_decays(pdgs)
    #dR for top quarks
    #dR=delta_R(etas,phis,t0[0][0],t0[1][0])
    #del_R.append(dR)


    muon=False
    anti_muon=False
    
    electron=False
    anti_electron=False 
    
    neutrino=False
    anti_neutrino=False

    
    for p in gen_particles:
        pdg,status,pt,eta,phi = p
        pdgs.append(pdg)
        pts.append(pt)

        #print "%-5d %-5d %8.5f" % (pdg,status,pt)

        
        
        '''#finding the muons pt
        if muon==False and status==3:
            if pdg==-13:
                muon=True                
                muon_pt.append(pt)
        if anti_muon==False and status==3:
            if pdg==13:
                anti_muon=True
                muon_pt.append(pt)
                
    #finding the electrons pt
        if electron==False and status==3:
            if pdg==-11:
                electron=True                
                electron_pt.append(pt)
        if anti_electron==False and status==3:
            if pdg==11:
                anti_electron=True
                electron_pt.append(pt)
            
    #finding the neutrinos pt
        if neutrino==False and status==3:
            if pdg==-12 or pdg==-14 or pdg==-16:
                neutrino=True                
                neutrino_pt.append(pt)
        if anti_neutrino==False and status==3:
            if pdg==12 or pdg==14 or pdg==16:
                anti_neutrino=True
                neutrino_pt.append(pt)
            
    #finding the quarks pt
    if pdgs[t0[0][3]]<6 and pdgs[t0[0][4]]<6:
        quarks_pt.append(pts[t0[0][3]])
        quarks_pt.append(pts[t0[0][4]])
            
    if pdgs[t0[1][3]]<6 and pdgs[t0[1][4]]<6:
        quarks_pt.append(pts[t0[1][3]])
        quarks_pt.append(pts[t0[1][4]])'''

#print del_R
'''#Finding top pt
    top_pt.append(pts[t0[0][0]])
    top_pt.append(pts[t0[1][0]])        

    #Finding W pt
    W_pt.append(pts[t0[0][1]])
    W_pt.append(pts[t0[1][1]])
    
    #Finding bottom pt    
    bottom_pt.append(pts[t0[0][2]])
    bottom_pt.append(pts[t0[1][2]])
    
    
    ######################################### Delta R
    
    
    
    
    
    
    
    
    
        #print "%-5d %-5d %8.5f %12.5f %12.5f" % (pdg,status,pt,eta,phi)

    #print "-------"
    #for p in ak5jets:
        #mass,pt,eta,phi = p

        #print "%8.5f %8.5f %12.5f %12.5f" % (mass,pt,eta,phi)

    #print "-------"
    #for p in ca8jets:
        #mass,pt,eta,phi = p

        #print "%8.5f %8.5f %12.5f %12.5f" % (mass,pt,eta,phi)










plt.figure(1)
#plt.hist(top_pt,bins=50)
lkn.hist_err(top_pt,bins=50)
plt.title("Top and Antitop Pt")

plt.figure(2)
#plt.hist(W_pt,bins=50)
lkn.hist_err(W_pt,bins=50)
plt.title("W and Anti_W Pt")

plt.figure(3)
#plt.hist(bottom_pt,bins=50)
lkn.hist_err(bottom_pt,bins=50)
plt.title("B and Anti_b Pt")


plt.figure (4)
plt.hist(muon_pt,bins=50)
#lkn.hist_err(muon_pt,bins=50)
plt.title("Muon Pt")


plt.figure (5)
plt.hist(electron_pt,bins=50)
#lkn.hist_err(electron_pt,bins=50)
plt.title("Electron Pt")



plt.figure (6)
plt.hist(neutrino_pt,bins=50)
#lkn.hist_err(neutrino_pt,bins=50)
plt.title("Neutrino Pt")


plt.figure (7)
plt.hist(quarks_pt,bins=50)
#lkn.hist_err(quarks_pt,bins=50)
plt.title("Quark Pt")
plt.show()'''