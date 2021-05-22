#!/usr/bin/env bash
iterations="$1"
processName="python"
ls_com="ls"
runtime="nohup python runit.py &>/dev/null &" 
direct_runtime="python runit.py &>/dev/null &"

echo "Will spawn $cmd $processName instances"
for ((c=1; c<=$iterations;c++))
do
nohup ./runit.py &>/dev/null &
done
