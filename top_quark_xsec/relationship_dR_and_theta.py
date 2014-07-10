#Looking at the relationship between dR and theta

import numpy as np
import decay_tools as d_tools
import math
import numpy as np
import matplotlib.pylab as plt
import sys
import lichen.lichen as lkn
import hep_tools_text_files as hep



def delta_theta(pt1,eta1,phi1,pt2,eta2,phi2):
    x1=pt1*math.cos(phi1)
    y1=pt1*math.sin(phi1)
    z1=pt1*math.sinh(eta1)
    mpt1=pt1*math.cosh(eta1)    
    
    x2=pt2*math.cos(phi2)
    y2=pt2*math.sin(phi2)
    z2=pt2*math.sinh(eta2)
    mpt2=pt2*math.cosh(eta2) 
    
    t=math.acos((x1*x2+y1*y2+z1*z2)/(mpt1*mpt2))
    
    return t



f = open(sys.argv[1])


top_eta_test=[]
antitop_eta_test=[]
top_phi_test=[]
antitop_phi_test=[]
d_phi=[]
d_eta=[]



del_Theta=[]
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

    
    '''#dR for e or mu and b on other side which is hadronic  
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
            del_R_mu_other_b.append(dR_mu_other_b[0])'''        


    #dR and dTheta for e or mu and b on same side which is hadronic  
    if abs(pdgs[t0[0][3]])<6 and abs(pdgs[t0[1][3]])>6:
        if pdgs[t0[1][3]]==11 or pdgs[t0[1][3]]==13:
            dR_mu_b=d_tools.delta_R(etas,phis,t0[1][2],t0[1][3])
            del_R_mu_b.append(dR_mu_b[0])

            del_Theta.append(delta_theta(pts[t0[1][2]],etas[t0[1][2]],phis[t0[1][2]],pts[t0[1][3]],etas[t0[1][3]],phis[t0[1][3]]))
            
        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_b=d_tools.delta_R(etas,phis,t0[1][2],t0[1][4])
            del_R_mu_b.append(dR_mu_b[0])
            
            del_Theta.append(delta_theta(pts[t0[1][2]],etas[t0[1][2]],phis[t0[1][2]],pts[t0[1][4]],etas[t0[1][4]],phis[t0[1][4]]))

            
    if abs(pdgs[t0[0][3]])>6 and abs(pdgs[t0[1][3]])<6:
        if pdgs[t0[0][3]]==-11 or pdgs[t0[0][3]]==-13:
            dR_mu_b=d_tools.delta_R(etas,phis,t0[0][2],t0[0][3])
            del_R_mu_b.append(dR_mu_b[0]) 
            
            del_Theta.append(delta_theta(pts[t0[0][2]],etas[t0[0][2]],phis[t0[0][2]],pts[t0[0][3]],etas[t0[0][3]],phis[t0[0][3]]))

        elif pdgs[t0[1][4]]==11 or pdgs[t0[1][4]]==13:
            dR_mu_b=d_tools.delta_R(etas,phis,t0[0][2],t0[0][4])
            del_R_mu_b.append(dR_mu_b[0]) 
            
            del_Theta.append(delta_theta(pts[t0[0][2]],etas[t0[0][2]],phis[t0[0][2]],pts[t0[0][4]],etas[t0[0][4]],phis[t0[0][4]]))














'''
plt.figure(1)
plt.subplot(2, 1, 1)
#plt.hist(del_R_mu_other_b,bins=50)
lkn.hist_err(del_R_mu_other_b,bins=100,range=(0,8))
plt.axis([0, 8, 0, 8])
plt.title(r"e/mu and opposite b $\Delta$R")
#plt.xlabel(r"$\Delta$R")

plt.subplot(2, 1, 2)
#plt.hist(del_R_mu_b,bins=50)
lkn.hist_err(del_R_mu_b,bins=100,range=(0,8))
plt.axis([0, 8, 0, 8])
plt.title(r"e/mu and same side b $\Delta$R")
plt.xlabel(r"$\Delta$R")'''

#####################################
plt.figure(2)
plt.plot(del_Theta,del_R_mu_b,'.')






plt.show()

