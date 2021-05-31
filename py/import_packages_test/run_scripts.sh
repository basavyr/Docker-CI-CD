#!/usr/bin/env bash

echo 'Running the main test...'
sleep 1
python test_scripts.py
echo 
echo 'Running the test components for <<module1>>...'
sleep 1
cd tests
python test_module1.py