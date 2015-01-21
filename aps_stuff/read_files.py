import siena_cms_made_simple as cms
import numpy as np
import matplotlib.pylab as plt
import sys

f = open(sys.argv[1])

collisions = cms.get_collisions(f)

for collision in collisions:

    jets,topjets,muons,electrons,photons,met = collision

    print "njets: %d" % (len(jets))
    for j in jets:
        print j
