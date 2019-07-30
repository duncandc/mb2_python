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

This package contains functions to load and manipulate both processed object catalogs and the raw particle data associated witht the MassiveBlack-II simulation.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
    - [readSnap](#readSnap)
    - [readgc]()
    - [readsgc]()
    - [readGroup](#loadGroup)
    - [readSubhalo](#loadSubhalo)
4. [Data](#data)
    - [Snapshots]()
    - [Subhaloes]()
    - [Directory Structure]()


## Requirements <a name="requirements"></a>

In order to use the functions in this package, you will need the following Python packages installed:

* [numpy](http://www.numpy.org)
* [pygadgetreader](https://bitbucket.org/rthompson/pygadgetreader/src/default/)


## Installation <a name="installation"></a>

Place this directory in your PYTHONPATH.  The various functions can then be imported as, e.g.:

```
from mb2_python import load_subhalo
```

## Usage <a name="usage"></a>

Here I give a simple description of the major functions available in this module.  For a more detailed decription the functions, please refer to the doc strings.


### readSnap() <a name="readSnap"></a>

This function reads particle data from the snapshot files chunk by chunk.  You can read in for all chunks at once, but beware, this is slow.

```
from mb2_python load readSnap
from mb2_python.data import basePath_default as basePath

# load DM particle positions and velocities at redshift 0 for one data chunk
result = readSnap(basePath, 85, 1, fields=['pos','vel'], chunkNum=0)
```

### loadGroup() <a name="loadGroup"></a>

This function reads particle data for a given host halo, or for for multiple host haloes (ordered by host halo).

```
from mb2_python load loadHalo
from mb2_python.data import basePath_default as basePath

# load DM particle positions and velocities at redshift 0 for host halo ID=0
result = loadHalo(basePath, 85, 1, fields=['pos','vel'], ids=[0])
```

### loadSubhalo() <a name="loadSubhalo"></a>

This function reads particle data for a given subhalo, or for for multiple subhaloes (ordered by subhalo).

```
from mb2_python load loadSubhalo
from mb2_python.data import basePath_default as basePath

# load DM particle positions and velocities at redshift 0 for subhalo ID=0
result = loadSubhalo(basePath, 85, 1, fields=['pos','vel'], ids=[0])
```



## Data <a name="data"></a>

MBII data products are stored on the [Coma](http://coma.pbworks.com) cluster at Carnegie Mellon University.  The Coma cluster is only accessible to researchers in the [McWilliams Center](https://www.cmu.edu/cosmology/) at CMU.
  

### Snapshots <a name="snapshots"></a>

The raw MBII data was written to disk at 85 points throughout its evolution.  These points in its evolution are referred to as "snapshots".  An individual snapshot is indexed using `[snapNum]`.  

For each of these 85 snapshots, the data was split into 1024 "chunks" to make the size of each file more managable.  These chunks are indexed using `[chunkNum]`.  

The files are saved in the Gadget-1 binary [format](https://wwwmpa.mpa-garching.mpg.de/gadget/users-guide.pdf).  The MBII snapshot filenames have the form: `snapshot_[snapNum].[chunkNum]`.

Snapshot data can be accessed using the `snapshot` module.


### Subhaloes <a name="subhaloes"></a>

A subset of particle data has be reformated according its host (sub-)halo.  Particles not identified to be part of a host halo are not present in this data.  

This data can be accesed using the `subhalos` module. 


### Directory Structure <a name="directory_structure"></a>

This module assumes the MBII data is stored in a particular directory heirarchy.  There are two primary subdirectories within the `[basePath]`, `snapdir` and `subhalos`.  

The `snapdir` directory stores raw the simulation output.  It is split into subdirectories by snapshot, e.g. `snapdir_085` corresponds to the last snapshot of the simulation.

The `subhalos` directory is split into subdirectories by snapshot, e.g. `085` corresponds to the last snapshot of the simulation.  Within each snapshot directory, there are 5 subdirectotries, `0`, `1`, `2`, `3`, `4`, `5` corresponding to the the particle types.  Within each of these directories are header files and individual files that stores particle property arrays, e.g. `pos.raw` contains the particle positions.    


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
│   │   │   header.txt
│   │   │   id.raw
│   │   │   pos.raw
│   │   │   ...
│   │   │
│   │   └───1
│   │   │   header.txt
│   │   │   id.raw
│   │   │   pos.raw
│   │   │   ...
│   │   │
│   │   └───2
│   │   │   header.txt
│   │   │   id.raw
│   │   │   pos.raw
│   │   │   ...
│   │   │
│   │   └───3
│   │   │   header.txt
│   │   │   id.raw
│   │   │   pos.raw
│   │   │   ...
│   │   │
│   │   └───4
│   │   │   header.txt
│   │   │   id.raw
│   │   │   pos.raw
│   │   │   ...
│   │   │
│   │   └───5
│   │   │   header.txt
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