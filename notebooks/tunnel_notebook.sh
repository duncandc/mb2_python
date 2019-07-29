#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source $DIR/credentials.sh
printf "username: %s \n" $UserName
printf "remote host: %s \n" $HostName
printf "port: %s \n" $NotebookPort

ssh -L $NotebookPort:localhost:$NotebookPort -t $UserName@$HostName "jupyter notebook"
