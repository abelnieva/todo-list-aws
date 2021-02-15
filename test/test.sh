#!/bin/sh
echo "test Repors"
coverage run -m TestToDo
coverage report -m
echo "Flake tests"
flake8 . --count
echo "Bandit"
bandit -r .
echo "Radon"
radon cc . 

echo "Press CTRL+C to exit"