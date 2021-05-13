#!/usr/bin/env python
import psutil as ps
import sys
import re

process_file = 'plist.dat'

with open(process_file, 'r+') as procs:
    processes = procs.readlines()


def Check_Process_Exists(process_name, process_list):
    all_procs = []
    for proc in process_list:
        current_proc = proc.strip()
        if(process_name in current_proc):
            all_procs.append(current_proc)
    print(f'Found {process_name} in {len(all_procs)} instances')
    if(len(all_procs)):
        return 1
    return 0


def Create_Process_Registry(process_name, process_list):
    all_procs = []
    return all_procs


try:
    proc_name = sys.argv[1]
except IndexError as error:
    proc_name = 'brave'
# else:
#     proc_name = 'brave'

Check_Process_Exists(proc_name, processes)
