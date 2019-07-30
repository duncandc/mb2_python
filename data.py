"""
default data access information for MBII
"""

import numpy as np
from collections import OrderedDict
from readgadget.modules.gadget_blockordering import BLOCKORDERING

basePath_default = '/physics/yfeng1/mb2'

pNames = {0: 'GAS  ',
          1: 'DM   ',
          2: 'DISK ',
          3: 'BULGE',
          4: 'STAR ',
          5: 'BNDRY'}

"""
Format of block ordering dictionary looks like this:
(BlockName, [ParticleTypes,FlagsToCheck])
    BlockName : string
        must be equal to those in dataTypes value
        (value!!, not key, see below)
    ParticleTypes : integer list
        defines what types of particles have this block
        -1 means ALL particles
    FlagsToCheck : string
        which flags (if any) to check that determine if block
        is present
"""

BLOCKORDERING3 = OrderedDict([
    ('pos',      [-1]),
    ('vel',      [-1]),
    ('id',       [-1]),
    ('mass',     [-1]),
    ('ie',       [0]),
    ('entropy',  [0, 'flag_pressure_entropy']),
    ('rho',      [0]),
    ('rhoegy',   [0, 'flag_pressure_entropy']),
    ('ye',       [0, 'flag_cool']),
    ('xHI',      [0, 'flag_cool']),
    ('sml',      [0]),
    ('sfr',      [0, 'flag_sfr']),
    ('sft',      [0, 'flag_sft']),
    ('met',      [0, 'flag_met']),
    ('bhmass',   [0, 'flag_cool']),
    ('bhmdot',   [0, 'flag_cool']),
    ('bhnprogs', [0, 'flag_cool']),
])
BLOCKORDERING['CMU'] = BLOCKORDERING3

subdtype = np.dtype([
    ('mass', 'f4'), 
    ('len', 'i4'), 
    ('pos', ('f4', 3)),           # potential min pos
    ('vel', ('f4', 3)),   
    ('vdisp', 'f4'),  
    ('vcirc', 'f4'),  
    ('rcirc', 'f4'),  
    ('parent', 'i4'),             # parent structure
    ('massbytype', ('f4', 6)),  
    ('lenbytype', ('u4',6)), 
    ('unused', 'u4'),    
    ('groupid', 'u4'),            # group id
   ])

groupdtype = np.dtype([
    ('mass', 'f4'),      
    ('len', 'i4'), 
    ('pos', ('f4', 3)),         # 
    ('vel', ('f4', 3)), 
    ('nhalo', 'i4'),            # number of subhalos (contamination)
    ('massbytype', ('f4', 6)),  
    ('lenbytype', ('u4',6)), 
   ])

pdtype = np.dtype([
    ('pos', ('f4', 3)), # position in comoving kpc/h
    ('vel', ('f4', 3)), # velocity in proper units (NOT in GADGET internal unit)
    ('mass', 'f4'),     # mass in 1e10 Msun/h
    ('id', 'u8'),       # unit id of the particle
    ('type', 'u1'),     # type 0 (gas) 1(dm) 4(star) 5(bh)
    ('SEDindex', 'i8'),  # to look up stellar band luminosity
    ('recfrac', 'f4'),   # stellar recycling fraction (ask wilkins)
    ])

