import siena_cms_tools as cms
import numpy as np
import matplotlib.pylab as plt
import math
import sys
import lichen.lichen as lkn



f = open(sys.argv[1])

invarient_mass=[]

collisions = cms.get_collisions(f)

print "Number of collisions:"
print len(collisions)

for collision in collisions:

    #cms.pretty_print(collision)

    jets,topjets,muons,electrons,photons,met = collision

    ##################################################################
    #### Find 2 jets to look for hadronicly decaying W
    ##################################################################    

    njets = len(jets)
    if njets>=2:
        for i in range(0,njets):
            for j in range(i+1,njets):

                mass=np.sqrt(((jets[i][0]+jets[j][0])**2)-((jets[i][1]+jets[j][1])**2+(jets[i][2]+jets[j][2])**2+(jets[i][3]+jets[j][3])**2))
                invarient_mass.append(mass)

           

plt.figure(1)


plt.hist(invarient_mass,bins=150,range=(0,400))
#lkn.hist_err(invarent_mass,bins=200)
plt.xlim([0,400])
name = r"Hadronic Decay of W $%s$" % (sys.argv[1].split('/')[-1])
plt.title(name)
plt.ylabel(r"Frequency")
plt.xlabel(r"Invariant Mass")

plt.show()


