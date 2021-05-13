#!/usr/bin/env python
import psutil as ps
import re

process_file = 'plist.dat'

with open(process_file, 'r+') as procs:
    processes = procs.readlines()


for proc in processes:
    x = proc.strip()
    if("brave" in x):
        print(x)
