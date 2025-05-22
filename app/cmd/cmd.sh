#! /bin/bash

DIR="$(realpath "$(dirname "$0")/../")"

CMD=$1
shift 1

if [[ $CMD == "conf" ]]; then
    env "DIR=$DIR" $DIR/cmd/lib/$CMD.sh "$@"
    exit
fi

CHECK=$(env "DIR=$DIR" $DIR/cmd/lib/conf.sh check)
if [[ $CHECK == 0 ]]; then
    echo "You need configure first!"
    exit
fi

CONF=$(cat $DIR/etc/local)
ENV="$(cat $CONF | xargs) DIR=$DIR"
source $CONF

if ! [ -f $DIR/cmd/lib/$CMD.sh ]; then
    echo "command not found"
    exit
fi

env $ENV $DIR/cmd/lib/$CMD.sh "$@"