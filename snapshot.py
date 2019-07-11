"""
File I/O related to the snapshot files. 
"""

import numpy as np

def snapPath(basePath, snapNum, chunkNum=0):
    """ 
    Return absolute path to a snapshot HDF5 file (modify as needed). 
    """
    snapPath = basePath + '/snapdir'
    snapPath += '/snapdir_' + str(snapNum).zfill(3) + '/'
    filePath = snapPath + 'snap_' + str(snapNum).zfill(3)
    filePath += '.' + str(chunkNum) + '.hdf5'
    return filePath


