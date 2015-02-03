import siena_cms_tools as cms
import numpy as np
import matplotlib.pylab as plt
import sys

f = open(sys.argv[1])

collisions = cms.get_collisions(f)

for collision in collisions:

    cms.pretty_print(collision)

    jets,topjets,muons,electrons,photons,met = collision

    '''
    print "njets: %d" % (len(jets))
    for j in jets:
        print j
    '''
