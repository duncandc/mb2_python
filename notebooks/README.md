# Notebooks

This directy contains [Jupyter](https://jupyter.org) notebook tutorials, demonstrating some uses of `mb2_python`.  


## Running Notebooks Remotely

Given the size of the data associated with MBII, it is most likely not feasable to run an analysis on your local machine.  However, it is very useful to be able to run Jupyter notebooks to facilitate quick prototyping of analyses and for data exploration.  

[Here](https://github.com/McWilliamsCenter/slurm_jupyter) ar some instructions to run Jupyter notebooks remotely on the [Coma](http://coma.pbworks.com) cluster at Carnegie Mellon University.  

We also provide some convenience scripts that may help:`jupyter.job` which can be used to submit an interactive Jupyter notebook job on the Coma cluster, and `tunnel_notebook.sh` which can be used to access a notebook running on the Coma cluster on your local machine.

To use these scripts, you should modify `credentials.py` with your information. Correspondingly, you should change the output files and the `NotebookPort` variable in the `jupyter.job` script.  

Once set up, you can submit a job to run an interactive Jupyter notebook by executing:

```console
user@local:~$ sbatch jupyter.job
``` 

You can check on the status of your job with the following command:

```console
user@local:~$ squeue -u [USERNAME]
```

You can access the notebook on your local machine by executing the following command:

```
user$ ./tunnel_notebook [NODE_NAME]
```

Simply replace `[NODE_NAME]` with the name of the node that the job is running on.


When you are done, do not forget to kill your job:

```console
user@local:~$ scancel [JOB_ID]
```





	