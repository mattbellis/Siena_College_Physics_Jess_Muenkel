import siena_cms_tools as cms
import numpy as np
import matplotlib.pylab as plt
import math
import sys
import lichen.lichen as lkn

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




f = open(sys.argv[1])

invariant_mass_W=[]
invariant_mass_Z=[]
invariant_mass_3jet=[]
invariant_mass_top=[]
btag = []
QCD_jets=[]
collisions = cms.get_collisions(f)

print "Number of collisions:"
print len(collisions)

combos = []
ntops = []

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

                mass=inv_mass([jets[i],jets[j]])
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
                    mass=inv_mass([electrons[i],electrons[j]])
                    invariant_mass_Z.append(mass)
                   

    if nmuons>=2:
        for i in range(0,nmuons):
            for j in range (i+1,nmuons):
                if muons[i][4]!=muons[j][4]:
                    mass=inv_mass([muons[i],muons[j]])
                    invariant_mass_Z.append(mass)
                        
        
         





    ##################################################################
    #### Find Hadronic Top Quark
    ##################################################################    
    
    ncombos = 0
    ntop = 0
    if njets>=3:
        for i in range(0,njets):
            btag.append(jets[i][4])

            for j in range (i+1,njets):
                for k in range (j+1,njets):
                    mass=inv_mass([jets[i],jets[j],jets[k]])
                    invariant_mass_3jet.append(mass)
                    ncombos += 1
                    if (jets[i][4]>1.0):
                        wmass = inv_mass([jets[j],jets[k]])
                        if wmass>70 and wmass<100:
                            invariant_mass_top.append(mass)
                            ntop += 1
                    elif (jets[j][4]>1.0):
                        wmass = inv_mass([jets[i],jets[k]])
                        if wmass>70 and wmass<100:
                            invariant_mass_top.append(mass)
                            ntop += 1
                    elif (jets[k][4]>1.0):
                        wmass = inv_mass([jets[i],jets[j]])
                        if wmass>70 and wmass<100:
                            invariant_mass_top.append(mass)
                            ntop += 1

    ntops.append(ntop)
    combos.append(ncombos)
                   
    ##################################################################
    #### Find number of jets for QCD
    ##################################################################
    QCD_jets.append(len(jets))
    




#plt.figure(figsize=(9,9))

'''plt.figure(1)
#plt.subplot(3,3,1)
#plt.hist(invariant_mass_W,bins=150,range=(0,400))
lkn.hist_err(invariant_mass_W,bins=200,range=(0,400))
name = r"Hadronic Decay of W $%s$" % (sys.argv[1].split('/')[-1])
plt.title(name)
plt.ylabel(r"Frequency")
plt.xlabel(r"Invariant Mass")'''

'''plt.figure(2)
#plt.subplot(3,3,2)
lkn.hist_err(invariant_mass_Z,bins=200)
plt.xlim([0,400])
name = r"Decay of Z $%s$" % (sys.argv[1].split('/')[-1])
plt.title(name)
plt.ylabel(r"Frequency")
plt.xlabel(r"Invariant Mass")'''

'''plt.figure(3)
#plt.subplot(3,3,3)
plt.hist(invariant_mass_3jet,bins=300,range=(0,600))
#lkn.hist_err(invariant_mass_3jet,bins=350,range=(0,600))
plt.xlim([0,600])
name = r"Hadronic Top Decay $%s$" % (sys.argv[1].split('/')[-1])
plt.title(name)
plt.ylabel(r"Frequency")
plt.xlabel(r"Invariant Mass of 3-jet combinations $(GeV/c^2)$")
'''
#plt.subplot(3,3,4)
#lkn.hist_err(combos)
#plt.ylabel(r"Entries")
#plt.xlabel(r"Number of combinations")

#btag = np.array(btag)
#plt.subplot(3,3,5)
#lkn.hist_err(btag[btag>0])
#plt.ylabel(r"Entries")
#plt.xlabel(r"b-tag")

#plt.subplot(3,3,6)
plt.figure(4)
plt.hist(invariant_mass_top,bins=300,range=(0,600))
#lkn.hist_err(invariant_mass_top,bins=350,range=(0,600))
plt.xlim([0,600])
name = r"Hadronic Top Decay $%s$" % (sys.argv[1].split('/')[-1])
plt.title(name)
plt.ylabel(r"Frequency")
plt.xlabel(r"Invariant Mass of top candidate $(GeV/c^2)$")

#plt.subplot(3,3,7)
#lkn.hist_err(ntops)
#plt.ylabel(r"Entries")
#plt.xlabel(r"Number of top candidates")


#QCD # of Jets

plt.figure(5)
plt.hist(QCD_jets,bins=10,range=(0,10))
#lkn.hist_err(QCD_jets,bins=10,range=(0,10))
plt.xlim([0,10])
name = r"QCD Numer of Jets $%s$" % (sys.argv[1].split('/')[-1])
plt.title(name)
plt.ylabel(r"Frequency")
plt.xlabel(r"Number of Jets per Event")

plt.show()


