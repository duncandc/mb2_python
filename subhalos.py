"""
File I/O related to the MBII (sub-)halo particle files
"""

from __future__ import print_function
import numpy as np
import os
from mb2_python.utils import packarray
from mb2_python.data import pdtype
from mb2_python.groupcat import readshc, readgc


__all__=['shPath', 'shHeader', 'loadHalo', 'loadSubhalo']
__author__=['Duncan Campbell', 'Yu Feng']


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


def loadSubhalo(basePath, snapNum, partType, field, ids=None):
    """
    Load all particles/cells of one type for a specific subhalo

    Parameters
    ----------
    basePath : string
        absolute path to mb2 data directory

    snapNum : int
        snapshot number

    partType : int
        particle type--must be in the range [0,5]

    field : string
        particle property name

    ids : array_like, optional
        array of subhalo IDs

    Returns
    -------
    p_arr : pack_array
        pack_array object storing requested particle data ordered by subhalo
    """
    
    # check particle type
    partType = int(partType)
    if str(partType) in '012345':
    	pass
    else:
    	msg = ('partType has to be 0 - 5')
    	raise KeyError(msg)

    # check field
    if field in pdtype.names:
        dtype = pdtype[field]
    else:
        msg = ("{0} not available.".format(field))
        raise ValueError(msg)

    fname = _partType_filename(basePath, snapNum, str(partType), field)
    size = os.path.getsize(fname)

    if size == 0:
        rt = np.fromfile(fname, dtype=dtype)
    else:
        rt = np.memmap(fname, mode='r', dtype=dtype)

    g = readshc(basePath, snapNum)

    if ids is None:
        rt = packarray(rt, g['lenbytype'][:, partType])
    else:
    	ids = np.atleast_1d(ids)
    	rt = packarray(rt, g['lenbytype'][ids, partType])

    return rt


def loadHalo(basePath, snapNum, partType, field, ids=None):
    """
    Load all particles/cells of one type for a specific halo

    Parameters
    ----------
    basePath : string
        absolute path to mb2 data directory

    snapNum : int
        snapshot number

    partType : int
        particle type--must be in the range [0,5]

    field : string
        particle property name

    ids : array_like, optional
        array of halo IDs

    Returns
    -------
    p_arr : pack_array
        pack_array object storing requested particle data ordered by halo
    """
	
	# check particle type
    partType = int(partType)
    if str(partType) in '012345':
        pass
    else:
    	msg = ('partType has to be 0 - 5')
    	raise KeyError(msg)

    # check field
    if field in pdtype.names:
        dtype = pdtype[field]
    else:
        msg = ("{0} not available.".format(field))
        raise ValueError(msg)

    fname = _partType_filename(basePath, snapNum, str(partType), field)
    size = os.path.getsize(fname)

    if size == 0:
        rt = np.fromfile(fname, dtype=dtype)
    else:
        rt = np.memmap(fname, mode='r', dtype=dtype)

    g = readgc(basePath, snapNum)

    if ids is None:
        rt = packarray(rt, g['lenbytype'][:, partType])
    else:
    	ids = np.atleast_1d(ids)
    	rt = packarray(rt, g['lenbytype'][ids, partType])

    return rt



def _partType_filename(basePath, snapNum, partType, field):
    """ 
    the file name of a type/field
    """
    fpath = shPath(basePath, snapNum)
    if isinstance(partType, basestring):
        return fpath + '%s/%s.raw' % (partType, field)
    else:
        return fpath + '%d/%s.raw' % (partType, field)



