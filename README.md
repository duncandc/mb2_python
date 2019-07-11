# MassiveBlack-II Python

This package contains functions to aid in calculations with [MassiveBlack-II](https://arxiv.org/abs/1402.0888) data products.


## Description

This package contains functions that load:

* group particle data
* subhalo particle data


## Requirements

In order to use the functions in this package, you will need the following Python packages installed:

* [numpy](http://www.numpy.org)
* [astropy](http://www.astropy.org)
* [pygadgetreader](https://bitbucket.org/rthompson/pygadgetreader/src/default/)


## Installation

Place this directory in your PYTHONPATH.  The various functions can then be imported as, e.g.:

```
from mb2_python import load_subhalo
```


## Data

### Snapshots

The raw MBII data was written to disk at 85 points throughout its evolution.  These points in its evolution are referred to as "snapshots", while an individual snapshot is indexed using a snap number, i.e. snapNum.  For each of these 85 snapshots, the data was split into 1024 chunks to make the size of each file more managable.  These chunks are indexed using a chunk number, i.e. chunkNum.  The files are saved in the Gadget-2 binary format.  Snapshot filenames have the form: `snapshot_[snapNum].[chunkNum]`.


### Subhaloes



### Direcotry Structure

This module assumes the MBII data is stored in a particular directory heirarchy. This heirarchy is reproduced below.


```
basePath 
└───snapdir
│   └───snapdir_001
│   │   snapshot_001.0
│   │   snapshot_001.1
│   │   ...
│
│   └───snapdir_002
│   │   snapshot_001.0
│   │   snapshot_001.1
│   │   ...
│
└───...
│
└───subhalos
│   └───0
│   │   └───0
│   │   |   id.raw
│   │   |   pos.raw
│   │   |   ...
│   │   └───1
│   │   |   id.raw
│   │   |   pos.raw
│   │   |   ...
│   │   └───2
│   │   |   id.raw
│   │   |   pos.raw
│   │   |   ...
│   │   └───3
│   │   |   id.raw
│   │   |   pos.raw
│   │   |   ...
│   │   └───4
│   │   |   id.raw
│   │   |   pos.raw
│   │   |   ...
│   │   └───5
│   │   |   id.raw
│   │   |   pos.raw
│   │   |   ...
│   └───1
│   └───...
```	