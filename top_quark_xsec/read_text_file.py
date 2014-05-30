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

    gen_particles = hep.get_truth_particles_from_collision(collision)

    print "--------------------------"
    for p in gen_particles:
        pdg,status,pt,eta,phi = p

        print "%-5d %-5d %8.5f %12.5f %12.5f" % (pdg,status,pt,eta,phi)

