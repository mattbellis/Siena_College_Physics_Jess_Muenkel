
#plots the pt of Top, B, W, and Muons 

import numpy as np
import matplotlib.pylab as plt
import sys
import decay_tools as d_tools
import lichen.lichen as lkn
import hep_tools_text_files as hep

t0=[]       #top and decay 
        
    
    
f = open(sys.argv[1])

top_pt=[]
W_pt=[]
bottom_pt=[]
muon_pt=[]

print "Reading in the data...."
collisions = hep.get_collisions(f)

print len(collisions)

count = 0
for collision in collisions:

    gen_particles,ak5jets,ca8jets = hep.get_truth_particles_from_collision(collision)
    
    print "--------------------------"


    pdgs=[]
    pts=[]

    muon=False
    anti_muon=False
    for p in gen_particles:
        pdg,status,pt,eta,phi = p
        pdgs.append(pdg)
        pts.append(pt)
        
        if muon==False:
            if pdg==-13:
                muon=True                
                muon_pt.append(pt)
        if anti_muon==False:
            if pdg==13:
                anti_muon=True
                muon_pt.append(pt)
        print "%-5d %-5d %8.5f" % (pdg,status,pt)
        
           
    t0=d_tools.return_top_decays(pdgs)
    


    top_pt.append(pts[t0[0][0]])
    top_pt.append(pts[t0[1][0]])        

    W_pt.append(pts[t0[0][1]])
    W_pt.append(pts[t0[1][1]])
        
    bottom_pt.append(pts[t0[0][2]])
    bottom_pt.append(pts[t0[1][2]])

plt.figure(1)
#plt.hist(top_pt,bins=50)
lkn.hist_err(top_pt,bins=50)
plt.title("Top and Antitop Pt")

plt.figure(2)
#plt.hist(W_pt,bins=50)
lkn.hist_err(W_pt,bins=50)
plt.title("W and Anti_W Pt")

plt.figure(3)
#plt.hist(bottom_pt,bins=50)
lkn.hist_err(bottom_pt,bins=50)
plt.title("B and Anti_b Pt")


plt.figure (4)
#plt.hist(muon_pt,bins=50)
lkn.hist_err(muon_pt,bins=50)
plt.title("Muon Pt")
plt.show()




        
        #print "%-5d %-5d %8.5f %12.5f %12.5f" % (pdg,status,pt,eta,phi)
########   group the decay of top and antitop     
        
        #print pdg
'''        
        if pdg==6 or pdg==-6:            
            if pdg==6:
                top=True
            if pdg==-6:
                top_=True
        if top==True or top_==True:

            if pdg!=21 and pdg!=5 and pdg!=-5 and pdg!=24 and pdg!=-24 and pdg!=6 and pdg!=-6:            
                #print pdg
                test.append(pdg)
                
                if pdg==11 or pdg==13 or pdg==15:
                    print "Antitop decayed leptonicly"
            
                elif pdg==-11 or pdg==-13 or pdg==-15:
                    print "Top decayed leptonicly"  
            
                elif pdg==-2 or pdg==-4 or pdg==1 or pdg==3:
                    print "Antitop decayed hadronicly"
                    
                elif pdg==-1 or pdg==-3 or pdg==2 or pdg==4:
                    print "Top decayed hadronicly"

            print pdg
    print test            
        

        if pdg==-5:            
            top=True
            
        if top==True:

            if pdg!=21 and pdg!=5 and pdg!=-5 and pdg!=24 and pdg!=-24 and pdg!=6 and pdg!=-6:            
                print pdg
                test.append(pdg)
                
                if pdg==11 or pdg==13 or pdg==15:
                    print "Antitop decayed leptonicly"
            
                elif pdg==-11 or pdg==-13 or pdg==-15:
                    print "Top decayed leptonicly"  
            
                elif pdg==-2 or pdg==-4 or pdg==1 or pdg==3:
                    print "Antitop decayed hadronicly"
                    
                elif pdg==-1 or pdg==-3 or pdg==2 or pdg==4:
                    print "Top decayed hadronicly"

            #print pdg
    print test'''




            















                
                
###python2.7-32 read_text_file_edited.py small_file.txt 
