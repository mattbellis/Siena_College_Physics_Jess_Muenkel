import siena_cms_tools as cms
import matplotlib.pylab as plt

import numpy as np

import sys

import time

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
    #lines,fig,ax = cms.display_collision3D(collisions[i],fig=fig,ax=ax)
    #plt.pause(0.0001)
    #name = "Plots/img_%04d.png" % (i)
    #plt.savefig(name)

    jets,topjets,muons,electrons,photons,met = collisions[i]

    # Find interesting events and save those subset
    is_either_muon_high_pt = False
    for muon in muons:
        E,px,py,pz,charge = muon
        pt = np.sqrt(px*px + py*py)
        if pt>200:
            print pt
            is_either_muon_high_pt = True

    if (is_either_muon_high_pt==True):
        collisions_to_save.append(collisions[i])

# Write it to a file for later processing
cms.write_to_file(collisions_to_save,'interesting_zz')

#plt.show(block=False)

