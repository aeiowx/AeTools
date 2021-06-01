#! /bin/bash

path=$1

if [ -z $path ]
then
    echo "please enter correct scan path."
    exit
fi

for file in $(find $path -type l)
do
    if [ ! -e $file ]
    then
        echo "rm $file"
        rm -f $file
    fi
done
