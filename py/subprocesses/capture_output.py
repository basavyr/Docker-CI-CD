#!/usr/bin/env python
import subprocess
import sys
import os


def run(cmd):
    os.environ['PYTHONUNBUFFERED'] = "1"
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            )
    stdout, stderr = proc.communicate()

    return proc.returncode, stdout.decode('UTF-8'), stderr


code, out, err = run(['ls'])


print(f'out --> \n{out}')
# print("err: '{}'".format(err))
# print("exit: {}".format(code))

ls = subprocess.run(['ls', '-la'], capture_output=True,
                    text=True).stdout.strip("\n")
