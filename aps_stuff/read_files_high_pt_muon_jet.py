import siena_cms_tools as cms
import numpy as np
import matplotlib.pylab as plt
import math
import sys

f = open(sys.argv[1])

pt1=[]
pt2=[]
jet_pt=[]
muon_pt=[]


collisions = cms.get_collisions(f)

for collision in collisions:

    #cms.pretty_print(collision)

    jets,topjets,muons,electrons,photons,met = collision


    pt1=[]
    pt2=[]

##################################################################
#### Find the highest Pt Jet
##################################################################    
    print "n_jets: %d" % (len(jets))
    if len(jets)>0:
        for j in jets:
            #print j[0]
            pt=math.sqrt(j[1]*j[1]+j[2]*j[2])
            pt1.append(pt)
        jet_pt.append(max(pt1))


##################################################################
#### Find the highest Pt Muons
################################################################## 


    print "n_muons: %d" % (len(muons))
    if len(muons)>0:
        for m in muons:
            pt=math.sqrt(m[1]*m[1]+m[2]*m[2])
            pt2.append(pt)
        muon_pt.append(max(pt2))


plt.figure(1)

plt.subplot(2,1,1)
plt.hist(jet_pt,bins=100)
plt.title(r"$Highest$ $p$$_t$ $t$ $\bar{t}$")
plt.ylabel(r"$Jet$ $Frequency$")

plt.subplot(2,1,2)
plt.hist(muon_pt,bins=100)
plt.xlabel(r"$p$$_t$")
plt.ylabel(r"$Muon$ $Frequency$")

plt.show()
#print jet_pt
#print muon_pt
