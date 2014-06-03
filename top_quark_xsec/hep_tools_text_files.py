import numpy as np


################################################################################
################################################################################
def get_collisions(infile,verbose=False):

    collisions = np.loadtxt(infile,unpack=False,dtype='float')

    return collisions

################################################################################
def get_truth_particles_from_collision(collision):

    #print collision
    nvariables_particles = 5
    nvariables_ak5jets = 4
    nvariables_ca8jets = 4

    nparticles = 32
    nak5jets = 16
    nca8jets = 16

    nparticle_vals = nvariables_particles*nparticles
    nak5jet_vals = nvariables_ak5jets*nak5jets
    nca8jet_vals = nvariables_ca8jets*nca8jets

    #######################
    # Get the particles
    #######################
    particles = []
    index = np.arange(0,nparticle_vals,nvariables_particles)
    #print index
    #print collision[index]
    pdgs = collision[index].astype('int')
    statuses = collision[index+1].astype('int')
    pts = collision[index+2]
    etas = collision[index+3]
    phis = collision[index+4]

    for i in xrange(nparticles):
        particles.append([pdgs[i],statuses[i],pts[i],etas[i],phis[i]])

    #######################
    # Get the ak5jets
    #######################
    ak5jets = []
    index = np.arange(nparticle_vals,nparticle_vals+nak5jet_vals,nvariables_ak5jets)
    #print index
    #print collision[index]
    masses = collision[index]
    pts = collision[index+1]
    etas = collision[index+2]
    phis = collision[index+3]

    for i in xrange(nak5jets):
        ak5jets.append([masses[i],pts[i],etas[i],phis[i]])

    #######################
    # Get the ca8jets
    #######################
    ca8jets = []
    index = np.arange(nparticle_vals+nak5jet_vals,nparticle_vals+nak5jet_vals+nca8jet_vals,nvariables_ca8jets)
    #print index
    #print collision[index]
    masses = collision[index]
    pts = collision[index+1]
    etas = collision[index+2]
    phis = collision[index+3]

    for i in xrange(nca8jets):
        ca8jets.append([masses[i],pts[i],etas[i],phis[i]])


    return particles,ak5jets,ca8jets
