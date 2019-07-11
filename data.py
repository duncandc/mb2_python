"""
default data access information
"""

from collections import OrderedDict
from pygadgetreader.readgadget import BLOCKORDERING

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
