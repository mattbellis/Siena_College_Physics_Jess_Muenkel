import numpy as np
import matplotlib.pylab as plt
import sys
import math
import decay_tools as d_tools
import lichen.lichen as lkn
import hep_tools_text_files as hep

t0=[]       #top and decay 
   
    

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




    #print "--------------------------"
    pdgs=[]
    pts=[]
    etas=[]
    phis=[]


    for p in gen_particles:
        pdg,status,pt,eta,phi = p
        pdgs.append(pdg)
        etas.append(eta)
        phis.append(phi)
        
    t0=d_tools.return_top_decays(pdgs)


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

        
        
        #finding the muons pt
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
        quarks_pt.append(pts[t0[1][4]])


#Finding top pt
    top_pt.append(pts[t0[0][0]])
    top_pt.append(pts[t0[1][0]])        

    #Finding W pt
    W_pt.append(pts[t0[0][1]])
    W_pt.append(pts[t0[1][1]])
    
    #Finding bottom pt    
    bottom_pt.append(pts[t0[0][2]])
    bottom_pt.append(pts[t0[1][2]])
    
    




plt.figure(1)
#plt.hist(top_pt,bins=50)
lkn.hist_err(top_pt,bins=100,range=(0,300))
plt.title(r"Top and Antitop p$_T$")
plt.xlabel(r"p$_T$(GeV/c)")

plt.figure(2)
#plt.hist(W_pt,bins=50)
lkn.hist_err(W_pt,bins=100,range=(0,300))
plt.title(r"W and Anti_W p$_T$")
plt.xlabel(r"p$_T$(GeV/c)")

plt.figure(3)
#plt.hist(bottom_pt,bins=50)
lkn.hist_err(bottom_pt,bins=100,range=(0,300))
plt.title(r"B and Anti_b p$_T$")
plt.xlabel(r"p$_T$(GeV/c)")


plt.figure (4)
#plt.hist(muon_pt,bins=50)
lkn.hist_err(muon_pt,bins=100,range=(0,300))
plt.title(r"Muon p$_T$")
plt.xlabel(r"p$_T$(GeV/c)")


plt.figure (5)
#plt.hist(electron_pt,bins=50)
lkn.hist_err(electron_pt,bins=100,range=(0,300))
plt.title(r"Electron p$_T$")
plt.xlabel(r"p$_T$(GeV/c)")



plt.figure (6)
#plt.hist(neutrino_pt,bins=50)
lkn.hist_err(neutrino_pt,bins=100,range=(0,300))
plt.title(r"Neutrino p$_T$")
plt.xlabel(r"p$_T$(GeV/c)")


plt.figure (7)
#plt.hist(quarks_pt,bins=50)
lkn.hist_err(quarks_pt,bins=100,range=(0,300))
plt.title(r"Quark p$_T$")
plt.xlabel(r"p$_T$(GeV/c)")
plt.show()
