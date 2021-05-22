#!/usr/bin/env python
import time
import sys

execution_time = int(sys.argv[1])

run = True
x = 1
start_time = time.time()
while(run):
    x = x+1
    print(x, x+1)
    time.sleep(1)
    if(time.time()-start_time >= execution_time):
        run = False
        break
