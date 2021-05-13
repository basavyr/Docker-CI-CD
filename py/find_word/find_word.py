#!/usr/bin/env python
import psutil as ps
import re

story = 'logstash --logstash-process'

proc_name = 'logstash'

match = re.search('logs', story.lower())
match_2 = re.findall('logst', story.lower())

print(match.group(0))
print(match_2)

process_file = 'plist.dat'

with open(process_file, 'r+') as procs:
    processes = procs.readlines()


for proc in processes:
    if(re.search('bash', proc.lower())):
        print('found bash in proc list')


if(len(match_2) > 0):
    print(f'The process {proc_name} has been found running')
else:
    print(f'{proc_name} is not a running process')


def FindProcess(process_list, process_name):
    # searches for a process within a list
    return 1
