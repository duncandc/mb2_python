# MassiveBlack-II Python

This package contains functions to aid in calculations with [MassiveBlack-II](https://arxiv.org/abs/1402.0888) simulation data products.  

Inspired by the [illustris_python](https://bitbucket.org/illustris/illustris_python/src/default/) package, this repository represents my effort to collect, organize, and tidy-up the work of many different researchers who have created and used MBII data products.  An incomplete list includes:

* [Yu Feng](http://rainwoodman.github.io/website/)
* Ananth Tennetti
* Aklant Bhowmick
* [Hung-Jin Huang](https://github.com/hungjinh)
* [Simon Samuroff](https://github.com/ssamuroff)
* [Francois Lanusse](https://github.com/EiffL)

To the best of my ability, I have tried to give credit within the code for the work of others.


## Description

This package contains functions to load and manipulate both processed object catalogs and the raw particle data associated witht the MassiveBlack-II simulation.

In the parlance of this module, "group" refers to objects identified by an FoF halo finder.  Given this, "group" could be interpreted as "host halo".  On the other hand, "subhalo" refers to objects identified using the subfind algorithm run on particles identified to be parts of groups.  In this sense, these objects match up closely to what is meant by the term <em>subhalo</em> in the halo model.  However, it should be noted that the bulk of material that would gnerally be identified as belonging to the host halo (and not any substructure) is most often identified as belonging to a massive "subhalo".


## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
    - [readSnap](#readSnap)
    - [readgc](#readgc)
    - [readshc](#readshc)
    - [loadGroup](#loadGroup)
    - [loadSubhalo](#loadSubhalo)
4. [Simulation](#simulation)
5. [Data](#data)
    - [Snapshots](#snapshots)
    - [Subhaloes](#subhaloes)
    - [Directory Structure](#directory_structure)


## Requirements <a name="requirements"></a>

In order to use the functions in this package, you will need the following Python packages installed:

* [numpy](http://www.numpy.org)
* [pygadgetreader](https://bitbucket.org/rthompson/pygadgetreader/src/default/)


## Installation <a name="installation"></a>

Place this directory in your PYTHONPATH.  The various functions can then be imported as, e.g.:

```
from mb2_python import loadSubhalo
```

## Usage <a name="usage"></a>

Here I give a simple description of the major functions available in this module.  For a more detailed decription the functions, please refer to the associated doc strings.

There are also some tutorials demonstrating some basic tasks in the [notebooks](https://github.com/duncandc/mb2_python/tree/master/notebooks) directory.


### readSnap() <a name="readSnap"></a>

This function reads particle data from the snapshot files chunk by chunk.  You can read in for all chunks at once, but beware, this is slow.

```
from mb2_python load readSnap
from mb2_python.data import basePath_default as basePath

# load DM particle positions and velocities at redshift 0 for one data chunk
result = readSnap(basePath, 85, 1, fields=['pos','vel'], chunkNum=0)
```

### readgc() <a name="readgc"></a>

This function reads the basic group (i.e. host haloes) catalog.

```
from mb2_python load readgc
from mb2_python.data import basePath_default as basePath

# load group catalog for redshift 0
groupcat = readgc(basePath, 85)
```


### readshc() <a name="readshc"></a>

This function reads the basic subhalo catalog.

```
from mb2_python load readshc
from mb2_python.data import basePath_default as basePath

# load subhalo catalog for redshift 0
subhalocat = readshc(basePath, 85)
```


### loadGroup() <a name="loadGroup"></a>

This function reads particle data for a given host halo, or for multiple host haloes (ordered by host halo).

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

This module assumes the MBII data is stored in a particular directory heirarchy.  There are two primary subdirectories within the `[basePath]`, `snapdir` and `subhalos`.  Note that on the Coma cluster, the you may import the default `[basePath]` from mb2_python.data as:

```
from mb2_python.data import basePath_default as basePath
print(basePath)

>>> /physics/yfeng1/mb2
```   

Wthin the `[basePath]` diurectory, the `snapdir` directory stores the raw simulation output.  This data is split into subdirectories by snapshot number, e.g. `snapdir_085` corresponds to the last snapshot of the simulation.

The `subhalos` directory is split into subdirectories by snapshot, e.g. `085` corresponds to the last snapshot of the simulation.  Within each snapshot directory, there are 5 subdirectories, `0`, `1`, `2`, `3`, `4`, `5` corresponding to the particle types.  Within each of these directories are header files and individual files that store particle property arrays, e.g. `pos.raw` contains the particle positions.    


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