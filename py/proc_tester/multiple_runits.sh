#!/usr/bin/env bash
iterations="$1" #number of python scripts that will be spawned simultaneously

processName="python"
runtime="nohup python runit.py &>/dev/null &" 
direct_runtime="nohup ./runit.py &>/dev/null &"

echo "Will spawn $cmd $processName instances"
for ((c=1; c<=$iterations;c++))
do
nohup ./runit.py 10 &>/dev/null & #if the execution of the python script is called via the variables with $, the script waits for every script instance to finish
done
