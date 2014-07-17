
####Make a text file that writes out for each event the highest pt top, pt muon and dR between them

import numpy as np
import decay_tools as d_tools
import math
import numpy as np
import matplotlib.pylab as plt
import sys
import hep_tools_text_files as hep




f = open(sys.argv[1])


file=open("highest_pt.txt","w")


print "Reading in the data...."
collisions = hep.get_collisions(f)

print len(collisions)

count = 0
for collision in collisions:

    gen_particles,ak5jets,ca8jets = hep.get_truth_particles_from_collision(collision)


    pdgs=[]
    pts=[]
    etas=[]
    phis=[]
    muon_pt=[]
    output = ""
    top_eta=0
    top_phi=0
    muon_eta=0
    muon_phi=0
    del_r=[]

    for p in gen_particles:
        pdg,status,pt,eta,phi = p
        pdgs.append(pdg)
        pts.append(pt)
        etas.append(eta)
        phis.append(phi)


    t0=d_tools.return_top_decays(pdgs)
    if pdgs[t0[0][3]]==13 or pdgs[t0[0][3]]==-13 or pdgs[t0[0][4]]==13 or pdgs[t0[0][4]]==-13 or pdgs[t0[1][3]]==13 or pdgs[t0[1][3]]==-13 or pdgs[t0[1][4]]==13 or pdgs[t0[1][4]]==-13:
        max_top_pt=max(pts[t0[0][0]],pts[t0[1][0]])
        output += "%f " % (max_top_pt)
        if pts[t0[0][0]]>pts[t0[1][0]]:
            top_eta=etas[t0[0][0]]
            top_phi=phis[t0[0][0]]
        else:
            top_eta=etas[t0[1][0]]
            top_phi=phis[t0[1][0]]
    
    if pdgs[t0[0][3]]==13 or pdgs[t0[0][3]]==-13:
        muon_pt.append(pts[t0[0][3]])
    if pdgs[t0[0][4]]==13 or pdgs[t0[0][4]]==-13:
        muon_pt.append(pts[t0[0][4]])
    if pdgs[t0[1][3]]==13 or pdgs[t0[1][3]]==-13:
        muon_pt.append(pts[t0[1][3]])
    if pdgs[t0[1][4]]==13 or pdgs[t0[1][4]]==-13:
        muon_pt.append(pts[t0[1][4]])

    if len(muon_pt)>0:
        
        max_muon_pt=max(muon_pt)
        i=0

        while pts[i]!=max_muon_pt:
            i=i+1
        
        muon_eta=etas[i]
        muon_phi=phis[i]
            
        output += "%f " % (max_muon_pt)
        
        del_r=d_tools.delta_R_jet(top_eta,top_phi,muon_eta,muon_phi)

        output += "%f " % (del_r)
        
        output+= "\n"
    
        file.write(output)
    
file.close()



    
    
    
    
    
    
    
