#!/bin/sh

mkdir -p test/output

echo "Flake apps"
flake8 ./todos --count
echo "Bandit"
bandit -r ./todos --exit-zero --format txt --output test/output/bandit.txt
cat output/bandit.txt
grep -il 'No issues identified' ./test/output/bandit.txt || echo 'Bandit: failed!'
echo "Radon"
radon cc . 

echo "test Repors"
cd test/
coverage run    -m TestToDo 
coverage html --fail-under=50  -d output

echo "Press CTRL+C to exit"