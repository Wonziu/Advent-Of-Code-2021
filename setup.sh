#! /bin/bash
path="$PWD/Day_$1"

template="filename = \"$path/input.txt\"

if __name__ == '__main__':
    with open(filename) as file:"


if [ ! -d $path ]; then
    mkdir -p $path;
    cd $path
    touch main.py
    touch input.txt
    echo "$template" > main.py
fi