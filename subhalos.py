"""
File I/O related to the MBII subhalo particle files
"""

from __future__ import print_function
import numpy as np
import os
from mb2_python.data import pdtype
from mb2_python.groupcat import readshc, readgc


__all__=['shPath', 'shHeader', 'loadHalo', 'loadSubhalo']


def shPath(basePath, snapNum):
    """
    Return absolute path to a subhalo directory
    """

    shPath = basePath + '/subhalos'
    shPath += '/' + str(snapNum).zfill(3) + '/'
    return shPath


def shHeader(basePath, snapNum):
    """
    Return subhalo header dict
    """

    header_path = shPath(basePath, snapNum)
    headerfile = os.path.join(header_path, 'header.txt') 

    if not os.path.exists(headerfile):
    	msg = ('subhalo header file not found at: {0}'.format(headerfile))
    	raise ValueError(msg)
    
    header_dict = {}
    for line in file(headerfile, 'r'):

        # double flag
        if line.startswith('flag_double(header) = 0'):
            header_dict['flag_double'] = False
        elif line.startswith('flag_double(header) = 1'):
            header_dict['flag_double'] = True

        # redshift
        if line.startswith('redshift(header) = '):
            header_dict['redshift'] = float(line[19:])
        
        # boxsize
        if line.startswith('boxsize(header) = '):
            header_dict['boxsize'] = float(line[18:])

    return header_dict


def loadSubhalo(basePath, snapNum, id, partType, fields=None):
    """
    Load all particles/cells of one type for a specific subhalo
    (optionally restricted to a subset fields)
    """
    
    # check particle type
    partType = int(partType)
    if partType in '012345':
    	pass
    else:
    	msg = ('type has to be "subhalo" or 0 - 5')
    	raise KeyError('msg')

    # check field
    if field in pdtype.names:
        dtype = pdtype[field]
    else:
        msg = ("{0} not available.".format(field))
        raise ValueError(msh)

    fname = _partType_filename(basePath, snapNum, str(partType), field)
    size = os.path.getsize(fname)

    if size == 0:
        rt = np.fromfile(fname, dtype=dtype)
    else:
        rt = np.memmap(fname, mode='r', dtype=dtype)

    g = readshc(basePath, snapNum)
    rt = packarray(rt, g['nhalo'] + 1)

    return rt


def loadHalo(basePath, snapNum, id, partType, fields=None):
	"""
	Load all particles/cells of one type for a specific halo
    (optionally restricted to a subset fields) 
	"""
	pass


def _partType_filename(basePath, snapNum, partType, field):
    """ 
    the file name of a type/field
    """
    fpath = shPath(basePath, snapNum)
    if isinstance(partType, basestring):
        return fpath + '%s/%s.raw' % (partType, field)
    else:
        return fpath + '%d/%s.raw' % (partType, field)



