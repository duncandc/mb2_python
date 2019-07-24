

tmux new -s jupyter
srun -p main --time=02:00:00 --ntasks-per-node 2 --pty bash

source ~/.bash_profile
source ./.bash_mb2_profile

conda create conda-env
source activate conda-env

jpt 8888
