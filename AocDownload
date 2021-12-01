#!/bin/bash
echo "Year?"
read year

echo "Day?"
read day

if [ ! -d "$year/day$day" ]; then
    mkdir "$year/day$day"
fi

if [ -f "$year/day$day/input.txt" ]; then
    echo "Input already exists"
    exit 1
fi

curl -H "cookie: session=$(cat ~/.aocrc)" https://adventofcode.com/$year/day/$day/input -o $year/day$day/input.txt
