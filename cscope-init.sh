#!/usr/bin/bash

#this is broken right now, trying to be too fancy
#http://cscope.sourceforge.net/large_projects.html

if [ $# -lt 1 ]
then  
    echo "usage: cscope-init <source dir>"
    exit 1
fi

if [ ! -e $1 ] ; then
    echo "$1 doesn't exist: enter an existing source directory."
    exit 1
fi

pushd $1 &>/dev/null
find ./ -name "*.c" -o -name "*.h" -o -name "*.py" -o \
    -name "*.sh" -o -name "*.in" -o -name "*.am" -o \
    -name "*.l" -o -name "*.y" -o -name "*.java" \
    -o -name "*.pm" -o -name "*.t" > cscope.files
 
cscope -q -R -b -i cscope.files

echo "new cscope database is located in $1/cscope.out"
 
popd &>/dev/null
