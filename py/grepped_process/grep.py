#!/usr/bin/env python
import os
import subprocess
import time


utf8 = 'UTF-8'


def RunCommand(command):
    executed_command = subprocess.Popen(command, shell=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output, errors = executed_command.communicate(timeout=10)
    except subprocess.TimeoutExpired:
        executed_command.kill()
        output, errors = executed_command.communicate()
    return output, errors


command = "ls -la"

print(RunCommand(command)[0].decode(utf8))
