#!/usr/bin/env python
import subprocess
import sys
import os


to_utf8 = lambda x: x.decode('UTF-8')


def Get_Command_Output(command):
    os.environ['PYTHONUNBUFFERED'] = "1"
    proc = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            )
    stdout, stderr = proc.communicate()
    stdout = to_utf8(stdout)
    stderr = to_utf8(stderr)
    return stdout, stderr


def run(cmd):
    os.environ['PYTHONUNBUFFERED'] = "1"
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            )
    stdout, stderr = proc.communicate()

    return proc.returncode, stdout.decode('UTF-8'), stderr


print(run(['ls']))

ls = subprocess.run(['ps', 'aux'], capture_output=True,
                    text=True).stdout.strip("\n")
