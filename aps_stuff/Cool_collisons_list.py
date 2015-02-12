import siena_cms_tools as cms
import numpy as np
import matplotlib.pylab as plt
import math
import sys
import lichen.lichen as lkn



#f = open(sys.argv[1])

cool_collisions=[]

#collisions = cms.get_collisions_from_file_name(sys.argv[1])
collisions = cms.get_collisions(sys.argv[1])
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
        if jets[i][4]>0:
            b_tag.append(jets[i][4])
            
    output += "%d " % (len(b_tag))

    ##################################################################
    #### b-tag jet value for highest b-tag jet value
    ##################################################################    

    if len(b_tag)==0: 
        output += "%f " % (-999)
    else:
        output += "%f " % (max(b_tag))

    ##################################################################
    #### pt of highest pt b-tag jet (-999 if no b-tag jet)
    ##################################################################    

    b_tag_pt=[]
    for i in range(0,len(jets)):
        if jets[i][4]>0:
            pt=math.sqrt(jets[i][1]**2+jets[i][2]**2+jets[i][3]**2)
            b_tag_pt.append(pt)
    if len(b_tag_pt)==0: 
        output += "%f " % (-999)
    else:
        output += "%f " % (max(b_tag_pt))

    ##################################################################
    #### pt of highest pt non b-tag jet
    ##################################################################    

    non_b_tag_pt=[]
    for i in range(0,len(jets)):
        if jets[i][4]<0:
            pt=math.sqrt(jets[i][1]**2+jets[i][2]**2+jets[i][3]**2)
            non_b_tag_pt.append(pt)
    if len(non_b_tag_pt)==0: 
        output += "%f " % (-999)
    else:
        output += "%f " % (max(non_b_tag_pt))

    ##################################################################
    #### pt of highest pt muon
    ##################################################################    
    muon_pt=[]
    for i in range(0,len(muons)):
        pt=math.sqrt(muons[i][1]**2+muons[i][2]**2+muons[i][3]**2)
        muon_pt.append(pt)

    if len(muon_pt)==0: 
        output += "%f " % (-999)
    else:
        output += "%f " % (max(muon_pt))

    ##################################################################
    #### biggest dR for any pt muon and any jet
    ##################################################################    
    #px=ptcos(phi)
    #py=ptsin(phi)
    #pz=ptsinh(eta)
    #
    #pt=sqrt(px**2+py**2)

    #
    #
    #



    ##################################################################
    #### biggest dR for highest pt muon and any jet
    ##################################################################    






    # When you're finished filling the output string
    output += "\n"

    outfile.write(output)


outfile.close()


           


