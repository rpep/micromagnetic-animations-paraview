import numpy as np
import scipy as sp


# Constants
mu0 = 4 * np.pi * 1e-7

# Gilbert Damping
alpha = 0.2
gamma = 2.211e5



ts = np.linspace(0, 5e-10, 100)



H = np.array([0, 0, 0.2


def dmdt(f, m, t):
    mxH = np.cross(m, H)
    
    -gamma/(1+alpha*alpha) * 
    
    
