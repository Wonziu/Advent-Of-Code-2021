#! /bin/bash

template=$'filename = \"input.txt\"\n\nif __name__ == \'__main__\':\n    with open(filename) as file:'

path="$PWD/Day_$1"

if [ ! -d $path ]; then
    mkdir -p $path;
    cd $path
    touch main.py
    touch input.txt
    echo "$template" > main.py
fi