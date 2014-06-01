#!/bin/bash

export LANG=en_US.UTF-8

# find script dir
pushd $(dirname $0) >/dev/null
SCRIPT_DIR=$(pwd -P)
popd >/dev/null

REPOS="$1"
TXN="$2"

HOOKS_PATH=${SCRIPT_DIR}
SVNLOOK=$(which svnlook)
PYTHON=$(which python)
SVNCHECKER=${HOOKS_PATH}/svnchecker/main.py

cd $HOOKS_PATH
msg=`$PYTHON $SVNCHECKER $REPOS $TXN 2>&1` && code=$? || code=$?
echo $msg 1>&2
exit $code


