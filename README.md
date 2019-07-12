# MassiveBlack-II Python

This package contains functions to aid in calculations with [MassiveBlack-II](https://arxiv.org/abs/1402.0888) simulation data products.  

Inspired by the [illustris_python](https://bitbucket.org/illustris/illustris_python/src/default/) package, this repository represents my effort to collect, organize, and tidy-up the work of many different researchers who have created and used MBII data products.  An incomplete list includes:

* [Yu Feng](http://rainwoodman.github.io/website/)
* Ananth Tennetti
* Aklant Bhowmick
* Hung-Jin Huang
* Simon Samuroff
* Francois Lanusse

To the best of my ability, I have tried to give credit within the code for the work of others.


## Description

This package contains functions that load:

* raw particle data
* group particle data
* subhalo particle data
* subhalo object catalog


## Requirements

In order to use the functions in this package, you will need the following Python packages installed:

* [numpy](http://www.numpy.org)
* [pygadgetreader](https://bitbucket.org/rthompson/pygadgetreader/src/default/)


## Installation

Place this directory in your PYTHONPATH.  The various functions can then be imported as, e.g.:

```
from mb2_python import load_subhalo
```


## Data

MBII data products are stored on the [Coma](http://coma.pbworks.com) cluster at Carnegie Mellon University.  The Coma cluster is only accessible to researchers in the [McWilliams Center](https://www.cmu.edu/cosmology/) at CMU.
  

### Snapshots

The raw MBII data was written to disk at 85 points throughout its evolution.  These points in its evolution are referred to as "snapshots".  An individual snapshot is indexed using `[snapNum]`.  

For each of these 85 snapshots, the data was split into 1024 "chunks" to make the size of each file more managable.  These chunks are indexed using `[chunkNum]`.  

The files are saved in the Gadget-1 binary [format](https://wwwmpa.mpa-garching.mpg.de/gadget/users-guide.pdf).  The MBII snapshot filenames have the form: `snapshot_[snapNum].[chunkNum]`.


### Subhaloes



### Directory Structure

This module assumes the MBII data is stored in a particular directory heirarchy. 


```
basePath 
└───snapdir
│   └───snapdir_001
│   │   snapshot_001.0
│   │   snapshot_001.1
│   │   ...
│   │
│   └───snapdir_002
│   │   snapshot_002.0
│   │   snapshot_002.1
│   │   ...
│   │
│   └───...
│
└───subhalos
│   └───0
│   │   └───0
│   │   │   id.raw
│   │   │   pos.raw
│   │   │   ...
│   │   │
│   │   └───1
│   │   │   id.raw
│   │   │   pos.raw
│   │   │   ...
│   │   │
│   │   └───2
│   │   │   id.raw
│   │   │   pos.raw
│   │   │   ...
│   │   │
│   │   └───3
│   │   │   id.raw
│   │   │   pos.raw
│   │   │   ...
│   │   │
│   │   └───4
│   │   │   id.raw
│   │   │   pos.raw
│   │   │   ...
│   │   │
│   │   └───5
│   │   │   id.raw
│   │   │   pos.raw
│   │   │   ...
│   │   │
│   └───1
│   │   └───...
│   │ 
│   └───...
│
│
```	

contact:
duncanc@andrew.cmu.edu