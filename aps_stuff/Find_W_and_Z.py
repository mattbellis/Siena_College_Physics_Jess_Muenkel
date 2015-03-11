import siena_cms_tools as cms
import numpy as np
import matplotlib.pylab as plt
import math
import sys
import lichen.lichen as lkn



f = open(sys.argv[1])

invariant_mass_W=[]
invariant_mass_Z=[]
invariant_mass_top=[]

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
                invariant_mass_W.append(mass)

    ##################################################################
    #### Find 2 same leptons to look for Z
    ##################################################################    
    nelectrons=len(electrons)
    nmuons=len(muons)
    if nelectrons>=2:
        for i in range(0,nelectrons):
            for j in range (i+1,nelectrons):
                if electrons[i][4]!=electrons[j][4]:
                    mass=np.sqrt(((electrons[i][0]+electrons[j][0])**2)-((electrons[i][1]+electrons[j][1])**2+(electrons[i][2]+electrons[j][2])**2+(electrons[i][3]+electrons[j][3])**2))
                    invariant_mass_Z.append(mass)
                   

    if nmuons>=2:
        for i in range(0,nmuons):
            for j in range (i+1,nmuons):
                if muons[i][4]!=muons[j][4]:
                    mass=np.sqrt(((muons[i][0]+muons[j][0])**2)-((muons[i][1]+muons[j][1])**2+(muons[i][2]+muons[j][2])**2+(muons[i][3]+muons[j][3])**2))
                    invariant_mass_Z.append(mass)
                        
        
         





    ##################################################################
    #### Find Hadronic Top Quark
    ##################################################################    
    
    if njets>=3:
        for i in range(0,njets):
            for j in range (i+1,njets):
                for k in range (j+1,njets):
                    mass=np.sqrt(((jets[i][0]+jets[j][0]+jets[k][0])**2)-((jets[i][1]+jets[j][1]+jets[k][1])**2+(jets[i][2]+jets[j][2]+jets[k][2])**2+(jets[i][3]+jets[j][3]+jets[k][3])**2))
                    invariant_mass_top.append(mass)
                   

    




'''plt.figure(1)


#plt.hist(invariant_mass_W,bins=150,range=(0,400))
lkn.hist_err(invariant_mass_W,bins=200)
plt.xlim([0,400])
name = r"Hadronic Decay of W $%s$" % (sys.argv[1].split('/')[-1])
plt.title(name)
plt.ylabel(r"Frequency")
plt.xlabel(r"Invariant Mass")

plt.figure(2)


#plt.hist(invariant_mass_Z,bins=100,range=(0,250))
lkn.hist_err(invariant_mass_Z,bins=200)
plt.xlim([0,400])
name = r"Decay of Z $%s$" % (sys.argv[1].split('/')[-1])
plt.title(name)
plt.ylabel(r"Frequency")
plt.xlabel(r"Invariant Mass")'''

plt.figure(3)
#plt.hist(invariant_mass_top,bins=100,range=(0,250))
lkn.hist_err(invariant_mass_top,bins=350)
plt.xlim([0,600])
name = r"Hadronic Top Decay $%s$" % (sys.argv[1].split('/')[-1])
plt.title(name)
plt.ylabel(r"Frequency")
plt.xlabel(r"Invariant Mass")

plt.show()


