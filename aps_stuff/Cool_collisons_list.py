import siena_cms_tools as cms
import numpy as np
import matplotlib.pylab as plt
import math
import sys
import lichen.lichen as lkn



f = open(sys.argv[1])

cool_collisions=[]

collisions = cms.get_collisions(f)

print "Number of collisions:"
print len(collisions)

outfilename = "default.out"
if (len(sys.argv)>2):
    outfilename = sys.argv[2]

outfile = open(outfilename,'w')


for collision in collisions:

    output = ""

    jets,topjets,muons,electrons,photons,met = collision
    cms.pretty_print(collision)
    
    ##################################################################
    #### Type of datafile
    ##################################################################      

    if "ttbar" in sys.argv[1].split('/')[-1]:
        output += "0 "
    elif"wjets" in sys.argv[1].split('/')[-1]:
        output += "1 "
    elif"zz" in sys.argv[1].split('/')[-1]:
        output += "2 "
    elif"ww" in sys.argv[1].split('/')[-1]:
        output += "3 "
    elif"wz" in sys.argv[1].split('/')[-1]:
        output += "4 "
    elif"dy" in sys.argv[1].split('/')[-1]:
        output += "5 "
    elif"qcd" in sys.argv[1].split('/')[-1]:
        output += "6 "

    ##################################################################
    #### Number of jets
    ##################################################################    

    output += "%d " % (len(jets))

    ##################################################################
    #### Number of muons
    ##################################################################    

    output += "%d " % (len(muons))

    ##################################################################
    #### Number of electrons
    ##################################################################    

    output += "%d " % (len(electrons))

    ##################################################################
    #### Number of b-tag jets
    ##################################################################    

    b_tag=[]
    for i in range(0,len(jets)):
        if jet[i][4]>0:
            b_tag.append(jet[i][4])
            
    output += "%d " % (len(b_tag))

    ##################################################################
    #### b-tag jet value for highest b-tag jet value
    ##################################################################    

    output += "%f " % (max(b_tag))

    ##################################################################
    #### pt of highest pt b-tag jet (-999 if no b-tag jet)
    ##################################################################    

    b_tag_pt=[]
    for i in range(0,len(jets)):
        if jet[i][4]>0:
            pt=math.sqrt(jet[i][1]**2+jet[i][2]**2+jet[i][3]**2)
            b_tag_pt.append(pt)
    if len(b_tag_pt)==0: 
        output += "%f " % (-999)
    else:
        output += "%f " % (max(b_tag_jet))

    ##################################################################
    #### pt of highest pt non b-tag jet
    ##################################################################    

    non_b_tag_pt=[]
    for i in range(0,len(jets)):
        if jet[i][4]<0:
            pt=math.sqrt(jet[i][1]**2+jet[i][2]**2+jet[i][3]**2)
            non_b_tag_pt.append(pt)

    output += "%f " % (max(non_b_tag_pt))

    ##################################################################
    #### pt of highest pt muon
    ##################################################################    
    muon_pt=[]
    for i in range(0,len(muon)):
        pt=math.sqrt(muon[i][1]**2+muon[i][2]**2+muon[i][3]**2)
        muon_pt.append(pt)
    output += "%f " % (max(muon_pt))

    ##################################################################
    #### biggest dR for any pt muon and any jet
    ##################################################################    




    ##################################################################
    #### biggest dR for highest pt muon and any jet
    ##################################################################    






    # When you're finished filling the output string
    output += "\n"

    outfile.write(output)


outfile.close()


#    njets = len(jets)
#    if njets>=2:
#        for i in range(0,njets):
#            for j in range(i+1,njets):

                

           

