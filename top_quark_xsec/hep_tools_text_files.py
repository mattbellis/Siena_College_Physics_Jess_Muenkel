import numpy as np


################################################################################
################################################################################
def get_collisions(infile,verbose=False):

    collisions = np.loadtxt(infile,unpack=False,dtype='float')

    return collisions

################################################################################
def get_truth_particles_from_collision(collision):

    #print collision
    nvariables = 5
    nvals = len(collision)
    nparticles = nvals/nvariables

    particles = []
    index = np.arange(0,nvals,nvariables)
    #print index
    #print collision[index]
    pdgs = collision[index].astype('int')
    statuses = collision[index+1].astype('int')
    pts = collision[index+2]
    etas = collision[index+3]
    phis = collision[index+4]

    for i in xrange(nparticles):
        particles.append([pdgs[i],statuses[i],pts[i],etas[i],phis[i]])

    return particles
