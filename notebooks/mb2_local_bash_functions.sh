#!/bin/bash

# load username and remote location
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/credentials.sh
printf "username: %s \n" $UserName
printf "remote host: %s \n" $HostName

function jptnode(){
    ssh -t -t $UserName@$HostName -L $1:localhost:$1 ssh $2 -L $1:localhost:$1
}
