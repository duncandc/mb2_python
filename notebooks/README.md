# Notebooks

This directy contains [Jupyter](https://jupyter.org) notebook tutorials, demonstrating some uses of `mb2_python`.  


## Running Notebooks Remotely

Given the size of the data associated with MBII, it is most likely not feasable to run an analysis on your local machine.  However, it is very useful to be able to run Jupyter notebooks to facilitate quick prototyping of analysis and data exploration.  

Here we provide a set of instructions and tools to run Jupyter notebooks remotely on the [Coma](http://coma.pbworks.com) cluster at Carnegie Mellon University.  For these instructions, I have closely followed the tutorial on the Alexander Lab [website](https://alexanderlabwhoi.github.io/post/2019-03-08_jpn-slurm/).


### Preperation

There a couple steps you will only need to preform once.

First, you will need the `mb2_python` module installed on Coma.  One way to accomplish this is to simply clone the `mb2_python` repository into your home directory.  Regardless, note the locaion of your `mb2_python` installation on the cluster, `[PATH_TO_MB2_PYTHON]`.

You should also set a password for accessing Jupyter notebooks (more about this [here](https://jupyter-notebook.readthedocs.io/en/stable/security.html)).  In your home directory, navigate to `~/.jupyter` and execute the following command to set a password:

```
jupyter notebook password
```

You will also need `mb2_python` installed on your local machine, again noting the installation directory.  You should modify the username variable in the `credentials.sh` file in this directory to your username for logging onto the Coma Cluster.

That's it!  You are now ready to start an interactive notebook on the cluster.


### On the Coma Cluster

To run a remote notebook, log onto the cluster.  In order to prevent your session timing out you can use the `screen` program:

```
screen -S jupyter
```

Next, you can submit a job using the slurm `srun` command.  As an example, here I am using the `short` queue.  Note that you can/should customize this to your needs and the resources to which you have access.  

```
srun --pty -p short --nodes 1 --ntasks-per-node 8 bash
```

```
salloc --partition=long --ntasks=8 -t 24:00:00
``

When this job executes, you will be logged onto a node which will be in your command line prompt.  On Coma, node names look something like `compute-2-40`.  At this point, you may want to source your bash startup script, e.g. `source ~/.bash_profile`.  In addition, you can access some useful bash commands by executing the following: 

```
source [PATH_TO_MB2_PYTHON]/notebooks/mb2_remote_bash_functions.sh
```
 
If you want to run the notebooks in this directory, you need to navigate to this tutorial directory.

```
cd [PATH_TO_MB2_PYTHON]/notebooks
```

Using one of the commands sourced earlier, you can start a Jupyter notebook:

```
jpt 8888
```

Note that `8888` here is the port you have selected.  You can change this if desired.


### On Your Local Machine

Now, on your local machine you can access some bash functions by executing the following command: 

```
source [PATH_TO_MB2_PYTHON]/notebooks/mb2_local_bash_functions.sh
```

To create the tunnel, you then execute the following command:

```
jptnode 8888 [COMPUTE_NODE]
```

Make sure to use the correct node name, e.g. `compute-2-40`.

Now, you can open your browser of choice, navigate to go to `localhost:8888`, enter your Jupyter notbook password created earlier, and you should see a Jupyter dashboard.  You are then free to select a tutorial notebook or to create a new one.


### When You're Done

Make sure that after you are done you close your notebook on Coma.  After looging back onto Coma, log back into the screen session you started earlier:

```
screen -r jupyter
``` 

Use `ctrl-C` to shutdown the Jupyter notebook.

	