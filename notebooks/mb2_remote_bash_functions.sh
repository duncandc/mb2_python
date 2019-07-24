
UserName="duncanc"
HostName="coma.hpc1.cs.cmu.edu"

export XDG_RUNTIME_DIR=""

function jpt(){
    jupyter notebook --no-browser --port=$1
}

function jptnode(){
    ssh -t -t $UserName@$HostName -L $1:localhost:$1 ssh $2 -L $1:localhost:$1
}

