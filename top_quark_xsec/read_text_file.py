import numpy as np
import matplotlib.pylab as plt
import sys

import hep_tools_text_files as hep

f = open(sys.argv[1])

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
    for p in gen_particles:
        pdg,status,pt,eta,phi = p

        print "%-5d %-5d %8.5f %12.5f %12.5f" % (pdg,status,pt,eta,phi)

    print "-------"
    for p in ak5jets:
        mass,pt,eta,phi = p

        print "%8.5f %8.5f %12.5f %12.5f" % (mass,pt,eta,phi)

    print "-------"
    for p in ca8jets:
        mass,pt,eta,phi = p

        print "%8.5f %8.5f %12.5f %12.5f" % (mass,pt,eta,phi)
