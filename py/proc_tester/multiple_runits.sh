#!/usr/bin/env bash
iterations="$1"
processName="python"

echo "Will spawn $cmd $processName instances"
for ((c=1; c<=$iterations;c++))
do
echo "$c"
done
