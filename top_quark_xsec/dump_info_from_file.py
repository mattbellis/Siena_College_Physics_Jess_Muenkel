#!/usr/bin/env python
# ==============================================================================
# ==============================================================================

from ROOT import gRandom, TH1, TH1D, cout, TCanvas
from ROOT import kRed,kBlack,kBlue
from ROOT import TLorentzVector,TH2D

import ROOT

import sys

import numpy as np



tag = "ttbar_MC_truth"
#tag = "data"

# ==============================================================================
#  Read in the data.
# ==============================================================================

#ROOT.gStyle.SetOptStat(111111111)
ROOT.gStyle.SetOptStat(1)

chain = ROOT.TChain("Events")

for file in sys.argv[1:]:
        chain.AddFile(file)

outfilename = sys.argv[1].split('.root')[0]
outfilename = "%s.dat" % (outfilename)
outfile=open(outfilename,"w")

###############################################################################
# List the specfic data elements that we want to get from the file.
###############################################################################
# Top Truth
truth_str = []
truth_str.append("floats_pfShyftTupleGenParticles_pdgId_ANA.obj")
truth_str.append("floats_pfShyftTupleGenParticles_status_ANA.obj")
truth_str.append("floats_pfShyftTupleGenParticles_pt_ANA.obj")
truth_str.append("floats_pfShyftTupleGenParticles_eta_ANA.obj")
truth_str.append("floats_pfShyftTupleGenParticles_phi_ANA.obj")

p4 = TLorentzVector()

#chain.SetBranchStatus('*', 1 )
chain.SetBranchStatus('*', 0 )
for s in truth_str:
    chain.SetBranchStatus(s, 1 )
#for s in top_str:
    #chain.SetBranchStatus(s, 1 )


nev = chain.GetEntries()
print "About to loop over %d collisions" % (nev)

maximum_number_of_gen_particles = 32

################################################################################
# Loop over the events
################################################################################
for n in xrange(nev):
    output=""
    if n%1000==0:
        print "%d of %d" % (n,nev)

    chain.GetEntry(n)

    #print '---------------------'
    for i in xrange(32):
        pdg = chain.GetLeaf(truth_str[0]).GetValue(i)
        status = chain.GetLeaf(truth_str[1]).GetValue(i)
        pt = chain.GetLeaf(truth_str[2]).GetValue(i)
        eta = chain.GetLeaf(truth_str[3]).GetValue(i)
        phi = chain.GetLeaf(truth_str[4]).GetValue(i)

        #print "%-5d %-5d %8.5f %12.5f %12.5f" % (pdg,status,pt,eta,phi)


        output+="%-5d " % (pdg)
        output+="%-5d " % (status)
        output+="%8.5f " % (pt)
        output+="%12.5f " % (eta)
        output+="%12.5f " % (phi)

    output += "\n"


        
    outfile.write(output)

        
outfile.close()






################################################################################
if __name__=="__main__":
    rep = ''
    while not rep in [ 'q', 'Q' ]:
        rep = raw_input( 'enter "q" to quit: ' )
        if 1 < len(rep):
            rep = rep[0]





