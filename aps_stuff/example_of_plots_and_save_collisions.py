import siena_cms_tools as cms
import matplotlib.pylab as plt

import numpy as np

import sys

import time




################################################################################
# Inv mass
################################################################################
def inv_mass(p):

    ptot = [0.0,0.0,0.0,0.0]
    for pvals in p:
        ptot[0] += pvals[0]
        ptot[1] += pvals[1]
        ptot[2] += pvals[2]
        ptot[3] += pvals[3]

    mass = np.sqrt(ptot[0]*ptot[0] - (ptot[1]*ptot[1] + ptot[2]*ptot[2] + ptot[3]*ptot[3]))

    return mass

################################################################################




start = time.time()
collisions = cms.get_collisions(sys.argv[1])
print "Time to read in %d collisions: %f seconds" % (len(collisions),time.time()-start)

print len(collisions)

#fig = plt.figure(figsize=(7,5),dpi=100)
#ax = fig.add_subplot(1,1,1)
#ax = fig.gca(projection='3d')
#plt.subplots_adjust(top=0.98,bottom=0.02,right=0.98,left=0.02)

fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
ax = fig.gca(projection='3d')

collisions_to_save = []


nevents = len(collisions)

for i in xrange(nevents):
    # Animate 
    lines,fig,ax = cms.display_collision3D(collisions[i],fig=fig,ax=ax)
    plt.xlabel(r"$P_x$ $(GeV/c^2)$")
    plt.ylabel(r"$P_y$ $(GeV/c^2)$")
    ax.set_zlabel(r"$P_z$ $(GeV/c^2)$")
    plt.title("4-Vector Display $%s$" % (sys.argv[1].split('/')[-1]))
    plt.pause(0.0001)

    #name = "Plots/img_%04d.png" % (i)
    #plt.savefig(name)

    jets,topjets,muons,electrons,photons,met = collisions[i]
    
    # Find interesting events and save those subset
    
    #############################
    #### Looking for High pt Muons 
    #############################
    '''is_either_muon_high_pt = False
    for muon in muons:
        E,px,py,pz,charge = muon
        pt = np.sqrt(px*px + py*py)
        if pt>200:
            print pt
            is_either_muon_high_pt = True

    if (is_either_muon_high_pt==True):
        collisions_to_save.append(collisions[i])'''

    #############################
    #### Looking for ZZZZZZZs 
    #############################
    '''is_there_z=False
    nmuons=len(muons)

    if nmuons>=2:
        for i in range(0,nmuons):
            for j in range (i+1,nmuons):
                if muons[i][4]!=muons[j][4]:
                    mass=inv_mass([muons[i],muons[j]])
                    if mass<91.4 and mass>91:
                        is_there_z=True
                        #print mass
        if is_there_z==True:
            collisions_to_save.append(collisions[i])'''

    #############################
    #### Looking for Tops 
    #############################
    '''is_there_w=False
    njets=len(jets)
    if njets>=3:
        for i in range(0,njets):

            for j in range (i+1,njets):
                for k in range (j+1,njets):
                    
                    if (jets[i][4]>1.0):
                        wmass = inv_mass([jets[j],jets[k]])
                        if wmass>79.5 and wmass<81.5:
                            is_there_w=True
                    elif (jets[j][4]>1.0):
                        wmass = inv_mass([jets[i],jets[k]])
                        if wmass>79.5 and wmass<81.5:
                            is_there_w=True
                    elif (jets[k][4]>1.0):
                        wmass = inv_mass([jets[i],jets[j]])
                        if wmass>79.5  and wmass<81.5:
                            is_there_w=True
        if is_there_w==True:
            collisions_to_save.append(collisions[i])'''

    #############################
    #### Looking for QCD jets 
    #############################

    '''if len(jets)>5:
        collisions_to_save.append(collisions[i])'''

#print len(collisions_to_save)


# Write it to a file for later processing
#cms.write_to_file(collisions_to_save,'interesting_w_data_file')

plt.show(block=False)

