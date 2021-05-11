#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import psutil


process_list = 'plist.dat'

# Iterate over all running process
with open(process_list, 'w+') as writer:
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            # print(processName, ' ::: ', processID)
            writer.write(f'{str(processName).lower()} ::: {processID}\n')
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print('Works!')
