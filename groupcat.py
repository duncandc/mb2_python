"""
File I/O related to the MBII (sub-)halo catalogs
"""

from __future__ import print_function, division
from mb2_python.utils import packarray
from mb2_python.data import subdtype, groupdtype
import numpy as np

__all__=['gcPath', 'shPath']
__author__=['Duncan Campbell']


def gcPath(basePath, snapNum):
    """ 
    Return absolute path to a group catalog.
    """
    gcPath = basePath + '/subhalos'
    gcPath += '/' + str(snapNum).zfill(3) + '/'
    filePath = gcPath + 'grouphalotab.raw'
    return filePath


def shcPath(basePath, snapNum):
    """
    Return absolute path to a subhalo catalog. 
    """
    shcPath = basePath + '/subhalos'
    shcPath += '/' + str(snapNum).zfill(3) + '/'
    filePath = shcPath + 'subhalotab.raw'
    return filePath


def readshc(basePath, snapNum):
    """ 
    Read the basic subhalo catelog.
    """

    subhalofile = shcPath(basePath, snapNum)
    return np.memmap(subhalofile, mode='r', dtype=subdtype)


def readgc(basePath, snapNum):
    """ 
    read the basic group catelog.
    """

    groupfile = gcPath(basePath, snapNum)
    return np.memmap(groupfile, mode='r', dtype=groupdtype)