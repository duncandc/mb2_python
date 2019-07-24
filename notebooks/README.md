# Notebooks

This directy contains [Jupyter](https://jupyter.org) notebook tutorials, demonstrating some uses of `mb2_python`.  


## Running Notebooks Remotely

Given the size of the data associated with MBII, it is most likely not feasable to run your analysis on your local machine.  However, it is very useful to be able to run Jupyter notebooks to facilitate quick prototyping of analysis and data exploration.  

Here we provide a set of instructions and tools to run Jupyter notebooks remotely on the [Coma](http://coma.pbworks.com) cluster at Carnegie Mellon University.  For these instructions, I have closely followed the tutorial on the Alexander Lab [website](https://alexanderlabwhoi.github.io/post/2019-03-08_jpn-slurm/).


### On Coma

First, you will need the `mb2_python` module installed on Coma.  One way to accomplkish this is to simply clone the `mb2_python` repo in your home directoy on Coma.  Regardless, note the locaion of your `mb2_python` installation, `[PATH_TO_MB2_PYTHON]`.

In order to prevent your session timing out you can use the `tmux` program:

```
tmux new -s jupyter
```

You can submit a job using the slurm `srun` command.  As an example, here I ask for 2 hours, running on two CPUs, using the `physics` queue.  Note that you can/should customize this to your needs and the resources to which you have access.  

```
srun -p physics --time=02:00:00 --ntasks-per-node 2 --pty bash
```

When this job executes, you will be logged onto some node which will be noted in your command prompt.  At this point, you may want to source your bash startup script, e.g. `source ~/.bash_profile`.  You can access a bunch of useful bash commands by executing the following command: 

```
source [PATH_TO_MB2_PYTHON]/mb2_remote_bash_functions.sh
```
 
You can create a conda environment by executing the following commands:

```
conda create conda-env
source activate conda-env
```

Using one of the commands in `/mb2_remote_bash_functions.sh`, you can start a Jupyter notebook:

```
jpt 8888
```

Note that `8888` here is the port you have selected.


### On Your Local Machine

You will also need `mb2_python` installed on your local machine, again noting the installation directoy, `[PATH_TO_MB2_PYTHON]`.  You should modify the username variable in the `credentials.sh` file in this directory to your username for the Coma Cluster.  Now, on your local machine you can access some bash functions by executing the following command: 

```
source [PATH_TO_MB2_PYTHON]/mb2_local_bash_functions.sh
```


### When You're Done

Make sure that after you are done you close your notebook on Coma.  After looging back onto Coma, log back into the tmux session you started earlier:

```
tmux a -t jupyter
``` 

Use `ctrl-C` to shutdown the Jupyter notebook.

	