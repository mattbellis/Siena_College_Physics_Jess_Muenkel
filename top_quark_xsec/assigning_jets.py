import numpy as np
import matplotlib.pylab as plt
import sys
import math
import decay_tools as d_tools
import lichen.lichen as lkn
import hep_tools_text_files as hep

t0=[]       #top and decay 

      
    

f = open(sys.argv[1])




minimal_dR=[]
minimal_pt=[]
pt_jet=[]
pt_top=[]



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
    
    ######################################### Top Jets
    
    
    top_pt=[]
    del_r=[]
    del_r_anti=[]
    found=False
    founda=False
    foundr=False
    foundra=False
    

############################Matching the top and anti top jets
    if abs(pdgs[t0[0][3]])<6 or abs(pdgs[t0[1][3]])<6:

        #print "-------"
        for p in ca8jets:
           mass,pt,eta,phi = p
           jet_pt.append(pt)
           jet_eta.append(eta)
           jet_phi.append(phi)
           #print "%8.5f %8.5f %12.5f %12.5f" % (mass,pt,eta,phi)
        

        if abs(pdgs[t0[0][3]])<6:
            for i in range (16):
                del_r.append(d_tools.delta_R_jet(jet_eta[i],jet_phi[i],etas[t0[0][0]],phis[t0[0][0]]))


            min_dR=(min(del_r))

            j=0
            if del_r[j]!=min_dR and foundr==False:
               j=j+1
            elif del_r[j]==min_dR:
                foundr=True
            
            minimal_pt.append(abs(jet_pt[j]-pts[t0[0][0]]))
            minimal_dR.append(min(del_r))
            pt_jet.append(abs(jet_pt[j]))
            pt_top.append(abs(pts[t0[0][0]]))


            
        if abs(pdgs[t0[1][3]])<6:
            for i in range (16):
                del_r_anti.append(d_tools.delta_R_jet(jet_eta[i],jet_phi[i],etas[t0[1][0]],phis[t0[1][0]]))

            min_dR=min(del_r_anti)

            j=0
            if del_r_anti[j]!=min_dR and foundra==False:
               j=j+1
            elif del_r_anti[j]==min_dR:
                foundra=True
            
            minimal_dR.append(min(del_r_anti))            
            minimal_pt.append(abs(jet_pt[j]-pts[t0[1][0]]))
            pt_jet.append(abs(jet_pt[j]))
            pt_top.append(abs(pts[t0[1][0]]))            

    
    
    
    
    






    
    
        #print "%-5d %-5d %8.5f %12.5f %12.5f" % (pdg,status,pt,eta,phi)

    #print "-------"
    #for p in ak5jets:
        #mass,pt,eta,phi = p

        #print "%8.5f %8.5f %12.5f %12.5f" % (mass,pt,eta,phi)















'''plt.figure(1)
plt.subplot(2, 1, 1)
#plt.hist(del_R_mu_other_b,bins=50)
lkn.hist_err(minimal_dR,bins=100)
plt.title("Top and Antitop")
plt.xlabel(r"Abs($\delta$R)")

plt.subplot(2, 1, 2)
#plt.hist(del_R_mu_b,bins=50)
lkn.hist_err(minimal_pt,bins=100)
plt.xlabel("Abs(pt)")'''


'''plt.figure(2)
plt.subplot(2, 1, 1)
#plt.hist(del_R_mu_other_b,bins=50)
lkn.hist_err(minimal_dR,bins=100)
plt.title("Bottom")
plt.xlabel(r"Abs($\delta$R)")

plt.subplot(2, 1, 2)
#plt.hist(del_R_mu_b,bins=50)
lkn.hist_err(minimal_pt,bins=100)
plt.xlabel("Abs(pt)")'''

plt.figure(3)

#plt.hist(del_R_mu_other_b,bins=50)
lkn.hist_2D(minimal_dR,pt_jet,xbins=80,ybins=80,xrange=(-3,3), yrange=(0,200))
plt.title(r"$Jet$ $vs$ $\delta$$R$")
plt.xlabel(r"$Abs($$\delta$R)")
plt.ylabel(r"$Jet$ $p$$_t$")


plt.figure(4)
#plt.hist(del_R_mu_b,bins=50)
lkn.hist_2D(minimal_dR,pt_top,xbins=80,ybins=80,xrange=(-3,3), yrange=(0,200))
plt.title(r"$t$ $\bar{t}$ $vs$ $\delta$$R$")
plt.xlabel(r"$Abs($$\delta$$R)$")
plt.ylabel(r"$t$ $\bar{t}$ $p$$_t$")

plt.show()

#python2.7-32 assigning_jets.py small_file.txt