"""
File I/O related to the gadget snapshot MBII files
"""

import sys
import numpy as np
import pygadgetreader as pyg
from readgadget.modules import header as pyg_header
from readgadget.modules.common import pollOptions, initUnits, gadgetPrinter
from readgadget.modules import gadget1, gadget2
from mb2_python.data import BLOCKORDERING, pNames


__all__ = ['snapPath', 'snapHeader', 'getNumPart']
__author__ = ['Duncan Campbell']


def snapPath(basePath, snapNum, chunkNum=None):
    """
    Return absolute path to a snapshot file
    """
    if chunkNum is None:
        chunkNum = 0

    snapPath = basePath + '/snapdir'
    snapPath += '/snapdir_' + str(snapNum).zfill(3) + '/'
    filePath = snapPath + 'snapshot_' + str(snapNum).zfill(3)
    filePath += '.' + str(chunkNum)
    return filePath


def snapHeader(basePath, snapNum, chunkNum=None):
    """
    Return snapshot header

    Notes
    -----
    The Gadget snapshot files for MBII use a custom block ordering.
    This block ordering is defined in ``mb2_python.data.py``.
    In order to use the pygadgetreader module,
    the block ordering attribute of the header object is replaced.
    """

    if chunkNum is None:
        chunkNum = 0

    fname = snapPath(basePath, snapNum, chunkNum)
    header = pyg.readheader(fname, 'header')
    header.BLOCKORDER = BLOCKORDERING['CMU']
    return header


def getNumPart(header):
    """
    Calculate number of particles of all types given a snapshot header.
    """
    nTypes = 6

    nPart = np.zeros(nTypes, dtype=np.int64)
    for j in range(nTypes):
        nPart[j] = header['npartTotal'][j]

    return nPart


def readSnap(basePath, snapNum, partType, fields=None, chunkNum=None, **kwargs):
    """
    Load a subset of fields for all particles/cells of a given partType.
    """
    snap = snapPath(basePath, snapNum, chunkNum=None)
    h = pyg_header.Header(snap, 0)
    h.BLOCKORDER = BLOCKORDERING['CMU']

    d, p = pollOptions(h, kwargs, fields, partType)
    h.reading = d

    f = h.f
    initUnits(h)

    for i in range(0, h.nfiles):
        if i > 0:
            h = pyg_header.Header(snap, i, kwargs)
            f = h.f
            h.reading = d
            initUnits(h)

        if h.npartThisFile[p] == 0:
            if h.nfiles > 1:
                continue
            print('no %s particles present!' % pNames[p])
            sys.exit()

        elif h.fileType == 'gadget1':
            arr = gadget1.gadget_read(f, h, p, d)
        elif h.fileType == 'gadget2':
            arr = gadget2.gadget_type2_read(f, h, p)

        f.close()

        # return nth value
        if h.nth > 1:
            arr = arr[0::h.nth]

        # put arrays together
        if i == 0:
            return_arr = arr
            gadgetPrinter(h, d, p)
            if h.nth > 1 and not h.suppress:
                print('selecting every %d particles' % h.nth)
        elif i > 0:
            if len(arr) > 0:
                return_arr = np.concatenate((return_arr, arr))

        # if requesting a single file, break out of loop
        if h.singleFile:
            break

    if h.double and h.reading != 'pid' and h.reading != 'ParticleIDs':
        return_arr = return_arr.astype(np.float64)

    return return_arr




