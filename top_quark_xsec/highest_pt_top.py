
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
    top_pt=0
    top_eta=0
    top_phi=0
    muon_pt=0
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
    
    if abs(pdgs[t0[0][3]])==13 or abs(pdgs[t0[0][4]])==13 or abs(pdgs[t0[1][3]])==13 or abs(pdgs[t0[1][4]])==13:
        if abs(pdgs[t0[0][3]])<7 or abs(pdgs[t0[0][4]])<7 or abs(pdgs[t0[1][3]])<7 or abs(pdgs[t0[1][4]])<7:
            ###Find Top that decays hadronicly when other side decays to muon
            if abs(pdgs[t0[0][3]])<7 or abs(pdgs[t0[0][4]])<7:
                top_pt=pts[t0[0][0]]
                top_eta=etas[t0[0][0]]
                top_phi-phis[t0[0][0]]
                
            elif abs(pdgs[t0[1][3]])<7 or abs(pdgs[t0[1][4]])<7:
                top_pt=pts[t0[1][0]]
                top_eta=etas[t0[1][0]]
                top_phi-phis[t0[1][0]]                
                

            output += "%f " % (top_pt)
            
            if abs(pdgs[t0[0][3]])==13:
                muon_pt=pts[t0[0][3]]
                muon_eta=etas[t0[0][3]]
                muon_phi=phis[t0[0][3]]
            elif abs(pdgs[t0[0][4]])==13:
                muon_pt=pts[t0[0][4]]
                muon_eta=etas[t0[0][4]]
                muon_phi=phis[t0[0][4]]            
            elif abs(pdgs[t0[1][3]])==13:
                muon_pt=pts[t0[1][3]]
                muon_eta=etas[t0[1][3]]
                muon_phi=phis[t0[1][3]]            
            elif abs(pdgs[t0[1][4]])==13:
                muon_pt=pts[t0[1][4]]
                muon_eta=etas[t0[1][4]]
                muon_phi=phis[t0[1][4]]            
            
            
            
            output += "%f " % (muon_pt)
        
            del_r=d_tools.delta_R_jet(top_eta,top_phi,muon_eta,muon_phi)

            output += "%f " % (del_r)
        
            output+= "\n"
    
            file.write(output)
    
file.close()



    
    
    
    
    
    
    
