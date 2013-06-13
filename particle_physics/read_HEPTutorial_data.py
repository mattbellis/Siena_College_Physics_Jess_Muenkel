import numpy as np
import matplotlib.pylab as plt
import itertools

#import ROOT


import sys

f = open(sys.argv[1])

not_at_end = True

masses_muons1 = []
masses_muons2 = []
e=[]
px=[]
py=[]
pz=[]
bq=[]
event_count = 0
while ( not_at_end ):

    ############################################################################
    # Read in one event
    ############################################################################
    line = f.readline()

    if event_count%1000==0:
        print "Event count: ",event_count

    if line=="":
        not_at_end = False

    if line.find("Event")>=0:
        new_event = True

    if new_event==True:

        # Read in the jet info for this event.
        jets = []
        line = f.readline()
        njets = int(line)
        for i in xrange(njets):
            line = f.readline()
            vals = line.split()
            e = float(vals[0])
            px = float(vals[1])
            py = float(vals[2])
            pz = float(vals[3])
            bquark_jet_tag = float(vals[4])
            jets.append([e,px,py,pz,bquark_jet_tag])

        # Read in the muon info for this event.
        muons = []
        line = f.readline()
        nmuons = int(line)
        num_mu=0
        for i in xrange(nmuons):
            line = f.readline()
            vals = line.split()
            e = float(vals[0])
            px = float(vals[1])
            py = float(vals[2])
            pz = float(vals[3])
            charge = int(vals[4])
            muons.append([e,px,py,pz,charge])
            num_mu+=1
            

        # Read in the electron info for this event.
        electrons = []
        line = f.readline()
        nelectrons = int(line)
        for i in xrange(nelectrons):
            line = f.readline()
            vals = line.split()
            e = float(vals[0])
            px = float(vals[1])
            py = float(vals[2])
            pz = float(vals[3])
            charge = int(vals[4])
            electrons.append([e,px,py,pz,charge])

        # Read in the photon info for this event.
        photons = []
        line = f.readline()
        nphotons = int(line)
        for i in xrange(nphotons):
            line = f.readline()
            vals = line.split()
            e = float(vals[0])
            px = float(vals[1])
            py = float(vals[2])
            pz = float(vals[3])
            photons.append([e,px,py,pz])


        # Read in the information about the missing transverse energy (MET) in the event.
        # This is really the x and y direction for the missing momentum.
        line = f.readline()
        vals = line.split()
        met_px = float(vals[0])
        met_py = float(vals[1])

        new_event = False
        event_count += 1

        ########################################################################
        # Now that you've read in the information for *one* event, 
        # do a calculation!
        ########################################################################
        '''mc_dy.txt
#Find the invarent mass for each pair of muons        
        if len(muons)==2:
            e0,e1 =   muons[0][0],muons[1][0]
            px0,px1 = muons[0][1],muons[1][1]
            py0,py1 = muons[0][2],muons[1][2]
            pz0,pz1 = muons[0][3],muons[1][3]

            mass1 = np.sqrt((e0+e1)**2-((px0+px1)**2+(py-+py1)**2+(pz0+pz1)**2))
            masses_muons1.append(mass1)

        ''' 
        ''' # mass of muons      
        for muon in muons:
            e0 = muon[0]
            px0 = muon[1]
            py0= muon[2]
            pz0= muon[3]

            mass2 = np.sqrt(e0**2 - ( px0**2 + py0**2 + pz0**2 ))

            masses_muons2.append(mass2)
        '''
        njets = len(jets)
        for i in range(0,njets):
            for j in range(i+1,njets):
                for k in range(j+1,njets):
                    e0,e1,e2 =   jets[i][0],jets[j][0],jets[k][0]
                    px0,px1,px2 = jets[i][1],jets[j][1],jets[k][1]
                    py0,py1,py2 = jets[i][2],jets[j][2],jets[k][2]
                    pz0,pz1,pz2 = jets[i][3],jets[j][3],jets[k][3]
                    bqj0,bqj1,bqj2=jets[i][4],jets[j][4],jets[k][4]
                    
                    if bqj0>0 or bqj1>0 or bqj2>0:
                        mass1 = np.sqrt((e0+e1+e2)**2-((px0+px1+px2)**2+(py0+py1+py2)**2+(pz0+pz1+pz2)**2))
                        masses_muons1.append(mass1)
                    
    
                
            
''' mass of muons           
plt.figure()
plt.hist(masses_muons2,range=(0,1),bins=100)
'''
'''#find z Boson mc_dy.txt
plt.figure()
plt.hist(masses_muons1,range=(0,240),bins=100)
plt.figure()
plt.hist(masses_muons1,range=(0,30),bins=100)
'''
#mc_ttbar.txt invarent mass
#plt.figure()
#plt.hist(masses_muons1,range=(40,349),bins=100)
#plt.title('Invariant Mass from Jets')

#mc_ttbar.txt invarent mass Pass the cut
plt.figure()
plt.hist(masses_muons1,range=(0,349),bins=100)
plt.title('Invariant Mass from Jets (pass the cut)')

plt.show()

# mc_dy.txt plt.title('Z Boson')

    



