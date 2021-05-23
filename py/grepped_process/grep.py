#!/usr/bin/env python
import os
import subprocess
import time


utf8 = 'UTF-8'


def RunCommand(command):
    executed_command = subprocess.Popen(command, shell=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        output, errors = executed_command.communicate(timeout=3)
    except subprocess.TimeoutExpired:
        executed_command.kill()
        output, errors = executed_command.communicate()
    except OSError as error:
        print(f'There was an issue with running the command.\n{error}')

    # the command should stop after the try/except block
    check_finish = executed_command.poll()
    return_code = executed_command.returncode
    print(f'Finished status: {check_finish}\nReturn code: {return_code}')

    return output, errors


listed_command = "dmesg --help"
string_command = "ls -la"

print(RunCommand(listed_command))
# print(RunCommand(string_command)[0].decode(utf8))
