import numpy as np
import matplotlib.pylab as plt

#import ROOT


import sys

f = open(sys.argv[1])

not_at_end = True

masses_muons1 = []
masses_muons2 = []

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
        
        if len(jets)>2 and bquark_jet_tag>0:
            if len(jets)==3:
                e0,e1,e2 =   jets[0][0],jets[1][0],jets[2][0]
                px0,px1,px2 = jets[0][1],jets[1][1],jets[2][1]
                py0,py1,py2 = jets[0][2],jets[1][2],jets[2][2]
                pz0,pz1,pz2 = jets[0][3],jets[1][3],jets[2][3]
                mass1 = np.sqrt((e0+e1+e2)**2-((px0+px1+px2)**2+(py0+py1+py2)**2+(pz0+pz1+pz2)**2))
                masses_muons1.append(mass1)
            if len(jets)==4:
                e0,e1,e2,e3 =   jets[0][0],jets[1][0],jets[2][0],jets[3][0]
                px0,px1,px2,px3 = jets[0][1],jets[1][1],jets[2][1],jets[3][1]
                py0,py1,py2,py3 = jets[0][2],jets[1][2],jets[2][2],jets[3][2]
                pz0,pz1,pz2,pz3 = jets[0][3],jets[1][3],jets[2][3],jets[3][3]
                mass1 = np.sqrt((e0+e1+e2)**2-((px0+px1+px2)**2+(py0+py1+py2)**2+(pz0+pz1+pz2)**2))
                masses_muons1.append(mass1)
                mass1 = np.sqrt((e0+e1+e3)**2-((px0+px1+px3)**2+(py0+py1+py3)**2+(pz0+pz1+pz3)**2))
                masses_muons1.append(mass1)
                mass1 = np.sqrt((e0+e2+e3)**2-((px0+px2+px3)**2+(py0+py2+py3)**2+(pz0+pz2+pz3)**2))
                masses_muons1.append(mass1)
                mass1 = np.sqrt((e1+e2+e3)**2-((px1+px2+px3)**2+(py1+py2+py3)**2+(pz1+pz2+pz3)**2))
                masses_muons1.append(mass1)
            if len(jets)==5:
                e0,e1,e2,e3,e4 =   jets[0][0],jets[1][0],jets[2][0],jets[3][0],jets[4][0]
                px0,px1,px2,px3,px4 = jets[0][1],jets[1][1],jets[2][1],jets[3][1],jets[4][1]
                py0,py1,py2,py3,py4 = jets[0][2],jets[1][2],jets[2][2],jets[3][2],jets[4][2]
                pz0,pz1,pz2,pz3,pz4 = jets[0][3],jets[1][3],jets[2][3],jets[3][3],jets[4][3]
                
                mass1 = np.sqrt((e0+e1+e2)**2-((px0+px1+px2)**2+(py0+py1+py2)**2+(pz0+pz1+pz2)**2))
                masses_muons1.append(mass1)
                mass1 = np.sqrt((e0+e1+e3)**2-((px0+px1+px3)**2+(py0+py1+py3)**2+(pz0+pz1+pz3)**2))
                masses_muons1.append(mass1)
                mass1 = np.sqrt((e0+e2+e3)**2-((px0+px2+px3)**2+(py0+py2+py3)**2+(pz0+pz2+pz3)**2))
                masses_muons1.append(mass1)
                mass1 = np.sqrt((e1+e2+e3)**2-((px1+px2+px3)**2+(py1+py2+py3)**2+(pz1+pz2+pz3)**2))
                masses_muons1.append(mass1)
                mass1 = np.sqrt((e0+e1+e4)**2-((px0+px1+px4)**2+(py0+py1+py4)**2+(pz0+pz1+pz4)**2))
                masses_muons1.append(mass1)
                mass1 = np.sqrt((e0+e2+e4)**2-((px0+px2+px4)**2+(py0+py2+py4)**2+(pz0+pz2+pz4)**2))
                masses_muons1.append(mass1)
                mass1 = np.sqrt((e0+e3+e4)**2-((px0+px3+px4)**2+(py0+py3+py4)**2+(pz0+pz3+pz4)**2))
                masses_muons1.append(mass1)
                mass1 = np.sqrt((e1+e2+e4)**2-((px1+px2+px4)**2+(py1+py2+py4)**2+(pz1+pz2+pz4)**2))
                masses_muons1.append(mass1)
                mass1 = np.sqrt((e1+e3+e4)**2-((px1+px3+px4)**2+(py1+py3+py4)**2+(pz1+pz3+pz4)**2))
                masses_muons1.append(mass1)
                mass1 = np.sqrt((e2+e3+e4)**2-((px2+px3+px4)**2+(py2+py3+py4)**2+(pz2+pz3+pz4)**2))
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

    



