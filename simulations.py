"""
basic simulation properties
"""

from astropy import cosmology
import numpy as numpy

cosmo = astropy.cosmology.FlatLambdaCDM(H0=70.2, Om0=0.275, Ob0=0.046)

Lbox = 100.0  # In units of h^-1 Mpc
Nptcl = 2*1792^3
dm_ptcl_mass = 1.1*10^7  # Msol
gas_ptcl_mass = 2.2*10^6  # Msol
softening_length = 1.85  # h^-1 kpc