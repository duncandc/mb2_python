"""
basic simulation properties
"""

from astropy import cosmology
import numpy as numpy

cosmo = astropy.cosmology.FlatLambdaCDM(H0=70.2, Om0=0.275, Ob0=0.046)

Lbox = 100.0  # In units of h^-1 Mpc
dm_ptcl_mass = 1.1*10^7  # Msol (scaled with h?)
gas_ptcl_mass = 2.2*10^6  # Msol (scaled with h?)
softening_length = 1.85  # h^-1 kpc