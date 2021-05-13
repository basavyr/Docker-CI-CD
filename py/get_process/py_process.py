#!/usr/bin/env python
import psutil

# save the processes to a file for later usage
process_list = 'plist.dat'


def Check_Process_Exists(process_name):
    # this method will look for any process with the given name within the system
    # proc_state = False
    for proc in psutil.process_iter():
        try:
            proc_name = str(proc.name()).lower()
            proc_id = proc.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        if(proc_name == process_name):
            print(
                f'Found 1 process with name{process_name}: {proc_name}:::{proc_id}')
            # proc_state=True
        else:
            pass


def Create_Process_List(process_list):
    with open(process_list, 'w+') as writer:
        for proc in psutil.process_iter():
            try:
                processName = str(proc.name()).lower()
                processID = proc.pid
                writer.write(f'{processName}:::{processID}\n')
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass


Create_Process_List(process_list)

# Iterate over all running process
# with open(process_list, 'w+') as writer:
#   for proc in psutil.process_iter():
#      try:
# Get process name & pid from process object.
#         processName = proc.name()
#        processID = proc.pid
# print(processName, ' ::: ', processID)
#       writer.write(f'{str(processName).lower()} ::: {processID}\n')
#   except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#      pass
# print('Works!')
# Check_Process_Exists('python')
