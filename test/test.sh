#!/bin/sh
mkdir -p output
echo "test Repors"
coverage run -m TestToDo 
coverage xml -o output/coverage.xml
ls -l 
echo "Flake tests"
#flake8 . --count
echo "Bandit"
#bandit -r .
echo "Radon"
#radon cc . 

echo "Press CTRL+C to exit"